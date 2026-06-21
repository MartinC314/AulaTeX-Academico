{
  "summary": [
    "Se consolida refuerzo lateral entre actividades hermanas sin copiar contenido específico.",
    "Se preserva identidad UnADM y marco curricular de Filosofía del Derecho.",
    "Se mantiene normalización obligatoria: no propagar sin JSON parseable y estructura completa.",
    "Se fijan ejes reutilizables: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se conserva distinción entre bibliografía base y bibliografía específica por actividad.",
    "Supuesto: falta consigna local de Actividad 5; se aplica estructura base con preguntas abiertas."
  ],
  "identity_rules": [
    "Mantener tono formal académico con precisión jurídica.",
    "Alinear toda salida con UnADM y Licenciatura en Derecho.",
    "Conservar referencia curricular: semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas de modelos como provisionales hasta verificación local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Distinguir afirmación, evidencia e inferencia jurídica.",
    "Cerrar con conclusión jurídica transferible a práctica profesional.",
    "Alinear formato final al producto pedido por planeación semanal."
  ],
  "activity_rules": [
    "Adaptar el entregable al enunciado real de Actividad 5.",
    "Evitar entregas solo descriptivas; incluir postura argumentada del estudiante.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar conclusiones específicas desde actividades hermanas.",
    "No reutilizar bibliografía de otra semana sin confirmar pertinencia."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en afirmaciones relevantes.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Comprobar correspondencia entre producto entregado y consigna local.",
    "Aplicar revisión manual extra en memoria con incidentes previos de parseo."
  ],
  "latex_rules": [
    "Usar acentos y codificación en español de forma consistente en .tex y .bib.",
    "Mantener claves BibTeX estables ya citadas en .tex.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Validar nombres reales de archivos cuando README tenga tokens sin expandir.",
    "Resolver marcadores tipo $(@{...}.Slug) antes de automatizar rutas."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Registrar en .bib solo fuentes realmente citadas.",
    "No inventar referencias ni metadatos.",
    "Mantener metadatos mínimos: autor, título, año, editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Tratar filosofia-del-derecho-clean.bib como potencialmente temático de otra semana hasta confirmar pertinencia."
  ],
  "propagation_hints": [
    "Propagar solo patrones reutilizables de identidad, estructura y calidad.",
    "No transferir redacción literal ni conclusiones concretas entre hermanos.",
    "No transferir bibliografía exclusiva sin validación local.",
    "Preservar reglas útiles previas y agregar solo mejoras verificables.",
    "Aplicar deduplicación semántica sin pérdida de reglas vigentes.",
    "Mantener bandera histórica de riesgo por salidas no parseables."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 5.",
    "Confirmar rúbrica y criterios de evaluación específicos.",
    "Confirmar tipo de producto requerido: reporte, presentación o recurso visual.",
    "Confirmar nombre canónico final del .bib de la asignatura.",
    "Confirmar si fuentes de Semana 7 aplican a Actividad 5 o no."
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
      "Convertir planeación semanal en entregables académicos sólidos.",
      "Asegurar trazabilidad entre consigna, desarrollo y cierre argumentativo.",
      "Garantizar consistencia técnica, jurídica y editorial en LaTeX."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales.",
      "Supuestos explícitos cuando falten datos.",
      "Cierre con utilidad profesional.",
      "Sin relleno ni ambigüedad argumentativa."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> inferencia jurídica.",
      "Contraste doctrinal breve -> postura propia.",
      "Conclusión -> transferencia a práctica profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalización JSON",
        "Ejes editoriales troncales",
        "Consistencia cita-.bib",
        "Supuestos explícitos",
        "Pertinencia bibliográfica por actividad"
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
          "target": "Ejes editoriales troncales",
          "kind": "supports",
          "justification": "Define tono, rigor y finalidad del entregable."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo válido no hay transferencia confiable."
        },
        {
          "source": "Consistencia cita-.bib",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión exige respaldo verificable."
        },
        {
          "source": "Pertinencia bibliográfica por actividad",
          "target": "No copiar bibliografía exclusiva entre hermanos",
          "kind": "contrasts",
          "justification": "Reusar solo cuando la consigna local lo justifique."
        },
        {
          "source": "Supuestos explícitos",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Evita invención de datos no confirmados."
        }
      ],
      "evidence": [
        "README fija identidad UnADM, integridad académica y conclusión jurídica propia.",
        "Programa analítico fija ejes problema-conceptos-fuentes-análisis-cierre.",
        "Historial registra incidentes de salida no parseable y exige gate técnico.",
        "Bibliografía clean indica foco de Semana 7 y requiere validación de pertinencia."
      ]
    },
    "reinforcement_log": [
      "Ciclo 68: deduplicación lossless aplicada sobre reglas repetidas.",
      "Ciclo 68: se refuerza transferencia lateral por patrones, no por contenido literal.",
      "Ciclo 68: se mantiene guardia de parseo JSON como condición de propagación.",
      "Ciclo 68: se preserva separación entre bibliografía base y específica de actividad."
    ]
  }
}