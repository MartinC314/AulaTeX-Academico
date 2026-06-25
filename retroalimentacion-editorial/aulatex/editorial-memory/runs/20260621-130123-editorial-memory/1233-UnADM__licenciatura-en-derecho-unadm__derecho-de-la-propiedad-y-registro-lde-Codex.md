{
  "summary": [
    "Se consolida sincronización transversal con base institucional UnADM ya verificada.",
    "Se transfieren solo abstracciones estables desde Filosofía del Derecho hacia Propiedad y Registro.",
    "Se refuerzan ejes comunes: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se mantiene política de normalización obligatoria para salidas no JSON.",
    "Se conserva estrategia progresiva y conservadora sin regresión."
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
    "Separar en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Transformar planeación en reporte, presentación o producto visual según consigna."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Relacionar el desarrollo con propiedad y registro cuando aplique.",
    "No asumir fuentes de semanas posteriores sin validación de consigna.",
    "Verificar que el producto final corresponda a la actividad solicitada."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar que no existan placeholders sin resolver en .tex."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Conservar clase article con opciones spanish, letterpaper y oneside salvo instrucción distinta.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Verificar nombres reales de archivos antes de automatizar rutas.",
    "Mantener metadatos base de la plantilla y actualizar título/subtítulo por actividad."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes jurídicas verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Registrar fuentes específicas en derecho-de-la-propiedad-y-registro.bib.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Mantener trazabilidad entre citas usadas y entradas existentes del .bib."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y no ambiguas.",
    "Compartir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferir redacción literal o datos hiperlocales del nodo origen.",
    "Mantener compresión lossless por unión y deduplicación.",
    "Aplicar normalización manual en ciclos con antecedentes no estructurados."
  ],
  "open_questions": [
    "Supuesto: falta rúbrica local detallada por actividad; confirmar criterio de evaluación.",
    "Supuesto: falta consigna específica de próxima actividad; confirmar tipo de entregable.",
    "Confirmar si existe estilo de citación jurídica exigido por figura docente.",
    "Confirmar sustitución del placeholder de Figura docente en plantilla .tex.",
    "Confirmar si habrá fuentes obligatorias de propiedad y registro por semana."
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
        "Carpeta de asignatura como entrada canónica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 7, bloque 1, obligatoria, 8 créditos.",
        "Materia: Derecho de la propiedad y registro."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Conceptos, normas y doctrina pertinentes.",
      "Evidencia verificable.",
      "Análisis propio y postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos.",
      "Asegurar trazabilidad entre consigna, argumentación y cierre.",
      "Sostener calidad editorial reproducible en LaTeX."
    ],
    "style_markers": [
      "Enunciados breves y accionables.",
      "Supuestos marcados de forma explícita.",
      "Sin afirmaciones sin fuente.",
      "Sin placeholders al cierre."
    ],
    "argumentative_patterns": [
      "Del problema al marco conceptual.",
      "Del marco normativo a la evidencia.",
      "De la evidencia al análisis propio.",
      "Del análisis a una conclusión aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad académica",
        "Problema jurídico",
        "Marco normativo/doctrinal",
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
          "justification": "La pauta institucional exige citas verificables y formato consistente."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis debe responder al problema planteado."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica requiere fundamento normativo y doctrinal."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay reutilización segura."
        },
        {
          "source": "Trazabilidad bibliográfica",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La consistencia entre texto y .bib evita afirmaciones no verificables."
        }
      ],
      "evidence": [
        "README de la materia: pauta editorial y ubicación curricular.",
        "Programa analítico: propósito y ejes de trabajo.",
        "derecho-de-la-propiedad-y-registro.bib: claves institucionales existentes."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin pérdida semántica.",
      "Se preservaron gates críticos heredados sobre JSON y normalización.",
      "Se reforzó patrón argumentativo común transferible entre materias de Derecho.",
      "Se evitó migrar contenido temático específico de Filosofía no estable para esta materia."
    ]
  }
}