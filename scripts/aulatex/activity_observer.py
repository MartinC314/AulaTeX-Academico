from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .activity_contract import evaluate_activity_contract
from .compilation_diagnostics import classify_compile_failure, is_environment_issue
from .editorial_memory import EditorialMemoryStore
from .extractor_adapter import CORE_EXTRACTOR_ARTIFACTS, ExtractorAdapter, ExtractorRequest
from .workspace import AulaTeXWorkspace, EditorialScope


@dataclass(frozen=True)
class ActivityObservationRequest:
    target: str
    activity_number: int = 1
    output: str = ""
    compile_check: bool = False


@dataclass(frozen=True)
class ActivityObservationResult:
    run_id: str
    run_dir: Path
    ok: bool
    state_path: Path
    evaluation_path: Path
    actions_path: Path


class ActivityObserver:
    def __init__(self, workspace: AulaTeXWorkspace | None = None) -> None:
        self.workspace = workspace or AulaTeXWorkspace()
        self.memory_store = EditorialMemoryStore(self.workspace)
        self.extractor = ExtractorAdapter(self.workspace)
        self.root = self.workspace.feedback_root / "activity-observer" / "runs"
        self.root.mkdir(parents=True, exist_ok=True)

    def observe(self, request: ActivityObservationRequest) -> ActivityObservationResult:
        run_id = f"{self.workspace.timestamp()}-activity-{int(request.activity_number):02d}-observer"
        run_dir = self._resolve_run_dir(request, run_id)
        # timestamp() tiene resolución de segundos; en flujos anidados (monitor ->
        # compilation-repair -> observe) varios observes caen en el mismo segundo y
        # colisionan de directorio, provocando FileNotFoundError al leer artefactos
        # de un run pisado por otro. Garantizar unicidad con sufijo incremental,
        # tanto con output implícito como explícito.
        if run_dir.exists() and any(run_dir.iterdir()):
            suffix = 1
            base_run_id = run_id
            while run_dir.exists() and any(run_dir.iterdir()):
                run_id = f"{base_run_id}-{suffix:02d}"
                run_dir = self._resolve_run_dir(request, run_id)
                suffix += 1
        run_dir.mkdir(parents=True, exist_ok=True)

        scope = self.workspace.find_scope_for_target(request.target, activity_number=request.activity_number)
        target_root = self.workspace.resolve_target(scope.relative_path if scope is not None else request.target)
        tex_path = self._find_activity_tex(target_root, request.activity_number)
        pdf_path = tex_path.with_suffix(".pdf") if tex_path is not None else None
        bib_path = self._find_canonical_bib(target_root)
        clean_bib_path = target_root / f"{target_root.name.removesuffix('-lde')}-clean.bib"
        if not clean_bib_path.exists():
            clean_bib_path = target_root / "filosofia-del-derecho-clean.bib"

        tex_text = self._read_text(tex_path)
        active_tex = self._strip_tex_comments(tex_text)
        bib_text = self._read_text(bib_path)
        bib_keys = self._extract_bib_keys(bib_text)
        cited_keys = self._extract_cite_keys(active_tex)
        missing_keys = sorted(key for key in cited_keys if key not in bib_keys)
        placeholder_hits = self._find_placeholders(active_tex)
        sections = self._extract_sections(active_tex)
        extractor_state = self._observe_extractor(target_root, request.activity_number)
        compile_result = self._compile_if_requested(tex_path, request.compile_check)
        extractor_summary = self._load_json(target_root / "extractor-aulatex" / CORE_EXTRACTOR_ARTIFACTS["planeacion"])
        extractor_concepts = self._load_json(target_root / "extractor-aulatex" / CORE_EXTRACTOR_ARTIFACTS["conceptos"])
        editing_details = self._load_editing_details(scope)

        state = self._build_state(
            run_id=run_id,
            scope=scope,
            request=request,
            target_root=target_root,
            tex_path=tex_path,
            pdf_path=pdf_path,
            bib_path=bib_path,
            clean_bib_path=clean_bib_path if clean_bib_path.exists() else None,
            cited_keys=cited_keys,
            missing_keys=missing_keys,
            placeholder_hits=placeholder_hits,
            sections=sections,
            extractor_state=extractor_state,
            extractor_summary=extractor_summary,
            extractor_concepts=extractor_concepts,
            editing_details=editing_details,
            active_tex=active_tex,
            compile_result=compile_result,
        )
        evaluation = self._build_evaluation(state)
        state["next_action"] = evaluation["next_action"]
        actions = self._build_actions_markdown(state, evaluation)

        state_path = run_dir / "estado-agente.json"
        evaluation_path = run_dir / "evaluacion.json"
        actions_path = run_dir / "acciones-recomendadas.md"
        state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")
        evaluation_path.write_text(json.dumps(evaluation, ensure_ascii=False, indent=2), encoding="utf-8")
        actions_path.write_text(actions, encoding="utf-8")

        manifest = {
            "run_id": run_id,
            "kind": "activity-observer",
            "target": self.workspace.relative(target_root),
            "activity_number": int(request.activity_number),
            "ok": bool(evaluation["passed"]),
            "state": self.workspace.relative(state_path),
            "evaluation": self.workspace.relative(evaluation_path),
            "actions": self.workspace.relative(actions_path),
        }
        (run_dir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
        self.workspace.append_bitacora(run_id, "activity-observer", manifest)
        return ActivityObservationResult(run_id, run_dir, bool(evaluation["passed"]), state_path, evaluation_path, actions_path)

    def _resolve_run_dir(self, request: ActivityObservationRequest, run_id: str) -> Path:
        if request.output.strip():
            return self.workspace.resolve_target(request.output) / run_id
        return self.root / run_id

    def _find_activity_tex(self, target_root: Path, activity_number: int) -> Path | None:
        if target_root.is_file() and target_root.suffix.lower() == ".tex":
            return target_root
        if not target_root.exists() or not target_root.is_dir():
            return None
        patterns = [
            f"*Actividad-{int(activity_number)}.tex",
            f"*Actividad_{int(activity_number)}.tex",
            f"*actividad-{int(activity_number)}.tex",
            f"*actividad_{int(activity_number)}.tex",
        ]
        for pattern in patterns:
            matches = sorted(
                (path for path in target_root.glob(pattern) if path.is_file()),
                key=lambda path: (not path.name.lower().startswith("reporte-"), path.name.lower()),
            )
            if matches:
                return matches[0]
        activity_re = re.compile(rf"actividad[-_\s]*0?{int(activity_number)}", re.IGNORECASE)
        for path in sorted(target_root.glob("*.tex")):
            if activity_re.search(path.stem):
                return path
        return None

    def _find_canonical_bib(self, target_root: Path) -> Path | None:
        if not target_root.exists():
            return None
        if target_root.is_file():
            target_root = target_root.parent
        direct = sorted(path for path in target_root.glob("*.bib") if path.is_file() and "clean" not in path.stem.lower())
        if direct:
            preferred = [path for path in direct if path.stem == target_root.name.removesuffix("-lde")]
            return preferred[0] if preferred else direct[0]
        return None

    def _observe_extractor(self, target_root: Path, activity_number: int) -> dict[str, Any]:
        candidates = [
            target_root / "extractor-aulatex" / f"actividad-{int(activity_number):02d}",
            target_root / "extractor-aulatex",
        ]
        for candidate in candidates:
            if candidate.exists():
                artifacts = {
                    name: {
                        "present": (candidate / filename).exists(),
                        "path": self.workspace.relative(candidate / filename),
                    }
                    for name, filename in CORE_EXTRACTOR_ARTIFACTS.items()
                }
                return {
                    "ready": all(item["present"] for item in artifacts.values()),
                    "output_dir": self.workspace.relative(candidate),
                    "artifacts": artifacts,
                    "missing_artifacts": [name for name, item in artifacts.items() if not item["present"]],
                }
        preview = self.extractor.preview_markdown(ExtractorRequest(target=str(target_root), activity_number=activity_number))
        return {
            "ready": False,
            "output_dir": "",
            "artifacts": {},
            "missing_artifacts": list(CORE_EXTRACTOR_ARTIFACTS.keys()),
            "preview": preview,
        }

    def _compile_if_requested(self, tex_path: Path | None, enabled: bool) -> dict[str, Any]:
        if not enabled:
            return {"enabled": False, "ok": None, "returncode": None}
        if tex_path is None:
            return {"enabled": True, "ok": False, "returncode": None, "error": "No se encontró TEX de actividad.", "category": "missing-tex"}
        result = self.workspace.compile_tex(tex_path, clean_mode="safe")
        combined = f"{result.stdout}\n{result.stderr}"
        category = classify_compile_failure(combined) if not result.ok else "ok"
        return {
            "enabled": True,
            "ok": result.ok,
            "returncode": result.returncode,
            "category": category,
            "environment_issue": bool(not result.ok and is_environment_issue(category)),
            "stdout_tail": result.stdout[-3000:],
            "stderr_tail": result.stderr[-3000:],
        }

    def _build_state(
        self,
        *,
        run_id: str,
        scope: EditorialScope | None,
        request: ActivityObservationRequest,
        target_root: Path,
        tex_path: Path | None,
        pdf_path: Path | None,
        bib_path: Path | None,
        clean_bib_path: Path | None,
        cited_keys: list[str],
        missing_keys: list[str],
        placeholder_hits: list[str],
        sections: list[str],
        extractor_state: dict[str, Any],
        extractor_summary: dict[str, Any] | list[Any] | None,
        extractor_concepts: dict[str, Any] | list[Any] | None,
        editing_details: dict[str, Any],
        active_tex: str,
        compile_result: dict[str, Any],
    ) -> dict[str, Any]:
        bibliography_ready = bool(bib_path and bib_path.exists() and not missing_keys)
        draft_ready = bool(tex_path and tex_path.exists() and not placeholder_hits)
        if not compile_result.get("enabled"):
            compile_ready = "unknown"
        elif compile_result.get("ok"):
            compile_ready = True
        elif compile_result.get("environment_issue"):
            compile_ready = "environment-blocked"
        else:
            compile_ready = False
        next_action = self._next_action(bibliography_ready, draft_ready, extractor_state, compile_ready, missing_keys, placeholder_hits)
        return {
            "schema_version": 1,
            "run_id": run_id,
            "agent_mode": "activity-observer",
            "scope_key": scope.key if scope is not None else "",
            "activity_number": int(request.activity_number),
            "target_root": self.workspace.relative(target_root),
            "target_tex": self.workspace.relative(tex_path) if tex_path else "",
            "target_pdf": self.workspace.relative(pdf_path) if pdf_path and pdf_path.exists() else "",
            "bib_ref": self.workspace.relative(bib_path) if bib_path else "",
            "clean_bib_ref": self.workspace.relative(clean_bib_path) if clean_bib_path else "",
            "observed_state": {
                "memory_ready": bool(scope),
                "detail_planner_ready": bool(editing_details),
                "planeacion_ready": "unknown",
                "extractor_ready": bool(extractor_state.get("ready")),
                "bibliography_ready": bibliography_ready,
                "draft_ready": draft_ready,
                "compile_ready": compile_ready,
                "evaluation_ready": True,
            },
            "editing_details": editing_details,
            "signals": {
                "sections": sections,
                "sections_count": len(sections),
                "cited_keys": cited_keys,
                "cited_keys_count": len(cited_keys),
                "missing_bib_keys": missing_keys,
                "placeholder_hits": placeholder_hits,
                "objective_present": bool(re.search(r"\\textbf\{Objetivo:\}|\\section\{Objetivo", active_tex, re.IGNORECASE)),
                "purpose_present": bool(re.search(r"\\textbf\{Prop[óo]sito:\}|prop[óo]sito", active_tex, re.IGNORECASE)),
                "conclusion_present": bool(sections and any("conclus" in section.lower() for section in sections)) or bool(re.search(r"en conclusi[óo]n", active_tex, re.IGNORECASE)),
                "ai_declaration_present": bool(re.search(r"inteligencia artificial|uso de\s+ia\b|herramienta[s]?\s+de\s+ia\b", active_tex, re.IGNORECASE)),
                "ai_declaration_as_footnote": bool(
                    re.search(
                        r"\\footnote\{[^}]*(inteligencia artificial|uso de\s+ia\b|herramienta[s]?\s+de\s+ia\b)",
                        active_tex,
                        re.IGNORECASE | re.DOTALL,
                    )
                ),
                "ai_declaration_as_section": bool(
                    re.search(
                        r"\\section\*?\{[^}]*(declaraci[óo]n[^}]*inteligencia artificial|uso[^}]*inteligencia artificial|declaraci[óo]n[^}]*\bia\b)",
                        active_tex,
                        re.IGNORECASE,
                    )
                ),
                "product_visual_detected": bool(re.search(r"tikzpicture|\\begin\{figure\}|mapa conceptual|cuadro|tabla|diagrama", active_tex, re.IGNORECASE)),
                "metadiscourse_hits": self._find_metadiscourse(active_tex),
                "evaluation_criteria_present": bool(re.search(r"criterios|r[úu]brica|evaluaci[óo]n", active_tex, re.IGNORECASE)),
                "questionnaire_detected": bool(re.search(r"cuestionario|reactivo|pregunta\s*\d+", active_tex, re.IGNORECASE)),
                "questionnaire_contract_satisfied": bool(
                    re.search(r"cuestionario", active_tex, re.IGNORECASE)
                    and re.search(r"pregunta", active_tex, re.IGNORECASE)
                    and re.search(r"respuesta", active_tex, re.IGNORECASE)
                    and re.search(r"justificaci[óo]n", active_tex, re.IGNORECASE)
                ),
                "table_contract_satisfied": bool(
                    re.search(r"\\begin\{longtable\}|\\begin\{tabular\}", active_tex, re.IGNORECASE)
                    and re.search(r"\\toprule|\\midrule|\\hline", active_tex, re.IGNORECASE)
                    and re.search(r"\\caption\{|\\textbf\{.*?\}", active_tex, re.IGNORECASE)
                ),
                "case_study_detected": bool(re.search(r"estudio de caso|an[áa]lisis del caso|hechos", active_tex, re.IGNORECASE)),
                "didactic_technique_present": bool(re.search(r"mapa conceptual|estudio de caso|cuadro comparativo|diagrama|tabla|cuestionario|foro diagn[óo]stico|longtable|tabular", active_tex, re.IGNORECASE)),
                "extractor_planeacion_present": bool(isinstance(extractor_summary, dict) and extractor_summary),
                "extractor_objective_present": bool(isinstance(extractor_summary, dict) and str(extractor_summary.get("objetivo", "")).strip()),
                "extractor_criteria_count": len(extractor_summary.get("criterios_entrega", [])) if isinstance(extractor_summary, dict) and isinstance(extractor_summary.get("criterios_entrega", []), list) else 0,
                "extractor_verbs_count": len(extractor_summary.get("verbos_operativos", [])) if isinstance(extractor_summary, dict) and isinstance(extractor_summary.get("verbos_operativos", []), list) else 0,
                "extractor_concepts_count": len(extractor_concepts) if isinstance(extractor_concepts, list) else 0,
                "extractor": extractor_state,
                "compile": compile_result,
            },
            "next_action": next_action,
        }

    def _build_evaluation(self, state: dict[str, Any]) -> dict[str, Any]:
        observed = state["observed_state"]
        signals = state["signals"]
        checks = {
            "tex_exists": bool(state.get("target_tex")),
            "pdf_exists": bool(state.get("target_pdf")),
            "detail_planner_ready": bool(observed.get("detail_planner_ready")),
            "bibliography_ready": bool(observed.get("bibliography_ready")),
            "extractor_ready": bool(observed.get("extractor_ready")),
            "draft_without_placeholders": bool(observed.get("draft_ready")),
            "sections_minimum": int(signals.get("sections_count", 0)) >= 3,
            "compile_ready": observed.get("compile_ready") in {True, "unknown", "environment-blocked"},
        }
        critical = []
        warnings = []
        if not checks["tex_exists"]:
            critical.append("No se encontró TEX de actividad.")
        if not checks["detail_planner_ready"]:
            warnings.append("No existen editing_details persistidos para el nodo.")
        if not checks["bibliography_ready"]:
            critical.append("Hay claves bibliográficas faltantes o no hay .bib canónico.")
        if not checks["extractor_ready"]:
            critical.append("No existe salida verificable del extractor para esta actividad.")
        if not checks["draft_without_placeholders"]:
            critical.append("Hay placeholders o pendientes activos.")
        if observed.get("compile_ready") is False:
            critical.append("La compilación falló.")
        elif observed.get("compile_ready") == "environment-blocked":
            warnings.append("La compilación no pudo verificarse por una dependencia faltante del entorno TeX; no se penaliza el score editorial.")
        contract = evaluate_activity_contract(state)
        next_action = state["next_action"]
        if next_action == "finalize" and not contract["passed"]:
            next_action = "revise-activity"
            critical.extend(item for item in contract["findings"] if item not in critical)
        if next_action != "finalize":
            critical.append(f"El ciclo aún no puede cerrarse: siguiente acción requerida `{next_action}`.")
        basic_score = round(100 * sum(1 for ok in checks.values() if ok) / max(1, len(checks)), 2)
        score = round((basic_score * 0.55) + (contract["score"] * 0.45), 2)
        return {
            "passed": next_action == "finalize" and not critical and basic_score >= 85 and contract["passed"],
            "score": score,
            "basic_score": basic_score,
            "checks": checks,
            "critical_findings": critical,
            "warnings": warnings,
            "next_action": next_action,
            "contract": contract,
        }

    def _load_editing_details(self, scope: EditorialScope | None) -> dict[str, Any]:
        if scope is None:
            return {}
        memory = self.memory_store.get_memory(scope.key)
        return dict((memory.get("node_metadata") or {}).get("editing_details") or {})

    def _build_actions_markdown(self, state: dict[str, Any], evaluation: dict[str, Any]) -> str:
        lines = [
            "# Acciones recomendadas",
            "",
            f"- Actividad: {state['activity_number']}",
            f"- Scope: `{state.get('scope_key', '')}`",
            f"- TEX: `{state.get('target_tex', '')}`",
            f"- Score: {evaluation['score']}",
            f"- Siguiente acción: `{evaluation['next_action']}`",
            "",
            "## Hallazgos críticos",
            "",
        ]
        if evaluation["critical_findings"]:
            lines.extend(f"- {item}" for item in evaluation["critical_findings"])
        else:
            lines.append("- No hay hallazgos críticos.")
        warnings = evaluation.get("warnings") or []
        if warnings:
            lines.extend(["", "## Advertencias", ""])
            lines.extend(f"- {item}" for item in warnings)
        missing = state["signals"].get("missing_bib_keys", [])
        if missing:
            lines.extend(["", "## Claves bibliográficas faltantes", ""])
            lines.extend(f"- `{key}`" for key in missing)
            lines.extend([
                "",
                "Acción sugerida: buscar equivalentes en el `.bib` canónico antes de reescribir contenido.",
            ])
        placeholders = state["signals"].get("placeholder_hits", [])
        if placeholders:
            lines.extend(["", "## Pendientes detectados", ""])
            lines.extend(f"- `{item}`" for item in placeholders[:20])
        extractor = state["signals"].get("extractor", {})
        if not extractor.get("ready"):
            lines.extend(["", "## Extractor", ""])
            lines.append("- No hay salida completa del extractor para esta actividad.")
            if extractor.get("missing_artifacts"):
                lines.append("- Faltantes: " + ", ".join(extractor["missing_artifacts"]))
        lines.append("")
        return "\n".join(lines)

    def _next_action(
        self,
        bibliography_ready: bool,
        draft_ready: bool,
        extractor_state: dict[str, Any],
        compile_ready: bool | str,
        missing_keys: list[str],
        placeholder_hits: list[str],
    ) -> str:
        if missing_keys or not bibliography_ready:
            return "repair-bibliography"
        if compile_ready is False:
            return "repair-compilation"
        if not extractor_state.get("ready"):
            return "run-extractor"
        if placeholder_hits or not draft_ready:
            return "revise-activity"
        return "finalize"

    def _read_text(self, path: Path | None) -> str:
        if path is None or not path.exists() or not path.is_file():
            return ""
        return path.read_text(encoding="utf-8", errors="replace")

    def _load_json(self, path: Path | None) -> dict[str, Any] | list[Any] | None:
        if path is None or not path.exists() or not path.is_file():
            return None
        try:
            return json.loads(path.read_text(encoding="utf-8", errors="replace"))
        except json.JSONDecodeError:
            return None

    def _strip_tex_comments(self, text: str) -> str:
        lines = []
        for line in text.splitlines():
            if line.lstrip().startswith("%"):
                continue
            lines.append(line)
        return "\n".join(lines)

    def _extract_cite_keys(self, text: str) -> list[str]:
        keys: list[str] = []
        pattern = re.compile(r"\\cite[t|p]?\*?(?:\[[^\]]*\])*\{([^}]+)\}")
        for match in pattern.finditer(text):
            keys.extend(key.strip() for key in match.group(1).split(",") if key.strip())
        return sorted(set(keys))

    def _extract_bib_keys(self, text: str) -> set[str]:
        return {match.group(1).strip() for match in re.finditer(r"@\w+\s*\{\s*([^,\s]+)", text)}

    def _find_placeholders(self, text: str) -> list[str]:
        hits = []
        case_insensitive_patterns = (r"\\pendiente\{[^}]*\}", r"\bPENDIENTE\b", r"Actividad X", r"Semana X")
        for pattern in case_insensitive_patterns:
            hits.extend(match.group(0) for match in re.finditer(pattern, text, re.IGNORECASE))
        for pattern in (r"\bTODO\b", r"\bFIXME\b"):
            hits.extend(match.group(0) for match in re.finditer(pattern, text))
        return sorted(set(hits))

    def _find_metadiscourse(self, text: str) -> list[str]:
        """Detecta metadiscurso de ejecución visible que el contrato prohíbe.

        Incluye residuos del flujo antiguo (Refuerzo editorial Ciclo A) y menciones
        de 'la actividad N' / 'esta actividad' / 'el producto solicitado' como narrador
        externo. No penaliza el mismo texto dentro de comentarios TEX (que ya fueron
        removidos por _strip_tex_comments antes de invocar este método).
        """
        hits: list[str] = []
        patterns = (
            r"Refuerzo editorial",
            r"Ciclo A\b",
            r"\bLa Actividad\s+\d+",
            r"\bEsta actividad\b",
            r"el producto solicitado",
            r"la t[ée]cnica usada",
            r"\\section\*?\{[^}]*[Rr]efuerzo",
        )
        for pattern in patterns:
            hits.extend(match.group(0).strip() for match in re.finditer(pattern, text, re.IGNORECASE))
        return sorted(set(hits))

    def _extract_sections(self, text: str) -> list[str]:
        return [match.group(1).strip() for match in re.finditer(r"\\section\{([^}]+)\}", text)]
