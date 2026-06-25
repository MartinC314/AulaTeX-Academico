{
  "summary": [
    "Se consolida refuerzo lateral para Actividad 5 con deduplicación lossless.",
    "Se preserva identidad UnADM y ubicación curricular verificable desde README y programa analítico.",
    "Se mantiene regla crítica: no propagar nada sin JSON parseable y estructura mínima completa.",
    "Se transfieren patrones reutilizables desde Actividad 1 sin copiar conclusiones ni bibliografía exclusiva.",
    "Se mantiene como supuesto la falta de consigna y rúbrica local detallada de Actividad 5."
  ],
  "identity_rules": [
    "Mantener tono formal académico y precisión jurídica.",
    "Alinear toda entrega a UnADM, Licenciatura en Derecho, Filosofía del Derecho.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Conservar integridad académica con citas verificables.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar memorias de modelos previos como provisionales, no como fuentes académicas."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir en cada bloque afirmación, evidencia e inferencia.",
    "Cerrar con conclusión jurídica transferible a práctica profesional.",
    "Alinear el formato final al producto solicitado por la planeación semanal."
  ],
  "activity_rules": [
    "Adaptar contenido al enunciado real de Actividad 5 cuando esté disponible.",
    "Evitar entregas descriptivas sin postura argumentada del estudiante.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar bibliografía de otra semana sin confirmar pertinencia.",
    "Si falta instrucción local, registrar supuesto operativo y continuar con consistencia."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar presencia de todas las claves del esquema requerido.",
    "Revisar consistencia entre citas en texto y archivo .bib.",
    "Confirmar respaldo o marca de supuesto en cada afirmación relevante.",
    "Rechazar contradicciones con reglas institucionales ya consolidadas.",
    "Aplicar revisión manual extra en memoria con historial de parseo defectuoso."
  ],
  "latex_rules": [
    "Usar español con acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar compilación rota.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Corregir rutas con tokens sin expandir tipo $(@{...}.Slug).",
    "Supuesto: nombre canónico esperado del .bib es filosofia-del-derecho.bib; confirmar localmente."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Registrar en .bib solo fuentes realmente usadas en la actividad.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Tratar filosofia-del-derecho-clean.bib como potencialmente de otra semana hasta verificar pertinencia."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir solo patrones generales reutilizables entre nodos hermanos.",
    "No transferir redacción literal ni conclusiones particulares de otra actividad.",
    "No transferir bibliografía exclusiva sin validación de pertinencia local.",
    "Preservar reglas útiles previas y agregar solo mejoras verificables.",
    "Mantener bitácora de supuestos pendientes de confirmación."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 5.",
    "Confirmar rúbrica de evaluación específica de Actividad 5.",
    "Confirmar si el producto es reporte, presentación o recurso visual.",
    "Confirmar nombre canónico final del archivo .bib en la asignatura.",
    "Confirmar si referencias de Semana 7 aplican a Actividad 5.",
    "Confirmar fuentes obligatorias explícitas de la semana correspondiente."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico",
        "Claro y jurídicamente preciso",
        "Argumentativo con criterio propio"
      ],
      "institutional": [
        "Alineación explícita con UnADM",
        "Integridad académica con citas verificables",
        "Carpeta de asignatura como entrada canónica"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Semestre 1, bloque 2, obligatoria, 8 créditos",
        "Asignatura: Filosofía del Derecho"
      ]
    },
    "essence": [
      "Problema jurídico o social",
      "Conceptos y marco normativo o doctrinal",
      "Evidencia verificable",
      "Análisis propio",
      "Conclusión jurídica transferible"
    ],
    "reason_for_being": [
      "Convertir planeación semanal en entregables académicos sólidos.",
      "Asegurar trazabilidad entre problema, evidencia y conclusión.",
      "Formar criterio jurídico argumentado y verificable."
    ],
    "style_markers": [
      "Encuadre breve al inicio",
      "Secciones funcionales y explícitas",
      "Postura propia sustentada",
      "Supuestos marcados cuando falte información",
      "Cierre con utilidad profesional"
    ],
    "argumentative_patterns": [
      "Problema -> marco -> análisis -> conclusión",
      "Afirmación -> evidencia -> inferencia jurídica",
      "Contraste doctrinal breve -> toma de postura",
      "Regla general -> aplicación al caso -> cierre transferible"
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalización JSON",
        "Problema jurídico",
        "Marco normativo o doctrinal",
        "Evidencia verificable",
        "Análisis propio",
        "Conclusión transferible",
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
          "justification": "Define tono, formato y estándar académico."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo válido no hay transferencia confiable."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis parte de una pregunta delimitada."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica exige respaldo trazable."
        },
        {
          "source": "Bibliografía base",
          "target": "Bibliografía específica de actividad",
          "kind": "contrasts",
          "justification": "La base orienta; la específica responde a la consigna."
        },
        {
          "source": "Supuestos explícitos",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Evita presentar inferencias como hechos."
        }
      ],
      "evidence": [
        "README: identidad UnADM, citas verificables, conclusión jurídica propia.",
        "Programa analítico: ejes problema, conceptos, fuentes, análisis y cierre.",
        "Historial: incidentes de salida no parseable exigen gate de estructura.",
        "Supuesto: aún falta consigna y rúbrica local de Actividad 5."
      ]
    },
    "reinforcement_log": [
      "Ciclo 14: deduplicación completa de reglas repetidas.",
      "Ciclo 14: se mantiene ADN institucional y ejes argumentativos troncales.",
      "Ciclo 14: se refuerza separación entre bibliografía base y específica.",
      "Ciclo 14: se preserva política de no inventar fuentes y marcar supuestos.",
      "Ciclo 14: se consolida transferencia lateral controlada entre hermanos."
    ]
  }
}