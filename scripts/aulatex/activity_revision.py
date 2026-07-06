from __future__ import annotations

import re
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .activity_observer import ActivityObservationRequest, ActivityObserver
from .workspace import AulaTeXWorkspace


@dataclass(frozen=True)
class ActivityRevisionRequest:
    target: str
    activity_number: int = 1
    output: str = ""
    apply: bool = False
    backup: bool = True


@dataclass(frozen=True)
class ActivityRevisionResult:
    run_id: str
    run_dir: Path
    ok: bool
    plan_path: Path
    report_path: Path
    patched_tex_path: Path | None = None


class ActivityReviser:
    def __init__(self, workspace: AulaTeXWorkspace | None = None) -> None:
        self.workspace = workspace or AulaTeXWorkspace()
        self.observer = ActivityObserver(self.workspace)
        self.root = self.workspace.feedback_root / "activity-revision" / "runs"
        self.root.mkdir(parents=True, exist_ok=True)

    def revise(self, request: ActivityRevisionRequest) -> ActivityRevisionResult:
        run_id = f"{self.workspace.timestamp()}-activity-{int(request.activity_number):02d}-revision"
        run_dir = self._resolve_run_dir(request, run_id)
        run_dir.mkdir(parents=True, exist_ok=True)
        observation = self.observer.observe(
            ActivityObservationRequest(
                target=request.target,
                activity_number=request.activity_number,
                output=str(run_dir / "obs"),
                compile_check=False,
            )
        )
        state = json.loads(observation.state_path.read_text(encoding="utf-8"))
        evaluation = json.loads(observation.evaluation_path.read_text(encoding="utf-8"))
        contract = evaluation.get("contract", {})
        findings = list(evaluation.get("critical_findings") or []) + list(contract.get("findings") or [])
        tex_path = self.workspace.resolve_target(state.get("target_tex", ""))
        patched_tex_path, applied_actions = self._apply_simple_patches(tex_path, state, evaluation, request)

        plan = {
            "run_id": run_id,
            "target": state.get("target_tex", ""),
            "activity_number": int(request.activity_number),
            "next_action": evaluation.get("next_action", "revise-activity"),
            "revision_targets": self._revision_targets(state, evaluation),
            "applied_actions": applied_actions,
            "apply": bool(request.apply),
            "findings": findings,
            "observation": self.workspace.relative(observation.state_path),
            "evaluation": self.workspace.relative(observation.evaluation_path),
            "patched_tex": self.workspace.relative(patched_tex_path) if patched_tex_path else "",
        }
        plan_path = run_dir / "plan-revision-actividad.json"
        report_path = run_dir / "reporte-revision-actividad.md"
        plan_path.write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8")
        report_path.write_text(self._render_report(plan), encoding="utf-8")
        self.workspace.append_bitacora(run_id, "activity-revision", plan)
        return ActivityRevisionResult(run_id, run_dir, bool(plan["revision_targets"]), plan_path, report_path, patched_tex_path)

    def _resolve_run_dir(self, request: ActivityRevisionRequest, run_id: str) -> Path:
        if request.output.strip():
            return self.workspace.resolve_target(request.output)
        return self.root / run_id

    def _revision_targets(self, state: dict[str, Any], evaluation: dict[str, Any]) -> list[dict[str, str]]:
        contract = evaluation.get("contract", {})
        checks = contract.get("checks", {})
        actions: list[dict[str, str]] = []
        if not checks.get("evaluation_criteria", True):
            actions.append({
                "action": "explicitar-criterios-entrega",
                "reason": "Falta evidencia contractual de criterios de evaluación o entrega.",
            })
        if not checks.get("didactic_technique", True):
            actions.append({
                "action": "aclarar-tecnica-didactica",
                "reason": "No queda clara la técnica didáctica o el producto solicitado.",
            })
        if state.get("signals", {}).get("placeholder_hits"):
            actions.append({
                "action": "resolver-placeholders",
                "reason": "Persisten placeholders o pendientes en el TEX.",
            })
        if not checks.get("final_reflection", True):
            actions.append({
                "action": "reforzar-cierre-argumentativo",
                "reason": "No se detecta una conclusión suficientemente explícita.",
            })
        if not actions:
            actions.append({
                "action": "revision-manual",
                "reason": "La actividad requiere revisión editorial fina, no una corrección determinística segura.",
            })
        return actions

    def _apply_simple_patches(
        self,
        tex_path: Path,
        state: dict[str, Any],
        evaluation: dict[str, Any],
        request: ActivityRevisionRequest,
    ) -> tuple[Path | None, list[str]]:
        if not tex_path.exists() or not tex_path.is_file():
            return None, []
        original = tex_path.read_text(encoding="utf-8", errors="replace")
        patched = original
        applied_actions: list[str] = []
        contract_checks = (evaluation.get("contract") or {}).get("checks", {})
        if not contract_checks.get("evaluation_criteria", True):
            patched = self._ensure_evaluation_criteria_section(patched, state)
            if patched != original:
                applied_actions.append("explicitar-criterios-entrega")
        if patched == original:
            return None, applied_actions
        if request.apply:
            if request.backup:
                backup_path = tex_path.with_suffix(tex_path.suffix + ".activity-revision.bak")
                backup_path.write_text(original, encoding="utf-8")
            tex_path.write_text(patched, encoding="utf-8")
            return tex_path, applied_actions
        preview_path = self._resolve_run_dir(request, "preview") / tex_path.name
        preview_path.parent.mkdir(parents=True, exist_ok=True)
        preview_path.write_text(patched, encoding="utf-8")
        return preview_path, applied_actions

    def _ensure_evaluation_criteria_section(self, text: str, state: dict[str, Any]) -> str:
        if re.search(r"\\section\{Criterios de entrega y evaluaci[óo]n\}", text, re.IGNORECASE):
            return text
        product = "el mapa conceptual" if state.get("signals", {}).get("product_visual_detected") else "el entregable solicitado"
        section = (
            "\n\\section{Criterios de entrega y evaluación}\n\n"
            "Para considerar cumplida esta actividad, se verifican los siguientes criterios de entrega:\n\n"
            "\\begin{enumerate}\n"
            f"\t\\item \\textbf{{Pertinencia del producto}}: {product.capitalize()} debe responder al objetivo y propósito de la actividad.\n"
            "\t\\item \\textbf{Cobertura conceptual}: el desarrollo debe incorporar los conceptos fundamentales identificados en la bibliografía y en la síntesis previa.\n"
            "\t\\item \\textbf{Sustento académico}: toda afirmación relevante debe mantenerse trazable a las fuentes citadas en el documento.\n"
            "\t\\item \\textbf{Claridad argumentativa}: la explicación del producto debe mostrar coherencia, orden expositivo y cierre reflexivo.\n"
            "\\end{enumerate}\n"
        )
        conclusion_match = re.search(r"\n\\section\{Conclusi[óo]n\}", text)
        if conclusion_match:
            return text[: conclusion_match.start()] + section + text[conclusion_match.start() :]
        bibliography_match = re.search(r"\n\\begin\{thebibliography\}", text)
        if bibliography_match:
            return text[: bibliography_match.start()] + section + text[bibliography_match.start() :]
        return text + section

    def _render_report(self, plan: dict[str, Any]) -> str:
        lines = [
            "# Revisión de actividad",
            "",
            f"- TEX objetivo: {plan['target']}",
            f"- Actividad: {plan['activity_number']}",
            f"- Siguiente acción observada: {plan['next_action']}",
            "",
            "## Hallazgos",
            "",
        ]
        findings = plan.get("findings") or []
        if findings:
            lines.extend(f"- {item}" for item in findings)
        else:
            lines.append("- No se registraron hallazgos adicionales.")
        lines.extend(["", "## Acciones propuestas", ""])
        lines.extend(f"- {item['action']}: {item['reason']}" for item in plan.get("revision_targets", []))
        applied = plan.get("applied_actions") or []
        if applied:
            lines.extend(["", "## Parches aplicados", ""])
            lines.extend(f"- {item}" for item in applied)
        patched_tex = plan.get("patched_tex")
        if patched_tex:
            lines.extend(["", "## TEX resultante", "", f"- {patched_tex}"])
        lines.append("")
        return "\n".join(lines)