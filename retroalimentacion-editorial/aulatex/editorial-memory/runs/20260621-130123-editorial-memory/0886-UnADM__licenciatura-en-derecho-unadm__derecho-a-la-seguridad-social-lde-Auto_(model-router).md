```json
{
  "summary": [
    "Se sincronizan abstracciones editoriales estables desde actividad de Filosofía del Derecho hacia la materia Derecho a la Seguridad Social.",
    "Se preserva identidad UnADM, estructura por ejes y control de calidad sin transferir contenido temático ajeno.",
    "La compresión aplica unión y deduplicación sin regresión ni pérdida.",
    "Se refuerza el patrón editorial transversal: problema, fundamento, evidencia, análisis propio y conclusión jurídica.",
    "Se consolida cerebro editorial mínimo del destino con foco institucional y verificable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino; marcar divergencias como [supuesto].",
    "No sobrescribir reglas válidas previas; solo unir y deduplicar.",
    "Conservar trazabilidad de reglas heredadas provisionales.",
    "Usar carpeta de la materia como punto de entrada canónico."
  ],
  "structure_rules": [
    "Alinear toda entrega a cinco ejes: problema, conceptos/norma, producto, análisis y conclusión.",
    "Tomar README y programa analítico de la materia como canon estructural local.",
    "Separar claramente marco normativo/doctrinal y análisis propio.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Normalizar nombres de archivos antes de usarlos como canon."
  ],
  "activity_rules": [
    "Definir objetivo y problema jurídico desde el inicio.",
    "Sustentar afirmaciones con normas, doctrina o datos verificables.",
    "Incluir postura argumentada propia; evitar entregas solo descriptivas.",
    "Ajustar formato y alcance al producto solicitado en la planeación.",
    "Marcar explícitamente como [supuesto] lo no verificable en la consigna."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de reutilizar.",
    "Confirmar respaldo verificable o marca de [supuesto] en afirmaciones relevantes.",
    "Verificar coherencia entre objetivo, desarrollo y conclusión.",
    "Asegurar compresión lossless por unión-dedupe."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener metadatos institucionales consistentes en todos los .tex.",
    "Evitar cambios de clase o formato sin justificación técnica.",
    "Corregir rutas, nombres corruptos o tokens sin expandir antes de compilar.",
    "Compilar sin errores críticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Usar el archivo .bib local de la materia como fuente central.",
    "No inventar referencias; agregar solo fuentes realmente consultables.",
    "Conservar metadatos mínimos completos en cada entrada.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Verificar correspondencia entre citas en texto y entradas BibTeX."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Evitar transferir redacción literal o contenido temático del origen.",
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Mantener bandera de riesgo por antecedentes de salidas no parseables.",
    "No reducir especificidad local del destino."
  ],
  "open_questions": [
    "Confirmar norma de citación requerida para la materia [supuesto].",
    "Verificar vigencia de fuentes provisionales heredadas [supuesto].",
    "Confirmar productos exactos solicitados en planeaciones específicas.",
    "Definir figura docente en plantillas cuando exista dato oficial."
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
        "Uso de datos curriculares oficiales del destino"
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
      "Convertir consignas en productos jurídicos verificables y profesionales.",
      "Garantizar coherencia editorial transversal entre materias.",
      "Preservar calidad, trazabilidad y reutilización segura del conocimiento."
    ],
    "style_markers": [
      "Frases cortas y accionables",
      "Separación visible entre marco y análisis",
      "Etiquetado explícito de [supuesto]",
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
        "Compresión unión-dedupe"
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
        },
        {
          "source": "Compresión unión-dedupe",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Conserva reglas útiles sin pérdida ni duplicado."
        }
      ],
      "evidence": [
        "README y programa analítico del destino definen estructura y propósito.",
        "Archivo .bib local confirma base normativa e institucional.",
        "Reglas heredadas validadas en ciclos previos sin regresión."
      ]
    },
    "reinforcement_log": [
      "Se refuerza patrón editorial común sin mezclar contenidos temáticos.",
      "Se preservan reglas locales del destino con identidad UnADM.",
      "Se consolida cerebro editorial mínimo reconstruible y verificable."
    ]
  }
}
```