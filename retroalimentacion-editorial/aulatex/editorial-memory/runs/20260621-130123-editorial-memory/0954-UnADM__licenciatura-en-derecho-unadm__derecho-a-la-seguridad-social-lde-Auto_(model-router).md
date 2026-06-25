```json
{
  "summary": [
    "Se consolida cerebro editorial mínimo para la materia Derecho a la Seguridad Social con identidad UnADM.",
    "Se sincronizan abstracciones editoriales estables desde un nodo de actividad no equivalente.",
    "Se refuerza patrón transversal: problema, fundamento, evidencia, análisis propio y conclusión jurídica.",
    "Se preservan reglas locales del destino sin mezclar contenido temático de Filosofía del Derecho.",
    "La compresión aplicada es union-dedupe sin pérdida ni regresión."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redacción.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 créditos.",
    "Usar la carpeta de la materia como punto de entrada canónico.",
    "Marcar como [supuesto] todo dato no visible en la consigna o fuentes locales.",
    "Conservar trazabilidad cuando una regla heredada sea provisional.",
    "No sobrescribir reglas válidas previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar el README de la materia como canon estructural.",
    "Alinear cada producto a cinco ejes: problema, conceptos/norma, producto, análisis y conclusión.",
    "Usar estructura mínima: portada, desarrollo por ejes, conclusión y referencias.",
    "Mantener consistencia entre reporte, presentación y programa analítico.",
    "Definir objetivo puntual antes del desarrollo."
  ],
  "activity_rules": [
    "Delimitar explícitamente el problema jurídico o social.",
    "Vincular el desarrollo con marco constitucional, legal y doctrinal pertinente.",
    "Incluir postura académica propia argumentada.",
    "Distinguir hechos, conceptos, normas y opinión.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Ajustar formato y alcance al producto solicitado en la planeación semanal."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Normalizar manualmente salidas no estructuradas antes de reutilizar.",
    "Validar estructura mínima completa antes de propagar.",
    "Confirmar que toda afirmación tenga respaldo verificable o marca [supuesto].",
    "Verificar correspondencia entre consigna, desarrollo y conclusión.",
    "Confirmar que la compresión aplicada sea union-dedupe y no recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener metadatos institucionales y de curso consistentes.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Evitar comandos no estándar sin justificación técnica.",
    "Corregir rutas, nombres corruptos o tokens sin expandir antes de compilar."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como archivo bibliográfico central.",
    "Priorizar fuentes institucionales y normativas verificables.",
    "Agregar solo referencias específicas de actividad con metadatos completos.",
    "No inventar fuentes; marcar faltantes como pendientes.",
    "Verificar correspondencia entre citas en texto y entradas BibTeX."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Propagar arriba y laterales únicamente tras validar JSON y estructura.",
    "Reutilizar reglas generales de identidad, calidad y estructura.",
    "Evitar transferir redacción literal o contenido temático específico.",
    "Mantener bandera de riesgo por antecedentes de salidas no parseables."
  ],
  "open_questions": [
    "Confirmar norma de citación requerida para la materia [supuesto].",
    "Confirmar consignas y productos específicos de cada actividad.",
    "Definir nombre oficial de figura docente cuando esté disponible.",
    "Verificar vigencia de reglas provisionales heredadas de otros contextos."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico",
        "Claro",
        "Jurídicamente preciso",
        "Argumentativo con criterio propio"
      ],
      "institutional": [
        "Alineación explícita con UnADM",
        "Integridad académica con citas verificables",
        "Normalización estructurada obligatoria antes de propagar"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Materia: Derecho a la Seguridad Social",
        "Semestre 2, bloque 1, obligatoria, 8 créditos",
        "Uso del programa analítico como guía editorial"
      ]
    },
    "essence": [
      "Identidad institucional UnADM",
      "Problema jurídico delimitado",
      "Marco normativo verificable",
      "Evidencia pertinente",
      "Análisis propio",
      "Conclusión jurídica transferible"
    ],
    "reason_for_being": [
      "Convertir consignas en productos jurídicos verificables.",
      "Garantizar coherencia, fundamento y utilidad profesional.",
      "Permitir reutilización segura de reglas editoriales entre materias."
    ],
    "style_markers": [
      "Frases cortas y accionables",
      "Separación clara entre marco, análisis y cierre",
      "Marcado explícito de [supuesto]",
      "Cierre con implicación práctica"
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo",
      "Exponer marco normativo y doctrinal",
      "Contrastar evidencia relevante",
      "Fijar postura propia sustentada",
      "Concluir con impacto jurídico práctico"
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema jurídico",
        "Marco normativo",
        "Evidencia verificable",
        "Análisis propio",
        "Conclusión jurídica transferible",
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
          "justification": "El análisis requiere una cuestión jurídica delimitada."
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
        },
        {
          "source": "Compresión union-dedupe",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Conserva reglas útiles sin pérdida ni duplicación."
        }
      ],
      "evidence": [
        "README y programa analítico definen estructura y propósito.",
        "Archivo .bib local confirma base normativa e institucional.",
        "Reglas de calidad y normalización preservadas del origen."
      ]
    },
    "reinforcement_log": [
      "Se refuerza patrón editorial común transversal.",
      "Se preservan reglas locales del destino.",
      "Se evita contaminación temática entre materias.",
      "Se mantiene control institucional y técnico de propagación."
    ]
  }
}
```