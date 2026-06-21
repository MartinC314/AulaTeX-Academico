{
  "summary": [
    "Se consolida refuerzo lateral desde Actividad 1 a Actividad 5 sin copiar contenido específico.",
    "Se preservan reglas troncales UnADM: identidad institucional, estructura argumentativa y control de calidad.",
    "Se aplica deduplicación lossless: se unifican reglas repetidas sin recortar reglas útiles.",
    "Se mantiene prioridad de normalización JSON parseable antes de propagación recursiva.",
    "Se conserva criterio de marcar como supuesto todo dato no visible en la consigna local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y encuadre.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Conservar enfoque jurídico-académico con claridad, fundamento y transferencia profesional.",
    "Marcar explícitamente como supuesto cualquier dato no visible en la consigna de Actividad 5.",
    "Tratar fuentes heredadas de modelos como provisionales hasta verificación local.",
    "No usar memorias de modelo como fuentes académicas citables."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir afirmaciones, evidencia y conclusión en bloques claros.",
    "Alinear el entregable al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Adaptar el producto al enunciado real de Actividad 5 sin romper reglas de asignatura.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar bibliografía de otra semana sin confirmar pertinencia.",
    "Registrar supuesto operativo si falta alcance o formato de la consigna."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en cada afirmación relevante.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que el producto responda al problema y no solo resuma conceptos.",
    "Aplicar revisión manual extra en memorias con incidentes previos de parseo."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Validar nombres reales de archivos cuando el README tenga tokens sin expandir.",
    "Resolver tokens tipo $(@{...}.Slug) en README y programa analítico antes de automatizar rutas.",
    "Supuesto: el .bib canónico esperado es filosofia-del-derecho.bib hasta confirmación local."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar en .bib solo fuentes realmente citadas en la actividad.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Tratar filosofia-del-derecho-clean.bib como potencialmente de otra semana hasta validar pertinencia para Actividad 5."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir solo patrones reutilizables: identidad, estructura, calidad, conceptos y relaciones recurrentes.",
    "No propagar redacción literal, conclusiones específicas ni bibliografía exclusiva entre actividades hermanas.",
    "Conservar reglas útiles previas y agregar solo mejoras verificables.",
    "Si falta consigna local, propagar plantilla base y preguntas abiertas."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual completa de Actividad 5; confirmar producto exacto solicitado.",
    "Confirmar rúbrica de evaluación específica de Actividad 5.",
    "Confirmar si Actividad 5 requiere reporte, presentación o recurso visual.",
    "Confirmar nombre canónico final del archivo .bib en la asignatura.",
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
      "Problema jurídico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable.",
      "Análisis propio y postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en producto académico con estructura jurídica sólida.",
      "Asegurar trazabilidad entre consigna, desarrollo, evidencia y cierre argumentativo.",
      "Preservar continuidad editorial entre actividades sin contaminación de contenido específico."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones funcionales y explícitas.",
      "Postura propia sustentada.",
      "Uso visible de supuestos cuando falta información local.",
      "Cierre con utilidad profesional jurídica."
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
        "Estructura de actividad jurídica",
        "Evidencia verificable",
        "Conclusión transferible",
        "Normalización JSON",
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
          "target": "Estructura de actividad jurídica",
          "kind": "supports",
          "justification": "La pauta institucional define tono, forma y objetivo del entregable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La validez jurídica del cierre depende del respaldo documental."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia confiable."
        },
        {
          "source": "Supuestos explícitos",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Evita presentar inferencias no verificadas como hechos."
        },
        {
          "source": "Bibliografía específica de actividad",
          "target": "Bibliografía base",
          "kind": "contrasts",
          "justification": "La base orienta la asignatura; la específica responde a la consigna puntual."
        }
      ],
      "evidence": [
        "README exige identidad UnADM, citas verificables y conclusión jurídica propia.",
        "Programa analítico fija ejes: problema, conceptos, fuentes, análisis y cierre.",
        "Historial de parseo no válido justifica gate estricto de estructura.",
        "Transferencia entre hermanos requiere patrones generales, no contenido específico."
      ]
    },
    "reinforcement_log": [
      "Ciclo 80: se refuerza transferencia lateral controlada y deduplicación lossless.",
      "Ciclo 80: se mantiene regla de no propagar salidas no parseables.",
      "Ciclo 80: se conserva separación bibliografía base vs específica de actividad.",
      "Ciclo 80: se preserva núcleo argumentativo institucional sin copiar conclusiones de Actividad 1."
    ]
  }
}