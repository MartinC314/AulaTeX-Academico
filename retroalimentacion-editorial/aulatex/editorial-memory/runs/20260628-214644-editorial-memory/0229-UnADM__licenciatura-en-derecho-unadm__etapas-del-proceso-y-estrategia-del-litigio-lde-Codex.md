{
  "summary": [
    "Sincronizacion transversal ciclo 2 aplicada con estrategia progresiva y conservadora.",
    "Se preservan reglas estables del origen y del destino sin recorte.",
    "Se refuerza compresion lossless por union-dedupe y control de no regresion.",
    "Se mantiene validacion JSON parseable como puerta obligatoria de propagacion.",
    "Se priorizan abstracciones reutilizables: identidad, estructura, calidad y grafo conceptual."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables a Licenciatura en Derecho, semestre 5, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Conservar trazabilidad de origen editorial en cada consolidacion.",
    "Marcar como [supuesto] todo dato no visible en consigna o documento local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Usar macros de portada: documenttitle, coursename, coursecode, universityname.",
    "Usar coursecode LDE-S5B2 mientras no exista correccion institucional. [supuesto]"
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto pedido por planeacion semanal.",
    "Seguir cinco ejes editoriales: problema, conceptos, producto, analisis propio, conclusion transferible.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Verificar instruccion especifica de cada actividad antes de redactar.",
    "Rubricar cada entrega contra los cinco ejes del programa analitico.",
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Incluir postura argumentada del estudiante y evitar entrega solo descriptiva.",
    "Agregar fuentes especificas de actividad al .bib local antes de la version final.",
    "No reutilizar reglas laterales sin comprobar pertinencia juridica local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la memoria no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que toda afirmacion factual tenga fuente o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Aplicar union-dedupe sin eliminar reglas utiles previas.",
    "Confirmar ausencia de contradicciones con reglas institucionales heredadas."
  ],
  "latex_rules": [
    "Usar la plantilla .tex local de la materia como base.",
    "Mantener compatibilidad con espanol y letterpaper segun plantilla.",
    "No eliminar campos de portada; completar faltantes segun actividad.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Mantener claves BibTeX estables para evitar rupturas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo corruptos en README antes de referenciar. [supuesto]"
  ],
  "bibliography_rules": [
    "Usar etapas-del-proceso-y-estrategia-del-litigio.bib como repositorio local.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Incluir fecha de consulta cuando la fuente sea web o institucional dinamica.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No citar bibliografia base si no fue usada en el argumento."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales y estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "No propagar redaccion literal ni metadatos hiperlocales de una actividad.",
    "Mantener advertencia de normalizacion manual para memorias heredadas no parseables.",
    "Preservar union-dedupe sin regresion en ciclos posteriores."
  ],
  "open_questions": [
    "Confirmar estilo de citacion juridica requerido por la asignatura (APA, Chicago, ISO 690 u otro).",
    "Confirmar si documentauthor debe ser fijo de plantilla o variable por estudiante. [supuesto]",
    "Confirmar existencia operativa de plantilla de presentacion en el destino. [supuesto]",
    "Validar correccion final de tokens Slug sin expandir en README y programa analitico.",
    "Confirmar si la fuente provisional GPT-Pro debe quedar solo como nota tecnica."
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
        "Carpeta de asignatura como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 5, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Etapas del proceso y estrategia del litigio."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas y doctrina pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y utiles para practica juridica.",
      "Sostener coherencia institucional y calidad verificable en toda entrega."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones claras y reutilizables.",
      "Citas trazables.",
      "Cierre juridico con criterio propio.",
      "Marcado explicito de [supuesto] cuando falte evidencia local."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> implicacion practica.",
      "Consigna -> desarrollo alineado -> verificacion por rubrica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Cinco ejes editoriales",
        "Integridad academica",
        "Evidencia verificable",
        "Conclusion juridica transferible",
        "Normalizacion JSON",
        "Compresion union-dedupe sin perdida"
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
          "justification": "La identidad exige trazabilidad y citas verificables."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La secuencia metodologica culmina en cierre aplicable."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Compresion union-dedupe sin perdida",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay fusion segura sin recorte."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Toda afirmacion requiere fuente o marca [supuesto]."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "Archivo .bib local con claves institucionales base.",
        "Plantilla .tex con macros institucionales y coursecode LDE-S5B2. [supuesto operativo]"
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: se conserva validacion JSON parseable como gate duro.",
      "Ciclo 2: se mantiene union-dedupe lossless y no regresion.",
      "Ciclo 2: se refuerzan cinco ejes editoriales como patron transversal estable.",
      "Ciclo 2: se evita transferencia literal de contenido disciplinar de Filosofia del Derecho.",
      "Ciclo 2: se conservan vacios locales abiertos con preguntas accionables."
    ]
  }
}