{
  "summary": [
    "Se consolida refuerzo lateral desde Actividad 1 hacia Actividad 5 con deduplicación lossless.",
    "Se preserva identidad UnADM y marco curricular de Derecho sin copiar contenido específico entre hermanos.",
    "Se mantienen ejes editoriales troncales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se refuerza control de normalización JSON y trazabilidad antes de propagación recursiva.",
    "Supuesto: falta consigna local completa de Actividad 5; se conserva estructura base y preguntas abiertas."
  ],
  "identity_rules": [
    "Mantener tono institucional UnADM, formal y jurídico-académico.",
    "Vincular toda entrega a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar memorias de modelos previos como provisionales hasta verificación local.",
    "No usar trazas de modelos como fuente académica."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Separar explícitamente afirmación, evidencia e inferencia.",
    "Cerrar con conclusión jurídica transferible a práctica profesional.",
    "Alinear formato final al producto pedido por la planeación semanal."
  ],
  "activity_rules": [
    "Adaptar el desarrollo al enunciado real de Actividad 5.",
    "Incluir postura argumentada del estudiante; evitar resumen descriptivo puro.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar bibliografía de otra semana sin confirmar pertinencia.",
    "Si falta instrucción, registrar supuesto operativo y continuar con consistencia."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de guardar o propagar.",
    "Confirmar respaldo o marca de supuesto en afirmaciones clave.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Rechazar contradicciones con reglas institucionales vigentes.",
    "Aplicar revisión manual extra en memoria con historial de parseo defectuoso."
  ],
  "latex_rules": [
    "Mantener codificación y acentos correctos en .tex y .bib.",
    "Conservar claves BibTeX estables ya usadas en .tex.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver tokens sin expandir en README y programa analítico antes de referenciar archivos.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib; confirmar localmente."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Registrar en .bib solo fuentes realmente citadas en el texto.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Tratar filosofia-del-derecho-clean.bib como potencialmente temático de otra semana hasta confirmar pertinencia."
  ],
  "propagation_hints": [
    "Propagar solo patrones reutilizables: identidad, estructura, calidad y relaciones conceptuales.",
    "No propagar conclusiones concretas ni bibliografía exclusiva entre actividades hermanas.",
    "Aplicar unión y deduplicación sin recorte semántico.",
    "Preservar reglas útiles previas y añadir solo mejoras verificables.",
    "Mantener bandera de riesgo por incidentes históricos de salida no parseable.",
    "Si falta consigna local, propagar plantilla estructural y preguntas abiertas."
  ],
  "open_questions": [
    "Confirmar consigna textual completa de Actividad 5.",
    "Confirmar rúbrica específica de evaluación para Actividad 5.",
    "Confirmar formato exigido: reporte, presentación o recurso visual.",
    "Confirmar nombre canónico final del .bib de la asignatura.",
    "Confirmar si bibliografía de Interpretación jurídica (Semana 7) aplica o no a Actividad 5."
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
      "Convertir planeación semanal en productos académicos sólidos.",
      "Garantizar continuidad editorial entre actividades sin contaminación de contenido específico.",
      "Asegurar calidad formal, argumentativa y técnica en ecosistema LaTeX."
    ],
    "style_markers": [
      "Inicio con encuadre breve.",
      "Secciones funcionales y explícitas.",
      "Supuestos declarados cuando falte información.",
      "Cierre con utilidad jurídica práctica."
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
        "Bibliografía base",
        "Bibliografía específica de actividad"
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
          "justification": "El marco institucional fija tono, forma y criterios mínimos."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "Sin problema delimitado no hay análisis argumentativo consistente."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica requiere sustento trazable."
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
          "justification": "La base orienta la asignatura; la específica responde la consigna puntual."
        }
      ],
      "evidence": [
        "README define identidad UnADM, citas verificables y conclusión jurídica propia.",
        "Programa analítico define ejes problema-conceptos-fuentes-análisis-cierre.",
        "Historial registra incidentes de salida no parseable y exige gate de estructura."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas preservando contenido útil.",
      "Se reforzó separación entre patrones transferibles y contenido específico de hermano.",
      "Se mantuvo control estricto de JSON parseable como condición de propagación.",
      "Se conservó política de supuestos explícitos ante falta de consigna local."
    ]
  }
}