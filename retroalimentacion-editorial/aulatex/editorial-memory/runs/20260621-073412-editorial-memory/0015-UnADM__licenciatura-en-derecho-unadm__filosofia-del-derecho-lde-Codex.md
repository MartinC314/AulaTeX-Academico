{
  "summary": [
    "Se consolida la memoria de materia con abstracción ascendente desde actividad-1, sin regresión.",
    "Se preserva compresión lossless por unión y deduplicación de reglas, conceptos y trazas.",
    "Se mantiene como núcleo editorial: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se refuerza control de ingesta: normalizar insumos no JSON parseable antes de propagar.",
    "Se integra trazabilidad curricular verificada con README y programa analítico de la materia."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, redacción y formato.",
    "Alinear entregables con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de materia como entrada canónica de actividades y entregables.",
    "Marcar como [supuesto] todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local. [supuesto]",
    "Usar malla-curricular-derecho-unadm.pdf como respaldo curricular verificado.",
    "No eliminar reglas heredadas útiles de calidad y normalización."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Alinear cada producto al tipo solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener trazabilidad entre actividad, archivo .tex y archivo .bib de materia."
  ],
  "activity_rules": [
    "Delimitar el problema de la actividad al inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir que fuentes de semanas posteriores aplican a actividad-1. [supuesto]",
    "Agregar fuentes específicas de actividad solo cuando sean verificables."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en texto y entradas del .bib.",
    "Verificar correspondencia del producto con la consigna de la actividad."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "No renombrar claves citadas sin migración completa.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir nombres/rutas anómalas antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Registrar fuentes de actividad en el .bib de la asignatura.",
    "No completar entradas truncadas sin verificación local. [supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Elevar al ancestro reglas reutilizables de identidad, calidad, argumentación y trazabilidad.",
    "No propagar redacción literal de actividades; propagar patrones editoriales.",
    "Mantener etiqueta de compresión union-dedupe lossless en cada ciclo.",
    "Evitar regresiones frente a reglas útiles ya consolidadas.",
    "Si falta consigna textual, propagar solo reglas generales verificadas."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-1 para fijar producto final.",
    "Confirmar nombre canónico definitivo del .bib de la asignatura.",
    "Confirmar si actividad-1 reutiliza .bib existente o requiere .bib propio.",
    "Resolver placeholder Slug en README/programa analítico. [supuesto]",
    "Verificar integridad completa de scjnIncapacidadResistencia2019. [supuesto]"
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
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable.",
      "Análisis propio y postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en entregables académicos sólidos.",
      "Garantizar coherencia entre identidad institucional, método argumentativo y evidencia.",
      "Sostener trazabilidad editorial entre consigna, .tex y .bib."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable y explícito.",
      "Marcado de supuestos cuando falte dato verificable.",
      "Cierre con criterio jurídico propio."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer marco conceptual y normativo.",
      "Evaluar con análisis crítico y postura propia.",
      "Concluir con aplicabilidad jurídica profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofía del Derecho",
        "Hermenéutica e interpretación jurídica",
        "Argumentación jurídica",
        "Derecho y moral",
        "Justicia",
        "Análisis crítico del fenómeno jurídico",
        "Trazabilidad editorial",
        "Normalización de ingesta"
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
          "justification": "Abre el debate entre validez normativa y dimensión axiológica."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusión jurídica transferible",
          "kind": "depends_on",
          "justification": "La conclusión exige soporte normativo verificable."
        }
      ],
      "evidence": [
        "README de materia: identidad y pauta editorial.",
        "Programa analítico: propósito y cinco ejes de trabajo.",
        "Bib local: claves jurídicas recurrentes y verificables.",
        "Actividad-1: patrón problema-conceptos-evidencia-análisis-conclusión."
      ]
    },
    "reinforcement_log": [
      "Ciclo 15: se eleva patrón de actividad a regla de materia sin pérdida semántica.",
      "Ciclo 15: se deduplican reglas repetidas y se conservan todas las útiles.",
      "Ciclo 15: se mantiene bloqueo por JSON no parseable y normalización obligatoria.",
      "Ciclo 15: se refuerza trazabilidad curricular y bibliográfica verificable."
    ]
  }
}