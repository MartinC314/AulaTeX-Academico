{
  "summary": [
    "Se consolida sincronizacion transversal desde actividad de Filosofia del Derecho hacia materia de Derecho financiero y bancario.",
    "Se preservan reglas institucionales UnADM y se deduplican sin perdida semantica.",
    "Se refuerza flujo editorial estable: problema, conceptos/normas, evidencia, analisis propio y conclusion juridica transferible.",
    "Se mantiene gate critico de JSON parseable y normalizacion previa a propagacion.",
    "Se confirma contexto local de destino: semestre 3, bloque 2, obligatoria, 8 creditos [verificado en README].",
    "Se conserva manejo de fuentes heredadas de motor como provisionales y auditables [supuesto operativo vigente]."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar Licenciatura en Derecho como programa academico del destino.",
    "Mantener datos curriculares verificados: semestre 3, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Conservar autoria y matricula locales del .tex mientras no haya instruccion oficial contraria.",
    "Marcar como supuesto todo dato no confirmado de docente, grupo o consigna.",
    "Tratar toda fuente heredada de motor como provisional hasta verificacion local."
  ],
  "structure_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener coherencia entre README, programa analitico, .tex y .bib.",
    "Corregir artefactos de plantilla en nombres de archivo antes de publicar."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar afirmaciones sin respaldo o sin marca de supuesto.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No transferir redaccion literal entre nodos no equivalentes; transferir solo patrones.",
    "Adaptar profundidad y formato a la consigna real de cada actividad."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Validar deduplicacion semantica antes de guardar memoria.",
    "Confirmar trazabilidad de cada regla a contexto local o memoria heredada.",
    "Bloquear si hay campos obligatorios vacios sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Mantener documentclass article en spanish, letterpaper, oneside salvo instruccion contraria.",
    "Mantener acentos y codificacion correctos en .tex y .bib.",
    "Reemplazar titulo y subtitulo de plantilla por los reales de la actividad antes de entrega.",
    "Completar Figura docente con dato real o etiqueta explicita de supuesto.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, citas rotas ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico."
  ],
  "bibliography_rules": [
    "Usar derecho-financiero-y-bancario.bib como archivo canonico de la materia.",
    "Mantener entradas base institucionales ya existentes.",
    "Agregar entradas BibTeX solo con fuente verificable.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/editorial o URL.",
    "Incluir fecha de consulta en referencias web.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas, generales y deduplicadas.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferir contenido tematico especifico de Filosofia del Derecho a Financiero/Bancario.",
    "Aplicar estrategia progresiva y conservadora: agregar mejoras verificables sin borrar reglas utiles.",
    "Si reaparece salida no estructurada, aplicar normalizacion manual antes de reuso."
  ],
  "open_questions": [
    "Confirmar nombre real de la figura docente en plantilla local.",
    "Confirmar formato obligatorio de citacion de la materia [supuesto: no definido].",
    "Confirmar si debe mostrarse grupo en tabla de identificacion.",
    "Confirmar si la localizacion de portada se mantiene por lineamiento institucional.",
    "Confirmar consigna y rubrica de la proxima actividad para ajustar profundidad argumentativa."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Sobrio y verificable.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Trazabilidad documental entre README, programa, .tex y .bib.",
        "No regresion de reglas utiles previas."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Derecho financiero y bancario.",
        "Semestre 3, bloque 2, obligatoria, 8 creditos.",
        "Fuente curricular institucional: malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Marco conceptual y normativo pertinente.",
      "Evidencia verificable.",
      "Analisis juridico propio.",
      "Conclusion transferible a practica profesional.",
      "Normalizacion estructurada previa a propagacion."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos consistentes y verificables.",
      "Asegurar continuidad editorial transversal sin contaminar nodos no equivalentes.",
      "Preservar memoria util con compresion lossless por union-dedupe."
    ],
    "style_markers": [
      "Frases directas y accionables.",
      "Supuestos marcados de forma explicita.",
      "Sin fuentes inventadas.",
      "Consistencia entre estructura, citas y cierre juridico."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Objetivo puntual.",
      "Conceptos y norma/doctrina aplicable.",
      "Analisis propio sustentado.",
      "Conclusion juridica aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Normalizacion estructurada",
        "Evidencia verificable",
        "Analisis juridico propio",
        "Conclusion transferible",
        "Consistencia .tex-.bib"
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
          "justification": "La identidad institucional exige verificabilidad y trazabilidad."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Consistencia .tex-.bib",
          "kind": "supports",
          "justification": "La normalizacion reduce errores de compilacion y de referencias."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis juridico propio",
          "kind": "supports",
          "justification": "El analisis gana validez cuando se sustenta en fuentes comprobables."
        },
        {
          "source": "Analisis juridico propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion profesional deriva del razonamiento argumentado."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Integridad academica",
          "kind": "depends_on",
          "justification": "Sin estructura verificable no hay auditoria confiable de fuentes y reglas."
        }
      ],
      "evidence": [
        "README de la materia: ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y ejes de trabajo.",
        "derecho-financiero-y-bancario.bib: fuentes institucionales base.",
        "Plantilla .tex local: metadatos academicos y campos pendientes."
      ]
    },
    "reinforcement_log": [
      "Ciclo 18: deduplicacion semantica aplicada sin eliminar reglas utiles previas.",
      "Ciclo 18: se refuerza gate JSON parseable como condicion de propagacion.",
      "Ciclo 18: se transfiere patron argumentativo estable y no contenido literal del nodo origen.",
      "Ciclo 18: se mantienen vacios locales como preguntas abiertas con marca de supuesto."
    ]
  }
}