{
  "summary": [
    "Sincronizacion transversal ciclo 17 aplicada por union-dedupe lossless y sin regresion.",
    "Se preserva ADN UnADM del destino y se refuerzan abstracciones estables del origen.",
    "Se transfiere solo estructura reusable: objetivo, evidencia, analisis propio, coherencia y cierre transferible.",
    "Se evita migrar contenido tematico exclusivo de Filosofia del Derecho al nodo de Antropologia.",
    "Se mantiene alerta activa por salidas no JSON parseables y necesidad de normalizacion previa."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar toda fuente heredada no verificada como provisional.",
    "No transferir metadatos curriculares de otra asignatura al destino."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en bloques: conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear el producto al entregable real de la planeacion semanal.",
    "Separar artefactos: reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias canonicas locales."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Cerrar con conclusion transferible a practica juridica.",
    "Evitar afirmaciones sin respaldo o sin marca de supuesto."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar esquema minimo completo antes de reutilizar memoria.",
    "Normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Verificar consistencia entre citas en texto y archivo .bib.",
    "Verificar que no existan placeholders sin resolver en README, programa y .tex.",
    "No promover reglas provisionales a definitivas sin validacion local."
  ],
  "latex_rules": [
    "Mantener configuracion en espanol y compatibilidad con plantilla local.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Conservar claves BibTeX estables para evitar quiebres de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens dinamicos tipo $(@{...}.Slug) a nombres literales antes de compilar.",
    "Corregir rutas o nombres con caracteres truncados antes de referenciar."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales pertinentes.",
    "Registrar fuentes especificas de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener trazabilidad de procedencia en notas cuando aplique."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y abstraidas.",
    "Transferir patrones editoriales estables, no redaccion literal ni contenido tematico ajeno.",
    "Preservar reglas utiles previas y agregar mejoras verificables sin sustitucion destructiva.",
    "Registrar incidencias de parseo como alertas transversales reutilizables.",
    "Si falta contexto local, mantener cerebro minimo y abrir preguntas de verificacion."
  ],
  "open_questions": [
    "Supuesto: falta consigna puntual de actividades de la materia destino; confirmar formatos por semana.",
    "Confirmar estandar unico de citacion institucional para la licenciatura.",
    "Confirmar si coursecode LDE-S4B2 es oficial o clave operativa local.",
    "Confirmar si la conclusion juridica es obligatoria en todas las actividades de antropologia.",
    "Confirmar politica final para resolver y persistir nombres derivados de Slug en README y programa."
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
        "Asignatura: Antropologia de la cultura en Mexico."
      ]
    },
    "essence": [
      "Problema, conceptos, evidencia, analisis propio y conclusion transferible.",
      "Normalizacion estructurada antes de propagacion.",
      "Compresion lossless por deduplicacion y sin regresion."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables y argumentados.",
      "Sostener continuidad editorial transversal entre nodos no equivalentes.",
      "Asegurar calidad tecnica y academica en LaTeX y bibliografia."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Cierre con aplicacion profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> cita verificable -> interpretacion propia.",
      "Consigna -> desarrollo alineado -> cierre coherente."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Validacion JSON parseable",
        "Normalizacion estructurada",
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
          "justification": "Sin estructura valida no hay propagacion confiable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura se legitima con respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "El cierre util surge del razonamiento y no del resumen."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y trazabilidad."
        }
      ],
      "evidence": [
        "README y programa analitico del destino fijan ejes editoriales comunes.",
        "Memoria origen confirma gates de parseo JSON y normalizacion previa.",
        "Bibliografia local del destino contiene claves base institucionales verificables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 17: se consolidan reglas transversales estables sin mover contenidos disciplinares especificos.",
      "Ciclo 17: se refuerzan quality gates de parseo, estructura minima y trazabilidad bibliografica.",
      "Ciclo 17: se mantiene estrategia conservadora de supuestos y fuentes provisionales."
    ]
  }
}