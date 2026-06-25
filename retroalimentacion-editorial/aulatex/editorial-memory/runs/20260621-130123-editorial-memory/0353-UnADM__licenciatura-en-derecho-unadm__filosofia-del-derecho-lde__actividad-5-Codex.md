{
  "summary": [
    "Se consolida refuerzo lateral entre actividades hermanas con deduplicación lossless.",
    "Se preserva identidad UnADM y marco curricular de Filosofía del Derecho.",
    "Se mantienen ejes troncales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se refuerza control obligatorio de normalización JSON antes de propagación recursiva.",
    "Se evita transferencia de redacción literal, conclusiones específicas y bibliografía exclusiva de Actividad 1.",
    "Supuesto: falta consigna local completa de Actividad 5; se mantiene estructura base reusable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, encuadre y formato.",
    "Vincular toda entrega a Licenciatura en Derecho y asignatura Filosofía del Derecho.",
    "Respetar ubicación curricular: semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar memorias de modelos previos como provisionales hasta verificación local.",
    "No usar trazas de modelo como fuente académica."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir afirmación, evidencia e inferencia en cada bloque argumentativo.",
    "Cerrar con conclusión jurídica transferible a práctica profesional.",
    "Alinear estructura al producto solicitado por la planeación semanal.",
    "Conservar salida estructurada y parseable para memoria y propagación."
  ],
  "activity_rules": [
    "Adaptar contenido al enunciado real de Actividad 5 sin romper reglas de asignatura.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar bibliografía de otra semana sin confirmar pertinencia.",
    "Registrar supuesto operativo cuando falte detalle de alcance.",
    "Mantener trazabilidad entre consigna, desarrollo y criterio de evaluación."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en toda afirmación relevante.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Rechazar respuestas no estructuradas antes de reutilización.",
    "Aplicar revisión manual extra por historial de incidentes de parseo.",
    "Validar que el producto responda al problema y no solo resuma conceptos."
  ],
  "latex_rules": [
    "Usar acentos y codificación en español de forma consistente en .tex y .bib.",
    "Mantener claves BibTeX estables ya usadas en .tex.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Validar nombres canónicos de archivos antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: el .bib canónico esperado es filosofia-del-derecho.bib hasta confirmación final."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes jurídicas verificables.",
    "Registrar en .bib solo fuentes realmente citadas.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Tratar filosofia-del-derecho-clean.bib como potencialmente acotado a Semana 7 hasta confirmar pertinencia para Actividad 5.",
    "Conservar claves citadas para evitar ruptura de compilación."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas reutilizables y verificadas.",
    "Preservar reglas útiles previas; agregar solo mejoras verificables.",
    "Aplicar unión y deduplicación sin pérdida semántica.",
    "No propagar conclusiones específicas entre actividades hermanas.",
    "No propagar bibliografía exclusiva sin validación de pertinencia local.",
    "Mantener bandera de riesgo histórico por salidas no parseables.",
    "Si falta consigna local, propagar plantilla estructural y preguntas abiertas."
  ],
  "open_questions": [
    "Confirmar enunciado completo de Actividad 5.",
    "Confirmar rúbrica de evaluación específica de Actividad 5.",
    "Confirmar formato exigido: reporte, presentación o recurso visual.",
    "Confirmar si Actividad 5 requiere .bib propio o reutiliza uno existente.",
    "Confirmar nombre canónico final del archivo .bib de la asignatura.",
    "Confirmar pertinencia de fuentes de Semana 7 para Actividad 5."
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
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en entregables con claridad jurídica y trazabilidad argumentativa.",
      "Asegurar continuidad editorial entre actividades sin perder especificidad local."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones funcionales y explícitas.",
      "Uso visible de supuestos cuando falten datos.",
      "Cierre con transferencia a práctica profesional."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> inferencia jurídica.",
      "Contraste doctrinal breve -> toma de postura fundada."
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
          "target": "Estructura argumentativa de actividad",
          "kind": "supports",
          "justification": "La pauta institucional fija tono, forma y exigencia de integridad académica."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia confiable."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis requiere un conflicto delimitado."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La validez de la conclusión depende del respaldo trazable."
        },
        {
          "source": "Bibliografía base",
          "target": "Bibliografía específica de actividad",
          "kind": "contrasts",
          "justification": "La base orienta el curso; la específica responde a la consigna puntual."
        }
      ],
      "evidence": [
        "README establece identidad UnADM, citas verificables y conclusión jurídica propia.",
        "Programa analítico define ejes problema-conceptos-fuentes-análisis-cierre.",
        "Historial documenta incidentes de salida no parseable; se mantiene gate de estructura."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin eliminar contenido útil.",
      "Se reforzó separación entre patrones transferibles y contenido específico de actividad hermana.",
      "Se mantuvo trazabilidad de supuestos por ausencia de consigna local completa.",
      "Se preservó control estricto de calidad para JSON, citas y compilación LaTeX."
    ]
  }
}