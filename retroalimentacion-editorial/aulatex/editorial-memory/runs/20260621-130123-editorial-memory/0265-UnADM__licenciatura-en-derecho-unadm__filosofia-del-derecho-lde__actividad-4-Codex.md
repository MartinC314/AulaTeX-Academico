{
  "summary": [
    "Se consolida refuerzo lateral para Actividad 4 con unión y deduplicación lossless.",
    "Se preserva identidad UnADM y marco curricular verificable: semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Se mantienen ejes editoriales base: problema, conceptos/fuentes, producto, análisis propio, conclusión jurídica.",
    "Se refuerza validación JSON estricta por antecedentes de salidas no parseables.",
    "Se mantiene regla de marcar supuestos cuando falte consigna local."
  ],
  "identity_rules": [
    "Mantener tono formal académico y precisión jurídica.",
    "Alinear la actividad a Licenciatura en Derecho y Filosofía del Derecho.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Vincular ubicación curricular a la malla institucional verificable.",
    "Tratar fuentes heredadas no verificadas como provisionales.",
    "Marcar como supuesto todo dato no visible en la consigna."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Alinear formato final al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Adaptar Actividad 4 a los cinco ejes del programa analítico.",
    "Evitar entregas solo descriptivas; incluir postura argumentada del estudiante.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No trasladar conclusiones específicas de Actividad 1 a Actividad 4."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna local de Actividad 4."
  ],
  "latex_rules": [
    "Usar codificación correcta en español en .tex y .bib.",
    "Citar solo claves existentes en el .bib activo.",
    "Mantener claves BibTeX estables para evitar rupturas de compilación.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens sin expandir en README y programa analítico antes de compilar.",
    "Confirmar nombre canónico del .bib de asignatura antes de referenciarlo."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Usar filosofia-del-derecho-clean.bib solo si la consigna de Actividad 4 coincide con su tema."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validación JSON y estructura.",
    "Transferir solo patrones reutilizables de identidad, estructura, calidad y método argumentativo.",
    "Evitar copiar redacción literal o bibliografía exclusiva entre nodos hermanos.",
    "Preservar reglas útiles previas sin regresión.",
    "Mantener bandera de normalización manual en ciclo 1 y 2 cuando haya salidas no estructuradas."
  ],
  "open_questions": [
    "Supuesto: no se ve la consigna textual de Actividad 4; confirmar producto exacto.",
    "Confirmar rúbrica específica de evaluación para Actividad 4.",
    "Confirmar si Actividad 4 requiere reporte, presentación u otro formato.",
    "Confirmar nombre final del archivo .bib canónico por token Slug no resuelto.",
    "Confirmar si la bibliografía de interpretación jurídica (Semana 7) aplica o no a Actividad 4."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro.",
        "Jurídicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Normalización estructurada obligatoria antes de propagar.",
        "Carpeta de asignatura como entrada canónica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Filosofía del Derecho.",
        "Semestre 1, bloque 2.",
        "Obligatoria, 8 créditos."
      ]
    },
    "essence": [
      "Resolver un problema jurídico o social con método académico.",
      "Articular conceptos, normas y doctrina con evidencia verificable.",
      "Transformar la planeación semanal en producto evaluable.",
      "Sostener análisis propio y postura académica.",
      "Concluir con utilidad jurídica transferible."
    ],
    "reason_for_being": [
      "Estandarizar calidad editorial entre actividades hermanas sin perder contexto local.",
      "Garantizar trazabilidad de fuentes y consistencia argumentativa.",
      "Evitar contaminación entre actividades por copia literal o fuentes no pertinentes."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Secciones funcionales y orden lógico jurídico.",
      "Distinción entre hechos, conceptos y argumentos.",
      "Supuestos marcados de forma explícita.",
      "Cierre con conclusión jurídica propia."
    ],
    "argumentative_patterns": [
      "Problema inicial -> marco conceptual/normativo -> análisis propio -> conclusión.",
      "Afirmación -> evidencia -> interpretación -> postura.",
      "Consistencia vertical entre consigna, desarrollo y cierre."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalización estructurada",
        "Validación JSON estricta",
        "Ejes editoriales de la asignatura",
        "Integridad académica y verificabilidad",
        "Conclusión jurídica transferible"
      ],
      "citations": [
        "README de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Tono formal académico",
          "kind": "supports",
          "justification": "La pauta editorial exige alineación institucional explícita."
        },
        {
          "source": "Ejes editoriales de la asignatura",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Los ejes definen el orden reusable del contenido."
        },
        {
          "source": "Validación JSON estricta",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo válido no hay reutilización segura."
        },
        {
          "source": "Integridad académica y verificabilidad",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión válida requiere respaldo verificable y análisis propio."
        }
      ],
      "evidence": [
        "Pauta editorial local en README.",
        "Ejes de trabajo en programa analítico.",
        "Antecedentes de salidas no parseables en ciclos previos."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas con variantes ortográficas.",
      "Se preservaron reglas útiles previas sin eliminación de capacidad.",
      "Se evitó transferencia de contenido específico de Actividad 1.",
      "Se reforzó control de supuestos por falta de consigna local visible."
    ]
  }
}