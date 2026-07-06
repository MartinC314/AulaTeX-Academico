from __future__ import annotations

from typing import Any


ACTIVITY_1_CONTRACT = {
    "required": {
        "objective": True,
        "instruction_source": True,
        "didactic_technique": True,
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
}


def evaluate_activity_contract(state: dict[str, Any]) -> dict[str, Any]:
    signals = state.get("signals", {})
    observed = state.get("observed_state", {})
    required_checks = {
        "objective": bool(signals.get("objective_present") or signals.get("extractor_objective_present")),
        "instruction_source": bool(signals.get("purpose_present") or signals.get("extractor_planeacion_present")),
        "didactic_technique": bool(
            signals.get("didactic_technique_present")
            or signals.get("product_visual_detected")
            or signals.get("extractor_verbs_count", 0) > 0
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
        "output_format": "No se detecta un formato de salida consistente para la actividad.",
        "bibliography": "La bibliografía no cumple el mínimo contractual.",
        "traceability": "La trazabilidad entre actividad, citas y extractor es insuficiente.",
        "evaluation_criteria": "No se detectan criterios de evaluación o entrega suficientemente explícitos.",
        "final_reflection": "No se detecta cierre argumentativo o conclusión final.",
        "sections_range": "La estructura de secciones queda fuera del rango contractual.",
        "concepts_min": "La cobertura conceptual extraída está por debajo del mínimo contractual.",
    }
    return messages.get(name, f"Incumplimiento contractual: {name}.")