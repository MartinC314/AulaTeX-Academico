{
  "summary": [
    "Se mantiene cerebro editorial de materia con identidad UnADM y contexto curricular local verificado.",
    "Se incorpora transferencia transversal estable desde actividad origen: ejes problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se refuerza normalizacion estructurada obligatoria antes de propagacion recursiva.",
    "Se preserva estrategia conservadora: no transferir contenido tematico especifico de Filosofia del Derecho al destino.",
    "Se confirma estado minimo operativo del destino: plantilla .tex, programa analitico y .bib local activos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local: Bases de derecho internacional publico.",
    "Alinear entregables a Licenciatura en Derecho, semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Usar codigo de curso LDE-S4B1 en metadatos.",
    "Usar carpeta de materia como entrada canonica.",
    "No mezclar metadatos curriculares del origen con el destino.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como procedencia provisional, no como identidad del entregable."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear estructura al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Distinguir reporte, presentacion y producto visual segun consigna.",
    "Conservar separacion entre README, programa analitico, .bib y plantillas .tex."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar extrapolar fuentes de semanas no confirmadas.",
    "Integrar conceptos, normas, doctrina o datos pertinentes al caso de actividad.",
    "Distinguir hechos, argumentos, normas y criterio propio.",
    "Marcar faltantes de consigna o evidencia como pendientes."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que README, programa analitico, .bib y plantillas locales coincidan.",
    "Validar sintaxis LaTeX y cierre de entornos antes de compilar."
  ],
  "latex_rules": [
    "Reutilizar plantilla .tex local de la materia sin romper identidad institucional.",
    "Mantener compatibilidad con clase article, spanish, letterpaper y oneside.",
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir caracteres anomalos en nombres de archivo y rutas antes de compilar.",
    "Revisar y cerrar correctamente entornos tabular antes de compilar."
  ],
  "bibliography_rules": [
    "Registrar fuentes de actividad en bases-de-derecho-internacional-publico.bib.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Validar que toda clave citada exista en el .bib local.",
    "Conservar entradas institucionales base: unadmSitioWeb y unadmMallaDerecho2024."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferir redaccion literal o contenido tematico especifico del origen.",
    "Preservar reglas utiles previas sin regresion.",
    "Aplicar compresion lossless por union y deduplicacion.",
    "Mantener trazabilidad de incidencias historicas de parseo no estructurado."
  ],
  "open_questions": [
    "Confirmar criterio editorial final sobre publico sin acento frente a publico con acento en nombres visibles.",
    "Confirmar correccion definitiva de tokens $(@{...}.Slug) en README y programa analitico.",
    "Confirmar reparacion completa del entorno tabular truncado en reporte-bases-de-derecho-internacional-publico.tex.",
    "Supuesto: no hay consigna de actividad especifica cargada en este ciclo para reglas de formato fino.",
    "Confirmar si se define plantilla de conclusion juridica por tipo de evidencia en esta materia."
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
        "Destino verificado: semestre 4, bloque 1, obligatoria, 8 creditos.",
        "No mezclar contexto curricular de nodos origen."
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
      "Transformar planeacion semanal en productos academicos juridicos verificables.",
      "Asegurar consistencia entre consigna, desarrollo argumentativo y cierre.",
      "Permitir propagacion segura entre nodos mediante memoria estructurada."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y no redundantes.",
      "Supuestos siempre etiquetados.",
      "Cierre con criterio juridico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> norma/doctrina -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> postura propia.",
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
          "justification": "El formato y profundidad del entregable dependen de la consigna local."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica valida exige respaldo documental."
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
        },
        {
          "source": "Ejes editoriales transversales",
          "target": "Calidad de entregables de materia",
          "kind": "develops",
          "justification": "La estructura reusable mejora coherencia y evaluabilidad."
        }
      ],
      "evidence": [
        "README destino: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico destino: proposito y ejes de trabajo.",
        "Archivo .bib destino: claves institucionales existentes.",
        "Memoria origen: refuerzo de gates JSON, supuestos etiquetados y estructura argumentativa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 79: se integran abstracciones estables del origen sin traslado tematico.",
      "Ciclo 79: se refuerzan quality gates de parseo JSON y respaldo de afirmaciones.",
      "Ciclo 79: se mantiene politica conservadora de no regresion y deduplicacion lossless.",
      "Ciclo 79: se prioriza coherencia curricular local del destino sobre metadatos heredados."
    ]
  }
}