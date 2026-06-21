{
  "summary": [
    "Se consolida la memoria de materia desde Actividad 1 con abstraccion ascendente y deduplicacion lossless.",
    "Se preserva identidad UnADM, trazabilidad curricular y control de calidad sin regresion.",
    "Se elevan patrones transferibles: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene bloqueo de propagacion para salidas no JSON parseable y normalizacion previa obligatoria.",
    "Se conserva trazabilidad entre README, programa analitico, .tex y .bib de la materia."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y criterios de integridad academica.",
    "Alinear entregables a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica de la asignatura.",
    "Marcar como [supuesto] todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local. [supuesto]",
    "Conservar trazabilidad de fuentes provisionales heredadas Codex y GPT-Pro hasta sustitucion verificada. [supuesto]"
  ],
  "structure_rules": [
    "Iniciar cada producto con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear el formato final al producto solicitado por la planeacion semanal."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante y evitar entregas solo descriptivas.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir que bibliografia de semanas posteriores aplica a Actividad 1. [supuesto]",
    "Validar que el producto corresponda a la consigna especifica de cada actividad."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de [supuesto].",
    "Validar consistencia entre citas en texto y entradas en .bib."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables y no renombrarlas sin migracion completa.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico. [supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No completar entradas truncadas sin verificacion local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas por README, programa analitico y .bib local.",
    "Elevar patrones editoriales y de calidad desde actividad hacia materia sin copiar redaccion literal.",
    "Conservar trazabilidad de citas recurrentes y conceptos nucleares al subir de nivel.",
    "No propagar nombres de archivo anomalo hasta correccion local. [supuesto]",
    "Mantener estrategia union-dedupe lossless en cada ciclo."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 1 para fijar producto final.",
    "Confirmar nombre canonico final del .bib de la asignatura.",
    "Resolver definitivamente el placeholder $(@{...}.Slug) en README y programa analitico. [supuesto]",
    "Confirmar si filosofia-del-derecho-clean.bib se limita a Semana 7 o se reutiliza parcialmente en Actividad 1. [supuesto]",
    "Verificar integridad completa de la entrada scjnIncapacidadResistencia2019."
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
      "Problema juridico o social.",
      "Conceptos, normas y doctrina pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables academicos solidos y trazables.",
      "Garantizar coherencia entre identidad institucional, rigor argumentativo y practica juridica."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Seccionado estable y funcional.",
      "Postura propia sustentada.",
      "Marcado explicito de supuestos."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Desarrollar marco conceptual y normativo.",
      "Sostener analisis critico con evidencia.",
      "Cerrar con conclusion aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofia del Derecho",
        "Hermeneutica juridica",
        "Argumentacion juridica",
        "Derecho y moral",
        "Justicia",
        "Analisis critico del fenomeno juridico",
        "Trazabilidad editorial"
      ],
      "citations": [
        "hernandezManriquezHermeneutica2019",
        "scjnMemoriaArgumentacion2008",
        "scjnViolenciaFisica2022",
        "scjnIncapacidadResistencia2019",
        "ruiz_rodriguez_filosofia_derecho_2009",
        "rojas_gonzalez_filosofia_derecho_2018"
      ],
      "relations": [
        {
          "source": "Hermeneutica juridica",
          "target": "Argumentacion juridica",
          "kind": "supports",
          "justification": "La interpretacion fundamenta la construccion argumentativa."
        },
        {
          "source": "Argumentacion juridica",
          "target": "Analisis critico del fenomeno juridico",
          "kind": "develops",
          "justification": "Permite evaluar razones, normas y consecuencias."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "La conclusion exige respaldo normativo verificable."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "Integra debate axiologico y validez normativa."
        }
      ],
      "evidence": [
        "README de materia: pauta editorial e identidad.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "Bibliografia local: claves juridicas recurrentes y verificables.",
        "Actividad 1: patron problema-conceptos-evidencia-analisis-conclusion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 46: se transfieren patrones de Actividad 1 a materia con abstraccion ascendente.",
      "Ciclo 46: se elimina duplicidad formal y se preserva contenido util sin recorte semantico.",
      "Ciclo 46: se refuerzan puertas de calidad JSON, trazabilidad .tex/.bib y control de supuestos."
    ]
  }
}