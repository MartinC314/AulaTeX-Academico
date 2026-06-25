{
  "summary": [
    "Se consolida refuerzo lateral desde Actividad 1 a Actividad 5 sin copiar contenido específico.",
    "Se preservan reglas válidas de identidad UnADM, estructura académica y control de calidad.",
    "Se aplica deduplicación lossless y se eliminan repeticiones semánticas.",
    "Se mantiene como obligatorio el control de JSON parseable antes de propagación.",
    "Se refuerza transferencia por patrones reutilizables: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Supuesto: falta consigna textual y rúbrica local de Actividad 5; se conserva estructura base abierta."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y encuadre.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Conservar enfoque jurídico-académico con claridad, fundamento y transferencia profesional.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas de modelos como provisionales hasta verificación local.",
    "No usar memorias de modelo como fuentes académicas citables."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir afirmaciones, evidencia e inferencia jurídica en bloques claros.",
    "Alinear el entregable al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Adaptar el producto al enunciado real de Actividad 5 sin romper reglas de asignatura.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar bibliografía de otra semana sin confirmar pertinencia.",
    "Registrar supuesto operativo cuando exista ambigüedad de alcance."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en cada afirmación relevante.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que el producto responda a la consigna local y no solo a plantilla general.",
    "Aplicar revisión manual extra en nodos con historial de incidentes de parseo."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables ya usadas en el .tex.",
    "Compilar sin errores críticos, sin referencias rotas y sin warnings bloqueantes.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Validar nombres reales de archivos cuando README contenga tokens sin expandir.",
    "Resolver o sustituir tokens tipo $(@{...}.Slug) antes de compilación o documentación final.",
    "Supuesto: el .bib canónico esperado es filosofia-del-derecho.bib hasta confirmación local."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes jurídicas verificables.",
    "Agregar al .bib solo obras realmente citadas en el texto final.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Tratar filosofia-del-derecho-clean.bib como potencialmente específico de otra semana hasta validar pertinencia para Actividad 5."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir solo patrones reutilizables; no copiar conclusiones ni bibliografía exclusiva de nodo hermano.",
    "Conservar reglas útiles previas y agregar solo mejoras verificables.",
    "Aplicar unión + deduplicación semántica para compresión lossless.",
    "Mantener bandera de riesgo histórico por salidas no parseables en ciclos previos.",
    "Si falta consigna local, propagar estructura base y preguntas abiertas en lugar de contenido inventado."
  ],
  "open_questions": [
    "Supuesto: falta enunciado textual de Actividad 5; confirmar producto exacto solicitado.",
    "Confirmar rúbrica de evaluación específica de Actividad 5.",
    "Confirmar si el entregable requerido es reporte, presentación o recurso visual.",
    "Confirmar nombre canónico final del archivo .bib de la asignatura.",
    "Confirmar si la bibliografía de Interpretación jurídica (Semana 7) aplica total, parcial o no aplica a Actividad 5."
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
      "Problema jurídico o social bien delimitado.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable con trazabilidad.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos y verificables.",
      "Asegurar continuidad editorial entre actividades sin perder especificidad local."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones funcionales, no ornamentales.",
      "Postura propia sustentada.",
      "Supuestos explícitos cuando falte información.",
      "Cierre con utilidad profesional jurídica."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> inferencia jurídica.",
      "Contraste doctrinal breve -> toma de postura -> transferencia práctica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Ejes editoriales troncales",
        "Normalización JSON",
        "Consistencia cita-.bib",
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
          "justification": "La identidad institucional define tono, rigor y forma de entrega."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo válido no hay transferencia confiable."
        },
        {
          "source": "Pertinencia bibliográfica por actividad",
          "target": "Consistencia cita-.bib",
          "kind": "supports",
          "justification": "Evita arrastre de fuentes no alineadas a la consigna local."
        },
        {
          "source": "Ejes editoriales troncales",
          "target": "Actividad 5",
          "kind": "develops",
          "justification": "Permiten continuidad lateral sin copiar resultados de Actividad 1."
        }
      ],
      "evidence": [
        "README exige identidad UnADM, citas verificables y conclusión jurídica propia.",
        "Programa analítico fija ejes problema-conceptos-fuentes-análisis-cierre.",
        "Historial reporta incidentes de salida no parseable; se mantiene gate estructural."
      ]
    },
    "reinforcement_log": [
      "Ciclo 22: refuerzo lateral aplicado con deduplicación semántica.",
      "Se preservaron reglas útiles previas sin eliminación regresiva.",
      "Se añadieron mejoras verificables: inferencia jurídica explícita y gate de pertinencia bibliográfica por actividad.",
      "Se evitó transferencia de redacción literal, conclusiones específicas y bibliografía exclusiva de Actividad 1."
    ]
  }
}