{
  "summary": [
    "Se consolida sincronizacion transversal entre nodos no equivalentes con transferencia de abstracciones estables.",
    "Se preservan reglas utiles previas y se aplica deduplicacion lossless sin recorte semantico.",
    "Se refuerzan ejes comunes reutilizables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene bloqueo de propagacion para salidas no JSON parseable y normalizacion obligatoria.",
    "Supuesto: no hay consigna local de actividad especifica en destino; se conserva cerebro editorial minimo de materia."
  ],
  "identity_rules": [
    "Mantener identidad explicita UnADM en tono, portada y metadatos.",
    "Usar nombre exacto de materia: Derecho de la propiedad y registro.",
    "Conservar programa: Licenciatura en Derecho.",
    "Registrar ubicacion curricular local: semestre 7, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No propagar metadatos curriculares de otra materia al destino."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al entregable pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Transformar planeacion en reporte, presentacion o producto visual segun consigna.",
    "Verificar nombres reales de archivo en README antes de automatizar rutas.",
    "Resolver tokens no expandidos de Slug en README y programa analitico."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Vincular cada actividad con el producto solicitado por su consigna.",
    "No asumir fuentes de semanas posteriores sin validacion local.",
    "Relacionar desarrollo con propiedad y registro cuando aplique.",
    "Distinguir problema, fundamento, analisis y cierre argumentativo."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar que el producto final corresponda a la consigna activa.",
    "Confirmar que no existan placeholders sin resolver antes de entrega."
  ],
  "latex_rules": [
    "Conservar plantilla base .tex de la materia como punto de partida.",
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Completar metadatos academicos obligatorios antes de compilar.",
    "Corregir campos incompletos de portada y tabla de autor antes de entrega.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en rutas y nombres de archivo."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Usar el .bib local de la materia para fuentes especificas.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Agregar fuentes de actividad en derecho-de-la-propiedad-y-registro.bib.",
    "Mantener trazabilidad entre cita en texto y entrada BibTeX."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas, estables y no ambiguas.",
    "Compartir solo abstracciones editoriales entre nodos transversales.",
    "Evitar transferir redaccion literal o contenido tematico exclusivo del origen.",
    "Preservar estrategia progresiva y conservadora sin regresiones.",
    "Si falta contexto local, mantener cerebro editorial minimo y abrir vacios como preguntas."
  ],
  "open_questions": [
    "Confirmar rubrica de evaluacion local para Derecho de la propiedad y registro.",
    "Confirmar si cada actividad exige reporte, presentacion u otro formato.",
    "Confirmar estilo de citacion juridica solicitado por figura docente.",
    "Confirmar sustitucion del placeholder 'Figura docente' en plantilla .tex.",
    "Supuesto: tokens corruptos en README requieren correccion manual definitiva."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador en inferencias."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Entrada canonica por carpeta de asignatura.",
        "Normalizacion estructurada obligatoria antes de propagacion."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 7, bloque 1, obligatoria, 8 creditos.",
        "Materia: Derecho de la propiedad y registro.",
        "Codigo local: LDE-S7B1."
      ]
    },
    "essence": [
      "Problema juridico claro.",
      "Fundamento conceptual y normativo.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica aplicable."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos consistentes.",
      "Garantizar trazabilidad argumentativa y bibliografica.",
      "Sostener identidad institucional y calidad tecnica en LaTeX."
    ],
    "style_markers": [
      "Frases breves y accionables.",
      "Supuestos marcados explicitamente.",
      "Sin afirmaciones sin fuente.",
      "Sin placeholders al cierre."
    ],
    "argumentative_patterns": [
      "Del problema al marco conceptual.",
      "Del marco normativo a la evidencia.",
      "De la evidencia al analisis propio.",
      "Del analisis a la conclusion transferible."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Problema juridico",
        "Marco normativo o doctrinal",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion JSON",
        "Trazabilidad bibliografica"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige forma consistente y citas verificables."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis debe responder al problema planteado."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion requiere fundamento juridico explicito."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia segura."
        },
        {
          "source": "Trazabilidad bibliografica",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La consistencia cita-.bib evita afirmaciones no verificables."
        }
      ],
      "evidence": [
        "README de la materia: pauta editorial e identidad institucional.",
        "Programa analitico: proposito y ejes de trabajo.",
        "Bib local: claves institucionales existentes.",
        "Regla persistente: bloquear salidas no JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 11: deduplicacion lossless aplicada sobre reglas transversales estables.",
      "Ciclo 11: se conserva gate critico de JSON parseable sin cambios.",
      "Ciclo 11: se refuerza patron argumentativo comun sin transferir contenido tematico de Filosofia del Derecho.",
      "Ciclo 11: se mantienen vacios locales como preguntas abiertas para no inventar contexto."
    ]
  }
}