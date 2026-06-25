```json
{
  "summary": [
    "Se consolida sincronización transversal entre actividad de Filosofía del Derecho y materia Derecho a la Seguridad Social.",
    "Se preservan reglas institucionales UnADM, estructura por ejes y control de calidad JSON.",
    "Se transfieren solo abstracciones editoriales estables, sin contenido temático ajeno.",
    "Se refuerza patrón común: problema, fundamento, evidencia, análisis propio y conclusión jurídica.",
    "La compresión aplicada es lossless por unión y deduplicación, sin regresión."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar datos curriculares oficiales del destino; marcar discrepancias como [supuesto].",
    "Conservar trazabilidad de reglas heredadas cuando sean provisionales.",
    "No sobrescribir reglas válidas previas; unir y deduplicar.",
    "Usar carpeta de la materia como punto de entrada canónico."
  ],
  "structure_rules": [
    "Alinear cada producto a cinco ejes: problema, conceptos/norma, producto, análisis y conclusión.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Separar claramente marco normativo/doctrinal, análisis propio y cierre.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Tomar README y programa analítico como canon estructural local."
  ],
  "activity_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Incluir postura académica propia, no solo descripción.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Distinguir hechos, normas, doctrina y opinión.",
    "Marcar como [supuesto] todo dato no visible en la consigna."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Normalizar manualmente respuestas no estructuradas antes de reutilizar.",
    "Verificar coherencia entre objetivo, desarrollo y conclusión.",
    "Confirmar que toda afirmación relevante tenga respaldo o marca de [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib local."
  ],
  "latex_rules": [
    "Mantener plantilla base de la materia; personalizar solo campos variables.",
    "Evitar comandos o clases no estándar sin justificación editorial.",
    "Usar codificación correcta en español en .tex y .bib.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Corregir rutas o nombres corruptos antes de compilar."
  ],
  "bibliography_rules": [
    "Usar el archivo .bib local de la materia como fuente central.",
    "Priorizar fuentes institucionales y normativas verificables.",
    "No inventar referencias; marcar faltantes como pendientes.",
    "Conservar metadatos mínimos completos.",
    "Distinguir bibliografía base de bibliografía específica de actividad."
  ],
  "propagation_hints": [
    "Propagar solo reglas generales validadas a nodos laterales compatibles.",
    "Evitar transferir redacción literal o contenido temático específico.",
    "Mantener bandera de riesgo por antecedentes de salida no parseable.",
    "Aplicar siempre compresión union-dedupe sin pérdida.",
    "No mezclar contenido de Filosofía con Seguridad Social."
  ],
  "open_questions": [
    "Confirmar rúbrica específica de actividades en la materia destino.",
    "Definir norma de citación exigida si difiere de la institucional.",
    "Confirmar nombre canónico de plantillas de Actividad 1 en la materia.",
    "Verificar vigencia de fuentes provisionales heredadas [supuesto]."
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
        "Normalización estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho a la Seguridad Social.",
        "Uso de datos curriculares oficiales del destino."
      ]
    },
    "essence": [
      "Patrón editorial común reutilizable entre materias.",
      "Centralidad del problema jurídico.",
      "Fundamento normativo verificable.",
      "Análisis propio del estudiante.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Servir como cerebro editorial persistente para productos jurídicos UnADM.",
      "Garantizar coherencia, calidad y reutilización segura entre nodos.",
      "Evitar regresiones y pérdidas de reglas útiles."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Separación visible entre marco, análisis y cierre.",
      "Etiquetado explícito de [supuesto].",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo y doctrinal.",
      "Contrastar evidencia.",
      "Fijar postura propia sustentada.",
      "Concluir con implicación jurídica práctica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Problema jurídico",
        "Marco normativo",
        "Evidencia verificable",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "Identidad institucional UnADM",
        "JSON parseable",
        "Compresión union-dedupe"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024",
        "cpeum2026",
        "lss2026",
        "lissste2026"
      ],
      "relations": [
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis requiere una pregunta jurídica delimitada."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión válida depende de fundamento legal verificable."
        },
        {
          "source": "JSON parseable",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura válida no hay reutilización segura."
        }
      ],
      "evidence": [
        "README y programa analítico del destino.",
        "Archivo .bib local con fuentes normativas vigentes.",
        "Reglas heredadas consolidadas sin duplicación."
      ]
    },
    "reinforcement_log": [
      "Se refuerza identidad UnADM sin mezclar contenidos temáticos.",
      "Se preserva patrón editorial común entre nodos transversales.",
      "Se mantiene control estricto de calidad y propagación."
    ]
  }
}
```