{
  "summary": [
    "Se sincroniza memoria transversal desde actividad origen a materia destino con estrategia conservadora.",
    "Se preservan reglas institucionales UnADM, estructura de cinco ejes y control de supuestos.",
    "Se mantiene compresion lossless por union-dedupe sin eliminar reglas utiles previas.",
    "Se refuerza gate critico: bloquear propagacion si la salida no es JSON parseable.",
    "Se consolidan abstracciones estables y se evita transferir contenido literal de otra asignatura."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre exacto de asignatura: Derecho de la contratacion internacional.",
    "Vincular la materia a Licenciatura en Derecho, semestre 6, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en consigna o planeacion oficial.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar trazabilidad del origen transversal: filosofia-del-derecho-lde/actividad-1."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear cada entrega al producto solicitado en la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Transformar planeacion en reporte, presentacion o producto visual segun consigna.",
    "Corregir placeholders y rutas corruptas del README antes de reutilizar nombres de archivo."
  ],
  "activity_rules": [
    "Identificar problema juridico o social que activa la actividad.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Diferenciar resumen descriptivo de postura argumentada del estudiante.",
    "Vincular argumentos con norma, doctrina o evidencia verificable.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Declarar limites del analisis cuando falten datos de consigna.",
    "No asumir fuentes de otras semanas o materias sin validacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que nombres de archivos en README coincidan con archivos reales.",
    "Normalizar respuestas no estructuradas antes de propagacion recursiva.",
    "No sobrescribir reglas locales mas especificas con reglas transversales."
  ],
  "latex_rules": [
    "Mantener plantilla article en espanol con letterpaper y oneside cuando aplique.",
    "Conservar macros institucionales de curso, universidad y autor.",
    "Completar \\documenttitle y \\documentsubtitle segun actividad real.",
    "Evitar paquetes o comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Usar codificacion y acentos correctos en .tex y .bib.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico."
  ],
  "bibliography_rules": [
    "Usar derecho-de-la-contratacion-internacional.bib como repositorio principal local.",
    "No inventar referencias; incluir solo fuentes consultables.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Agregar fuentes especificas por actividad en el .bib local.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Incluir fecha de consulta en fuentes web o mutables.",
    "No citar fuentes heredadas de origen si no fueron usadas en destino."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar propagar redaccion literal, citas no verificadas o rutas corruptas.",
    "Aplicar union-dedupe semantico por regla sin recorte informativo.",
    "Mantener etiqueta de incidencia historica JSON hasta cierre verificado.",
    "Registrar en cada salto la relacion transversal y el ciclo de consolidacion."
  ],
  "open_questions": [
    "Supuesto: persiste incidencia historica de salida no JSON parseable; confirmar cierre.",
    "Confirmar formato uniforme de cita juridica para norma, jurisprudencia y doctrina.",
    "Confirmar checklist minimo por tipo de actividad: reporte, presentacion y visual.",
    "Confirmar planeacion oficial de actividades de la materia para ajustar granularidad.",
    "Supuesto: README y programa aun requieren correccion de placeholders de Slug.",
    "Confirmar si existe rubrica institucional especifica para conclusion juridica transferible."
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
        "Trazabilidad editorial de herencias.",
        "Entrada canonica por carpeta de materia."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 6, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Derecho de la contratacion internacional."
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Conceptos y marco normativo pertinentes.",
      "Producto alineado a planeacion.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables.",
      "Garantizar fundamento juridico, evidencia y criterio propio.",
      "Asegurar reutilizacion segura de memoria editorial en propagacion transversal."
    ],
    "style_markers": [
      "Frases directas y accionables.",
      "Secciones funcionales con orden estable.",
      "Supuestos etiquetados de forma explicita.",
      "Cierre con aplicacion profesional concreta."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis -> conclusion.",
      "Afirmacion -> evidencia verificable -> inferencia juridica.",
      "Descripcion breve -> postura propia sustentada."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion JSON",
        "Integridad academica",
        "Trazabilidad editorial",
        "Problema juridico",
        "Marco normativo y doctrinal",
        "Analisis propio",
        "Conclusion juridica transferible"
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
          "justification": "La identidad institucional exige citas verificables y formato consistente."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Trazabilidad editorial",
          "kind": "supports",
          "justification": "La estructura parseable permite auditoria y propagacion segura."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere delimitacion previa del problema."
        },
        {
          "source": "Marco normativo y doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion profesional valida depende del sustento juridico."
        },
        {
          "source": "Estructura de cinco ejes",
          "target": "Calidad editorial de entregas",
          "kind": "develops",
          "justification": "El patron estabiliza coherencia entre consigna, desarrollo y cierre."
        }
      ],
      "evidence": [
        "README de materia con ubicacion curricular y pauta editorial.",
        "Programa analitico con proposito y cinco ejes de trabajo.",
        "Bib local existente como repositorio base verificable.",
        "Incidencia historica documentada de salidas no JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 1: se deduplican reglas repetidas sin perdida semantica.",
      "Ciclo 1: se conservan gates criticos de parseo JSON y validacion estructural.",
      "Ciclo 1: se refuerza politica de supuestos y fuentes provisionales.",
      "Ciclo 1: se ancla correccion de tokens Slug no expandidos como mejora verificable.",
      "Ciclo 1: se prioriza transferencia de abstracciones estables sobre contenido literal."
    ]
  }
}