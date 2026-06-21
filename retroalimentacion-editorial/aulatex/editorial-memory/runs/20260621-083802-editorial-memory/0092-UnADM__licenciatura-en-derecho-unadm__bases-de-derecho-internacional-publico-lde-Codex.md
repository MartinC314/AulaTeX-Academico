{
  "summary": [
    "Se consolida sincronizacion transversal desde actividad origen hacia materia destino con estrategia conservadora.",
    "Se preservan reglas validas previas del destino y se deduplican sin perdida.",
    "Se refuerzan abstracciones estables: identidad UnADM, estructura argumentativa, calidad y normalizacion.",
    "No se transfiere contenido tematico especifico de Filosofia del Derecho al destino.",
    "Se mantienen incidencias historicas de salidas no parseables como control de riesgo editorial."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local: Bases de derecho internacional publico.",
    "Usar contexto curricular verificado del destino: semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "No mezclar metadatos curriculares entre materias.",
    "Tratar Codex/GPT-Pro como procedencia provisional, no como identidad del entregable.",
    "Marcar como supuesto todo dato no visible en la consigna local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Estructurar en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el desarrollo al producto solicitado por la planeacion semanal.",
    "Distinguir reporte, presentacion y producto visual segun consigna.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
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
    "Verificar correspondencia entre consigna, producto entregado y programa analitico."
  ],
  "latex_rules": [
    "Reutilizar plantilla .tex local sin romper identidad institucional.",
    "Mantener compatibilidad con article, spanish, letterpaper y oneside.",
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Corregir caracteres anomalos en nombres y rutas antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Revisar cierre correcto de entornos tabular antes de compilar."
  ],
  "bibliography_rules": [
    "Registrar fuentes de actividad en bases-de-derecho-internacional-publico.bib.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Validar que toda clave citada exista en el .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas, estables y no duplicadas.",
    "Aplicar compresion lossless por union-dedupe sin recorte semantico.",
    "No propagar supuestos como reglas definitivas.",
    "Preservar reglas utiles previas aunque cambien de categoria.",
    "Mantener trazabilidad de incidencias historicas de parseo.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual en saltos transversales."
  ],
  "open_questions": [
    "Confirmar correccion de entradas con caracteres anomalos en README.",
    "Confirmar resolucion de tokens $(@{...}.Slug) en README y programa analitico.",
    "Confirmar criterio editorial final sobre publico con o sin acento en nombres visibles.",
    "Confirmar si existe rubrica local por actividad para ajustar profundidad argumentativa.",
    "Supuesto: el .bib canonico del destino es bases-de-derecho-internacional-publico.bib; validar en automatizacion."
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
        "No mezclar contexto curricular de nodos origen."
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
      "Transformar planeacion semanal en productos academicos rigurosos y verificables.",
      "Asegurar consistencia institucional, argumentativa y tecnica en cada entrega."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales sin redundancia.",
      "Supuestos siempre etiquetados.",
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
          "justification": "El producto y su forma dependen de la instruccion local."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica valida requiere respaldo comprobable."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Sincronizacion transversal",
          "kind": "depends_on",
          "justification": "Sin parseo valido no hay propagacion segura."
        },
        {
          "source": "Consistencia cita-bibliografia",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita afirmaciones sin fuente y errores de referencia."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura argumentativa juridica",
          "kind": "develops",
          "justification": "La identidad define tono, formato y exigencia de rigor."
        }
      ],
      "evidence": [
        "README del destino: identidad, ubicacion curricular, pauta editorial.",
        "Programa analitico del destino: proposito y ejes de trabajo.",
        "Archivo .bib local con fuentes institucionales base.",
        "Regla heredada valida: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 92: se consolidan reglas transversales estables sin traslado tematico del origen.",
      "Ciclo 92: se refuerza gate de JSON parseable como precondicion de propagacion recursiva.",
      "Ciclo 92: se conserva deduplicacion lossless y no regresion de reglas utiles previas."
    ]
  }
}