{
  "summary": [
    "Sincronizacion transversal conservadora aplicada desde actividad de Filosofia del Derecho hacia materia de Antropologia.",
    "Se preserva identidad UnADM y contexto curricular local del destino sin mezclar metadatos de otra asignatura.",
    "Se refuerzan abstracciones estables: objetivo, problema, evidencia, analisis propio y conclusion transferible.",
    "Se mantiene compresion lossless por union-dedupe y control de no regresion.",
    "Se conserva alerta institucional: bloquear propagacion si no hay JSON parseable y normalizar salidas no estructuradas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener materia destino: Antropologia de la cultura en Mexico.",
    "Mantener ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales.",
    "No transferir metadatos especificos de Filosofia del Derecho al destino."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Distinguir reporte, presentacion y bibliografia como artefactos separados.",
    "Usar README y programa analitico como guias canonicas de estructura.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Evitar extrapolar contenidos tematicos de otra materia sin puente argumentativo.",
    "Comprobar que el producto final corresponde a la consigna real de la actividad."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar memoria.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que afirmaciones sin respaldo esten eliminadas o marcadas como supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No promover reglas provisionales a definitivas sin verificacion local."
  ],
  "latex_rules": [
    "Usar codificacion en español consistente en .tex y .bib.",
    "Mantener clase y configuracion base de plantilla salvo justificacion academica.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Mantener coursename y coursecode locales del destino salvo instruccion institucional.",
    "Resolver placeholders tipo $(@{...}.Slug) a nombres literales antes de compilar.",
    "Corregir rutas o nombres con caracteres truncados antes de compilar.",
    "Compilar sin errores criticos, sin referencias rotas y sin tokens sin expandir."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales pertinentes.",
    "Registrar fuentes de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No citar claves inexistentes en el .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas estables y validadas.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferir redaccion literal o contenido tematico exclusivo del nodo origen.",
    "Mantener union-dedupe lossless en ciclos futuros.",
    "Registrar incidencias de parseo como alertas transversales reutilizables."
  ],
  "open_questions": [
    "Supuesto: falta consigna puntual de actividades locales de Antropologia; confirmar productos exactos por semana.",
    "Confirmar estandar institucional de citacion para toda la licenciatura.",
    "Confirmar si LDE-S4B2 es clave oficial definitiva o clave operativa local.",
    "Confirmar si toda actividad de la materia exige conclusion juridica explicita.",
    "Confirmar politica final para nombres de archivo cuando existan placeholders heredados."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con trazabilidad de fuentes.",
        "Entrada canonica por carpeta de materia."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Antropologia de la cultura en Mexico.",
        "Semestre 4, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema claro.",
      "Conceptos pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y utiles para la formacion juridica."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Cierre con valor profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente verificable -> interpretacion propia.",
      "Coherencia vertical entre consigna, desarrollo y cierre."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON parseable",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Separacion de artefactos (reporte/presentacion/bibliografia)"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Validacion JSON parseable",
          "target": "Normalizacion estructurada",
          "kind": "depends_on",
          "justification": "La propagacion confiable requiere estructura valida."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura academica gana solidez con respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion util depende del razonamiento y no del resumen."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Separacion de artefactos (reporte/presentacion/bibliografia)",
          "kind": "supports",
          "justification": "La consistencia editorial institucional exige estructura estable."
        }
      ],
      "evidence": [
        "README de la materia destino.",
        "Programa analitico de la materia destino.",
        "Archivo BibTeX local con entradas institucionales verificables.",
        "Regla heredada validada: bloquear salidas no JSON parseables."
      ]
    },
    "reinforcement_log": [
      "Se reforzo regla de no mezclar metadatos curriculares entre materias.",
      "Se reforzo gate de parseo JSON como condicion de propagacion.",
      "Se reforzo patron argumentativo comun sin transferir contenido tematico de Filosofia del Derecho.",
      "Se reforzo resolucion de placeholders en rutas y nombres de archivo."
    ]
  }
}