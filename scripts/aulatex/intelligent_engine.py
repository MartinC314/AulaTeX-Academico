from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Literal

from .workspace import AulaTeXWorkspace


@dataclass(frozen=True)
class IntelligentEngineRequest:
    target: str = "."
    activity_number: int = 0
    output: str = ""
    backend: Literal["langgraph", "classic"] = "langgraph"
    max_targets: int = 12
    audit_path: str = ""
    include_reports: bool = True
    include_presentations: bool = True
    engines: tuple[str, ...] = ("Codex", "Auto (model-router)", "GPT-Pro", "Claude Foundry")


@dataclass(frozen=True)
class IntelligentEngineResult:
    ok: bool
    run_id: str
    run_dir: Path
    manifest_path: Path
    report_path: Path


class IntelligentEngine:
    """Planificador v1 del motor inteligente editorial."""

    def __init__(self, workspace: AulaTeXWorkspace | None = None) -> None:
        self.workspace = workspace or AulaTeXWorkspace()
        self.root = self.workspace.feedback_root / "intelligent-engine" / "runs"
        self.root.mkdir(parents=True, exist_ok=True)

    def run(self, request: IntelligentEngineRequest) -> IntelligentEngineResult:
        run_id = f"{self.workspace.timestamp()}-intelligent-engine"
        run_dir = self._resolve_run_dir(request, run_id)
        run_dir.mkdir(parents=True, exist_ok=True)

        scope = self.workspace.find_scope_for_target(
            request.target,
            activity_number=request.activity_number or None,
        )
        target_root = self.workspace.resolve_target(request.target)
        target_root_relative = self.workspace.relative(target_root)
        inventory = self._collect_tex_inventory(request, target_root)
        audit_payload = self._load_audit_payload(request.audit_path)
        issues_by_target = self._group_audit_issues(audit_payload, target_root_relative)
        audit_status = self._audit_status(request.audit_path, audit_payload, issues_by_target)
        plans = self._build_target_plans(request, inventory, issues_by_target)

        manifest = {
            "kind": "intelligent-engine",
            "version": 1,
            "run_id": run_id,
            "request": {
                **asdict(request),
                "engines": list(request.engines),
            },
            "scope": {
                "resolved": scope is not None,
                "scope_key": scope.key if scope else "",
                "scope_level": scope.level if scope else "",
                "scope_label": scope.label if scope else "",
                "target_root": target_root_relative,
            },
            "architecture": self._build_architecture_contract(request),
            "graph_contract": self._build_graph_contract(request),
            "audit_status": audit_status,
            "inventory_summary": {
                "tex_total": len(inventory),
                "report_total": sum(1 for item in inventory if item["tex_kind"] == "report"),
                "presentation_total": sum(1 for item in inventory if item["tex_kind"] == "presentation"),
                "audit_targets": len(issues_by_target),
                "planned_targets": len(plans),
            },
            "targets": plans,
        }
        manifest_path = run_dir / "manifest.json"
        report_path = run_dir / "report.md"
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
        report_path.write_text(self._build_markdown_report(manifest), encoding="utf-8")

        return IntelligentEngineResult(
            ok=True,
            run_id=run_id,
            run_dir=run_dir,
            manifest_path=manifest_path,
            report_path=report_path,
        )

    def _resolve_run_dir(self, request: IntelligentEngineRequest, run_id: str) -> Path:
        if request.output:
            candidate = Path(request.output)
            if not candidate.is_absolute():
                candidate = self.workspace.repo_root / candidate
            return candidate.resolve()
        return self.root / run_id

    def _collect_tex_inventory(self, request: IntelligentEngineRequest, target_root: Path) -> list[dict[str, Any]]:
        items: list[dict[str, Any]] = []
        for tex in sorted(target_root.rglob("*.tex")):
            tex_kind = self._detect_tex_kind(tex)
            if tex_kind == "report" and not request.include_reports:
                continue
            if tex_kind == "presentation" and not request.include_presentations:
                continue
            if tex_kind == "other":
                continue
            pdf_path = tex.with_suffix(".pdf")
            items.append(
                {
                    "target": self.workspace.relative(tex),
                    "directory": self.workspace.relative(tex.parent),
                    "tex_kind": tex_kind,
                    "activity_number": self._extract_activity_number(tex.stem),
                    "pdf_exists": pdf_path.exists(),
                }
            )
        return items

    def _load_audit_payload(self, audit_path: str) -> dict[str, Any]:
        if not audit_path:
            return {}
        candidate = Path(audit_path)
        if not candidate.is_absolute():
            candidate = self.workspace.repo_root / candidate
        if not candidate.exists() or not candidate.is_file():
            return {}
        try:
            payload = json.loads(candidate.read_text(encoding="utf-8-sig"))
        except json.JSONDecodeError:
            return {}
        return payload if isinstance(payload, dict) else {}

    def _audit_status(self, audit_path: str, audit_payload: dict[str, Any], issues_by_target: dict[str, list[dict[str, str]]]) -> dict[str, Any]:
        candidate = Path(audit_path) if audit_path else Path()
        if audit_path and not candidate.is_absolute():
            candidate = self.workspace.repo_root / candidate
        return {
            "path": audit_path,
            "exists": bool(audit_path) and candidate.exists() and candidate.is_file(),
            "loaded": bool(audit_payload),
            "issue_total": len(audit_payload.get("issues", [])) if isinstance(audit_payload.get("issues", []), list) else 0,
            "target_total": len(issues_by_target),
        }

    def _group_audit_issues(self, audit_payload: dict[str, Any], target_root_relative: str) -> dict[str, list[dict[str, str]]]:
        grouped: dict[str, list[dict[str, str]]] = {}
        target_prefix = "" if target_root_relative == "." else target_root_relative.rstrip("/") + "/"
        for issue in audit_payload.get("issues", []):
            if not isinstance(issue, dict):
                continue
            target = str(issue.get("Target") or issue.get("target") or "").strip()
            if not target:
                continue
            if target_root_relative not in ("", "."):
                if target != target_root_relative and not target.startswith(target_prefix):
                    continue
            grouped.setdefault(target, []).append(
                {
                    "severity": str(issue.get("Severity") or issue.get("severity") or "warning"),
                    "kind": str(issue.get("Kind") or issue.get("kind") or "issue"),
                    "detail": str(issue.get("Detail") or issue.get("detail") or ""),
                }
            )
        return grouped

    def _build_target_plans(
        self,
        request: IntelligentEngineRequest,
        inventory: list[dict[str, Any]],
        issues_by_target: dict[str, list[dict[str, str]]],
    ) -> list[dict[str, Any]]:
        plans: list[dict[str, Any]] = []
        for item in inventory:
            target = str(item["target"])
            issues = issues_by_target.get(target, [])
            score = self._score_target(item, issues)
            actions = self._propose_actions(request, item, issues)
            if score <= 0 and not actions:
                continue
            plans.append(
                {
                    "target": target,
                    "directory": item["directory"],
                    "tex_kind": item["tex_kind"],
                    "activity_number": item["activity_number"],
                    "priority_score": score,
                    "issues": issues,
                    "recommended_actions": actions,
                }
            )
        plans.sort(key=lambda item: (-int(item["priority_score"]), item["target"]))
        limit = max(1, int(request.max_targets)) if plans else 0
        return plans[:limit]

    def _score_target(self, item: dict[str, Any], issues: list[dict[str, str]]) -> int:
        score = 0
        if not bool(item.get("pdf_exists")):
            score += 25
        weights = {
            "error": 20,
            "warning": 8,
            "quality": 5,
        }
        kind_weights = {
            "pdf-faltante": 40,
            "pdf-desactualizado": 20,
            "tex-sin-memoria-directa": 12,
            "reporte-preguntas-duplicadas": 18,
            "reporte-con-pendientes-o-placeholders": 16,
            "reporte-analisis-propio-insuficiente": 14,
            "reporte-introduccion-debil": 10,
            "reporte-conclusion-debil": 10,
            "presentacion-muy-breve": 16,
            "presentacion-sin-tema-visual": 14,
            "presentacion-sin-recursos-didacticos": 12,
            "memoria-json-invalido": 18,
            "memoria-ruta-inexistente": 16,
        }
        for issue in issues:
            score += weights.get(issue.get("severity", "warning"), 5)
            score += kind_weights.get(issue.get("kind", "issue"), 4)
        return score

    def _propose_actions(
        self,
        request: IntelligentEngineRequest,
        item: dict[str, Any],
        issues: list[dict[str, str]],
    ) -> list[dict[str, Any]]:
        target = str(item["target"])
        directory = str(item["directory"])
        tex_kind = str(item["tex_kind"])
        activity_number = int(item.get("activity_number") or 0)
        issue_kinds = {issue.get("kind", "") for issue in issues}
        actions: list[dict[str, Any]] = []

        if "tex-sin-memoria-directa" in issue_kinds or any(kind.startswith("memoria-") for kind in issue_kinds):
            actions.append(
                self._action(
                    "refresh-editorial-memory",
                    "Restablecer memoria editorial cercana al TEX antes de volver a revisar o compilar.",
                    [
                        ".\\scripts\\aulatex.ps1",
                        "editorial-memory",
                        "--target",
                        directory,
                        "--build-level",
                        "materia",
                        "--propagation-mode",
                        "local",
                    ],
                    blocking=False,
                )
            )

        if tex_kind == "report" and any(kind.startswith("reporte-") for kind in issue_kinds):
            command = [
                ".\\scripts\\aulatex.ps1",
                "activity-monitor",
                "--target",
                target,
                "--workflow-backend",
                request.backend,
                "--max-cycles",
                "2",
                "--compile-check",
            ]
            if activity_number > 0:
                command.extend(["--activity", str(activity_number)])
            actions.append(
                self._action(
                    "repair-report-editorially",
                    "Aplicar bucle monitorizado con heurísticas y revisiones acotadas sobre el reporte.",
                    command,
                )
            )

        if tex_kind == "presentation" and any(kind.startswith("presentacion-") for kind in issue_kinds):
            actions.append(
                self._action(
                    "plan-presentation-upgrade",
                    "Planear mejora Beamer institucional sin acoplar el motor a una escuela o script específico.",
                    [
                        ".\\scripts\\aulatex.ps1",
                        "intelligent-engine",
                        "--target",
                        directory,
                        "--backend",
                        request.backend,
                        "--no-reports",
                        "--max-targets",
                        "1",
                    ],
                    blocking=False,
                )
            )

        if "pdf-faltante" in issue_kinds or "pdf-desactualizado" in issue_kinds or not bool(item.get("pdf_exists")):
            actions.append(
                self._action(
                    "compile-target",
                    "Compilar y verificar frescura del PDF como validación final del target.",
                    [".\\scripts\\latexmk-build.ps1", target],
                    blocking=True,
                )
            )

        if not actions:
            actions.append(
                self._action(
                    "observe-only",
                    "Mantener target en cola de observación; no requiere acción inmediata en v1.",
                    [".\\scripts\\aulatex.ps1", "activity-observe", "--target", target],
                    blocking=False,
                )
            )
        return actions

    def _action(self, action_id: str, rationale: str, command: list[str], *, blocking: bool = True) -> dict[str, Any]:
        return {
            "action_id": action_id,
            "blocking": blocking,
            "rationale": rationale,
            "command": command,
        }

    def _build_architecture_contract(self, request: IntelligentEngineRequest) -> dict[str, Any]:
        return {
            "goal": "Operar campañas masivas por lotes y ciclos con priorización, memoria, LLM y validación reproducible.",
            "control_plane": {
                "runtime": "PowerShell",
                "responsibilities": [
                    "lanzar campañas",
                    "particionar lotes",
                    "coordinar compilación",
                    "publicar artefactos",
                ],
            },
            "engine_plane": {
                "runtime": "Python",
                "responsibilities": [
                    "descubrir targets",
                    "consolidar auditoría",
                    "priorizar",
                    "enrutar acciones",
                    "persistir manifiestos y reportes",
                ],
            },
            "workflow_plane": {
                "backend": request.backend,
                "responsibilities": [
                    "grafo de estados",
                    "reintentos acotados",
                    "transiciones deterministas",
                    "observabilidad por nodo",
                ],
            },
            "modules": [
                {"name": "campaign_scheduler", "status": "planned", "purpose": "segmentación de campañas y lotes"},
                {"name": "scope_inventory", "status": "available", "purpose": "inventario de scopes y TEX"},
                {"name": "audit_ingestor", "status": "available", "purpose": "consumo de audit.json y manifest previos"},
                {"name": "priority_router", "status": "scaffolded", "purpose": "ranking de targets y mapeo de acciones"},
                {"name": "execution_runner", "status": "planned", "purpose": "ejecución de acciones con checkpointing"},
                {"name": "validation_gate", "status": "planned", "purpose": "validación de diffs, compilación y score editorial"},
                {"name": "memory_retrieval", "status": "planned", "purpose": "ADN editorial relevante por target"},
                {"name": "telemetry_store", "status": "planned", "purpose": "costos, throughput, éxitos y fallos"},
            ],
            "contracts": {
                "manifest": "run manifest persistido por campaña",
                "target_plan": "lista priorizada de acciones por TEX",
                "graph_state": "estado serializable para reanudación",
            },
        }

    def _build_graph_contract(self, request: IntelligentEngineRequest) -> dict[str, Any]:
        return {
            "backend": request.backend,
            "state": {
                "run_id": "string",
                "scope_key": "string",
                "batch_id": "string",
                "queue": "list[target_plan]",
                "current_target": "string",
                "current_action": "string",
                "completed": "list[action_result]",
                "failed": "list[action_result]",
                "metrics": {
                    "issue_total_before": "int",
                    "issue_total_after": "int",
                    "pdf_fresh": "int",
                    "llm_calls": "int",
                },
                "resume_cursor": "int",
            },
            "nodes": [
                "discover",
                "ingest_audit",
                "prioritize",
                "route_action",
                "execute_memory",
                "execute_report",
                "execute_presentation",
                "compile",
                "validate",
                "promote",
                "stop",
            ],
            "transitions": [
                "discover -> ingest_audit",
                "ingest_audit -> prioritize",
                "prioritize -> route_action",
                "route_action -> execute_memory|execute_report|execute_presentation|compile",
                "execute_* -> validate",
                "validate -> promote|route_action|stop",
            ],
            "batches": {
                "strategy": "small-first",
                "recommended_batch_size": 1,
                "recommended_max_batches": 1,
            },
        }

    def _build_markdown_report(self, manifest: dict[str, Any]) -> str:
        lines = [
            "# Motor inteligente AulaTeX v1",
            "",
            f"- Run: {manifest['run_id']}",
            f"- Backend de flujo: {manifest['graph_contract']['backend']}",
            f"- Scope: {manifest['scope']['scope_key'] or manifest['scope']['target_root']}",
            f"- TEX inventariados: {manifest['inventory_summary']['tex_total']}",
            f"- Targets planificados: {manifest['inventory_summary']['planned_targets']}",
            "",
            "## Módulos v1",
        ]
        for module in manifest["architecture"]["modules"]:
            lines.append(f"- {module['name']}: {module['status']} | {module['purpose']}")
        lines.extend(["", "## Targets priorizados"])
        for target in manifest["targets"]:
            issue_kinds = ", ".join(issue["kind"] for issue in target["issues"][:6]) or "sin issues de auditoría"
            lines.append(f"- {target['target']} | score={target['priority_score']} | {issue_kinds}")
            for action in target["recommended_actions"]:
                command = " ".join(action["command"])
                lines.append(f"  - {action['action_id']}: {action['rationale']} | {command}")
        if not manifest["targets"]:
            lines.append("- No se generaron acciones; revisar filtros o aportar audit.json.")
        lines.extend(
            [
                "",
                "## Estado serializable",
                "- queue, current_target, current_action, completed, failed y metrics quedan definidos para implementar reanudación en la siguiente iteración.",
            ]
        )
        return "\n".join(lines) + "\n"

    def _detect_tex_kind(self, tex: Path) -> str:
        name = tex.name.lower()
        if name.startswith("reporte-"):
            return "report"
        if name.startswith("presentacion-"):
            return "presentation"
        return "other"

    def _extract_activity_number(self, stem: str) -> int:
        lower = stem.lower()
        marker = "actividad"
        if marker not in lower:
            return 0
        suffix = lower.split(marker, 1)[1]
        digits = "".join(char for char in suffix if char.isdigit())
        return int(digits) if digits else 0


__all__ = [
    "IntelligentEngine",
    "IntelligentEngineRequest",
    "IntelligentEngineResult",
]