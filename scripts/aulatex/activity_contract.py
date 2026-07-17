from __future__ import annotations

from typing import Any


REALIZAR_ACTIVIDAD_PIPELINE_CONTRACT = {
    "intent": "realizar-actividad",
    "purpose": "Tomar un nodo, carpeta o archivo de actividad y llevarlo desde memoria e insumos hasta TEX/PDF final validado mediante ciclos repetibles.",
    "inputs": {
        "target": "archivo TEX, carpeta de materia o nodo de actividad",
        "activity_number": "número de actividad cuando aplica",
        "local_sources": "notas, PDF, Markdown, planeación, programa de asignatura, referencias, bibliografía y memorias editoriales locales",
        "online_sources": "fuentes institucionales, normativas, académicas o web verificables; obligatorias cuando las respuestas del cuestionario no estén sustentadas por corpus local suficiente",
        "answered_questionnaire": "reactivos, respuestas correctas y justificaciones; deben validarse contra fuentes locales sólidas o fuentes en línea verificables antes de consolidarse en TEX/PDF",
        "editorial_memory_nodes": "memoria local, ascendente y nodos editoriales relacionados; deben consultarse antes de redactar o corregir",
        "engines": "motores LLM configurados para planificar, investigar, redactar, evaluar y criticar",
    },
    "phases": [
        {
            "id": "discover_node",
            "goal": "Resolver scope editorial, TEX canónico, bibliografía, PDF esperado, memoria local y fuentes de referencia.",
            "outputs": ("scope", "target_tex", "target_pdf", "bib", "memory_bundle", "source_inventory"),
        },
        {
            "id": "build_editorial_memory",
            "goal": "Construir, refrescar y consultar memoria editorial local, ascendente y nodos relacionados antes de redactar.",
            "actions": ("editorial-memory local", "editorial-memory ascendente", "recuperación de nodos hermanos", "resumen de reglas del nodo"),
        },
        {
            "id": "ingest_sources",
            "goal": "Extraer e incorporar notas, programas, PDF, Markdown, referencias locales y memoria editorial; buscar fuentes externas cuando falte sustento formal.",
            "actions": ("extractor", "pdftotext si hay PDF", "investigation local", "investigation online", "normalización de corpus"),
        },
        {
            "id": "validate_questionnaire_inputs",
            "goal": "Validar reactivos, respuestas y justificaciones del cuestionario contra fuentes locales sólidas o fuentes en línea verificables antes de consolidar la redacción.",
            "actions": ("contrastar respuestas con bibliografía local", "consultar fuentes institucionales/académicas si falta sustento", "marcar respuestas dudosas", "actualizar .bib con fuentes verificables"),
            "outputs": ("validated_answers", "source_support_map", "unresolved_or_doubtful_answers"),
        },
        {
            "id": "detect_contracts",
            "goal": "Detectar técnica didáctica, formato solicitado, criterios de entrega, rúbrica, subject/título y bibliografía mínima.",
            "outputs": ("didactic_contract", "delivery_contract", "bibliography_contract", "heading_contract"),
        },
        {
            "id": "draft_or_repair_content",
            "goal": "Crear o mejorar el TEX conservando la técnica didáctica y elevando rigor, fuentes y redacción.",
            "actions": ("agent realizar-actividad", "activity-revise --apply", "bibliography-repair --apply"),
        },
        {
            "id": "evaluate_quality",
            "goal": "Observar contrato de actividad, trazabilidad, cobertura conceptual, citas, redacción, formato y coherencia jurídica/académica.",
            "actions": ("activity-observe --compile-check", "quality gates", "crítica adversarial"),
        },
        {
            "id": "compile_and_repair",
            "goal": "Compilar PDF, clasificar errores, reparar bibliografía o LaTeX y verificar frescura del PDF.",
            "actions": ("latexmk-build", "compilation-repair", "bibliography-repair"),
        },
        {
            "id": "repeat_until_pass",
            "goal": "Repetir memoria, extracción, redacción, evaluación y compilación hasta aprobar criterios o agotar ciclos.",
            "stop_conditions": ("activity_contract.passed", "pdf_fresh", "sin citas indefinidas", "sin placeholders", "consensus_score suficiente"),
        },
        {
            "id": "align_report_and_presentation",
            "goal": "Cuando existan reporte y presentación de la misma actividad, alinear la presentación con el reporte: reflejar conceptos, profundidad, fuentes y conclusión, conservando el estilo Beamer institucional y añadiendo una diapositiva de referencias APA y declaración de IA si aplica.",
            "actions": ("comparar reporte vs presentación", "actualizar diapositivas desfasadas", "espejar estructura y fuentes", "compilar presentación", "verificar visualmente"),
            "outputs": ("presentacion_alineada", "presentacion_pdf"),
        },
        {
            "id": "promote_artifacts",
            "goal": "Persistir TEX, PDF, .bib, extractor, memoria, manifiestos, reportes y bitácora de decisión.",
            "outputs": ("tex_final", "pdf_final", "memory", "manifest", "quality_report"),
        },
    ],
    "quality_gates": {
        "memory": "memoria local, ascendente y nodos editoriales relacionados consultados antes de redactar o corregir",
        "sources": "fuentes locales incorporadas y fuentes formales citables cuando haya afirmaciones sustantivas",
        "questionnaire_validation": "si hay cuestionario resuelto, cada respuesta y justificación debe estar contrastada con bibliografía local sólida o fuentes en línea verificables; respuestas dudosas se marcan o se corrigen antes de compilar",
        "online_validation": "si el corpus local no sustenta una respuesta, ejecutar investigación en línea con fuentes institucionales, académicas, normativas o editoriales confiables y materializarlas en .bib",
        "didactic_format": "la forma visible del producto respeta cuestionario, foro, caso, mapa, tabla u otro contrato",
        "headings": "título sin Actividad #; subtítulo compacto; subject/equivalente = Actividad # - Materia",
        "bibliography": "todas las citas visibles tienen entrada .bib, no hay entradas inventadas y el número de referencias aumenta cuando el corpus previo no sostiene todas las respuestas",
        "visible_citations": "las fuentes nuevas deben aparecer como citas visibles en introducción, marco conceptual, tabla o conclusión; no basta con agregar entradas al .bib",
        "reference_growth": "si realizar-actividad valida cuestionarios o afirmaciones sustantivas, debe incrementar o confirmar explícitamente el mapa de soporte bibliográfico: mínimo 3 fuentes sólidas para actividad simple y mínimo 5 para cuestionarios extensos, salvo memoria local suficiente documentada",
        "content": "sin placeholders, con contexto/problema integrado en introducción, análisis propio integrado en conclusión, postura personal integrada en conclusión y transferencia profesional",
        "visible_style": "sin metadiscurso de ejecución: no hablar de 'esta actividad', 'producto solicitado', 'se presenta' o 'la técnica usada' como narrador externo; hablar del tema, problema, concepto, cuestionario, caso o tabla según corresponda",
        "organization_notes": "el criterio de organización, técnica didáctica, herramienta didáctica, nivel cognitivo aplicado o trazabilidad metodológica debe quedar comentado en TEX cuando no sea parte solicitada del producto visible",
        "introduction": "la introducción absorbe contexto y problema; evitar una subsección visible separada 'Contexto y problema' salvo consigna expresa",
        "development_section": "si el producto es cuestionario, la sección Desarrollo debe estar ocupada por el cuestionario con su título; el marco conceptual va dentro de esa misma sección, no como sección/subsección independiente salvo consigna expresa",
        "conclusion": "la conclusión integra síntesis, análisis propio, postura personal, razón y consecuencia; evitar secciones visibles separadas de 'Análisis propio' o 'Postura personal' salvo consigna expresa",
        "compile": "PDF existe, está fresco y no presenta errores críticos ni citas indefinidas",
        "report_presentation_alignment": "cuando existan reporte y presentación de la misma actividad, la presentación debe reflejar el contenido, la profundidad, los conceptos, las fuentes y la conclusión del reporte, con estilo Beamer institucional y una diapositiva final de referencias APA y declaración de IA si el reporte la incluye",
    },
    "source_validation_rules": {
        "questionnaire_answers": (
            "Todo cuestionario resuelto requiere mapa de soporte: reactivo -> respuesta -> fuente local o fuente en línea verificable. "
            "No basta con respuestas autogeneradas, memoria interna ni entradas .bib sin citas visibles."
        ),
        "visible_reference_growth": (
            "Cuando se valida información, el TEX final debe mostrar el incremento: citas visibles en el cuerpo y nuevas claves en .bib. "
            "Si no se agregan fuentes nuevas, debe existir memoria local suficiente y verificable que justifique no hacerlo."
        ),
        "local_first_online_when_needed": (
            "Priorizar bibliografía, programa, notas y memorias editoriales locales; si no alcanzan para validar, buscar fuentes en línea sólidas "
            "y registrarlas en .bib con citas visibles en TEX."
        ),
        "editorial_memory_first": (
            "Antes de redactar, consultar nodos de memoria editorial local, ascendente y relacionados para heredar reglas, tono, fuentes y decisiones previas."
        ),
        "no_unsupported_answers": "No consolidar respuestas dudosas sin marcarlas, corregirlas o respaldarlas con fuente verificable.",
    },
    "visible_text_rules": {
        "avoid_metadiscourse": (
            "En el cuerpo final no narrar el proceso de elaboración ni mencionar la palabra 'Actividad' como sujeto del análisis; "
            "en su lugar hablar del tema, problema, concepto, cuestionario, caso, tabla o fenómeno estudiado."
        ),
        "comment_organization_criteria": (
            "El criterio de organización, la técnica didáctica aplicada, la herramienta didáctica y la trazabilidad editorial se conservan como comentarios TEX "
            "si sirven al motor o a la memoria, pero no deben aparecer como sección visible salvo que la consigna lo pida."
        ),
        "fold_context_into_introduction": (
            "El contexto y el problema se integran en la introducción; no crear una subsección visible 'Contexto y problema' "
            "salvo instrucción expresa de la consigna."
        ),
        "comment_cognitive_level": (
            "El nivel cognitivo aplicado es guía metodológica para el motor y debe quedar comentado en TEX, no como subsección visible, "
            "salvo que la consigna lo pida expresamente."
        ),
        "questionnaire_as_development": (
            "Si el producto es cuestionario, la sección Desarrollo debe titular y contener directamente el cuestionario. "
            "El marco conceptual se integra dentro de esa sección como apoyo breve o comentario, no como bloque visible separado."
        ),
        "fold_analysis_into_conclusion": (
            "El análisis propio y la postura personal se integran en la conclusión mediante posición, razón y consecuencia; "
            "no crear secciones visibles independientes de análisis propio o postura personal salvo instrucción expresa."
        ),
        "prefer_theme_language": "Usar 'el tema', 'el problema', 'el cuestionario', 'la tabla', 'el caso' o el nombre del concepto antes que 'la actividad'.",
    },
    "compilation_rules": {
        "orphan_bbl": (
            "Si las citas salen como [?] o no aparece la lista de referencias, revisar si existe un .bbl HUÉRFANO y VACÍO junto al .tex "
            "(latexmk lo marca como 'Foreign .bbl' y no lo regenera). Solución: borrar el .bbl y .aux huérfanos y recompilar con "
            "latexmk -bibtex, asegurando TEXINPUTS y BIBINPUTS con la carpeta de la materia."
        ),
        "extractor_deps": (
            "El extractor scripts/extractor-conceptos-ideas requiere en el .venv: scikit-learn, pandas, pymupdf, python-docx, openpyxl, "
            "numpy, python-dotenv y anthropic. Ante ModuleNotFoundError, instalar la dependencia faltante."
        ),
        "extractor_env": (
            "El adaptador del extractor debe cargar scripts/aulatex.env y exportar PYTHONUTF8=1 al subproceso para heredar credenciales "
            "Foundry y evitar UnicodeEncodeError en Windows (cp1252)."
        ),
        "encoding_safety": (
            "NUNCA editar archivos .tex con PowerShell (Set-Content / -replace): corrompe la codificación UTF-8 (mojibake doble). "
            "Usar siempre herramientas de edición que preserven UTF-8. Si ocurre mojibake, reparar con reemplazos dirigidos "
            "(Ã¡->á, Âº->º, â€\"->—) por Python, no re-decodificando todo el archivo."
        ),
        "build_command": (
            "Para builds con bibliografía y múltiples pasadas estables: cmd /c \"latexmk -f -pdf -bibtex -interaction=nonstopmode "
            "-output-directory=.build\\latex\\aux <src>\" con TEXINPUTS='.;<repo>\\base\\Plantilla-Informe;<carpeta-materia>;' y "
            "BIBINPUTS='<carpeta-materia>;'; luego copiar el PDF de .build\\latex\\aux al destino."
        ),
        "page_control": (
            "Usar \\clearpage para forzar que una sección (p. ej. Conclusión) inicie en su propia página. El entorno landscape siempre "
            "abre página nueva: compactar el contenido previo para evitar huecos."
        ),
        "verify_visually": (
            "Verificar el resultado renderizando páginas a PNG (pdftoppm) e inspeccionando el diagrama, no solo el returncode de compilación."
        ),
    },
    "iterative_improvement_rules": {
        "avoid_full_cycle_agent": (
            "Para MEJORAR incrementalmente contenido (agregar conceptos/relaciones) NO usar 'agent --cycle-mode full' con muchos ciclos: "
            "no es observable (guarda todo al final) y es vulnerable a cuelgues de red sin timeout (puede colgarse horas)."
        ),
        "prefer_observable_monitor": (
            "Preferir un bucle observable: activity-monitor (escribe por ciclo, aplica parches verificables, compila y cierra temprano si "
            "pasa el contrato) o un orquestador dedicado que en cada ciclo llame al LLM con timeout, integre el aporte, compile y revierta si rompe."
        ),
        "monitor_note": (
            "activity-monitor NO agrega conceptos nuevos (sus parches son deterministas: placeholders, criterios, bibliografía). Para "
            "enriquecer con razonamiento LLM se requiere un orquestador que pida subconceptos nuevos en JSON, deduplique contra lo existente "
            "y apile con tope por rama para no saturar el layout."
        ),
        "tex_target_priority": (
            "Al observar una actividad con reporte y presentación, priorizar el TEX de reporte (reporte-*) sobre la presentación al resolver "
            "el objetivo, porque el orden alfabético pondría 'presentacion-' primero."
        ),
    },
    "report_presentation_alignment_rules": {
        "principle": (
            "El reporte (reporte-*.tex) es la fuente de verdad; la presentación (presentacion-*.tex) debe reflejar su contenido y nivel de "
            "profundidad. Cuando el reporte se enriquece (más conceptos, principios, fuentes), la presentación debe actualizarse para no quedar desfasada."
        ),
        "content_parity": (
            "Cada eje/tema desarrollado en el reporte debe tener al menos una diapositiva que lo cubra con el mismo nivel de detalle esencial: "
            "conceptos clave, subconceptos relevantes, fundamentos normativos y ejemplos jurídicos verificables."
        ),
        "structure_mirror": (
            "La presentación debe reflejar la estructura del reporte: propósito/objetivo, metodología (si aplica), desarrollo por ejes, conclusión "
            "y una diapositiva final de Referencias (APA 7) más la declaración de uso de IA cuando el reporte la incluya."
        ),
        "style_rule": (
            "Conservar el estilo Beamer institucional (paleta UnADM, frametitle, footline). Usar bloques y columnas para condensar; una idea "
            "central por diapositiva; negritas para conceptos clave; sin saturar de texto."
        ),
        "consistency_checks": (
            "Verificar que fuentes citadas, principios (universalidad, interdependencia, indivisibilidad, progresividad, no regresión) y "
            "conceptos jurídicos (pro persona, interpretación conforme, control de convencionalidad, amparo, etc.) coincidan entre reporte y presentación."
        ),
        "compile_note": (
            "La presentación Beamer se compila con el mismo flujo latexmk (TEXINPUTS con la plantilla); verificar el número de diapositivas y "
            "revisar visualmente que no haya desbordes."
        ),
    },
    "recommended_cycle": (
        "editorial-memory local/ascendente/relacionada -> investigation con queries bibliográficas -> extractor/investigation local -> "
        "validación de cuestionario -> investigation online si falta sustento -> expansión .bib + citas visibles -> "
        "agent realizar-actividad -> activity-observe -> activity-revise/bibliography-repair -> latexmk-build -> repetir hasta aprobar"
    ),
}


DIDACTIC_TECHNIQUE_CONTRACTS = {
    "cuestionario_diagnostico": {
        "aliases": ("cuestionario", "diagnóstico", "diagnostico", "reactivo"),
        "required_visible_elements": ("pregunta", "respuesta", "justificación"),
        "preservation_rule": "Si el insumo es cuestionario, el desarrollo visible debe conservar reactivos, respuestas y justificaciones en tabla compacta o lista estructurada; no debe transformarse en ensayo salvo que la consigna lo pida.",
        "visible_style_rule": "No explicar en el texto visible que 'esta actividad' usa una técnica; si hace falta, dejar el criterio de organización o herramienta didáctica como comentario TEX y hablar del tema o del cuestionario.",
        "structure_rule": "Integrar contexto y problema en la introducción; si el producto es cuestionario, Desarrollo debe contener el cuestionario con su título y el marco conceptual debe integrarse dentro de la misma sección; nivel cognitivo aplicado va comentado salvo consigna expresa.",
        "closure_rule": "Integrar análisis propio y postura personal en la conclusión, con posición, razón y consecuencia.",
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
        "depth_rule": (
            "Un mapa conceptual sólido no puede ser esquelético: exige raíz + ramas del contenido temático + varios niveles de "
            "profundidad (subconceptos, subtipos, ejemplos jurídicos, fundamentos normativos y consecuencias). Cada rama debe tener "
            "al menos 3-4 conceptos; cubrir explícitamente todos los subtemas de la planeación (p. ej. antecedentes, generaciones, "
            "concepto, principios y garantías) sin omitir ninguno."
        ),
        "relations_rule": (
            "Las flechas deben llevar proposiciones de enlace explícitas (conectores como 'se rige por', 'se hace efectivo con', "
            "'se clasifica en') y deben existir relaciones cruzadas entre ramas que evidencien interdependencia e indivisibilidad."
        ),
        "graphic_rule": (
            "Construir el diagrama con TikZ jerárquico. Apilar subconceptos DEBAJO de la cola de cada rama (below= del último nodo), "
            "nunca encimarlos a la derecha ni con posiciones absolutas que desborden. Escalar el diagrama con \\resizebox{!}{0.80\\textheight} "
            "dentro de un entorno landscape para llenar la página sin desbordar; NO usar \\resizebox{\\linewidth}{!} porque desborda en alto."
        ),
        "structure_rule": (
            "Orden recomendado dentro de la sección Mapa conceptual: (2.1) Metodología de construcción (texto justificado con los pasos), "
            "(2.2) Representación gráfica con el diagrama en su propia página landscape, (2.3) Desarrollo de las ramas. La metodología va ANTES "
            "del diagrama; compactar la lista para que quepa en una página y el mapa entre limpio en la siguiente sin hueco visible."
        ),
        "apa_ia_rule": (
            "Rúbrica de mapa conceptual exige citación APA 7 y, si se usó IA, declaración de uso de IA conforme a lineamientos UnADM. "
            "Las referencias APA y la declaración de IA NO deben amontonarse al pie del diagrama: van en la sección de Referencias del final "
            "(la declaración de IA como sección propia antes de \\bibliography)."
        ),
        "closure_rule": (
            "La conclusión puede llevar \\clearpage para iniciar en su propia página cuando el documento lo amerite; integra síntesis, "
            "análisis propio y postura personal."
        ),
    },
    "tabla_didactica": {
        "aliases": ("tabla", "cuadro", "cuadro comparativo", "longtable", "tabular"),
        "required_visible_elements": ("título", "encabezados", "filas", "criterio de lectura"),
        "preservation_rule": "Si la técnica usa tabla o cuadro, conservar estructura tabular visible con título/caption, encabezados claros, filas completas y una lectura breve; usar longtable, landscape, scriptsize, tabcolsep y arraystretch cuando el contenido sea amplio.",
        "visible_style_rule": "El criterio de organización de la tabla y la herramienta didáctica deben quedar comentados si son guía editorial; el texto visible debe entrar directo al tema sin metadiscurso.",
        "structure_rule": "Integrar contexto y problema en la introducción; si la tabla corresponde a cuestionario, Desarrollo debe contener directamente el cuestionario con su título y cualquier marco conceptual debe ir dentro de la misma sección; nivel cognitivo aplicado va comentado salvo consigna expresa.",
        "closure_rule": "El análisis derivado de la tabla y la postura personal se cierran en la conclusión, no en secciones visibles separadas salvo consigna expresa.",
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
        "visible_citations_min": 3,
        "questionnaire_bibliography_entries_min": 5,
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
        "visible_citations": int(signals.get("cited_keys_count", 0)) >= ACTIVITY_1_CONTRACT["acceptable_ranges"]["visible_citations_min"],
        "questionnaire_sources_min": (not signals.get("questionnaire_detected")) or int(signals.get("cited_keys_count", 0)) >= ACTIVITY_1_CONTRACT["acceptable_ranges"]["questionnaire_bibliography_entries_min"],
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
        "visible_citations": "Las fuentes no aparecen como citas visibles suficientes en el cuerpo del TEX.",
        "questionnaire_sources_min": "El cuestionario resuelto no alcanza el mínimo de fuentes citadas para validar respuestas y justificaciones.",
        "traceability": "La trazabilidad entre actividad, citas y extractor es insuficiente.",
        "evaluation_criteria": "No se detectan criterios de evaluación o entrega suficientemente explícitos.",
        "final_reflection": "No se detecta cierre argumentativo o conclusión final.",
        "sections_range": "La estructura de secciones queda fuera del rango contractual.",
        "concepts_min": "La cobertura conceptual extraída está por debajo del mínimo contractual.",
    }
    return messages.get(name, f"Incumplimiento contractual: {name}.")