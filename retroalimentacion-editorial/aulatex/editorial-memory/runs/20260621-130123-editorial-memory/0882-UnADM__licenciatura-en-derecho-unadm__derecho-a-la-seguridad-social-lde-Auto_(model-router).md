```json
{
  "summary": [
    "Se consolida sincronización transversal desde una actividad teórica hacia una materia sustantiva sin mezclar contenido temático.",
    "Se preserva identidad institucional UnADM, estructura por ejes y control de calidad como reglas estables.",
    "La transferencia prioriza abstracciones editoriales reutilizables y refuerza un cerebro editorial mínimo del destino.",
    "Se mantiene compresión lossless por unión y deduplicación, sin regresión."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino; marcar cualquier desviación como [supuesto].",
    "Conservar trazabilidad de reglas heredadas cuando sean provisionales.",
    "No sobrescribir reglas válidas previas; solo unir y deduplicar.",
    "Usar la carpeta de la materia como punto de entrada canónico."
  ],
  "structure_rules": [
    "Alinear toda entrega a cinco ejes: problema, marco normativo/doctrinal, evidencia, análisis propio y conclusión.",
    "Tomar README y programa analítico de la materia como canon estructural.",
    "Separar claramente marco, análisis y cierre.",
    "Normalizar nombres de archivos y secciones antes de usarlos como referencia."
  ],
  "activity_rules": [
    "Definir objetivo y problema jurídico desde el inicio.",
    "Sustentar afirmaciones con normas, doctrina o datos verificables.",
    "Incluir postura argumentada del estudiante; evitar solo descripción.",
    "Cerrar con conclusión jurídica aplicable a la práctica.",
    "Ajustar formato y alcance al producto solicitado en la planeación."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Confirmar estructura mínima completa antes de reutilizar.",
    "Verificar que toda afirmación tenga respaldo o marca de [supuesto].",
    "Validar coherencia entre objetivo, desarrollo y conclusión.",
    "Confirmar correspondencia entre citas en texto y archivo .bib local."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia; personalizar solo campos variables.",
    "Mantener metadatos institucionales consistentes en todos los .tex.",
    "Evitar comandos no estándar sin justificación técnica.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Corregir rutas o nombres corruptos antes de compilar."
  ],
  "bibliography_rules": [
    "Usar el archivo .bib local de la materia como fuente central.",
    "Agregar solo referencias realmente consultables y verificables.",
    "No inventar fuentes; marcar faltantes como pendientes.",
    "Conservar metadatos mínimos completos en cada entrada.",
    "Verificar que cada cita tenga su entrada BibTeX correspondiente."
  ],
  "propagation_hints": [
    "Propagar solo reglas editoriales estables entre nodos no equivalentes.",
    "Evitar transferir redacción literal o contenido temático específico.",
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Mantener bandera de riesgo por antecedentes de salidas no parseables en ciclo 1."
  ],
  "open_questions": [
    "Confirmar norma de citación requerida para la materia destino [supuesto].",
    "Verificar vigencia de cualquier fuente provisional heredada [supuesto].",
    "Confirmar productos específicos solicitados en las primeras planeaciones.",
    "Definir campos pendientes de plantilla cuando existan datos oficiales."
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
      "Problema jurídico delimitado.",
      "Marco normativo verificable.",
      "Evidencia pertinente.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir consignas en productos jurídicos verificables.",
      "Garantizar coherencia editorial transversal entre materias.",
      "Servir como cerebro editorial persistente y reutilizable."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Marcado explícito de [supuesto].",
      "Separación visible entre marco, análisis y cierre.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo y doctrinal.",
      "Contrastar evidencia relevante.",
      "Fijar postura propia sustentada.",
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
        "README y programa analítico del destino como canon estructural.",
        "Archivo .bib local confirma base normativa e institucional.",
        "Reglas de calidad heredadas y validadas en ciclo 1."
      ]
    },
    "reinforcement_log": [
      "Se refuerza patrón editorial común sin mezclar contenidos temáticos.",
      "Se preservan reglas útiles previas sin regresión.",
      "Se establece cerebro editorial mínimo reconstruible para el destino."
    ]
  }
}
```