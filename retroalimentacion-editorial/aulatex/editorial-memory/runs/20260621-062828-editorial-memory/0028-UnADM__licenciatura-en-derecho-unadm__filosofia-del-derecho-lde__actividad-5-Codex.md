{
  "summary": [
    "Se consolida memoria lateral de Actividad 5 con deduplicación lossless y sin recorte útil.",
    "Se preserva identidad UnADM y ubicación curricular: Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Se refuerzan ejes troncales reutilizables: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se mantiene control estricto de normalización JSON antes de propagación recursiva.",
    "Se mantiene separación entre bibliografía base de asignatura y bibliografía específica por actividad.",
    "Se evita transferir conclusiones específicas o bibliografía exclusiva de Actividad 1 hacia Actividad 5."
  ],
  "identity_rules": [
    "Mantener tono formal académico y precisión jurídica.",
    "Alinear toda pieza con identidad institucional UnADM.",
    "Vincular explícitamente la actividad a Licenciatura en Derecho y Filosofía del Derecho.",
    "Usar carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar memoria de modelos previos como fuente provisional no académica."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir afirmación, evidencia e inferencia jurídica en bloques claros.",
    "Cerrar con conclusión jurídica transferible a práctica profesional.",
    "Alinear el producto al formato exigido por la planeación semanal."
  ],
  "activity_rules": [
    "Adaptar contenido al enunciado real de Actividad 5.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entrega solo descriptiva o de resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar bibliografía de otras semanas sin confirmar pertinencia."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de reutilizar.",
    "Confirmar respaldo o marca de supuesto en afirmaciones relevantes.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar manualmente memoria con historial de incidentes de parseo.",
    "Verificar que el producto responda a la consigna y no solo a ejes genéricos."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables ya citadas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: .bib canónico esperado: filosofia-del-derecho.bib; confirmar localmente."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Registrar en .bib solo fuentes realmente citadas.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de asignatura vs bibliografía específica de actividad.",
    "Tratar filosofia-del-derecho-clean.bib como probable insumo de Semana 7 hasta confirmar pertinencia para Actividad 5."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir solo patrones reutilizables, no redacción literal ni cierres específicos.",
    "Conservar reglas útiles previas y agregar solo mejoras verificables.",
    "Aplicar unión y deduplicación semántica en ciclos siguientes.",
    "Mantener bandera de riesgo por salidas históricas no parseables.",
    "Cuando falte consigna local, propagar plantilla base y preguntas abiertas."
  ],
  "open_questions": [
    "Confirmar enunciado exacto de Actividad 5.",
    "Confirmar rúbrica de evaluación específica de Actividad 5.",
    "Confirmar formato requerido: reporte, presentación o recurso visual.",
    "Confirmar nombre canónico final del .bib de asignatura.",
    "Confirmar si la bibliografía de Interpretación jurídica (Semana 7) aplica a Actividad 5.",
    "Supuesto: el contexto curricular heredado de Actividad 1 se mantiene para Actividad 5."
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
      "Evidencia verificable y trazable.",
      "Análisis propio con inferencia jurídica.",
      "Conclusión transferible a práctica profesional."
    ],
    "reason_for_being": [
      "Convertir la planeación semanal en entregables jurídicos sólidos.",
      "Asegurar coherencia entre consigna, desarrollo, evidencia y cierre.",
      "Sostener continuidad editorial entre actividades hermanas sin contaminación específica."
    ],
    "style_markers": [
      "Inicio con encuadre breve.",
      "Secciones funcionales y trazables.",
      "Postura propia sustentada.",
      "Supuestos explícitos cuando falte dato local.",
      "Cierre jurídico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> inferencia jurídica.",
      "Contraste doctrinal breve -> toma de postura.",
      "Cierre con transferencia profesional."
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
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib",
        "malla-curricular-derecho-unadm.pdf"
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
          "justification": "El análisis requiere una pregunta jurídica delimitada."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión válida exige respaldo trazable."
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
          "justification": "La base orienta la asignatura; la específica responde a la consigna local."
        }
      ],
      "evidence": [
        "README: pauta editorial e identidad institucional.",
        "Programa analítico: ejes de trabajo y propósito de realización.",
        "Historial de ciclos: incidentes de parseo y necesidad de normalización previa.",
        "Regla de transferencia actual: solo patrones reutilizables entre nodos hermanos."
      ]
    },
    "reinforcement_log": [
      "Ciclo 28: se deduplican reglas repetidas en destino sin perder contenido útil.",
      "Ciclo 28: se preserva gate crítico de JSON parseable para propagación.",
      "Ciclo 28: se refuerza separación entre bibliografía base y específica.",
      "Ciclo 28: se mantiene política de supuestos explícitos por falta de consigna local.",
      "Ciclo 28: se evita copiar conclusiones o bibliografía exclusiva de Actividad 1."
    ]
  }
}