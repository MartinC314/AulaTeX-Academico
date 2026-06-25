{
  "summary": [
    "Se mantiene sincronizacion transversal entre nodos con enfoque conservador y sin regresion.",
    "Se transfieren solo abstracciones estables: identidad UnADM, ejes de trabajo, calidad y trazabilidad.",
    "Se refuerza normalizacion obligatoria de salidas no estructuradas antes de propagacion.",
    "Se conserva criterio nuclear: problema, conceptos, evidencia, analisis propio y conclusion juridica."
  ],
  "identity_rules": [
    "Mantener identidad explicita UnADM en tono, portada y metadatos.",
    "Conservar materia destino exacta: Derecho de la propiedad y registro.",
    "Conservar programa: Licenciatura en Derecho.",
    "Conservar ubicacion curricular verificada: semestre 7, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al entregable pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener transformacion de planeacion en reporte o presentacion segun consigna."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante y evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Relacionar el desarrollo con propiedad y registro cuando aplique.",
    "No asumir fuentes de semanas posteriores sin validacion de consigna.",
    "Verificar correspondencia entre producto final y actividad solicitada."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar que no existan placeholders sin resolver antes de entrega."
  ],
  "latex_rules": [
    "Mantener clase article con opciones spanish, letterpaper y oneside salvo instruccion distinta.",
    "Usar acentos y codificacion en espanol correctos en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Verificar rutas y nombres de archivo reales antes de automatizar.",
    "Corregir campos incompletos en portada y tabla de autor."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Usar derecho-de-la-propiedad-y-registro.bib como archivo local canonico de la materia.",
    "Agregar fuentes especificas por actividad en el .bib local.",
    "No inventar referencias; usar solo obras consultables o archivos locales existentes.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas, estables y no ambiguas.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "No transferir redaccion literal ni contenido tematico exclusivo de Filosofia del Derecho.",
    "Mantener compresion lossless por union y deduplicacion.",
    "Si falta contexto local en nodos hijos, crear base minima y abrir preguntas."
  ],
  "open_questions": [
    "Confirmar rubrica local de evaluacion por actividad en esta materia.",
    "Confirmar estilo de citacion juridica exigido por figura docente.",
    "Confirmar si cada actividad requiere reporte, presentacion u otro formato.",
    "Supuesto: persisten tokens corruptos en README/programa; confirmar si ya fueron saneados.",
    "Confirmar nombre definitivo de figura docente para sustituir placeholder."
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
        "Normalizacion estructurada antes de propagacion.",
        "Entrada canonica por carpeta de asignatura."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 7, bloque 1, obligatoria, 8 creditos.",
        "Materia: Derecho de la propiedad y registro.",
        "Codigo local: LDE-S7B1."
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
      "Convertir planeacion semanal en productos academicos claros y verificables.",
      "Asegurar fundamento juridico y trazabilidad de fuentes.",
      "Sostener continuidad editorial entre actividades y materia."
    ],
    "style_markers": [
      "Frases breves y accionables.",
      "Supuestos etiquetados de forma explicita.",
      "Sin afirmaciones sin fuente.",
      "Sin placeholders al cierre."
    ],
    "argumentative_patterns": [
      "Del problema al marco conceptual.",
      "Del marco normativo a la evidencia.",
      "De la evidencia al analisis propio.",
      "Del analisis a una conclusion aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad academica",
        "Normalizacion JSON",
        "Problema juridico",
        "Marco normativo/doctrinal",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion transferible",
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
          "justification": "La identidad institucional exige rigor formal y verificabilidad."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Trazabilidad bibliografica",
          "kind": "supports",
          "justification": "La estructura valida permite control de consistencia entre reglas y fuentes."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis debe responder al problema formulado."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica requiere fundamento legal y doctrinal."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Las citas comprobables evitan afirmaciones infundadas."
        }
      ],
      "evidence": [
        "README de la materia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y ejes de trabajo.",
        "derecho-de-la-propiedad-y-registro.bib: claves institucionales existentes."
      ]
    },
    "reinforcement_log": [
      "Ciclo 5: deduplicacion completa de reglas repetidas y preservacion de reglas utiles previas.",
      "Ciclo 5: transferencia transversal limitada a abstracciones estables, sin arrastre de contenido tematico no equivalente.",
      "Ciclo 5: refuerzo de gates criticos: JSON parseable, supuestos marcados, citas trazables.",
      "Ciclo 5: mantenimiento del ADN editorial UnADM con estructura argumentativa reusable."
    ]
  }
}