{
  "summary": [
    "Se refuerza memoria lateral de Actividad 5 con patrones reutilizables de Actividad 1.",
    "Se preservan ejes troncales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se mantiene normalización estructurada obligatoria antes de propagación recursiva.",
    "Se deduplica sin pérdida y sin copiar conclusiones específicas entre hermanos.",
    "Supuesto: falta consigna textual local de Actividad 5; se conserva estructura base verificable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Conservar enfoque jurídico-académico con criterio propio.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar memorias de modelos previos como provisionales hasta verificación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir explícitamente afirmación, evidencia e inferencia.",
    "Alinear el entregable al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Adaptar el producto al enunciado real de Actividad 5 sin romper reglas de asignatura.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar bibliografía de otra semana sin confirmar pertinencia.",
    "Registrar supuesto operativo cuando falte instrucción específica."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en cada afirmación relevante.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Validar correspondencia del producto con la consigna local de Actividad 5.",
    "Aplicar revisión manual extra por historial de incidentes de parseo."
  ],
  "latex_rules": [
    "Usar acentos y codificación en español de forma consistente en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y referencias de archivo.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib hasta confirmación local."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar en .bib solo fuentes realmente citadas en el texto.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib está orientado a otra actividad temática; confirmar pertinencia para Actividad 5."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir solo patrones reutilizables; no copiar redacción ni conclusiones específicas.",
    "Conservar reglas útiles previas y agregar solo mejoras verificables.",
    "Aplicar unión y deduplicación lossless para evitar regresiones.",
    "Mantener bandera de riesgo histórico por salidas no parseables en ciclos previos.",
    "Cuando falte dato local, propagar plantilla base y preguntas abiertas."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 5.",
    "Confirmar rúbrica de evaluación específica de Actividad 5.",
    "Confirmar tipo de producto requerido: reporte, presentación o recurso visual.",
    "Confirmar nombre canónico final del archivo .bib de la asignatura.",
    "Confirmar si la bibliografía limpia de Semana 7 aplica o no a Actividad 5."
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
        "Semestre 1, bloque 2, obligatoria, 8 créditos.",
        "Asignatura: Filosofía del Derecho."
      ]
    },
    "essence": [
      "Problema jurídico delimitado.",
      "Marco conceptual y normativo pertinente.",
      "Evidencia verificable.",
      "Análisis propio no descriptivo.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en entregables académicos sólidos.",
      "Sostener continuidad institucional entre actividades hermanas.",
      "Asegurar trazabilidad entre consigna, argumentos, evidencia y cierre."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones funcionales y explícitas.",
      "Supuestos marcados cuando falte información.",
      "Cierre con postura jurídica propia."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> inferencia jurídica.",
      "Contraste doctrinal breve -> toma de postura.",
      "Transferencia del resultado a práctica profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Problema jurídico",
        "Marco normativo/doctrinal",
        "Análisis propio",
        "Conclusión transferible",
        "Normalización JSON",
        "Consistencia cita-.bib",
        "Bibliografía base",
        "Bibliografía específica por actividad"
      ],
      "citations": [
        "README.md",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Estructura de actividad",
          "kind": "supports",
          "justification": "Define tono, rigor y formato del entregable."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis requiere una pregunta jurídica delimitada."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión válida depende de respaldo trazable."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia confiable."
        },
        {
          "source": "Bibliografía específica por actividad",
          "target": "Bibliografía base",
          "kind": "contrasts",
          "justification": "La base orienta; la específica responde a la consigna local."
        },
        {
          "source": "Patrones de Actividad 1",
          "target": "Actividad 5",
          "kind": "develops",
          "justification": "Se transfieren reglas reutilizables sin copiar contenido particular."
        }
      ],
      "evidence": [
        "README exige identidad UnADM, citas verificables y conclusión jurídica.",
        "Programa analítico define ejes problema-conceptos-fuentes-análisis-cierre.",
        "Historial reporta incidentes de salida no parseable; se mantiene gate de estructura.",
        "Se aplicó deduplicación lossless y preservación de reglas útiles."
      ]
    },
    "reinforcement_log": [
      "Ciclo 12: consolidación lateral hermano->hermano sin recorte semántico.",
      "Se reforzó control de parseo JSON como condición de propagación.",
      "Se consolidó separación entre bibliografía base y bibliografía por actividad.",
      "Se mantuvo regla de marcar supuestos ante ausencia de consigna local."
    ]
  }
}