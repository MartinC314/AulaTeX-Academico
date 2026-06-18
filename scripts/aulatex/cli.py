from __future__ import annotations

import argparse
import json
from pathlib import Path

from .agent import AgentRequest, AulaTeXAgent
from .agentic_patterns import pattern_catalog_markdown
from .config import credential_status, load_aulatex_env
from .gui import main as gui_main
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
    agent.add_argument("--level", default="materia", choices=("institucion", "carrera", "materia"))
    agent.add_argument("--action", default="generar-plantilla")
    agent.add_argument("--activity", type=int, default=1)
    agent.add_argument("--engine", action="append", choices=LLM_ENGINES)
    agent.add_argument("--iterations", type=int, default=5)
    agent.add_argument("--no-compile", action="store_true")
    agent.add_argument("--apply-feedback", action="store_true")

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
            engines=args.engine or ["Codex", "Claude Foundry", "GPT-Pro", "Auto (model-router)"],
            iterations=args.iterations,
            compile_tex=not args.no_compile,
            apply_feedback=args.apply_feedback,
        )
        result = AulaTeXAgent().run(request)
        print(json.dumps({"ok": result.ok, "run_dir": str(result.run_dir), "report": str(result.report_path)}, indent=2))
        return

    if args.command == "compile":
        result = AulaTeXWorkspace().compile_tex(args.tex)
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
        raise SystemExit(result.returncode)

    parser.error(f"Unknown command: {args.command}")
