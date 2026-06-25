{
  "summary": [
    "Se consolida sincronizacion transversal con transferencia solo de abstracciones editoriales estables.",
    "Se preserva identidad UnADM y contexto curricular local del destino sin mezclar metadatos del origen.",
    "Se refuerzan ejes reutilizables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene estrategia conservadora: no transferir contenido tematico especifico de Filosofia del Derecho.",
    "Se conserva regla critica de normalizacion estructurada y bloqueo por JSON no parseable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local de la materia en todos los entregables.",
    "Usar codigo local LDE-S4B1 en metadatos de reporte y presentacion.",
    "Usar la carpeta de materia como entrada canonica.",
    "No mezclar contexto curricular del origen con el destino.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar Codex y GPT-Pro solo como procedencia provisional."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear la estructura al producto solicitado en la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Distinguir reporte, presentacion y producto visual segun consigna."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante y evitar resumen meramente descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, normas, argumentos y criterio propio.",
    "No extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna activa."
  ],
  "latex_rules": [
    "Reutilizar plantillas .tex locales sin romper identidad institucional.",
    "Mantener compatibilidad con article, spanish, letterpaper y oneside.",
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo con caracteres anómalos antes de referenciar."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas de actividad en el .bib local de la materia.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Validar que toda clave citada exista en el .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas, generales y no duplicadas.",
    "Aplicar compresion lossless por union-dedupe sin recorte semantico.",
    "Preservar reglas utiles previas y evitar regresiones.",
    "No propagar supuestos como reglas definitivas.",
    "Mantener trazabilidad de incidencias historicas de parseo."
  ],
  "open_questions": [
    "Confirmar consigna local de la siguiente actividad para ajustar tipo de producto.",
    "Confirmar si el nombre editorial final usara publico o público. [supuesto]",
    "Confirmar correccion definitiva de tokens $(@{...}.Slug) en README y programa analitico.",
    "Confirmar reparacion completa del entorno tabular truncado en el reporte base.",
    "Confirmar si existe rubrica local que exija formato de conclusion juridica especifico."
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
        "Destino: semestre 4, bloque 1, obligatoria, 8 creditos.",
        "Asignatura: Bases de derecho internacional publico.",
        "Codigo local: LDE-S4B1."
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
      "Convertir planeacion semanal en entregables juridicos claros, sustentados y utiles para la practica.",
      "Garantizar consistencia institucional, argumentativa y bibliografica en cada actividad."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y no redundantes.",
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
          "justification": "El formato y profundidad dependen del producto pedido."
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
          "justification": "La propagacion segura exige estructura parseable y control de referencias."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura argumentativa juridica",
          "kind": "develops",
          "justification": "La identidad fija tono, metadatos y forma academica estable."
        }
      ],
      "evidence": [
        "README local del destino.",
        "Programa analitico local del destino.",
        "Archivo .bib local con claves institucionales.",
        "Reglas heredadas de calidad sobre parseo JSON y normalizacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 14: se transfieren reglas transversales estables desde actividad origen a materia destino.",
      "Ciclo 14: se conserva politica de no mezclar contexto curricular entre materias.",
      "Ciclo 14: se refuerza gate de bloqueo por JSON no parseable.",
      "Ciclo 14: se agregan acciones de saneamiento por tokens Slug sin expandir.",
      "Ciclo 14: no se trasladan contenidos tematicos especificos del origen por no equivalencia de nodo."
    ]
  }
}