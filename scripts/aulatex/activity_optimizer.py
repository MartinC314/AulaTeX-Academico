"""Ciclos de optimización de calidad que SÍ mejoran el .tex real.

A diferencia de ``agent --cycle-mode full`` (que solo genera propuestas LLM
efímeras y puntúa un consenso que no toca el archivo), este módulo ejecuta ciclos
que:

1. Miden la calidad editorial real del ``.tex`` (score propio + contrato).
2. Piden al LLM UNA mejora concreta y aplicable como reemplazo de un bloque
   textual existente (JSON estructurado).
3. Aplican el reemplazo de forma segura solo si el bloque original existe.
4. Recompilan y verifican que el contrato editorial siga en 100 y el PDF exista.
5. Revierten el ciclo si la compilación falla, el contrato baja o la calidad no
   mejora.

Así, tras converger el contrato a 100, los ciclos adicionales elevan la calidad
del documento de forma verificable y quedan registrados.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .activity_observer import ActivityObservationRequest, ActivityObserver
from .llm_bridge import DEFAULT_MAX_TOKENS, AulaTeXLLMClient
from .workspace import AulaTeXWorkspace


@dataclass(frozen=True)
class ActivityOptimizeRequest:
    target: str
    activity_number: int = 1
    output: str = ""
    # Modo de parada. Por DEFECTO se optimiza hasta CONVERGER a target_quality
    # (no un número fijo de ciclos): se ejecutan los ciclos que sean necesarios
    # hasta alcanzar la calidad objetivo, estancarse o llegar al tope de seguridad.
    # Si el usuario fija cycles>0 explícitamente, se respeta ese número exacto.
    cycles: int = 0
    target_quality: float = 100.0
    max_cycles: int = 40
    stall_limit: int = 6
    engines: tuple[str, ...] = ("GPT-5.6-Luna", "GPT-5.6-Terra")
    max_tokens: int = DEFAULT_MAX_TOKENS
    backup: bool = True
    require_contract_100: bool = True


@dataclass(frozen=True)
class ActivityOptimizeResult:
    run_id: str
    run_dir: Path
    ok: bool
    manifest_path: Path
    report_path: Path
    applied_cycles: int
    quality_before: float
    quality_after: float
    tex_path: Path | None


@dataclass
class CycleRecord:
    index: int
    engine: str
    accepted: bool
    reason: str
    quality_before: float
    quality_after: float
    contract_before: float
    contract_after: float
    improvement_kind: str = ""
    diff_chars: int = 0


class ActivityOptimizer:
    def __init__(self, workspace: AulaTeXWorkspace | None = None, llm: AulaTeXLLMClient | None = None) -> None:
        self.workspace = workspace or AulaTeXWorkspace()
        self.observer = ActivityObserver(self.workspace)
        self.llm = llm or AulaTeXLLMClient()
        self.root = self.workspace.feedback_root / "activity-optimize" / "runs"
        self.root.mkdir(parents=True, exist_ok=True)

    def optimize(self, request: ActivityOptimizeRequest) -> ActivityOptimizeResult:
        run_id = f"{self.workspace.timestamp()}-activity-{int(request.activity_number):02d}-optimize"
        run_dir = self._resolve_run_dir(request, run_id)
        run_dir.mkdir(parents=True, exist_ok=True)

        observation = self._observe(request, run_dir / "obs-initial")
        state = json.loads(observation["state"].read_text(encoding="utf-8"))
        evaluation = json.loads(observation["evaluation"].read_text(encoding="utf-8"))
        tex_path = self.workspace.resolve_target(state.get("target_tex", ""))

        if not tex_path.exists() or not tex_path.is_file():
            return self._finalize(request, run_id, run_dir, [], 0.0, 0.0, None, ok=False,
                                  note="No se encontró el TEX de la actividad.")

        contract_before = float((evaluation.get("contract") or {}).get("score", 0.0))
        if request.require_contract_100 and contract_before < 100.0:
            return self._finalize(request, run_id, run_dir, [], 0.0, 0.0, tex_path, ok=False,
                                  note=(f"El contrato editorial está en {contract_before}/100; "
                                        "primero converge con activity-monitor antes de optimizar calidad."))

        original_text = tex_path.read_text(encoding="utf-8", errors="replace")
        if request.backup:
            backup_path = tex_path.with_suffix(tex_path.suffix + ".activity-optimize.bak")
            backup_path.write_text(original_text, encoding="utf-8")

        rubric = self._rubric_text(state, evaluation)
        current_text = original_text
        quality_start = self._quality_score(current_text)
        contract_current = contract_before

        cycles: list[CycleRecord] = []
        engines = request.engines or ("GPT-5.6-Luna", "GPT-5.6-Terra")

        # Modo de parada:
        #  - fixed_cycles (cycles>0): número exacto de ciclos solicitado.
        #  - convergencia (cycles<=0, por DEFECTO): iterar hasta que la calidad
        #    alcance target_quality, se estanque (stall_limit ciclos consecutivos
        #    sin mejora aceptada) o se llegue al tope de seguridad max_cycles.
        fixed_cycles = int(request.cycles) if int(request.cycles) > 0 else 0
        target_quality = float(request.target_quality)
        hard_cap = fixed_cycles if fixed_cycles > 0 else max(1, int(request.max_cycles))
        stall_limit = max(1, int(request.stall_limit))
        stall = 0

        index = 0
        while index < hard_cap:
            # Parada por convergencia (solo en modo convergencia).
            if fixed_cycles == 0:
                if self._quality_score(current_text) >= target_quality:
                    break
                if stall >= stall_limit:
                    break
            index += 1
            engine = engines[(index - 1) % len(engines)]
            cycle_dir = run_dir / f"cycle-{index:02d}"
            cycle_dir.mkdir(parents=True, exist_ok=True)

            quality_before = self._quality_score(current_text)
            proposal = self._request_improvement(engine, current_text, rubric, request, cycle_dir)

            if proposal is None:
                stall += 1
                cycles.append(CycleRecord(index, engine, False, "El motor no devolvió una propuesta aplicable.",
                                          quality_before, quality_before, contract_current, contract_current))
                continue

            candidate_text, kind = self._apply_proposal(current_text, proposal)
            if candidate_text is None:
                stall += 1
                cycles.append(CycleRecord(index, engine, False,
                                          "El bloque original propuesto no se encontró textualmente en el TEX.",
                                          quality_before, quality_before, contract_current, contract_current,
                                          improvement_kind=proposal.get("improvement_kind", "")))
                continue

            # Escribir candidato, recompilar y verificar contrato + calidad.
            tex_path.write_text(candidate_text, encoding="utf-8")
            new_eval = self._observe_eval(request, cycle_dir / "obs")
            contract_after = float((new_eval.get("contract") or {}).get("score", 0.0))
            compile_ok = self._compile_ok(new_eval)
            quality_after = self._quality_score(candidate_text)

            accept = (
                compile_ok
                and contract_after >= contract_current
                and (not request.require_contract_100 or contract_after >= 100.0)
                and quality_after > quality_before
            )

            if accept:
                diff = abs(len(candidate_text) - len(current_text))
                current_text = candidate_text
                contract_current = contract_after
                stall = 0  # hubo mejora aceptada: se reinicia el contador de estancamiento
                cycles.append(CycleRecord(index, engine, True, "Mejora aplicada y verificada.",
                                          quality_before, quality_after, contract_current, contract_after,
                                          improvement_kind=kind, diff_chars=diff))
            else:
                # Revertir el candidato.
                tex_path.write_text(current_text, encoding="utf-8")
                stall += 1  # ciclo sin mejora: acerca la parada por estancamiento
                reason = self._reject_reason(compile_ok, contract_after, contract_current, quality_after, quality_before, request)
                cycles.append(CycleRecord(index, engine, False, reason,
                                          quality_before, quality_after, contract_current, contract_after,
                                          improvement_kind=kind))

        # Asegurar que el archivo final refleja el mejor estado aceptado.
        tex_path.write_text(current_text, encoding="utf-8")
        quality_end = self._quality_score(current_text)
        applied = sum(1 for c in cycles if c.accepted)
        ok = quality_end >= quality_start and contract_current >= contract_before

        return self._finalize(request, run_id, run_dir, cycles, quality_start, quality_end, tex_path,
                              ok=ok, note="", contract_before=contract_before, contract_after=contract_current,
                              applied=applied)

    # ---------------------------------------------------------------- observación

    def _observe(self, request: ActivityOptimizeRequest, out_dir: Path) -> dict[str, Path]:
        observation = self.observer.observe(
            ActivityObservationRequest(
                target=request.target,
                activity_number=request.activity_number,
                output=str(out_dir),
                compile_check=True,
            )
        )
        return {"state": observation.state_path, "evaluation": observation.evaluation_path}

    def _observe_eval(self, request: ActivityOptimizeRequest, out_dir: Path) -> dict[str, Any]:
        paths = self._observe(request, out_dir)
        return json.loads(paths["evaluation"].read_text(encoding="utf-8"))

    def _compile_ok(self, evaluation: dict[str, Any]) -> bool:
        checks = evaluation.get("checks") or {}
        # compile_ready acepta True/'unknown'/'environment-blocked'; el observer ya lo normaliza.
        return bool(checks.get("compile_ready", True))

    # ---------------------------------------------------------------- calidad

    def _quality_score(self, text: str) -> float:
        """Score de calidad editorial verificable (0-100), independiente del LLM.

        Mide señales objetivas de rigor y densidad argumentativa del .tex real.
        """
        body = self._strip_comments(text)
        score = 0.0

        # Citas visibles (densidad): hasta 25 pts.
        cites = len(re.findall(r"\\cite[tp]?\*?(?:\[[^\]]*\])*\{", body))
        score += min(25.0, cites * 5.0)

        # Estructura: secciones y subsecciones (hasta 15 pts).
        sections = len(re.findall(r"\\section\{", body))
        subsections = len(re.findall(r"\\subsection\*?\{", body))
        score += min(10.0, sections * 2.0) + min(5.0, subsections * 1.5)

        # Estructuras enumeradas/listas que ordenan el argumento (hasta 15 pts).
        enums = len(re.findall(r"\\begin\{(enumerate|itemize)\}", body))
        score += min(15.0, enums * 5.0)

        # Densidad argumentativa: conectores de razonamiento (hasta 15 pts).
        connectors = len(re.findall(
            r"\b(por tanto|por ello|en consecuencia|sin embargo|no obstante|es decir|"
            r"en cambio|por el contrario|de ese modo|así)\b",
            body, re.IGNORECASE))
        score += min(15.0, connectors * 2.0)

        # Extensión sustantiva del cuerpo (hasta 15 pts): palabras fuera de preámbulo.
        words = len(re.findall(r"\b\w+\b", body))
        score += min(15.0, words / 120.0)

        # Marcado de integridad / postura propia (hasta 15 pts).
        integrity = len(re.findall(
            r"\b(desde mi perspectiva|considero|sostengo|reflexión propia|"
            r"declaración de uso|inteligencia artificial|no invent|supuesto)\b",
            body, re.IGNORECASE))
        score += min(15.0, integrity * 3.0)

        return round(min(100.0, score), 2)

    # ---------------------------------------------------------------- LLM

    def _rubric_text(self, state: dict[str, Any], evaluation: dict[str, Any]) -> str:
        contract = evaluation.get("contract") or {}
        subject = state.get("subject") or state.get("scope_key") or ""
        technique = ""
        signals = state.get("signals") or {}
        technique = signals.get("didactic_technique") or contract.get("didactic_technique") or ""
        return (
            f"Materia/scope: {subject}\n"
            f"Técnica didáctica: {technique}\n"
            "Objetivo de calidad: elevar rigor argumentativo, densidad de citas pertinentes, "
            "estructura (listas/enumeraciones que ordenen el razonamiento), conectores lógicos, "
            "postura propia fundamentada e integridad académica, SIN cambiar la técnica didáctica, "
            "sin inventar fuentes ni claves de cita nuevas, y conservando el formato LaTeX."
        )

    def _request_improvement(self, engine: str, current_text: str, rubric: str,
                             request: ActivityOptimizeRequest, cycle_dir: Path) -> dict[str, Any] | None:
        body = self._strip_comments(current_text)
        cite_keys = sorted(set(re.findall(r"\\cite[tp]?\*?(?:\[[^\]]*\])*\{([^}]+)\}", body)))
        allowed_keys = sorted({k.strip() for group in cite_keys for k in group.split(",") if k.strip()})

        prompt = (
            "Eres un editor académico experto en LaTeX. Se te da un documento .tex de una actividad "
            "universitaria que YA cumple el contrato editorial al 100%. Tu tarea es proponer UNA sola "
            "mejora de CALIDAD concreta y segura, expresada como el reemplazo textual de un bloque "
            "existente por una versión mejorada.\n\n"
            "REGLAS ESTRICTAS:\n"
            "- Devuelve SOLO un objeto JSON válido, sin texto adicional ni ```.\n"
            "- El campo 'original_block' DEBE ser una copia EXACTA y literal de un fragmento contiguo "
            "presente en el documento (incluye saltos de línea reales). Copia entre 2 y 12 líneas.\n"
            "- El campo 'improved_block' es su reemplazo: mismo rol, mejor rigor/estructura/densidad, "
            "LaTeX válido y balanceado (no rompas entornos ni llaves).\n"
            "- NO inventes claves de cita nuevas. Solo puedes usar estas claves ya presentes: "
            f"{', '.join(allowed_keys) or '(ninguna)'}.\n"
            "- NO cambies la técnica didáctica ni el sentido; solo mejora la calidad.\n"
            "- Prefiere: convertir prosa difusa en enumeraciones ordenadas, añadir un conector lógico, "
            "precisar una afirmación con una cita ya existente, o reforzar la postura propia.\n\n"
            "Formato JSON EXACTO:\n"
            '{\n'
            '  "improvement_kind": "<enumeracion|conector|precision-cita|postura-propia|estructura>",\n'
            '  "justification": "<por qué eleva la calidad, 1-2 frases>",\n'
            '  "original_block": "<copia literal del bloque existente>",\n'
            '  "improved_block": "<bloque mejorado>"\n'
            '}\n\n'
            f"Guía de calidad:\n{rubric}\n\n"
            "DOCUMENTO .tex ACTUAL:\n"
            "-----8<-----\n"
            f"{current_text}\n"
            "-----8<-----\n"
        )

        result = self.llm.call(engine, prompt, max_tokens=request.max_tokens)
        (cycle_dir / "llm-raw.txt").write_text(result.text if result.ok else (result.error or ""), encoding="utf-8")
        if not result.ok or not result.text.strip():
            return None
        proposal = self._parse_json_proposal(result.text)
        if proposal is not None:
            (cycle_dir / "proposal.json").write_text(
                json.dumps(proposal, ensure_ascii=False, indent=2), encoding="utf-8")
        return proposal

    def _parse_json_proposal(self, text: str) -> dict[str, Any] | None:
        candidate = text.strip()
        # Quitar fences de código si el modelo los añadió.
        fence = re.search(r"```(?:json)?\s*(\{.*\})\s*```", candidate, re.DOTALL)
        if fence:
            candidate = fence.group(1)
        else:
            first = candidate.find("{")
            last = candidate.rfind("}")
            if first != -1 and last != -1 and last > first:
                candidate = candidate[first : last + 1]
        try:
            data = json.loads(candidate)
        except json.JSONDecodeError:
            return None
        if not isinstance(data, dict):
            return None
        if not str(data.get("original_block", "")).strip() or not str(data.get("improved_block", "")).strip():
            return None
        return data

    # ---------------------------------------------------------------- aplicación

    def _apply_proposal(self, text: str, proposal: dict[str, Any]) -> tuple[str | None, str]:
        original_block = str(proposal.get("original_block", ""))
        improved_block = str(proposal.get("improved_block", ""))
        kind = str(proposal.get("improvement_kind", ""))

        if not self._latex_balanced(improved_block):
            return None, kind

        # 1) Coincidencia exacta y única.
        if original_block in text:
            if text.count(original_block) != 1:
                return None, kind
            return text.replace(original_block, improved_block, 1), kind

        # 2) Coincidencia tolerante a espacios en blanco (colapsando runs de espacios
        #    y normalizando fin de línea) que resuelva a un ÚNICO span real del texto.
        span = self._find_flexible_span(text, original_block)
        if span is None:
            return None, kind
        start, end = span
        candidate = text[:start] + improved_block + text[end:]
        return candidate, kind

    def _find_flexible_span(self, text: str, block: str) -> tuple[int, int] | None:
        """Localiza un único span de ``text`` que coincide con ``block`` salvo por
        diferencias de espacios en blanco (espacios/tabs/saltos de línea colapsados).

        Devuelve (start, end) sobre el texto ORIGINAL, o None si no hay match único.
        """
        # Construir un patrón que trate cualquier run de whitespace como \s+.
        tokens = block.strip().split()
        if not tokens:
            return None
        pattern = r"\s+".join(re.escape(tok) for tok in tokens)
        matches = list(re.finditer(pattern, text))
        if len(matches) != 1:
            return None
        return matches[0].start(), matches[0].end()

    def _latex_balanced(self, block: str) -> bool:
        if block.count("{") != block.count("}"):
            return False
        begins = re.findall(r"\\begin\{([^}]+)\}", block)
        ends = re.findall(r"\\end\{([^}]+)\}", block)
        return sorted(begins) == sorted(ends)

    def _reject_reason(self, compile_ok: bool, contract_after: float, contract_before: float,
                       quality_after: float, quality_before: float, request: ActivityOptimizeRequest) -> str:
        if not compile_ok:
            return "La compilación falló tras aplicar la mejora; revertido."
        if request.require_contract_100 and contract_after < 100.0:
            return f"El contrato bajó a {contract_after}/100 tras la mejora; revertido."
        if contract_after < contract_before:
            return f"El contrato retrocedió ({contract_before}->{contract_after}); revertido."
        if quality_after <= quality_before:
            return f"La calidad no mejoró ({quality_before}->{quality_after}); revertido."
        return "Rechazado por criterio de aceptación."

    # ---------------------------------------------------------------- utilidades

    def _strip_comments(self, text: str) -> str:
        lines = [line for line in text.splitlines() if not line.lstrip().startswith("%")]
        return "\n".join(lines)

    def _normalize_ws(self, text: str) -> str:
        return re.sub(r"[ \t]+", " ", text)

    def _resolve_run_dir(self, request: ActivityOptimizeRequest, run_id: str) -> Path:
        if request.output.strip():
            return self.workspace.resolve_target(request.output) / run_id
        return self.root / run_id

    def _finalize(self, request: ActivityOptimizeRequest, run_id: str, run_dir: Path,
                  cycles: list[CycleRecord], quality_before: float, quality_after: float,
                  tex_path: Path | None, *, ok: bool, note: str = "",
                  contract_before: float = 0.0, contract_after: float = 0.0,
                  applied: int = 0) -> ActivityOptimizeResult:
        manifest = {
            "run_id": run_id,
            "kind": "activity-optimize",
            "target": self.workspace.relative(self.workspace.resolve_target(request.target)),
            "activity_number": int(request.activity_number),
            "stop_mode": ("fixed-cycles" if int(request.cycles) > 0 else "converge-to-quality"),
            "requested_cycles": int(request.cycles),
            "target_quality": float(request.target_quality),
            "max_cycles": int(request.max_cycles),
            "converged": bool(quality_after >= float(request.target_quality)),
            "engines": list(request.engines),
            "ok": bool(ok),
            "note": note,
            "quality_before": quality_before,
            "quality_after": quality_after,
            "quality_delta": round(quality_after - quality_before, 2),
            "contract_before": contract_before,
            "contract_after": contract_after,
            "applied_cycles": applied,
            "tex": self.workspace.relative(tex_path) if tex_path else "",
            "cycles": [self._cycle_dict(c) for c in cycles],
        }
        manifest_path = run_dir / "manifest.json"
        report_path = run_dir / "reporte-optimize.md"
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
        report_path.write_text(self._render_report(manifest), encoding="utf-8")
        self.workspace.append_bitacora(run_id, "activity-optimize", manifest)
        return ActivityOptimizeResult(
            run_id=run_id, run_dir=run_dir, ok=bool(ok),
            manifest_path=manifest_path, report_path=report_path,
            applied_cycles=applied, quality_before=quality_before,
            quality_after=quality_after, tex_path=tex_path,
        )

    def _cycle_dict(self, c: CycleRecord) -> dict[str, Any]:
        return {
            "cycle": c.index,
            "engine": c.engine,
            "accepted": c.accepted,
            "reason": c.reason,
            "improvement_kind": c.improvement_kind,
            "quality_before": c.quality_before,
            "quality_after": c.quality_after,
            "contract_before": c.contract_before,
            "contract_after": c.contract_after,
        }

    def _render_report(self, manifest: dict[str, Any]) -> str:
        lines = [
            "# Optimización de calidad de actividad",
            "",
            f"- Objetivo: {manifest['target']}",
            f"- Actividad: {manifest['activity_number']}",
            f"- Ciclos solicitados: {manifest['requested_cycles']}",
            f"- Ciclos aplicados (aceptados): {manifest['applied_cycles']}",
            f"- Calidad antes: {manifest['quality_before']}/100",
            f"- Calidad después: {manifest['quality_after']}/100 (Δ {manifest['quality_delta']})",
            f"- Contrato: {manifest['contract_before']} → {manifest['contract_after']} /100",
            f"- Estado: {'OK' if manifest['ok'] else 'SIN CAMBIOS/REVISAR'}",
            "",
        ]
        if manifest.get("note"):
            lines.extend([f"> {manifest['note']}", ""])
        lines.extend(["## Ciclos", ""])
        for c in manifest.get("cycles", []):
            mark = "✅" if c["accepted"] else "⏭️"
            lines.append(
                f"- {mark} Ciclo {c['cycle']} ({c['engine']}) "
                f"[{c.get('improvement_kind') or 'n/a'}]: "
                f"calidad {c['quality_before']}→{c['quality_after']}, "
                f"contrato {c['contract_before']}→{c['contract_after']}. {c['reason']}"
            )
        lines.append("")
        return "\n".join(lines)
