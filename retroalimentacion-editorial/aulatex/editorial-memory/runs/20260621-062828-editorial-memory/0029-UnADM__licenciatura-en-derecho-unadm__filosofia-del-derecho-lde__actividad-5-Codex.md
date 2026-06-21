{
  "summary": [
    "Se refuerza memoria lateral de Actividad 5 con patrones reutilizables de Actividad 1.",
    "Se conserva identidad UnADM, encuadre jurídico y ejes editoriales troncales.",
    "Se mantiene normalización obligatoria: no propagar salidas no parseables.",
    "Se aplica deduplicación lossless y se eliminan repeticiones formales.",
    "Supuesto: falta consigna local completa de Actividad 5; se conserva estructura base abierta."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear la actividad con Licenciatura en Derecho y asignatura Filosofía del Derecho.",
    "Usar ubicación curricular: semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Conservar enfoque jurídico-académico con criterio propio.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar memorias de modelos previos como provisionales hasta verificación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en: conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Distinguir afirmación, evidencia e inferencia jurídica en bloques claros.",
    "Alinear el entregable al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a práctica profesional."
  ],
  "activity_rules": [
    "Adaptar el desarrollo al enunciado real de Actividad 5.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar conclusiones específicas de Actividad 1.",
    "No reutilizar bibliografía de otra semana sin confirmar pertinencia."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de guardar o propagar.",
    "Confirmar respaldo o marca de supuesto en cada afirmación relevante.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Rechazar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Aplicar revisión manual extra en memoria con historial de incidentes de parseo."
  ],
  "latex_rules": [
    "Usar acentos y codificación española de forma consistente en .tex y .bib.",
    "Mantener claves BibTeX estables ya usadas en .tex.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Validar nombres reales de archivos cuando README tenga tokens sin expandir.",
    "Resolver tokens tipo $(@{...}.Slug) antes de automatizar rutas.",
    "Supuesto: .bib canónico esperado es filosofia-del-derecho.bib hasta confirmación final."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes jurídicas verificables.",
    "Registrar en .bib solo obras realmente consultables y citadas.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, editorial/fuente o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Tratar filosofia-del-derecho-clean.bib como potencialmente específico de Semana 7 hasta validar pertinencia para Actividad 5."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir solo patrones generales reutilizables entre hermanos.",
    "Evitar copiar redacción literal, conclusiones y bibliografía exclusiva.",
    "Preservar reglas útiles previas y agregar solo mejoras verificables.",
    "Mantener bandera de riesgo histórico por salidas no parseables en ciclos previos."
  ],
  "open_questions": [
    "Confirmar consigna textual completa de Actividad 5.",
    "Confirmar rúbrica de evaluación específica de Actividad 5.",
    "Confirmar formato requerido: reporte, presentación o recurso visual.",
    "Confirmar nombre canónico final del .bib de asignatura.",
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
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos jurídicos consistentes.",
      "Asegurar trazabilidad entre consigna, evidencia y conclusión.",
      "Sostener continuidad editorial institucional entre actividades."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales no ornamentales.",
      "Postura personal sustentada.",
      "Supuestos explícitos cuando falten datos."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> inferencia jurídica.",
      "Contraste doctrinal breve -> toma de postura -> transferencia práctica."
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
          "justification": "Define tono, forma y criterios de integridad académica."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis requiere una pregunta delimitada."
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
          "source": "Bibliografía base",
          "target": "Bibliografía específica de actividad",
          "kind": "contrasts",
          "justification": "La base orienta; la específica responde a consigna local."
        }
      ],
      "evidence": [
        "README establece identidad UnADM, integridad académica y conclusión jurídica propia.",
        "Programa analítico fija ejes problema-conceptos-fuentes-análisis-cierre.",
        "Historial confirma gate obligatorio por incidentes de parseo JSON.",
        "README y programa muestran tokens Slug sin expandir; requiere validación de rutas."
      ]
    },
    "reinforcement_log": [
      "Se consolidaron reglas duplicadas por unión y deduplicación.",
      "Se preservaron ejes troncales heredados sin recorte semántico.",
      "Se añadió control explícito de transferencia entre nodos hermano.",
      "Se mantuvo separación entre patrones reutilizables y contenido específico no transferible."
    ]
  }
}