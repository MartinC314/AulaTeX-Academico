{
  "summary": [
    "Se consolida refuerzo lateral para Actividad 5 con deduplicación lossless.",
    "Se preserva identidad UnADM y ubicación curricular oficial.",
    "Se mantienen ejes editoriales troncales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se refuerza control de normalización JSON antes de propagación recursiva.",
    "Se evita copiar conclusiones o bibliografía exclusiva de Actividad 1.",
    "Supuesto: falta consigna local completa de Actividad 5; se conserva estructura base y preguntas abiertas."
  ],
  "identity_rules": [
    "Mantener tono formal académico y precisión jurídica.",
    "Alinear toda entrega con UnADM y Licenciatura en Derecho.",
    "Conservar referencia curricular: semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar memorias de modelos previos como provisionales hasta verificación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir explícitamente afirmación, evidencia e inferencia.",
    "Cerrar con conclusión jurídica transferible a práctica profesional.",
    "Alinear formato final al producto solicitado por la planeación semanal."
  ],
  "activity_rules": [
    "Adaptar el contenido al enunciado real de Actividad 5.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar bibliografía de otra semana sin validar pertinencia.",
    "Registrar supuesto operativo cuando el alcance no esté explícito."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de guardar.",
    "Confirmar respaldo o marca de supuesto en afirmaciones clave.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Rechazar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Mantener revisión manual extra por historial de incidentes de parseo."
  ],
  "latex_rules": [
    "Usar acentos y codificación española de forma consistente en .tex y .bib.",
    "Mantener claves BibTeX estables ya citadas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver tokens sin expandir en README y programa analítico.",
    "Validar nombre canónico del .bib antes de compilar.",
    "Supuesto: el .bib canónico esperado es filosofia-del-derecho.bib."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Agregar al .bib solo fuentes realmente citadas.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Tratar filosofia-del-derecho-clean.bib como potencialmente de otra semana hasta confirmar pertinencia."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir solo patrones reutilizables de identidad, estructura y calidad.",
    "Evitar regresiones: no eliminar reglas útiles previas.",
    "Aplicar unión y deduplicación como método de compresión lossless.",
    "No propagar fuentes provisionales como bibliografía académica.",
    "Mantener bandera histórica de riesgo por salidas no parseables en ciclos previos."
  ],
  "open_questions": [
    "Confirmar consigna textual completa de Actividad 5.",
    "Confirmar rúbrica específica de evaluación de Actividad 5.",
    "Confirmar tipo de entregable requerido: reporte, presentación o recurso visual.",
    "Confirmar si Actividad 5 reutiliza bibliografía de Semana 7.",
    "Confirmar nombre canónico final del archivo .bib en la asignatura."
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
      "Resolver problemas jurídicos con base conceptual y normativa.",
      "Convertir planeación semanal en producto evaluable.",
      "Sostener análisis propio con evidencia verificable.",
      "Concluir con aplicabilidad profesional."
    ],
    "reason_for_being": [
      "Asegurar continuidad editorial entre actividades hermanas sin copiar contenido específico.",
      "Mantener calidad técnica y argumentativa en toda entrega.",
      "Preservar memoria institucional estable para propagación recursiva."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Secciones funcionales y trazables.",
      "Uso explícito de supuestos cuando falta información.",
      "Cierre con conclusión jurídica propia."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> inferencia jurídica.",
      "Contraste doctrinal breve -> toma de postura."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Problema jurídico",
        "Marco normativo/doctrinal",
        "Evidencia verificable",
        "Análisis propio",
        "Conclusión transferible",
        "Normalización JSON",
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
          "justification": "La pauta institucional define tono, formato y exigencia académica."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "Sin problema delimitado no hay argumentación focalizada."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión válida requiere sustento trazable."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "La transferencia segura exige estructura parseable."
        },
        {
          "source": "Bibliografía base",
          "target": "Bibliografía específica de actividad",
          "kind": "contrasts",
          "justification": "La base orienta la materia; la específica responde a la consigna puntual."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad académica y conclusión jurídica propia.",
        "Programa analítico: ejes problema, conceptos, fuentes, análisis y cierre.",
        "Historial de memoria: incidentes de salida no parseable obligan control de estructura."
      ]
    },
    "reinforcement_log": [
      "Ciclo 23: se deduplican reglas repetidas y se conserva contenido útil previo.",
      "Ciclo 23: se transfiere solo patrón reusable desde Actividad 1 a Actividad 5.",
      "Ciclo 23: se mantiene separación entre bibliografía base y bibliografía específica.",
      "Ciclo 23: se conserva gate estricto de JSON parseable para propagación recursiva."
    ]
  }
}