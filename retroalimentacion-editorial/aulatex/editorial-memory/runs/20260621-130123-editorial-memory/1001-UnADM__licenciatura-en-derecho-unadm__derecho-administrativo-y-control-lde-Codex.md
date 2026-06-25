{
  "summary": [
    "Se sincroniza memoria transversal desde actividad de Filosofía del Derecho a materia de Derecho administrativo y control sin regresión.",
    "Se preservan reglas institucionales válidas y se deduplican en modo lossless por unión.",
    "Se refuerzan ejes editoriales estables: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se mantiene prioridad de normalización estructurada antes de propagación recursiva.",
    "Se evita transferir contenido doctrinal específico no equivalente entre materias."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en tono, portada, metadatos y formato.",
    "Usar nombre exacto de materia: Derecho administrativo y control.",
    "Conservar enfoque de Licenciatura en Derecho en todos los entregables.",
    "Usar carpeta de materia como entrada canónica.",
    "Marcar como [supuesto] todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Mantener encuadre curricular local: semestre 6, bloque 1, obligatoria, 8 créditos."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a práctica profesional.",
    "Mantener consistencia entre README, .tex y .bib.",
    "Corregir placeholders y tokens sin expandir en README y programa analítico. [supuesto]"
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo descripción.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Identificar explícitamente tipo de producto: reporte, presentación o visual.",
    "Vincular el análisis al campo de control administrativo y práctica profesional.",
    "No reutilizar automáticamente fuentes de otras semanas o materias sin validación local."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que reglas heredadas no contradigan programa analítico local."
  ],
  "latex_rules": [
    "Mantener español y codificación correcta en .tex y .bib.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Asegurar coherencia entre \\documenttitle, \\documentsubtitle y actividad real.",
    "Reemplazar 'Actividad X' por número y nombre real antes de entrega.",
    "Sustituir 'Nombre por definir' por figura docente oficial antes de entrega.",
    "Resolver tokens tipo $(@{...}.Slug) por slug literal en rutas y nombres. [supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y documentos jurídicos verificables.",
    "Registrar fuentes específicas de cada actividad en derecho-administrativo-y-control.bib.",
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Usar malla curricular local como fuente de ubicación curricular."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir solo abstracciones editoriales estables en nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferencia de redacción literal y doctrina específica de otra materia.",
    "Mantener estrategia conservadora: sin eliminar reglas útiles previas.",
    "Aplicar normalización manual cuando la fuente heredada sea provisional."
  ],
  "open_questions": [
    "Confirmar convención final para archivo de referencias adicional en README. [supuesto]",
    "Confirmar corrección de artefactos de nombre 'eporte-' y 'eferencias-' en estructura README. [supuesto]",
    "Confirmar si año de consulta 2026 del sitio UnADM se mantiene en futuras entregas.",
    "Confirmar formato institucional de citación requerido por la licenciatura.",
    "Confirmar fuente definitiva para retirar etiquetas provisionales Codex/GPT-Pro."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Institucional y conservador ante fuentes no verificadas."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Normalización estructurada previa a propagación.",
        "No invención de fuentes.",
        "Carpeta de materia como entrada canónica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho administrativo y control.",
        "Semestre 6, bloque 1, obligatoria, 8 créditos.",
        "Coursecode local: LDE-S6B1."
      ]
    },
    "essence": [
      "Problema jurídico delimitado.",
      "Conceptos, normas y doctrina pertinentes.",
      "Evidencia verificable.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible a práctica profesional."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos rigurosos y aplicables.",
      "Garantizar trazabilidad entre afirmaciones, citas y bibliografía.",
      "Sostener una memoria editorial reutilizable sin pérdida de reglas útiles."
    ],
    "style_markers": [
      "Secciones explícitas y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Cierre con criterio jurídico aplicable.",
      "Consistencia entre README, LaTeX y .bib."
    ],
    "argumentative_patterns": [
      "Problema y objetivo al inicio.",
      "Marco conceptual y normativo antes del juicio propio.",
      "Postura del estudiante sustentada con evidencia.",
      "Conclusión práctica y jurídicamente transferible."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalización estructurada",
        "Problema jurídico",
        "Marco normativo/doctrinal",
        "Evidencia verificable",
        "Análisis propio",
        "Conclusión transferible",
        "Control administrativo"
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
          "justification": "La identidad institucional exige trazabilidad y rigor de fuentes."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin JSON válido y completo no se propaga memoria."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis requiere problema delimitado."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión aplicable necesita sustento jurídico."
        },
        {
          "source": "Control administrativo",
          "target": "Conclusión transferible",
          "kind": "develops",
          "justification": "La materia orienta aplicación profesional en administración y control."
        }
      ],
      "evidence": [
        "README local de la materia.",
        "Programa analítico local.",
        "derecho-administrativo-y-control.bib.",
        "Regla consolidada: bloquear salidas no JSON parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 9: se consolidan reglas transversales estables sin trasladar doctrina específica de Filosofía del Derecho.",
      "Ciclo 9: se mantiene compresión lossless por deduplicación y unión.",
      "Ciclo 9: se refuerza gate crítico de parseabilidad JSON y estructura mínima.",
      "Ciclo 9: se preservan alertas sobre fuentes provisionales con marcado [supuesto]."
    ]
  }
}