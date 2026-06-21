{
  "summary": [
    "Sincronizacion transversal aplicada desde actividad de Filosofia del Derecho hacia materia de Antropologia con estrategia conservadora.",
    "Se preservan reglas institucionales UnADM, normalizacion estructurada y compresion por union-dedupe sin regresion.",
    "Se transfieren solo abstracciones estables: objetivo, evidencia verificable, analisis propio, coherencia y cierre transferible.",
    "Se evita transferir contenidos tematicos exclusivos de Filosofia del Derecho al destino.",
    "Se refuerza resolucion de placeholders en README y programa para nombre literal del .bib local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener contexto curricular local del destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar toda fuente heredada no verificada como provisional.",
    "No trasladar metadatos curriculares especificos de Filosofia del Derecho a Antropologia."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Separar artefactos: reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias canonicas de estructura."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Evitar afirmaciones sin puente argumentativo entre cultura y derecho.",
    "Cerrar con conclusion transferible a la practica juridica."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa del esquema antes de reutilizar.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No promover reglas provisionales a definitivas sin validacion local disciplinar."
  ],
  "latex_rules": [
    "Usar codificacion y espanol coherentes con la plantilla local.",
    "Mantener clase y formato base salvo justificacion academica.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README, programa y rutas de archivos."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables y consultables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales pertinentes.",
    "Registrar fuentes especificas de cada actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Marcar como supuesto cualquier extrapolacion bibliografica no confirmada."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y abstractas entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar propagar redaccion literal o contenido tematico exclusivo de otra materia.",
    "Mantener compresion lossless por deduplicacion y union.",
    "Registrar incidencias de parseo como alertas reutilizables inter-materias."
  ],
  "open_questions": [
    "[Supuesto] Confirmar si la conclusion juridica es obligatoria en todas las actividades de Antropologia.",
    "Confirmar estandar unico de citacion aplicable a la licenciatura.",
    "Confirmar si LDE-S4B2 es clave institucional definitiva o clave local.",
    "Confirmar si existen fuentes base obligatorias adicionales para la materia destino.",
    "Confirmar resolucion final de placeholders del .bib en documentos auxiliares."
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
        "Asignatura destino: Antropologia de la cultura en Mexico.",
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
      "Convertir planeacion semanal en productos academicos verificables y utiles para la practica.",
      "Sostener coherencia institucional y calidad transversal entre materias."
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
      "Coherencia entre consigna, desarrollo y cierre."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON parseable",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Resolucion de placeholders",
        "Compresion union-dedupe lossless"
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
          "justification": "Sin JSON valido no hay reutilizacion confiable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura gana validez cuando esta respaldada."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion deriva del razonamiento y no del resumen."
        },
        {
          "source": "Resolucion de placeholders",
          "target": "Normalizacion estructurada",
          "kind": "supports",
          "justification": "Evita rutas corruptas y mejora consistencia editorial."
        }
      ],
      "evidence": [
        "README destino confirma identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico confirma ejes: problema, conceptos, producto, analisis y cierre.",
        "Bib local confirma fuentes base institucionales verificables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 69: se consolidan abstracciones estables del origen sin arrastre tematico disciplinar.",
      "Ciclo 69: se mantiene gate estricto de JSON parseable y normalizacion previa.",
      "Ciclo 69: se refuerza trazabilidad bibliografica y resolucion de tokens dinamicos."
    ]
  }
}