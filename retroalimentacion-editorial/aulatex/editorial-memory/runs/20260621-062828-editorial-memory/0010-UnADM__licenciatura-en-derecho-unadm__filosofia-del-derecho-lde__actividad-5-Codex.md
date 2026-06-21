{
  "summary": [
    "Memoria lateral consolidada para Actividad 5 con deduplicación lossless.",
    "Se preserva identidad UnADM y contexto curricular de Filosofía del Derecho.",
    "Se refuerzan ejes troncales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se mantiene gate crítico: no propagar sin JSON parseable y estructura mínima completa.",
    "Se conserva regla de tratar fuentes heredadas de modelos como provisionales.",
    "Supuesto: falta consigna y rúbrica local de Actividad 5; se mantiene plantilla base verificable."
  ],
  "identity_rules": [
    "Mantener tono formal académico y precisión jurídica.",
    "Alinear toda entrega con UnADM y Licenciatura en Derecho.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Conservar encuadre curricular: semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar memorias de modelos previos como insumo provisional no académico."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Separar afirmaciones, evidencia e inferencia jurídica de forma explícita.",
    "Alinear el formato final al producto pedido por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a práctica profesional."
  ],
  "activity_rules": [
    "Adaptar el desarrollo al enunciado real de Actividad 5 cuando esté disponible.",
    "Incluir postura argumentada del estudiante y evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar conclusiones específicas de actividades hermanas.",
    "No reutilizar bibliografía de otra semana sin confirmar pertinencia."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar esquema completo antes de guardar o propagar.",
    "Confirmar respaldo o marca de supuesto en afirmaciones críticas.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Rechazar contradicciones con reglas institucionales vigentes.",
    "Aplicar revisión manual extra por historial de incidentes de parseo."
  ],
  "latex_rules": [
    "Mantener compatibilidad con .tex y .bib canónicos de la asignatura.",
    "No cambiar claves BibTeX ya citadas sin migración controlada.",
    "Usar acentos y codificación en español de forma consistente.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens sin expandir en README y programa analítico antes de compilar.",
    "Supuesto: nombre canónico esperado del .bib es filosofia-del-derecho.bib."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Agregar al .bib solo fuentes efectivamente citadas.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a Semana 7 y requiere validación para Actividad 5."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas reutilizables y verificadas.",
    "Preservar reglas útiles previas y agregar solo mejoras comprobables.",
    "Evitar copia literal de redacción y conclusiones entre hermanos.",
    "Transferir patrones de identidad, estructura y calidad; no contenido específico.",
    "Mantener bandera de riesgo por parseo histórico en ciclos previos.",
    "Si falta dato local, propagar pregunta abierta y no contenido inventado."
  ],
  "open_questions": [
    "Confirmar enunciado oficial de Actividad 5.",
    "Confirmar rúbrica de evaluación de Actividad 5.",
    "Confirmar tipo de entregable requerido: reporte, presentación o recurso visual.",
    "Confirmar archivo .bib canónico definitivo en la carpeta.",
    "Confirmar pertinencia de bibliografía de Semana 7 para Actividad 5.",
    "Confirmar corrección de rutas con tokens sin expandir en README."
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
      "Problema jurídico como punto de partida.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable con cita trazable.",
      "Análisis propio del estudiante.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos.",
      "Asegurar coherencia entre consigna, desarrollo y cierre.",
      "Sostener calidad institucional en cada actividad."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales sin relleno.",
      "Distinción explícita entre afirmación y evidencia.",
      "Postura personal fundamentada.",
      "Marcado explícito de supuestos."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> inferencia jurídica.",
      "Contraste doctrinal breve -> toma de postura.",
      "Cierre con transferencia a práctica profesional."
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
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Estructura de actividad",
          "kind": "supports",
          "justification": "Define tono, formato y criterios de integridad."
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
          "justification": "La conclusión jurídica válida necesita respaldo trazable."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia confiable."
        },
        {
          "source": "Bibliografía específica de actividad",
          "target": "Bibliografía base",
          "kind": "contrasts",
          "justification": "La base orienta; la específica responde a la consigna local."
        }
      ],
      "evidence": [
        "README fija identidad UnADM, integridad y conclusión jurídica propia.",
        "Programa analítico fija ejes problema-conceptos-fuentes-análisis-cierre.",
        "Historial reporta incidentes de salida no parseable y exige gate estructural."
      ]
    },
    "reinforcement_log": [
      "Ciclo 10: deduplicación integral sin pérdida semántica.",
      "Ciclo 10: se reforzó transferencia lateral por patrones, no por contenido específico.",
      "Ciclo 10: se mantuvo regla estricta de normalización JSON previa a propagación.",
      "Ciclo 10: se preservó separación entre bibliografía base y bibliografía por actividad."
    ]
  }
}