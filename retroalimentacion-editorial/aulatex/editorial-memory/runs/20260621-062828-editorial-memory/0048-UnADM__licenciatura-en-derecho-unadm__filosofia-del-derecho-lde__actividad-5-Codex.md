{
  "summary": [
    "Se refuerza memoria lateral de Actividad 5 con patrones reutilizables de Actividad 1.",
    "Se conserva identidad UnADM y ubicación curricular oficial sin cambios.",
    "Se mantiene compresión lossless por unión y deduplicación semántica.",
    "Se preserva gate crítico: no propagar si JSON no es parseable.",
    "Se evita transferir conclusiones específicas o bibliografía exclusiva de un hermano a otro.",
    "Supuesto: falta consigna textual y rúbrica local de Actividad 5."
  ],
  "identity_rules": [
    "Mantener tono institucional UnADM, formal y jurídico-académico.",
    "Vincular siempre a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar carpeta de asignatura como entrada canónica de decisión editorial.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar memoria de modelos previos como provisional hasta verificación local.",
    "No usar trazas de modelo como fuente académica."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir bloques de afirmación, evidencia e inferencia.",
    "Alinear secciones al producto real pedido por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a práctica profesional."
  ],
  "activity_rules": [
    "Adaptar el entregable al enunciado real de Actividad 5.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Evitar arrastre automático de bibliografía de otras semanas.",
    "Si falta alcance, registrar supuesto operativo y continuar con consistencia."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar esquema mínimo completo antes de guardar o propagar.",
    "Confirmar respaldo o marca de supuesto en cada afirmación relevante.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar manualmente memoria con historial de incidentes de parseo.",
    "Verificar que el producto responda a la consigna y no solo a una plantilla."
  ],
  "latex_rules": [
    "Usar español con acentos y codificación consistente en .tex y .bib.",
    "Mantener claves BibTeX estables ya citadas en .tex.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib hasta confirmación local."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Agregar al .bib solo fuentes realmente citadas.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib está orientado a Semana 7 y requiere validación de pertinencia para Actividad 5."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validación de JSON y estructura.",
    "Transferir solo patrones reutilizables, no redacción literal entre hermanos.",
    "Preservar reglas útiles previas y añadir solo mejoras verificables.",
    "Aplicar unión-dedupe para evitar regresiones y duplicados.",
    "Mantener bandera de riesgo histórico por salidas no parseables previas.",
    "Si falta dato local, propagar estructura base y preguntas abiertas."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 5.",
    "Confirmar rúbrica de evaluación de Actividad 5.",
    "Confirmar tipo de producto principal: reporte, presentación o recurso visual.",
    "Confirmar nombre canónico final del .bib de la asignatura.",
    "Confirmar si la bibliografía de Semana 7 aplica total, parcial o nada a Actividad 5."
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
      "Problema jurídico o social delimitado.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable con trazabilidad.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir la planeación semanal en productos académicos sólidos.",
      "Asegurar continuidad editorial entre actividades sin copiar contenido específico.",
      "Garantizar calidad estructural y argumentativa antes de propagación."
    ],
    "style_markers": [
      "Inicio breve y focalizado.",
      "Secciones funcionales, no ornamentales.",
      "Inferencias explícitas desde evidencia.",
      "Supuestos declarados cuando falte información.",
      "Cierre con aplicabilidad jurídica."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> inferencia jurídica.",
      "Contraste doctrinal breve -> toma de postura.",
      "Conclusión -> transferencia a práctica profesional."
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
        "Supuestos explícitos"
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
          "justification": "Define tono, forma y criterio de integridad académica."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "Sin delimitación del problema no hay análisis jurídico consistente."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La validez práctica de la conclusión depende del respaldo trazable."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "La transferencia confiable exige estructura parseable."
        },
        {
          "source": "Bibliografía base",
          "target": "Bibliografía específica de actividad",
          "kind": "contrasts",
          "justification": "La base orienta; la específica responde a la consigna concreta."
        },
        {
          "source": "Supuestos explícitos",
          "target": "Control de calidad",
          "kind": "supports",
          "justification": "Evitan afirmaciones no verificadas cuando faltan datos locales."
        }
      ],
      "evidence": [
        "README fija identidad UnADM, integridad académica y conclusión jurídica propia.",
        "Programa analítico fija ejes: problema, conceptos, fuentes, análisis, cierre.",
        "Historial de parseo obliga gate estricto de JSON antes de propagar.",
        "README y programa muestran token Slug sin expandir; requiere normalización de nombres."
      ]
    },
    "reinforcement_log": [
      "Ciclo 48: deduplicación completa de reglas repetidas en destino.",
      "Ciclo 48: refuerzo lateral de estructura argumentativa reusable sin copiar contenido hermano.",
      "Ciclo 48: conservación explícita de guardas JSON y trazabilidad cita-.bib.",
      "Ciclo 48: incorporación de regla de supuestos explícitos como seguro editorial.",
      "Ciclo 48: mantenimiento de incertidumbres abiertas por falta de consigna local."
    ]
  }
}