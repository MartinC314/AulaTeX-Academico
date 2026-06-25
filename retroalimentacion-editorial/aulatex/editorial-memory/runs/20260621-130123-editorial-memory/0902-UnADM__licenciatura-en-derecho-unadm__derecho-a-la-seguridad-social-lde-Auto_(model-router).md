```json
{
  "summary": [
    "Se sincroniza memoria editorial transversal desde actividad no equivalente hacia materia.",
    "Se preserva identidad UnADM y patrón editorial común por ejes.",
    "Se refuerza cerebro editorial mínimo del destino sin mezclar contenido temático.",
    "La compresión aplicada es union-dedupe, sin regresión.",
    "Se mantiene alerta institucional por antecedentes de salidas no parseables."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino; no heredar datos del origen.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Conservar trazabilidad de reglas heredadas provisionales.",
    "No sobrescribir reglas válidas previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Usar README de la materia como canon estructural.",
    "Alinear toda entrega a ejes reutilizables: problema, marco, análisis, evidencia y conclusión.",
    "Separar explícitamente marco normativo, análisis propio y cierre.",
    "Mantener consistencia entre reporte, presentación y programa analítico."
  ],
  "activity_rules": [
    "Definir problema jurídico y objetivo antes del desarrollo.",
    "Sustentar afirmaciones con normas, doctrina o evidencia verificable.",
    "Incluir postura argumentada propia; evitar solo resumen.",
    "Cerrar con conclusión jurídica transferible a la práctica."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Normalizar manualmente salidas no estructuradas antes de reutilizar.",
    "Validar estructura mínima completa antes de propagar recursivamente.",
    "Confirmar respaldo o marca de [supuesto] en toda afirmación relevante.",
    "Verificar correspondencia entre citas en texto y archivo .bib local."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener idioma español y metadatos institucionales consistentes.",
    "Evitar comandos no estándar sin justificación técnica.",
    "Corregir rutas, nombres corruptos o tokens antes de compilar."
  ],
  "bibliography_rules": [
    "Usar el .bib local de la materia como fuente central.",
    "Agregar solo referencias verificables y específicas de la actividad.",
    "No inventar fuentes; marcar faltantes como pendientes.",
    "Mantener metadatos mínimos completos en cada entrada."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Evitar transferir redacción literal o contenido temático del origen.",
    "Propagar reglas de identidad, estructura y calidad a laterales compatibles.",
    "Mantener bandera de riesgo por antecedentes de ciclo 1."
  ],
  "open_questions": [
    "Confirmar norma de citación específica requerida por la materia [supuesto].",
    "Definir figura docente cuando el dato oficial esté disponible.",
    "Verificar si existen rúbricas específicas por actividad [supuesto]."
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
        "Semestre 2, bloque 1, obligatoria, 8 créditos."
      ]
    },
    "essence": [
      "Patrón editorial común por ejes.",
      "Identidad institucional estable.",
      "Control de calidad y trazabilidad.",
      "Transferencia profesional del conocimiento jurídico."
    ],
    "reason_for_being": [
      "Garantizar coherencia editorial transversal en la suite académica.",
      "Permitir reutilización segura de reglas sin mezclar contenidos.",
      "Asegurar productos jurídicos verificables y profesionales."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explícito de [supuesto].",
      "Separación visible entre marco, análisis y conclusión.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo.",
      "Analizar con postura propia.",
      "Concluir con implicación jurídica práctica."
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
        }
      ],
      "evidence": [
        "README y programa analítico del destino.",
        "Archivo .bib local del destino.",
        "Reglas institucionales heredadas de AulaTeX."
      ]
    },
    "reinforcement_log": [
      "Se reforzó patrón editorial común sin mezclar contenidos.",
      "Se preservó identidad UnADM y control de calidad.",
      "Se consolidó cerebro editorial mínimo del destino."
    ]
  }
}
```