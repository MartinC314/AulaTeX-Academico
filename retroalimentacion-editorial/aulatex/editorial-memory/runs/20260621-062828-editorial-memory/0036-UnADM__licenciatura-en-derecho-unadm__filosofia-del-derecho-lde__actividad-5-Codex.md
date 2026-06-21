{
  "summary": [
    "Se consolida refuerzo lateral para Actividad 5 con deduplicación lossless.",
    "Se preserva identidad UnADM y contexto curricular de Filosofía del Derecho.",
    "Se mantiene normalización JSON obligatoria antes de propagación recursiva.",
    "Se transfieren solo patrones reutilizables desde Actividad 1.",
    "No se copian conclusiones específicas ni bibliografía exclusiva entre hermanos.",
    "Se conserva eje editorial: problema, conceptos, evidencia, análisis propio y conclusión jurídica."
  ],
  "identity_rules": [
    "Mantener tono institucional UnADM en todo entregable.",
    "Vincular actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Conservar enfoque jurídico-académico con precisión conceptual.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar memorias de modelos previos como provisionales hasta validación local.",
    "No usar trazas de modelo como fuente académica."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir afirmación, evidencia e inferencia en bloques claros.",
    "Cerrar con conclusión jurídica transferible a práctica profesional.",
    "Alinear forma final al producto pedido por la planeación semanal."
  ],
  "activity_rules": [
    "Adaptar el desarrollo al enunciado real de Actividad 5.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entrega solo descriptiva o de resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar fuentes de otras semanas sin confirmar pertinencia."
  ],
  "quality_gates": [
    "Bloquear propagación si salida no es JSON parseable.",
    "Validar esquema mínimo completo antes de guardar.",
    "Confirmar respaldo o supuesto explícito en cada afirmación relevante.",
    "Validar consistencia entre citas en texto y .bib.",
    "Rechazar relaciones con tipo fuera de supports|contrasts|depends_on|develops.",
    "Aplicar revisión manual extra por historial de incidentes de parseo."
  ],
  "latex_rules": [
    "Mantener acentos y codificación española consistentes en .tex y .bib.",
    "No cambiar claves BibTeX ya usadas en .tex.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Verificar nombre canónico real del .bib antes de compilar.",
    "Supuesto: .bib canónico esperado es filosofia-del-derecho.bib hasta confirmación final."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Registrar en .bib solo fuentes realmente citadas.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Tratar filosofia-del-derecho-clean.bib como posible material de otra semana hasta confirmar.",
    "Conservar estabilidad de claves para evitar roturas de compilación."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Aplicar unión y deduplicación sin pérdida semántica.",
    "Preservar reglas útiles previas y agregar solo mejoras verificables.",
    "Transferir patrones, no redacción literal entre actividades hermanas.",
    "Si falta consigna local, propagar plantilla base y abrir preguntas.",
    "Mantener bandera histórica de riesgo por salidas no parseables."
  ],
  "open_questions": [
    "Confirmar enunciado textual de Actividad 5.",
    "Confirmar rúbrica específica de evaluación de Actividad 5.",
    "Confirmar tipo de producto requerido: reporte, presentación o recurso visual.",
    "Confirmar nombre canónico final del archivo .bib de asignatura.",
    "Confirmar si bibliografía de Interpretación jurídica (Semana 7) aplica en Actividad 5."
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
      "Análisis propio con postura.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en entregables con rigor jurídico y utilidad profesional.",
      "Asegurar continuidad editorial entre actividades sin perder especificidad local."
    ],
    "style_markers": [
      "Inicio breve con encuadre del problema.",
      "Secciones funcionales y trazables.",
      "Supuestos explícitos cuando falte dato local.",
      "Cierre con criterio jurídico propio."
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
        "Evidencia verificable",
        "Consistencia cita-.bib",
        "Análisis propio",
        "Conclusión transferible"
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
          "target": "Análisis propio",
          "kind": "supports",
          "justification": "Define tono, rigor y encuadre del argumento."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La validez práctica depende del respaldo trazable."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo válido no hay transferencia confiable."
        },
        {
          "source": "Bibliografía base",
          "target": "Bibliografía específica por actividad",
          "kind": "contrasts",
          "justification": "La base orienta; la específica responde a la consigna local."
        },
        {
          "source": "Consistencia cita-.bib",
          "target": "Calidad editorial",
          "kind": "develops",
          "justification": "Reduce errores y fortalece verificabilidad."
        }
      ],
      "evidence": [
        "README exige identidad UnADM, citas verificables y conclusión jurídica propia.",
        "Programa analítico fija ejes problema-conceptos-fuentes-análisis-cierre.",
        "Historial registra incidentes de salida no parseable; se mantiene gate estructural.",
        "Supuesto: falta consigna local completa de Actividad 5."
      ]
    },
    "reinforcement_log": [
      "Ciclo 36: deduplicación de reglas repetidas y normalización semántica.",
      "Ciclo 36: transferencia lateral limitada a patrones reutilizables.",
      "Ciclo 36: se preservan ejes troncales y controles de calidad previos.",
      "Ciclo 36: se añade validación de tipos permitidos en relaciones del grafo."
    ]
  }
}