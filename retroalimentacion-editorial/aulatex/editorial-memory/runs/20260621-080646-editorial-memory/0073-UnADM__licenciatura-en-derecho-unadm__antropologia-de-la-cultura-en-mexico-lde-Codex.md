{
  "summary": [
    "Sincronizacion transversal consolidada con union-dedupe lossless y sin regresion.",
    "Se preserva identidad UnADM del destino y se transfieren solo abstracciones estables del origen.",
    "Se refuerzan ejes reutilizables: objetivo, problema, conceptos, evidencia, analisis propio y cierre transferible.",
    "Se mantiene bloqueo por salida no JSON parseable y normalizacion previa obligatoria.",
    "Se evita traslado de contenido tematico exclusivo de Filosofia del Derecho al nodo de Antropologia."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar toda fuente heredada no verificada como provisional hasta validacion local.",
    "No transferir metadatos curriculares especificos de otra asignatura."
  ],
  "structure_rules": [
    "Iniciar con objetivo puntual y encuadre breve del problema juridico o social.",
    "Separar secciones en: conceptos clave, marco normativo o teorico, analisis propio y cierre.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias canonicas de estructura.",
    "Cerrar con conclusion transferible a la practica juridica."
  ],
  "activity_rules": [
    "Definir objetivo de la actividad antes del desarrollo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Evitar afirmaciones juridicas o culturales sin puente argumentativo."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa del esquema antes de reutilizar.",
    "Revisar y normalizar respuestas no estructuradas antes de propagar.",
    "Confirmar que toda afirmacion tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No promover reglas provisionales a definitivas sin validacion disciplinar."
  ],
  "latex_rules": [
    "Usar configuracion en espanol coherente con la plantilla local.",
    "Mantener clase y formato base salvo justificacion academica.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Mantener campos institucionales completos y consistentes.",
    "Resolver placeholders tipo $(@{...}.Slug) en README, programa y rutas antes de compilar.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales pertinentes.",
    "Registrar fuentes especificas de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No citar claves ausentes en el .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y abstractas entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates y grafo conceptual.",
    "Evitar transferencia literal de redaccion o contenido tematico local del origen.",
    "Mantener compresion lossless por deduplicacion, sin recorte.",
    "Registrar incidencias de parseo como alertas reutilizables inter-materias.",
    "Si falta contexto local, conservar cerebro minimo y abrir vacios como preguntas."
  ],
  "open_questions": [
    "Supuesto: falta confirmacion institucional del estandar unico de citas para la licenciatura.",
    "Supuesto: confirmar si LDE-S4B2 es clave oficial o local.",
    "Confirmar si todas las actividades de Antropologia exigen conclusion juridica explicita.",
    "Confirmar producto exacto por actividad cuando la consigna semanal no este disponible.",
    "Confirmar que no quedan placeholders activos en archivos de la materia."
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
        "Semestre 4, bloque 2, obligatoria, 8 creditos.",
        "Asignatura destino: Antropologia de la cultura en Mexico."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros, trazables y utiles para practica profesional.",
      "Sostener coherencia institucional y tecnica en toda entrega LaTeX."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados cuando falte evidencia.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente verificable -> interpretacion propia.",
      "Coherencia entre consigna, desarrollo y cierre."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON parseable",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Resolucion de placeholders"
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
          "justification": "Sin parseo valido no hay propagacion confiable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura personal requiere respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "El cierre util deriva del razonamiento argumentado."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "La pauta institucional exige integridad academica."
        }
      ],
      "evidence": [
        "README de materia: identidad UnADM, ubicacion curricular y pauta editorial.",
        "Programa analitico: ejes problema, conceptos, producto, analisis y cierre.",
        "Bib local: unadmSitioWeb y unadmMallaDerecho2024.",
        "Memoria heredada: alerta de salidas no estructuradas y normalizacion manual."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin perdida semantica.",
      "Se conservaron gates criticos de parseo y normalizacion.",
      "Se incorporaron abstracciones estables del origen sin arrastrar contenido tematico de Filosofia del Derecho.",
      "Se reforzo control de placeholders en rutas y nombres de archivo."
    ]
  }
}