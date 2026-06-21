{
  "summary": [
    "Se consolida sincronizacion transversal con reglas estables y reutilizables.",
    "Se preserva identidad UnADM y contexto curricular local del destino.",
    "Se refuerza normalizacion estructurada obligatoria antes de propagacion recursiva.",
    "Se transfieren ejes editoriales abstractos: problema, conceptos, evidencia, analisis y conclusion.",
    "Se mantiene estrategia conservadora: no trasladar contenido tematico especifico de Filosofia del Derecho."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local: Bases de derecho internacional publico.",
    "Usar contexto curricular verificado del destino: semestre 4, bloque 1, obligatoria, 8 creditos.",
    "No mezclar metadatos curriculares entre materias.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como procedencia provisional, no como identidad."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear estructura al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Distinguir claramente reporte, presentacion y producto visual segun consigna."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, normas, doctrina, argumentos y criterio propio.",
    "Evitar extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar memoria.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregado y consigna vigente.",
    "Validar sintaxis LaTeX y referencias sin ruptura antes de compilar."
  ],
  "latex_rules": [
    "Reutilizar plantilla .tex local de la materia como base.",
    "Mantener compatibilidad con clase article, spanish, letterpaper y oneside.",
    "Completar metadatos sin romper identidad institucional.",
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Corregir caracteres anomalos en rutas y nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Revisar y cerrar entornos tabular incompletos en plantillas locales."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas de actividad en bases-de-derecho-internacional-publico.bib.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Validar que toda clave citada exista en el .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas, abstractas y no duplicadas.",
    "Aplicar compresion lossless por union y deduplicacion.",
    "Preservar reglas utiles previas sin regresion.",
    "No propagar supuestos como reglas definitivas.",
    "Registrar incidencias historicas de parseo como control de riesgo.",
    "Si falta contexto local, mantener cerebro minimo y abrir vacios como preguntas."
  ],
  "open_questions": [
    "Confirmar criterio editorial final para 'publico' con o sin acento en nombres visibles.",
    "Confirmar correccion integral de tokens $(@{...}.Slug) en archivos de contexto.",
    "Confirmar reparacion completa del entorno tabular truncado en reporte base.",
    "Confirmar rubrica de evaluacion local por actividad para ajustar profundidad.",
    "Supuesto: no hay lista obligatoria adicional de fuentes para cada semana en destino."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada obligatoria antes de propagacion."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Destino: semestre 4, bloque 1, obligatoria, 8 creditos.",
        "No mezclar contexto curricular del origen con el destino."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables academicos consistentes.",
      "Garantizar trazabilidad, calidad formal y rigor argumentativo.",
      "Sostener un cerebro editorial persistente, estable y reutilizable."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales sin redundancia.",
      "Supuestos etiquetados de forma visible.",
      "Cierre con criterio juridico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> norma/doctrina -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> posicion propia.",
      "Consigna -> desarrollo alineado -> verificacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Consigna de actividad",
        "Estructura argumentativa juridica",
        "Evidencia verificable",
        "Conclusion transferible",
        "Normalizacion JSON",
        "Consistencia cita-bibliografia"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Consigna de actividad",
          "target": "Estructura argumentativa juridica",
          "kind": "depends_on",
          "justification": "La forma del entregable depende del producto solicitado."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica valida requiere respaldo documental."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia segura."
        },
        {
          "source": "Consistencia cita-bibliografia",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita afirmaciones sin fuente y referencias rotas."
        }
      ],
      "evidence": [
        "README destino: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico destino: proposito y ejes de trabajo.",
        "Bibliografia local: claves institucionales base.",
        "Memoria origen: regla transversal de normalizacion y ejes editoriales."
      ]
    },
    "reinforcement_log": [
      "Ciclo 62: se fusionaron reglas transversales estables sin arrastre tematico especifico.",
      "Ciclo 62: se reforzo gate de JSON parseable como requisito de propagacion.",
      "Ciclo 62: se mantuvo compresion lossless por deduplicacion y sin regresion."
    ]
  }
}