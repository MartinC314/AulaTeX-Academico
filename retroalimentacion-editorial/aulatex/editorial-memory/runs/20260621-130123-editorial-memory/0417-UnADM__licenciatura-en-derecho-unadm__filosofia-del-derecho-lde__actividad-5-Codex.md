{
  "summary": [
    "Se refuerza Actividad 5 con patrones reutilizables de Actividad 1 sin copiar contenido específico.",
    "Se conserva identidad UnADM y marco curricular de Derecho como regla estable.",
    "Se mantiene gate crítico: no propagar nada no JSON parseable.",
    "Se consolida eje editorial troncal: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se marca como supuesto toda ausencia de consigna local de Actividad 5."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y encuadre.",
    "Vincular explícitamente la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Conservar enfoque jurídico-académico con criterio propio.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar fuentes heredadas de modelos como provisionales hasta verificación local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Distinguir en cada sección: afirmación, evidencia, inferencia.",
    "Cerrar con conclusión jurídica transferible a práctica profesional.",
    "Alinear el entregable al producto pedido por la planeación semanal."
  ],
  "activity_rules": [
    "Adaptar contenido al enunciado real de Actividad 5.",
    "Evitar entregas solo descriptivas.",
    "Incluir postura argumentada del estudiante.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar conclusiones ni bibliografía exclusiva de otra actividad sin pertinencia confirmada."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en afirmaciones relevantes.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que el producto responda a la consigna local de Actividad 5.",
    "Aplicar revisión manual extra si hay historial de parseo defectuoso."
  ],
  "latex_rules": [
    "Usar acentos y codificación en español de forma consistente en .tex y .bib.",
    "Mantener claves BibTeX estables ya citadas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver tokens sin expandir en README o programa antes de fijar nombres de archivo.",
    "Supuesto: el .bib canónico esperado es filosofia-del-derecho.bib, pendiente de confirmación local."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Registrar en .bib solo fuentes realmente citadas.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Tratar filosofia-del-derecho-clean.bib como potencialmente temático de otra semana hasta validar pertinencia para Actividad 5."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir solo patrones reutilizables, no redacciones literales.",
    "Preservar reglas útiles previas y agregar solo mejoras verificables.",
    "Mantener bandera de riesgo histórico por salidas no parseables.",
    "Cuando falte consigna local, propagar estructura base y preguntas abiertas."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 5; confirmar producto exacto solicitado.",
    "Confirmar rúbrica específica de evaluación de Actividad 5.",
    "Confirmar si el entregable es reporte, presentación o recurso visual.",
    "Confirmar nombre canónico final del archivo .bib de la asignatura.",
    "Confirmar si la bibliografía de Interpretación jurídica (Semana 7) aplica a Actividad 5."
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
      "Conceptos y marco normativo pertinente.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en entregables jurídicos sólidos.",
      "Asegurar trazabilidad entre consigna, evidencia y conclusión.",
      "Sostener continuidad editorial institucional entre actividades hermanas."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Secciones funcionales y explícitas.",
      "Inferencias jurídicas visibles.",
      "Supuestos marcados cuando falte información."
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
          "justification": "La pauta institucional fija tono, integridad y forma."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis requiere conflicto delimitado."
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
          "source": "Bibliografía base",
          "target": "Bibliografía específica de actividad",
          "kind": "contrasts",
          "justification": "La base orienta; la específica responde a la consigna local."
        }
      ],
      "evidence": [
        "README: identidad UnADM, citas verificables y conclusión jurídica.",
        "Programa analítico: eje problema-conceptos-fuentes-análisis-cierre.",
        "Historial: incidentes de salida no parseable obligan gate estricto."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin pérdida semántica.",
      "Se eliminó arrastre literal de contenido específico de Actividad 1.",
      "Se reforzó distinción entre patrones transferibles y contenido local.",
      "Se conservaron controles de calidad y parseo como núcleo persistente."
    ]
  }
}