```json
{
  "summary": [
    "Se consolida sincronización transversal desde actividad hacia materia con enfoque conservador.",
    "Se transfieren solo abstracciones editoriales estables y reutilizables.",
    "Se refuerza patrón común UnADM: problema, fundamento, evidencia, análisis propio y conclusión.",
    "Se preservan reglas locales del destino sin mezclar contenido temático del origen.",
    "La compresión aplicada es union-dedupe sin pérdida ni regresión."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en todo producto.",
    "Usar datos curriculares oficiales del destino; no heredar los del origen.",
    "Marcar como [supuesto] cualquier regla heredada no verificable localmente.",
    "No sobrescribir reglas válidas previas; solo unir y deduplicar.",
    "Conservar trazabilidad de reglas transversales heredadas."
  ],
  "structure_rules": [
    "Alinear toda entrega a ejes reutilizables: problema, marco, evidencia, análisis y conclusión.",
    "Usar README y programa analítico del destino como canon estructural.",
    "Separar explícitamente marco normativo y análisis propio.",
    "Cerrar siempre con conclusión jurídica transferible.",
    "Normalizar estructura antes de propagar recursivamente."
  ],
  "activity_rules": [
    "Definir objetivo y problema jurídico desde el inicio.",
    "Sustentar afirmaciones con fuentes verificables o marcar [supuesto].",
    "Incluir postura académica propia; evitar solo descripción.",
    "Ajustar formato y alcance al producto solicitado localmente.",
    "Relacionar el contenido con la materia destino cuando aplique."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Confirmar estructura mínima completa antes de reutilizar.",
    "Verificar coherencia entre problema, desarrollo y conclusión.",
    "Validar correspondencia entre citas en texto y .bib local.",
    "Confirmar compresión lossless por union-dedupe."
  ],
  "latex_rules": [
    "Mantener plantilla base del destino y personalizar solo campos variables.",
    "Conservar metadatos institucionales consistentes.",
    "Evitar comandos no estándar sin justificación técnica.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Corregir rutas o nombres corruptos antes de compilar."
  ],
  "bibliography_rules": [
    "Usar el archivo .bib local del destino como fuente central.",
    "Agregar solo referencias realmente consultables.",
    "No inventar fuentes; marcar pendientes explícitamente.",
    "Conservar metadatos mínimos completos.",
    "Validar que toda cita tenga entrada BibTeX."
  ],
  "propagation_hints": [
    "Propagar solo reglas generales y estables entre nodos no equivalentes.",
    "Evitar transferir redacción literal o contenido temático específico.",
    "Priorizar identidad, estructura reusable y gates de calidad.",
    "Mantener bandera de riesgo por antecedentes de salidas no parseables.",
    "Aplicar normalización manual si se detecta salida no estructurada."
  ],
  "open_questions": [
    "Confirmar consignas específicas de actividades del destino.",
    "Definir norma de citación jurídica requerida por la materia [supuesto].",
    "Confirmar nombres canónicos de archivos de actividad.",
    "Verificar vigencia de fuentes provisionales heredadas [supuesto]."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico",
        "Claro",
        "Jurídicamente preciso",
        "Argumentativo"
      ],
      "institutional": [
        "Alineación explícita con UnADM",
        "Integridad académica",
        "Normalización estructurada obligatoria"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Respeto a semestre y bloque del destino",
        "Uso del programa analítico como guía"
      ]
    },
    "essence": [
      "Problema jurídico delimitado",
      "Marco normativo verificable",
      "Evidencia pertinente",
      "Análisis propio",
      "Conclusión jurídica transferible"
    ],
    "reason_for_being": [
      "Servir como cerebro editorial persistente y reutilizable.",
      "Garantizar coherencia institucional entre materias.",
      "Asegurar calidad y verificabilidad en productos académicos."
    ],
    "style_markers": [
      "Frases cortas y accionables",
      "Separación visible entre marco y análisis",
      "Marcado explícito de [supuesto]",
      "Cierre con utilidad profesional"
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo",
      "Exponer fundamento normativo",
      "Contrastar evidencia",
      "Fijar postura propia",
      "Concluir con implicación práctica"
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
      "citations": [],
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
          "justification": "La conclusión válida depende de fundamento legal."
        },
        {
          "source": "JSON parseable",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura válida no hay reutilización segura."
        }
      ],
      "evidence": [
        "README y programa analítico del destino",
        "Reglas institucionales UnADM heredadas",
        "Gates de calidad consolidados"
      ]
    },
    "reinforcement_log": [
      "Se refuerza patrón editorial común sin mezclar contenidos.",
      "Se preservan reglas locales del destino.",
      "Se consolida sincronización transversal conservadora."
    ]
  }
}
```