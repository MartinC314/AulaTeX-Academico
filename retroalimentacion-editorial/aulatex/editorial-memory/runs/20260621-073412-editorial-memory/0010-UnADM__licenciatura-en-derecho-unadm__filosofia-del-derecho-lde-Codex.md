{
  "summary": [
    "Se consolida la memoria de materia desde actividad-1 con abstraccion ascendente y deduplicacion lossless.",
    "Se preservan reglas utiles previas sin regresion y se mantiene trazabilidad hacia fuentes locales.",
    "Se fija como obligatorio normalizar insumos no parseables antes de cualquier propagacion.",
    "Se refuerzan ejes editoriales transferibles: problema, conceptos, evidencia, analisis propio y conclusion juridica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y criterios de integridad academica.",
    "Alinear la materia a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica de actividades y entregables.",
    "Marcar como [supuesto] cualquier dato no visible en la consigna o no verificado localmente.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta sustitucion confirmada."
  ],
  "structure_rules": [
    "Abrir cada producto con encuadre breve del problema juridico o social.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear siempre el producto al tipo solicitado en planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Sustentar afirmaciones sustantivas con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir que fuentes de semanas posteriores aplican a actividad-1. [supuesto]",
    "Conservar trazabilidad entre actividad, archivo .tex y .bib de la materia."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Validar correspondencia del producto con la consigna de la actividad.",
    "Validar consistencia entre citas en texto y entradas del .bib."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar sin migracion completa.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) antes de fijar nombres canonicos."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente/editorial o URL.",
    "No completar entradas truncadas sin verificacion local. [supuesto]"
  ],
  "propagation_hints": [
    "Elevar al ancestro solo patrones reutilizables, no redaccion literal de actividad.",
    "Propagar recursivamente solo reglas verificadas por README, programa analitico y .bib local.",
    "Mantener etiqueta de compresion union-dedupe lossless en cada ciclo.",
    "Conservar trazabilidad de citas recurrentes y riesgos de ingesta no parseable.",
    "Evitar propagar nombres de archivo anomalos hasta corregirlos localmente. [supuesto]"
  ],
  "open_questions": [
    "Confirmar nombre canonico final del .bib de la materia tras resolver token Slug. [supuesto]",
    "Confirmar consigna exacta y rubrica de actividad-1 para afinar profundidad argumentativa. [supuesto]",
    "Confirmar si el .bib depurado de Semana 7 se reutiliza parcialmente en actividad-1. [supuesto]",
    "Verificar integridad completa de la entrada scjnIncapacidadResistencia2019. [supuesto]"
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
      "Problema juridico o social como punto de partida.",
      "Uso de conceptos, normas y doctrina pertinentes.",
      "Evidencia verificable con trazabilidad bibliografica.",
      "Analisis propio con postura academica.",
      "Conclusion juridica aplicable a la practica."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos rigurosos y transferibles.",
      "Estandarizar calidad editorial en reportes y presentaciones de la materia."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable y funcional.",
      "Cierre juridico con criterio propio.",
      "Marcado explicito de supuestos."
    ],
    "argumentative_patterns": [
      "Delimitacion del problema.",
      "Marco conceptual y normativo.",
      "Analisis critico con postura propia.",
      "Conclusion transferible con soporte normativo."
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
          "justification": "La interpretacion fundamenta la construccion de argumentos juridicos."
        },
        {
          "source": "Argumentacion juridica",
          "target": "Analisis critico del fenomeno juridico",
          "kind": "develops",
          "justification": "La argumentacion permite evaluar validez, razones y consecuencias."
        },
        {
          "source": "Marco normativo y doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "La conclusion requiere soporte normativo verificable."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "La materia integra debate axiologico y juridico."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "Bibliografia local: claves juridicas recurrentes y verificables.",
        "Actividad-1: patron estable problema-conceptos-evidencia-analisis-conclusion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 10: se elevo ADN editorial reusable desde actividad-1 hacia materia.",
      "Ciclo 10: se elimino duplicidad textual conservando contenido valido.",
      "Ciclo 10: se mantuvo regla de no propagacion sin normalizacion parseable.",
      "Ciclo 10: se reforzo trazabilidad entre identidad, estructura, citas y calidad."
    ]
  }
}