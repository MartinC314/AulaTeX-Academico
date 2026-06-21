{
  "summary": [
    "Sincronizacion transversal aplicada con union-dedupe lossless y sin regresion.",
    "Se conserva identidad UnADM y adscripcion a Licenciatura en Derecho en nodo materia.",
    "Se transfieren solo abstracciones estables desde Filosofia del Derecho.",
    "Se refuerzan ejes reutilizables: problema, conceptos, evidencia, analisis propio y conclusion transferible.",
    "Se mantiene alerta institucional: bloquear propagacion si no hay JSON parseable.",
    "Se conserva regla de marcar supuestos cuando falte consigna local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener datos curriculares locales del destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar toda fuente heredada no verificada como provisional.",
    "No trasladar metadatos especificos de Filosofia del Derecho al destino."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Distinguir artefactos: reporte, presentacion y bibliografia.",
    "Cerrar con conclusion transferible a la practica profesional."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Evitar afirmaciones juridicas o culturales sin puente argumentativo.",
    "Validar que el producto final corresponda a la consigna real de la actividad."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar memoria.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No promover reglas provisionales a definitivas sin verificacion local."
  ],
  "latex_rules": [
    "Usar configuracion en espanol y acentos correctos en .tex y .bib.",
    "Mantener plantilla base de la materia salvo necesidad justificada.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README, programa y rutas.",
    "Corregir nombres de archivo truncados antes de compilar.",
    "Compilar sin errores criticos y sin referencias rotas."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales pertinentes.",
    "Registrar fuentes especificas de cada actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "No citar claves ausentes en el .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y abstractas.",
    "Priorizar identidad, gates de calidad, estructura reusable y grafo conceptual.",
    "Evitar transferencia de contenido tematico literal entre materias no equivalentes.",
    "Mantener compresion lossless por union-dedupe.",
    "Registrar incidencias de parseo como alerta transversal reutilizable.",
    "Preservar reglas utiles previas sin eliminacion."
  ],
  "open_questions": [
    "Supuesto: falta consigna puntual de actividades locales; confirmar formato exigido por semana.",
    "Confirmar rubrica oficial de evaluacion para ajustar profundidad argumentativa.",
    "Confirmar estandar de citacion institucional unico para la licenciatura.",
    "Confirmar si la conclusion juridica es obligatoria en todas las actividades de la materia.",
    "Confirmar si la clave LDE-S4B2 es definitiva institucional o solo local."
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
        "Integridad academica con trazabilidad.",
        "Entrada canonica por carpeta de materia."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 4, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Antropologia de la cultura en Mexico."
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
      "Convertir planeacion semanal en productos academicos validos.",
      "Asegurar coherencia entre consigna, desarrollo y cierre.",
      "Sostener calidad institucional en propagacion transversal."
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
      "Pregunta guia -> desarrollo coherente -> respuesta final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON parseable",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Supuestos marcados"
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
          "justification": "La postura personal gana solidez con respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion util surge del razonamiento, no del resumen."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "La integridad academica institucional exige citas comprobables."
        }
      ],
      "evidence": [
        "README de materia destino: identidad UnADM y pauta editorial.",
        "Programa analitico destino: ejes de trabajo reutilizables.",
        "Bib local destino: claves base institucionales verificables.",
        "Memoria origen: gate de JSON parseable y normalizacion previa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 62: se consolidan abstracciones estables sin trasladar contenido tematico de Filosofia del Derecho.",
      "Ciclo 62: se refuerza gate de JSON parseable como condicion de propagacion.",
      "Ciclo 62: se preserva union-dedupe lossless y politica sin regresion.",
      "Ciclo 62: se mantiene regla de marcar supuestos ante vacios de consigna."
    ]
  }
}