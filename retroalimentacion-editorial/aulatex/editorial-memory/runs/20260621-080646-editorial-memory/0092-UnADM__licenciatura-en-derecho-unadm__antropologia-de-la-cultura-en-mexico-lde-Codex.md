{
  "summary": [
    "Sincronizacion transversal conservadora aplicada desde actividad de Filosofia del Derecho hacia materia de Antropologia.",
    "Se preservan reglas institucionales UnADM y se deduplican sin perdida.",
    "Se transfieren solo abstracciones estables: objetivo, estructura argumentativa, evidencia y cierre profesional.",
    "Se evita transferir contenidos tematicos exclusivos de Filosofia del Derecho al destino.",
    "Se mantiene bloqueo de propagacion ante salidas no JSON parseable.",
    "Se refuerza normalizacion de placeholders de rutas y nombres de archivos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener contexto curricular local del destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar toda fuente heredada no verificada como provisional hasta validacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o teorico, analisis propio y cierre.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Cerrar con conclusion transferible a la practica juridica o sociojuridica."
  ],
  "activity_rules": [
    "Sustentar afirmaciones relevantes con fuente verificable y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Integrar puente argumentativo entre analisis cultural y efecto juridico cuando aplique.",
    "No asumir fuentes de semanas o materias distintas sin confirmacion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa del esquema antes de reutilizar.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No promover reglas provisionales a definitivas sin validacion disciplinar."
  ],
  "latex_rules": [
    "Usar codificacion en español y acentos correctos en .tex y .bib.",
    "Mantener plantilla base de la materia y campos institucionales completos.",
    "Actualizar documenttitle y documentsubtitle por actividad real.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens dinamicos tipo $(@{...}.Slug) en README, programa y rutas antes de compilar."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales pertinentes.",
    "Registrar fuentes especificas de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, año, fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener trazabilidad de procedencia de archivos locales usados como evidencia."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferir redaccion literal y metadatos curriculares de otra materia.",
    "Mantener compresion lossless por union-dedupe y sin regresion.",
    "Registrar incidencias de parseo como alertas reutilizables inter-materias.",
    "Si falta contexto local de actividad, conservar cerebro minimo y abrir preguntas."
  ],
  "open_questions": [
    "Supuesto: falta consigna puntual de actividades especificas en el destino; confirmar productos requeridos.",
    "Confirmar estandar unico de citacion para la licenciatura (APA u otro).",
    "Confirmar si la conclusion juridica es obligatoria en todas las actividades de Antropologia.",
    "Confirmar si la clave LDE-S4B2 es oficial institucional o etiqueta local.",
    "Confirmar que no queden placeholders en README y programa analitico."
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
        "Entrada canonica por carpeta de materia."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Destino: Antropologia de la cultura en Mexico.",
        "Semestre 4, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema relevante.",
      "Conceptos y marco pertinente.",
      "Evidencia trazable.",
      "Analisis propio.",
      "Conclusion transferible."
    ],
    "reason_for_being": [
      "Convertir la planeacion semanal en productos academicos verificables y utiles.",
      "Sostener coherencia institucional, metodologica y argumentativa en toda la suite."
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
        "Conclusion transferible",
        "Puente sociojuridico"
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
          "source": "Identidad institucional UnADM",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "La pauta institucional exige trazabilidad y rigor academico."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura personal se fortalece con respaldo comprobable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion util surge del razonamiento, no del resumen."
        },
        {
          "source": "Puente sociojuridico",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "Conecta hallazgos culturales con implicaciones juridicas aplicables."
        }
      ],
      "evidence": [
        "README local: identidad UnADM y pauta editorial.",
        "Programa analitico local: ejes problema, conceptos, producto, analisis y cierre.",
        ".bib local: unadmSitioWeb y unadmMallaDerecho2024.",
        "Regla heredada estable: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 92: deduplicacion completa sin eliminar reglas utiles previas.",
      "Ciclo 92: transferencia transversal limitada a abstracciones estables.",
      "Ciclo 92: fortalecidos gates de parseo, estructura minima y trazabilidad bibliografica.",
      "Ciclo 92: preservada identidad UnADM con contexto curricular local del destino."
    ]
  }
}