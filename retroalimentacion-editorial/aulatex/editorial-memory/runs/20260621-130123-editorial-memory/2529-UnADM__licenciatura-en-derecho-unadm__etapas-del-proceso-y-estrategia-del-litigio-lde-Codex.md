{
  "summary": [
    "Se consolida sincronizacion transversal entre nodos no equivalentes con transferencia de abstracciones estables.",
    "Se preservan reglas utiles previas del destino y se deduplican sin recorte semantico.",
    "Se refuerzan ejes reutilizables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene gate obligatorio de JSON parseable antes de propagacion recursiva.",
    "Se conserva trazabilidad de fuentes provisionales como nota tecnica, no como autoridad academica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Usar tono academico-juridico formal, claro y verificable.",
    "Exigir postura propia sustentada; evitar neutralidad descriptiva.",
    "Marcar como [supuesto] todo dato no visible en consigna o documentos locales.",
    "Conservar trazabilidad de origen editorial en cada consolidacion.",
    "Registrar fuentes heredadas no verificadas como provisionales."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en bloques: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear estructura al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Aplicar los cinco ejes del programa analitico como columna estructural."
  ],
  "activity_rules": [
    "Verificar instruccion especifica de cada actividad antes de redactar.",
    "Rubricar cada entrega contra los cinco ejes editoriales.",
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Incluir analisis propio del estudiante en toda entrega.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Agregar fuentes especificas de actividad al .bib local antes de version final.",
    "No asumir reutilizacion automatica de fuentes de otras semanas o materias."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de fusionar memoria.",
    "Aplicar compresion lossless por union-dedupe sin eliminar reglas utiles previas.",
    "Confirmar que toda afirmacion factual tenga fuente o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Evitar contradicciones con reglas institucionales heredadas."
  ],
  "latex_rules": [
    "Usar plantilla .tex local de la materia como base.",
    "Conservar macros institucionales: documenttitle, coursename, coursecode, universityname.",
    "Mantener compatibilidad con espanol y letterpaper segun plantilla.",
    "No eliminar campos de portada; completar faltantes segun actividad.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y documentos auxiliares.",
    "Corregir nombres de archivo con caracteres anomalos antes de referenciar. [supuesto]"
  ],
  "bibliography_rules": [
    "Usar etapas-del-proceso-y-estrategia-del-litigio.bib como repositorio local.",
    "Conservar fuentes institucionales base ya registradas en la materia.",
    "No inventar referencias; usar solo obras consultables y verificables.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Registrar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Incluir fecha de consulta en fuentes web o institucionales dinamicas.",
    "No citar bibliografia no usada en el argumento."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales y estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "No propagar redaccion literal de actividades ni metadatos hiperlocales.",
    "Mantener advertencia de normalizacion manual para memorias heredadas no parseables (ciclos tempranos).",
    "Aplicar estrategia progresiva y conservadora: sumar sin regressiones."
  ],
  "open_questions": [
    "Confirmar si documentauthor debe ser fijo de plantilla o variable por estudiante. [supuesto]",
    "Confirmar estilo de citacion juridica exigido por la asignatura (APA, Chicago, ISO 690 u otro).",
    "Confirmar si existen requisitos de formato por tipo de producto visual.",
    "Confirmar correccion de entradas README con tokens sin resolver y lineas corruptas. [supuesto]",
    "Confirmar si coursecode LDE-S5B2 es definitivo a nivel institucional. [supuesto]"
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Juridicamente preciso.",
        "Claro y verificable.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta de asignatura como entrada canonica.",
        "Trazabilidad editorial en consolidaciones."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 5, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Etapas del proceso y estrategia del litigio."
      ]
    },
    "essence": [
      "Problema juridico o social como detonante.",
      "Fundamento conceptual y normativo pertinente.",
      "Evidencia verificable en soporte del argumento.",
      "Analisis propio con postura academica.",
      "Conclusion juridica aplicable a practica profesional."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos robustos.",
      "Asegurar coherencia entre consigna, desarrollo y cierre juridico.",
      "Sostener una memoria editorial persistente, estable y reusable."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Bloques argumentativos visibles.",
      "Citas trazables.",
      "Cierre juridico transferible.",
      "Marcado explicito de [supuesto] cuando aplique."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis propio -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> implicacion practica.",
      "Consigna -> objetivo -> desarrollo -> verificacion de rubrica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Cinco ejes editoriales",
        "JSON parseable",
        "Normalizacion estructurada",
        "Union-dedupe sin regresion",
        "Conclusion juridica transferible",
        "Fuentes provisionales no equivalen a autoridad academica"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "JSON parseable",
          "target": "Normalizacion estructurada",
          "kind": "depends_on",
          "justification": "Sin parseo valido no hay fusion segura."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Union-dedupe sin regresion",
          "kind": "supports",
          "justification": "Permite compresion lossless y evita perdida de reglas."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La secuencia editorial culmina en cierre aplicable."
        },
        {
          "source": "Identidad UnADM",
          "target": "Fuentes provisionales no equivalen a autoridad academica",
          "kind": "supports",
          "justification": "La integridad institucional exige distinguir provisionalidad."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "Bib local: claves institucionales verificables.",
        "Plantilla .tex: macros de portada y coursecode visible."
      ]
    },
    "reinforcement_log": [
      "Ciclo 17: se integra transferencia transversal desde actividad de otra materia como abstracciones estables.",
      "Ciclo 17: se preservan y refuerzan gates de parseo JSON y normalizacion previa.",
      "Ciclo 17: se mantiene compresion lossless por deduplicacion, sin recorte.",
      "Ciclo 17: no se incorporan fuentes nuevas no verificadas ni citas inventadas."
    ]
  }
}