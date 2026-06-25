{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre actividad origen y materia destino.",
    "Se preservan reglas utiles previas sin recorte y con deduplicacion lossless.",
    "Se refuerzan abstracciones estables: identidad UnADM, cinco ejes editoriales, validacion estructural y trazabilidad.",
    "Se evita transferir redaccion literal o detalles exclusivos de Actividad 1 de otra asignatura.",
    "Se mantiene estado provisional de fuentes heredadas no verificadas como nota tecnica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 2, obligatoria, 8 creditos.",
    "Usar tono academico-juridico formal, claro y con postura propia sustentada.",
    "Marcar como [supuesto] todo dato no visible en consigna o documentos locales.",
    "Conservar trazabilidad de origen editorial en cada fusion de memoria.",
    "Registrar fuentes heredadas no verificadas como provisionales y no como autoridad academica."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear estructura al producto solicitado en planeacion semanal.",
    "Aplicar cinco ejes: problema, conceptos, producto solicitado, analisis propio, conclusion transferible.",
    "Cerrar con conclusion juridica aplicable a practica profesional."
  ],
  "activity_rules": [
    "Verificar instruccion especifica de cada actividad antes de redactar.",
    "Rubricar cada entrega contra los cinco ejes del programa analitico.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Incluir postura argumentada del estudiante en cada producto.",
    "Agregar fuentes especificas de actividad al .bib local antes de la version final."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de fusionar memoria.",
    "Aplicar union-dedupe sin eliminar reglas utiles previas.",
    "Confirmar que cada afirmacion factual tenga fuente o marca de [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar y normalizar salidas no estructuradas antes de reutilizar aguas abajo.",
    "Evitar contradicciones con reglas institucionales ya consolidadas."
  ],
  "latex_rules": [
    "Usar plantilla .tex local de la materia como base.",
    "Conservar macros institucionales de portada: documenttitle, coursename, coursecode, universityname.",
    "Mantener compatibilidad con espanol y letterpaper definidos en plantilla.",
    "No eliminar campos de portada; completar segun actividad.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo con caracteres anomales antes de compilar. [supuesto]"
  ],
  "bibliography_rules": [
    "Usar etapas-del-proceso-y-estrategia-del-litigio.bib como repositorio local.",
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/editorial o URL.",
    "Incluir fecha de consulta en fuentes web o institucionales dinamicas.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No citar bibliografia no usada en el argumento final."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales y estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "No propagar metadatos o redaccion literal de actividades de otra asignatura.",
    "Mantener advertencia de normalizacion manual para memorias heredadas no parseables.",
    "Reforzar en nodos vecinos la regla de JSON parseable previo a fusion."
  ],
  "open_questions": [
    "Confirmar estilo de citacion juridica requerido por la asignatura.",
    "Confirmar si documentauthor es fijo de plantilla o variable por estudiante. [supuesto]",
    "Confirmar correccion de tokens Slug sin expandir en README y programa analitico.",
    "Confirmar checklist minimo por tipo de producto: reporte, presentacion y visual.",
    "Confirmar si la fuente provisional Codex queda solo como nota tecnica historica."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Juridicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Entrada canonica en carpeta de asignatura."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 5, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Etapas del proceso y estrategia del litigio."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Fundamento conceptual y normativo.",
      "Producto alineado a planeacion.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos utiles, verificables y profesionalmente transferibles."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Bloques argumentativos visibles.",
      "Citas trazables.",
      "Cierre juridico aplicable.",
      "Marcado explicito de [supuesto] cuando falte evidencia local."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis propio -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> implicacion practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Cinco ejes editoriales",
        "JSON parseable",
        "Normalizacion estructurada",
        "Union-dedupe sin regresion",
        "Conclusion juridica transferible",
        "Trazabilidad editorial"
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
          "justification": "Permite compresion lossless sin perder reglas utiles."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La estructura culmina en cierre aplicable a practica."
        },
        {
          "source": "Identidad UnADM",
          "target": "Trazabilidad editorial",
          "kind": "supports",
          "justification": "La consistencia institucional exige historial verificable."
        }
      ],
      "evidence": [
        "README de materia y programa analitico local.",
        "Plantilla tex local con macros institucionales.",
        "Bib local con fuentes institucionales base."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: deduplicacion completa sin eliminar reglas validas previas.",
      "Ciclo 2: transferencia transversal limitada a abstracciones estables.",
      "Ciclo 2: reforzada regla de no usar fuentes provisionales como autoridad academica."
    ]
  }
}