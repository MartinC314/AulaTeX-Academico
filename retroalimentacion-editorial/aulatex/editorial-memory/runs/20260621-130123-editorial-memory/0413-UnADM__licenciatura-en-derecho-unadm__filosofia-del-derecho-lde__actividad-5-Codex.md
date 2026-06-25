{
  "summary": [
    "Se consolida refuerzo lateral desde Actividad 1 hacia Actividad 5 con deduplicación lossless.",
    "Se preserva identidad UnADM, ejes editoriales troncales y control de normalización JSON.",
    "Se transfiere solo patrón reutilizable; no se copian conclusiones ni bibliografía exclusiva del hermano origen.",
    "Se mantiene como supuesto la falta de consigna y rúbrica local de Actividad 5."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y encuadre.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Conservar enfoque jurídico-académico con criterio propio.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar memoria de modelos previos como provisional hasta verificación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir afirmación, evidencia e inferencia en bloques claros.",
    "Alinear el entregable al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Adaptar el producto al enunciado real de Actividad 5 sin romper reglas de asignatura.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar bibliografía de otra semana sin confirmar pertinencia.",
    "Registrar supuesto operativo cuando falte alcance específico."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en afirmaciones relevantes.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que el producto responda a la consigna y no solo resuma conceptos.",
    "Aplicar revisión manual extra en memoria con incidentes previos de parseo."
  ],
  "latex_rules": [
    "Usar acentos y codificación en español de forma consistente en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Validar nombres canónicos de archivos antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes jurídicas verificables.",
    "Registrar en .bib solo fuentes realmente citadas en el texto.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib está orientado a Interpretación jurídica (Semana 7), confirmar pertinencia para Actividad 5."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Reutilizar reglas institucionales sin reducir especificidad local.",
    "Evitar regresiones de reglas útiles previas.",
    "Cuando falte consigna local, propagar estructura base y preguntas abiertas.",
    "No propagar como académicas fuentes de memoria no verificadas.",
    "Mantener bandera histórica de riesgo por salidas no parseables en ciclos previos."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 5; confirmar producto exacto solicitado.",
    "Confirmar rúbrica de evaluación específica de Actividad 5.",
    "Confirmar si el formato principal es reporte, presentación o recurso visual.",
    "Confirmar nombre canónico final del archivo .bib de la asignatura.",
    "Confirmar si Actividad 5 reutiliza bibliografía existente o requiere .bib específico."
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
      "Problema jurídico o social.",
      "Conceptos y marco normativo-doctrinal pertinente.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en entregables académicos sólidos.",
      "Asegurar trazabilidad entre consigna, desarrollo y cierre.",
      "Sostener estándar institucional UnADM en todas las actividades."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales.",
      "Postura propia sustentada.",
      "Supuestos explícitos cuando falten datos."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> inferencia jurídica.",
      "Contraste doctrinal breve -> toma de postura."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalización JSON",
        "Problema jurídico",
        "Evidencia verificable",
        "Análisis propio",
        "Conclusión transferible",
        "Consistencia cita-.bib"
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
          "justification": "Define tono, integridad y formato del entregable."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis requiere una pregunta delimitada."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica exige respaldo trazable."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo válido no hay transferencia confiable."
        },
        {
          "source": "Bibliografía específica de actividad",
          "target": "Bibliografía base",
          "kind": "contrasts",
          "justification": "La base orienta; la específica responde a consigna local."
        },
        {
          "source": "Ejes troncales de asignatura",
          "target": "Actividad 5",
          "kind": "develops",
          "justification": "La estrategia lateral transfiere patrón, no contenido cerrado."
        }
      ],
      "evidence": [
        "README establece identidad UnADM, integridad académica y conclusión jurídica propia.",
        "Programa analítico fija ejes: problema, conceptos, fuentes, análisis y cierre.",
        "Historial previo reporta incidentes de salida no parseable; se mantiene gate técnico.",
        "Archivo clean.bib indica foco de Semana 7; su reutilización en Actividad 5 requiere confirmación."
      ]
    },
    "reinforcement_log": [
      "Ciclo 16: deduplicación integral de reglas repetidas y variantes ortográficas.",
      "Ciclo 16: refuerzo de separación entre bibliografía base y bibliografía específica.",
      "Ciclo 16: mantenimiento explícito de política de supuestos por falta de consigna local.",
      "Ciclo 16: conservación de gate de parseo JSON como condición de propagación."
    ]
  }
}