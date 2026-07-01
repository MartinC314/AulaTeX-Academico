{
  "summary": [
    "Se consolida refuerzo lateral entre actividades hermanas con deduplicación lossless.",
    "Se preserva identidad UnADM y encuadre curricular de Filosofía del Derecho.",
    "Se mantiene regla crítica: no propagar sin JSON parseable y estructura mínima completa.",
    "Se transfieren solo patrones reutilizables de estructura, calidad y argumentación.",
    "Se evita copiar conclusiones específicas o bibliografía exclusiva de otra actividad.",
    "Supuesto: falta consigna local completa de Actividad 5; se mantiene plantilla base verificable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y encuadre.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Conservar enfoque jurídico-académico con claridad, fundamento y transferencia profesional.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas de modelos como provisionales hasta verificación local.",
    "No tratar memoria de modelos como fuente académica citables."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir explícitamente afirmación, evidencia e inferencia.",
    "Alinear el entregable al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a práctica profesional."
  ],
  "activity_rules": [
    "Adaptar el producto al enunciado real de Actividad 5 sin romper reglas troncales de asignatura.",
    "Incluir postura argumentada del estudiante y evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar bibliografía de otra semana sin confirmar pertinencia temática.",
    "Registrar supuesto operativo si falta alcance o rúbrica y continuar con consistencia."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en afirmaciones relevantes.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Validar que el producto responda al problema y no solo resuma conceptos.",
    "Aplicar revisión manual extra cuando exista historial de incidentes de parseo."
  ],
  "latex_rules": [
    "Usar acentos y codificación en español de forma consistente en .tex y .bib.",
    "Mantener claves BibTeX estables ya citadas para evitar compilaciones rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Validar nombres reales de archivos cuando README tenga tokens sin expandir.",
    "Resolver marcadores tipo $(@{...}.Slug) antes de fijar rutas finales."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Agregar al .bib solo fuentes realmente citadas en el texto.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Confirmar pertinencia de filosofia-del-derecho-clean.bib antes de reutilizar en Actividad 5."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales validadas y deduplicadas.",
    "Conservar reglas útiles previas y agregar solo mejoras verificables.",
    "No transferir redacción literal, conclusiones ni bibliografía exclusiva entre hermanos.",
    "Mantener bandera de riesgo histórico por salidas no parseables en ciclos previos.",
    "Aplicar normalización manual si se detecta salida no estructurada en nodos vecinos."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual completa de Actividad 5; confirmar producto exacto.",
    "Confirmar si Actividad 5 requiere reporte, presentación o recurso visual.",
    "Confirmar rúbrica específica para ajustar profundidad argumentativa.",
    "Confirmar nombre canónico final del .bib de la asignatura.",
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
      "Problema jurídico delimitado.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir la planeación semanal en productos académicos jurídicamente sólidos.",
      "Asegurar trazabilidad entre consigna, evidencia, análisis y cierre.",
      "Preservar continuidad editorial entre actividades sin contaminar contenidos específicos."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales y explícitas.",
      "Supuestos declarados cuando falte información.",
      "Cierre con criterio jurídico propio."
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
        "Evidencia verificable",
        "Análisis propio",
        "Conclusión transferible",
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
          "justification": "El marco institucional define enfoque y pertinencia del planteamiento."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "Sin delimitación del problema no hay argumentación focalizada."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión válida requiere sustento trazable."
        },
        {
          "source": "Normalización JSON",
          "target": "Consistencia cita-.bib",
          "kind": "develops",
          "justification": "La estructura controlada facilita validaciones automáticas de calidad."
        },
        {
          "source": "Bibliografía base",
          "target": "Bibliografía específica de actividad",
          "kind": "contrasts",
          "justification": "La base orienta la asignatura; la específica responde a la consigna concreta."
        }
      ],
      "evidence": [
        "README exige identidad UnADM, integridad académica, citas verificables y conclusión jurídica propia.",
        "Programa analítico fija ejes: problema, conceptos, fuentes, análisis y cierre.",
        "Historial de incidentes de parseo justifica gate estricto de JSON.",
        "Archivo clean.bib está etiquetado para 'Interpretación jurídica' (Semana 7), requiere validación de pertinencia."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: se reforzó transferencia lateral por patrones y no por contenido específico.",
      "Se eliminaron duplicados semánticos y se conservaron reglas útiles previas.",
      "Se añadió control explícito de no usar memoria de modelo como fuente académica.",
      "Se mantuvo política de supuestos explícitos ante falta de consigna local."
    ]
  }
}