{
  "summary": [
    "Consolidar memoria de materia con abstracción ascendente desde Actividad 1.",
    "Preservar reglas útiles previas sin regresión mediante unión y deduplicación lossless.",
    "Mantener identidad UnADM, trazabilidad curricular y cierre jurídico con criterio propio.",
    "Exigir normalización estructurada antes de cualquier propagación recursiva.",
    "Registrar insumos no parseables como riesgo de ingesta sin perder señales válidas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en redacción y formato.",
    "Alinear la materia a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Usar malla-curricular-derecho-unadm.pdf como respaldo curricular verificado.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local. [supuesto]",
    "Conservar referencias provisionales heredadas (Codex, GPT-Pro) hasta sustitución verificada. [supuesto]"
  ],
  "structure_rules": [
    "Abrir cada entrega con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Alinear cada producto al tipo solicitado por la planeación semanal.",
    "Mantener trazabilidad entre actividad, archivo .tex y .bib de materia.",
    "No canonizar nombres anómalos del README hasta corrección local. [supuesto]"
  ],
  "activity_rules": [
    "Iniciar cada actividad con problema delimitado.",
    "Integrar conceptos, normas, doctrina o datos pertinentes.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Validar que el producto corresponda a la consigna específica de la actividad.",
    "No asumir que fuentes de semanas posteriores aplican a Actividad 1. [supuesto]"
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que no se eliminen reglas útiles previas en cada ciclo."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar sin migración completa.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Separar entregables por tipo en archivos .tex dedicados (reporte, presentación).",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Supuesto operativo: archivo .bib canónico esperado filosofia-del-derecho.bib hasta confirmación final. [supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Registrar fuentes de actividad en el .bib de la asignatura.",
    "No inventar referencias; usar solo obras realmente consultables.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Preservar y deduplicar entradas verificables de UNAM, IIJ y SCJN.",
    "No completar entradas BibTeX truncadas sin verificación local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Elevar al ancestro patrones reutilizables, no redacción literal de la actividad.",
    "Propagar reglas generales cuando falte consigna textual y marcar supuestos.",
    "Mantener etiqueta de compresión union-dedupe lossless en toda propagación.",
    "Evitar propagar placeholders de nombres de archivo no resueltos.",
    "Reusar puertas de calidad institucionales como filtro previo en nodos vecinos."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 1 para fijar plantilla final.",
    "Confirmar nombre canónico definitivo del .bib de la materia.",
    "Determinar si filosofia-del-derecho-clean.bib aplica fuera de Semana 7. [supuesto]",
    "Completar y verificar campos de scjnIncapacidadResistencia2019.",
    "Sustituir referencias provisionales heredadas por fuentes locales verificadas."
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
      "Conceptos y marco normativo.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos y trazables.",
      "Asegurar coherencia entre identidad institucional, método argumentativo y evidencia.",
      "Sostener una memoria editorial persistente sin pérdida de reglas válidas."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable.",
      "Citas explícitas y verificables.",
      "Marcado explícito de supuestos.",
      "Cierre con criterio jurídico propio."
    ],
    "argumentative_patterns": [
      "Delimitación del problema.",
      "Marco conceptual y normativo.",
      "Contraste doctrinal o jurisprudencial.",
      "Toma de postura argumentada.",
      "Conclusión aplicable a práctica jurídica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofía del Derecho",
        "Hermenéutica e interpretación jurídica",
        "Argumentación jurídica",
        "Derecho y moral",
        "Justicia",
        "Análisis crítico del fenómeno jurídico",
        "Trazabilidad actividad-.tex-.bib"
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
          "justification": "Permite evaluar validez, coherencia y consecuencias."
        },
        {
          "source": "Filosofía del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "Integra el debate axiológico y normativo."
        },
        {
          "source": "Marco normativo y doctrinal",
          "target": "Conclusión jurídica transferible",
          "kind": "depends_on",
          "justification": "La conclusión requiere soporte verificable."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicación curricular y pauta editorial.",
        "Programa analítico: propósito y cinco ejes de trabajo.",
        "Bib local: recurrencia de claves UNAM/IIJ/SCJN.",
        "Actividad 1: patrón estable problema-conceptos-evidencia-análisis-conclusión."
      ]
    },
    "reinforcement_log": [
      "Ciclo 32: se eleva patrón argumentativo de actividad a materia sin copia literal.",
      "Ciclo 32: se refuerza bloqueo por JSON no parseable y normalización obligatoria.",
      "Ciclo 32: se preserva trazabilidad curricular y bibliográfica con deduplicación lossless.",
      "Ciclo 32: se mantienen referencias provisionales como supuestos hasta verificación."
    ]
  }
}