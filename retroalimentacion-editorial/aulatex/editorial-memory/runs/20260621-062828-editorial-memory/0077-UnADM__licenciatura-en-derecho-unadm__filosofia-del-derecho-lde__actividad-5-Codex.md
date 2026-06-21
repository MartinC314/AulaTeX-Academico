{
  "summary": [
    "Se consolida memoria lateral para Actividad 5 con deduplicación lossless y sin recorte de reglas útiles.",
    "Se preserva identidad UnADM y ubicación curricular: Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Se refuerza la regla de normalización: no propagar contenido no JSON parseable.",
    "Se mantienen ejes editoriales troncales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se limita la transferencia a patrones reutilizables; no se copian conclusiones ni bibliografía exclusiva de actividad hermana."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y encuadre.",
    "Alinear la actividad a Licenciatura en Derecho y asignatura Filosofía del Derecho.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Sostener enfoque jurídico-académico con criterio propio.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas de modelos como provisionales hasta validación local.",
    "Referenciar malla curricular institucional para ubicación curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir explícitamente afirmación, evidencia e inferencia.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Alinear la estructura al producto solicitado en la planeación semanal.",
    "Validar estructura JSON parseable antes de guardar o propagar."
  ],
  "activity_rules": [
    "Adaptar el entregable al enunciado real de Actividad 5.",
    "Incluir postura argumentada del estudiante; evitar resumen meramente descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar bibliografía de otra semana sin confirmar pertinencia.",
    "Registrar supuesto operativo cuando falte alcance o rúbrica."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar integridad de esquema mínimo completo antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en afirmaciones clave.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Rechazar contradicciones con reglas institucionales vigentes.",
    "Aplicar revisión manual extra a memoria con historial de incidentes de parseo."
  ],
  "latex_rules": [
    "Usar acentos y codificación en español de forma consistente en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Validar nombre canónico del .bib antes de compilar.",
    "Supuesto: .bib canónico esperado es filosofia-del-derecho.bib, pendiente confirmación local."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes jurídicas verificables.",
    "Registrar en .bib solo fuentes realmente citadas.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Tratar filosofia-del-derecho-clean.bib como potencialmente temática de Semana 7 hasta confirmar pertinencia para Actividad 5.",
    "Conservar claves ya usadas en .tex cuando correspondan a fuentes válidas."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir solo patrones reutilizables de identidad, estructura, calidad y relaciones conceptuales.",
    "Evitar copiar redacción literal, conclusiones específicas o bibliografía exclusiva del nodo hermano.",
    "Aplicar unión y deduplicación sin regresión de reglas útiles.",
    "Mantener bandera de riesgo histórico por incidentes de parseo en ciclos previos."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 5; confirmar producto exacto solicitado.",
    "Confirmar rúbrica de evaluación específica de Actividad 5.",
    "Confirmar si el formato requerido es reporte, presentación o recurso visual.",
    "Confirmar nombre canónico final del archivo .bib de la asignatura.",
    "Confirmar pertinencia de bibliografía de Interpretación jurídica (Semana 7) para Actividad 5."
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
      "Análisis propio con postura.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir la planeación semanal en productos académicos sólidos.",
      "Asegurar consistencia institucional, metodológica y argumentativa.",
      "Garantizar trazabilidad entre consigna, desarrollo y cierre jurídico."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones funcionales y explícitas.",
      "Supuestos etiquetados cuando falte información.",
      "Cierre con utilidad profesional."
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
          "justification": "Define tono, forma y criterio académico del entregable."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis requiere un conflicto o pregunta delimitada."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica válida depende de respaldo trazable."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo correcto no hay transferencia confiable."
        },
        {
          "source": "Bibliografía específica de actividad",
          "target": "Bibliografía base",
          "kind": "contrasts",
          "justification": "La base orienta el curso; la específica responde a la consigna puntual."
        }
      ],
      "evidence": [
        "README fija identidad UnADM, integridad académica y conclusión jurídica propia.",
        "Programa analítico fija ejes problema-conceptos-fuentes-análisis-cierre.",
        "Historial de ciclos previos reporta incidentes de salida no parseable.",
        "README y programa muestran token Slug sin expandir en nombre de .bib."
      ]
    },
    "reinforcement_log": [
      "Ciclo 77: deduplicación integral de reglas repetidas en destino.",
      "Ciclo 77: preservación de reglas institucionales y gates de calidad sin recorte.",
      "Ciclo 77: transferencia lateral controlada solo de patrones reutilizables.",
      "Ciclo 77: se mantiene separación entre bibliografía base y específica.",
      "Ciclo 77: se consolidan preguntas abiertas por falta de consigna local verificable."
    ]
  }
}