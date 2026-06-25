{
  "summary": [
    "Se consolida sincronizacion transversal desde actividad de otra materia sin trasladar contenido tematico no equivalente.",
    "Se preservan reglas utiles previas del destino y se refuerzan con abstracciones editoriales estables del origen.",
    "Se mantiene estrategia conservadora: identidad local del destino, estructura reusable y control estricto de calidad.",
    "Se refuerza normalizacion JSON y deduplicacion lossless como puerta obligatoria de propagacion.",
    "Se confirma cerebro editorial activo para Bases de derecho internacional publico con vacios locales abiertos como supuestos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local: Bases de derecho internacional publico.",
    "Usar contexto curricular verificado del destino: semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Usar codigo de curso local LDE-S4B1 en metadatos.",
    "No mezclar metadatos curriculares del origen con el destino.",
    "Usar carpeta de materia como entrada canonica.",
    "Tratar Codex y GPT-Pro como procedencia provisional, no como identidad del entregable.",
    "Marcar como supuesto todo dato no visible en consigna local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeacion semanal.",
    "Distinguir reporte, presentacion y producto visual segun consigna.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Conservar separacion entre README, programa analitico, .bib y plantillas .tex."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Integrar conceptos, normas, doctrina o datos pertinentes al caso.",
    "Evitar extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna de la actividad vigente.",
    "Mantener auditoria de parseo y cambios por ciclo para evitar regresiones."
  ],
  "latex_rules": [
    "Reutilizar plantilla .tex local sin romper identidad institucional.",
    "Mantener compatibilidad con clase article, spanish, letterpaper y oneside.",
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Mantener claves BibTeX estables.",
    "Corregir caracteres anomalos en rutas y nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Revisar y cerrar correctamente entornos tabular antes de compilar."
  ],
  "bibliography_rules": [
    "Registrar fuentes de actividad en bases-de-derecho-internacional-publico.bib.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Validar que toda clave citada exista en el .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "No transferir redaccion literal ni contenido tematico especifico de Filosofia del Derecho.",
    "Aplicar compresion por union-dedupe sin eliminar reglas utiles previas.",
    "No convertir supuestos en reglas definitivas sin verificacion local.",
    "Si aparece salida no estructurada, normalizar manualmente antes de propagar."
  ],
  "open_questions": [
    "Confirmar criterio editorial final sobre publico sin acento frente a publico con acento en nombre de materia.",
    "Confirmar correccion de nombres con caracteres anomalos en README.",
    "Confirmar resolucion de tokens $(@{...}.Slug) en README y programa analitico.",
    "Confirmar reparacion completa del entorno tabular en reporte .tex.",
    "Supuesto: faltan consignas de actividades especificas del destino para granularidad adicional."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador ante evidencia incompleta."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada obligatoria antes de propagacion.",
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Destino verificado: semestre 4, bloque 1, obligatoria, 8 creditos.",
        "Asignatura: Bases de derecho internacional publico.",
        "No mezclar contexto curricular entre materias."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables juridicos claros, verificables y utiles para practica profesional.",
      "Sostener continuidad editorial entre actividades sin perder identidad local."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales no redundantes.",
      "Supuestos etiquetados.",
      "Cierre con criterio juridico aplicable.",
      "Consistencia cita-bibliografia."
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
          "justification": "La conclusion juridica valida requiere respaldo."
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
        "Bib local destino: claves institucionales existentes.",
        "Memoria origen: gates de parseo JSON, estructura minima, supuestos y evidencia verificable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 15: se refuerza transferencia transversal conservadora sin contaminacion tematica entre materias.",
      "Ciclo 15: se preservan reglas previas del destino y se deduplican equivalencias semanticas.",
      "Ciclo 15: se incorporan del origen solo abstracciones estables de estructura, calidad y argumentacion.",
      "Ciclo 15: se mantienen abiertos vacios locales de contexto como supuestos verificables."
    ]
  }
}