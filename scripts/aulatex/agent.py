from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

from .agentic_patterns import (
    AgentTask,
    AgenticStateMachine,
    EditorialConsensusEngine,
    SharedMemory,
    build_editorial_tasks,
    pattern_catalog_markdown,
    safe_invoke,
)
from .editorial_memory import EditorialMemoryStore
from .llm_bridge import LLM_ENGINES, AulaTeXLLMClient, LLMCallResult
from .template_materializer import MaterializationResult, TemplateMaterializer
from .workspace import AulaTeXWorkspace


@dataclass
class AgentRequest:
    target: str = "."
    level: str = "materia"
    action: str = "generar-plantilla"
    activity_number: int = 1
    generation_mode: str = "direct"
    parent_scope_key: str = ""
    child_level: str = ""
    child_name: str = ""
    engines: list[str] = field(default_factory=lambda: ["Codex", "Claude Foundry", "GPT-Pro", "Auto (model-router)"])
    iterations: int = 5
    compile_tex: bool = True
    max_tokens: int = 1600
    apply_feedback: bool = False


@dataclass
class AgentRunResult:
    run_id: str
    run_dir: Path
    ok: bool
    report_path: Path
    manifest_path: Path


@dataclass(frozen=True)
class AgentTargetContext:
    target_path: Path
    context_path: Path
    scope_key: str
    display_target: str
    generation_mode: str
    parent_scope_key: str = ""
    child_level: str = ""
    child_name: str = ""
    child_preview: str = ""


class AulaTeXAgent:
    def __init__(
        self,
        workspace: AulaTeXWorkspace | None = None,
        llm_bridge: AulaTeXLLMClient | None = None,
    ) -> None:
        self.workspace = workspace or AulaTeXWorkspace()
        self.llm = llm_bridge or AulaTeXLLMClient()
        self.editorial_memory = EditorialMemoryStore(self.workspace)
        self.template_materializer = TemplateMaterializer(self.workspace)

    def run(self, request: AgentRequest) -> AgentRunResult:
        target_ctx = self._resolve_target_context(request)
        target = target_ctx.target_path
        run_id = self.workspace.timestamp()
        safe_action = request.action.lower().replace(" ", "-")
        run_dir = self.workspace.feedback_root / "runs" / f"{run_id}-{safe_action}"
        run_dir.mkdir(parents=True, exist_ok=True)

        workflow = AgenticStateMachine()
        memory = SharedMemory()
        context = self.workspace.context_summary(target_ctx.context_path)
        if target_ctx.generation_mode == "downward":
            context += (
                "\n\n## Generacion descendente\n"
                f"- Padre seleccionado: {target_ctx.parent_scope_key}\n"
                f"- Nivel hijo: {target_ctx.child_level}\n"
                f"- Hijo solicitado: {target_ctx.child_name or f'Actividad {request.activity_number}'}\n"
                f"- Vista previa: {target_ctx.child_preview or 'Pendiente de definir'}\n"
                "- Regla: reutiliza memoria editorial ascendente del padre y genera hacia abajo sin asumir que el hijo exista ya.\n"
            )
        if target_ctx.scope_key:
            memory_context = self.editorial_memory.summarize_for_scope(target_ctx.scope_key, include_ancestors=True, max_chars=6000)
            if memory_context.strip():
                context += "\n\n## Memoria editorial persistente\n" + memory_context
        base_tasks = build_editorial_tasks(request, context, memory)
        selected_tasks = base_tasks[: max(1, min(request.iterations, len(base_tasks)))]
        engines = self._normalize_engines(request.engines)
        stage_results: list[LLMCallResult] = []

        for index, _task in enumerate(selected_tasks, start=1):
            task = build_editorial_tasks(request, context, memory)[index - 1]
            engine = engines[(index - 1) % len(engines)]
            workflow.record("llm-start", "ok", f"{task.stage}: {task.role} via {engine}")
            result = self.llm.call(engine, task.prompt, max_tokens=request.max_tokens)
            stage_results.append(result)
            if result.ok:
                memory.remember("proposal" if task.stage in {"planificar", "generar"} else "risk", result.text[:900])
                workflow.record("llm-end", "ok", f"{task.stage}: {len(result.text)} chars")
            else:
                memory.remember("risk", f"{task.stage} fallo con {result.engine}: {result.error}")
                workflow.record("llm-end", "error", f"{task.stage}: {result.error}")
            if task.stage == "planificar":
                workflow.transition("planned", "plan editorial producido")
            elif task.stage == "investigar":
                workflow.transition("researched", "diagnostico documental producido")
            elif task.stage == "generar":
                workflow.transition("generated", "propuesta editorial producida")

        for index, (task, result) in enumerate(zip(selected_tasks, stage_results), start=1):
            stage_path = run_dir / f"stage-{index:02d}-{task.stage}.md"
            stage_path.write_text(self._format_stage(result, task), encoding="utf-8")

        materialization_result: MaterializationResult | None = None
        if self._should_materialize_template(request, target_ctx):
            workflow.record("materialize-start", "ok", "generar-plantilla materializara estructura canonica de archivos")
            materialization_result = self.template_materializer.materialize_subject(
                target_ctx.target_path,
                activity_number=request.activity_number,
                force=True,
            )
            workflow.record(
                "materialize-end",
                "ok" if materialization_result.ok else "error",
                f"{len(materialization_result.artifacts)} artefactos procesados",
            )

        compile_results = []
        if request.compile_tex:
            workflow.record("tool-select", "ok", "latexmk-build.ps1 seleccionado para compilar objetivos canonicos")
            for tex in self._select_compile_targets(target_ctx):
                invocation = safe_invoke(self.workspace.compile_tex, tex, clean_mode="safe")
                if invocation.ok:
                    build = invocation.result
                    ok = bool(build.ok)
                    returncode = int(build.returncode)
                    stdout = build.stdout
                    stderr = build.stderr
                else:
                    ok = False
                    returncode = 1
                    stdout = ""
                    stderr = invocation.error
                compile_results.append(
                    {
                        "tex": self.workspace.relative(tex),
                        "ok": ok,
                        "returncode": returncode,
                        "stdout_tail": stdout[-3000:],
                        "stderr_tail": stderr[-3000:],
                    }
                )
                log_path = run_dir / f"compile-{tex.stem}.log.txt"
                log_path.write_text(stdout + "\n" + stderr, encoding="utf-8")
                workflow.record("tool-result", "ok" if ok else "error", f"{self.workspace.relative(tex)} rc={returncode}")
            if workflow.state == "generated":
                workflow.transition("compiled", "compilacion latexmk ejecutada")

        consensus = EditorialConsensusEngine().evaluate(selected_tasks, stage_results)
        workflow.record("consensus", "ok" if consensus.passed else "warn", f"score={consensus.consensus_score:.2f}")
        if workflow.state in {"planned", "researched", "generated", "compiled"}:
            workflow.transition("evaluated", "validacion y consenso completados")
        workflow.transition("finalized", "ciclo agentico cerrado")

        workflow_path = run_dir / "workflow-trace.md"
        workflow_path.write_text(workflow.to_markdown(), encoding="utf-8")
        memory_path = run_dir / "shared-memory.md"
        memory_path.write_text("# Memoria compartida AulaTeX\n\n" + memory.summary(max_chars=12000), encoding="utf-8")
        patterns_path = run_dir / "agentic-patterns.md"
        patterns_path.write_text(pattern_catalog_markdown(), encoding="utf-8")

        manifest = {
            "run_id": run_id,
            "target": self.workspace.relative(target),
            "display_target": target_ctx.display_target,
            "level": request.level,
            "action": request.action,
            "activity_number": request.activity_number,
            "generation_mode": request.generation_mode,
            "parent_scope_key": request.parent_scope_key,
            "child_level": request.child_level,
            "child_name": request.child_name,
            "child_preview": target_ctx.child_preview,
            "engines": engines,
            "agentic_patterns": [
                "planning-memory",
                "tool-using-workflow",
                "verification-validation",
                "collective-consensus",
            ],
            "tasks": [
                {
                    "stage": task.stage,
                    "role": task.role,
                    "mission": task.mission,
                    "engine": stage_results[index].engine if index < len(stage_results) else "",
                }
                for index, task in enumerate(selected_tasks)
            ],
            "llm_results": [
                {"engine": r.engine, "ok": r.ok, "error": r.error, "chars": len(r.text)}
                for r in stage_results
            ],
            "compile_results": compile_results,
            "materialization": self._materialization_manifest(materialization_result),
            "consensus": consensus.as_dict(),
            "workflow_events": workflow.as_dicts(),
        }
        manifest_path = run_dir / "manifest.json"
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

        report_path = run_dir / "reporte-aulatex.md"
        report_path.write_text(
            self._build_report(request, target_ctx, selected_tasks, stage_results, compile_results, consensus),
            encoding="utf-8",
        )
        if materialization_result is not None:
            report_path.write_text(
                report_path.read_text(encoding="utf-8")
                + "\n"
                + self._render_materialization_report(materialization_result),
                encoding="utf-8",
            )
        self.workspace.append_bitacora(run_id, request.action, manifest)

        if request.apply_feedback:
            self._write_target_feedback(target, report_path)

        ok = all(r.ok for r in stage_results) and all(item.get("ok") for item in compile_results or [{"ok": True}])
        ok = ok and consensus.passed
        if materialization_result is not None:
            ok = ok and materialization_result.ok
        return AgentRunResult(run_id, run_dir, ok, report_path, manifest_path)

    def _build_prompts(self, request: AgentRequest, context: str) -> list[str]:
        base = (
            "Eres AulaTeX, agente editorial academico para plantillas LaTeX institucionales. "
            "Trabaja en espanol academico, con criterio editorial, trazabilidad, enfoque institucional "
            "y salida accionable. No inventes fuentes; si falta informacion, marca supuestos.\n\n"
            f"Nivel: {request.level}\n"
            f"Accion: {request.action}\n"
            f"Actividad: {request.activity_number}\n\n"
            f"Contexto local:\n{context}\n"
        )
        research = (
            base
            + "\nTAREA 1 INVESTIGAR: diagnostica el estado editorial del objetivo. "
            "Identifica identidad institucional, estructura, bibliografia, faltantes, riesgos de compilacion "
            "y oportunidades de mejora. Devuelve hallazgos priorizados."
        )
        generate = (
            base
            + "\nTAREA 2 GENERAR: propone la plantilla o actividad solicitada. "
            "Incluye estructura para reporte y presentacion cuando aplique, pauta de realizacion, "
            "bibliografia local y criterios de revision. Entrega bloques listos para convertir a archivos."
        )
        evaluate = (
            base
            + "\nTAREA 3 EVALUAR: revisa la propuesta como editor severo. "
            "Devuelve checklist, pruebas de compilacion recomendadas, riesgos, criterios de aceptacion "
            "y siguiente ciclo incremental investigar-compilar-evaluar."
        )
        return [research, generate, evaluate]

    def _normalize_engines(self, engines: list[str]) -> list[str]:
        allowed = set(self.llm.engines() or LLM_ENGINES)
        out = [engine for engine in engines if engine in allowed]
        return out or ["Codex", "Claude Foundry"]

    def _resolve_target_context(self, request: AgentRequest) -> AgentTargetContext:
        target = self.workspace.resolve_target(request.target)
        if request.generation_mode != "downward":
            scope = self.workspace.find_scope_for_target(target, activity_number=request.activity_number)
            return AgentTargetContext(
                target_path=target,
                context_path=target,
                scope_key=scope.key if scope is not None else "",
                display_target=self.workspace.relative(target),
                generation_mode="direct",
            )

        by_key, _children = self.workspace.editorial_scope_index()
        parent_scope = by_key.get(request.parent_scope_key)
        if parent_scope is None:
            raise ValueError("No se pudo resolver el padre editorial para la generacion descendente.")

        parent_path = self.workspace.resolve_target(parent_scope.relative_path)
        child_name = request.child_name.strip() if request.child_name.strip() else f"Actividad {request.activity_number}"
        child_preview = self._preview_child(parent_scope, request.child_level, child_name, request.activity_number)
        return AgentTargetContext(
            target_path=parent_path,
            context_path=parent_path,
            scope_key=parent_scope.key,
            display_target=f"{parent_scope.key} -> {request.child_level}:{child_name}",
            generation_mode="downward",
            parent_scope_key=parent_scope.key,
            child_level=request.child_level,
            child_name=child_name,
            child_preview=child_preview,
        )

    def _preview_child(self, parent_scope, child_level: str, child_name: str, activity_number: int) -> str:
        parent_rel = parent_scope.relative_path.rstrip("/")
        if child_level == "actividad":
            return f"{parent_rel} :: reporte-{parent_scope.label}-Actividad-{activity_number}.tex"
        slug = child_name.strip().lower().replace(" ", "-")
        return f"{parent_rel}/{slug}"

    def _select_compile_targets(self, target_ctx: AgentTargetContext) -> list[Path]:
        if target_ctx.generation_mode == "downward":
            return []
        tex_files = self.workspace.find_tex_files(target_ctx.target_path, limit=30)
        reports = [p for p in tex_files if p.name.startswith("reporte-")]
        presentations = [p for p in tex_files if p.name.startswith("presentacion-")]
        selected = reports[:1] + presentations[:1]
        return selected or tex_files[:1]

    def _should_materialize_template(self, request: AgentRequest, target_ctx: AgentTargetContext) -> bool:
        return (
            request.action.strip().lower() == "generar-plantilla"
            and target_ctx.generation_mode == "direct"
            and request.level in {"materia", "actividad"}
        )

    def _materialization_manifest(self, result: MaterializationResult | None) -> dict:
        if result is None:
            return {"enabled": False}
        return {
            "enabled": True,
            "ok": result.ok,
            "target_dir": self.workspace.relative(result.target_dir),
            "artifacts": [self.workspace.relative(path) for path in result.artifacts],
            "notes": list(result.notes),
        }

    def _render_materialization_report(self, result: MaterializationResult) -> str:
        lines = [
            "## Materializacion de plantilla",
            "",
            f"- Estado: {'OK' if result.ok else 'CON OBSERVACIONES'}",
            f"- Carpeta: `{self.workspace.relative(result.target_dir)}`",
            "",
            "### Artefactos",
        ]
        lines.extend(f"- `{self.workspace.relative(path)}`" for path in result.artifacts)
        lines.append("")
        return "\n".join(lines)

    def _format_stage(self, result: LLMCallResult, task: AgentTask) -> str:
        status = "ok" if result.ok else "error"
        body = result.text if result.ok else result.error
        return (
            "# AulaTeX stage\n\n"
            f"- Etapa: {task.stage}\n"
            f"- Rol: {task.role}\n"
            f"- Mision: {task.mission}\n"
            f"- Motor: {result.engine}\n"
            f"- Estado: {status}\n\n"
            f"{body}\n"
        )

    def _build_report(
        self,
        request: AgentRequest,
        target_ctx: AgentTargetContext,
        tasks: list[AgentTask],
        stage_results: list[LLMCallResult],
        compile_results: list[dict],
        consensus,
    ) -> str:
        lines = [
            "# Reporte AulaTeX",
            "",
            f"- Objetivo: `{target_ctx.display_target}`",
            f"- Nivel: {request.level}",
            f"- Accion: {request.action}",
            f"- Actividad: {request.activity_number}",
            "",
            "## Arquitectura agentica",
            "",
            "- Planificacion con memoria compartida",
            "- Uso de herramientas con invocacion segura",
            "- Flujo con maquina de estados y auditoria",
            "- Verificacion/validacion editorial",
            "- Consenso multiagente con critico adversarial",
            "",
            "## Contexto de ejecucion",
            "",
            f"- Modo de generacion: {request.generation_mode}",
            f"- Padre editorial: {target_ctx.parent_scope_key or 'N/A'}",
            f"- Nivel hijo: {target_ctx.child_level or 'N/A'}",
            f"- Hijo solicitado: {target_ctx.child_name or 'N/A'}",
            f"- Vista previa: {target_ctx.child_preview or 'N/A'}",
            "",
            "## Ciclo LLM",
            "",
        ]
        for index, (task, result) in enumerate(zip(tasks, stage_results), start=1):
            lines.append(f"### {index}. {task.stage} - {task.role} - {result.engine}")
            lines.append("")
            lines.append(result.text if result.ok else f"ERROR: {result.error}")
            lines.append("")
        lines.append(consensus.to_markdown())
        lines.extend(["## Compilacion", ""])
        if compile_results:
            for item in compile_results:
                lines.append(f"- {item['tex']}: {'OK' if item['ok'] else 'ERROR'} ({item['returncode']})")
        else:
            lines.append("- No se compilaron archivos en este ciclo.")
        lines.append("")
        return "\n".join(lines)

    def _write_target_feedback(self, target: Path, report_path: Path) -> None:
        if target.is_file():
            target = target.parent
        feedback_dir = target / "retroalimentacion-aulatex"
        feedback_dir.mkdir(parents=True, exist_ok=True)
        dest = feedback_dir / report_path.name
        dest.write_text(report_path.read_text(encoding="utf-8"), encoding="utf-8")
