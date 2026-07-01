{
  "summary": [
    "Se sincroniza memoria transversal con reglas estables reutilizables y sin copiar redaccion literal.",
    "Se conserva identidad UnADM, estructura de cinco ejes y cierre juridico transferible.",
    "Se mantiene compresion lossless por union-dedupe con no regresion.",
    "Se preserva incidente historico de JSON no parseable hasta verificacion de cierre.",
    "Se refuerza normalizacion de README y programa por placeholders de slug y rutas corruptas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre exacto de asignatura: Derecho de la contratacion internacional.",
    "Vincular a Licenciatura en Derecho, semestre 6, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna o planeacion.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar trazabilidad del origen transversal: filosofia-del-derecho-lde/actividad-1."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto pedido por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "No eliminar reglas utiles previas; solo anexar mejoras verificables."
  ],
  "activity_rules": [
    "Diferenciar resumen descriptivo y postura propia.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Vincular cada argumento con norma, doctrina, dato o evidencia.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Declarar limites del analisis cuando falten datos de actividad.",
    "No asumir fuentes de semanas distintas sin confirmacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Verificar que nombres de archivos del README coincidan con archivos reales."
  ],
  "latex_rules": [
    "Mantener clase article en espanol con letterpaper y oneside cuando aplique.",
    "Conservar macros institucionales y no sustituirlas por texto libre sin necesidad.",
    "Completar documenttitle y documentsubtitle segun actividad real.",
    "Usar acentos y codificacion correctos en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Resolver placeholders sin expandir tipo $(@{...}.Slug) en README y programa.",
    "Corregir rutas corruptas detectadas en README antes de referenciar."
  ],
  "bibliography_rules": [
    "Usar derecho-de-la-contratacion-internacional.bib como repositorio principal.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas consultables.",
    "No inventar referencias ni citar heredadas no usadas en destino.",
    "Agregar fuentes especificas por actividad en el .bib local.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente o URL.",
    "Incluir fecha de consulta en recursos web o mutables."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir solo abstracciones estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "No sobrescribir reglas locales mas especificas con reglas generales.",
    "Mantener aviso de incidente JSON hasta evidencia de resolucion.",
    "Aplicar union-dedupe semantica por regla, no por recorte textual."
  ],
  "open_questions": [
    "Supuesto: persiste incidencia historica de JSON no parseable; confirmar cierre en este ciclo.",
    "Confirmar checklist minimo por tipo de producto: reporte, presentacion y visual.",
    "Confirmar formato uniforme de cita juridica para norma, jurisprudencia y doctrina.",
    "Supuesto: README y programa aun requieren correccion final de placeholders y rutas.",
    "Confirmar si existe rubrica oficial de actividades para ajustar profundidad argumentativa."
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
        "Entrada canonica por carpeta de materia.",
        "Trazabilidad de herencias editoriales."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 6, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Derecho de la contratacion internacional."
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Marco conceptual y normativo pertinente.",
      "Analisis propio sustentado.",
      "Cierre con transferencia profesional.",
      "Control explicito de supuestos."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros, fundamentados y verificables.",
      "Asegurar coherencia entre consigna, evidencia y conclusion juridica.",
      "Sostener una memoria editorial estable y reusable sin regresiones."
    ],
    "style_markers": [
      "Frases directas y accionables.",
      "Secciones funcionales con orden fijo.",
      "Supuestos etiquetados de forma explicita.",
      "Cierre juridico aplicable a practica."
    ],
    "argumentative_patterns": [
      "Problema -> marco normativo/doctrinal -> analisis -> conclusion.",
      "Afirmacion -> evidencia verificable -> inferencia juridica.",
      "Descripcion breve -> postura propia sustentada."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion JSON",
        "Trazabilidad editorial",
        "Problema juridico",
        "Marco normativo y doctrinal",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Control de supuestos"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La identidad exige formato consistente y citas verificables."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin delimitacion del problema no hay analisis juridico valido."
        },
        {
          "source": "Marco normativo y doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion requiere fundamento verificable."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Trazabilidad editorial",
          "kind": "supports",
          "justification": "La estructura parseable permite auditoria y propagacion segura."
        },
        {
          "source": "Control de supuestos",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita presentar con certeza datos no confirmados."
        }
      ],
      "evidence": [
        "README de materia con identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico con proposito y cinco ejes de trabajo.",
        "Bib local con fuentes institucionales base.",
        "Incidente historico de salidas no estructuradas registrado en memoria."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas entre origen y destino sin perdida semantica.",
      "Se transfirieron solo abstracciones editoriales estables por relacion transversal.",
      "Se evitaron citas y contenidos tematicos especificos de Filosofia del Derecho no pertinentes al destino.",
      "Se reforzaron gates de JSON, supuestos y consistencia bib-texto.",
      "Se preservaron reglas locales de materia y se anadieron mejoras verificables."
    ]
  }
}