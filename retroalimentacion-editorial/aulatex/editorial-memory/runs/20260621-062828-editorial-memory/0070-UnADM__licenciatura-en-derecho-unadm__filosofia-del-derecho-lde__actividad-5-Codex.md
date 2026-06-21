{
  "summary": [
    "Se consolida memoria lateral de Actividad 5 con deduplicación lossless.",
    "Se preserva identidad UnADM y ubicación curricular verificable.",
    "Se refuerzan ejes troncales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se mantiene normalización JSON obligatoria antes de propagación recursiva.",
    "Se evita traslado literal de conclusiones y bibliografía exclusiva entre actividades hermanas.",
    "Supuesto: falta consigna y rúbrica local de Actividad 5; se mantiene estructura base reusable."
  ],
  "identity_rules": [
    "Mantener tono institucional UnADM, formal y jurídico-académico.",
    "Vincular actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar memoria de modelos previos como provisional hasta verificación local.",
    "No usar fuentes de memoria como fuentes académicas."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en bloques: conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Distinguir explícitamente afirmación, evidencia e inferencia.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Alinear formato final al producto solicitado por la planeación semanal."
  ],
  "activity_rules": [
    "Adaptar contenido al enunciado real de Actividad 5.",
    "Incluir postura argumentada del estudiante; evitar resumen descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar bibliografía de otra semana sin validar pertinencia.",
    "Si falta dato operativo, registrar supuesto y continuar con consistencia."
  ],
  "quality_gates": [
    "Bloquear propagación si salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en cada afirmación relevante.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que el producto responda al problema y no solo liste conceptos.",
    "Aplicar revisión manual extra ante historial de incidentes de parseo."
  ],
  "latex_rules": [
    "Mantener acentos y codificación en español consistentes en .tex y .bib.",
    "Mantener claves BibTeX estables ya usadas en .tex.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos, referencias rotas ni claves faltantes.",
    "Resolver tokens sin expandir en README y programa analítico antes de referenciar archivos.",
    "Supuesto: nombre canónico esperado del .bib es filosofia-del-derecho.bib; confirmar localmente."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Agregar al .bib solo fuentes realmente citadas en el texto.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a Semana 7; validar pertinencia para Actividad 5."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir solo patrones reutilizables, no redacción ni conclusiones específicas.",
    "Preservar reglas útiles previas y agregar solo mejoras verificables.",
    "Aplicar unión y deduplicación sin recorte semántico.",
    "Mantener bandera de riesgo por salidas no parseables en ciclos previos.",
    "Si falta consigna local, propagar plantilla estructural y preguntas abiertas."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 5.",
    "Confirmar rúbrica de evaluación específica de Actividad 5.",
    "Confirmar tipo de entregable requerido: reporte, presentación o recurso visual.",
    "Confirmar archivo .bib canónico final de la asignatura.",
    "Confirmar si bibliografía de Interpretación jurídica (Semana 7) aplica a Actividad 5.",
    "Confirmar títulos de secciones obligatorias definidos por docente."
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
      "Convertir planeación semanal en productos académicos con rigor jurídico.",
      "Garantizar trazabilidad entre consigna, desarrollo y cierre argumentativo.",
      "Asegurar calidad estructural y verificabilidad bibliográfica antes de propagar."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Secciones funcionales y trazables.",
      "Postura propia sustentada.",
      "Marcado explícito de supuestos.",
      "Cierre aplicado a práctica profesional."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> inferencia jurídica.",
      "Contraste doctrinal breve -> toma de postura.",
      "Regla general -> aplicación al caso -> consecuencia jurídica."
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
          "justification": "Define tono, integridad y formato del entregable."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "Sin delimitación del problema no hay argumentación focalizada."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica requiere respaldo trazable."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo válido no hay transferencia confiable."
        },
        {
          "source": "Bibliografía base",
          "target": "Bibliografía específica de actividad",
          "kind": "contrasts",
          "justification": "La base orienta; la específica responde a la consigna local."
        },
        {
          "source": "Consistencia cita-.bib",
          "target": "Calidad editorial",
          "kind": "supports",
          "justification": "Evita citas huérfanas y mantiene reproducibilidad."
        }
      ],
      "evidence": [
        "README establece identidad UnADM, integridad académica y conclusión jurídica propia.",
        "Programa analítico fija ejes: problema, conceptos, fuentes, análisis y cierre.",
        "Historial registra incidentes de salida no parseable; se justifica gate de estructura.",
        "Tokens sin expandir en rutas justifican validación de nombres canónicos."
      ]
    },
    "reinforcement_log": [
      "Ciclo 70: deduplicación integral de reglas repetidas en destino.",
      "Ciclo 70: preservadas reglas útiles del origen sin copiar contenido específico de Actividad 1.",
      "Ciclo 70: reforzado gate de JSON parseable y revisión manual por riesgo histórico.",
      "Ciclo 70: mantenida separación entre bibliografía base y bibliografía por actividad.",
      "Ciclo 70: añadidas preguntas abiertas por falta de consigna local verificable."
    ]
  }
}