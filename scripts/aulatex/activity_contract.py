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
            "id": "optimize_concept_map_layout",
            "goal": "Cuando el producto sea un MAPA CONCEPTUAL (TikZ con estilos mc*), aplicar el optimizador de layout (aulatex mapa-layout --write) partiendo del layout relativo agrupado por ramas: convertir a coordenadas absolutas, resolver choques, colocar las palabras de enlace sin empalmes (place_labels), y SEPARAR en vertical/horizontal (--vspread/--hspread, con cap para no salir de página) dando aire a las etiquetas y llenando el alto. Verificar el render real con pdftoppm/view_image y que el mapa + caption 'Figura' queden en la misma página.",
            "actions": ("partir del layout relativo agrupado", "aulatex mapa-layout --write (vspread/hspread/label-clearance)", "verificar render sin empalmes y sin desborde", "ajustar etiquetas root->rama y cruzadas con pos", "recompilar"),
            "outputs": ("mapa_sin_choques", "etiquetas_sin_empalmes", "mapa_y_caption_misma_pagina"),
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
        "three_part_structure": "el cuerpo visible se organiza en TRES actos: (1) Introducción, (2) una única sección de Desarrollo y (3) Conclusiones. No fragmentar el desarrollo en varias secciones de primer nivel: el marco conceptual, el producto solicitado y su análisis son SUBsecciones de la misma sección de desarrollo. El marco conceptual, las semejanzas/diferencias u otros apoyos NO son secciones \\section independientes.",
        "introduction": "la introducción absorbe contexto y problema; evitar una subsección visible separada 'Contexto y problema' salvo consigna expresa",
        "development_section": "el segundo acto (desarrollo) NO debe titularse 'Desarrollo': lleva un título cosmético y descriptivo del TEMA (p. ej. 'Clasificación de los tipos de seguro', no 'Desarrollo'). Dentro de él se organizan como subsecciones: preparación conceptual -> producto solicitado (mapa/tabla/cuadro) -> análisis derivado. El producto solicitado es el NÚCLEO protagónico de este acto.",
        "product_centric_gravity": "el producto solicitado (mapa conceptual, cuadro, tabla, esquema) tiene protagonismo imperativo dentro del desarrollo: el texto GRAVITA a su alrededor, antes preparándolo (marco conceptual que conduce a él) y después interpretándolo (lectura, semejanzas/diferencias, implicaciones). El protagonismo es del TEMA y del producto, no de la etiqueta 'desarrollo' ni de metadiscurso.",
        "conclusion": "la conclusión integra síntesis, análisis propio, postura personal, razón y consecuencia; evitar secciones visibles separadas de 'Análisis propio' o 'Postura personal' salvo consigna expresa",
        "ai_declaration": "la declaración de uso de inteligencia artificial, cuando exista, se materializa como \\footnote ligada a una frase oportuna del documento (por defecto de la conclusión), NUNCA como \\section/\\section* ni como bloque separado; debe indicar herramienta y propósito (organizar ideas, revisar redacción) y afirmar que no sustituyó el análisis propio",
        "compile": "PDF existe, está fresco y no presenta errores críticos ni citas indefinidas",
        "report_presentation_alignment": "cuando existan reporte y presentación de la misma actividad, la presentación debe reflejar el contenido, la profundidad, los conceptos, las fuentes y la conclusión del reporte, con estilo Beamer institucional y una diapositiva final de referencias APA y declaración de IA si el reporte la incluye",
        "concept_map_layout": "cuando el producto sea un mapa conceptual (TikZ mc*), el layout debe estar optimizado partiendo del layout relativo agrupado por ramas: sin choques entre nodos, sin palabras de enlace empalmadas ni 'comidas' sobre los nodos (place_labels + separación vertical/horizontal con --vspread/--hspread), y con el mapa y su caption 'Figura' en la MISMA página sin desbordar (verificado con el render real). Aplicar 'aulatex mapa-layout --write' (integrado en el post-proceso de realizar-actividad).",
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
        "three_part_body": (
            "Estructurar el cuerpo visible en tres actos: Introducción, Desarrollo y Conclusiones. El desarrollo es UNA sola sección "
            "(no varias \\section de primer nivel); marco conceptual, producto solicitado y análisis van como subsecciones dentro de ella."
        ),
        "development_title_cosmetic": (
            "El título del acto de desarrollo debe ser descriptivo del tema, no la palabra 'Desarrollo'. Ejemplos válidos: "
            "'Clasificación de los tipos de seguro', 'Marco y clasificación de los derechos humanos'. El nombre nombra el fenómeno, no la etiqueta didáctica."
        ),
        "product_centric_development": (
            "Dar protagonismo imperativo al producto solicitado (mapa conceptual, cuadro, tabla, esquema) dentro del desarrollo. "
            "El desarrollo gravita a su alrededor: ANTES lo prepara (marco conceptual-teórico que conduce al producto) y DESPUÉS lo interpreta "
            "(lectura del producto, semejanzas y diferencias, implicaciones). El énfasis recae en el tema y en el producto, no en la etiqueta ni en el metadiscurso."
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
        "extractor_output_folder": (
            "CONTRATO DE CARPETA DEL EXTRACTOR: la base conceptual de CADA actividad se almacena en su PROPIA subcarpeta bajo "
            "extractor-aulatex/, con el patrón 'conceptos-<materia-slug>-actividad-N' (materia-slug = nombre de la carpeta de materia sin "
            "sufijo de programa como -lde/-mga). El adaptador (extractor_adapter._resolve_output_dir/_activity_concept_dir) IDENTIFICA el "
            "número de actividad, LOCALIZA una carpeta existente que corresponda a esa actividad (patrón 'conceptos-*-actividad-N' o "
            "'conceptos-*-sN') y, si no existe, la CREA (mkdir). Así una corrida NUNCA sobrescribe la base conceptual de otra semana. "
            "PROHIBIDO escribir los artefactos del extractor en la raíz de extractor-aulatex/ cuando hay número de actividad; solo la corrida "
            "sin actividad (activity=0) usa la raíz. Verificar con --activity N que la salida caiga en la subcarpeta correcta."
        ),
        "extractor_long_paths": (
            "En Windows, si las rutas absolutas de las fuentes (p. ej. libros en referencias-*/libros-*) superan MAX_PATH (260 chars) con "
            "LongPathsEnabled=0, is_file()/exists() fallan SILENCIOSAMENTE y el extractor reporta 'Fuentes cargables: 0'. El extractor ya "
            "maneja esto con el prefijo de ruta extendida \\\\?\\ en document_reader._win_long_path (descubrimiento) y pdf_reader._openable_path "
            "(apertura con PyMuPDF). Si aparece '0 fuentes' pese a haber PDFs, verificar la longitud de la ruta y que estos helpers estén activos."
        ),
        "encoding_safety": (
            "NUNCA editar archivos .tex con PowerShell (Set-Content / -replace): corrompe la codificación UTF-8 (mojibake doble). "
            "Usar siempre herramientas de edición que preserven UTF-8. Si ocurre mojibake, reparar con reemplazos dirigidos "
            "(Ã¡->á, Âº->º, â€\"->—) por Python, no re-decodificando todo el archivo."
        ),
        "always_use_latexmk": (
            "SIEMPRE compilar con latexmk vía scripts/latexmk-build.ps1 (o workspace.compile_tex, que lo invoca). El .latexmkrc de la raíz "
            "ya fija $out_dir='.build/latex' y $aux_dir='.build/latex/aux' + TEXINPUTS/BIBINPUTS/BSTINPUTS, de modo que TODOS los auxiliares "
            "(.aux .bbl .blg .log .out .toc .fls .fdb_latexmk .synctex.gz) quedan AISLADOS en .build/latex y el PDF final se copia junto al .tex. "
            "PROHIBIDO compilar con pdflatex/bibtex manuales sin -output-directory (dejan residuos junto al .tex y ensucian la carpeta de la materia). "
            "latexmk además resuelve solo el ciclo pdflatex->bibtex->pdflatex x2 (max_repeat=5). Si aparece un warning no fatal 'Missing input file .toc' "
            "tras limpiar auxiliares, es cosmético: latexmk regenera el .toc en la 2ª pasada; usar -f (force) para que no aborte el exit code."
        ),
        "build_command": (
            "Comando canónico (respeta el .latexmkrc, NO deja residuos junto al .tex): "
            "powershell -File scripts/latexmk-build.ps1 <src.tex> -CleanMode safe. "
            "Equivale a 'latexmk -f -pdf -interaction=nonstopmode -file-line-error <src>' con el .latexmkrc que aísla auxiliares en "
            ".build/latex/aux y copia el PDF al lado del .tex. NO usar invocaciones manuales de pdflatex/bibtex que escriban junto al .tex."
        ),
        "no_build_residues": (
            "La carpeta de cada materia/actividad SOLO debe contener FUENTES (.tex .bib .md .json) y el PDF final; NUNCA residuos de compilación "
            "(.aux .bbl .blg .log .out .toc .fls .fdb_latexmk .synctex.gz .nav .snm .vrb .xdv .run.xml) ni respaldos .bak del optimizador ya aplicados. "
            "Como latexmk (con el .latexmkrc) aísla todo en .build/latex, la única fuente de residuos son compilaciones manuales antiguas: si aparecen, "
            "BORRARLOS. El post-proceso de realizar-actividad debe barrer estos residuos de la carpeta de la actividad tras la compilación final."
        ),
        "page_control": (
            "Usar \\clearpage para forzar que una sección (p. ej. Conclusión) inicie en su propia página. El entorno landscape siempre "
            "abre página nueva: compactar el contenido previo para evitar huecos."
        ),
        "no_gap_before_visual_deliverable": (
            "PROHIBIDO dejar un hueco grande (media página o más en blanco) inmediatamente antes de un entregable visual en landscape "
            "(tabla, cuadro comparativo, mapa conceptual, esquema). Como el entorno landscape abre página nueva, el texto que lo precede "
            "no debe quedar a media página. Estrategias en orden de preferencia: (1) enriquecer con contenido útil el bloque previo "
            "—p. ej. una guía de lectura de columnas/ramas o la metodología de construcción— hasta llenar la página; (2) iniciar la "
            "sección del entregable en página nueva con \\clearpage para que el hueco quede al final de la sección anterior y no entre "
            "el título y la tabla; (3) en caso extremo, ajustar la redacción del texto colindante para equilibrar el llenado. Verificar "
            "SIEMPRE con pdftoppm que no quede una página semivacía antes del entregable ni una página landscape vacía extra."
        ),
        "landscape_single_page": (
            "Tabla/caption o diagrama/leyenda de un entregable visual deben caber JUNTOS en UNA sola página landscape. Si el caption o la "
            "leyenda se desbordan a una segunda página landscape (dejando la primera casi vacía), compactar: \\arraystretch<=1.2, caption "
            "en \\footnotesize pegado con \\\\[0.3cm], y evitar \\vspace*{\\fill} superior e inferior simultáneos que empujan a 2 páginas. "
            "No anteponer \\clearpage a \\begin{landscape} porque pdflscape ya inserta el salto y se generaría una página landscape vacía."
        ),
        "conclusion_single_page": (
            "La conclusión inicia con \\clearpage y debe ocupar preferentemente una sola página, sin arrastrar contenido a una página extra "
            "casi vacía. La declaración de uso de IA se liga como \\footnote a una frase oportuna de la conclusión (no como bloque separado "
            "ni amontonada al pie de una tabla)."
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
            "Construir el diagrama con TikZ y estilos mc* (mcroot/mcbranch/mcleaf/mcsub); cada liga con node[mclabel]{proposición}. "
            "PUNTO DE PARTIDA recomendado: layout RELATIVO en abanico (raíz arriba-centro; ramas con below left/below right a distancias "
            "crecientes; hojas apiladas con below= bajo su rama; nodos de enriquecimiento en RACIMOS LATERALES con left=/right= anclados a cada "
            "hoja base, NO prolongando la columna). Esto AGRUPA por ramas y evita el aspecto de columnas largas. Después ejecutar el optimizador de "
            "layout (véase layout_optimizer_rule) que convierte a coordenadas absolutas, resuelve choques y separa las etiquetas. Escalar con "
            "\\resizebox{\\linewidth}{!} (por ancho) cuando el mapa optimizado es ancho-bajo; el mapa y su caption Figura deben caber en la misma página."
        ),
        "layout_optimizer_rule": (
            "OBLIGATORIO tras generar/editar el mapa: correr 'aulatex mapa-layout <tex> --write' (scripts/optimize_mapa_layout.py) que "
            "(1) parte del layout relativo agrupado por ramas, (2) convierte a coordenadas absolutas, (3) resuelve choques entre nodos con fuerza "
            "dirigida, (4) COLOCA las palabras de enlace con pos+xshift/yshift anti-empalme (place_labels), (5) SEPARA en vertical (--vspread) y un "
            "poco en horizontal (--hspread, con cap automático para NO salir de página) dando aire a las etiquetas y usando el alto libre, y "
            "(6) reserva holgura de etiqueta (--label-clearance). Parámetros óptimos verificados: --iters 1200 --repulsion 0.35 --step 0.2 "
            "--spring 0.03 --xlim 13.5 --ylim 11 --target-aspect 1.4 --vspread 1.4 --hspread 1.08 --label-clearance 1.35 (son los DEFAULTS). "
            "REGLAS DE ORO: (a) partir del layout relativo agrupado, NUNCA reoptimizar coordenadas ya dispersas (empeora y desborda); (b) verificar el "
            "RENDER real con view_image (el conteo 'overlaps->0' es del modelo, no del render); (c) confirmar que el caption 'Figura 1' quede en la "
            "misma página del mapa y que x_max<ancho_pag (sin desborde); (d) los 2 empalmes residuales típicos (etiquetas root->rama muy juntas y ligas "
            "cruzadas to[bend]) se ajustan a mano con node[mclabel, pos=0.16..0.85]; (e) si el resultado empeora, RESTAURAR el layout relativo y reintentar. "
            "Integrado en el post-proceso de realizar-actividad cuando el producto es mapa conceptual (agent._optimize_mapa_layout, flag --no-mapa-layout)."
        ),
        "structure_rule": (
            "Cuerpo en TRES actos: Introducción, un Desarrollo con título temático (NO 'Desarrollo') y Conclusiones. El mapa conceptual es el "
            "NÚCLEO del acto de desarrollo y todo gravita a su alrededor. Orden dentro del desarrollo: (a) preparación conceptual-teórica que conduce "
            "al mapa (marco/metodología breve), (b) el diagrama en su propia página landscape como pieza protagónica, (c) lectura y desarrollo de las ramas "
            "tras el diagrama. La preparación va ANTES del mapa; el análisis va DESPUÉS. El énfasis es del tema y del mapa, no de la etiqueta 'desarrollo'."
        ),
        "three_act_gravity_rule": (
            "El desarrollo NO se fragmenta en varias secciones \\section: marco conceptual, mapa y análisis son subsecciones de una sola sección de desarrollo "
            "cuyo título nombra el tema. El producto (mapa conceptual) manda: el texto lo prepara antes y lo interpreta después, dándole protagonismo imperativo."
        ),
        "no_gap_rule": (
            "PROHIBIDO dejar media página o más en blanco justo antes del diagrama landscape. Si la metodología o el texto previo no llena "
            "la página, ampliarlo con la explicación de la lectura del mapa o iniciar la sección con \\clearpage; en caso extremo, ajustar "
            "la redacción colindante. Verificar con pdftoppm que no quede una página semivacía antes del mapa ni una página landscape vacía extra."
        ),
        "apa_ia_rule": (
            "Rúbrica de mapa conceptual exige citación APA 7 y, si se usó IA, declaración de uso de IA conforme a lineamientos UnADM. "
            "Las referencias APA y la declaración de IA NO deben amontonarse al pie del diagrama: van en la sección de Referencias del final "
            "(la declaración de IA como sección propia antes de \\bibliography, o como \\footnote ligada a una frase oportuna de la conclusión)."
        ),
        "closure_rule": (
            "La conclusión inicia con \\clearpage en su propia página y ocupa preferentemente una sola página; integra síntesis, análisis propio "
            "y postura personal. La declaración de uso de IA puede ligarse como \\footnote a una frase oportuna de la conclusión."
        ),
    },
    "tabla_didactica": {
        "aliases": ("tabla", "cuadro", "cuadro comparativo", "longtable", "tabular"),
        "required_visible_elements": ("título", "encabezados", "filas", "criterio de lectura"),
        "preservation_rule": "Si la técnica usa tabla o cuadro, conservar estructura tabular visible con título/caption, encabezados claros, filas completas y una lectura breve; usar longtable, landscape, scriptsize, tabcolsep y arraystretch cuando el contenido sea amplio.",
        "visible_style_rule": "El criterio de organización de la tabla y la herramienta didáctica deben quedar comentados si son guía editorial; el texto visible debe entrar directo al tema sin metadiscurso.",
        "structure_rule": (
            "Cuerpo en TRES actos: Introducción, un Desarrollo con título temático (NO 'Desarrollo') y Conclusiones. La tabla/cuadro es el NÚCLEO del "
            "acto de desarrollo. Orden dentro del desarrollo: (a) marco conceptual-teórico breve que prepara y da sentido a la tabla, (b) la tabla en su "
            "página landscape como pieza protagónica, (c) semejanzas y diferencias u otro análisis derivado DESPUÉS de la tabla. Contexto y problema van en "
            "la introducción; nivel cognitivo aplicado va comentado salvo consigna expresa."
        ),
        "three_act_gravity_rule": (
            "El desarrollo NO se fragmenta en varias secciones \\section: marco conceptual, tabla y análisis (semejanzas/diferencias) son subsecciones de una "
            "sola sección de desarrollo cuyo título nombra el tema. El producto (cuadro/tabla) manda: el texto lo prepara antes y lo interpreta después."
        ),
        "layout_rule": (
            "El cuadro/tabla va en orientación horizontal (landscape) en su PROPIA página, con la tabla y su caption juntos en una sola "
            "página landscape. La sección que introduce la tabla NO debe quedar a media página dejando un hueco antes del salto a landscape: "
            "llenar ese bloque con una guía de lectura de las columnas (qué informa cada una y cómo contrastarlas) o iniciar la sección con "
            "\\clearpage; en caso extremo, ajustar la redacción del texto colindante. No anteponer \\clearpage al \\begin{landscape}. "
            "Compactar con \\arraystretch<=1.2 y caption en \\footnotesize para que quepan tabla y caption en una sola página."
        ),
        "no_gap_rule": (
            "PROHIBIDO dejar media página o más en blanco justo antes del cuadro. Verificar visualmente con pdftoppm el flujo de páginas: "
            "la página previa al landscape debe estar razonablemente llena y no debe existir una página landscape vacía extra."
        ),
        "closure_rule": "El análisis derivado de la tabla y la postura personal se cierran en la conclusión, no en secciones visibles separadas salvo consigna expresa. La conclusión inicia con \\clearpage y ocupa preferentemente una sola página; la declaración de uso de IA se liga como \\footnote a una frase oportuna de la conclusión.",
    },
    "foro_diagnostico": {
        "aliases": ("foro", "foro diagnóstico", "foro diagnostico", "participación en foro", "participacion en foro"),
        "required_visible_elements": ("preguntas guía", "respuesta", "participación textual publicada", "cierre"),
        "preservation_rule": "Si el producto es foro diagnóstico, conservar preguntas guía y respuestas compactas sin convertirlo en ensayo extenso.",
        "visible_style_rule": (
            "No explicar en el texto visible que 'esta actividad' usa la técnica foro ni describir la ficha de las 100 técnicas didácticas; "
            "esa trazabilidad va como comentario TEX. El texto visible habla del tema y del diálogo, no del proceso editorial."
        ),
        "structure_rule": (
            "Cuerpo en TRES actos: (1) Introducción, (2) una única sección de Desarrollo con título temático (NO 'Desarrollo' ni 'Participación en el foro') "
            "y (3) Conclusiones. El PRODUCTO solicitado del foro —la participación textual publicada— es el NÚCLEO del acto de desarrollo y va como SUBsección "
            "dentro de esa única sección, no como \\section de primer nivel. Orden dentro del desarrollo: (a) breve marco/encuadre que conduce a las preguntas guía, "
            "(b) las respuestas a las preguntas guía, (c) la participación textual publicada en el foro como subsección protagónica (bloque de código verbatim/listings) "
            "y su lectura breve."
        ),
        "three_act_gravity_rule": (
            "El desarrollo NO se fragmenta en varias secciones \\section: marco, preguntas guía, participación publicada y su lectura son subsecciones de una sola "
            "sección de desarrollo cuyo título nombra el tema del foro. El producto (la participación publicada) manda: el texto lo prepara antes y lo interpreta después."
        ),
        "forum_participation_block_rule": (
            "La participación publicada en el foro debe materializarse como un BLOQUE de código textual (entorno sourcecode de la plantilla, o listings con estilo propio "
            "cuando el documento no cargue la plantilla) que reproduzca literalmente lo que se publica: encuadre/apertura, respuesta a la pregunta detonante o preguntas guía, "
            "y un cierre que invite al diálogo entre pares con al menos una pregunta al grupo. El bloque debe seguir la estructura de la técnica foro (apertura, participación, "
            "coordinación, cierre). REQUISITOS DE FORMATO: cada respuesta/párrafo es UNA sola línea lógica en el fuente (una entrada por número); el bloque hace ajuste de línea "
            "(breaklines) para el texto largo pero NO numera las líneas de continuación del ajuste (si se usa numeración, numbers=left con numberstyle que solo marque la línea de origen, "
            "no las envueltas). El contenido del bloque debe ser SELECCIONABLE Y COPIABLE en el PDF (evitar literate/mapeos de caracteres que rompan el copiado; preferir fuente con "
            "soporte de copia como \\ttfamily estándar o inputenc utf8 con extendedchars)."
        ),
        "apa_citation_rule": (
            "REGLA HOMOGÉNEA PARA TODO FORO: la participación publicada DEBE integrar al menos UNA cita TEXTUAL (entrecomillada) de una fuente formal, con su "
            "referencia APA 7 dentro del propio bloque del foro. La cita textual va incrustada de forma orgánica en la respuesta que corresponda —no como 'ejemplo de cita' ni "
            "como metadiscurso— con el formato (Apellido, Año, p.~N) inmediatamente después de las comillas de cierre. Al final del bloque del foro, tras el cierre y la firma, se "
            "reproduce un apartado titulado 'Referencia' (o 'Referencias' si son varias) con sangría francesa (\\hangindent), tal como se publicaría en el foro. "
            "COBERTURA COMPLETA: el apartado de referencias del forobox debe listar TODAS las fuentes citadas dentro de ESE forobox (cada \\citep{...} y cada cita textual), no solo la "
            "que aparece en formato textual; una sola cita textual es suficiente para el requisito de 'cita textual', pero toda fuente mencionada debe tener su entrada APA 7 en el "
            "apartado de referencias, ordenada alfabéticamente. Cada forobox (participación y, si existe, retroalimentación) lleva su PROPIO apartado de referencias con las fuentes que "
            "cita ese bloque. Esta cita+referencias forma parte de la reproducción literal de lo publicado y es independiente de la bibliografía general del documento; puede o no tener "
            "entrada .bib. PROHIBIDO usar un ítem del tipo 'Ejemplo de cita en formato APA' como reactivo de la lista: la cita se usa, no se enuncia."
        ),
        "feedback_block_rule": (
            "Cuando el foro pida además retroalimentación a la participación de otra persona, esa retroalimentación publicada también se materializa en su PROPIO forobox "
            "(caja del foro), separado del forobox de la participación propia, para reflejar que es contenido publicado en el hilo. Antes del forobox de retroalimentación, un breve "
            "párrafo en prosa presenta —sin nombre, por privacidad académica— la idea a la que se responde. Dentro del forobox de retroalimentación se cierra con una pregunta dirigida "
            "a quien participó."
        ),
        "closure_rule": (
            "La conclusión integra síntesis, análisis propio y postura personal (posición, razón y consecuencia); no crear secciones visibles separadas de análisis o postura. "
            "La conclusión inicia SIEMPRE con \\clearpage inmediatamente antes de la \\section, de modo que arranque en una PÁGINA NUEVA por sí sola y ocupe preferentemente una sola página, sin quedar pegada al bloque de participación del foro. "
            "La declaración de uso de IA se liga como \\footnote a una frase oportuna de la conclusión, nunca como \\section."
        ),
    },
    "resena": {
        "aliases": ("reseña", "resena", "reseña académica", "resena academica", "reseña crítica", "resena critica", "reseña literaria", "resena literaria"),
        "required_visible_elements": ("ficha bibliográfica", "título", "introducción", "cuerpo", "conclusiones"),
        "preservation_rule": (
            "Si el producto es reseña, conservar los 5 ELEMENTOS OFICIALES (UnADM 100 técnicas) DENTRO de un recuadro (resenabox): "
            "(1) ficha bibliográfica de la obra (macro \\fichabibliografica), (2) título propio distinto al de la obra, "
            "(3) introducción que describe la temática y presenta la obra/autor, (4) cuerpo con el contenido de la obra + comentarios/críticas, "
            "(5) conclusiones con una recomendación/valoración. No convertir la reseña en ensayo suelto sin recuadro."
        ),
        "visible_style_rule": (
            "No explicar en el texto visible que 'esta actividad' usa la técnica reseña; esa trazabilidad va como comentario TEX. "
            "El texto visible habla de la OBRA y del TEMA, no del proceso editorial. Prohibidos rótulos de proceso "
            "(Exposición/Valoración crítica narrando el método); permitidos rótulos TEMÁTICOS que mapeen la rúbrica."
        ),
        "reporte_vs_producto_rule": (
            "El REPORTE (contenedor) tiene su propia Introducción y Conclusión (reflexión del TEMA en 1a persona). El PRODUCTO (la reseña) "
            "va ANIDADO dentro de un resenabox como subsección del desarrollo, homólogo al forobox del foro. La Introducción/Conclusión del "
            "reporte NO se confunden con la introducción/conclusiones internas de la reseña."
        ),
        "marco_gravita_afuera_rule": (
            "El MARCO CONCEPTUAL gravita AFUERA del resenabox: se materializa como subsecciones temáticas del reporte (una por eje conceptual "
            "del extractor) con sus citas de sustento (\\citep de referencias externas). Esto mantiene la reseña CEÑIDA dentro del recuadro, "
            "sin diluir su estructura con el aparato teórico."
        ),
        "structure_rule": (
            "Cuerpo en TRES actos: (1) Introducción del reporte (contextualiza el TEMA), (2) una sección de Desarrollo con título temático "
            "(p. ej. 'Marco jurídico y fundamento...') que contiene primero las subsecciones del marco conceptual (ejes del extractor con sus citas) "
            "y luego la subsección 'Reseña de <objeto>' con el resenabox protagónico, (3) Conclusión del reporte. La reseña (resenabox) es el NÚCLEO."
        ),
        "cinco_elementos_oficiales_rule": (
            "DENTRO del resenabox deben aparecer los 5 elementos: ficha bibliográfica (\\fichabibliografica), un título propio distinto al de la obra, "
            "una introducción que inicia con el sujeto real (p. ej. 'La Constitución...') describiendo el tema y presentando la obra, un cuerpo con "
            "rótulos TEMÁTICOS en negrita que mapean 1:1 los rubros de la rúbrica (con cita textual \\enquote de la obra y \\citep de sustento), y "
            "conclusiones con recomendación/valoración explícita ('recomiendo la lectura...')."
        ),
        "citas_y_fuentes_rule": (
            "Según la guía LEO, la reseña combina información externa + análisis propios: las referencias externas (\\citep) SON correctas y "
            "recomendadas para sustentar; la obra reseñada aporta citas TEXTUALES (\\enquote con página). La reseña es autocontenida en su ESTRUCTURA "
            "y JUICIO, pero se compone a partir de fuentes externas."
        ),
        "extension_dos_paginas_rule": (
            "La reseña (dentro del resenabox) debe ocupar ~2 páginas contando la ficha (~7 filas). Si se pasa, RECORTAR párrafos ~30% "
            "(NO reducir la ficha). Párrafos concisos por rótulo, redacción fluida y clara, sin subordinadas anidadas largas."
        ),
        "closure_rule": (
            "Las conclusiones internas de la reseña cierran con una RECOMENDACIÓN/valoración. La Conclusión del reporte (fuera del recuadro) integra "
            "síntesis, análisis propio y postura personal sobre el TEMA; inicia con \\clearpage y ocupa preferentemente una sola página; la declaración "
            "de uso de IA se liga como \\footnote a una frase oportuna, nunca como \\section."
        ),
    },
    "socioaprendizaje": {
        "aliases": ("socioaprendizaje", "aprendizaje social", "wiki", "wiki colaborativa", "wiki de la plataforma", "trabajo colaborativo en wiki", "contribución a la wiki", "contribucion a la wiki", "edición de wiki", "edicion de wiki", "participación en wiki", "participacion en wiki"),
        "required_visible_elements": ("contribución publicada", "base conceptual", "cita textual", "referencias", "reflexión colaborativa"),
        "equivalence_rule": (
            "SOCIOAPRENDIZAJE (#53 planeación / #78 catálogo) y WIKI son lo MISMO en este sistema: el Socioaprendizaje es la TÉCNICA didáctica (método de "
            "aprendizaje social/colaborativo) y la wiki es la HERRAMIENTA/soporte de plataforma con que se materializa (construcción coral). El producto "
            "wiki (wikibox) ES el producto del socioaprendizaje. Se detectan y contractualizan bajo el id canónico 'socioaprendizaje'."
        ),
        "preservation_rule": (
            "El PRODUCTO del socioaprendizaje se materializa como una CONTRIBUCIÓN publicada en la wiki de la plataforma (herramienta de trabajo colaborativo). "
            "Otras técnicas colaborativas (glosario colaborativo, trabajo cooperativo, proyectos colaborativos) también pueden materializarse en wiki. El PRODUCTO es la CONTRIBUCIÓN "
            "PUBLICADA en la wiki y se reproduce ANIDADA en un recuadro (wikibox), homólogo al forobox del foro y al resenabox de la reseña. Conservar "
            "el contenido tal como se publica (aportes + complementos a otros), no convertirlo en ensayo suelto."
        ),
        "visible_style_rule": (
            "No explicar en el texto visible que 'esta actividad' usa una wiki; esa trazabilidad va como comentario TEX. El texto visible REPRODUCE la "
            "contribución (aportes/definiciones) y habla del TEMA, no del proceso ('en esta wiki aporté...'). Prohibido metadiscurso de proceso."
        ),
        "reporte_vs_producto_rule": (
            "El REPORTE (contenedor: portada + resumen + índice + 3 secciones + referencias) tiene su propia Introducción y Conclusión. El PRODUCTO "
            "(contribución a la wiki) va ANIDADO en el Desarrollo dentro de una wikibox. La Conclusión del reporte reflexiona sobre el APORTE colaborativo "
            "y lo aprendido; no repite el contenido de la wiki. La declaración de IA como \\footnote va en la Conclusión del reporte."
        ),
        "boton_copiar_txt_rule": (
            "La wikibox DEBE llevar un BOTÓN 'Copiar contribución' en su esquina superior derecha (\\wikiCopyButton via \\usepackage{attachfile}, "
            "homólogo al \\foroCopyButton del foro), justo tras \\begin{wikibox}: \\hfill\\wikiCopyButton{wiki-participacion-Actividad-N.txt}. El .txt "
            "reproduce la contribución en TEXTO PLANO copiable (sin LaTeX) y se crea JUNTO al .tex/.pdf en UTF-8, para pegar directo en la plataforma. "
            "Requiere \\attachfilesetup{color={0.373 0.561 0.227},print=false} (color RGB triple numérico; un nombre HTML rompe attachfile)."
        ),
        "tres_secciones_rule": (
            "El reporte tiene EXACTAMENTE 3 secciones de contenido: (1) Introducción (contextualiza el TEMA y el trabajo colaborativo), (2) Desarrollo con "
            "título temático (NO 'Desarrollo') que contiene la base conceptual en subsecciones + la wikibox, (3) Conclusiones. Más portada, resumen, índice "
            "y referencias como partes de la plantilla consolidada."
        ),
        "base_conceptual_gravita_afuera_rule": (
            "La BASE CONCEPTUAL (subsecciones temáticas con conceptos del extractor + citas de sustento \\citep) va AFUERA de la wikibox, como \\subsection "
            "del Desarrollo, preparando y sosteniendo de forma orgánica y fluida el producto. Bien articulada (títulos y subsecciones adecuadas), respalda "
            "con solidez la contribución y gravita ALREDEDOR del producto sin encerrarlo."
        ),
        "aportacion_tres_elementos_rule": (
            "Cada APORTACIÓN a la wiki desarrolla 3 ELEMENTOS (planeación real S3): (1) una confusión/práctica/idea que CONTRADICE el tema; "
            "(2) una explicación breve de por qué es un problema; (3) una alternativa para prevenirla/transformarla, con ejemplo concreto "
            "(educación a distancia, trabajo académico, campo jurídico). Se incluye al menos una aportación propia + 1-2 complementos a aportes previos."
        ),
        "colaborativo_rule": (
            "Al ser TRABAJO COLABORATIVO EN PLATAFORMA (Socioaprendizaje), la wikibox evidencia construcción CORAL respetando las reglas reales: NO repetir "
            "ideas; NO eliminar ni modificar aportes de otros (solo AMPLIAR con otro ejemplo/consecuencia/propuesta, referidos SIN nombre: 'ampliando un aporte "
            "previo...'); cerrar con una invitación/pregunta que abra a seguir colaborando. Escritura colectiva e hipertextual, no texto individual."
        ),
        "citas_y_referencias_rule": (
            "MATIZ WIKI (distinto al foro): la wiki formativa NO exige citas ni referencias APA en cada aportación; solo mencionar la fuente (Autor, año) SI se usa "
            "una cita textual (\\enquote). NO se obliga a un apartado 'Referencias' dentro de la wikibox. En cambio, la BASE CONCEPTUAL del desarrollo (afuera de "
            "la wikibox) y la bibliografía general del reporte SÍ se rigen por los Lineamientos UnADM (APA 7 formal con \\citep + \\bibliography)."
        ),
        "closure_rule": (
            "La Conclusión del reporte integra síntesis, análisis propio y postura personal sobre el APORTE colaborativo; inicia con \\clearpage y ocupa "
            "preferentemente una sola página; la declaración de uso de IA se liga como \\footnote a una frase oportuna, nunca como \\section."
        ),
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
        "ai_declaration_footnote": True,
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
        # Fuente de consigna/propósito: planeación oficial O, en su defecto, propósito
        # derivable del propio marco conceptual del documento (fallback UCNL sin planeación).
        "instruction_source": bool(
            signals.get("purpose_present")
            or signals.get("extractor_planeacion_present")
            or signals.get("document_purpose_present")
        ),
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
        # Trazabilidad: extractor listo con citas suficientes O, sin planeación oficial,
        # trazabilidad interna sólida (citas visibles ligadas a un marco conceptual).
        "traceability": (
            bool(observed.get("extractor_ready")) and int(signals.get("cited_keys_count", 0)) >= 3
        )
        or (
            bool(signals.get("document_purpose_present"))
            and int(signals.get("cited_keys_count", 0)) >= 3
            and int(signals.get("document_concepts_count", 0)) >= ACTIVITY_1_CONTRACT["acceptable_ranges"]["concepts_min"]
        ),
        "evaluation_criteria": bool(signals.get("evaluation_criteria_present") or signals.get("extractor_criteria_count", 0) > 0),
        "final_reflection": bool(signals.get("conclusion_present")),
        # La declaración de uso de IA, cuando exista, debe ir como \footnote ligada a
        # una frase oportuna (por defecto de la conclusión), NO como sección/bloque
        # separado. Si no hay declaración de IA, el check no penaliza.
        "ai_declaration_footnote": (
            (not bool(signals.get("ai_declaration_present")))
            or (
                bool(signals.get("ai_declaration_as_footnote"))
                and not bool(signals.get("ai_declaration_as_section"))
            )
        ),
    }
    range_checks = {
        "sections_range": ACTIVITY_1_CONTRACT["acceptable_ranges"]["sections_min"]
        <= int(signals.get("sections_count", 0))
        <= ACTIVITY_1_CONTRACT["acceptable_ranges"]["sections_max"],
        # Cobertura conceptual: conceptos de la planeación oficial O, en su defecto,
        # conceptos identificables en el marco conceptual del propio documento.
        "concepts_min": max(
            int(signals.get("extractor_concepts_count", 0)),
            int(signals.get("document_concepts_count", 0)),
        )
        >= ACTIVITY_1_CONTRACT["acceptable_ranges"]["concepts_min"],
        # El cuerpo visible no debe contener metadiscurso de ejecución ni residuos de
        # flujos antiguos (p. ej. 'Refuerzo editorial Ciclo A', 'La Actividad N',
        # 'Esta actividad', 'el producto solicitado'). Si el observer no provee la
        # señal (None), el check no penaliza.
        "no_metadiscourse": len(signals.get("metadiscourse_hits") or []) == 0,
        # ENCABEZADOS: el \documenttitle debe ser temático, no 'Actividad #'.
        "thematic_title": not bool(signals.get("title_generic_activity")),
        # ESTRUCTURA: la sección de desarrollo NO debe titularse literalmente 'Desarrollo'.
        "development_thematic_heading": not bool(signals.get("development_section_literal")),
        # POSTURA: análisis propio / postura personal presente (idealmente en conclusión).
        "personal_stance": bool(signals.get("personal_stance_present")),
        # POSTURA INTEGRADA: el análisis propio y la postura NO deben figurar como
        # \section/\subsection separadas; deben fundirse en la prosa de la conclusión.
        "stance_integrated_in_conclusion": not bool(signals.get("stance_as_separate_section")),
        # CUESTIONARIO: las opciones no deben quedar como lista visible suelta
        # ('Opciones: a) ...'); deben ir en la tabla o comentadas.
        "questionnaire_options_hidden": not bool(signals.get("questionnaire_options_visible")),
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
        "ai_declaration_footnote": "La declaración de uso de IA debe ir como \\footnote ligada a una frase oportuna (por ejemplo de la conclusión), no como sección o bloque separado.",
        "sections_range": "La estructura de secciones queda fuera del rango contractual.",
        "concepts_min": "La cobertura conceptual extraída está por debajo del mínimo contractual.",
        "no_metadiscourse": "El cuerpo visible contiene metadiscurso de ejecución o residuos de flujos antiguos (p. ej. 'Refuerzo editorial Ciclo A', 'La Actividad N', 'Esta actividad'); deben eliminarse o pasar a comentario TEX.",
        "thematic_title": "El \\documenttitle es genérico ('Actividad #'); debe ser un título TEMÁTICO del producto (p. ej. 'Cuestionario resuelto de conceptos introductorios de microeconomía').",
        "development_thematic_heading": "La sección de desarrollo se titula literalmente 'Desarrollo'; debe llevar un título temático del contenido (p. ej. 'Conceptos fundamentales de la microeconomía').",
        "personal_stance": "Falta análisis propio o postura personal (primera persona académica: 'Considero...', 'Desde mi análisis...', 'A mi juicio...'), preferentemente integrada en la conclusión.",
        "stance_integrated_in_conclusion": "El análisis propio o la postura personal aparecen como sección/subsección separada (p. ej. '\\section{Postura personal}', '\\subsection{Análisis propio}'); deben integrarse ORGÁNICAMENTE en la prosa de la conclusión, no como apartados propios.",
        "questionnaire_options_hidden": "Las opciones del cuestionario aparecen como lista visible suelta ('Opciones: a) ...'); deben integrarse en la tabla o ir comentadas.",
    }
    return messages.get(name, f"Incumplimiento contractual: {name}.")