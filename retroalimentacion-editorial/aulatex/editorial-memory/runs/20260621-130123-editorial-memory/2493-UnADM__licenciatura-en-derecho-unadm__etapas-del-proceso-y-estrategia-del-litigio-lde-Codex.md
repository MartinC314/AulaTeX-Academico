{
  "summary": [
    "Se consolida sincronizacion transversal en materia destino con compresion lossless por union-dedupe.",
    "Se preservan reglas estables del origen: normalizacion estructurada, cinco ejes editoriales y conclusion juridica con criterio propio.",
    "Se evita transferencia literal de actividad; solo se propagan abstracciones editoriales reutilizables.",
    "Se mantiene bloqueo de propagacion para salidas no JSON parseable.",
    "Se refuerza trazabilidad de fuentes provisionales como nota tecnica y no como autoridad academica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Usar tono academico-juridico formal, claro y argumentativo.",
    "Exigir postura propia sustentada en evidencia verificable.",
    "Marcar como [supuesto] todo dato no visible en consigna o documentos locales.",
    "Conservar trazabilidad de origen editorial en cada fusion de memoria.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Aplicar cinco ejes editoriales: problema, conceptos, producto solicitado, analisis propio, conclusion transferible.",
    "Alinear estructura al producto solicitado en planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Verificar instruccion especifica de cada actividad antes de redactar.",
    "Rubricar cada entrega contra los cinco ejes del programa analitico.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Asegurar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Agregar fuentes especificas de actividad al .bib local antes de version final."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de fusionar memoria.",
    "Confirmar que cada afirmacion factual tenga fuente o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Comprobar union-dedupe sin eliminar reglas utiles previas.",
    "Normalizar manualmente cualquier herencia no estructurada antes de reutilizar.",
    "Validar que relaciones del grafo usen tipos permitidos: supports, contrasts, depends_on, develops."
  ],
  "latex_rules": [
    "Usar plantilla .tex local de la materia como base.",
    "Conservar macros institucionales de portada y curso.",
    "Mantener compatibilidad con espanol y letterpaper.",
    "No eliminar campos de portada; completar segun actividad.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Mantener claves BibTeX estables para evitar roturas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo con caracteres corruptos visibles en README. [supuesto]"
  ],
  "bibliography_rules": [
    "Usar etapas-del-proceso-y-estrategia-del-litigio.bib como repositorio local.",
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "No inventar referencias; usar solo fuentes consultables.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Incluir fecha de consulta en fuentes web o institucionales dinamicas.",
    "No citar bibliografia no usada en el argumento."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales y estables entre nodos no equivalentes.",
    "Priorizar identidad, gates de calidad, estructura reusable y grafo conceptual.",
    "No propagar metadatos locales de actividad origen al nivel materia destino.",
    "Aplicar validacion JSON y no regresion antes de cualquier fusion lateral o ascendente.",
    "Si falta contexto local en nodos vecinos, crear cerebro editorial minimo y dejar vacios en open_questions."
  ],
  "open_questions": [
    "Confirmar estilo de citacion juridica requerido por la asignatura.",
    "Confirmar si documentauthor es fijo de plantilla o variable por estudiante. [supuesto]",
    "Confirmar correccion final de coursecode LDE-S5B2 en documentos oficiales. [supuesto]",
    "Confirmar y corregir rutas con caracteres corruptos en README.",
    "Confirmar checklist minimo por tipo de producto: reporte, presentacion, material visual."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Claro y verificable."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta de asignatura como entrada canonica.",
        "Fuentes provisionales separadas de autoridad academica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 5, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Etapas del proceso y estrategia del litigio."
      ]
    },
    "essence": [
      "Cinco ejes editoriales como columna vertebral.",
      "Problema juridico y cierre transferible a practica profesional.",
      "Normalizacion estructurada previa a toda propagacion.",
      "Compresion lossless por union-dedupe sin regresion."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos solidos, verificables y aplicables.",
      "Asegurar continuidad editorial entre nodos con control de calidad estricto."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Bloques argumentativos visibles.",
      "Citas trazables.",
      "Marcado explicito de [supuesto] cuando aplique.",
      "Cierre juridico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis propio -> conclusion juridica.",
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
        "Integridad academica y citas verificables"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica y citas verificables",
          "kind": "supports",
          "justification": "La pauta editorial institucional exige verificabilidad y forma academica."
        },
        {
          "source": "JSON parseable",
          "target": "Normalizacion estructurada",
          "kind": "depends_on",
          "justification": "Sin formato parseable no hay fusion confiable."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Union-dedupe sin regresion",
          "kind": "supports",
          "justification": "La deduplicacion lossless requiere estructura consistente."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La estructura de ejes conduce a un cierre aplicable y argumentado."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "Bib local: fuentes institucionales registradas.",
        "Plantilla tex local: macros y metadatos institucionales."
      ]
    },
    "reinforcement_log": [
      "Ciclo 8: deduplicacion completa de reglas repetidas en summary, identidad, estructura y gates.",
      "Ciclo 8: se conservaron reglas utiles heredadas y se eliminaron redundancias literales.",
      "Ciclo 8: se reforzo transferencia transversal por abstracciones estables, sin arrastre de redaccion de actividad.",
      "Ciclo 8: se mantuvo separacion entre fuentes provisionales y autoridad academica."
    ]
  }
}