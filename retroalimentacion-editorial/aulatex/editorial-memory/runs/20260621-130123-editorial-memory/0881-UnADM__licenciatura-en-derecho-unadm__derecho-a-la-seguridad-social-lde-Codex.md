{
  "summary": [
    "Se sincroniza memoria transversal con enfoque conservador y sin regresión.",
    "Se preserva identidad UnADM y canon local de Derecho a la Seguridad Social.",
    "Se refuerza patrón reusable: problema, fundamento, evidencia, análisis propio y conclusión jurídica.",
    "Se mantiene compresión lossless por unión y deduplicación.",
    "Se conserva alerta institucional: no propagar salidas no parseables sin normalización."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 créditos.",
    "Usar la carpeta de materia como entrada canónica editorial.",
    "No sobrescribir reglas válidas previas; solo unir y deduplicar.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local."
  ],
  "structure_rules": [
    "Tomar README de la materia como canon de estructura.",
    "Alinear cada entrega a ejes: problema, conceptos/norma, producto, análisis y conclusión.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar desarrollo en conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Alinear formato final al producto pedido por planeación semanal.",
    "Mantener consistencia entre reporte, presentación y programa analítico."
  ],
  "activity_rules": [
    "Delimitar al inicio el problema jurídico o social de la actividad.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Cerrar con conclusión jurídica transferible a práctica profesional.",
    "Relacionar el contenido con seguridad social cuando corresponda."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizar.",
    "Validar estructura mínima completa antes de propagación recursiva.",
    "Confirmar que toda afirmación relevante tenga respaldo o marca [supuesto].",
    "Verificar correspondencia entre producto entregado y consigna vigente.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificación y acentos correctos en español en .tex y .bib.",
    "Evitar comandos no estándar sin justificación técnica.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Normalizar nombres y rutas de archivos antes de compilar.",
    "Resolver marcadores o tokens sin expandir en README y programa analítico."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliográfica central.",
    "Priorizar fuentes institucionales UnADM y normas jurídicas vigentes verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Registrar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de materia y bibliografía específica de actividad.",
    "Verificar que cada cita LaTeX tenga su entrada BibTeX correspondiente."
  ],
  "propagation_hints": [
    "Propagar lateral y hacia arriba solo reglas estables ya validadas.",
    "Transferir abstracciones editoriales, no contenido temático literal de Filosofía del Derecho.",
    "Conservar reglas locales del destino sin mezclar bibliografía temática ajena.",
    "Mantener bandera de riesgo por antecedentes de salida no parseable en ciclo 1.",
    "Aplicar unión-dedupe sin pérdida en cada ciclo."
  ],
  "open_questions": [
    "Confirmar norma de citación exigida por la materia (APA, ISO, institucional o jurídica mexicana) [supuesto].",
    "Confirmar si el código local LDE-S2B1 es oficial en todos los entregables [supuesto].",
    "Verificar si persiste alguna regla provisional heredada desde nodos no jurídicos [supuesto].",
    "Confirmar rúbricas por actividad para ajustar profundidad argumentativa [supuesto]."
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
      "Producto jurídico verificable con estructura estable.",
      "Fundamento normativo y evidencia trazable.",
      "Análisis propio con cierre profesional transferible."
    ],
    "reason_for_being": [
      "Convertir consignas en entregables jurídicos claros, verificables y útiles para práctica profesional.",
      "Asegurar continuidad editorial entre nodos sin perder contexto local."
    ],
    "style_markers": [
      "Frases directas y accionables.",
      "Marcado explícito de [supuesto].",
      "Separación visible entre marco, análisis y conclusión.",
      "Trazabilidad de decisiones editoriales."
    ],
    "argumentative_patterns": [
      "Encuadrar problema y objetivo.",
      "Presentar marco normativo y doctrinal pertinente.",
      "Contrastar evidencia verificable.",
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
          "justification": "Sin delimitación del problema no hay argumentación sólida."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión válida requiere sustento legal verificable."
        },
        {
          "source": "JSON parseable",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "La reutilización segura exige estructura válida."
        },
        {
          "source": "Compresión unión-dedupe",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Preserva reglas útiles sin duplicidad ni recorte."
        }
      ],
      "evidence": [
        "README de la materia define estructura canónica local.",
        "Programa analítico define propósito y ejes jurídicos.",
        "Archivo .bib local confirma base normativa e institucional.",
        "Regla institucional vigente: normalizar antes de propagar."
      ]
    },
    "reinforcement_log": [
      "Se transfirieron solo abstracciones editoriales estables entre nodos no equivalentes.",
      "Se evitó mover contenido temático específico de Filosofía del Derecho al destino.",
      "Se reforzaron gates de calidad, trazabilidad y validación bibliográfica.",
      "Se mantuvo estrategia progresiva y conservadora sin eliminar reglas útiles previas."
    ]
  }
}