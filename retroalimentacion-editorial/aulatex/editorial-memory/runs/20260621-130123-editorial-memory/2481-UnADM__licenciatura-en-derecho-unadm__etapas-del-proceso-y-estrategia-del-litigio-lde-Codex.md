{
  "summary": [
    "Memoria de materia consolidada con identidad UnADM y enfoque jurídico aplicado.",
    "Se mantiene compresión lossless por unión y deduplicación sin regresión.",
    "Se refuerza transferencia transversal por abstracciones estables, no por redacción literal.",
    "Se preservan cinco ejes editoriales: problema, conceptos, producto, análisis propio y conclusión jurídica.",
    "Se mantiene validación de JSON parseable y normalización estructurada antes de propagar."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Conservar trazabilidad del origen editorial en cada consolidación.",
    "Marcar como [supuesto] todo dato no visible en consigna o documentos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales y no como autoridad académica."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en bloques: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear la estructura al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Aplicar los cinco ejes editoriales como columna estructural reutilizable."
  ],
  "activity_rules": [
    "Verificar instrucción específica de cada actividad antes de redactar.",
    "Rubricar cada entrega contra los cinco ejes del programa analítico.",
    "Sustentar afirmaciones con evidencia verificable y cita explícita.",
    "Exigir postura argumentativa propia, no solo resumen descriptivo.",
    "Agregar fuentes específicas de actividad al .bib local antes de la versión final.",
    "Evitar reutilizar reglas de otras materias sin validar pertinencia jurídica local."
  ],
  "quality_gates": [
    "Bloquear propagación si la memoria no es JSON parseable.",
    "Revisar estructura mínima completa antes de fusionar o propagar.",
    "Validar unión-dedupe sin eliminar reglas útiles previas.",
    "Confirmar que toda afirmación factual tenga fuente o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Normalizar manualmente insumos no estructurados heredados de ciclos previos."
  ],
  "latex_rules": [
    "Usar plantilla .tex local de la materia como base.",
    "Conservar macros institucionales: documenttitle, coursename, coursecode, universityname.",
    "Mantener compatibilidad en español y letterpaper según plantilla.",
    "No eliminar campos de portada; completar según actividad.",
    "Usar reporte-etapas-del-proceso-y-estrategia-del-litigio.tex para reportes.",
    "Usar presentacion-etapas-del-proceso-y-estrategia-del-litigio.tex si existe. [supuesto]",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir nombres de archivo con caracteres corruptos antes de compilar."
  ],
  "bibliography_rules": [
    "Usar etapas-del-proceso-y-estrategia-del-litigio.bib como repositorio canónico local.",
    "Conservar fuentes institucionales base: unadmSitioWeb y unadmMallaDerecho2024.",
    "No inventar referencias; registrar solo fuentes consultables y verificables.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Incluir metadatos mínimos: autor, título, año y fuente o URL.",
    "Incluir fecha de consulta en fuentes web o institucionales dinámicas."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas estables de identidad, estructura y calidad.",
    "Priorizar gates de parseo JSON y no regresión en nodos vecinos.",
    "Propagar los cinco ejes editoriales como patrón transversal en Derecho.",
    "No propagar metadatos específicos de actividad origen a materia destino.",
    "Mantener marca de provisionalidad para herencias no verificadas.",
    "Aplicar estrategia progresiva y conservadora: agregar solo mejoras verificables."
  ],
  "open_questions": [
    "Confirmar si documentauthor debe ser fijo de plantilla o variable por estudiante. [supuesto]",
    "Confirmar estilo de citación requerido por asignatura (APA, Chicago, ISO 690 u otro). [supuesto]",
    "Confirmar si coursecode LDE-S5B2 es definitivo institucionalmente. [supuesto]",
    "Confirmar existencia operativa de plantilla de presentación en todos los entornos. [supuesto]",
    "Confirmar checklist mínimo por tipo de producto: reporte, presentación y material visual."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Jurídicamente preciso.",
        "Claro y verificable.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Carpeta de asignatura como entrada canónica.",
        "Fuentes provisionales separadas de autoridad académica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 5, bloque 2, obligatoria, 8 créditos.",
        "Asignatura: Etapas del proceso y estrategia del litigio."
      ]
    },
    "essence": [
      "Identidad UnADM sostenida en productos académicos.",
      "Cinco ejes editoriales como núcleo reusable.",
      "Normalización estructurada antes de propagación.",
      "Compresión por unión-dedupe sin pérdida.",
      "Conclusión jurídica transferible como cierre obligatorio."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en entregables jurídicos claros, fundados y aplicables.",
      "Asegurar evidencia verificable y análisis propio en cada actividad.",
      "Mantener continuidad editorial transversal sin pérdida de reglas útiles."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Bloques argumentativos explícitos.",
      "Citas trazables.",
      "Cierre con implicación práctica jurídica.",
      "Marcado explícito de [supuesto] cuando falte evidencia local."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis propio -> conclusión jurídica.",
      "Afirmación -> evidencia -> interpretación -> implicación práctica.",
      "Objetivo puntual al inicio y verificación de coherencia al cierre."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Cinco ejes editoriales",
        "JSON parseable",
        "Normalización estructurada",
        "Unión-dedupe sin regresión",
        "Conclusión jurídica transferible",
        "Trazabilidad de fuentes"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "JSON parseable",
          "target": "Normalización estructurada",
          "kind": "depends_on",
          "justification": "La propagación segura requiere estructura válida."
        },
        {
          "source": "Normalización estructurada",
          "target": "Unión-dedupe sin regresión",
          "kind": "supports",
          "justification": "Permite fusionar memoria sin pérdida de reglas útiles."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Conclusión jurídica transferible",
          "kind": "develops",
          "justification": "El eje final exige cierre aplicable a práctica profesional."
        },
        {
          "source": "Identidad UnADM",
          "target": "Trazabilidad de fuentes",
          "kind": "supports",
          "justification": "La integridad académica institucional exige verificabilidad."
        }
      ],
      "evidence": [
        "README de la materia: identidad, ubicación curricular y pauta editorial.",
        "Programa analítico: propósito y cinco ejes de trabajo.",
        "Bib local: fuentes institucionales base verificables.",
        "Plantilla .tex local: macros institucionales y metadatos de curso."
      ]
    },
    "reinforcement_log": [
      "Ciclo 5: se preservan reglas válidas previas y se deduplican variantes.",
      "Ciclo 5: se añade regla transversal de transferencia por abstracciones estables.",
      "Ciclo 5: se refuerza resolución de tokens Slug sin expandir en README/programa.",
      "Ciclo 5: se mantiene separación entre fuentes provisionales y autoridad académica.",
      "Ciclo 5: sin eliminación de reglas útiles heredadas."
    ]
  }
}