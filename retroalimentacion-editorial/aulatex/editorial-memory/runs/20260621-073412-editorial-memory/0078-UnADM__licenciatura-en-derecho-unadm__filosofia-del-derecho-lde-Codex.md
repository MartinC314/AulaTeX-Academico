{
  "summary": [
    "Consolidar memoria de materia con abstracción ascendente desde actividad-1.",
    "Preservar compresión lossless por unión y deduplicación sin regresión.",
    "Mantener normalización obligatoria para insumos no JSON parseable.",
    "Fijar ADN editorial: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Usar la carpeta de materia como entrada canónica de entregables y bibliografía."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, redacción y formato.",
    "Alinear la materia a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar malla-curricular-derecho-unadm.pdf como fuente curricular verificada.",
    "Marcar como [supuesto] todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local. [supuesto]",
    "Conservar referencias provisionales heredadas (Codex, GPT-Pro) con etiqueta de riesgo. [supuesto]",
    "No eliminar reglas heredadas útiles de calidad y normalización."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Alinear cada entrega al producto solicitado por la planeación semanal.",
    "Mantener trazabilidad entre actividad, archivo .tex y .bib de la materia.",
    "Separar artefactos por tipo: reporte y presentación en archivos dedicados."
  ],
  "activity_rules": [
    "Iniciar cada actividad con problema delimitado.",
    "Integrar conceptos, normas, doctrina o datos pertinentes.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir fuentes de semanas posteriores para actividad-1 sin verificación.",
    "Confirmar que el producto corresponda a la consigna específica."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna de la actividad."
  ],
  "latex_rules": [
    "Usar codificación correcta en español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar sin migración completa.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Corregir caracteres anómalos en rutas y nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Tratar nombres anómalos del README como pendientes, no como canon final. [supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Registrar fuentes de actividad en el .bib de la materia.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "No completar entradas truncadas sin verificación local.",
    "Mantener trazables claves recurrentes de SCJN/UNAM ya verificadas."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Elevar al ancestro solo patrones reutilizables, no redacción literal de actividades.",
    "Reusar puertas de calidad institucional sin perder especificidad local.",
    "Registrar incidencias de ingesta no parseable como riesgo persistente.",
    "Evitar propagar nombres de archivo anómalos hasta corrección local.",
    "Aplicar estrategia progresiva: primero identidad y calidad, luego estructura y citas."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-1. [supuesto]",
    "Confirmar formato principal exigido (reporte, presentación u otro). [supuesto]",
    "Confirmar rúbrica específica para profundidad argumentativa. [supuesto]",
    "Confirmar nombre canónico final del .bib de la materia.",
    "Confirmar si filosofia-del-derecho-clean.bib aplica fuera de Semana 7. [supuesto]",
    "Completar y verificar la entrada truncada scjnIncapacidadResistencia2019. [supuesto]"
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
      "Resolver problemas jurídicos con base conceptual y normativa.",
      "Vincular evidencia verificable con análisis propio.",
      "Producir conclusiones transferibles a práctica jurídica."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos.",
      "Estandarizar calidad editorial de actividades en LaTeX.",
      "Preservar trazabilidad entre contenido, citas y entregables."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable y explícito.",
      "Cierre con postura jurídica propia.",
      "Marcado explícito de [supuesto] cuando falte evidencia."
    ],
    "argumentative_patterns": [
      "Problema delimitado -> marco conceptual/normativo -> análisis crítico -> conclusión aplicada.",
      "Afirmación sustantiva -> evidencia verificable -> inferencia propia.",
      "Consigna -> producto específico -> validación de coherencia final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofía del Derecho",
        "Hermenéutica e interpretación jurídica",
        "Argumentación jurídica",
        "Derecho y moral",
        "Justicia",
        "Análisis crítico del fenómeno jurídico",
        "Problema-conceptos-evidencia-análisis-conclusión"
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
          "justification": "La interpretación aporta criterios para construir argumentos."
        },
        {
          "source": "Argumentación jurídica",
          "target": "Análisis crítico del fenómeno jurídico",
          "kind": "develops",
          "justification": "La argumentación permite evaluar razones, normas y consecuencias."
        },
        {
          "source": "Filosofía del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "La asignatura integra validez normativa y dimensión axiológica."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusión jurídica transferible",
          "kind": "depends_on",
          "justification": "La conclusión profesional exige sustento normativo verificable."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicación curricular y pauta editorial.",
        "Programa analítico: propósito y cinco ejes de trabajo.",
        "filosofia-del-derecho-clean.bib: referencias jurídicas recurrentes.",
        "Regla persistente: bloquear propagación sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Se elevan patrones de actividad-1 al nivel materia sin copiar redacción literal.",
      "Se deduplican reglas repetidas y se conserva cobertura semántica completa.",
      "Se mantiene trazabilidad de citas recurrentes y fuentes provisionales etiquetadas.",
      "Se refuerzan puertas de calidad y normalización como núcleo no regresivo."
    ]
  }
}