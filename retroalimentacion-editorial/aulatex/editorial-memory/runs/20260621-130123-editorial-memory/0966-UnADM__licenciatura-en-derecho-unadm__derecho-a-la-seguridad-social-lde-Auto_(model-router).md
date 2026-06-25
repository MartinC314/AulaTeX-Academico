```json
{
  "summary": [
    "Se sincroniza ADN editorial estable desde una actividad de Filosofía del Derecho hacia la materia Derecho a la Seguridad Social.",
    "La transferencia es transversal: se comparten abstracciones editoriales, no contenido temático.",
    "Se preserva identidad UnADM, estructura por ejes y control de calidad institucional.",
    "La compresión aplicada es lossless por unión y deduplicación, sin regresión.",
    "El destino consolida un cerebro editorial mínimo, ampliable por contexto local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino; no heredar datos del origen.",
    "Marcar como [supuesto] cualquier dato no verificable localmente.",
    "Conservar trazabilidad de reglas heredadas cuando sean provisionales.",
    "No sobrescribir reglas válidas previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Usar README de la materia como canon estructural local.",
    "Alinear todo producto a cinco ejes: problema, conceptos/norma, evidencia, análisis propio y conclusión.",
    "Separar explícitamente marco normativo/doctrinal y postura del estudiante.",
    "Cerrar siempre con conclusión jurídica transferible a la práctica.",
    "Normalizar estructura antes de propagar reglas aguas abajo."
  ],
  "activity_rules": [
    "Definir objetivo y problema jurídico al inicio de cada actividad.",
    "Sustentar afirmaciones con normas, doctrina o datos verificables.",
    "Incluir postura argumentada; evitar entregas solo descriptivas.",
    "Ajustar formato y alcance al producto solicitado en la planeación.",
    "Relacionar el análisis con el campo específico de seguridad social."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de reutilizar reglas.",
    "Confirmar respaldo o marca [supuesto] en toda afirmación relevante.",
    "Verificar correspondencia entre consigna, desarrollo y conclusión.",
    "Asegurar compresión por unión-dedupe, nunca por recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener idioma español, metadatos institucionales y consistencia de clase.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Corregir rutas o nombres corruptos antes de compilar.",
    "Evitar comandos no estándar sin justificación editorial."
  ],
  "bibliography_rules": [
    "Usar el archivo .bib local de la materia como fuente central.",
    "Priorizar fuentes institucionales y normativas vigentes.",
    "No inventar referencias; marcar faltantes como pendientes.",
    "Verificar correspondencia entre citas en texto y BibTeX.",
    "Distinguir bibliografía base de bibliografía específica de actividad."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Evitar transferir redacción literal o contenido temático del origen.",
    "Propagar recursivamente solo tras validación de JSON y estructura.",
    "Mantener bandera de riesgo por antecedentes de salidas no parseables.",
    "No reducir especificidad local del destino."
  ],
  "open_questions": [
    "Confirmar norma de citación requerida por la materia [supuesto].",
    "Definir rúbricas específicas de actividades futuras.",
    "Confirmar productos exactos solicitados en planeaciones locales.",
    "Verificar si se requieren criterios jurisprudenciales obligatorios.",
    "Confirmar vigencia de cualquier fuente provisional heredada [supuesto]."
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
        "Respeto a semestre y bloque oficiales del destino",
        "Uso del programa analítico como guía editorial"
      ]
    },
    "essence": [
      "Problema jurídico delimitado",
      "Marco normativo verificable",
      "Evidencia pertinente",
      "Análisis propio argumentado",
      "Conclusión jurídica transferible"
    ],
    "reason_for_being": [
      "Convertir consignas en productos jurídicos claros y verificables.",
      "Garantizar coherencia editorial entre actividades y materias.",
      "Facilitar transferencia profesional del aprendizaje."
    ],
    "style_markers": [
      "Frases cortas y accionables",
      "Separación visible entre marco, análisis y cierre",
      "Marcado explícito de [supuesto]",
      "Cierre con utilidad práctica"
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo",
      "Exponer fundamento normativo",
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
          "justification": "Conserva reglas útiles sin pérdida ni duplicados."
        }
      ],
      "evidence": [
        "README y programa analítico del destino definen estructura y propósito.",
        "Reglas institucionales UnADM heredadas y verificadas.",
        "Archivo .bib local confirma base normativa vigente."
      ]
    },
    "reinforcement_log": [
      "Se refuerza patrón editorial común sin mezclar contenido temático.",
      "Se preserva identidad UnADM y control de calidad.",
      "Se consolida cerebro editorial mínimo y reconstruible."
    ]
  }
}
```