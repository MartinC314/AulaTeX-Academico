{
  "summary": [
    "Se consolida sincronización transversal conservadora entre actividad de origen y materia destino.",
    "Se preservan reglas útiles previas y se deduplican sin recorte semántico.",
    "Se refuerza el modelo estable de cinco ejes: problema, conceptos, producto, análisis propio y conclusión jurídica.",
    "Se mantiene la normalización obligatoria de salidas no estructuradas antes de propagar.",
    "Se incorpora control técnico de placeholders tipo $(@{...}.Slug) detectados en README y programa analítico del destino."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares confirmados del destino: semestre 4, bloque 1, obligatoria, 8 créditos.",
    "Conservar enfoque disciplinar en contratos y obligaciones.",
    "Usar la carpeta de materia como entrada canónica.",
    "Marcar como [supuesto] todo dato no visible en la consigna local.",
    "Tratar herencias no verificadas (Codex/GPT-Pro) como provisionales hasta confirmación local.",
    "Usar LDE-S4B1 cuando la plantilla lo requiera.",
    "[supuesto] Mantener autor y ubicación institucional por defecto solo si la actividad no instruye cambios."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Alinear el entregable al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener trazabilidad entre objetivo, evidencia, argumento y conclusión.",
    "Distinguir bibliografía base de fuentes específicas por actividad."
  ],
  "activity_rules": [
    "Explicitar postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y cierre.",
    "No trasladar contenido de otras materias sin adecuación al contexto contractual.",
    "Marcar supuestos cuando falte instrucción específica de actividad.",
    "Confirmar que el producto final coincida con la consigna semanal."
  ],
  "quality_gates": [
    "Bloquear persistencia y propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar correspondencia entre citas en texto y archivo .bib local.",
    "Corregir placeholders o tokens sin expandir en rutas y nombres de archivo antes de compilar.",
    "No degradar reglas útiles previas durante unión-deduplicación."
  ],
  "latex_rules": [
    "Usar plantilla base local de reporte o presentación según consigna.",
    "Mantener metadatos completos: curso, autor, universidad, ubicación y subtítulo de actividad.",
    "Actualizar documenttitle y documentsubtitle al producto real antes de compilar.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens $(@{...}.Slug) en README/programa antes de referenciar .bib canónico."
  ],
  "bibliography_rules": [
    "Usar derechos-de-los-contratos-y-obligaciones.bib como archivo canónico local.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Agregar fuentes específicas por actividad con metadatos mínimos: autor, título, año y fuente/URL.",
    "Priorizar fuentes institucionales UnADM y normas/doctrina/jurisprudencia verificables.",
    "No inventar referencias.",
    "Marcar [supuesto] cuando una fuente requerida no esté disponible al momento."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas transversales estables, no redacción literal.",
    "Aplicar lateralmente solo tras validar compatibilidad disciplinar.",
    "Excluir metadatos específicos de materia cuando el nodo destino no coincida.",
    "Mantener estrategia progresiva y conservadora: agregar mejoras verificables sin borrar reglas útiles.",
    "Registrar ciclos con necesidad de normalización manual cuando haya herencia no estructurada."
  ],
  "open_questions": [
    "Confirmar guía formal de citación obligatoria para esta materia.",
    "Confirmar rúbrica de evaluación por actividad para calibrar profundidad argumentativa.",
    "Confirmar alcance normativo por actividad: federal, local o mixto.",
    "Confirmar si presentación comparte todos los metadatos del reporte.",
    "Confirmar que el .bib canónico en README/programa ya quedó sin token dinámico."
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
      "Resolver problemas jurídicos con estructura verificable.",
      "Sostener análisis propio con evidencia trazable.",
      "Cerrar con criterio jurídico aplicable."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos y verificables.",
      "Unificar identidad institucional y calidad técnica en cada entrega."
    ],
    "style_markers": [
      "Supuestos etiquetados como [supuesto].",
      "Secciones funcionales y trazables.",
      "Conclusión jurídica operativa.",
      "Control de consistencia entre consigna, contenido y evidencia."
    ],
    "argumentative_patterns": [
      "Problema delimitado -> marco conceptual/normativo -> análisis propio -> conclusión transferible.",
      "Objetivo explícito antes del desarrollo.",
      "Afirmación relevante siempre con respaldo verificable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalización estructurada",
        "Cinco ejes editoriales",
        "Integridad académica",
        "Contratos",
        "Obligaciones",
        "Análisis jurídico propio",
        "Conclusión transferible"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La pauta institucional exige formato consistente y citas verificables."
        },
        {
          "source": "Normalización estructurada",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Evita propagar errores de salidas no parseables."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Análisis jurídico propio",
          "kind": "develops",
          "justification": "La estructura guía el razonamiento y evita entregas descriptivas."
        },
        {
          "source": "Análisis jurídico propio",
          "target": "Conclusión transferible",
          "kind": "depends_on",
          "justification": "La conclusión válida deriva del argumento sustentado."
        },
        {
          "source": "Contratos",
          "target": "Obligaciones",
          "kind": "develops",
          "justification": "El enfoque disciplinar del destino integra ambas categorías jurídicas."
        }
      ],
      "evidence": [
        "README de materia: identidad UnADM, ubicación curricular y pauta editorial.",
        "Programa analítico: cinco ejes de trabajo y propósito de realización.",
        "Archivo .bib local: entradas institucionales base verificables.",
        "Detección local de token $(@{...}.Slug) en README/programa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 18: deduplicación lossless aplicada sin eliminar reglas útiles.",
      "Ciclo 18: se transfiere solo abstracción transversal estable desde actividad no equivalente.",
      "Ciclo 18: se preserva gate duro de JSON parseable y normalización previa a propagación.",
      "Ciclo 18: se refuerza control técnico de placeholders en rutas y nombres de bibliografía."
    ]
  }
}