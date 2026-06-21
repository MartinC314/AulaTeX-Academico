{
  "summary": [
    "Se consolida memoria lateral de Actividad 5 con transferencia reusable desde Actividad 1.",
    "Se preserva identidad UnADM, ejes editoriales y control de calidad sin copiar contenido específico de hermano.",
    "Se mantiene normalización estructurada obligatoria antes de propagación recursiva.",
    "Se refuerza regla de deduplicación lossless y eliminación de ruido duplicado.",
    "Supuesto: falta consigna y rúbrica locales de Actividad 5; se conserva estructura base."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Conservar enfoque jurídico-académico con criterio propio.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar memorias de modelos previos como provisionales hasta verificación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir afirmaciones, evidencia y conclusión en bloques claros.",
    "Alinear el entregable al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a práctica profesional."
  ],
  "activity_rules": [
    "Adaptar el producto al enunciado real de Actividad 5.",
    "Incluir postura argumentada del estudiante y evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar conclusiones específicas de Actividad 1.",
    "No reutilizar bibliografía de otra semana sin confirmar pertinencia."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en afirmaciones relevantes.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Rechazar relaciones con tipos fuera de supports|contrasts|depends_on|develops.",
    "Aplicar revisión manual extra en memorias con historial de parseo defectuoso."
  ],
  "latex_rules": [
    "Usar acentos y codificación consistente en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar compilaciones rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib hasta confirmación local."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Registrar en .bib solo fuentes realmente citadas.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Tratar filosofia-del-derecho-clean.bib como provisional para Actividad 5 si corresponde a otra semana."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir solo patrones reutilizables de identidad, estructura, calidad y conceptos troncales.",
    "Evitar copiar redacción literal, conclusiones o bibliografía exclusiva de nodos hermanos.",
    "Aplicar unión y deduplicación sin pérdida semántica.",
    "Conservar reglas útiles previas y agregar solo mejoras verificables."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 5.",
    "Confirmar rúbrica de evaluación específica de Actividad 5.",
    "Confirmar formato requerido: reporte, presentación o recurso visual.",
    "Confirmar si Actividad 5 usa bibliografía propia o reutiliza parte de la base.",
    "Confirmar nombre canónico final del .bib en presencia de tokens sin expandir."
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
      "Transformar planeación semanal en productos académicos sólidos.",
      "Garantizar trazabilidad entre consigna, argumento, evidencia y cierre.",
      "Mantener continuidad editorial institucional entre actividades."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones funcionales sin ornamentación.",
      "Inferencias jurídicas explícitas.",
      "Supuestos marcados cuando falte información local."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> inferencia jurídica.",
      "Contraste doctrinal breve -> postura propia."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalización JSON",
        "Problema jurídico",
        "Marco normativo/doctrinal",
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
          "target": "Problema jurídico",
          "kind": "supports",
          "justification": "El encuadre institucional define pertinencia del planteamiento."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "No hay análisis sólido sin conflicto delimitado."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión transferible",
          "kind": "develops",
          "justification": "La conclusión deriva del razonamiento argumentado."
        },
        {
          "source": "Consistencia cita-.bib",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La solidez de cierre requiere respaldo verificable."
        },
        {
          "source": "Normalización JSON",
          "target": "Identidad UnADM",
          "kind": "supports",
          "justification": "La gobernanza editorial exige estructura válida para memoria persistente."
        }
      ],
      "evidence": [
        "README establece identidad UnADM, integridad académica y conclusión jurídica propia.",
        "Programa analítico fija ejes problema-conceptos-fuentes-análisis-cierre.",
        "Historial de parseo no válido justifica gate estricto de estructura."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas de origen y destino sin pérdida de intención.",
      "Se retiró transferencia de contenido específico no reusable entre hermanos.",
      "Se reforzó validación de tipo de relación en knowledge_graph.",
      "Se mantuvo separación entre bibliografía base y específica por actividad.",
      "Se conservaron supuestos abiertos donde faltan datos locales verificables."
    ]
  }
}