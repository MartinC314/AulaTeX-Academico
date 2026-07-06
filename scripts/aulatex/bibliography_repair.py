from __future__ import annotations

import json
import re
import shutil
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any

from .activity_observer import ActivityObserver
from .workspace import AulaTeXWorkspace


KNOWN_BIB_ALIASES = {
    "finnis_estudios_2017": "finnisEstudiosTeoriaDerecho2017",
    "lovon_manual_2020": "lovonManualPracticoFilosofia2020",
    "ruiz_rodriguez_filosofia_derecho_2009": "ruizrodriguezFilosofiaDerecho2009",
    "rojas_gonzalez_filosofia_derecho_2018": "rojas-gonzalezFilosofiaDerecho2018",
    "franzoni_acevedo_ley_2017": "franzoniacevedoLeyGeneralAcceso2017",
    "noauthor_constitucion_nodate": "cpeum2026",
    "de_victimas_ley_2013": "LeyGeneralVictimas",
    "generales_ley_2021": "LeyAmparoReglamentaria",
    "gandara_ley_2015": "lastraConceptosJuridicosFundamentales",
}


@dataclass(frozen=True)
class BibliographyRepairRequest:
    target: str
    activity_number: int = 1
    output: str = ""
    apply: bool = False
    backup: bool = True
    min_confidence: float = 0.72


@dataclass(frozen=True)
class BibliographyRepairResult:
    run_id: str
    run_dir: Path
    ok: bool
    plan_path: Path
    report_path: Path
    patched_tex_path: Path | None = None


class BibliographyRepairer:
    def __init__(self, workspace: AulaTeXWorkspace | None = None) -> None:
        self.workspace = workspace or AulaTeXWorkspace()
        self.observer = ActivityObserver(self.workspace)
        self.root = self.workspace.feedback_root / "bibliography-repair" / "runs"
        self.root.mkdir(parents=True, exist_ok=True)

    def repair(self, request: BibliographyRepairRequest) -> BibliographyRepairResult:
        run_id = f"{self.workspace.timestamp()}-activity-{int(request.activity_number):02d}-bib-repair"
        run_dir = self._resolve_run_dir(request, run_id)
        run_dir.mkdir(parents=True, exist_ok=True)

        observation = self.observer.observe(
            self._observation_request(request, run_dir)
        )
        state = json.loads(observation.state_path.read_text(encoding="utf-8"))
        tex_path = self.workspace.resolve_target(state.get("target_tex", ""))
        bib_path = self.workspace.resolve_target(state.get("bib_ref", ""))
        tex_text = tex_path.read_text(encoding="utf-8", errors="replace") if tex_path.exists() else ""
        bib_text = bib_path.read_text(encoding="utf-8", errors="replace") if bib_path.exists() else ""
        bib_keys = sorted(self._extract_bib_keys(bib_text))
        missing_keys = list(state.get("signals", {}).get("missing_bib_keys", []))
        replacements = [self._suggest_replacement(key, bib_keys, request.min_confidence) for key in missing_keys]
        actionable = [item for item in replacements if item["status"] == "mapped"]
        unresolved = [item for item in replacements if item["status"] != "mapped"]

        patched_text = tex_text
        for item in actionable:
            patched_text = self._replace_cite_key(patched_text, item["old_key"], item["new_key"])

        changed = patched_text != tex_text
        patched_tex_path: Path | None = None
        if request.apply and changed:
            if request.backup:
                backup_path = tex_path.with_suffix(tex_path.suffix + f".{run_id}.bak")
                shutil.copy2(tex_path, backup_path)
            tex_path.write_text(patched_text, encoding="utf-8")
            patched_tex_path = tex_path
        else:
            patched_tex_path = run_dir / tex_path.name if tex_path.name else None
            if patched_tex_path is not None:
                patched_tex_path.write_text(patched_text, encoding="utf-8")

        plan = {
            "run_id": run_id,
            "target_tex": self.workspace.relative(tex_path),
            "bib_ref": self.workspace.relative(bib_path),
            "apply": bool(request.apply),
            "backup": bool(request.backup),
            "changed": changed,
            "missing_keys": missing_keys,
            "replacements": replacements,
            "actionable_count": len(actionable),
            "unresolved_count": len(unresolved),
            "observation": self.workspace.relative(observation.state_path),
            "patched_preview": self.workspace.relative(patched_tex_path) if patched_tex_path else "",
        }
        ok = bool(missing_keys) and len(unresolved) == 0 and changed
        if request.apply:
            ok = ok and patched_tex_path is not None

        plan_path = run_dir / "plan-reparacion-bibliografia.json"
        report_path = run_dir / "reporte-reparacion-bibliografia.md"
        plan_path.write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8")
        report_path.write_text(self._render_report(plan), encoding="utf-8")
        (run_dir / "manifest.json").write_text(json.dumps({**plan, "ok": ok, "report": self.workspace.relative(report_path)}, ensure_ascii=False, indent=2), encoding="utf-8")
        self.workspace.append_bitacora(run_id, "bibliography-repair", {**plan, "ok": ok})
        return BibliographyRepairResult(run_id, run_dir, ok, plan_path, report_path, patched_tex_path)

    def _observation_request(self, request: BibliographyRepairRequest, run_dir: Path):
        from .activity_observer import ActivityObservationRequest

        return ActivityObservationRequest(
            target=request.target,
            activity_number=request.activity_number,
            output=str(run_dir / "observer"),
            compile_check=False,
        )

    def _resolve_run_dir(self, request: BibliographyRepairRequest, run_id: str) -> Path:
        if request.output.strip():
            return self.workspace.resolve_target(request.output) / run_id
        return self.root / run_id

    def _suggest_replacement(self, old_key: str, bib_keys: list[str], min_confidence: float) -> dict[str, Any]:
        if old_key in KNOWN_BIB_ALIASES and KNOWN_BIB_ALIASES[old_key] in bib_keys:
            return {
                "old_key": old_key,
                "new_key": KNOWN_BIB_ALIASES[old_key],
                "confidence": 1.0,
                "method": "known-alias",
                "status": "mapped",
            }
        normalized_old = self._normalize_key(old_key)
        scored = []
        for candidate in bib_keys:
            score = SequenceMatcher(None, normalized_old, self._normalize_key(candidate)).ratio()
            scored.append((score, candidate))
        scored.sort(reverse=True)
        best_score, best_key = scored[0] if scored else (0.0, "")
        return {
            "old_key": old_key,
            "new_key": best_key if best_score >= min_confidence else "",
            "confidence": round(best_score, 4),
            "method": "normalized-key-similarity",
            "status": "mapped" if best_score >= min_confidence else "unresolved",
            "best_candidate": best_key,
        }

    def _replace_cite_key(self, text: str, old_key: str, new_key: str) -> str:
        pattern = re.compile(r"(\\cite[t|p]?\*?(?:\[[^\]]*\])*\{)([^}]+)(\})")

        def repl(match: re.Match[str]) -> str:
            keys = [key.strip() for key in match.group(2).split(",")]
            keys = [new_key if key == old_key else key for key in keys]
            return match.group(1) + ",".join(keys) + match.group(3)

        return pattern.sub(repl, text)

    def _render_report(self, plan: dict[str, Any]) -> str:
        lines = [
            "# Reparación bibliográfica",
            "",
            f"- TEX: `{plan['target_tex']}`",
            f"- BIB: `{plan['bib_ref']}`",
            f"- Aplicado: {'sí' if plan['apply'] else 'no'}",
            f"- Cambios detectados: {'sí' if plan['changed'] else 'no'}",
            f"- Reemplazos accionables: {plan['actionable_count']}",
            f"- Sin resolver: {plan['unresolved_count']}",
            "",
            "## Reemplazos propuestos",
            "",
        ]
        for item in plan["replacements"]:
            status = item["status"]
            new_key = item.get("new_key") or item.get("best_candidate") or ""
            lines.append(f"- `{item['old_key']}` -> `{new_key}` | {status} | confianza={item['confidence']} | método={item['method']}")
        if plan.get("patched_preview"):
            lines.extend(["", "## Vista previa", "", f"- `{plan['patched_preview']}`"])
        lines.append("")
        return "\n".join(lines)

    def _extract_bib_keys(self, text: str) -> set[str]:
        return {match.group(1).strip() for match in re.finditer(r"@\w+\s*\{\s*([^,\s]+)", text)}

    def _normalize_key(self, value: str) -> str:
        return re.sub(r"[^a-z0-9]", "", value.lower())
