{
  "summary": [
    "Consolidar memoria de materia con abstracción ascendente desde actividad-1.",
    "Aplicar compresión lossless por unión y deduplicación sin regresión.",
    "Mantener identidad UnADM, trazabilidad curricular y control de calidad estructural.",
    "Bloquear propagación de salidas no JSON parseable hasta normalización.",
    "Preservar eje editorial común: problema, conceptos, evidencia, análisis propio y conclusión jurídica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y propósito académico.",
    "Alinear contenidos a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local. [supuesto]",
    "Conservar referencia de riesgo de ingesta: Codex y GPT-Pro no parseable."
  ],
  "structure_rules": [
    "Estructurar productos con: problema, conceptos/fuentes, análisis propio y cierre.",
    "Separar entregables por tipo: reporte, presentación, programa analítico y bibliografía.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear cada entrega al producto solicitado por planeación semanal.",
    "Cerrar con conclusión jurídica transferible a práctica profesional."
  ],
  "activity_rules": [
    "Iniciar cada actividad con problema jurídico o social delimitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar resumen solo descriptivo.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir que bibliografía de semanas posteriores aplica a actividad-1. [supuesto]"
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de reutilizar memoria.",
    "Normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Validar correspondencia entre citas en .tex y entradas en .bib.",
    "Confirmar que no se eliminen reglas útiles previas en cada ciclo."
  ],
  "latex_rules": [
    "Mantener claves BibTeX estables para evitar roturas de compilación.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Corregir caracteres anómalos y tokens sin expandir en rutas y nombres.",
    "Usar nombre canónico .bib verificado; mantener placeholder como pendiente. [supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Registrar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de materia y bibliografía específica por actividad.",
    "No completar entradas truncadas sin verificación local (ej. scjnIncapacidadResistencia2019). [supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas por README, programa analítico y .bib local.",
    "Elevar al ancestro patrones reutilizables, no redacción literal de actividades.",
    "Conservar trazabilidad de conceptos, citas recurrentes y puertas de calidad.",
    "Aplicar normalización manual en ciclos con insumos no estructurados.",
    "Evitar propagar nombres de archivo anómalos hasta corrección local."
  ],
  "open_questions": [
    "Confirmar nombre canónico final del archivo .bib de la materia.",
    "Confirmar consigna textual exacta de actividad-1 y su tipo de producto.",
    "Determinar si filosofia-del-derecho-clean.bib es solo Semana 7 o reutilizable en actividad-1. [supuesto]",
    "Resolver placeholder PowerShell en README y programa analítico. [supuesto]",
    "Completar y verificar campos faltantes de scjnIncapacidadResistencia2019. [supuesto]"
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
        "Carpeta de materia como entrada canónica editorial."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos.",
        "Asignatura: Filosofía del Derecho."
      ]
    },
    "essence": [
      "Formar análisis jurídico con base conceptual, normativa y crítica.",
      "Traducir planeación semanal en entregables académicos verificables.",
      "Sostener una conclusión jurídica propia y transferible."
    ],
    "reason_for_being": [
      "Garantizar consistencia editorial de la materia en LaTeX.",
      "Unificar estándares de calidad, citación y argumentación.",
      "Preservar memoria útil sin pérdida por deduplicación."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable y explícito.",
      "Citas verificables en afirmaciones sustantivas.",
      "Marcado explícito de [supuesto] cuando corresponda.",
      "Cierre con criterio jurídico propio."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer marco conceptual y normativo.",
      "Analizar críticamente con postura propia.",
      "Concluir con aplicación jurídica práctica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofía del Derecho",
        "Hermenéutica e interpretación jurídica",
        "Argumentación jurídica",
        "Derecho y moral",
        "Justicia",
        "Análisis crítico del fenómeno jurídico",
        "Eje editorial de cinco pasos"
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
          "justification": "La interpretación fundamenta la construcción de razones jurídicas."
        },
        {
          "source": "Argumentación jurídica",
          "target": "Análisis crítico del fenómeno jurídico",
          "kind": "develops",
          "justification": "Permite evaluar validez, coherencia y consecuencias normativas."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusión jurídica transferible",
          "kind": "depends_on",
          "justification": "La conclusión exige sustento verificable."
        },
        {
          "source": "Filosofía del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "Integra debate axiológico en la formación jurídica."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicación curricular y pauta editorial.",
        "Programa analítico: propósito y cinco ejes de trabajo.",
        "filosofia-del-derecho-clean.bib: claves jurídicas recurrentes.",
        "Memoria de actividad-1: patrón estable problema-conceptos-evidencia-análisis-conclusión."
      ]
    },
    "reinforcement_log": [
      "Ciclo 8: se eleva patrón argumentativo de actividad a materia sin copia literal.",
      "Ciclo 8: se preservan reglas heredadas y se deduplican variantes redundantes.",
      "Ciclo 8: se refuerza bloqueo por no-JSON y normalización previa obligatoria.",
      "Ciclo 8: se mantiene trazabilidad entre .tex, .bib, conceptos y citas."
    ]
  }
}