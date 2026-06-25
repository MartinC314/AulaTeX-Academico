```json
{
  "summary": [
    "Se sincroniza ADN editorial transversal desde actividad de Filosofía del Derecho hacia la materia Derecho a la Seguridad Social.",
    "Se preservan reglas válidas del destino y se integran abstracciones estables reutilizables.",
    "Se refuerza el patrón editorial común: problema, fundamento, evidencia, análisis propio y conclusión jurídica.",
    "La consolidación es lossless por unión y deduplicación, sin regresión.",
    "Se mantiene alerta institucional por antecedentes de salidas no parseables."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 créditos.",
    "Conservar trazabilidad de reglas heredadas marcadas como [supuesto].",
    "No sobrescribir reglas válidas previas; solo unir y deduplicar.",
    "Usar carpeta de la materia como punto de entrada canónico."
  ],
  "structure_rules": [
    "Alinear toda entrega a cinco ejes: problema, conceptos/norma, producto, análisis y conclusión.",
    "Tomar README y programa analítico como canon estructural local.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener consistencia entre reporte, presentación y otros productos."
  ],
  "activity_rules": [
    "Definir objetivo puntual y problema jurídico desde el inicio.",
    "Sustentar afirmaciones con fuentes verificables o marcar [supuesto].",
    "Incluir postura académica propia; evitar textos solo descriptivos.",
    "Vincular análisis con el campo de la seguridad social cuando corresponda.",
    "Ajustar formato y alcance al producto solicitado en la planeación."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Normalizar manualmente salidas no estructuradas antes de reutilizar.",
    "Validar estructura mínima completa antes de propagación recursiva.",
    "Confirmar coherencia entre objetivo, desarrollo y conclusión.",
    "Verificar correspondencia entre citas en texto y archivo .bib local."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificación correcta en español y compilación sin errores.",
    "Evitar comandos o clases no estándar sin justificación.",
    "Normalizar rutas y nombres de archivo antes de compilar.",
    "No copiar bloques LaTeX completos entre nodos; solo patrones."
  ],
  "bibliography_rules": [
    "Usar el archivo .bib local de la materia como fuente central.",
    "Priorizar fuentes institucionales y normativas verificables.",
    "No inventar referencias; marcar faltantes como pendientes.",
    "Mantener metadatos mínimos completos en cada entrada.",
    "Validar vigencia normativa antes de la entrega final."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Evitar transferir contenido temático literal de Filosofía del Derecho.",
    "Propagar reglas generales de identidad, estructura y calidad a laterales compatibles.",
    "Mantener bandera de riesgo por antecedentes de ciclo 1.",
    "Aplicar compresión union-dedupe sin pérdida ni regresión."
  ],
  "open_questions": [
    "Confirmar norma de citación específica exigida por la materia [supuesto].",
    "Definir rúbricas de evaluación locales para ajustar profundidad.",
    "Verificar actividades específicas que requieran jurisprudencia obligatoria.",
    "Confirmar si existen consignas con formato distinto a reporte o presentación."
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
        "Semestre 2, bloque 1, obligatoria, 8 créditos"
      ]
    },
    "essence": [
      "Problema jurídico delimitado",
      "Marco normativo verificable",
      "Evidencia pertinente",
      "Análisis propio sustentado",
      "Conclusión jurídica transferible"
    ],
    "reason_for_being": [
      "Funcionar como cerebro editorial persistente de la materia.",
      "Garantizar coherencia institucional y calidad académica.",
      "Permitir reutilización segura de reglas editoriales entre materias."
    ],
    "style_markers": [
      "Frases cortas y accionables",
      "Separación visible entre marco, análisis y cierre",
      "Marcado explícito de [supuesto]",
      "Cierre con utilidad profesional"
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo",
      "Exponer marco constitucional, legal o doctrinal",
      "Contrastar evidencia relevante",
      "Fijar postura propia argumentada",
      "Concluir con implicaciones prácticas"
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
          "justification": "El análisis requiere una pregunta jurídica claramente delimitada."
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
        "README y programa analítico de la materia destino",
        "Archivo .bib local con normativa vigente",
        "Reglas institucionales UnADM heredadas y validadas"
      ]
    },
    "reinforcement_log": [
      "Se refuerza patrón editorial común sin mezclar contenido temático.",
      "Se preservan reglas locales del destino.",
      "Se consolida sincronización transversal estable en ciclo 16."
    ]
  }
}
```