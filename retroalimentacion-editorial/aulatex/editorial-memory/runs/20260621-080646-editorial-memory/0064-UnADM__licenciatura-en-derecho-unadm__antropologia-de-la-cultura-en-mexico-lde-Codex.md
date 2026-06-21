{
  "summary": [
    "Sincronizacion transversal conservadora aplicada desde actividad de Filosofia del Derecho hacia materia de Antropologia.",
    "Se preservan reglas utiles previas del destino sin eliminaciones.",
    "Se agregan solo abstracciones estables: objetivo, evidencia, postura propia, coherencia y cierre transferible.",
    "Se evita transferir contenido tematico especifico de Filosofia del Derecho.",
    "Se mantiene compresion lossless por union-dedupe y control de no regresion.",
    "Se refuerza normalizacion estructurada por antecedente de salidas no JSON parseable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener contexto curricular local del destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar toda fuente heredada no verificada como provisional.",
    "No trasladar metadatos curriculares de Filosofia del Derecho a Antropologia."
  ],
  "structure_rules": [
    "Abrir cada entrega con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones reutilizables: conceptos, marco pertinente, analisis propio y cierre.",
    "Alinear el producto al entregable pedido por la planeacion semanal.",
    "Distinguir artefactos: reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias canonicas de estructura."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones relevantes con fuente verificable y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Evitar extrapolar fuentes o instrucciones de semanas distintas sin confirmacion.",
    "Cerrar con conclusion transferible a la practica juridica."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar esquema minimo completo antes de reutilizar memoria.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Verificar consistencia entre citas en texto y archivo .bib.",
    "No promover reglas provisionales a definitivas sin validacion local."
  ],
  "latex_rules": [
    "Mantener configuracion en espanol coherente con la plantilla local.",
    "Mantener clase y formato base salvo justificacion academica.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Conservar claves BibTeX estables para evitar quiebres de compilacion.",
    "Corregir rutas con caracteres truncados detectadas en README.",
    "Resolver tokens dinamicos tipo $(@{...}.Slug) a nombres literales antes de compilar."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes consultables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales pertinentes.",
    "Registrar fuentes de cada actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener trazabilidad de archivos locales usados como evidencia institucional."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates y grafo conceptual sobre redaccion literal.",
    "Etiquetar como supuesto toda inferencia no confirmada del destino.",
    "Mantener alertas de parseo como conocimiento transversal reutilizable.",
    "Aplicar estrategia progresiva: reforzar primero calidad y consistencia, luego ampliar detalle local."
  ],
  "open_questions": [
    "Supuesto: falta confirmacion de rubrica especifica por actividad en la materia destino.",
    "Confirmar estandar unico de citacion para la licenciatura.",
    "Confirmar si coursecode LDE-S4B2 es oficial institucional o convencion local.",
    "Confirmar si la conclusion juridica es obligatoria en todas las actividades de Antropologia.",
    "Confirmar resolucion definitiva de nombres corruptos en README."
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
        "Entrada canonica por carpeta de materia."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Antropologia de la cultura en Mexico.",
        "Semestre 4, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema claro.",
      "Conceptos pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Cierre juridico transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables y utiles.",
      "Sostener coherencia institucional y calidad tecnica en LaTeX y bibliografia."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Conclusiones con aplicacion profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente -> interpretacion propia.",
      "Pregunta guia -> desarrollo coherente -> respuesta final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON parseable",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Propagacion transversal conservadora"
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
          "justification": "Sin parseo valido no hay memoria reutilizable confiable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura academica se legitima con respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "El cierre profesional deriva del razonamiento y no del resumen."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Propagacion transversal conservadora",
          "kind": "supports",
          "justification": "La identidad comun permite transferir reglas estables entre materias."
        }
      ],
      "evidence": [
        "README y programa analitico del destino establecen ejes editoriales comunes.",
        "Memoria origen confirma gates de parseo y normalizacion como reglas estables.",
        "Bibliografia local del destino confirma base institucional verificable."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas de origen y destino sin perdida funcional.",
      "Se reforzaron gates de JSON y normalizacion por historial de fallas de parseo.",
      "Se conservaron reglas locales de Antropologia y se añadieron solo abstracciones transferibles.",
      "Se excluyo transferencia de conceptos tematicos exclusivos de Filosofia del Derecho."
    ]
  }
}