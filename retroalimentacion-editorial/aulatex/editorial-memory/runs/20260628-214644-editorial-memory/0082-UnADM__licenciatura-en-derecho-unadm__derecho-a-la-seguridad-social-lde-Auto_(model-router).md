```json
{
  "summary": [
    "Se sincronizan abstracciones editoriales estables desde actividad de Filosofía del Derecho hacia la materia Derecho a la Seguridad Social.",
    "La transferencia es transversal, progresiva y conservadora; no se mezcla contenido temático.",
    "Se refuerza patrón editorial común UnADM: problema, fundamento, evidencia, análisis propio y conclusión jurídica.",
    "Se preservan alertas institucionales por salidas no parseables y se mantiene normalización obligatoria.",
    "Se consolida cerebro editorial mínimo reconstruible para la materia destino."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino; no heredar datos del origen.",
    "Marcar como [supuesto] toda inferencia no visible en consigna o fuentes locales.",
    "No sobrescribir reglas válidas previas; unir y deduplicar sin regresión.",
    "Conservar trazabilidad de reglas heredadas cuando sean provisionales."
  ],
  "structure_rules": [
    "Alinear cada producto a cinco ejes reutilizables: problema, marco normativo/doctrinal, evidencia, análisis propio y conclusión.",
    "Tomar README y programa analítico del destino como canon local.",
    "Separar explícitamente marco, análisis y cierre.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Definir objetivo y problema jurídico desde el inicio.",
    "Sustentar afirmaciones con fuentes verificables o marcar [supuesto].",
    "Incluir postura argumentada propia; evitar entregas solo descriptivas.",
    "Ajustar formato y alcance al producto solicitado por la planeación semanal."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Normalizar manualmente salidas no estructuradas antes de reutilizar.",
    "Validar estructura mínima completa antes de propagar recursivamente.",
    "Confirmar correspondencia entre objetivos, desarrollo y conclusión.",
    "Verificar consistencia entre citas en texto y archivo .bib local."
  ],
  "latex_rules": [
    "Mantener plantilla base de la materia; personalizar solo campos variables.",
    "Conservar metadatos institucionales y del curso en todos los .tex.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Corregir rutas o nombres corruptos antes de compilar."
  ],
  "bibliography_rules": [
    "Usar el archivo .bib local del destino como fuente central.",
    "No inventar referencias; agregar solo fuentes consultables y verificables.",
    "Conservar metadatos mínimos completos en cada entrada.",
    "Distinguir bibliografía base de bibliografía específica de actividad."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Evitar transferir redacción literal o contenido temático del origen.",
    "Reutilizar reglas de identidad, estructura y calidad ya validadas.",
    "Mantener bandera de riesgo por antecedentes de salida no parseable en ciclo 1."
  ],
  "open_questions": [
    "Confirmar rúbrica específica de evaluación para la materia destino.",
    "Definir norma de citación requerida si difiere de la institucional.",
    "Confirmar productos exactos solicitados en cada actividad del destino."
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
        "Normalización estructurada obligatoria antes de propagar"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Materia: Derecho a la Seguridad Social",
        "Semestre 2, bloque 1, obligatoria, 8 créditos"
      ]
    },
    "essence": [
      "Patrón editorial común UnADM",
      "Problema jurídico delimitado",
      "Marco normativo verificable",
      "Evidencia pertinente",
      "Análisis propio",
      "Conclusión jurídica transferible"
    ],
    "reason_for_being": [
      "Garantizar coherencia transversal entre materias sin perder especificidad local.",
      "Convertir consignas en productos jurídicos verificables y profesionales."
    ],
    "style_markers": [
      "Frases cortas y accionables",
      "Etiquetado explícito de [supuesto]",
      "Separación visible entre marco, análisis y cierre",
      "Cierre con utilidad profesional"
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo",
      "Exponer marco normativo",
      "Contrastar evidencia",
      "Fijar postura propia sustentada",
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
        "README y programa analítico del destino como canon editorial.",
        "Reglas institucionales UnADM heredadas y validadas."
      ]
    },
    "reinforcement_log": [
      "Se refuerza patrón editorial común sin transferir contenido temático.",
      "Se preservan reglas útiles previas mediante unión y deduplicación.",
      "Se mantiene control institucional de calidad y propagación."
    ]
  }
}
```