```json
{
  "summary": [
    "Se consolida cerebro editorial mínimo del destino con identidad UnADM y control institucional.",
    "Se sincronizan abstracciones editoriales estables desde actividad origen sin mezclar contenido temático.",
    "Se refuerza patrón transversal: problema, fundamento, evidencia, análisis propio y conclusión jurídica.",
    "Se mantiene compresión lossless por unión-dedupe y alerta por salidas no parseables previas.",
    "La materia queda como punto de entrada canónico con estructura, calidad y grafo conceptual activos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redacción.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 créditos.",
    "Usar carpeta de la materia como punto de entrada canónico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Conservar trazabilidad de reglas heredadas cuando sean provisionales.",
    "No sobrescribir reglas válidas previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README de la materia como canon estructural local.",
    "Alinear cada entrega a cinco ejes: problema, conceptos/norma, producto, análisis y conclusión.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Separar marco normativo/doctrinal del análisis propio.",
    "Cerrar con conclusión jurídica transferible a la práctica.",
    "Mantener consistencia entre reporte, presentación y programa analítico."
  ],
  "activity_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Delimitar explícitamente el problema jurídico.",
    "Sustentar afirmaciones con fuentes verificables o marcar [supuesto].",
    "Incluir postura académica propia; evitar entregas solo descriptivas.",
    "Ajustar formato y alcance al producto solicitado en la planeación.",
    "Relacionar el contenido con el campo de seguridad social cuando corresponda."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Normalizar manualmente salidas no estructuradas antes de reutilizar.",
    "Validar estructura mínima completa antes de propagar recursivamente.",
    "Confirmar coherencia entre objetivo, desarrollo y conclusión.",
    "Comprobar correspondencia entre citas en texto y archivo .bib.",
    "Evitar regresiones respecto de reglas útiles previas."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia; personalizar solo campos variables.",
    "Mantener metadatos institucionales y de curso consistentes.",
    "Usar estructura mínima: portada, desarrollo por ejes, conclusión y referencias.",
    "Evitar comandos o clases no estándar sin justificación técnica.",
    "Corregir rutas, nombres corruptos o tokens sin expandir antes de compilar.",
    "Compilar sin errores críticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Usar el archivo .bib local de la materia como fuente central.",
    "Priorizar fuentes institucionales y normativas verificables.",
    "No inventar referencias; marcar faltantes como pendientes.",
    "Conservar metadatos mínimos completos en cada entrada.",
    "Validar que cada cita en LaTeX tenga entrada BibTeX correspondiente."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables a nodos laterales no equivalentes.",
    "Propagar arriba y laterales solo tras validar JSON y estructura.",
    "Mantener bandera de riesgo por antecedente de salida no parseable en ciclo 1.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Aplicar siempre compresión union-dedupe sin pérdida ni regresión."
  ],
  "open_questions": [
    "Confirmar norma de citación requerida para la materia [supuesto].",
    "Definir figura docente en plantilla cuando exista dato oficial.",
    "Verificar vigencia de cualquier fuente provisional heredada [supuesto].",
    "Confirmar consignas y rúbricas específicas de actividades iniciales."
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
      "Problema jurídico delimitado",
      "Marco normativo verificable",
      "Evidencia pertinente",
      "Análisis propio",
      "Conclusión jurídica transferible",
      "Identidad institucional UnADM"
    ],
    "reason_for_being": [
      "Convertir consignas en productos jurídicos verificables y profesionales.",
      "Asegurar coherencia editorial, calidad y reutilización segura.",
      "Permitir sincronización transversal entre materias no equivalentes."
    ],
    "style_markers": [
      "Frases cortas y accionables",
      "Etiquetado explícito de [supuesto]",
      "Separación visible entre marco, análisis y cierre",
      "Cierre con utilidad profesional"
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo",
      "Exponer marco normativo y doctrinal",
      "Contrastar evidencia relevante",
      "Fijar postura propia sustentada",
      "Concluir con implicación jurídica práctica"
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
        "README y programa analítico del destino definen estructura y propósito.",
        "Archivo .bib local confirma base normativa e institucional.",
        "Reglas heredadas refuerzan control de calidad y propagación segura."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin eliminar contenido útil.",
      "Se reforzó patrón editorial común sin transferir redacción literal.",
      "Se preservaron alertas institucionales y controles de calidad."
    ]
  }
}
```