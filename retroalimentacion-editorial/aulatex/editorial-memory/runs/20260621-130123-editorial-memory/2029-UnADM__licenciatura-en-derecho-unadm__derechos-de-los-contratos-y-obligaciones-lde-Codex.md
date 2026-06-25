{
  "summary": [
    "Se conserva base institucional UnADM y normalización estructurada obligatoria.",
    "Se refuerza sincronización transversal con abstracciones estables no literales.",
    "Se mantiene modelo de cinco ejes: problema, conceptos, producto, análisis propio y conclusión jurídica.",
    "Se preserva control técnico de JSON parseable antes de persistir o propagar.",
    "Se consolida resolución de placeholders tipo $(@{...}.Slug) en README y programa analítico."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares confirmados de la materia: semestre 4, bloque 1, obligatoria, 8 créditos.",
    "Conservar enfoque disciplinar en contratos y obligaciones.",
    "Usar código de curso LDE-S4B1 cuando la plantilla lo requiera.",
    "Mantener carpeta de materia como entrada canónica.",
    "Marcar como [supuesto] todo dato no visible en la consigna local.",
    "Tratar herencias no verificadas de Codex o GPT-Pro como provisionales."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Alinear el entregable al producto solicitado en la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener trazabilidad entre objetivo, evidencia, argumento y conclusión."
  ],
  "activity_rules": [
    "Adaptar cada actividad al formato solicitado: reporte, presentación u otro producto.",
    "Explicitar postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y cierre.",
    "Distinguir bibliografía base de fuentes específicas por actividad.",
    "No trasladar contenido de otras materias sin adecuación contractual."
  ],
  "quality_gates": [
    "Bloquear persistencia y propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "No degradar reglas útiles previas durante unión-deduplicación."
  ],
  "latex_rules": [
    "Usar plantilla LaTeX local de la materia según consigna.",
    "Mantener metadatos completos: curso, autor, universidad, ubicación y subtítulo de actividad.",
    "Actualizar documenttitle y documentsubtitle al producto real antes de compilar.",
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver placeholders tipo $(@{...}.Slug) en nombres de archivo antes de compilar."
  ],
  "bibliography_rules": [
    "Usar derechos-de-los-contratos-y-obligaciones.bib como archivo canónico local.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Agregar doctrina, normas o jurisprudencia solo si son verificables.",
    "No inventar referencias.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Declarar [supuesto] cuando una referencia requerida no esté disponible."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas transversales estables y verificadas.",
    "Excluir metadatos específicos cuando el nodo destino no sea equivalente.",
    "Mantener estrategia progresiva y conservadora: sumar sin recortar reglas útiles.",
    "Aplicar deduplicación lossless por unión semántica.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual."
  ],
  "open_questions": [
    "[supuesto] Falta guía formal de citación jurídica específica de la materia.",
    "[supuesto] Falta rúbrica por actividad para calibrar profundidad argumentativa.",
    "[supuesto] Falta confirmar alcance de fuentes: federales, locales o mixtas por actividad.",
    "[supuesto] Falta confirmar si presentación exige metadatos idénticos al reporte."
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
        "Carpeta de materia como entrada canónica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 4, bloque 1, obligatoria, 8 créditos.",
        "Asignatura: Derechos de los contratos y obligaciones."
      ]
    },
    "essence": [
      "Resolver problemas jurídicos con método y evidencia.",
      "Vincular conceptos y normas con análisis propio.",
      "Cerrar con criterio jurídico aplicable."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos verificables y transferibles.",
      "Asegurar consistencia editorial entre reporte, presentación y bibliografía.",
      "Sostener una memoria persistente sin regresiones."
    ],
    "style_markers": [
      "Supuestos etiquetados como [supuesto].",
      "Secciones funcionales y trazables.",
      "Conclusión jurídica operativa."
    ],
    "argumentative_patterns": [
      "Problema delimitado -> marco conceptual/normativo -> análisis propio -> conclusión.",
      "Objetivo explícito -> evidencia verificable -> inferencia jurídica -> cierre transferible.",
      "Evitar descripción pura; exigir postura sustentada."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalización estructurada",
        "JSON parseable",
        "Problema jurídico",
        "Marco normativo/doctrinal",
        "Análisis jurídico propio",
        "Conclusión transferible",
        "Contratos",
        "Obligaciones",
        "Bibliografía verificable"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalización estructurada",
          "target": "JSON parseable",
          "kind": "supports",
          "justification": "La estructura validable evita propagación defectuosa."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis jurídico propio",
          "kind": "depends_on",
          "justification": "El análisis requiere una cuestión delimitada."
        },
        {
          "source": "Análisis jurídico propio",
          "target": "Conclusión transferible",
          "kind": "develops",
          "justification": "El cierre deriva del razonamiento sustentado."
        },
        {
          "source": "Bibliografía verificable",
          "target": "Análisis jurídico propio",
          "kind": "supports",
          "justification": "La postura se legitima con fuentes comprobables."
        },
        {
          "source": "Identidad UnADM",
          "target": "Contratos",
          "kind": "develops",
          "justification": "El enfoque institucional se especializa en la materia destino."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicación curricular y pauta editorial.",
        "Programa analítico: cinco ejes de trabajo transversales.",
        "Archivo .bib local: entradas institucionales verificables.",
        "Regla técnica local: resolver placeholders $(@{...}.Slug)."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: deduplicación semántica aplicada sin eliminar reglas útiles previas.",
      "Ciclo 2: se transfiere solo abstracción estable desde actividad de otra materia.",
      "Ciclo 2: se evita propagar contenido temático específico de Filosofía del Derecho.",
      "Ciclo 2: se refuerzan gates de calidad, estructura reusable e identidad institucional."
    ]
  }
}