{
  "summary": [
    "Se consolida transferencia lateral desde Actividad 1 a Actividad 5 con deduplicación lossless.",
    "Se preserva identidad UnADM y marco curricular de Filosofía del Derecho sin cambios sustantivos.",
    "Se refuerzan patrones reutilizables: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se mantiene gate estricto de normalización JSON antes de propagación recursiva.",
    "Se evita copiar conclusiones específicas o bibliografía exclusiva del nodo hermano."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Conservar enfoque jurídico-académico con criterio propio.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas de modelos como provisionales hasta validación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir afirmaciones, evidencia e inferencia jurídica.",
    "Alinear el entregable al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Adaptar el producto al enunciado real de Actividad 5.",
    "Incluir postura argumentada del estudiante, no solo resumen descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar bibliografía de otra semana sin confirmar pertinencia.",
    "Si falta instrucción local, registrar supuesto operativo y continuar con consistencia."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en cada afirmación relevante.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar manualmente memoria con historial de incidentes de parseo."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: .bib canónico esperado es filosofia-del-derecho.bib hasta confirmación final."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar en .bib solo fuentes realmente citadas en el texto.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a Semana 7; validar pertinencia para Actividad 5."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir solo patrones reutilizables; no texto literal ni conclusiones de hermano.",
    "Preservar reglas útiles previas y agregar solo mejoras verificables.",
    "Aplicar unión y deduplicación sin recorte semántico.",
    "Mantener bandera de riesgo histórico por salidas no parseables en ciclos previos."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 5; confirmar producto exacto solicitado.",
    "Confirmar rúbrica específica de evaluación para ajustar profundidad argumentativa.",
    "Confirmar si Actividad 5 requiere reporte, presentación o recurso visual.",
    "Confirmar nombre canónico final del archivo .bib de la asignatura.",
    "Confirmar si la bibliografía de Semana 7 es pertinente para Actividad 5."
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
      "Problema jurídico o social que activa la asignatura.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeación.",
      "Análisis propio y postura académica.",
      "Conclusión transferible a la práctica jurídica."
    ],
    "reason_for_being": [
      "Transformar planeación semanal en entregables académicos sólidos.",
      "Asegurar trazabilidad entre consigna, evidencia y conclusión jurídica.",
      "Conservar continuidad editorial entre actividades sin contaminación de contenido específico."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones funcionales y explícitas.",
      "Supuestos declarados cuando falten datos.",
      "Cierre con postura jurídica propia."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> inferencia jurídica.",
      "Contraste doctrinal breve -> toma de postura."
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
          "justification": "Define tono, rigor y forma del entregable."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis requiere delimitación previa del conflicto."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica válida exige sustento trazable."
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
        "README: identidad UnADM, integridad académica y conclusión jurídica propia.",
        "Programa analítico: ejes problema-conceptos-fuentes-análisis-cierre.",
        "Historial de ciclo: incidentes de salida no parseable obligan gate estructural."
      ]
    },
    "reinforcement_log": [
      "Ciclo 18: deduplicación completa de reglas repetidas en destino.",
      "Ciclo 18: refuerzo lateral de patrones estructurales reutilizables desde hermano Actividad 1.",
      "Ciclo 18: mantenimiento de restricciones de no copiar bibliografía o conclusiones específicas.",
      "Ciclo 18: consolidación de supuestos abiertos por falta de consigna local verificable."
    ]
  }
}