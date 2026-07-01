{
  "summary": [
    "Materia destino con plantilla LaTeX, programa analítico y bibliografía local activos.",
    "Contexto local verificado: Garantías constitucionales, Licenciatura en Derecho, UnADM.",
    "Ubicación curricular verificada: semestre 2, bloque 1, obligatoria, 8 créditos.",
    "Se sincronizan solo abstracciones editoriales estables entre materias no equivalentes.",
    "Se conserva alerta institucional sobre salidas heredadas no JSON parseables.",
    "Las reglas heredadas operan como control editorial, no como contenido disciplinar.",
    "Se refuerza compresión lossless por unión y deduplicación.",
    "Se preserva separación entre estructura reusable y contenido temático local."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en portada, encabezados y referencias institucionales.",
    "Usar datos locales: Garantías constitucionales, LDE-S2B1, semestre 2, bloque 1.",
    "Registrar tipo Obligatoria y 8 créditos cuando aparezcan datos curriculares.",
    "Conservar coherencia con Licenciatura en Derecho en todo producto.",
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas desde Codex y GPT-Pro como provisionales.",
    "No trasladar contenido disciplinar de Filosofía del Derecho sin validación local.",
    "Citar la malla curricular institucional solo para ubicación curricular verificada."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por la planeación o consigna.",
    "Mantener separación entre reporte, presentación, programa analítico y bibliografía.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Preservar el programa analítico como guía editorial de la asignatura.",
    "Mantener la carpeta referencias-garantias-constitucionales como depósito local.",
    "Evitar cambios de nombres de archivo base salvo requerimiento explícito.",
    "Corregir nombres truncados en README antes de usarlo como índice operativo.",
    "Corregir placeholders generados antes de referenciar archivos."
  ],
  "activity_rules": [
    "Incluir problema jurídico o social claro desde la introducción.",
    "Distinguir conceptos, normas, doctrina, datos y postura personal.",
    "Sustentar afirmaciones relevantes con fuente verificable o norma identificable.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Confirmar que el producto corresponda a la consigna local.",
    "No asumir fuentes de otra semana o materia como aplicables.",
    "Cerrar con conclusión jurídica aplicable a la práctica profesional."
  ],
  "quality_gates": [
    "Bloquear propagación automática si la entrada no es JSON parseable.",
    "Validar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Verificar congruencia entre metadatos de portada y datos curriculares locales.",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Confirmar que toda cita usada tenga entrada bibliográfica local.",
    "Compilar LaTeX antes de entregar productos finales.",
    "Revisar truncamientos visibles en README y plantilla LaTeX.",
    "Verificar que no queden placeholders literales en rutas, nombres o bibliografía.",
    "Confirmar que las fuentes institucionales correspondan a archivos o enlaces disponibles.",
    "Aplicar unión-dedupe sin eliminar reglas útiles previas."
  ],
  "latex_rules": [
    "Conservar clase article en español, letterpaper y oneside según plantilla.",
    "Completar actividad, figura docente y fecha antes de entregar.",
    "Mantener tabla de autor con matrícula, semestre, bloque, tipo y créditos correctos.",
    "Preservar coursecode como LDE-S2B1 salvo indicación institucional distinta.",
    "Evitar comandos rotos o texto truncado en portada y metadatos.",
    "Verificar cierre completo de \\authortable y \\universityname.",
    "Reparar truncamiento detectado cerca de la macro de portada antes de compilar.",
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "No introducir paquetes nuevos sin necesidad editorial o técnica verificable.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Mantener nombres sin acentos solo si la plantilla lo requiere técnicamente."
  ],
  "bibliography_rules": [
    "Registrar fuentes específicas de actividad en garantias-constitucionales.bib.",
    "Mantener como base las entradas institucionales UnADM ya presentes.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Priorizar fuentes institucionales UnADM y fuentes jurídicas verificables.",
    "No inventar referencias.",
    "Usar solo fuentes consultadas y verificables.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Agregar normas jurídicas con identificador, emisor y fecha cuando sean usadas.",
    "Usar claves BibTeX estables y descriptivas.",
    "Incluir nota de consulta o procedencia cuando la fuente sea institucional o local.",
    "Corregir menciones bibliográficas que usen placeholders generados.",
    "Distinguir bibliografía base de bibliografía específica de actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar a nodos laterales solo reglas editoriales generales ya validadas.",
    "No propagar datos curriculares específicos fuera de Garantías constitucionales.",
    "No trasladar contenidos temáticos entre materias sin validación local.",
    "Mantener alerta de JSON no parseable como control institucional.",
    "Priorizar identidad, estructura, calidad, LaTeX, bibliografía y grafo conceptual.",
    "Aplicar normalización manual si se detecta salida no estructurada.",
    "Ciclo 1 requiere normalización manual si se reutiliza herencia incompleta.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Usar unión-dedupe como estrategia de compresión conservadora."
  ],
  "open_questions": [
    "Falta consigna textual de actividades locales de Garantías constitucionales.",
    "Falta confirmar producto exacto de cada actividad local.",
    "Falta confirmar rúbrica de evaluación específica.",
    "Falta definir nombre de figura docente en plantilla destino.",
    "Falta verificar y corregir truncamiento en reporte-garantias-constitucionales.tex.",
    "Falta corregir nombres truncados de archivos en README.md.",
    "Falta reemplazar placeholder bibliográfico en README.md y programa analítico.",
    "Falta confirmar si la fecha debe ser automática con \\today o fija por entrega.",
    "Falta validar estilo de citación requerido: APA, jurídico mexicano u otro.",
    "Supuesto: la herencia institucional no parseable se conserva solo como control de riesgo.",
    "Supuesto: las reglas de Filosofía del Derecho se transfieren solo como abstracciones editoriales."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Institucional sin rigidez excesiva.",
        "Práctico para productos evaluables."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Trazabilidad entre consigna, fuentes y producto.",
        "Carpeta de asignatura como entrada canónica.",
        "Control preventivo ante herencias no estructuradas."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Garantías constitucionales.",
        "Código local: LDE-S2B1.",
        "Semestre 2, bloque 1.",
        "Tipo obligatoria, 8 créditos."
      ]
    },
    "essence": [
      "Identidad institucional UnADM.",
      "Problema jurídico o social.",
      "Conceptos clave verificables.",
      "Marco normativo y doctrinal.",
      "Evidencia jurídica trazable.",
      "Análisis propio del estudiante.",
      "Conclusión jurídica transferible.",
      "Bibliografía local verificable.",
      "Normalización estructurada.",
      "Compresión union-dedupe sin regresión."
    ],
    "reason_for_being": [
      "Orientar productos académicos de Garantías constitucionales con claridad y fundamento.",
      "Transformar la planeación semanal en reporte, presentación o producto visual según consigna.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Asegurar trazabilidad entre afirmaciones, normas, doctrina y bibliografía.",
      "Evitar transferencias disciplinares impropias desde materias no equivalentes.",
      "Servir como cerebro editorial persistente de la materia."
    ],
    "style_markers": [
      "Explicitar objetivo al inicio.",
      "Usar secciones funcionales y consistentes.",
      "Marcar supuestos de forma visible.",
      "Evitar afirmaciones sin respaldo.",
      "Diferenciar norma, doctrina, dato y opinión.",
      "Mantener tono institucional UnADM.",
      "Cuidar precisión jurídica en conceptos constitucionales.",
      "Usar cierre aplicable a la práctica profesional.",
      "Preferir frases directas y verificables.",
      "Evitar redacción importada de otra materia."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> marco normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> interpretación -> implicación jurídica.",
      "Consigna -> producto alineado -> verificación de cierre.",
      "Norma identificable -> alcance -> aplicación al caso.",
      "Doctrina o fuente -> criterio propio -> límite argumentativo.",
      "Supuesto marcado -> verificación pendiente -> uso conservador.",
      "Bibliografía local -> cita en texto -> consistencia BibTeX.",
      "Control editorial -> validación JSON -> propagación segura."
    ],
    "knowledge_graph": {
      "concepts": [
        "Garantías constitucionales",
        "Licenciatura en Derecho",
        "Identidad institucional UnADM",
        "Ubicación curricular",
        "Problema jurídico o social",
        "Conceptos clave",
        "Marco normativo",
        "Doctrina jurídica",
        "Análisis propio",
        "Postura académica",
        "Conclusión jurídica transferible",
        "Integridad académica",
        "Bibliografía verificable",
        "Archivo .bib local",
        "Plantilla LaTeX",
        "Programa analítico",
        "Normalización estructurada",
        "JSON parseable",
        "Compresión union-dedupe",
        "Propagación recursiva controlada",
        "Herencia provisional"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La identidad institucional exige citas verificables y trazabilidad."
        },
        {
          "source": "Ubicación curricular",
          "target": "Garantías constitucionales",
          "kind": "supports",
          "justification": "El README local verifica semestre, bloque, tipo y créditos."
        },
        {
          "source": "Programa analítico",
          "target": "Problema jurídico o social",
          "kind": "develops",
          "justification": "El programa fija el problema como eje inicial de trabajo."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "El problema activa la postura argumentada del estudiante."
        },
        {
          "source": "Conceptos clave",
          "target": "Marco normativo",
          "kind": "depends_on",
          "justification": "Los conceptos requieren delimitación normativa o doctrinal."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "El cierre debe derivar de fuentes jurídicas identificables."
        },
        {
          "source": "Bibliografía verificable",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Las fuentes consultables reducen afirmaciones no respaldadas."
        },
        {
          "source": "Archivo .bib local",
          "target": "Bibliografía verificable",
          "kind": "supports",
          "justification": "El .bib local centraliza entradas usadas por la materia."
        },
        {
          "source": "Plantilla LaTeX",
          "target": "Identidad institucional UnADM",
          "kind": "supports",
          "justification": "La portada y metadatos preservan identidad institucional."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva controlada",
          "kind": "depends_on",
          "justification": "Sin estructura válida no hay transferencia segura."
        },
        {
          "source": "JSON parseable",
          "target": "Normalización estructurada",
          "kind": "supports",
          "justification": "El formato parseable permite validar y deduplicar memoria."
        },
        {
          "source": "Compresión union-dedupe",
          "target": "Herencia provisional",
          "kind": "supports",
          "justification": "La deduplicación conserva reglas útiles sin mezclar contenidos no validados."
        },
        {
          "source": "Herencia provisional",
          "target": "Garantías constitucionales",
          "kind": "contrasts",
          "justification": "La herencia no validada no sustituye el contexto local verificado."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 2, bloque 1, obligatoria, 8 créditos.",
        "README local: fuente curricular UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: pauta de identidad UnADM, integridad académica y citas verificables.",
        "Programa analítico local: productos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: ejes de problema, conceptos, fuentes, análisis propio y cierre.",
        "garantias-constitucionales.bib: entrada unadmSitioWeb.",
        "garantias-constitucionales.bib: entrada unadmMallaDerecho2024.",
        "Plantilla LaTeX local: coursecode LDE-S2B1.",
        "Plantilla LaTeX local: figura docente por definir.",
        "Plantilla LaTeX local: truncamiento visible en macro de portada.",
        "Regla institucional heredada: bloquear si no hay JSON parseable.",
        "Regla heredada validada como abstracción: revisar respuesta no estructurada antes de aplicar aguas abajo."
      ]
    },
    "reinforcement_log": [
      "Ciclo 1 sincroniza memoria transversal de actividad a materia.",
      "Se conservan reglas locales verificadas de Garantías constitucionales.",
      "Se deduplican reglas repetidas sin eliminar controles útiles.",
      "Se filtra contenido disciplinar de Filosofía del Derecho por no equivalencia temática.",
      "Se preservan solo patrones editoriales transversales.",
      "Se refuerza normalización JSON antes de propagación recursiva.",
      "Se corrigen relaciones del grafo a tipos permitidos.",
      "Se mantiene alerta sobre fuentes heredadas Codex y GPT-Pro como provisionales.",
      "Se consolida ADN editorial mínimo con identidad, estructura, calidad y trazabilidad.",
      "Se agregan vacíos locales como preguntas abiertas verificables."
    ]
  }
}