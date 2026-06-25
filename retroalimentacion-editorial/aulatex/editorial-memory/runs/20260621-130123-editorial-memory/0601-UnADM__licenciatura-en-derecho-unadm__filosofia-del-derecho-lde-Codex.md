{
  "summary": [
    "Se consolida memoria de materia desde actividad-1 con abstraccion ascendente y deduplicacion lossless.",
    "Se preservan reglas utiles previas sin regresion y se normalizan variantes duplicadas.",
    "Se refuerza identidad UnADM, trazabilidad curricular y control de calidad de ingesta JSON.",
    "Se elevan patrones transferibles: problema, conceptos, evidencia, analisis propio y conclusion juridica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en redaccion y formato.",
    "Alinear entregables con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en la consigna. [supuesto]",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local. [supuesto]",
    "Usar malla-curricular-derecho-unadm.pdf como respaldo curricular verificado."
  ],
  "structure_rules": [
    "Usar la materia como nodo canonico para reportes, presentaciones y bibliografia.",
    "Iniciar cada producto con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear cada entrega al producto solicitado por la planeacion semanal.",
    "Mantener trazabilidad entre actividad, .tex y .bib de la materia."
  ],
  "activity_rules": [
    "Delimitar problema juridico o social al inicio.",
    "Integrar conceptos, normas, doctrina o datos pertinentes.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante y evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir que fuentes de semanas posteriores aplican automaticamente a actividad-1. [supuesto]"
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar correspondencia entre citas en .tex y entradas en .bib.",
    "Confirmar que no se eliminen reglas utiles previas en cada ciclo."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables y no renombrarlas sin migracion completa.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Tratar nombres anomalo-placeholder como pendientes y no como canon definitivo. [supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "Registrar fuentes de actividad en el .bib de la asignatura con metadatos minimos.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar deduplicacion sin perdida y trazabilidad de claves citadas.",
    "No completar entradas truncadas sin verificacion local. [supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas por README, programa analitico y .bib local.",
    "Elevar a ancestros patrones editoriales y puertas de calidad, no redaccion literal de actividades.",
    "Conservar trazabilidad de citas recurrentes y su estado de verificacion.",
    "Aplicar union-dedupe lossless en cada salto y registrar incidencias de ingesta.",
    "Mantener ciclos con normalizacion manual cuando existan salidas no estructuradas."
  ],
  "open_questions": [
    "Confirmar nombre canonico final del .bib de la materia frente al token Slug en README. [supuesto]",
    "Confirmar consigna textual exacta de actividad-1 y su tipo de producto principal. [supuesto]",
    "Confirmar si filosofia-del-derecho-clean.bib se restringe a Semana 7 o se reutiliza por actividad. [supuesto]",
    "Completar y verificar campos faltantes de scjnIncapacidadResistencia2019. [supuesto]",
    "Sustituir fuentes provisionales heredadas por fuentes locales verificadas. [supuesto]"
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
      "Problema juridico o social.",
      "Conceptos y marco normativo/doctrinal.",
      "Evidencia verificable.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir la planeacion semanal en productos academicos trazables y utiles para practica juridica.",
      "Garantizar consistencia editorial entre actividades, fuentes y entregables LaTeX."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable.",
      "Marcado explicito de supuestos.",
      "Cierre con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer marco conceptual y normativo.",
      "Contrastar evidencia y doctrina.",
      "Sostener postura propia.",
      "Concluir con implicacion profesional."
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
          "justification": "La interpretacion fundamenta la construccion de razones juridicas."
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
          "justification": "La conclusion requiere soporte verificable."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "Integra debate axiologico y validez normativa."
        }
      ],
      "evidence": [
        "README de materia: identidad y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "Bib local: claves juridicas recurrentes y trazables.",
        "Regla estable: bloquear propagacion ante JSON no parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 19: deduplicacion semantica aplicada sin perdida de reglas utiles.",
      "Ciclo 19: patrones de actividad-1 elevados a nivel materia como reglas transferibles.",
      "Ciclo 19: se conserva trazabilidad de citas recurrentes y estado provisional cuando aplica."
    ]
  }
}