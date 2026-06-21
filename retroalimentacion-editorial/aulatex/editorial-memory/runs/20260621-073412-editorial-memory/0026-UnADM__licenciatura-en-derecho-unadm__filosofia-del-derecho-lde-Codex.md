{
  "summary": [
    "Consolidar memoria de materia desde actividad-1 con abstraccion ascendente y deduplicacion lossless.",
    "Mantener identidad UnADM, trazabilidad curricular y control de calidad sin regresion.",
    "Preservar eje editorial comun: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Bloquear reutilizacion de salidas no JSON parseable hasta normalizacion estructurada."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, redaccion y formato.",
    "Alinear entregables con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica y punto de trazabilidad.",
    "Marcar como [supuesto] todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local. [supuesto]",
    "Usar malla-curricular-derecho-unadm.pdf como respaldo curricular verificado."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en secciones: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener trazabilidad entre actividad, .tex y .bib de la materia."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir fuentes de semanas posteriores para actividad-1. [supuesto]",
    "Validar que el producto final corresponda a la consigna especifica de la actividad."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No eliminar reglas utiles previas en ciclos posteriores."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar sin migracion completa.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo con caracteres anomalos antes de compilar. [supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de actividad en el .bib de la materia.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No completar entradas truncadas sin verificacion local (ej. scjnIncapacidadResistencia2019). [supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas por README, programa analitico y .bib local.",
    "Elevar patrones reutilizables; no copiar redaccion literal de actividades.",
    "Conservar trazabilidad de citas recurrentes y puertas de calidad institucional.",
    "Aplicar union-dedupe lossless en cada salto para evitar regresion.",
    "Mantener registro de riesgos de ingesta por salidas no parseables."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-1 para fijar plantilla definitiva. [supuesto]",
    "Confirmar nombre canonico final del .bib de la asignatura.",
    "Confirmar si filosofia-del-derecho-clean.bib es auxiliar o canonico para toda la materia. [supuesto]",
    "Completar y verificar campos faltantes de scjnIncapacidadResistencia2019. [supuesto]",
    "Confirmar rubrica de evaluacion para calibrar profundidad argumentativa."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Filosofia del Derecho."
      ]
    },
    "essence": [
      "Resolver problemas juridicos con fundamento conceptual y normativo.",
      "Convertir planeacion semanal en productos academicos trazables.",
      "Sostener analisis propio con evidencia verificable."
    ],
    "reason_for_being": [
      "Estandarizar calidad editorial de la materia en reportes y presentaciones.",
      "Garantizar coherencia entre consigna, argumentacion y conclusion juridica.",
      "Preservar memoria util sin perder reglas previas validadas."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable.",
      "Cierre juridico aplicable.",
      "Marcado explicito de [supuesto].",
      "Citas verificables en todo enunciado sustantivo."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer marco conceptual y normativo.",
      "Desarrollar analisis critico con postura propia.",
      "Concluir con transferencia a practica juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofia del Derecho",
        "Hermeneutica e interpretacion juridica",
        "Argumentacion juridica",
        "Derecho y moral",
        "Justicia",
        "Analisis critico del fenomeno juridico",
        "Problema-conceptos-evidencia-analisis-conclusion"
      ],
      "citations": [
        "hernandezManriquezHermeneutica2019",
        "scjnMemoriaArgumentacion2008",
        "scjnViolenciaFisica2022",
        "scjnIncapacidadResistencia2019",
        "noauthor_constitucion_nodate",
        "de_victimas_ley_2013",
        "ruiz_rodriguez_filosofia_derecho_2009",
        "rojas_gonzalez_filosofia_derecho_2018"
      ],
      "relations": [
        {
          "source": "Hermeneutica e interpretacion juridica",
          "target": "Argumentacion juridica",
          "kind": "supports",
          "justification": "La interpretacion sustenta la construccion de razones juridicas."
        },
        {
          "source": "Argumentacion juridica",
          "target": "Analisis critico del fenomeno juridico",
          "kind": "develops",
          "justification": "Permite evaluar validez, coherencia y consecuencias."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "La conclusion exige soporte normativo verificable."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "Integra debate axiologico y validez juridica."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "filosofia-del-derecho-clean.bib: referencias juridicas recurrentes.",
        "Actividad-1: patron estable de estructura argumentativa."
      ]
    },
    "reinforcement_log": [
      "Se elevo patron argumentativo de actividad a materia sin copia literal.",
      "Se reforzo regla de normalizacion previa para salidas no parseables.",
      "Se preservaron citas y conceptos transferibles con trazabilidad.",
      "Se consolidaron reglas de LaTeX y bibliografia sin eliminar controles previos."
    ]
  }
}