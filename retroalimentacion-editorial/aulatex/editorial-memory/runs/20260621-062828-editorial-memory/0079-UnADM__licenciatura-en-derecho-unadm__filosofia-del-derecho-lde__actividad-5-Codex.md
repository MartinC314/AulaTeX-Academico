{
  "summary": [
    "Se consolida refuerzo lateral para Actividad 5 con deduplicación lossless.",
    "Se preserva identidad UnADM y ubicación curricular: Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Se mantiene normalización JSON obligatoria antes de propagación recursiva.",
    "Se refuerzan ejes troncales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se transfiere solo patrón reutilizable desde Actividad 1; no se copian conclusiones ni bibliografía exclusiva."
  ],
  "identity_rules": [
    "Mantener tono formal académico y precisión jurídica.",
    "Alinear toda entrega con identidad institucional UnADM.",
    "Vincular explícitamente la actividad a Licenciatura en Derecho y Filosofía del Derecho.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas de modelos como provisionales, no académicas."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar bloques: conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Distinguir afirmación, evidencia e inferencia en cada tramo argumental.",
    "Alinear el entregable al producto pedido por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a práctica profesional."
  ],
  "activity_rules": [
    "Adaptar el desarrollo al enunciado real de Actividad 5.",
    "Incluir postura argumentada del estudiante; evitar resumen descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar bibliografía de otra semana sin confirmar pertinencia.",
    "Si falta dato operativo, registrar supuesto y continuar con consistencia."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de reutilizar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en afirmaciones relevantes.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar manualmente memoria afectada por incidentes previos de parseo.",
    "Rechazar contenido que contradiga reglas institucionales vigentes."
  ],
  "latex_rules": [
    "Usar acentos y codificación española consistentes en .tex y .bib.",
    "Mantener claves BibTeX estables ya citadas en .tex.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Corregir tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: .bib canónico esperado es filosofia-del-derecho.bib hasta confirmación local."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Registrar en .bib solo fuentes realmente citadas.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Tratar filosofia-del-derecho-clean.bib como potencialmente de otra semana hasta confirmar pertinencia."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Preservar reglas útiles previas; agregar solo mejoras verificables.",
    "Aplicar unión y deduplicación sin recorte semántico.",
    "No propagar como académicas fuentes de trazabilidad de modelo.",
    "Cuando falte consigna local, propagar plantilla base y preguntas abiertas.",
    "Mantener bandera de riesgo histórico por salidas no parseables en ciclos previos."
  ],
  "open_questions": [
    "Supuesto: falta enunciado textual de Actividad 5; confirmar producto exacto solicitado.",
    "Confirmar rúbrica específica para ajustar profundidad argumentativa.",
    "Confirmar si Actividad 5 exige reporte, presentación o recurso visual.",
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
      "Problema jurídico o social delimitado.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable y trazable.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir la planeación semanal en productos académicos sólidos.",
      "Sostener continuidad editorial entre actividades hermanas.",
      "Asegurar calidad formal, argumentativa y técnica en LaTeX."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones funcionales y explícitas.",
      "Inferencias jurídicas justificadas.",
      "Uso explícito de supuestos cuando falte información."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> inferencia jurídica.",
      "Contraste doctrinal breve -> toma de postura.",
      "Cierre con aplicabilidad profesional."
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
          "justification": "Define tono, forma y criterio de integridad académica."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis requiere una pregunta o conflicto delimitado."
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
          "justification": "La base orienta el curso; la específica responde a la consigna."
        },
        {
          "source": "Ejes troncales",
          "target": "Actividad 5",
          "kind": "develops",
          "justification": "Se refuerzan por analogía controlada entre nodos hermanos."
        }
      ],
      "evidence": [
        "README exige identidad UnADM, citas verificables y conclusión jurídica propia.",
        "Programa analítico fija ejes problema-conceptos-fuentes-análisis-cierre.",
        "Historial reporta incidentes de salida no parseable; se mantiene gate técnico."
      ]
    },
    "reinforcement_log": [
      "Ciclo 79: deduplicación integral de reglas repetidas en destino.",
      "Ciclo 79: se preservaron reglas válidas previas sin recorte útil.",
      "Ciclo 79: se añadió restricción explícita de transferencia entre hermanos.",
      "Ciclo 79: se mantuvo separación entre bibliografía base y específica.",
      "Ciclo 79: se reforzó control de supuestos por falta de consigna local."
    ]
  }
}