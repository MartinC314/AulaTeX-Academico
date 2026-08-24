"""Preparación segura y reproducible del corpus del motor inteligente AulaTeX.

Este módulo contiene la lógica reutilizable por notebooks y pruebas. No carga
credenciales ni publica datos. Los datasets reales se escriben bajo
``data/private`` y deben permanecer fuera de Git.
"""

from __future__ import annotations

import hashlib
import json
import platform
import random
import re
import sys
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable, Iterator, Sequence

SCHEMA_VERSION = "1.0"
MIN_DOCUMENT_CHARS = 400
EXCLUDED_PARTS = {
    ".git", ".venv", ".aulatex-temp", ".build", "base", "node_modules",
    "outputs", "models", "data", "retroalimentacion-editorial", "__pycache__",
}
NATIVE_IMAGE_COMMANDS = (r"\insertimage", r"\begin{images}", r"\addimage")

SYSTEM_PROMPT = """Eres el motor inteligente editorial de AulaTeX. Genera una actividad académica rigurosa en LaTeX basada únicamente en el contexto y las claves bibliográficas permitidas. Conserva la técnica didáctica y organiza el cuerpo visible en Introducción, una única sección temática de desarrollo y Conclusiones. El producto solicitado debe ser el núcleo del desarrollo. No inventes fuentes ni claves de cita. Cuando uses imágenes en documentos que cargan el template AulaTeX, utiliza \\insertimage o el entorno images con \\addimage; no uses figure/includegraphics manual."""

_SECRET_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("aws_access_key", re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b")),
    ("private_key", re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----")),
    ("bearer_token", re.compile(r"\bBearer\s+[A-Za-z0-9._~+/=-]{20,}", re.I)),
    ("generic_secret", re.compile(r"(?i)\b(?:api[_-]?key|secret|token|password)\s*[:=]\s*['\"]?[^\s'\"]{12,}")),
)
_PII_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("email", re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I)),
    ("phone", re.compile(r"(?<!\d)(?:\+?52[\s.-]?)?(?:\d[\s.-]?){10}(?!\d)")),
    ("student_id", re.compile(r"(?i)\b(?:matr[ií]cula|student[_ -]?id)\s*[:#-]?\s*[A-Z0-9-]{5,}")),
    ("windows_path", re.compile(r"\b[A-Z]:\\Users\\[^\\\s]+", re.I)),
)


@dataclass(frozen=True)
class PrivacyFinding:
    kind: str
    source: str
    count: int


@dataclass(frozen=True)
class CorpusManifest:
    schema_version: str
    seed: int
    counts: dict[str, int]
    hashes: dict[str, str]
    source_root: str
    privacy_findings: int


def repo_root(start: Path | None = None) -> Path:
    current = (start or Path.cwd()).resolve()
    if current.is_file():
        current = current.parent
    for candidate in (current, *current.parents):
        if (candidate / "scripts" / "aulatex").is_dir() and (candidate / "base").is_dir():
            return candidate
    return Path(__file__).resolve().parents[2]


def environment_report() -> dict[str, Any]:
    report: dict[str, Any] = {
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "executable": sys.executable,
        "cuda_available": False,
        "gpu_count": 0,
    }
    try:
        import torch

        report.update({"torch": torch.__version__, "cuda_available": torch.cuda.is_available()})
        if torch.cuda.is_available():
            report.update({
                "cuda": torch.version.cuda,
                "gpu_count": torch.cuda.device_count(),
                "gpus": [
                    {
                        "name": torch.cuda.get_device_name(index),
                        "vram_gib": round(torch.cuda.get_device_properties(index).total_memory / 2**30, 2),
                        "bf16": bool(torch.cuda.is_bf16_supported()),
                    }
                    for index in range(torch.cuda.device_count())
                ],
            })
    except ImportError:
        report["torch"] = None
    for package in ("transformers", "datasets", "peft", "trl", "bitsandbytes"):
        try:
            module = __import__(package)
            report[package] = getattr(module, "__version__", "instalado")
        except (ImportError, OSError):
            report[package] = None
    return report


def iter_activity_tex(root: Path) -> Iterator[Path]:
    for path in sorted(root.rglob("*.tex")):
        if EXCLUDED_PARTS.intersection(path.relative_to(root).parts):
            continue
        lowered = path.name.lower()
        if lowered.startswith(("reporte-", "presentacion-")) and "actividad-" in lowered:
            yield path


def inventory_sources(root: Path) -> dict[str, list[Path]]:
    def safe(pattern: str) -> list[Path]:
        return [
            path for path in sorted(root.rglob(pattern))
            if not EXCLUDED_PARTS.intersection(path.relative_to(root).parts)
        ]

    return {
        "activities": list(iter_activity_tex(root)),
        "programs": safe("programa-analitico-*.md"),
        "plans": [p for p in safe("*.md") if "planeacion" in p.as_posix().lower()],
        "extractor": [p for p in safe("*.json") if "extractor-aulatex" in p.as_posix()],
        "bibliographies": safe("*.bib"),
    }


def read_utf8(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def document_body(text: str) -> str:
    match = re.search(r"\\begin\{document\}", text)
    body = text[match.end():] if match else text
    body = re.sub(r"\\end\{document\}.*", "", body, flags=re.DOTALL)
    body = "\n".join(line for line in body.splitlines() if not line.lstrip().startswith("%"))
    return re.sub(r"\n{3,}", "\n\n", body).strip()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def privacy_findings(text: str, source: str = "") -> list[PrivacyFinding]:
    findings: list[PrivacyFinding] = []
    for kind, pattern in (*_SECRET_PATTERNS, *_PII_PATTERNS):
        count = len(pattern.findall(text))
        if count:
            findings.append(PrivacyFinding(kind=kind, source=source, count=count))
    return findings


def redact_text(text: str) -> tuple[str, list[PrivacyFinding]]:
    findings = privacy_findings(text)
    redacted = text
    for kind, pattern in (*_SECRET_PATTERNS, *_PII_PATTERNS):
        redacted = pattern.sub(f"[REDACTED_{kind.upper()}]", redacted)
    return redacted, findings


def extract_bib_keys(text: str) -> list[str]:
    keys: set[str] = set()
    for group in re.findall(r"\\cite\w*\{([^}]+)\}", text):
        keys.update(key.strip() for key in group.split(",") if key.strip())
    return sorted(keys)


def detect_technique(text: str) -> str:
    lowered = text.lower()
    aliases = (
        ("mapa_conceptual", ("mapa conceptual", "tikzpicture")),
        ("tabla_didactica", ("cuadro comparativo", "longtable", "tabular")),
        ("cuestionario_diagnostico", ("cuestionario", "reactivo")),
        ("estudio_de_caso", ("estudio de caso", "caso práctico", "caso practico")),
        ("foro_diagnostico", ("foro diagnóstico", "foro diagnostico")),
    )
    return next((name for name, values in aliases if any(value in lowered for value in values)), "actividad_academica")


def make_instruction(path: Path, root: Path, text: str) -> str:
    relative = path.relative_to(root).as_posix()
    institution = relative.split("/", 1)[0]
    technique = detect_technique(text)
    citation_keys = extract_bib_keys(text)
    return (
        f"Genera una actividad para la institución {institution}. "
        f"Técnica didáctica: {technique}. Conserva el contrato editorial AulaTeX, "
        "estructura de tres actos y trazabilidad bibliográfica. "
        f"Claves bibliográficas permitidas: {', '.join(citation_keys) if citation_keys else 'ninguna'}."
    )


def build_sft_rows(root: Path, *, strict_privacy: bool = True) -> tuple[list[dict[str, Any]], list[PrivacyFinding]]:
    rows: list[dict[str, Any]] = []
    findings: list[PrivacyFinding] = []
    seen: set[str] = set()
    for path in iter_activity_tex(root):
        full_text = read_utf8(path)
        body = document_body(full_text)
        if len(body) < MIN_DOCUMENT_CHARS:
            continue
        source = path.relative_to(root).as_posix()
        current = privacy_findings(body, source)
        findings.extend(current)
        if current and strict_privacy:
            continue
        clean, _ = redact_text(body)
        fingerprint = sha256_text(re.sub(r"\s+", " ", clean).strip())
        if fingerprint in seen:
            continue
        seen.add(fingerprint)
        rows.append({
            "schema_version": SCHEMA_VERSION,
            "id": fingerprint[:16],
            "target": source,
            "group": str(path.parent.relative_to(root).as_posix()),
            "technique": detect_technique(clean),
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": make_instruction(path, root, clean)},
                {"role": "assistant", "content": clean},
            ],
            "allowed_citation_keys": extract_bib_keys(clean),
            "content_sha256": fingerprint,
        })
    return rows, findings


def validate_sft_row(row: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if row.get("schema_version") != SCHEMA_VERSION:
        errors.append("schema_version inválida")
    messages = row.get("messages")
    if not isinstance(messages, list) or [m.get("role") for m in messages] != ["system", "user", "assistant"]:
        errors.append("messages debe contener system, user y assistant")
    elif any(not str(message.get("content", "")).strip() for message in messages):
        errors.append("hay mensajes vacíos")
    if not str(row.get("target", "")).strip():
        errors.append("target vacío")
    return errors


def grouped_split(rows: Sequence[dict[str, Any]], *, seed: int = 42,
                  train_ratio: float = 0.8, validation_ratio: float = 0.1) -> dict[str, list[dict[str, Any]]]:
    if train_ratio <= 0 or validation_ratio < 0 or train_ratio + validation_ratio >= 1:
        raise ValueError("Las proporciones deben dejar una partición de prueba positiva")
    groups = sorted({str(row.get("group") or row.get("target")) for row in rows})
    random.Random(seed).shuffle(groups)
    if not groups:
        return {"train": [], "validation": [], "test": []}
    n_train = max(1, int(len(groups) * train_ratio))
    n_validation = int(len(groups) * validation_ratio)
    if len(groups) >= 3:
        n_validation = max(1, n_validation)
        n_train = min(n_train, len(groups) - 2)
    train_groups = set(groups[:n_train])
    validation_groups = set(groups[n_train:n_train + n_validation])
    result = {"train": [], "validation": [], "test": []}
    for row in rows:
        group = str(row.get("group") or row.get("target"))
        split = "train" if group in train_groups else "validation" if group in validation_groups else "test"
        result[split].append(row)
    return result


def assert_no_group_leakage(splits: dict[str, Sequence[dict[str, Any]]]) -> None:
    group_sets = {
        name: {str(row.get("group") or row.get("target")) for row in rows}
        for name, rows in splits.items()
    }
    names = list(group_sets)
    for index, left in enumerate(names):
        for right in names[index + 1:]:
            overlap = group_sets[left] & group_sets[right]
            if overlap:
                raise ValueError(f"Fuga entre {left} y {right}: {sorted(overlap)[:3]}")


def write_jsonl(path: Path, rows: Iterable[dict[str, Any]]) -> int:
    materialized = list(rows)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in materialized:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
    return len(materialized)


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        value = json.loads(line)
        if not isinstance(value, dict):
            raise ValueError(f"{path}:{line_number} no contiene un objeto JSON")
        rows.append(value)
    return rows


def write_splits(out_dir: Path, splits: dict[str, Sequence[dict[str, Any]]], *, seed: int = 42,
                 source_root: Path | None = None, privacy_count: int = 0) -> CorpusManifest:
    assert_no_group_leakage(splits)
    counts: dict[str, int] = {}
    hashes: dict[str, str] = {}
    for name, rows in splits.items():
        path = out_dir / f"sft-{name}.jsonl"
        counts[name] = write_jsonl(path, rows)
        hashes[path.name] = sha256_file(path)
    manifest = CorpusManifest(
        schema_version=SCHEMA_VERSION,
        seed=seed,
        counts=counts,
        hashes=hashes,
        source_root=str((source_root or repo_root()).resolve()),
        privacy_findings=privacy_count,
    )
    (out_dir / "manifest.json").write_text(
        json.dumps(asdict(manifest), ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return manifest


def dataset_stats(rows: Sequence[dict[str, Any]]) -> dict[str, Any]:
    techniques = Counter(str(row.get("technique", "")) for row in rows)
    lengths = [len(row["messages"][-1]["content"]) for row in rows if row.get("messages")]
    return {
        "rows": len(rows),
        "groups": len({str(row.get("group")) for row in rows}),
        "techniques": dict(techniques),
        "min_chars": min(lengths, default=0),
        "max_chars": max(lengths, default=0),
        "mean_chars": round(sum(lengths) / len(lengths), 1) if lengths else 0,
    }


def latex_generation_checks(text: str, allowed_citation_keys: Sequence[str] = ()) -> dict[str, Any]:
    cited = set(extract_bib_keys(text))
    allowed = set(allowed_citation_keys)
    manual_images = bool(re.search(r"\\includegraphics", text))
    native_images = any(command in text for command in NATIVE_IMAGE_COMMANDS)
    return {
        "has_introduction": bool(re.search(r"\\section\*?\{Introducci[oó]n\}", text, re.I)),
        "has_conclusion": bool(re.search(r"\\section\*?\{Conclusiones?\}", text, re.I)),
        "has_literal_development_heading": bool(re.search(r"\\section\*?\{Desarrollo\}", text, re.I)),
        "unknown_citation_keys": sorted(cited - allowed) if allowed else [],
        "uses_manual_includegraphics": manual_images,
        "uses_native_image_commands": native_images,
        "native_image_rule_ok": not manual_images or native_images,
        "has_placeholders": bool(re.search(r"\b(?:TODO|TBD|pendiente|lorem ipsum)\b", text, re.I)),
    }
