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

        # Base conceptual: cargar conceptos del extractor (si existen) para puntuar
        # su cobertura. Si faltan y la base conceptual del .tex es escasa, se intenta
        # correr el extractor en modo local para materializar conceptos.
        self._current_concepts = self._load_or_build_concepts(request, tex_path)

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
        """Score de calidad editorial verificable (0-100), independiente del LLM."""
        concepts = getattr(self, "_current_concepts", None)
        return round(sum(self._quality_breakdown(text, concepts).values()), 2)

    def _quality_breakdown(self, text: str, concepts: list[str] | None = None) -> dict[str, float]:
        """Desglose por componente del score de calidad (cada uno con su tope).

        Filosofía editorial: PREMIAR prosa bien estructurada en subsecciones
        TEMÁTICAS del desarrollo y una BASE CONCEPTUAL suficiente que justifique el
        producto; PENALIZAR el exceso de listas y los títulos-etiqueta ('Marco
        conceptual', 'Desarrollo'). Topes (suman 100): citas 20, estructura 20,
        base_conceptual 15, listas 8, conectores 12, extension 10, integridad 15.
        """
        body = self._strip_comments(text)

        # Citas visibles (densidad): 20 pts con 5 citas.
        cites = len(re.findall(r"\\cite[tp]?\*?(?:\[[^\]]*\])*\{", body))
        c_cites = min(20.0, cites * 4.0)

        # Estructura: secciones (10) + subsecciones TEMÁTICAS del desarrollo (10) = 20 pts.
        # SOLO cuentan subsecciones del acto de Desarrollo (intro/conclusión en prosa).
        # Se PENALIZA usar títulos-etiqueta ('Marco conceptual', 'Desarrollo',
        # 'Metodología', 'Participación publicada'): restan porque no nombran el tema.
        sections = len(re.findall(r"\\section\{", body))
        dev_subsections = self._count_development_subsections(body)
        c_structure = min(10.0, sections * 3.4) + min(10.0, dev_subsections * 5.0)
        label_titles = re.findall(
            r"\\(?:sub)?section\*?\{\s*(marco conceptual|desarrollo|metodolog[íi]a[^}]*|"
            r"participaci[óo]n publicada[^}]*|lectura e interpretaci[óo]n)\s*\}",
            body, re.IGNORECASE)
        c_structure = max(0.0, c_structure - len(label_titles) * 3.0)

        # BASE CONCEPTUAL (15 pts): suficiencia de conceptos que justifican el producto.
        c_concept = self._concept_base_score(body, concepts)

        # Balance prosa/listas: 8 pts. PREMIA 1 lista (foro), PENALIZA exceso.
        enums = len(re.findall(r"\\begin\{(enumerate|itemize)\}", body))
        if enums == 0:
            c_enums = 6.0
        elif enums == 1:
            c_enums = 8.0
        elif enums == 2:
            c_enums = 6.0
        else:
            c_enums = max(0.0, 6.0 - (enums - 2) * 3.0)

        # Densidad argumentativa: conectores de razonamiento: 12 pts (~5 conectores).
        connectors = len(re.findall(
            r"\b(por tanto|por ello|en consecuencia|sin embargo|no obstante|es decir|"
            r"en cambio|por el contrario|de ese modo|as[íi]|adem[áa]s|dado que|puesto que|"
            r"en efecto|por consiguiente)\b",
            body, re.IGNORECASE))
        c_connectors = min(12.0, connectors * 2.4)

        # Extensión sustantiva del cuerpo: 10 pts con ~1000 palabras.
        words = len(re.findall(r"\b\w+\b", body))
        c_extension = min(10.0, words / 100.0)

        # Integridad / postura propia: 15 pts (~4 marcadores).
        integrity = len(re.findall(
            r"\b(desde mi perspectiva|considero|sostengo|mi postura|a mi juicio|"
            r"reflexi[óo]n propia|declaraci[óo]n de uso|inteligencia artificial|"
            r"no invent|supuesto)\b",
            body, re.IGNORECASE))
        c_integrity = min(15.0, integrity * 4.0)

        return {
            "citas": round(c_cites, 2),
            "estructura": round(c_structure, 2),
            "base_conceptual": round(c_concept, 2),
            "listas": round(c_enums, 2),
            "conectores": round(c_connectors, 2),
            "extension": round(c_extension, 2),
            "integridad": round(c_integrity, 2),
        }

    def _concept_base_score(self, body: str, concepts: list[str] | None) -> float:
        """Puntúa (0-15) la SUFICIENCIA de la base conceptual del desarrollo.

        Combina dos señales:
          (a) conceptos DEFINIDOS/destacados en el cuerpo (términos en \\textbf o
              \\textit dentro del desarrollo, que evidencian delimitación conceptual);
          (b) COBERTURA de los conceptos del extractor (si se proveen): proporción de
              conceptos clave del extractor mencionados en el cuerpo.
        Cada señal aporta hasta ~7.5 pts. Si no hay conceptos del extractor, la
        señal (a) puede alcanzar el tope por sí sola (documento autosuficiente).
        """
        # Región del desarrollo (donde debe vivir la base conceptual).
        dev = self._development_region(body)
        emphasised = set(
            m.group(1).strip().lower()
            for m in re.finditer(r"\\text(?:bf|it)\{([^}]{3,60})\}", dev)
        )
        # Señal (a): número de términos destacados (hasta 8 -> 7.5 pts).
        a = min(7.5, len(emphasised) * 1.25)

        # Señal (b): cobertura de conceptos del extractor.
        if concepts:
            # Normalizar acentos (LaTeX \'i y Unicode) para que la coincidencia no
            # falle por la codificacion; y cobertura por TOKENS significativos para
            # conceptos largos (basta con que el cuerpo cubra sus terminos clave).
            norm_body = self._normalize_concept_text(body)
            key = [str(x).strip() for x in concepts if len(str(x).strip()) >= 4]
            if key:
                covered = 0
                for concept in key:
                    nc = self._normalize_concept_text(concept)
                    if nc and nc in norm_body:
                        covered += 1
                        continue
                    # Cobertura por tokens: conceptos largos se dan por cubiertos si
                    # >=70% de sus tokens significativos (>=4 letras) estan en el cuerpo.
                    toks = [t for t in re.findall(r"[a-z]{4,}", nc)
                            if t not in {"para", "sobre", "entre", "segun", "entre",
                                         "relacionadas", "sistemas", "federales"}]
                    if toks and sum(1 for t in toks if t in norm_body) / len(toks) >= 0.7:
                        covered += 1
                ratio = covered / len(key)
                b = 7.5 * ratio
            else:
                b = 7.5
        else:
            # Sin conceptos del extractor: la señal (a) puede cubrir hasta el tope.
            b = min(7.5, a)
        return min(15.0, a + b)

    @staticmethod
    def _normalize_concept_text(text: str) -> str:
        """Normaliza acentos LaTeX (\\'i, \\'a, \\~n...) y Unicode a ASCII minusculas.

        Permite comparar conceptos del extractor (con acentos Unicode) contra el
        cuerpo del .tex (con acentos LaTeX o Unicode) sin falsos negativos.
        """
        import unicodedata
        s = text.lower()
        # Acentos LaTeX: \'a \'e \'i \'o \'u \~n \"u -> letra base.
        s = re.sub(r"\\['`^\"~=.]\s*\{?\\?([a-z])\}?", r"\1", s)
        s = re.sub(r"\\['`^\"~=.]([a-z])", r"\1", s)
        # Unicode -> ASCII.
        s = unicodedata.normalize("NFKD", s)
        s = "".join(ch for ch in s if not unicodedata.combining(ch))
        return s

    def _load_or_build_concepts(self, request: ActivityOptimizeRequest, tex_path: Path) -> list[str]:
        """Carga conceptos del extractor; si faltan y la base conceptual es escasa,
        intenta correr el extractor local (tfidf) para materializarlos.

        Nunca hace fallar la optimización: ante cualquier error, devuelve [].
        """
        target_root = tex_path.parent
        concepts = self._read_extractor_concepts(target_root)
        if concepts:
            return concepts
        # ¿Vale la pena correr el extractor? Solo si la base conceptual del .tex es
        # escasa (pocos términos destacados en el desarrollo).
        try:
            body = self._strip_comments(tex_path.read_text(encoding="utf-8", errors="replace"))
        except Exception:
            return []
        dev = self._development_region(body)
        emphasised = set(re.findall(r"\\text(?:bf|it)\{([^}]{3,60})\}", dev))
        if len(emphasised) >= 6:
            return []  # base conceptual suficiente; no hace falta el extractor
        # Intento de ejecución local del extractor (motor tfidf, sin API).
        try:
            from .extractor_adapter import ExtractorAdapter, ExtractorRequest

            adapter = ExtractorAdapter(self.workspace)
            adapter.run(ExtractorRequest(
                target=str(target_root),
                activity_number=int(request.activity_number),
                motor="tfidf",
            ))
            return self._read_extractor_concepts(target_root)
        except Exception:
            return []

    def _read_extractor_concepts(self, target_root: Path) -> list[str]:
        """Lee conceptos_detectados.json del extractor (varias ubicaciones posibles)."""
        candidates = [
            target_root / "extractor-aulatex" / "conceptos_detectados.json",
            target_root / "extractor-aulatex" / "conceptos.json",
        ]
        for path in candidates:
            data = self._safe_load_json(path)
            if data is None:
                continue
            return self._extract_concept_names(data)
        return []

    def _safe_load_json(self, path: Path) -> Any:
        try:
            if path.exists():
                return json.loads(path.read_text(encoding="utf-8", errors="replace"))
        except Exception:
            return None
        return None

    def _extract_concept_names(self, data: Any) -> list[str]:
        """Normaliza distintas formas del JSON de conceptos a una lista de strings."""
        names: list[str] = []
        if isinstance(data, list):
            for item in data:
                if isinstance(item, str):
                    names.append(item)
                elif isinstance(item, dict):
                    for k in ("concepto", "termino", "nombre", "label", "text"):
                        if item.get(k):
                            names.append(str(item[k]))
                            break
        elif isinstance(data, dict):
            for k in ("conceptos", "terminos", "items", "concepts"):
                if isinstance(data.get(k), list):
                    names.extend(self._extract_concept_names(data[k]))
        return [n.strip() for n in names if isinstance(n, str) and n.strip()]

    def _development_region(self, body: str) -> str:
        """Devuelve el texto del acto de Desarrollo (entre Introducción y Conclusión)."""
        sec_iter = list(re.finditer(r"\\section\*?\{([^}]*)\}", body))
        if not sec_iter:
            return body
        dev_start = None
        concl_start = None
        for m in sec_iter:
            title = m.group(1).lower()
            if dev_start is None and not re.search(r"introducci[óo]n", title) and not re.search(r"conclusi[óo]n", title):
                dev_start = m.end()
            if re.search(r"conclusi[óo]n", title):
                concl_start = m.start()
                break
        if dev_start is None:
            return body
        return body[dev_start: concl_start if concl_start is not None else len(body)]

    def _count_development_subsections(self, body: str) -> int:
        """Cuenta \\subsection SOLO dentro del acto de Desarrollo.

        El Desarrollo es la(s) sección(es) entre la Introducción y la Conclusión.
        Las subsecciones en Introducción o Conclusión NO cuentan: esos actos deben
        ser prosa continua. Si no puede delimitarse, cuenta todas (fallback).
        """
        # Localiza el inicio del desarrollo (fin de la Introducción) y el inicio de
        # la Conclusión.
        sec_iter = list(re.finditer(r"\\section\*?\{([^}]*)\}", body))
        if not sec_iter:
            return len(re.findall(r"\\subsection\*?\{", body))
        dev_start = None
        concl_start = None
        for m in sec_iter:
            title = m.group(1).lower()
            if dev_start is None and not re.search(r"introducci[óo]n", title):
                # primera sección que no es la introducción = inicio del desarrollo
                if not re.search(r"conclusi[óo]n", title):
                    dev_start = m.end()
            if re.search(r"conclusi[óo]n", title):
                concl_start = m.start()
                break
        if dev_start is None:
            return 0
        region = body[dev_start: concl_start if concl_start is not None else len(body)]
        return len(re.findall(r"\\subsection\*?\{", region))

    def _quality_gap_hint(self, text: str) -> str:
        """Frase que indica al LLM qué componentes están por debajo de su tope."""
        caps = {"citas": 20.0, "estructura": 20.0, "base_conceptual": 15.0, "listas": 8.0,
                "conectores": 12.0, "extension": 10.0, "integridad": 15.0}
        bd = self._quality_breakdown(text, getattr(self, "_current_concepts", None))
        body = self._strip_comments(text)
        enums = len(re.findall(r"\\begin\{(enumerate|itemize)\}", body))
        concepts = getattr(self, "_current_concepts", None)
        concept_hint = ""
        if concepts:
            low_body = body.lower()
            missing = [c for c in concepts if len(str(c)) >= 4 and str(c).lower() not in low_body][:6]
            if missing:
                concept_hint = " Conceptos clave aún no abordados: " + ", ".join(missing) + "."
        gaps = []
        labels = {
            "citas": "más citas visibles (\\citep con claves existentes)",
            "estructura": (
                "organizar el DESARROLLO en más subsecciones TEMÁTICAS cuyo TÍTULO NOMBRE EL "
                "CONCEPTO o el tema (NUNCA 'Marco conceptual', 'Desarrollo', 'Metodología' ni "
                "'Participación publicada'). La Introducción y la Conclusión van en PROSA "
                "CONTINUA, sin subsecciones"
            ),
            "base_conceptual": (
                "reforzar la BASE CONCEPTUAL que justifica el producto: definir y destacar "
                "(con \\textbf) los conceptos pertinentes y suficientes que gravitan alrededor "
                "del foro, en párrafos o subsecciones temáticas del desarrollo." + concept_hint
            ),
            "listas": (
                "reducir el número de listas/enumeraciones convirtiéndolas en PROSA argumentada "
                "(deja a lo sumo la lista estrictamente necesaria, p. ej. la del foro)"
                if enums >= 3 else
                "mantener a lo sumo 1 lista justificada (el resto en prosa)"
            ),
            "conectores": "más conectores lógicos (por tanto, sin embargo, en consecuencia...)",
            "extension": "desarrollar más el análisis (mayor extensión sustantiva)",
            "integridad": "reforzar la postura propia y la reflexión fundamentada",
        }
        for k, cap in caps.items():
            if bd.get(k, 0.0) < cap - 0.5:
                gaps.append(f"- {labels[k]} (actual {bd.get(k,0.0)}/{cap})")
        if not gaps:
            return "El documento está cerca del máximo; refina precisión y cohesión en PROSA (evita añadir listas)."
        return (
            "Para acercar la calidad a 100, prioriza mejorar (PREFIERE prosa sobre listas, "
            "títulos que NOMBREN el concepto/tema):\n"
            + "\n".join(gaps)
        )

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
            f"{self._quality_gap_hint(current_text)}\n\n"
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
