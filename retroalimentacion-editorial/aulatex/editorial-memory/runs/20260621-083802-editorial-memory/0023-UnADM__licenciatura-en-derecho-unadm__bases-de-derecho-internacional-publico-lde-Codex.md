{
  "summary": [
    "Se consolida sincronizacion transversal con transferencia de abstracciones estables desde actividad origen.",
    "Se preserva identidad UnADM y contexto curricular local de la materia destino.",
    "Se refuerza normalizacion estructurada obligatoria antes de propagacion recursiva.",
    "Se mantienen ejes editoriales reutilizables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se evita traslado de contenido tematico especifico de Filosofia del Derecho por no equivalencia de nodos.",
    "Se incorpora correccion transversal verificable: resolver tokens sin expandir y caracteres anómalos en README/programa.",
    "Se mantiene incidencia historica: bloquear reutilizacion de salidas no JSON parseable sin normalizacion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local de la materia en todos los entregables.",
    "Alinear entregables a Licenciatura en Derecho, semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Usar LDE-S4B1 como codigo de curso en metadatos.",
    "Tratar Codex/GPT-Pro como procedencia provisional, no como identidad del entregable.",
    "Marcar como supuesto cualquier dato no visible en la consigna local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear estructura al producto solicitado por la planeacion semanal.",
    "Distinguir reporte, presentacion y producto visual segun consigna.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener separado README, programa analitico, .bib y plantillas .tex."
  ],
  "activity_rules": [
    "Adaptar cada actividad al producto exacto solicitado.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Distinguir hechos, argumentos, normas y criterio propio.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
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
    "Validar consistencia entre README, programa analitico, .bib y plantillas locales."
  ],
  "latex_rules": [
    "Reutilizar plantilla .tex local sin romper identidad institucional.",
    "Mantener compatibilidad con article, spanish, letterpaper y oneside.",
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Revisar y cerrar entornos tabular antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir caracteres anómalos en nombres de archivo y rutas antes de compilar."
  ],
  "bibliography_rules": [
    "Registrar fuentes de actividad en bases-de-derecho-internacional-publico.bib.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Validar que toda clave citada exista en el .bib local.",
    "Mantener unadmSitioWeb y unadmMallaDerecho2024 como base institucional."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas, estables y no duplicadas.",
    "Aplicar compresion lossless por union y deduplicacion.",
    "No propagar contenido tematico especifico entre nodos no equivalentes.",
    "Preservar reglas utiles previas aunque cambien de categoria.",
    "No convertir supuestos en reglas definitivas.",
    "Registrar incidencias historicas de parseo y exigir normalizacion previa.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual en saltos transversales."
  ],
  "open_questions": [
    "Confirmar criterio editorial final sobre publico vs público en nombres visibles.",
    "Confirmar si se normalizaran de inmediato tokens $(@{...}.Slug) en README y programa.",
    "Confirmar formato minimo de conclusion juridica por tipo de actividad.",
    "Confirmar rubrica local para calibrar profundidad argumentativa.",
    "Supuesto: no hay consigna de actividad especifica cargada en este ciclo para la materia destino."
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
        "Normalizacion estructurada obligatoria antes de propagacion.",
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 4, bloque 1, obligatoria, 8 creditos.",
        "Asignatura: Bases de derecho internacional publico."
      ]
    },
    "essence": [
      "Problema juridico o social que activa la actividad.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable y trazable.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en entregables juridicos claros, verificables y utiles para practica profesional.",
      "Garantizar consistencia editorial transversal sin perder contexto local de materia."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales sin redundancia.",
      "Supuestos etiquetados.",
      "Cierre con criterio juridico aplicable.",
      "Trazabilidad entre consigna, desarrollo, citas y bibliografia."
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
        "Consistencia cita-bibliografia",
        "Normalizacion de tokens de nombre de archivo"
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
          "justification": "El producto y la forma dependen de la instruccion semanal."
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
          "justification": "Sin estructura parseable no hay transferencia segura."
        },
        {
          "source": "Consistencia cita-bibliografia",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita afirmaciones sin fuente y citas rotas."
        },
        {
          "source": "Normalizacion de tokens de nombre de archivo",
          "target": "Compilacion LaTeX estable",
          "kind": "supports",
          "justification": "Eliminar tokens sin expandir reduce errores de referencia y rutas."
        }
      ],
      "evidence": [
        "README destino define identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico destino define proposito y ejes de trabajo.",
        "Archivo .bib local contiene claves institucionales verificables.",
        "Origen aporta regla estable de normalizacion estructurada previa a propagacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 23: se deduplican reglas repetidas y se preserva contenido util previo sin recorte.",
      "Ciclo 23: se agrega regla transversal verificable para resolver tokens $(@{...}.Slug).",
      "Ciclo 23: se mantiene estrategia conservadora, sin traslado de doctrina especifica de Filosofia del Derecho.",
      "Ciclo 23: se refuerzan gates de parseo JSON y consistencia cita-bibliografia."
    ]
  }
}