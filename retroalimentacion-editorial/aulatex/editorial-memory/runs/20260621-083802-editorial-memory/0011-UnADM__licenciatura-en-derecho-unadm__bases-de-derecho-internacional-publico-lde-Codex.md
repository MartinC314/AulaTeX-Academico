{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre actividad de origen y materia destino.",
    "Se preservan reglas utiles previas del destino y se deduplican formulaciones repetidas.",
    "Se transfieren solo abstracciones estables: identidad, estructura reusable, calidad y metodo argumentativo.",
    "Se mantiene bloqueo de propagacion ante salidas no parseables y normalizacion obligatoria.",
    "Se evita traslado de contenido tematico especifico de Filosofia del Derecho al nodo de Derecho Internacional Publico.",
    "Supuesto: no hay consigna local de actividad especifica en este ciclo para refinar reglas por tipo de producto."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local de la materia en todos los entregables.",
    "Alinear entregables a Licenciatura en Derecho, semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Usar LDE-S4B1 como codigo de curso en metadatos.",
    "Tratar Codex y GPT-Pro solo como trazabilidad provisional, no como identidad del entregable.",
    "Marcar como supuesto cualquier dato no visible en la consigna local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear la estructura al producto solicitado por la planeacion semanal.",
    "Distinguir reporte, presentacion y producto visual segun consigna.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Conservar separacion entre README, programa analitico, .bib y plantillas .tex."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, argumentos, normas y criterio propio.",
    "Integrar conceptos, normas, doctrina o datos pertinentes al caso.",
    "Evitar extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre consigna, programa analitico y producto generado.",
    "Mantener auditoria de parseo y cambios por ciclo para evitar regresiones."
  ],
  "latex_rules": [
    "Reutilizar plantillas .tex locales sin romper identidad institucional.",
    "Mantener compatibilidad con article, spanish, letterpaper y oneside.",
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Compilar sin errores criticos, sin referencias rotas y con entornos cerrados.",
    "Corregir caracteres anómalos en nombres de archivo y rutas antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico."
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
    "Propagar solo reglas generales verificadas en nodos no equivalentes.",
    "Aplicar compresion lossless por union y deduplicacion, sin recorte semantico.",
    "No propagar supuestos como reglas definitivas.",
    "Preservar reglas utiles previas aunque cambien de categoria.",
    "Registrar incidencias historicas de salida no estructurada para control de calidad.",
    "Priorizar identidad, gates de calidad y grafo conceptual en sincronizacion transversal.",
    "Si falta contexto local, mantener cerebro minimo y abrir preguntas."
  ],
  "open_questions": [
    "Confirmar criterio editorial final sobre publico sin acento vs publico con acento.",
    "Confirmar y corregir nombres con caracteres anómalos en README.",
    "Confirmar resolucion definitiva de tokens $(@{...}.Slug) en README y programa analitico.",
    "Confirmar si existe rubrica local por actividad para ajustar profundidad argumentativa.",
    "Supuesto: falta consigna puntual de actividad destino en este ciclo.",
    "Confirmar si se normaliza el entorno tabular truncado del reporte base antes del siguiente ciclo."
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
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 4, bloque 1, obligatoria, 8 creditos.",
        "Asignatura: Bases de derecho internacional publico."
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
      "Convertir planeacion semanal en entregables juridicos claros, verificables y utiles.",
      "Garantizar consistencia institucional y trazabilidad editorial entre nodos."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales sin redundancia.",
      "Supuestos etiquetados.",
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
          "justification": "La consigna define forma, alcance y tipo de producto."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "Sin respaldo documental la conclusion pierde validez academica y juridica."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Sincronizacion transversal",
          "kind": "depends_on",
          "justification": "La propagacion recursiva requiere memoria estructurada y parseable."
        },
        {
          "source": "Consistencia cita-bibliografia",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita afirmaciones sin fuente y referencias inexistentes."
        }
      ],
      "evidence": [
        "README de materia destino.",
        "Programa analitico de materia destino.",
        "Archivo .bib local con claves institucionales.",
        "Historial de incidencias por salidas no parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 11: deduplicacion completa de reglas repetidas sin perdida semantica.",
      "Ciclo 11: refuerzo de gates de parseo JSON y normalizacion previa a propagacion.",
      "Ciclo 11: transferencia transversal solo de abstracciones estables, sin contenido tematico de Filosofia del Derecho.",
      "Ciclo 11: mantenimiento de identidad curricular local de Derecho Internacional Publico."
    ]
  }
}