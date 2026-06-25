{
  "summary": [
    "Se mantiene base institucional UnADM y se refuerza sincronización transversal entre materias.",
    "Se transfieren solo abstracciones editoriales estables desde actividad de Filosofía del Derecho.",
    "Se conservan ejes comunes: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se preserva política de normalización obligatoria para salidas no JSON parseables.",
    "Se consolida estrategia progresiva y conservadora sin regresión."
  ],
  "identity_rules": [
    "Mantener identidad explícita UnADM en tono, portada y metadatos.",
    "Usar nombre exacto de materia: Derecho de la propiedad y registro.",
    "Mantener programa: Licenciatura en Derecho.",
    "Mantener ubicación curricular: semestre 7, bloque 1, obligatoria, 8 créditos.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener estructura reusable para reporte y presentación sin copiar redacción literal."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Relacionar desarrollo con propiedad y registro cuando aplique.",
    "No asumir fuentes de semanas posteriores sin validar consigna."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna de la actividad."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir placeholders en metadatos antes de entrega final."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes jurídicas verificables.",
    "Registrar fuentes específicas de actividad en derecho-de-la-propiedad-y-registro.bib.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Compartir transversalmente solo reglas generales y estables entre nodos no equivalentes.",
    "Evitar transferir contenido temático específico de Filosofía del Derecho al destino.",
    "Mantener compresión lossless por unión y deduplicación.",
    "Evitar regresiones respecto de reglas útiles previas."
  ],
  "open_questions": [
    "Confirmar rúbrica local de evaluación por actividad en Derecho de la propiedad y registro.",
    "Confirmar estilo de citación jurídica exigido por figura docente.",
    "Supuesto: el .bib canónico local es derecho-de-la-propiedad-y-registro.bib; validar en pipeline.",
    "Confirmar resolución definitiva de tokens corruptos en README.",
    "Confirmar dato faltante de Figura docente en plantilla .tex."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador en inferencias."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Normalización estructurada antes de propagación.",
        "Entrada canónica por carpeta de asignatura."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 7, bloque 1, obligatoria, 8 créditos.",
        "Materia: Derecho de la propiedad y registro."
      ]
    },
    "essence": [
      "Problema jurídico claro.",
      "Fundamento conceptual y normativo.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Transformar la planeación semanal en productos académicos sólidos y verificables.",
      "Asegurar trazabilidad editorial y bibliográfica en toda entrega.",
      "Mantener coherencia institucional transversal sin perder contexto local."
    ],
    "style_markers": [
      "Frases breves y accionables.",
      "Supuestos marcados explícitamente.",
      "Sin afirmaciones sin fuente.",
      "Sin placeholders al cierre."
    ],
    "argumentative_patterns": [
      "Del problema al marco conceptual.",
      "Del marco normativo a la evidencia.",
      "De la evidencia al análisis propio.",
      "Del análisis a la conclusión aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad académica",
        "Problema jurídico",
        "Marco normativo/doctrinal",
        "Evidencia verificable",
        "Análisis propio",
        "Conclusión transferible",
        "Normalización JSON",
        "Trazabilidad bibliográfica"
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
          "justification": "La identidad institucional exige trazabilidad y formato verificable."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis debe responder a una pregunta jurídica concreta."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión requiere fundamento normativo explícito."
        },
        {
          "source": "Normalización JSON",
          "target": "Trazabilidad bibliográfica",
          "kind": "depends_on",
          "justification": "La reutilización confiable depende de estructura parseable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Las afirmaciones válidas deben poder auditarse en fuentes."
        }
      ],
      "evidence": [
        "README local de la materia.",
        "Programa analítico local.",
        "Archivo BibTeX local derecho-de-la-propiedad-y-registro.bib.",
        "Regla heredada estable: bloquear propagación sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 6: deduplicación completa de reglas repetidas.",
      "Ciclo 6: refuerzo de gates de calidad compartidos entre nodos.",
      "Ciclo 6: transferencia conservadora sin arrastre temático específico de Filosofía del Derecho.",
      "Ciclo 6: mantenimiento de política lossless por unión-dedupe."
    ]
  }
}