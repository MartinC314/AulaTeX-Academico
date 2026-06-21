{
  "summary": [
    "Consolidar memoria de materia con abstracción ascendente desde actividad-1.",
    "Preservar reglas útiles previas sin regresión y con deduplicación lossless.",
    "Mantener identidad UnADM, trazabilidad curricular y entrada canónica en carpeta de materia.",
    "Aplicar normalización obligatoria a insumos no JSON parseable antes de propagar.",
    "Sostener eje editorial estable: problema, conceptos, evidencia, análisis propio y conclusión jurídica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en redacción y formato.",
    "Alinear entregables con Licenciatura en Derecho: semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar carpeta de materia como punto de entrada canónico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local. [supuesto]",
    "Usar malla-curricular-derecho-unadm.pdf como respaldo curricular verificado."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear cada producto al tipo solicitado en planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener trazabilidad entre actividad, archivo .tex y .bib de materia."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir que fuentes de semanas posteriores aplican a actividad-1. [supuesto]",
    "Agregar fuentes específicas de actividad solo tras verificación local."
  ],
  "quality_gates": [
    "Bloquear propagación si salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregado y consigna de actividad."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar sin migración completa.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Corregir nombres/rutas con caracteres anómalos antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico. [supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de materia y bibliografía específica de actividad.",
    "Registrar fuentes de actividad en .bib de materia con trazabilidad.",
    "No completar entradas truncadas sin verificación local. [supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas por README, programa analítico y .bib local.",
    "Elevar patrones reutilizables del hijo al ancestro sin copiar redacción literal.",
    "Conservar trazabilidad de citas recurrentes y puertas de calidad transferibles.",
    "Evitar propagar nombres de archivo anómalos hasta corrección local.",
    "Mantener etiqueta de compresión union-dedupe lossless en cada ciclo."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-1 y tipo de producto final. [supuesto]",
    "Confirmar nombre canónico definitivo del .bib de la materia. [supuesto]",
    "Confirmar si filosofia-del-derecho-clean.bib es solo Semana 7 o también base reutilizable. [supuesto]",
    "Verificar integridad completa de scjnIncapacidadResistencia2019 en .bib local. [supuesto]",
    "Sustituir fuentes provisionales heredadas por fuentes locales verificadas. [supuesto]"
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
      "Formar productos jurídicos con fundamento, evidencia y criterio propio.",
      "Conectar teoría filosófico-jurídica con aplicación profesional.",
      "Mantener consistencia metodológica en todas las actividades."
    ],
    "reason_for_being": [
      "Transformar planeación semanal en entregables verificables y argumentados.",
      "Asegurar continuidad editorial entre actividades y nivel materia.",
      "Garantizar calidad técnica LaTeX y calidad académica jurídica."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable y explícito.",
      "Cierre con conclusión jurídica aplicable.",
      "Marcado explícito de [supuesto] cuando falte evidencia local."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer marco conceptual y normativo.",
      "Analizar con postura propia.",
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
        "Eje problema-conceptos-evidencia-análisis-conclusión"
      ],
      "citations": [
        "ruiz_rodriguez_filosofia_derecho_2009",
        "rojas_gonzalez_filosofia_derecho_2018",
        "hernandezManriquezHermeneutica2019",
        "scjnMemoriaArgumentacion2008",
        "scjnViolenciaFisica2022",
        "scjnIncapacidadResistencia2019",
        "noauthor_constitucion_nodate",
        "de_victimas_ley_2013"
      ],
      "relations": [
        {
          "source": "Hermenéutica e interpretación jurídica",
          "target": "Argumentación jurídica",
          "kind": "supports",
          "justification": "La interpretación sostiene la construcción de razones jurídicas."
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
          "justification": "Integra discusión axiológica y normatividad."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusión jurídica transferible",
          "kind": "depends_on",
          "justification": "La conclusión requiere sustento verificable."
        }
      ],
      "evidence": [
        "README de materia: pauta editorial e identidad.",
        "Programa analítico: propósito y cinco ejes de trabajo.",
        "Bib local: claves jurídicas recurrentes verificables.",
        "Actividad-1: patrón argumentativo estable transferible al nivel materia."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas manteniendo cobertura completa.",
      "Se reforzó normalización JSON como puerta de entrada obligatoria.",
      "Se elevó el patrón editorial de actividad-1 a regla de materia reutilizable.",
      "Se preservaron citas y conceptos trazables sin inventar fuentes.",
      "Se marcaron incertidumbres operativas con etiqueta [supuesto]."
    ]
  }
}