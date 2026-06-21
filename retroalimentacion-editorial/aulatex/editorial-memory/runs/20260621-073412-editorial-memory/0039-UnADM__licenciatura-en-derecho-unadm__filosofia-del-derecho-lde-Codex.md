{
  "summary": [
    "Se consolida en materia la memoria valida de actividad-1 con abstraccion ascendente.",
    "Se preservan reglas utiles previas sin regresion y con deduplicacion lossless.",
    "Se mantiene identidad UnADM, trazabilidad curricular y control de normalizacion JSON.",
    "Se refuerzan ejes editoriales transferibles: problema, conceptos, evidencia, analisis propio y conclusion juridica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y redaccion.",
    "Alinear entregables con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica de asignatura.",
    "Marcar como [supuesto] todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local. [supuesto]",
    "Usar malla-curricular-derecho-unadm.pdf como respaldo curricular verificado."
  ],
  "structure_rules": [
    "Iniciar cada producto con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear formato final al producto solicitado en la planeacion semanal.",
    "Mantener trazabilidad entre actividad, archivo .tex y archivo .bib de materia."
  ],
  "activity_rules": [
    "Delimitar problema juridico o social desde la primera seccion.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir fuentes de semanas posteriores para actividad-1 sin evidencia local. [supuesto]",
    "Verificar correspondencia exacta entre producto entregado y consigna de actividad."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en texto y entradas en .bib.",
    "Confirmar en cada ciclo que no se eliminen reglas utiles previas."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar sin migracion completa.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Corregir caracteres anomalos en rutas y nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "No fijar como canon nombres con placeholder hasta verificacion local. [supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de actividad en el .bib de la asignatura.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No completar entradas truncadas sin verificacion local. [supuesto]",
    "Conservar trazabilidad de claves recurrentes de SCJN, UNAM e institucionales."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas por README, programa analitico y .bib local.",
    "Elevar al ancestro patrones reutilizables, no redaccion literal de actividad.",
    "Reusar puertas de calidad institucional en nodos laterales de Derecho.",
    "Aplicar union-dedupe lossless en cada ciclo para evitar regresion.",
    "Registrar salidas no parseables como riesgo de ingesta sin perder reglas utiles.",
    "Mantener ciclos 1 y 2 como nodos con normalizacion manual obligatoria si se reutilizan."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-1 para cerrar supuestos de formato. [supuesto]",
    "Confirmar nombre canonico final del archivo .bib de la materia.",
    "Confirmar si filosofia-del-derecho-clean.bib es solo de Semana 7 o reutilizable en actividad-1. [supuesto]",
    "Completar y verificar entrada truncada scjnIncapacidadResistencia2019 en .bib local. [supuesto]",
    "Confirmar rubrica especifica para ajustar profundidad argumentativa."
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
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico y utilidad profesional.",
      "Asegurar coherencia entre identidad institucional, evidencia y argumentacion."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable.",
      "Postura propia explicita.",
      "Cierre juridico aplicado.",
      "Marcado explicito de [supuesto]."
    ],
    "argumentative_patterns": [
      "Delimitacion del problema.",
      "Marco conceptual y normativo.",
      "Analisis critico con evidencia.",
      "Sintesis con postura propia.",
      "Conclusion aplicable a practica juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofia del Derecho",
        "Hermeneutica e interpretacion juridica",
        "Argumentacion juridica",
        "Derecho y moral",
        "Justicia",
        "Analisis critico del fenomeno juridico",
        "Trazabilidad editorial actividad-materia"
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
          "justification": "La interpretacion fundamenta la construccion de razones juridicas."
        },
        {
          "source": "Argumentacion juridica",
          "target": "Analisis critico del fenomeno juridico",
          "kind": "develops",
          "justification": "La argumentacion permite evaluar validez, coherencia y consecuencias."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "La asignatura integra debate axiologico y normativo."
        },
        {
          "source": "Marco normativo y doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "La conclusion profesional exige soporte verificable."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "Actividad-1: patron problema-conceptos-evidencia-analisis-conclusion.",
        "Regla persistente: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 39: se eleva memoria de actividad-1 al nivel materia sin perdida de reglas.",
      "Ciclo 39: se deduplican variantes ortograficas y se conserva contenido valido.",
      "Ciclo 39: se refuerza normalizacion obligatoria para insumos no estructurados.",
      "Ciclo 39: se preserva trazabilidad de citas recurrentes y control de supuestos."
    ]
  }
}