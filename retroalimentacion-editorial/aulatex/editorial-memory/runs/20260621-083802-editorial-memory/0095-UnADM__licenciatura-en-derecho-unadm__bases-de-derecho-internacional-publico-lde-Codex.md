{
  "summary": [
    "Se refuerza sincronización transversal con reglas estables y deduplicadas entre nodos no equivalentes.",
    "Se conserva identidad UnADM del destino sin mezclar metadatos curriculares del origen.",
    "Se consolidan ejes reutilizables: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se mantiene política estricta de normalización JSON antes de propagación recursiva.",
    "Se agregan mejoras verificables de saneamiento editorial detectadas en README y programa analítico del destino."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local: Bases de derecho internacional publico.",
    "Mantener contexto curricular del destino: semestre 4, bloque 1, obligatoria, 8 créditos.",
    "No mezclar metadatos curriculares de Filosofía del Derecho con la materia destino.",
    "Usar la carpeta de materia como entrada canónica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como procedencia provisional, no como identidad."
  ],
  "structure_rules": [
    "Iniciar cada entrega con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Estructurar en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear forma de entrega al producto solicitado en planeación semanal.",
    "Distinguir reporte, presentación y producto visual según consigna.",
    "Cerrar con conclusión jurídica transferible a práctica profesional."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Distinguir hechos, normas, argumentos y criterio propio.",
    "Evitar extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes."
  ],
  "quality_gates": [
    "Bloquear propagación si salida no es JSON parseable.",
    "Validar estructura mínima completa antes de reutilizar memoria.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Verificar correspondencia entre consigna, programa analítico y producto entregable."
  ],
  "latex_rules": [
    "Reutilizar plantilla .tex local sin romper identidad institucional.",
    "Usar codificación y acentos correctos en .tex y .bib.",
    "Mantener clase article con spanish, letterpaper y oneside según base local.",
    "Compilar sin errores críticos, referencias rotas ni entornos abiertos.",
    "Corregir caracteres anómalos en rutas y nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Verificar cierre de tabular en reporte base antes de nuevas actividades.",
    "No alterar estructura de portada sin instrucción editorial local."
  ],
  "bibliography_rules": [
    "Registrar fuentes de actividad en bases-de-derecho-internacional-publico.bib.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Mantener claves BibTeX estables para evitar roturas de compilación.",
    "Conservar entradas institucionales base: unadmSitioWeb y unadmMallaDerecho2024."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas transversales estables y verificadas.",
    "Aplicar compresión lossless por unión y deduplicación, sin recorte semántico.",
    "No propagar contenido temático específico de Filosofía del Derecho a Derecho Internacional Público.",
    "Preservar reglas útiles previas aunque cambie su categoría.",
    "Mantener trazabilidad de incidencias históricas de salida no estructurada.",
    "Ejecutar normalización manual cuando reaparezcan ciclos con salida no parseable."
  ],
  "open_questions": [
    "Confirmar corrección definitiva de nombres con caracteres anómalos en README.",
    "Confirmar resolución definitiva de token Slug sin expandir en README y programa analítico.",
    "Confirmar nombre editorial final con o sin acento para publico/público en todo el nodo.",
    "Confirmar reparación completa del entorno tabular truncado en reporte base.",
    "Supuesto: no existe aún rúbrica local detallada por actividad; confirmar."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Normalización estructurada obligatoria antes de propagación."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Destino verificado: semestre 4, bloque 1, obligatoria, 8 créditos.",
        "No mezclar contexto curricular entre materias."
      ]
    },
    "essence": [
      "Consigna guía la estructura.",
      "Evidencia sostiene la conclusión.",
      "Análisis propio distingue calidad jurídica.",
      "Formato institucional asegura consistencia transversal."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos verificables y útiles para práctica jurídica.",
      "Sostener un cerebro editorial persistente, estable y reusable entre actividades y materias."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Secciones funcionales sin redundancia.",
      "Supuestos siempre etiquetados.",
      "Cierre con criterio jurídico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> norma/doctrina -> análisis -> conclusión.",
      "Afirmación -> evidencia -> interpretación -> postura propia.",
      "Consigna -> desarrollo alineado -> verificación final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Consigna de actividad",
        "Estructura argumentativa jurídica",
        "Evidencia verificable",
        "Análisis propio",
        "Conclusión transferible",
        "Normalización JSON",
        "Consistencia cita-bibliografía"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Consigna de actividad",
          "target": "Estructura argumentativa jurídica",
          "kind": "depends_on",
          "justification": "La consigna define tipo de producto y profundidad."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "Sin respaldo no hay cierre jurídico sólido."
        },
        {
          "source": "Normalización JSON",
          "target": "Consistencia cita-bibliografía",
          "kind": "develops",
          "justification": "La estructura válida permite auditar calidad técnica y académica."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura argumentativa jurídica",
          "kind": "supports",
          "justification": "El marco institucional fija tono, forma y trazabilidad."
        }
      ],
      "evidence": [
        "README destino: ubicación curricular y pauta editorial.",
        "Programa analítico destino: propósito y ejes de trabajo.",
        "Archivo .bib destino: fuentes institucionales base verificables.",
        "Histórico de calidad: incidencia de salidas no parseables y regla de bloqueo."
      ]
    },
    "reinforcement_log": [
      "Ciclo 95: deduplicación completa sin pérdida de reglas útiles previas.",
      "Ciclo 95: transferencia conservadora solo de abstracciones estables.",
      "Ciclo 95: refuerzo de gates JSON, supuestos explícitos y consistencia cita-bib.",
      "Ciclo 95: se mantienen vacíos locales abiertos sin inventar contenido."
    ]
  }
}