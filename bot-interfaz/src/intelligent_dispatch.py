from __future__ import annotations

import json
import re
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.aulatex import IntelligentEngine, IntelligentEngineRequest, LLM_ENGINES  # type: ignore[import-not-found]

from .azure_openai_client import invoke_chat
from .config import Settings

INTELLIGENT_COMMAND_PREFIXES = ("motor:", "inteligente:", "aulatex:")
ENGINE_LABEL_BY_PROVIDER = {
    "azure-openai": "Auto (model-router)",
    "model-router": "Auto (model-router)",
    "auto": "Auto (model-router)",
    "codex": "Codex",
    "gpt-pro": "GPT-Pro",
    "claude-foundry": "Claude Foundry",
}
ENGINE_NAME_ALIASES = {
    "codex": "Codex",
    "gpt-pro": "GPT-Pro",
    "gpt pro": "GPT-Pro",
    "gptpro": "GPT-Pro",
    "claude": "Claude Foundry",
    "claude foundry": "Claude Foundry",
    "claude-foundry": "Claude Foundry",
    "model-router": "Auto (model-router)",
    "model router": "Auto (model-router)",
    "auto": "Auto (model-router)",
    "azure-openai": "Auto (model-router)",
    "azure openai": "Auto (model-router)",
}
INTELLIGENT_ROUTER_PROMPT = """Eres un enrutador de instrucciones para el motor inteligente de AulaTeX.
Convierte una instruccion libre del usuario en un objeto JSON valido con esta forma exacta:
{
  "target": ".",
  "activity_number": 0,
  "output": "",
  "backend": "langgraph",
  "max_targets": 12,
  "audit_path": "",
  "include_reports": true,
  "include_presentations": true,
  "engines": []
}

Reglas:
- target debe ser una ruta relativa al repositorio cuando el usuario identifique una carpeta o archivo. Usa "." si no se especifica.
- activity_number debe ser entero >= 0. Usa 0 si no se menciona.
- backend solo puede ser langgraph o classic.
- max_targets debe ser entero entre 1 y 24.
- include_reports=false si el usuario pide solo presentaciones.
- include_presentations=false si el usuario pide solo reportes.
- engines debe contener solo estos nombres exactos cuando el usuario los pida: Codex, Auto (model-router), GPT-Pro, Claude Foundry.
- Si el usuario no pide motores concretos, deja engines como lista vacia.
- No inventes rutas inexistentes si la instruccion no alcanza para resolverlas.
- Responde exclusivamente con JSON valido, sin Markdown ni explicaciones.
"""

EDITORIAL_PROPOSAL_PROMPT = """Eres un estratega editorial para AulaTeX.
Debes convertir una nota limpia en una propuesta operativa para trabajar sobre el repositorio actual.

Responde exclusivamente con JSON valido, sin Markdown ni explicaciones, con esta forma exacta:
{
    "instruction": "",
    "backend": "langgraph",
    "target_hint": ".",
    "nucleo": "",
    "desarrollo": "",
    "accionables": "",
    "evidencias": "",
    "sintesis": ""
}

Reglas:
- instruction debe ser una instruccion clara y ejecutable para /motor, centrada en campanas, lotes, rutas, ciclos o acciones editoriales sobre el repo.
- backend solo puede ser langgraph o classic. Prefiere langgraph salvo restriccion explicita.
- target_hint debe ser una ruta candidata observada en el repo o ".".
- nucleo, desarrollo, accionables, evidencias y sintesis deben redactarse como instrucciones para trabajo editorial sobre proyecto, no como comentario sobre una nota personal.
- accionables debe incluir lote/campana sugerido, criterios de prioridad y siguiente paso de ejecucion.
- no inventes rutas inexistentes.
"""


@dataclass(frozen=True)
class IntelligentDispatchPlan:
    instruction: str
    request: IntelligentEngineRequest
    payload: dict[str, Any]


@dataclass(frozen=True)
class IntelligentDispatchResult:
    instruction: str
    request: IntelligentEngineRequest
    manifest: dict[str, Any]
    result: Any


@dataclass(frozen=True)
class EditorialProposal:
    instruction: str
    backend: str
    target_hint: str
    sections: dict[str, str]


def instruction_help_text() -> str:
    return (
        "Usa /motor seguido de una instruccion editorial.\n\n"
        "Ejemplos:\n"
        "/motor planifica UCNL/licenciatura-en-administracion/administracion-i-lad actividad 1\n"
        "/motor revisa solo reportes en UnADM con backend classic y maximo 4 objetivos\n"
        "Tambien puedes escribir motor: <instruccion>."
    )


def extract_intelligent_instruction(text: str) -> str | None:
    raw = text.strip()
    lowered = raw.casefold()
    for prefix in INTELLIGENT_COMMAND_PREFIXES:
        if lowered.startswith(prefix):
            instruction = raw[len(prefix) :].strip()
            return instruction or ""
    return None


def _normalize_text(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", " ", ascii_text.casefold()).strip()


def _score_scope_candidate(instruction: str, candidate: str) -> int:
    instruction_tokens = set(_normalize_text(instruction).split())
    candidate_tokens = set(_normalize_text(candidate).split())
    if not instruction_tokens or not candidate_tokens:
        return 0
    overlap = instruction_tokens & candidate_tokens
    if not overlap:
        return 0
    score = len(overlap) * 3
    candidate_norm = _normalize_text(candidate)
    for token in overlap:
        if len(token) >= 4 and token in candidate_norm:
            score += 1
    return score


def _candidate_scope_lines(instruction: str) -> list[str]:
    scopes_root = [path for path in sorted(REPO_ROOT.iterdir()) if path.is_dir() and not path.name.startswith(".")]
    candidates: list[tuple[int, str]] = []
    for path in scopes_root:
        candidate = path.name
        score = _score_scope_candidate(instruction, candidate)
        if score > 0:
            candidates.append((score, candidate))
        for child in sorted(path.rglob("*.tex")):
            relative = child.relative_to(REPO_ROOT).as_posix()
            score = _score_scope_candidate(instruction, relative)
            if score > 0:
                candidates.append((score, relative))
    candidates.sort(key=lambda item: (-item[0], item[1]))
    unique_lines: list[str] = []
    seen: set[str] = set()
    for _, candidate in candidates:
        if candidate in seen:
            continue
        seen.add(candidate)
        unique_lines.append(candidate)
        if len(unique_lines) >= 12:
            break
    return unique_lines


def _default_engines(provider: str) -> tuple[str, ...]:
    preferred = ENGINE_LABEL_BY_PROVIDER.get(provider, "Auto (model-router)")
    ordered = [preferred, *LLM_ENGINES]
    seen: set[str] = set()
    result: list[str] = []
    for engine in ordered:
        if engine in seen:
            continue
        seen.add(engine)
        result.append(engine)
    return tuple(result)


def _normalize_engines(raw_engines: object, provider: str) -> tuple[str, ...]:
    if not isinstance(raw_engines, list) or not raw_engines:
        return _default_engines(provider)

    result: list[str] = []
    for raw in raw_engines:
        key = str(raw or "").strip()
        if not key:
            continue
        engine = ENGINE_NAME_ALIASES.get(key.casefold(), key)
        if engine in LLM_ENGINES and engine not in result:
            result.append(engine)
    return tuple(result) or _default_engines(provider)


def _coerce_bool(value: object, default: bool) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        normalized = value.strip().casefold()
        if normalized in {"1", "true", "yes", "si", "on"}:
            return True
        if normalized in {"0", "false", "no", "off"}:
            return False
    return default


def _coerce_int(value: object, default: int, minimum: int, maximum: int) -> int:
    try:
        parsed = int(value)
    except (TypeError, ValueError):
        return default
    return max(minimum, min(maximum, parsed))


def _build_router_messages(instruction: str) -> list[dict[str, str]]:
    candidates = _candidate_scope_lines(instruction)
    candidate_block = "\n".join(f"- {candidate}" for candidate in candidates) if candidates else "- ."
    return [
        {"role": "system", "content": INTELLIGENT_ROUTER_PROMPT},
        {
            "role": "user",
            "content": (
                f"Repositorio raiz: {REPO_ROOT.as_posix()}\n"
                f"Rutas candidatas observadas:\n{candidate_block}\n\n"
                f"Instruccion del usuario:\n{instruction}"
            ),
        },
    ]


def _request_from_payload(payload: dict[str, Any], settings: Settings) -> IntelligentEngineRequest:
    target = str(payload.get("target") or ".").strip() or "."
    target_path = Path(target)
    resolved_target = (REPO_ROOT / target_path).resolve() if not target_path.is_absolute() else target_path.resolve()
    if target != "." and not resolved_target.exists():
        raise RuntimeError(f"El target solicitado no existe en el repositorio: {target}")

    backend = str(payload.get("backend") or "langgraph").strip().lower() or "langgraph"
    if backend not in {"langgraph", "classic"}:
        backend = "langgraph"

    return IntelligentEngineRequest(
        target=target,
        activity_number=_coerce_int(payload.get("activity_number"), 0, 0, 999),
        output=str(payload.get("output") or "").strip(),
        backend=backend,
        max_targets=_coerce_int(payload.get("max_targets"), 12, 1, 24),
        audit_path=str(payload.get("audit_path") or "").strip(),
        include_reports=_coerce_bool(payload.get("include_reports"), True),
        include_presentations=_coerce_bool(payload.get("include_presentations"), True),
        engines=_normalize_engines(payload.get("engines"), settings.llm_provider),
    )


def build_editorial_proposal(note_title: str, corrected_text: str, concepts: str, settings: Settings) -> EditorialProposal:
    candidate_block = "\n".join(f"- {candidate}" for candidate in _candidate_scope_lines(f"{note_title}\n{corrected_text}")) or "- ."
    raw = invoke_chat(
        settings,
        [
            {"role": "system", "content": EDITORIAL_PROPOSAL_PROMPT},
            {
                "role": "user",
                "content": (
                    f"Repositorio raiz: {REPO_ROOT.as_posix()}\n"
                    f"Rutas candidatas observadas:\n{candidate_block}\n\n"
                    f"Titulo de referencia:\n{note_title}\n\n"
                    f"Nota limpia:\n{corrected_text}\n\n"
                    f"Conceptos detectados:\n{concepts}"
                ),
            },
        ],
        max_tokens=2200,
        temperature=0.2,
        response_format_json=True,
    )
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise RuntimeError("La propuesta editorial no devolvio JSON valido.") from exc
    if not isinstance(payload, dict):
        raise RuntimeError("La propuesta editorial no devolvio un objeto JSON.")

    instruction = str(payload.get("instruction") or "").strip()
    if not instruction:
        raise RuntimeError("La propuesta editorial no incluyo una instruccion ejecutable.")
    backend = str(payload.get("backend") or "langgraph").strip().lower() or "langgraph"
    if backend not in {"langgraph", "classic"}:
        backend = "langgraph"
    target_hint = str(payload.get("target_hint") or ".").strip() or "."
    target_path = Path(target_hint)
    resolved_target = (REPO_ROOT / target_path).resolve() if not target_path.is_absolute() else target_path.resolve()
    if target_hint != "." and not resolved_target.exists():
        target_hint = "."

    return EditorialProposal(
        instruction=instruction,
        backend=backend,
        target_hint=target_hint,
        sections={
            "Nucleo": str(payload.get("nucleo") or "").strip(),
            "Desarrollo": str(payload.get("desarrollo") or "").strip(),
            "Accionables": str(payload.get("accionables") or "").strip(),
            "Evidencias y supuestos": str(payload.get("evidencias") or "").strip(),
            "Sintesis breve": str(payload.get("sintesis") or "").strip(),
        },
    )


def plan_intelligent_dispatch(instruction: str, settings: Settings) -> IntelligentDispatchPlan:
    messages = _build_router_messages(instruction)
    raw = invoke_chat(
        settings,
        messages,
        max_tokens=1600,
        temperature=0.1,
        response_format_json=True,
    )
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise RuntimeError("El LLM no devolvio una instruccion JSON valida para el motor inteligente.") from exc
    if not isinstance(payload, dict):
        raise RuntimeError("La instruccion estructurada del motor inteligente no es un objeto JSON.")

    request = _request_from_payload(payload, settings)
    return IntelligentDispatchPlan(instruction=instruction, request=request, payload=payload)


def execute_intelligent_dispatch_plan(plan: IntelligentDispatchPlan) -> IntelligentDispatchResult:
    result = IntelligentEngine().run(plan.request)
    manifest = json.loads(result.manifest_path.read_text(encoding="utf-8"))
    return IntelligentDispatchResult(
        instruction=plan.instruction,
        request=plan.request,
        manifest=manifest,
        result=result,
    )


def run_intelligent_dispatch(instruction: str, settings: Settings) -> IntelligentDispatchResult:
    return execute_intelligent_dispatch_plan(plan_intelligent_dispatch(instruction, settings))


def _display_path(path: Path) -> str:
    resolved = path.resolve()
    try:
        return resolved.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return str(resolved)


def format_dispatch_plan_markdown(plan: IntelligentDispatchPlan) -> str:
    request = plan.request
    lines = [
        "# Validar ejecución del motor inteligente",
        "",
        "El motor inteligente todavía no se ha ejecutado. Revisa el plan y confirma si deseas continuar.",
        "",
        f"- Instrucción original: {plan.instruction}",
        f"- Target: `{request.target}`",
        f"- Actividad: {request.activity_number}",
        f"- Backend: `{request.backend}`",
        f"- Máximo de objetivos: {request.max_targets}",
        f"- Incluir reportes: {'sí' if request.include_reports else 'no'}",
        f"- Incluir presentaciones: {'sí' if request.include_presentations else 'no'}",
        f"- Motores: {', '.join(request.engines)}",
        "",
        "## JSON interpretado",
        "",
        "```json",
        json.dumps(plan.payload, ensure_ascii=False, indent=2),
        "```",
        "",
        "Pulsa **Ejecutar motor** para continuar o **Cancelar** para descartar.",
    ]
    return "\n".join(lines)


def format_dispatch_summary(dispatch: IntelligentDispatchResult) -> str:
    scope = dispatch.manifest.get("scope", {}) if isinstance(dispatch.manifest.get("scope"), dict) else {}
    inventory = dispatch.manifest.get("inventory_summary", {}) if isinstance(dispatch.manifest.get("inventory_summary", {}), dict) else {}
    request = dispatch.request
    run_dir = _display_path(dispatch.result.run_dir)
    manifest_path = _display_path(dispatch.result.manifest_path)
    report_path = _display_path(dispatch.result.report_path)
    lines = [
        "Motor inteligente ejecutado.",
        f"Target: {request.target}",
        f"Scope: {scope.get('scope_label') or scope.get('target_root') or request.target}",
        f"Backend: {request.backend}",
        f"Motores: {', '.join(request.engines)}",
        f"Objetivos planificados: {inventory.get('planned_targets', 0)}",
        f"Inventario TEX: {inventory.get('tex_total', 0)}",
        f"Run: {run_dir}",
        f"Manifest: {manifest_path}",
        f"Reporte: {report_path}",
    ]
    return "\n".join(lines)