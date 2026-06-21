{
  "summary": [
    "Sincronizacion transversal aplicada con union-dedupe lossless y sin regresion.",
    "Se preservan reglas institucionales UnADM, estructura canonica y gates de parseo JSON.",
    "Se incorporan abstracciones estables del origen: objetivo puntual, evidencia verificable, postura propia y coherencia argumentativa.",
    "Se evita transferir contenidos tematicos exclusivos de Filosofia del Derecho al nodo de Antropologia.",
    "Se refuerza resolucion de placeholders y tokens dinamicos en README, programa y rutas .bib/.tex.",
    "Se mantiene alerta de fuentes heredadas no verificadas como provisionales."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar toda fuente heredada no verificada como provisional.",
    "No trasladar metadatos curriculares de otra materia al destino."
  ],
  "structure_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Separar secciones en: conceptos clave, marco normativo o teorico, analisis propio y cierre.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Cerrar con conclusion transferible a la practica juridica.",
    "Distinguir reporte, presentacion y bibliografia como artefactos separados.",
    "Resolver nombres de archivo corruptos o truncados antes de compilar."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Integrar puentes entre analisis cultural y efecto juridico cuando aplique.",
    "No asumir fuentes de semanas o actividades distintas sin confirmacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa del esquema antes de reutilizar.",
    "Revisar y normalizar manualmente respuestas no estructuradas en ciclo 1.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que README, programa y .tex no tengan placeholders sin resolver.",
    "No promover reglas provisionales a definitivas sin validacion disciplinar."
  ],
  "latex_rules": [
    "Usar configuracion en espanol y acentos correctos en .tex y .bib.",
    "Mantener clase y formato base salvo justificacion academica.",
    "Compilar sin errores criticos, referencias rotas ni claves BibTeX inexistentes.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion.",
    "Actualizar documenttitle y documentsubtitle por actividad real.",
    "Resolver tokens tipo $(@{...}.Slug) a nombre literal antes de citar archivos.",
    "Verificar rutas y nombres del README antes de referenciarlos en LaTeX."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales pertinentes.",
    "Registrar fuentes especificas por actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y abstractas entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar propagar redaccion literal, citas tematicas locales o artefactos de otra materia.",
    "Registrar incidencias de parseo como alertas reutilizables inter-materias.",
    "Mantener estrategia progresiva y conservadora: agregar solo mejoras verificables.",
    "Si falta contexto local, mantener cerebro minimo y abrir preguntas explicitas."
  ],
  "open_questions": [
    "Supuesto: falta consigna puntual de la actividad destino; confirmar tipo de producto.",
    "Confirmar rubrica oficial de evaluacion para calibrar profundidad argumentativa.",
    "Confirmar estandar de citacion institucional unico para la licenciatura.",
    "Confirmar si la conclusion juridica es obligatoria en todas las actividades de la materia.",
    "Confirmar si la clave LDE-S4B2 es codificacion oficial o local."
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
        "Integridad academica con citas verificables.",
        "Carpeta de materia como entrada canonica."
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
      "Convertir planeacion semanal en productos academicos estructurados y verificables.",
      "Garantizar trazabilidad entre consigna, desarrollo y cierre argumentativo."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Uso consistente de supuestos marcados.",
      "Cierre con valor profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion relevante -> fuente verificable -> interpretacion propia.",
      "Coherencia entre pregunta guia y respuesta final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Normalizacion estructurada",
        "Validacion JSON parseable"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige trazabilidad y citas verificables."
        },
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
          "justification": "El criterio personal se legitima con respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion util surge del razonamiento y no del resumen."
        }
      ],
      "evidence": [
        "README de la materia destino: identidad UnADM y conclusion juridica.",
        "Programa analitico destino: ejes problema, conceptos, producto, analisis y cierre.",
        "Archivo .bib local: unadmSitioWeb y unadmMallaDerecho2024."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas preservando significado.",
      "Se transfirieron solo abstracciones editoriales estables del origen.",
      "Se excluyeron contenidos doctrinales exclusivos de Filosofia del Derecho.",
      "Se reforzo control de placeholders y parseo JSON como gate transversal."
    ]
  }
}