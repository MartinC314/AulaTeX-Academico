{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre actividad origen y materia destino.",
    "Se preservan reglas utiles previas y se deduplican sin perdida.",
    "Se transfieren solo abstracciones estables: identidad, estructura, calidad y metodo argumentativo.",
    "Se evita trasladar contenido tematico especifico de Filosofia del Derecho al destino.",
    "Se refuerza normalizacion JSON obligatoria antes de propagacion recursiva.",
    "Se mantiene contexto curricular local del destino como fuente canonica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local de la materia en todos los entregables.",
    "Usar carpeta de materia como entrada canonica.",
    "Alinear entregables al contexto curricular verificado del destino.",
    "No mezclar metadatos curriculares entre materias.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como procedencia provisional, no como identidad."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear la estructura al producto solicitado por la planeacion semanal.",
    "Distinguir reporte, presentacion y producto visual segun consigna.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Conservar separacion operativa entre README, programa analitico, .tex y .bib."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, normas, argumentos y criterio propio.",
    "Evitar extrapolar fuentes de semanas o materias no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes.",
    "Validar que cada actividad corresponda al producto solicitado."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre consigna, programa analitico y entregable.",
    "Mantener auditoria de parseo JSON por ciclo de propagacion."
  ],
  "latex_rules": [
    "Reutilizar plantillas .tex locales del destino como base.",
    "Mantener compatibilidad con clase article, spanish, letterpaper y oneside.",
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir en README y programa analitico antes de referenciar archivos.",
    "Corregir caracteres anomales en rutas o nombres de archivo antes de compilar."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas de actividad en el .bib local del destino.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Validar que todas las claves citadas existan en el .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo reglas generales estables en saltos transversales.",
    "Evitar traslado literal de redaccion entre nodos no equivalentes.",
    "No propagar supuestos como reglas definitivas.",
    "Preservar reglas utiles previas sin regresion.",
    "Aplicar compresion lossless por union y deduplicacion.",
    "Si falta contexto local, mantener cerebro minimo y abrir preguntas."
  ],
  "open_questions": [
    "[Supuesto] Falta consigna textual de actividades concretas del destino; confirmar productos por semana.",
    "Confirmar criterio editorial final sobre uso de publico/publico con acento en nombres visibles.",
    "Confirmar correccion de tokens $(@{...}.Slug) en README y programa analitico.",
    "Confirmar cierre correcto de entornos LaTeX en plantilla de reporte local.",
    "Confirmar si existe rubrica de evaluacion especifica para ajustar profundidad argumentativa."
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
        "Usar solo contexto curricular verificado en el destino.",
        "No mezclar contexto curricular del origen con el destino."
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
      "Convertir planeacion semanal en entregables con rigor juridico y trazabilidad.",
      "Asegurar calidad editorial reproducible entre actividades y formatos.",
      "Mantener coherencia institucional y tecnica en toda propagacion."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales sin redundancia.",
      "Supuestos etiquetados.",
      "Cierre aplicable a practica juridica."
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
          "justification": "El tipo de producto define la forma del desarrollo."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica valida requiere respaldo documental."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Consistencia cita-bibliografia",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay control de calidad automatizable."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura argumentativa juridica",
          "kind": "develops",
          "justification": "La identidad fija tono, formato y criterios de presentacion."
        }
      ],
      "evidence": [
        "README del destino: punto de entrada canonico y pauta editorial.",
        "Programa analitico del destino: proposito y ejes de trabajo.",
        "Reglas heredadas validadas: bloqueo por JSON no parseable y normalizacion previa."
      ]
    },
    "reinforcement_log": [
      "Se reforzo gate de parseo JSON como condicion de propagacion recursiva.",
      "Se consolido patron argumentativo transversal sin arrastrar contenido tematico del origen.",
      "Se mantuvo estrategia conservadora con deduplicacion lossless.",
      "Se preservaron reglas historicas utiles de calidad y trazabilidad."
    ]
  }
}