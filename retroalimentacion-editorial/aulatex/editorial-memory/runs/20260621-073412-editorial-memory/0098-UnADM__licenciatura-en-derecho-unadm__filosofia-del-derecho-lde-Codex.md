{
  "summary": [
    "Consolidar memoria de materia con abstraccion ascendente desde actividad-1.",
    "Preservar reglas validas sin regresion mediante union-dedupe lossless.",
    "Mantener identidad UnADM, trazabilidad curricular y normalizacion estructurada obligatoria.",
    "Fijar eje transversal: problema, conceptos, evidencia, analisis propio y conclusion juridica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear la materia a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local. [supuesto]",
    "Usar malla-curricular-derecho-unadm.pdf como referencia curricular verificada."
  ],
  "structure_rules": [
    "Estructurar productos con: encuadre del problema, conceptos o marco normativo, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear cada entrega al producto solicitado por la planeacion semanal.",
    "Separar entregables por tipo en archivos dedicados: reporte y presentacion.",
    "Mantener trazabilidad entre actividad, .tex y .bib de materia."
  ],
  "activity_rules": [
    "Iniciar cada actividad con problema juridico o social delimitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir fuentes de semanas posteriores como obligatorias para actividad-1. [supuesto]",
    "Confirmar que el producto final corresponda a la consigna especifica de la actividad."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Validar que toda afirmacion sustantiva tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en .tex y entradas en .bib.",
    "Confirmar que no se eliminen reglas utiles previas en cada ciclo."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar sin migracion completa.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) antes de fijar nombres canonicos.",
    "Corregir nombres de archivo con caracteres anomalos del README antes de compilar. [supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "Registrar fuentes de actividad en el .bib de la asignatura.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente editorial o URL.",
    "No completar entradas truncadas sin verificacion local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas y estructuradas.",
    "Elevar al ancestro patrones reutilizables, no redaccion literal de actividades.",
    "Mantener trazabilidad de citas recurrentes y puertas de calidad institucional.",
    "Evitar propagar nombres de archivo placeholder hasta resolver tokens locales.",
    "Reforzar en nodos vecinos el patron editorial de cinco ejes."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-1 para validar tipo de producto. [supuesto]",
    "Confirmar nombre canonico final del .bib de la materia tras resolver token Slug.",
    "Confirmar si filosofia-del-derecho-clean.bib es solo apoyo de Semana 7 o base compartida. [supuesto]",
    "Verificar campos completos de scjnIncapacidadResistencia2019 en .bib local. [supuesto]",
    "Sustituir fuentes provisionales heredadas por evidencia local verificable."
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
        "Carpeta de materia como entrada canonica editorial."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Filosofia del Derecho."
      ]
    },
    "essence": [
      "Problema juridico o social que activa la asignatura.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion transferible a la practica juridica."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en entregables argumentativos verificables.",
      "Asegurar transferencia profesional del razonamiento juridico.",
      "Conservar coherencia editorial entre actividades y materia."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable por funcion argumentativa.",
      "Cierre con conclusion juridica aplicable.",
      "Marcado explicito de supuestos."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer marco conceptual y normativo.",
      "Analizar con postura propia sustentada.",
      "Cerrar con conclusion transferible a practica juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofia del Derecho",
        "Hermeneutica e interpretacion juridica",
        "Argumentacion juridica",
        "Derecho y moral",
        "Justicia",
        "Analisis critico del fenomeno juridico"
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
          "source": "Hermeneutica e interpretacion juridica",
          "target": "Argumentacion juridica",
          "kind": "supports",
          "justification": "La interpretacion sustenta la construccion de razones juridicas."
        },
        {
          "source": "Argumentacion juridica",
          "target": "Analisis critico del fenomeno juridico",
          "kind": "develops",
          "justification": "El analisis critico depende de razones explicitas y contrastables."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "La materia integra debate axiologico sobre validez y justicia."
        },
        {
          "source": "Marco normativo y doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "La conclusion exige respaldo normativo verificable."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "Actividad-1: patron estable problema-conceptos-evidencia-analisis-conclusion.",
        "Regla institucional: normalizar salidas no parseables antes de propagar."
      ]
    },
    "reinforcement_log": [
      "Se elevo del hijo al ancestro el patron argumentativo reutilizable.",
      "Se conservaron reglas de calidad y bloqueo por JSON no parseable.",
      "Se reforzo trazabilidad entre .tex, citas y .bib.",
      "Se mantuvieron fuentes provisionales marcadas como supuesto sin convertirlas en canon."
    ]
  }
}