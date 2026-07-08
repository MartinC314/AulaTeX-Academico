from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

from .activity_monitor import ActivityMonitor, ActivityMonitorRequest
from .activity_observer import ActivityObservationRequest, ActivityObserver
from .activity_revision import ActivityRevisionRequest, ActivityReviser
from .agent import AgentRequest, AulaTeXAgent
from .agentic_patterns import pattern_catalog_markdown
from .bibliography_repair import BibliographyRepairer, BibliographyRepairRequest
from .compilation_repair import CompilationRepairRequest, CompilationRepairer
from .config import credential_status, load_aulatex_env
from .construction import ConstructionBuilder, ConstructionRequest
from .editorial_memory import EDITORIAL_LEVELS, EditorialMemoryBuilder, EditorialMemoryRequest
from .extractor_adapter import EXTRACTOR_MOTORS, ExtractorAdapter, ExtractorRequest
from .gui import main as gui_main
from .intelligent_engine import IntelligentEngine, IntelligentEngineRequest
from .investigation import InvestigationBuilder, InvestigationRequest
from .llm_bridge import DEFAULT_MAX_TOKENS, DEFAULT_TIMEOUT_SECONDS, LLM_ENGINES, AulaTeXLLMClient
from .workspace import AulaTeXWorkspace


def _editorial_checkpoint_root(workspace: AulaTeXWorkspace) -> Path:
    root = workspace.temp_root / "editorial-memory" / "checkpoints"
    root.mkdir(parents=True, exist_ok=True)
    return root


def _default_editorial_checkpoint_name(scope_key: str, build_level: str, propagation_mode: str) -> str:
    safe_scope = scope_key.replace("/", "__").replace("\\", "__")
    return f"{safe_scope}--{build_level}--{propagation_mode}.json"


def _resolve_editorial_checkpoint_path(
    workspace: AulaTeXWorkspace,
    checkpoint_ref: str,
    *,
    scope_key: str,
    build_level: str,
    propagation_mode: str,
) -> Path:
    root = _editorial_checkpoint_root(workspace)
    if checkpoint_ref:
        candidate = Path(checkpoint_ref)
        if candidate.is_absolute() or candidate.parent != Path("."):
            return candidate
        name = candidate.name if candidate.suffix == ".json" else f"{candidate.name}.json"
        return root / name
    return root / _default_editorial_checkpoint_name(scope_key, build_level, propagation_mode)


def _write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def _read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="aulatex", description="AulaTeX GUI and agentic editorial workflow.")
    sub = parser.add_subparsers(dest="command")

    gui = sub.add_parser("gui", help="Open the AulaTeX GUI.")
    gui.add_argument("--diagnostics", action="store_true", help="Enable diagnostic metrics and performance views.")
    sub.add_parser("agent-patterns", help="List the agentic patterns integrated in AulaTeX.")

    env_cmd = sub.add_parser("llm-env", help="Show AulaTeX LLM credential status without secrets.")

    check = sub.add_parser("llm-check", help="Check configured AulaTeX LLM engines.")
    check.add_argument("--engine", action="append", choices=LLM_ENGINES)

    prompt = sub.add_parser("llm-prompt", help="Run one prompt through one LLM engine.")
    prompt.add_argument("prompt")
    prompt.add_argument("--engine", default="Codex", choices=LLM_ENGINES)
    prompt.add_argument("--max-tokens", type=int, default=DEFAULT_MAX_TOKENS)
    prompt.add_argument("--timeout-seconds", type=int, default=DEFAULT_TIMEOUT_SECONDS)

    agent = sub.add_parser("agent", help="Run an incremental AulaTeX agent cycle.")
    agent.add_argument("--target", default=".")
    agent.add_argument("--level", default="materia", choices=("interinstitucional", "institucion", "carrera", "materia", "actividad"))
    agent.add_argument("--action", default="generar-plantilla")
    agent.add_argument("--activity", type=int, default=1)
    agent.add_argument("--generation-mode", default="direct", choices=("direct", "downward"))
    agent.add_argument("--parent-scope-key", default="")
    agent.add_argument("--child-level", default="")
    agent.add_argument("--child-name", default="")
    agent.add_argument("--engine", action="append", choices=LLM_ENGINES)
    agent.add_argument("--iterations", type=int, default=5)
    agent.add_argument("--cycle-mode", default="stages", choices=("stages", "full"), help="stages=1..5 etapas; full=N ciclos completos de todos los roles.")
    agent.add_argument("--no-compile", action="store_true")
    agent.add_argument("--apply-feedback", action="store_true")
    agent.add_argument("--run-extractor", action="store_true", help="Force run-extractor inside the agent cycle.")
    agent.add_argument("--no-extractor", action="store_true", help="Disable automatic extractor for generar/realizar actividad.")
    agent.add_argument("--extractor-probe", action="store_true", help="Run extractor adapter in probe/configuration mode.")
    agent.add_argument("--extractor-fuentes", default="")
    agent.add_argument("--extractor-planeacion", default="")
    agent.add_argument("--extractor-conceptos", default="")
    agent.add_argument("--extractor-salida", default="")
    agent.add_argument("--extractor-motor", default="anthropicfoundry", choices=EXTRACTOR_MOTORS)

    editorial = sub.add_parser("editorial-memory", help="Build persistent editorial memory from a selected scope.")
    editorial.add_argument("--target", default=".")
    editorial.add_argument("--activity", type=int, default=0)
    editorial.add_argument("--build-level", default="materia", choices=EDITORIAL_LEVELS)
    editorial.add_argument("--propagation-mode", default="ascendente", choices=("local", "ascendente", "ascendente-exhaustivo", "recursivo"))
    editorial.add_argument("--engine", action="append", choices=LLM_ENGINES)
    editorial.add_argument("--iterations", type=int, default=2)
    editorial.add_argument("--max-tokens", type=int, default=DEFAULT_MAX_TOKENS)
    editorial.add_argument("--timeout-seconds", type=int, default=DEFAULT_TIMEOUT_SECONDS)
    editorial.add_argument("--scope-offset", type=int, default=0)
    editorial.add_argument("--scope-limit", type=int, default=0)
    editorial.add_argument("--batch-size", type=int, default=0)
    editorial.add_argument("--max-batches", type=int, default=0)
    editorial.add_argument("--checkpoint", default="")
    editorial.add_argument("--resume-checkpoint", default="")

    investigation = sub.add_parser("investigation", help="Consolidate the knowledge base before extractor: local context, web sources and bibliography.")
    investigation.add_argument("--target", default=".")
    investigation.add_argument("--activity", type=int, default=0)
    investigation.add_argument("--engine", action="append", choices=LLM_ENGINES)
    investigation.add_argument("--iterations", type=int, default=2)
    investigation.add_argument("--max-tokens", type=int, default=DEFAULT_MAX_TOKENS)
    investigation.add_argument("--query", action="append", default=[])
    investigation.add_argument("--url", action="append", default=[])

    extractor = sub.add_parser("extractor", help="Run the concept extractor through the structured AulaTeX adapter.")
    extractor.add_argument("--target", default=".")
    extractor.add_argument("--activity", type=int, default=0)
    extractor.add_argument("--fuentes", default="")
    extractor.add_argument("--planeacion", default="")
    extractor.add_argument("--conceptos", default="")
    extractor.add_argument("--salida", default="")
    extractor.add_argument("--motor", default="anthropicfoundry", choices=EXTRACTOR_MOTORS)
    extractor.add_argument("--top-k", type=int, default=12)
    extractor.add_argument("--max-citas", type=int, default=8)
    extractor.add_argument("--recursivo", action=argparse.BooleanOptionalAction, default=True)
    extractor.add_argument("--probe", action="store_true")
    extractor.add_argument("--preview", action="store_true")
    extractor.add_argument("--timeout-seconds", type=int, default=3600)

    activity_observe = sub.add_parser("activity-observe", help="Observe and evaluate an activity without modifying source files.")
    activity_observe.add_argument("--target", required=True)
    activity_observe.add_argument("--activity", type=int, default=1)
    activity_observe.add_argument("--output", default="")
    activity_observe.add_argument("--compile-check", action="store_true")

    activity_monitor = sub.add_parser("activity-monitor", help="Run a monitored recursive activity loop with bounded retries.")
    activity_monitor.add_argument("--target", required=True)
    activity_monitor.add_argument("--activity", type=int, default=1)
    activity_monitor.add_argument("--output", default="")
    activity_monitor.add_argument("--max-cycles", type=int, default=2)
    activity_monitor.add_argument("--compile-check", action="store_true")
    activity_monitor.add_argument("--run-extractor", action="store_true")
    activity_monitor.add_argument("--extractor-motor", action="append", choices=EXTRACTOR_MOTORS)
    activity_monitor.add_argument("--apply-bibliography-repair", action="store_true")
    activity_monitor.add_argument("--no-apply-revision-patches", action="store_true")
    activity_monitor.add_argument("--no-bibliography-backup", action="store_true")
    activity_monitor.add_argument("--no-revision-backup", action="store_true")
    activity_monitor.add_argument("--keep-going", action="store_true")
    activity_monitor.add_argument("--workflow-backend", default="langgraph", choices=("langgraph", "classic"))

    activity_revise = sub.add_parser("activity-revise", help="Build a structured revision plan for an activity.")
    activity_revise.add_argument("--target", required=True)
    activity_revise.add_argument("--activity", type=int, default=1)
    activity_revise.add_argument("--output", default="")
    activity_revise.add_argument("--apply", action="store_true")
    activity_revise.add_argument("--no-backup", action="store_true")
    activity_revise.add_argument("--workflow-backend", default="langgraph", choices=("langgraph", "classic"))

    compilation_repair = sub.add_parser("compilation-repair", help="Attempt bounded compilation repair for an activity TEX.")
    compilation_repair.add_argument("--target", required=True)
    compilation_repair.add_argument("--activity", type=int, default=1)
    compilation_repair.add_argument("--output", default="")

    bib_repair = sub.add_parser("bibliography-repair", help="Plan or apply bibliography key repairs for an activity.")
    bib_repair.add_argument("--target", required=True)
    bib_repair.add_argument("--activity", type=int, default=1)
    bib_repair.add_argument("--output", default="")
    bib_repair.add_argument("--apply", action="store_true")
    bib_repair.add_argument("--no-backup", action="store_true")
    bib_repair.add_argument("--min-confidence", type=float, default=0.72)
    bib_repair.add_argument("--workflow-backend", default="langgraph", choices=("langgraph", "classic"))

    generation = sub.add_parser("generation", help="Create or reinforce an editorial node with foundational memory, plan and maqueta.")
    generation.add_argument("--parent-scope-key", default="interinstitucional")
    generation.add_argument("--node-level", required=True, choices=("institucion", "carrera", "materia", "actividad"))
    generation.add_argument("--node-name", required=True)
    generation.add_argument("--activity", type=int, default=1)
    generation.add_argument("--mode", default="crear", choices=("crear", "reforzar"))
    generation.add_argument("--destination", default="")
    generation.add_argument("--ingest-text", default="")
    generation.add_argument("--ingest-document", default="")
    generation.add_argument("--engine", action="append", choices=LLM_ENGINES)
    generation.add_argument("--iterations", type=int, default=2)
    generation.add_argument("--max-tokens", type=int, default=DEFAULT_MAX_TOKENS)

    intelligent_engine = sub.add_parser("intelligent-engine", help="Plan a resumable bulk editorial campaign over the current workspace.")
    intelligent_engine.add_argument("--target", default=".")
    intelligent_engine.add_argument("--activity", type=int, default=0)
    intelligent_engine.add_argument("--output", default="")
    intelligent_engine.add_argument("--backend", default="langgraph", choices=("langgraph", "classic"))
    intelligent_engine.add_argument("--max-targets", type=int, default=12)
    intelligent_engine.add_argument("--audit", default="")
    intelligent_engine.add_argument("--no-reports", action="store_true")
    intelligent_engine.add_argument("--no-presentations", action="store_true")
    intelligent_engine.add_argument("--engine", action="append", choices=LLM_ENGINES)

    compile_cmd = sub.add_parser("compile", help="Compile a TeX file with the shared latexmk wrapper.")
    compile_cmd.add_argument("tex")

    return parser


def main(argv: list[str] | None = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)

    if bool(getattr(args, "diagnostics", False)):
        os.environ["AULATEX_ENABLE_DIAGNOSTIC_METRICS"] = "1"

    if args.command in (None, "gui"):
        gui_main(diagnostics_enabled=bool(getattr(args, "diagnostics", False)))
        return

    if args.command == "agent-patterns":
        print(pattern_catalog_markdown())
        return

    if args.command == "llm-env":
        env_result = load_aulatex_env()
        print(f"env: {'OK' if env_result.exists else 'MISSING'} {env_result.path}")
        for status in credential_status():
            marker = "OK" if status.ok else "FALTAN"
            missing = ", ".join(status.missing) if status.missing else "-"
            print(f"{status.engine}: {marker} missing={missing}")
        return

    if args.command == "llm-check":
        bridge = AulaTeXLLMClient()
        engines = args.engine or list(bridge.engines())
        for engine in engines:
            result = bridge.check(engine)
            print(f"{result.engine}: {'OK' if result.ok else 'ERROR'} {result.text or result.error}")
        return

    if args.command == "llm-prompt":
        result = AulaTeXLLMClient().call(
            args.engine,
            args.prompt,
            max_tokens=args.max_tokens,
            timeout_seconds=args.timeout_seconds,
        )
        if not result.ok:
            raise SystemExit(f"{result.engine}: {result.error}")
        print(result.text)
        return

    if args.command == "agent":
        request = AgentRequest(
            target=args.target,
            level=args.level,
            action=args.action,
            activity_number=args.activity,
            generation_mode=args.generation_mode,
            parent_scope_key=args.parent_scope_key,
            child_level=args.child_level,
            child_name=args.child_name,
            engines=args.engine or ["Codex", "Claude Foundry", "GPT-Pro", "Auto (model-router)"],
            iterations=args.iterations,
            cycle_mode=args.cycle_mode,
            compile_tex=not args.no_compile,
            apply_feedback=args.apply_feedback,
            run_extractor=bool(args.run_extractor),
            skip_extractor=bool(args.no_extractor),
            extractor_probe_only=bool(args.extractor_probe),
            extractor_fuentes=args.extractor_fuentes,
            extractor_planeacion=args.extractor_planeacion,
            extractor_conceptos=args.extractor_conceptos,
            extractor_salida=args.extractor_salida,
            extractor_motor=args.extractor_motor,
        )
        result = AulaTeXAgent().run(request)
        print(json.dumps({"ok": result.ok, "run_dir": str(result.run_dir), "report": str(result.report_path)}, indent=2))
        return

    if args.command == "editorial-memory":
        workspace = AulaTeXWorkspace()
        scope = workspace.find_scope_for_target(args.target, activity_number=args.activity or None)
        if scope is None:
            raise SystemExit(f"No se pudo resolver un scope editorial para: {args.target}")
        builder = EditorialMemoryBuilder(workspace=workspace, llm_bridge=AulaTeXLLMClient())
        request = EditorialMemoryRequest(
            source_scope_key=scope.key,
            build_level=args.build_level,
            propagation_mode=args.propagation_mode,
            iterations=args.iterations,
            engines=args.engine or ["Codex", "Claude Foundry", "GPT-Pro"],
            max_tokens=args.max_tokens,
            timeout_seconds=args.timeout_seconds,
            scope_offset=args.scope_offset,
            scope_limit=args.scope_limit,
        )

        if args.batch_size > 0 or args.resume_checkpoint:
            full_plan = builder.plan_scopes(scope.key, args.build_level, args.propagation_mode)
            if not full_plan:
                raise SystemExit("No se pudo calcular el plan editorial para la corrida por lotes.")

            checkpoint_path = _resolve_editorial_checkpoint_path(
                workspace,
                args.resume_checkpoint or args.checkpoint,
                scope_key=scope.key,
                build_level=args.build_level,
                propagation_mode=args.propagation_mode,
            )
            start_offset = max(0, int(args.scope_offset))
            end_offset = len(full_plan)
            if args.scope_limit > 0:
                end_offset = min(len(full_plan), start_offset + int(args.scope_limit))
            batch_size = max(1, int(args.batch_size or 1))

            checkpoint_payload: dict
            if args.resume_checkpoint:
                if not checkpoint_path.exists():
                    raise SystemExit(f"Checkpoint no encontrado: {checkpoint_path}")
                checkpoint_payload = _read_json(checkpoint_path)
                if checkpoint_payload.get("source_scope_key") != scope.key:
                    raise SystemExit("El checkpoint no corresponde al scope editorial solicitado.")
                start_offset = max(start_offset, int(checkpoint_payload.get("next_scope_offset", start_offset)))
                end_offset = min(end_offset, int(checkpoint_payload.get("end_scope_offset", end_offset)))
                batch_size = max(1, int(checkpoint_payload.get("batch_size", batch_size)))
            else:
                checkpoint_payload = {
                    "mode": "editorial-memory-batch",
                    "status": "running",
                    "source_scope_key": scope.key,
                    "build_level": args.build_level,
                    "propagation_mode": args.propagation_mode,
                    "iterations": int(args.iterations),
                    "engines": request.engines,
                    "max_tokens": int(args.max_tokens),
                    "timeout_seconds": int(args.timeout_seconds),
                    "plan_scope_count": len(full_plan),
                    "start_scope_offset": start_offset,
                    "end_scope_offset": end_offset,
                    "next_scope_offset": start_offset,
                    "batch_size": batch_size,
                    "checkpoint_path": str(checkpoint_path),
                    "batches": [],
                }
                _write_json(checkpoint_path, checkpoint_payload)

            if start_offset >= end_offset:
                checkpoint_payload["status"] = "completed"
                checkpoint_payload["next_scope_offset"] = end_offset
                _write_json(checkpoint_path, checkpoint_payload)
                print(
                    json.dumps(
                        {
                            "ok": True,
                            "completed": True,
                            "checkpoint": str(checkpoint_path),
                            "processed_scopes": 0,
                            "next_scope_offset": end_offset,
                        },
                        ensure_ascii=False,
                        indent=2,
                    )
                )
                return

            offset = start_offset
            last_result = None
            executed_batches = 0
            while offset < end_offset:
                if args.max_batches > 0 and executed_batches >= int(args.max_batches):
                    checkpoint_payload["status"] = "paused"
                    break
                current_limit = min(batch_size, end_offset - offset)
                batch_request = EditorialMemoryRequest(
                    source_scope_key=scope.key,
                    build_level=args.build_level,
                    propagation_mode=args.propagation_mode,
                    iterations=args.iterations,
                    engines=request.engines,
                    max_tokens=args.max_tokens,
                    timeout_seconds=args.timeout_seconds,
                    scope_offset=offset,
                    scope_limit=current_limit,
                )
                result = builder.build(batch_request)
                processed_scopes = len(result.built_scopes)
                next_offset = offset + processed_scopes
                checkpoint_payload["batches"].append(
                    {
                        "scope_offset": offset,
                        "scope_limit": current_limit,
                        "processed_scopes": processed_scopes,
                        "ok": result.ok,
                        "cancelled": result.cancelled,
                        "run_dir": str(result.run_dir),
                        "manifest": str(result.manifest_path),
                    }
                )
                checkpoint_payload["next_scope_offset"] = next_offset
                checkpoint_payload["last_run_dir"] = str(result.run_dir)
                checkpoint_payload["last_manifest"] = str(result.manifest_path)
                checkpoint_payload["status"] = "running" if result.ok and not result.cancelled else "stopped"
                _write_json(checkpoint_path, checkpoint_payload)
                last_result = result
                executed_batches += 1
                if not result.ok or result.cancelled or processed_scopes <= 0:
                    break
                offset = next_offset

            finished = int(checkpoint_payload.get("next_scope_offset", start_offset)) >= end_offset
            checkpoint_payload["status"] = "completed" if finished else checkpoint_payload.get("status", "stopped")
            _write_json(checkpoint_path, checkpoint_payload)
            print(
                json.dumps(
                    {
                        "ok": bool(finished and last_result is not None and last_result.ok),
                        "completed": finished,
                        "checkpoint": str(checkpoint_path),
                        "next_scope_offset": checkpoint_payload["next_scope_offset"],
                        "end_scope_offset": end_offset,
                        "batch_size": batch_size,
                        "batches_executed": len(checkpoint_payload["batches"]),
                        "last_run_dir": checkpoint_payload.get("last_run_dir", ""),
                        "last_manifest": checkpoint_payload.get("last_manifest", ""),
                    },
                    ensure_ascii=False,
                    indent=2,
                )
            )
            return

        result = builder.build(request)
        print(
            json.dumps(
                {
                    "ok": result.ok,
                    "run_dir": str(result.run_dir),
                    "manifest": str(result.manifest_path),
                    "built_scopes": list(result.built_scopes),
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return

    if args.command == "extractor":
        adapter = ExtractorAdapter(AulaTeXWorkspace())
        request = ExtractorRequest(
            target=args.target,
            activity_number=args.activity,
            fuentes=args.fuentes,
            planeacion=args.planeacion,
            conceptos=args.conceptos,
            salida=args.salida,
            motor=args.motor,
            recursive=bool(args.recursivo),
            top_k=args.top_k,
            max_citas=args.max_citas,
            probe_only=bool(args.probe),
            timeout_seconds=args.timeout_seconds,
        )
        if args.preview:
            print(adapter.preview_markdown(request))
            return
        result = adapter.run(request)
        print(
            json.dumps(
                {
                    "ok": result.ok,
                    "run_dir": str(result.run_dir),
                    "manifest": str(result.manifest_path),
                    "output_dir": str(result.output_dir),
                    "stdout": str(result.stdout_path),
                    "stderr": str(result.stderr_path),
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return

    if args.command == "activity-observe":
        result = ActivityObserver(AulaTeXWorkspace()).observe(
            ActivityObservationRequest(
                target=args.target,
                activity_number=args.activity,
                output=args.output,
                compile_check=bool(args.compile_check),
            )
        )
        print(
            json.dumps(
                {
                    "ok": result.ok,
                    "run_dir": str(result.run_dir),
                    "state": str(result.state_path),
                    "evaluation": str(result.evaluation_path),
                    "actions": str(result.actions_path),
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return

    if args.command == "activity-monitor":
        result = ActivityMonitor(AulaTeXWorkspace()).run(
            ActivityMonitorRequest(
                target=args.target,
                activity_number=args.activity,
                output=args.output,
                max_cycles=args.max_cycles,
                compile_check=bool(args.compile_check),
                run_extractor=bool(args.run_extractor),
                extractor_motors=tuple(args.extractor_motor or ["anthropicfoundry", "tfidf"]),
                apply_bibliography_repair=bool(args.apply_bibliography_repair),
                apply_revision_patches=not bool(args.no_apply_revision_patches),
                backup_bibliography=not bool(args.no_bibliography_backup),
                backup_revision=not bool(args.no_revision_backup),
                stop_on_blocker=not bool(args.keep_going),
                workflow_backend=args.workflow_backend,
            )
        )
        print(
            json.dumps(
                {
                    "ok": result.ok,
                    "run_dir": str(result.run_dir),
                    "manifest": str(result.manifest_path),
                    "report": str(result.report_path),
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return

    if args.command == "activity-revise":
        result = ActivityReviser(AulaTeXWorkspace()).revise(
            ActivityRevisionRequest(
                target=args.target,
                activity_number=args.activity,
                output=args.output,
                apply=bool(args.apply),
                backup=not bool(args.no_backup),
                workflow_backend=args.workflow_backend,
            )
        )
        print(
            json.dumps(
                {
                    "ok": result.ok,
                    "run_dir": str(result.run_dir),
                    "plan": str(result.plan_path),
                    "report": str(result.report_path),
                    "patched_tex": str(result.patched_tex_path) if result.patched_tex_path else "",
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return

    if args.command == "compilation-repair":
        result = CompilationRepairer(AulaTeXWorkspace()).repair(
            CompilationRepairRequest(
                target=args.target,
                activity_number=args.activity,
                output=args.output,
            )
        )
        print(
            json.dumps(
                {
                    "ok": result.ok,
                    "run_dir": str(result.run_dir),
                    "plan": str(result.plan_path),
                    "report": str(result.report_path),
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return

    if args.command == "bibliography-repair":
        result = BibliographyRepairer(AulaTeXWorkspace()).repair(
            BibliographyRepairRequest(
                target=args.target,
                activity_number=args.activity,
                output=args.output,
                apply=bool(args.apply),
                backup=not bool(args.no_backup),
                min_confidence=args.min_confidence,
                workflow_backend=args.workflow_backend,
            )
        )
        print(
            json.dumps(
                {
                    "ok": result.ok,
                    "run_dir": str(result.run_dir),
                    "plan": str(result.plan_path),
                    "report": str(result.report_path),
                    "patched_tex": str(result.patched_tex_path) if result.patched_tex_path else "",
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return

    if args.command == "investigation":
        workspace = AulaTeXWorkspace()
        scope = workspace.find_scope_for_target(args.target, activity_number=args.activity or None)
        if scope is None:
            raise SystemExit(f"No se pudo resolver un scope editorial para: {args.target}")
        builder = InvestigationBuilder(workspace=workspace, llm_bridge=AulaTeXLLMClient())
        request = InvestigationRequest(
            scope_key=scope.key,
            iterations=args.iterations,
            engines=args.engine or ["Codex", "Auto (model-router)", "Claude Foundry", "GPT-Pro"],
            max_tokens=args.max_tokens,
            search_terms=tuple(args.query or []),
            seed_urls=tuple(args.url or []),
        )
        result = builder.build(request)
        print(
            json.dumps(
                {
                    "ok": result.ok,
                    "cancelled": result.cancelled,
                    "run_dir": str(result.run_dir),
                    "manifest": str(result.manifest_path),
                    "knowledge": str(result.knowledge_path),
                    "bibliography": str(result.bibliography_path),
                    "web_sources": str(result.web_sources_path),
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return

    if args.command == "generation":
        workspace = AulaTeXWorkspace()
        builder = ConstructionBuilder(workspace=workspace, llm_bridge=AulaTeXLLMClient())
        request = ConstructionRequest(
            parent_scope_key=args.parent_scope_key,
            node_level=args.node_level,
            node_name=args.node_name,
            activity_number=args.activity,
            operation_mode=args.mode,
            destination_path=args.destination,
            ingest_text=args.ingest_text,
            ingest_document_path=args.ingest_document,
            engines=args.engine or ["Codex", "Auto (model-router)", "Claude Foundry", "GPT-Pro"],
            iterations=args.iterations,
            max_tokens=args.max_tokens,
        )
        result = builder.build(request)
        print(
            json.dumps(
                {
                    "ok": result.ok,
                    "cancelled": result.cancelled,
                    "run_dir": str(result.run_dir),
                    "manifest": str(result.manifest_path),
                    "node_dir": str(result.node_dir),
                    "memory": str(result.memory_path),
                    "plan": str(result.plan_path),
                    "maqueta": str(result.maqueta_path),
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return

    if args.command == "intelligent-engine":
        result = IntelligentEngine(AulaTeXWorkspace()).run(
            IntelligentEngineRequest(
                target=args.target,
                activity_number=args.activity,
                output=args.output,
                backend=args.backend,
                max_targets=args.max_targets,
                audit_path=args.audit,
                include_reports=not bool(args.no_reports),
                include_presentations=not bool(args.no_presentations),
                engines=tuple(args.engine or ["Codex", "Auto (model-router)", "GPT-Pro", "Claude Foundry"]),
            )
        )
        print(
            json.dumps(
                {
                    "ok": result.ok,
                    "run_id": result.run_id,
                    "run_dir": str(result.run_dir),
                    "manifest": str(result.manifest_path),
                    "report": str(result.report_path),
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return

    if args.command == "compile":
        result = AulaTeXWorkspace().compile_tex(args.tex)
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
        raise SystemExit(result.returncode)

    parser.error(f"Unknown command: {args.command}")


if __name__ == "__main__":
    main()
