{
  "summary": [
    "Se consolida memoria lateral de Actividad 5 con transferencia reutilizable desde Actividad 1.",
    "Se preserva identidad UnADM, marco curricular y ejes editoriales troncales sin copiar contenido específico.",
    "Se refuerza control de normalización JSON y deduplicación lossless antes de propagación recursiva.",
    "Se mantiene separación entre bibliografía base de asignatura y bibliografía específica por actividad.",
    "Supuesto: falta consigna y rúbrica locales de Actividad 5; se mantiene estructura base verificable."
  ],
  "identity_rules": [
    "Mantener tono formal académico y precisión jurídica.",
    "Alinear toda entrega con UnADM y Licenciatura en Derecho.",
    "Vincular contexto curricular: semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar memorias de modelos previos como provisionales hasta verificación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir afirmación, evidencia e inferencia en bloques claros.",
    "Cerrar con conclusión jurídica transferible a práctica profesional.",
    "Alinear formato final al producto solicitado en la planeación semanal."
  ],
  "activity_rules": [
    "Adaptar el entregable al enunciado real de Actividad 5.",
    "Incluir postura argumentada del estudiante.",
    "Evitar textos solo descriptivos o de resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar conclusiones ni bibliografía exclusiva de otra actividad sin validar pertinencia."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de reutilizar.",
    "Confirmar respaldo o marca de supuesto en cada afirmación clave.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Rechazar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Revisar correspondencia entre producto entregado y consigna local."
  ],
  "latex_rules": [
    "Usar acentos y codificación en español de forma consistente en .tex y .bib.",
    "Mantener claves BibTeX estables ya citadas en .tex.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y rutas.",
    "Supuesto: nombre canónico esperado del .bib es filosofia-del-derecho.bib; confirmar localmente."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Registrar en .bib solo fuentes realmente citadas.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, editorial o URL.",
    "Distinguir bibliografía base de asignatura frente a bibliografía específica de actividad.",
    "Confirmar pertinencia antes de reutilizar filosofia-del-derecho-clean.bib en Actividad 5."
  ],
  "propagation_hints": [
    "Propagar solo patrones reutilizables: identidad, estructura, calidad y relaciones troncales.",
    "No propagar redacción literal ni conclusiones específicas entre nodos hermanos.",
    "Aplicar unión y deduplicación sin pérdida antes de guardar memoria.",
    "Conservar reglas útiles previas y agregar solo mejoras verificables.",
    "Mantener bandera histórica de riesgo por incidentes de parseo en ciclos previos.",
    "Si falta dato local, propagar plantilla y pregunta abierta en lugar de contenido inventado."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 5.",
    "Confirmar rúbrica de evaluación específica de Actividad 5.",
    "Confirmar tipo de producto requerido: reporte, presentación o recurso visual.",
    "Confirmar archivo .bib canónico final de la asignatura.",
    "Confirmar si la bibliografía de Semana 7 aplica total, parcial o no aplica a Actividad 5."
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
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos con fundamento jurídico.",
      "Garantizar trazabilidad entre consigna, argumentación, evidencia y cierre.",
      "Preservar continuidad editorial institucional entre actividades."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales.",
      "Postura propia explícita.",
      "Supuestos marcados cuando falte información.",
      "Cierre aplicable a práctica profesional."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> inferencia jurídica.",
      "Contraste doctrinal breve -> toma de postura.",
      "Conclusión -> transferencia a contexto profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalización JSON",
        "Problema jurídico",
        "Marco normativo/doctrinal",
        "Evidencia verificable",
        "Análisis propio",
        "Conclusión transferible",
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
          "justification": "Define tono, integridad y criterios de entrega."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis requiere conflicto o pregunta delimitada."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La validez jurídica del cierre depende del respaldo trazable."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo válido no hay transferencia confiable."
        },
        {
          "source": "Bibliografía específica por actividad",
          "target": "Bibliografía base",
          "kind": "contrasts",
          "justification": "La base orienta; la específica responde a la consigna concreta."
        }
      ],
      "evidence": [
        "README establece identidad UnADM, integridad académica y conclusión jurídica propia.",
        "Programa analítico fija ejes problema-conceptos-fuentes-análisis-cierre.",
        "Historial de incidentes no parseables justifica gate estricto de estructura.",
        "Tokens Slug sin expandir en README justifican validación de rutas y nombre .bib."
      ]
    },
    "reinforcement_log": [
      "Ciclo 10: deduplicación integral aplicada sin pérdida de reglas útiles.",
      "Ciclo 10: se reforzó transferencia lateral por patrones, no por contenido específico.",
      "Ciclo 10: se mantuvo separación entre reglas estables y supuestos pendientes.",
      "Ciclo 10: se conservó compatibilidad editorial y técnica para propagación recursiva."
    ]
  }
}