from __future__ import annotations

from typing import Any


DIDACTIC_TECHNIQUE_CONTRACTS = {
    "cuestionario_diagnostico": {
        "aliases": ("cuestionario", "diagnóstico", "diagnostico", "reactivo"),
        "required_visible_elements": ("pregunta", "respuesta", "justificación"),
        "preservation_rule": "Si el insumo es cuestionario, el desarrollo visible debe conservar reactivos, respuestas y justificaciones en tabla compacta o lista estructurada; no debe transformarse en ensayo salvo que la consigna lo pida.",
    },
    "estudio_de_caso": {
        "aliases": ("caso", "estudio de caso", "situación", "situacion"),
        "required_visible_elements": ("hechos", "análisis", "conclusión"),
        "preservation_rule": "Si el insumo es caso, conservar hechos relevantes, actores, problema y resolución argumentada.",
    },
    "mapa_conceptual": {
        "aliases": ("mapa conceptual", "conceptos", "diagrama"),
        "required_visible_elements": ("conceptos", "relaciones", "lectura explicativa"),
        "preservation_rule": "Si el producto es mapa conceptual, conservar jerarquía, relaciones y explicación breve de lectura.",
    },
    "tabla_didactica": {
        "aliases": ("tabla", "cuadro", "cuadro comparativo", "longtable", "tabular"),
        "required_visible_elements": ("título", "encabezados", "filas", "criterio de lectura"),
        "preservation_rule": "Si la técnica usa tabla o cuadro, conservar estructura tabular visible con título/caption, encabezados claros, filas completas y una lectura breve; usar longtable, landscape, scriptsize, tabcolsep y arraystretch cuando el contenido sea amplio.",
    },
    "foro_diagnostico": {
        "aliases": ("foro", "foro diagnóstico", "foro diagnostico"),
        "required_visible_elements": ("preguntas guía", "respuesta", "cierre"),
        "preservation_rule": "Si el producto es foro diagnóstico, conservar preguntas guía y respuestas compactas sin convertirlo en ensayo extenso.",
    },
}

ACTIVITY_1_CONTRACT = {
    "required": {
        "objective": True,
        "instruction_source": True,
        "didactic_technique": True,
        "didactic_format_preserved": True,
        "output_format": True,
        "bibliography": True,
        "traceability": True,
        "evaluation_criteria": True,
        "final_reflection": True,
    },
    "acceptable_ranges": {
        "sections_min": 3,
        "sections_max": 8,
        "bibliography_entries_min": 3,
        "concepts_min": 5,
    },
    "didactic_techniques": DIDACTIC_TECHNIQUE_CONTRACTS,
}


def evaluate_activity_contract(state: dict[str, Any]) -> dict[str, Any]:
    signals = state.get("signals", {})
    observed = state.get("observed_state", {})
    required_checks = {
        "objective": bool(signals.get("objective_present") or signals.get("extractor_objective_present")),
        "instruction_source": bool(signals.get("purpose_present") or signals.get("extractor_planeacion_present")),
        "didactic_technique": bool(
            signals.get("didactic_technique_present")
            or signals.get("questionnaire_detected")
            or signals.get("case_study_detected")
            or signals.get("product_visual_detected")
            or signals.get("extractor_verbs_count", 0) > 0
        ),
        "didactic_format_preserved": bool(
            signals.get("questionnaire_contract_satisfied")
            or signals.get("table_contract_satisfied")
            or (not signals.get("questionnaire_detected") and signals.get("didactic_technique_present"))
            or signals.get("product_visual_detected")
        ),
        "output_format": bool(state.get("target_tex")) and bool(signals.get("product_visual_detected") or state.get("target_pdf")),
        "bibliography": bool(observed.get("bibliography_ready")) and int(signals.get("cited_keys_count", 0)) >= ACTIVITY_1_CONTRACT["acceptable_ranges"]["bibliography_entries_min"],
        "traceability": bool(observed.get("extractor_ready")) and int(signals.get("cited_keys_count", 0)) >= 3,
        "evaluation_criteria": bool(signals.get("evaluation_criteria_present") or signals.get("extractor_criteria_count", 0) > 0),
        "final_reflection": bool(signals.get("conclusion_present")),
    }
    range_checks = {
        "sections_range": ACTIVITY_1_CONTRACT["acceptable_ranges"]["sections_min"]
        <= int(signals.get("sections_count", 0))
        <= ACTIVITY_1_CONTRACT["acceptable_ranges"]["sections_max"],
        "concepts_min": int(signals.get("extractor_concepts_count", 0)) >= ACTIVITY_1_CONTRACT["acceptable_ranges"]["concepts_min"],
    }
    all_checks = {**required_checks, **range_checks}
    required_hits = sum(1 for ok in required_checks.values() if ok)
    score = round(100 * sum(1 for ok in all_checks.values() if ok) / max(1, len(all_checks)), 2)
    findings = [
        _contract_finding(name)
        for name, ok in all_checks.items()
        if not ok
    ]
    passed = score >= 80 and required_hits >= 6 and range_checks["sections_range"]
    return {
        "score": score,
        "passed": passed,
        "required_hits": required_hits,
        "required_total": len(required_checks),
        "checks": all_checks,
        "required_checks": required_checks,
        "range_checks": range_checks,
        "findings": findings,
        "contract": ACTIVITY_1_CONTRACT,
    }


def _contract_finding(name: str) -> str:
    messages = {
        "objective": "Falta objetivo pedagógico verificable en TEX o planeación.",
        "instruction_source": "No hay evidencia suficiente de consigna o propósito instruccional.",
        "didactic_technique": "No se detecta con claridad la técnica didáctica o el producto esperado.",
        "didactic_format_preserved": "La técnica didáctica detectada no se preserva en el desarrollo; por ejemplo, un cuestionario debe conservar pregunta, respuesta y justificación.",
        "output_format": "No se detecta un formato de salida consistente para la actividad.",
        "bibliography": "La bibliografía no cumple el mínimo contractual.",
        "traceability": "La trazabilidad entre actividad, citas y extractor es insuficiente.",
        "evaluation_criteria": "No se detectan criterios de evaluación o entrega suficientemente explícitos.",
        "final_reflection": "No se detecta cierre argumentativo o conclusión final.",
        "sections_range": "La estructura de secciones queda fuera del rango contractual.",
        "concepts_min": "La cobertura conceptual extraída está por debajo del mínimo contractual.",
    }
    return messages.get(name, f"Incumplimiento contractual: {name}.")