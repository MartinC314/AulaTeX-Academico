{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre actividad origen y materia destino.",
    "Se preservan reglas utiles vigentes y se deduplican sin perdida.",
    "Se refuerzan abstracciones estables: identidad UnADM, estructura argumentativa, calidad y normalizacion.",
    "No se transfiere contenido tematico especifico de Filosofia del Derecho al destino.",
    "Se mantiene trazabilidad de incidencias de JSON no parseable en ciclos previos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local: Bases de derecho internacional publico.",
    "Usar contexto curricular verificado del destino: semestre 4, bloque 1, obligatoria, 8 creditos.",
    "No mezclar metadatos curriculares entre materias.",
    "Usar carpeta de materia como entrada canonica.",
    "Tratar Codex/GPT-Pro como procedencia provisional, no como identidad del entregable.",
    "Marcar como supuesto todo dato no visible en la consigna local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por la planeacion semanal.",
    "Distinguir reporte, presentacion y producto visual segun consigna.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Conservar separacion entre README, programa analitico, .bib y plantillas .tex."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, argumentos, normas y criterio propio.",
    "Evitar extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna de la actividad.",
    "Validar sintaxis LaTeX y cierre de entornos antes de compilar."
  ],
  "latex_rules": [
    "Reutilizar plantillas locales de la materia sin romper identidad institucional.",
    "Mantener compatibilidad con article, spanish, letterpaper y oneside.",
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo con caracteres anomalos antes de compilar."
  ],
  "bibliography_rules": [
    "Registrar fuentes de actividad en bases-de-derecho-internacional-publico.bib.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Validar que toda clave citada exista en el .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas, estables y no duplicadas.",
    "Aplicar compresion lossless por union-dedupe, sin recorte semantico.",
    "Preservar reglas utiles previas y evitar regresiones.",
    "No propagar supuestos como reglas definitivas.",
    "Transferir solo abstracciones editoriales transversales en nodos no equivalentes.",
    "Registrar incidencias historicas de parseo como memoria de riesgo."
  ],
  "open_questions": [
    "Confirmar criterio editorial final para publico vs público en nombres visibles. [supuesto]",
    "Confirmar correccion definitiva de tokens $(@{...}.Slug) en README y programa analitico.",
    "Confirmar si existe rubrica local por actividad para gates de profundidad argumentativa. [supuesto]",
    "Confirmar si se normalizara el corte detectado de entorno tabular en el reporte .tex."
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
      "Convertir planeacion semanal en productos academicos consistentes y verificables.",
      "Asegurar trazabilidad editorial y calidad tecnica en LaTeX y bibliografia."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales sin redundancia.",
      "Supuestos etiquetados.",
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
          "justification": "La forma y alcance del entregable dependen de la consigna."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica requiere respaldo documental."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo valido no hay transferencia segura."
        },
        {
          "source": "Consistencia cita-bibliografia",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita afirmaciones sin fuente y claves rotas."
        }
      ],
      "evidence": [
        "README y programa analitico del destino validan identidad y ejes editoriales.",
        "Archivo .bib local contiene claves institucionales base verificables.",
        "Historial de incidencias confirma gate de JSON parseable como regla critica."
      ]
    },
    "reinforcement_log": [
      "Ciclo 76: deduplicacion integral sin eliminar reglas utiles previas.",
      "Ciclo 76: refuerzo de gates transversales de parseo, respaldo y consistencia cita-bib.",
      "Ciclo 76: transferencia conservadora sin arrastre tematico de Filosofia del Derecho.",
      "Ciclo 76: persistencia de trazabilidad de fuentes provisionales como procedencia."
    ]
  }
}