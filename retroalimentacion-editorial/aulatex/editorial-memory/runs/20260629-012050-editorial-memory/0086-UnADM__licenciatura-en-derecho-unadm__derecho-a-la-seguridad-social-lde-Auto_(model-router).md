```json
{
  "summary": [
    "Se consolida sincronización transversal entre actividad de Filosofía del Derecho y materia Derecho a la Seguridad Social.",
    "Se transfieren solo abstracciones editoriales estables: identidad UnADM, estructura por ejes y control de calidad.",
    "No se mezcla contenido temático; se refuerza un patrón editorial jurídico común.",
    "La compresión aplicada es union-dedupe sin pérdida ni regresión.",
    "El destino queda con un cerebro editorial mínimo, consistente y reconstruible."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 créditos.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Conservar trazabilidad de reglas heredadas cuando sean provisionales.",
    "No sobrescribir reglas válidas previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README de la materia como canon estructural local.",
    "Organizar entregas en cinco ejes: problema, conceptos/norma, producto, análisis y conclusión.",
    "Separar marco normativo, análisis propio y cierre.",
    "Alinear cada producto a la planeación semanal correspondiente.",
    "Usar estructura mínima: portada, desarrollo por ejes, conclusión y referencias."
  ],
  "activity_rules": [
    "Definir desde el inicio el problema jurídico o social.",
    "Vincular el desarrollo con normas, doctrina y evidencia verificable.",
    "Incluir postura académica propia, no solo descripción.",
    "Distinguir hechos, conceptos, normas y opinión.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Normalizar manualmente respuestas no estructuradas antes de reutilizar.",
    "Verificar coherencia entre objetivo, desarrollo y conclusión.",
    "Confirmar que toda afirmación tenga respaldo o marca de [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib local."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener idioma español y metadatos institucionales consistentes.",
    "Evitar comandos no estándar sin justificación técnica.",
    "Corregir rutas o nombres corruptos antes de compilar.",
    "Compilar sin errores críticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Usar el archivo .bib local de la materia como fuente central.",
    "Priorizar fuentes institucionales y normativas verificables.",
    "No inventar referencias; marcar faltantes como pendientes.",
    "Conservar metadatos mínimos completos en cada entrada.",
    "Verificar que cada cita tenga su entrada BibTeX correspondiente."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables a nodos laterales.",
    "Evitar transferir redacción literal o contenido temático.",
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Mantener bandera de riesgo por antecedentes de salida no parseable.",
    "Preservar reglas locales del destino sin regresión."
  ],
  "open_questions": [
    "Confirmar norma de citación requerida por la materia [supuesto].",
    "Definir figura docente en plantillas cuando exista dato oficial.",
    "Confirmar consignas específicas de cada actividad de seguridad social.",
    "Verificar vigencia de fuentes normativas antes de entrega final."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico",
        "Claro y jurídicamente preciso",
        "Argumentativo con criterio propio"
      ],
      "institutional": [
        "Alineación explícita con UnADM",
        "Integridad académica con citas verificables",
        "Normalización estructurada obligatoria"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Materia: Derecho a la Seguridad Social",
        "Semestre 2, bloque 1, obligatoria, 8 créditos"
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
      "Transformar consignas en productos jurídicos claros, fundados y útiles.",
      "Garantizar coherencia editorial transversal entre materias UnADM.",
      "Servir como cerebro persistente reutilizable sin mezclar contenidos."
    ],
    "style_markers": [
      "Frases cortas y accionables",
      "Separación visible entre marco, análisis y cierre",
      "Marcado explícito de [supuesto]",
      "Cierre con utilidad profesional"
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo",
      "Exponer marco normativo",
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
      "citations": [
        "cpeum2026",
        "lss2026",
        "lissste2026",
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis requiere una cuestión jurídica claramente delimitada."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La validez de la conclusión depende del fundamento legal."
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
        "Archivo .bib local con normas vigentes",
        "Reglas institucionales UnADM consolidadas"
      ]
    },
    "reinforcement_log": [
      "Se refuerza patrón editorial común entre materias jurídicas.",
      "Se preserva identidad UnADM sin mezclar contenidos temáticos.",
      "Se consolida control de calidad y propagación segura en ciclo 2."
    ]
  }
}
```