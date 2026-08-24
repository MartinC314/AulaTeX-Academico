from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace

from scripts.aulatex.agent import AgentRequest, AgentTargetContext, AulaTeXAgent
from scripts.aulatex.agentic_patterns import AgentTask, AgenticStateMachine, EditorialConsensusEngine
from scripts.aulatex.intelligent_engine import IntelligentEngine, IntelligentEngineRequest
from scripts.aulatex.llm_bridge import LLMCallResult


class _Workspace:
    def relative(self, path: Path) -> str:
        return path.as_posix()


class _CaptureAgent:
    request: AgentRequest | None = None

    def __init__(self, _workspace: object) -> None:
        pass

    def run(self, request: AgentRequest) -> SimpleNamespace:
        type(self).request = request
        return SimpleNamespace(
            ok=False,
            run_dir=Path("run"),
            monitor_ok=False,
            optimize_ok=False,
            quality_before=7.0,
            quality_after=7.0,
            optimize_plan_summary=None,
            final_compile_ok=False,
            semantic_blocking_before=1,
            semantic_blocking_after=1,
            semantic_audit_available=True,
        )


def test_intelligent_engine_preserves_requested_tex(monkeypatch, tmp_path: Path) -> None:
    from scripts.aulatex import agent as agent_module

    tex = tmp_path / "presentacion-materia-Actividad-7.tex"
    tex.write_text("\\documentclass{beamer}", encoding="utf-8")
    monkeypatch.setattr(agent_module, "AulaTeXAgent", _CaptureAgent)

    engine = object.__new__(IntelligentEngine)
    engine.workspace = _Workspace()
    request = IntelligentEngineRequest(engines=("Auto (model-router)",))
    reporter = SimpleNamespace(notice=lambda *_: None, progress=lambda *_: None)

    ok, _ = engine._exec_realizar_actividad(
        request, str(tex), str(tmp_path), 7, tmp_path, reporter, 0.0, 1.0
    )

    assert not ok
    assert _CaptureAgent.request is not None
    assert Path(_CaptureAgent.request.target) == tex


def test_generated_beamer_applies_to_explicit_presentation(tmp_path: Path) -> None:
    tex = tmp_path / "presentacion-materia-Actividad-7.tex"
    tex.write_text(
        "\\documentclass{beamer}\n\\begin{document}\n"
        "\\begin{frame}{En construcción}Pendiente\\end{frame}\n\\end{document}\n",
        encoding="utf-8",
    )
    document = (
        "\\documentclass{beamer}\n\\begin{document}\n"
        "\\begin{frame}{Brief}Contenido completo\\end{frame}\n"
        "\\begin{frame}{Roles}Equipo\\end{frame}\n"
        "\\begin{frame}{Cierre}Validación\\end{frame}\n\\end{document}"
    )
    agent = object.__new__(AulaTeXAgent)
    agent.workspace = _Workspace()
    agent._select_compile_targets = lambda *_: [tex]
    target = AgentTargetContext(tex, tex, "scope", str(tex), "direct")
    task = AgentTask("generar", "arquitecto", "generar", "prompt")
    workflow = AgenticStateMachine()

    result = agent._apply_generated_tex(
        AgentRequest(action="realizar-actividad", activity_number=7),
        target,
        [task],
        [LLMCallResult("fake", True, f"```tex\n{document}\n```")],
        workflow,
    )

    assert result["applied"] is True
    assert tex.read_text(encoding="utf-8") == document


def test_empty_llm_response_blocks_consensus() -> None:
    task = AgentTask("generar", "arquitecto", "generar", "prompt")
    report = EditorialConsensusEngine().evaluate(
        [task], [LLMCallResult("fake", True, "")]
    )

    assert not report.passed
    assert any("sin respuesta util" in risk for risk in report.risks)
