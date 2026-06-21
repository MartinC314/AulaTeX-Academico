{
  "summary": [
    "Consolidar memoria de materia con abstracción ascendente desde actividad-1.",
    "Preservar reglas útiles previas sin regresión.",
    "Aplicar compresión lossless por unión y deduplicación.",
    "Mantener normalización obligatoria de insumos no JSON parseable.",
    "Reforzar identidad UnADM, trazabilidad curricular y calidad verificable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en redacción y formato.",
    "Alinear entregables a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar carpeta de materia como punto de entrada canónico.",
    "Marcar como [supuesto] todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local. [supuesto]",
    "Usar malla-curricular-derecho-unadm.pdf como fuente curricular verificada."
  ],
  "structure_rules": [
    "Estructurar productos con: problema, conceptos/fuentes, análisis propio y cierre.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, análisis y conclusión.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear cada entrega al producto solicitado por planeación semanal.",
    "Mantener trazabilidad entre actividad, .tex y .bib de materia."
  ],
  "activity_rules": [
    "Iniciar cada actividad con problema jurídico o social delimitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir fuentes de semanas posteriores para actividad-1 sin verificación. [supuesto]",
    "Verificar correspondencia del producto con la consigna específica."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar no regresión de reglas útiles previas en cada ciclo."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar sin migración completa.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir nombres de archivo anómalos antes de tomarlos como canónicos. [supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar fuentes específicas de actividad en el .bib de la asignatura.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "No completar entradas truncadas sin verificación local. [supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Elevar al ancestro reglas transferibles de identidad, calidad y trazabilidad.",
    "No copiar redacción literal de actividad; sintetizar patrones reutilizables.",
    "Propagar citas recurrentes como trazas, no como obligación universal.",
    "Mantener etiqueta de compresión union-dedupe lossless en ciclos siguientes.",
    "Aplicar normalización manual en nodos con historial no estructurado."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-1. [supuesto]",
    "Confirmar producto principal requerido en actividad-1 (reporte/presentación). [supuesto]",
    "Confirmar nombre canónico final del .bib de materia.",
    "Confirmar si filosofia-del-derecho-clean.bib es solo Semana 7 o base reutilizable. [supuesto]",
    "Completar y verificar entrada scjnIncapacidadResistencia2019 en .bib local. [supuesto]"
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
        "Carpeta de materia como entrada canónica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos.",
        "Asignatura: Filosofía del Derecho."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Conceptos, normas, doctrina y datos pertinentes.",
      "Evidencia verificable.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible a práctica profesional."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos.",
      "Asegurar calidad argumentativa y trazabilidad de fuentes.",
      "Estandarizar producción editorial LaTeX de la materia."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable y explícito.",
      "Marcado de supuestos.",
      "Cierre con criterio jurídico propio."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Construir marco conceptual y normativo.",
      "Analizar críticamente con postura propia.",
      "Concluir con aplicabilidad jurídica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofía del Derecho",
        "Hermenéutica e interpretación jurídica",
        "Argumentación jurídica",
        "Derecho y moral",
        "Justicia",
        "Análisis crítico del fenómeno jurídico"
      ],
      "citations": [
        "hernandezManriquezHermeneutica2019",
        "scjnMemoriaArgumentacion2008",
        "scjnViolenciaFisica2022",
        "scjnIncapacidadResistencia2019",
        "ruiz_rodriguez_filosofia_derecho_2009",
        "rojas_gonzalez_filosofia_derecho_2018",
        "noauthor_constitucion_nodate",
        "de_victimas_ley_2013"
      ],
      "relations": [
        {
          "source": "Hermenéutica e interpretación jurídica",
          "target": "Argumentación jurídica",
          "kind": "supports",
          "justification": "La interpretación sustenta la construcción de argumentos jurídicos."
        },
        {
          "source": "Argumentación jurídica",
          "target": "Análisis crítico del fenómeno jurídico",
          "kind": "develops",
          "justification": "La argumentación permite evaluar normas, razones y consecuencias."
        },
        {
          "source": "Filosofía del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "La materia integra discusión axiológica y validez normativa."
        },
        {
          "source": "Marco normativo y doctrinal",
          "target": "Conclusión jurídica transferible",
          "kind": "depends_on",
          "justification": "La conclusión profesional requiere soporte verificable."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicación curricular y pauta editorial.",
        "Programa analítico: propósito y cinco ejes de trabajo.",
        "filosofia-del-derecho-clean.bib: claves jurídicas recurrentes.",
        "Actividad-1: patrón problema-conceptos-evidencia-análisis-conclusión."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas y variantes ortográficas.",
      "Se conservaron gates críticos de parseo JSON y normalización.",
      "Se elevaron patrones argumentativos del nivel actividad al nivel materia.",
      "Se mantuvo trazabilidad de citas recurrentes sin inventar fuentes.",
      "Se marcaron incertidumbres como [supuesto] para control editorial."
    ]
  }
}