{
  "summary": [
    "Sincronizacion transversal consolidada desde actividad de Filosofia del Derecho hacia materia de Antropologia sin traslado tematico literal.",
    "Se preserva identidad UnADM, estructura canonica y compresion union-dedupe lossless sin regresion.",
    "Se refuerzan gates de parseo JSON, normalizacion estructurada y trazabilidad de fuentes.",
    "Se mantiene regla de marcar supuestos y fuentes heredadas no verificadas como provisionales.",
    "Se corrige a nivel editorial la necesidad de resolver placeholders de Slug en README y programa analitico."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener contexto curricular local del destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar toda fuente heredada no verificada como provisional hasta validacion local.",
    "No transferir metadatos curriculares especificos de Filosofia del Derecho al destino."
  ],
  "structure_rules": [
    "Iniciar cada entrega con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar secciones en: conceptos clave, marco normativo o teorico, analisis propio y cierre.",
    "Alinear el producto al entregable solicitado en la planeacion semanal.",
    "Separar artefactos: reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias canonicas de estructura."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Evitar afirmaciones culturales o juridicas sin puente argumentativo.",
    "Cerrar con conclusion transferible a la practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar memoria.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que toda afirmacion tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No promover reglas provisionales a definitivas sin validacion disciplinar."
  ],
  "latex_rules": [
    "Mantener codificacion y acentos correctos en espanol en .tex y .bib.",
    "Conservar clase y plantilla base salvo justificacion academica.",
    "Compilar sin errores criticos, sin referencias rotas y sin tokens sin resolver.",
    "Resolver placeholders tipo $(@{...}.Slug) a nombres literales de archivo.",
    "Verificar rutas y nombres de archivos del README antes de referenciarlos.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo obras verificables y consultables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes especificas de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener unadmSitioWeb y unadmMallaDerecho2024 como base institucional local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo abstracciones editoriales estables ya validadas.",
    "Aplicar union-dedupe lossless sin eliminar reglas utiles previas.",
    "Evitar traslado de contenido tematico propio de otra materia.",
    "Registrar incidencias de parseo como alertas transversales reutilizables.",
    "Si falta contexto local, mantener cerebro minimo y abrir vacios como preguntas."
  ],
  "open_questions": [
    "Supuesto: falta confirmacion del estandar de citas unico para la licenciatura.",
    "Confirmar si LDE-S4B2 es clave oficial institucional o clave local.",
    "Confirmar si toda actividad de la materia exige conclusion juridica explicita.",
    "Confirmar resolucion definitiva del nombre de .bib en documentos con placeholder Slug.",
    "Supuesto: reglas heredadas de fuentes no verificadas siguen en estado provisional."
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
        "Semestre 4, bloque 2, obligatoria, 8 creditos.",
        "Asignatura destino: Antropologia de la cultura en Mexico."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco pertinente.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros, verificables y utiles para practica profesional."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Cierre con valor profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente -> interpretacion propia.",
      "Consistencia entre pregunta guia y respuesta final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON parseable",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Resolucion de placeholders"
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
          "justification": "Sin parseo valido no hay propagacion confiable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura academica requiere respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion util deriva del razonamiento argumentado."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "La pauta institucional exige integridad academica."
        }
      ],
      "evidence": [
        "README y programa analitico del destino definen ejes editoriales y rol institucional.",
        "Archivo .bib local contiene base institucional verificable.",
        "Memoria origen aporta patrones estables de objetivo, evidencia, postura y coherencia."
      ]
    },
    "reinforcement_log": [
      "Ciclo 16: deduplicacion completa de reglas repetidas en summary, identidad, estructura y gates.",
      "Ciclo 16: transferencia conservadora solo de abstracciones estables entre nodos no equivalentes.",
      "Ciclo 16: se mantiene alerta historica de salidas no parseables y normalizacion manual cuando aplique.",
      "Ciclo 16: se refuerza no trasladar contenido tematico de Filosofia del Derecho a Antropologia."
    ]
  }
}