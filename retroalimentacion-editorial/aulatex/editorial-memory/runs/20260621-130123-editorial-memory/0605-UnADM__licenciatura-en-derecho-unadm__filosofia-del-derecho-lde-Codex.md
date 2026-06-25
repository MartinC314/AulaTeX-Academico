{
  "summary": [
    "Se consolida en materia la memoria válida de actividad-1 sin regresión.",
    "Se preserva identidad UnADM, trazabilidad curricular y control de calidad estructural.",
    "Se refuerza el patrón editorial base: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se mantiene compresión lossless por unión y deduplicación.",
    "Se mantiene normalización obligatoria de insumos no JSON parseable antes de propagar."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y propósito académico.",
    "Alinear la materia a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Marcar como [supuesto] todo dato no visible en la consigna o no verificado localmente.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local. [supuesto]",
    "Conservar referencia curricular verificable: malla-curricular-derecho-unadm.pdf."
  ],
  "structure_rules": [
    "Abrir cada producto con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el formato de entrega al producto solicitado en la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener trazabilidad entre actividad, archivo .tex y archivo .bib."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir que fuentes de semanas posteriores aplican a actividad-1. [supuesto]",
    "Confirmar correspondencia del producto con la consigna específica de cada actividad.",
    "Agregar fuentes específicas de actividad solo cuando sean verificables."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en texto y entradas en .bib.",
    "Confirmar que no se eliminen reglas útiles heredadas en cada ciclo."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar sin migración completa.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Tratar nombres anómalos de archivo como pendientes de corrección, no como canónicos. [supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Distinguir bibliografía base de materia y bibliografía específica por actividad.",
    "Registrar en .bib metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar entradas existentes y deduplicar sin pérdida.",
    "No completar entradas truncadas sin verificación local. [supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales verificadas en README, programa analítico y .bib local.",
    "Elevar al ancestro patrones reutilizables, no redacción literal de actividades.",
    "Conservar trazabilidad de citas recurrentes y reglas de calidad transferibles.",
    "Aplicar normalización manual en ciclos con insumos no estructurados.",
    "Evitar propagar como canónicos los placeholders o rutas con anomalías. [supuesto]"
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-1 para fijar plantilla final.",
    "Confirmar nombre canónico definitivo del .bib de la materia.",
    "Confirmar si actividad-1 reutiliza bibliografía existente o requiere .bib propio.",
    "Verificar integridad completa de la entrada scjnIncapacidadResistencia2019. [supuesto]",
    "Resolver en origen los placeholders $(@{...}.Slug) del README y programa analítico."
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
      "Problema jurídico o social delimitado.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable con cita.",
      "Análisis propio y postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en entregables académicos sólidos y trazables.",
      "Garantizar coherencia entre contenido jurídico, evidencia y criterio propio.",
      "Sostener una memoria editorial persistente sin pérdida de reglas útiles."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable y explícito.",
      "Marcado de [supuesto] cuando falte verificación.",
      "Cierre con aplicabilidad jurídica."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Definir objetivo.",
      "Exponer marco conceptual-normativo.",
      "Argumentar con evidencia verificable.",
      "Concluir con transferencia a práctica jurídica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofía del Derecho",
        "Hermenéutica e interpretación jurídica",
        "Argumentación jurídica",
        "Derecho y moral",
        "Justicia",
        "Análisis crítico del fenómeno jurídico",
        "Trazabilidad actividad-tex-bib"
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
          "justification": "La interpretación sustenta la construcción de razones jurídicas."
        },
        {
          "source": "Argumentación jurídica",
          "target": "Análisis crítico del fenómeno jurídico",
          "kind": "develops",
          "justification": "Permite evaluar validez, alcance y consecuencias normativas."
        },
        {
          "source": "Filosofía del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "Integra el debate entre validez normativa y contenido axiológico."
        },
        {
          "source": "Marco normativo y doctrinal",
          "target": "Conclusión jurídica transferible",
          "kind": "depends_on",
          "justification": "La conclusión exige fundamento verificable."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicación curricular y pauta editorial.",
        "Programa analítico: propósito y cinco ejes de trabajo.",
        "filosofia-del-derecho-clean.bib y filosofia-del-derecho.bib: base de trazabilidad bibliográfica.",
        "Memoria de actividad-1: patrón argumentativo estable y reusable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 20: se elevan reglas de actividad-1 al nivel materia por abstracción ascendente.",
      "Ciclo 20: se deduplican reglas y se conserva contenido útil sin recorte semántico.",
      "Ciclo 20: se mantiene bloqueo por no-JSON y normalización obligatoria.",
      "Ciclo 20: se preservan citas recurrentes y relaciones conceptuales transferibles."
    ]
  }
}