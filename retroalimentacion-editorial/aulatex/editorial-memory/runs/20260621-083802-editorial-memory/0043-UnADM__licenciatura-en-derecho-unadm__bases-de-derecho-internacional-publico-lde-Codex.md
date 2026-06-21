{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia conservadora y sin regresion.",
    "Se preservan reglas institucionales, de estructura y de calidad ya vigentes en el destino.",
    "Se transfieren solo abstracciones estables desde actividad origen: ejes editoriales y normalizacion previa a propagacion.",
    "Se evita traslado de contenido tematico especifico de Filosofia del Derecho por no equivalencia de nodo.",
    "Se mantiene incidencia historica: bloquear reutilizacion de salidas no parseables sin normalizacion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local de la materia en todos los entregables.",
    "Alinear entregables al contexto curricular verificado del destino.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como procedencia provisional, no como identidad."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear la estructura al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Distinguir reporte, presentacion u otro producto visual segun consigna."
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
    "Verificar correspondencia entre consigna, producto solicitado y entregable final."
  ],
  "latex_rules": [
    "Reutilizar plantillas .tex locales de la materia como base.",
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir en README y programa analitico antes de referenciar archivos."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de actividad en el .bib local de la materia.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Validar que toda clave citada exista en el .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir entre nodos no equivalentes solo reglas abstractas y reutilizables.",
    "No propagar supuestos como reglas definitivas.",
    "Preservar reglas utiles previas aunque se reubiquen de categoria.",
    "Aplicar compresion lossless por union y deduplicacion.",
    "Mantener bitacora de incidencias de parseo para prevenir regresiones."
  ],
  "open_questions": [
    "Confirmar consigna local de la proxima actividad para ajustar tipo de producto.",
    "Confirmar criterio editorial final sobre uso de publico/publico con acento en nombres visibles. [supuesto]",
    "Confirmar reparacion de tokens $(@{...}.Slug) en README y programa analitico.",
    "Confirmar si existe rubrica local que exija secciones adicionales."
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
        "Usar contexto curricular del destino verificado localmente.",
        "No mezclar metadatos curriculares de materias distintas."
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
      "Convertir planeacion semanal en entregables juridicos claros y verificables.",
      "Asegurar coherencia entre consigna, argumento y evidencia.",
      "Sostener identidad UnADM con calidad tecnica y academica."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales sin redundancia.",
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
          "justification": "La forma del entregable depende del producto solicitado."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica valida requiere respaldo comprobable."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Consistencia cita-bibliografia",
          "kind": "depends_on",
          "justification": "La propagacion segura exige estructura valida y trazable."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura argumentativa juridica",
          "kind": "develops",
          "justification": "La identidad define tono, formato y criterios de presentacion."
        }
      ],
      "evidence": [
        "README local del destino.",
        "Programa analitico local del destino.",
        "Archivo .bib local del destino.",
        "Regla heredada estable: bloquear salida no parseable antes de propagar."
      ]
    },
    "reinforcement_log": [
      "Ciclo 43: deduplicacion completa de reglas repetidas en origen y destino.",
      "Ciclo 43: transferencia transversal limitada a abstracciones estables reutilizables.",
      "Ciclo 43: se mantiene veto a propagacion de contenido tematico especifico del origen.",
      "Ciclo 43: se refuerzan gates de parseo JSON, supuestos y consistencia cita-.bib."
    ]
  }
}