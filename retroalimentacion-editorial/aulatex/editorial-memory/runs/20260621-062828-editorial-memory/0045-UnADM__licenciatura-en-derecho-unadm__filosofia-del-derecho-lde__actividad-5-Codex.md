{
  "summary": [
    "Se refuerza continuidad editorial entre actividades hermanas sin copiar contenido específico.",
    "Se preservan reglas troncales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se mantiene control estricto de normalización JSON antes de propagación recursiva.",
    "Se conserva identidad UnADM y ubicación curricular verificable desde README y programa analítico.",
    "Supuesto: falta consigna local completa de Actividad 5; se mantiene estructura base reusable."
  ],
  "identity_rules": [
    "Mantener tono formal académico y precisión jurídica.",
    "Alinear toda entrega a UnADM, Licenciatura en Derecho, Filosofía del Derecho.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar memorias de modelos previos como provisionales hasta verificación local.",
    "No usar trazas de modelos como fuente académica."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir afirmaciones, evidencia e inferencia jurídica.",
    "Cerrar con conclusión transferible a práctica profesional.",
    "Alinear formato final al producto solicitado por la planeación semanal."
  ],
  "activity_rules": [
    "Adaptar el entregable al enunciado real de Actividad 5.",
    "Evitar redacción meramente descriptiva.",
    "Incluir postura argumentada del estudiante.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "No arrastrar bibliografía de otra semana sin confirmar pertinencia."
  ],
  "quality_gates": [
    "Bloquear propagación si no hay JSON parseable.",
    "Validar esquema mínimo completo antes de guardar.",
    "Confirmar respaldo o marca de supuesto en afirmaciones relevantes.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar manualmente memoria con historial de incidentes de parseo.",
    "Rechazar relaciones o reglas con tipos no permitidos."
  ],
  "latex_rules": [
    "Usar acentos y codificación en español de forma consistente.",
    "Conservar claves BibTeX ya citadas para evitar rupturas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Corregir tokens sin expandir en rutas y nombres de archivo.",
    "Supuesto: nombre canónico .bib esperado es filosofia-del-derecho.bib hasta confirmar README."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Registrar en .bib solo fuentes realmente citadas.",
    "No inventar referencias ni metadatos.",
    "Mantener metadatos mínimos: autor, título, año y fuente o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a Semana 7; confirmar uso en Actividad 5."
  ],
  "propagation_hints": [
    "Propagar lateral y recursivo solo tras validar JSON y estructura.",
    "Transferir patrones reutilizables, no conclusiones ni bibliografía exclusiva de hermanos.",
    "Aplicar unión y deduplicación lossless en cada ciclo.",
    "Conservar reglas útiles previas y agregar solo mejoras verificables.",
    "Mantener bandera de riesgo por incidentes históricos de parseo.",
    "Cuando falte consigna local, propagar plantilla y preguntas abiertas."
  ],
  "open_questions": [
    "Confirmar consigna textual completa de Actividad 5.",
    "Confirmar rúbrica específica de evaluación de Actividad 5.",
    "Confirmar si el producto es reporte, presentación o recurso visual.",
    "Confirmar archivo .bib canónico final de la asignatura.",
    "Confirmar pertinencia de fuentes de Semana 7 para Actividad 5.",
    "Confirmar resolución de tokens de plantilla en README y programa analítico."
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
      "Problema jurídico o social como detonante.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable y análisis propio.",
      "Conclusión jurídica transferible.",
      "Normalización estructural previa a propagación."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en entregables sólidos y verificables.",
      "Asegurar coherencia jurídica entre premisas, evidencia y cierre.",
      "Preservar continuidad editorial entre actividades sin contaminación lateral."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales y trazables.",
      "Supuestos explícitos cuando falte información.",
      "Postura propia sustentada.",
      "Cierre con aplicabilidad profesional."
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
          "target": "Problema jurídico",
          "kind": "supports",
          "justification": "Define tono y enfoque del planteamiento inicial."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "Sin delimitación del problema no hay argumentación consistente."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión transferible",
          "kind": "develops",
          "justification": "La conclusión deriva del razonamiento jurídico explícito."
        },
        {
          "source": "Consistencia cita-.bib",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La validez práctica exige trazabilidad de fuentes."
        },
        {
          "source": "Normalización JSON",
          "target": "Identidad UnADM",
          "kind": "depends_on",
          "justification": "La memoria institucional solo se preserva con estructura válida."
        },
        {
          "source": "Bibliografía específica de actividad",
          "target": "Bibliografía base",
          "kind": "contrasts",
          "justification": "La base orienta curso; la específica responde a la consigna concreta."
        }
      ],
      "evidence": [
        "README exige identidad UnADM, citas verificables y conclusión jurídica propia.",
        "Programa analítico fija ejes problema-conceptos-fuentes-análisis-cierre.",
        "Historial registra incidentes de salida no parseable y exige gate de estructura.",
        "README y programa muestran tokens sin expandir en nombres de .bib."
      ]
    },
    "reinforcement_log": [
      "Ciclo 45: deduplicación completa de reglas repetidas.",
      "Ciclo 45: eliminación de tipos de relación no permitidos y normalización a esquema válido.",
      "Ciclo 45: conservación de ejes editoriales troncales del origen.",
      "Ciclo 45: refuerzo lateral sin copiar conclusiones específicas ni bibliografía exclusiva."
    ]
  }
}