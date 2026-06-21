{
  "summary": [
    "Sincronizacion transversal consolidada con union-dedupe lossless y sin regresion.",
    "Se preservan reglas institucionales UnADM, estructura canonica y gates de calidad.",
    "Se transfieren solo abstracciones estables desde actividad de Filosofia del Derecho.",
    "Se evita transferir contenido tematico especifico de Filosofia al nodo de Antropologia.",
    "Se refuerza normalizacion obligatoria ante salidas no JSON parseables.",
    "Se confirma contexto destino: semestre 4, bloque 2, obligatoria, 8 creditos [verificado en README].",
    "Se mantiene manejo de fuentes heredadas no verificadas como provisionales [supuesto hasta validacion local]."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Usar la carpeta de materia como entrada canonica.",
    "Mantener datos curriculares locales del destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "No trasladar metadatos curriculares de otras materias.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar toda fuente heredada no verificada como provisional."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear el entregable al producto solicitado en la planeacion semanal.",
    "Separar artefactos: reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias de estructura.",
    "Resolver placeholders de nombres de archivo antes de usar rutas."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar productos solo descriptivos.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion.",
    "Integrar puente argumentativo entre dimension cultural y juridica."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar esquema minimo completo antes de reutilizar memoria.",
    "Normalizar manualmente respuestas no estructuradas antes de propagar.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregado y consigna vigente.",
    "No promover reglas provisionales a definitivas sin validacion local."
  ],
  "latex_rules": [
    "Usar configuracion en espanol coherente con la plantilla local.",
    "Mantener clase base y formato institucional salvo justificacion academica.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir caracteres truncados o anomalias en rutas antes de compilar.",
    "Resolver tokens dinamicos tipo $(@{...}.Slug) en README, programa y rutas.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Usar solo obras verificables y consultables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales pertinentes.",
    "Registrar fuentes especificas por actividad en el .bib local de la materia.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y abstractas.",
    "Priorizar identidad, estructura reusable y gates de calidad en nodos no equivalentes.",
    "Evitar propagacion de redaccion literal o contenido tematico local.",
    "Mantener estrategia progresiva y conservadora: agregar sin borrar reglas utiles previas.",
    "Registrar alertas de parseo como conocimiento transversal reutilizable."
  ],
  "open_questions": [
    "Confirmar rubrica oficial de evaluacion para actividades de la materia destino.",
    "Confirmar estandar de citacion institucional unico para la licenciatura.",
    "Confirmar si la conclusion juridica es obligatoria en todas las actividades de antropologia.",
    "Confirmar si la clave de curso LDE-S4B2 es oficial o convenio local.",
    "Validar cierre definitivo de fuentes heredadas provisionales [supuesto pendiente]."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con trazabilidad de fuentes.",
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Antropologia de la cultura en Mexico.",
        "Semestre 4, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema.",
      "Conceptos.",
      "Evidencia.",
      "Analisis propio.",
      "Conclusion transferible."
    ],
    "reason_for_being": [
      "Convertir la planeacion semanal en productos academicos verificables.",
      "Sostener calidad editorial uniforme entre materias.",
      "Preservar identidad institucional y rigor argumentativo."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente -> interpretacion propia.",
      "Consigna -> desarrollo alineado -> cierre coherente."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON parseable",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Separacion de artefactos editoriales",
        "Manejo de supuestos"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Validacion JSON parseable",
          "target": "Normalizacion estructurada",
          "kind": "depends_on",
          "justification": "La propagacion confiable exige parseo valido."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura argumentativa requiere respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion util deriva del razonamiento."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Separacion de artefactos editoriales",
          "kind": "supports",
          "justification": "La consistencia institucional mejora control y evaluacion."
        }
      ],
      "evidence": [
        "README de la materia destino.",
        "Programa analitico de la materia destino.",
        "Archivo BibTeX local con fuentes institucionales."
      ]
    },
    "reinforcement_log": [
      "Ciclo 76: deduplicacion completa de reglas repetidas.",
      "Ciclo 76: refuerzo de gates JSON y normalizacion manual.",
      "Ciclo 76: transferencia limitada a abstracciones estables transversales.",
      "Ciclo 76: preservacion de reglas utiles previas sin eliminacion."
    ]
  }
}