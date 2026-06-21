{
  "summary": [
    "Se consolida memoria lateral de Actividad 5 con transferencia reutilizable desde Actividad 1.",
    "Se preserva identidad UnADM, encuadre jurídico-académico y ubicación curricular verificada.",
    "Se refuerza normalización JSON obligatoria por historial de salidas no parseables.",
    "Se mantiene eje editorial troncal: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se aplica compresión lossless por deduplicación, sin recortar reglas útiles previas.",
    "Supuesto: falta consigna local completa de Actividad 5; se mantiene estructura base y preguntas abiertas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y encuadre.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Conservar enfoque jurídico-académico con claridad, fundamento y transferencia profesional.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar memorias de modelos previos como provisionales hasta verificación local.",
    "No usar fuentes de trazabilidad técnica como bibliografía académica."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir afirmación, evidencia e inferencia jurídica en cada bloque.",
    "Alinear el entregable al producto pedido por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Usar estructura base cuando falte consigna específica."
  ],
  "activity_rules": [
    "Adaptar el contenido al enunciado real de Actividad 5 sin romper reglas de asignatura.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar conclusiones específicas desde actividades hermanas.",
    "No reutilizar bibliografía de otra semana sin confirmar pertinencia.",
    "Registrar supuesto operativo cuando exista incertidumbre de alcance."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en afirmaciones relevantes.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que el producto responda a la consigna y no solo resuma conceptos.",
    "Aplicar revisión manual extra en memoria con incidentes previos de parseo."
  ],
  "latex_rules": [
    "Usar acentos y codificación en español de forma consistente en .tex y .bib.",
    "Mantener claves BibTeX estables ya citadas en .tex.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos, citas rotas ni referencias indefinidas.",
    "Validar nombres reales de archivos cuando existan tokens sin expandir en README o programa.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib; confirmar localmente."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes jurídicas verificables.",
    "Registrar en .bib solo obras realmente consultables y citadas.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Tratar filosofia-del-derecho-clean.bib como potencialmente temático de otra semana hasta validar pertinencia.",
    "Conservar claves bibliográficas originales cuando ya estén enlazadas en el .tex."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir solo patrones reutilizables: identidad, estructura, calidad, conceptos y relaciones.",
    "Evitar copiar redacción literal, conclusiones puntuales o bibliografía exclusiva entre hermanos.",
    "Preservar reglas útiles previas y agregar solo mejoras verificables.",
    "Mantener bandera histórica de riesgo por salidas no parseables en ciclos tempranos.",
    "Aplicar unión y deduplicación semántica en cada ciclo para compresión lossless."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 5.",
    "Confirmar rúbrica de evaluación de Actividad 5.",
    "Confirmar si el formato requerido es reporte, presentación o recurso visual.",
    "Confirmar nombre canónico final del archivo .bib de la asignatura.",
    "Confirmar si la bibliografía de Interpretación jurídica (Semana 7) aplica o no a Actividad 5."
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
      "Resolver un problema jurídico con fundamento conceptual y normativo.",
      "Sostener postura propia con evidencia verificable.",
      "Cerrar con conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir la planeación semanal en productos académicos jurídicos claros y verificables.",
      "Garantizar trazabilidad entre consigna, desarrollo, evidencia y cierre argumentativo."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones funcionales y trazables.",
      "Inferencias explícitas desde evidencia.",
      "Uso explícito de supuestos cuando falte dato local."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> inferencia jurídica.",
      "Contraste doctrinal breve -> toma de postura.",
      "Cierre con aplicabilidad profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Problema jurídico",
        "Marco normativo o doctrinal",
        "Análisis propio",
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
          "target": "Estructura de actividad",
          "kind": "supports",
          "justification": "La pauta institucional define tono, integridad y forma del entregable."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis requiere una pregunta jurídica delimitada."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión válida depende de respaldo trazable."
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
          "justification": "La base orienta; la específica responde a la consigna puntual."
        },
        {
          "source": "Supuestos explícitos",
          "target": "Control de calidad",
          "kind": "supports",
          "justification": "Evita afirmaciones no verificadas cuando falta información local."
        }
      ],
      "evidence": [
        "README exige identidad UnADM, integridad académica, citas verificables y conclusión jurídica propia.",
        "Programa analítico fija ejes: problema, conceptos, fuentes, análisis y cierre.",
        "Historial de parseo obliga gate estricto de estructura antes de propagar."
      ]
    },
    "reinforcement_log": [
      "Ciclo 91: deduplicación semántica de reglas repetidas sin pérdida funcional.",
      "Ciclo 91: refuerzo lateral de patrones comunes entre actividades hermanas.",
      "Ciclo 91: se mantiene separación entre patrones transferibles y contenido específico no transferible.",
      "Ciclo 91: se conserva bandera de riesgo por parseo y normalización obligatoria."
    ]
  }
}