from __future__ import annotations

import argparse
import json
from pathlib import Path

from .agent import AgentRequest, AulaTeXAgent
from .agentic_patterns import pattern_catalog_markdown
from .config import credential_status, load_aulatex_env
from .construction import ConstructionBuilder, ConstructionRequest
from .editorial_memory import EDITORIAL_LEVELS, EditorialMemoryBuilder, EditorialMemoryRequest
from .gui import main as gui_main
from .investigation import InvestigationBuilder, InvestigationRequest
from .llm_bridge import LLM_ENGINES, AulaTeXLLMClient
from .workspace import AulaTeXWorkspace


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="aulatex", description="AulaTeX GUI and agentic editorial workflow.")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("gui", help="Open the AulaTeX GUI.")
    sub.add_parser("agent-patterns", help="List the agentic patterns integrated in AulaTeX.")

    env_cmd = sub.add_parser("llm-env", help="Show AulaTeX LLM credential status without secrets.")

    check = sub.add_parser("llm-check", help="Check configured AulaTeX LLM engines.")
    check.add_argument("--engine", action="append", choices=LLM_ENGINES)

    prompt = sub.add_parser("llm-prompt", help="Run one prompt through one LLM engine.")
    prompt.add_argument("prompt")
    prompt.add_argument("--engine", default="Codex", choices=LLM_ENGINES)
    prompt.add_argument("--max-tokens", type=int, default=1400)

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
    agent.add_argument("--no-compile", action="store_true")
    agent.add_argument("--apply-feedback", action="store_true")

    editorial = sub.add_parser("editorial-memory", help="Build persistent editorial memory from a selected scope.")
    editorial.add_argument("--target", default=".")
    editorial.add_argument("--activity", type=int, default=0)
    editorial.add_argument("--build-level", default="materia", choices=EDITORIAL_LEVELS)
    editorial.add_argument("--propagation-mode", default="ascendente", choices=("local", "ascendente", "ascendente-exhaustivo", "recursivo"))
    editorial.add_argument("--engine", action="append", choices=LLM_ENGINES)
    editorial.add_argument("--iterations", type=int, default=2)
    editorial.add_argument("--max-tokens", type=int, default=1400)

    investigation = sub.add_parser("investigation", help="Consolidate the knowledge base before extractor: local context, web sources and bibliography.")
    investigation.add_argument("--target", default=".")
    investigation.add_argument("--activity", type=int, default=0)
    investigation.add_argument("--engine", action="append", choices=LLM_ENGINES)
    investigation.add_argument("--iterations", type=int, default=2)
    investigation.add_argument("--max-tokens", type=int, default=1800)
    investigation.add_argument("--query", action="append", default=[])
    investigation.add_argument("--url", action="append", default=[])

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
    generation.add_argument("--max-tokens", type=int, default=1800)

    compile_cmd = sub.add_parser("compile", help="Compile a TeX file with the shared latexmk wrapper.")
    compile_cmd.add_argument("tex")

    return parser


def main(argv: list[str] | None = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command in (None, "gui"):
        gui_main()
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
        result = AulaTeXLLMClient().call(args.engine, args.prompt, max_tokens=args.max_tokens)
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
            compile_tex=not args.no_compile,
            apply_feedback=args.apply_feedback,
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
        )
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

    if args.command == "compile":
        result = AulaTeXWorkspace().compile_tex(args.tex)
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
        raise SystemExit(result.returncode)

    parser.error(f"Unknown command: {args.command}")
