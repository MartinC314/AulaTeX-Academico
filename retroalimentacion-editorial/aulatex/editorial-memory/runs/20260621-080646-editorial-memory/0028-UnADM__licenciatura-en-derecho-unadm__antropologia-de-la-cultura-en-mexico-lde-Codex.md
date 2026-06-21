{
  "summary": [
    "Sincronizacion transversal consolidada con union-dedupe lossless y sin regresion.",
    "Se preserva identidad UnADM y contexto local de Antropologia de la cultura en Mexico.",
    "Se transfieren solo abstracciones estables desde Filosofia del Derecho: objetivo, evidencia, postura y coherencia.",
    "Se mantiene bloqueo de propagacion para salidas no JSON parseable.",
    "Se refuerza resolucion de placeholders en README, programa y rutas de archivos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener materia destino: Antropologia de la cultura en Mexico.",
    "Conservar ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar toda fuente heredada no verificada como provisional.",
    "No trasladar metadatos curriculares de Filosofia del Derecho al destino."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o teorico, analisis propio y cierre.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Distinguir artefactos: reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias canonicas.",
    "Guardar fuentes de actividad en antropologia-de-la-cultura-en-mexico.bib."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Evitar extrapolar contenidos tematicos exclusivos de Filosofia del Derecho.",
    "Cerrar con conclusion transferible a la practica juridica."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa del esquema requerido.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que toda afirmacion tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregado y consigna local.",
    "No promover reglas provisionales a definitivas sin validacion disciplinar."
  ],
  "latex_rules": [
    "Usar codificacion en espanol consistente en .tex y .bib.",
    "Mantener clase y parametros base de plantilla salvo justificacion academica.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Mantener claves BibTeX estables.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens dinamicos tipo $(@{...}.Slug) a nombres literales.",
    "Corregir rutas truncadas o con caracteres anomalos antes de compilar."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes consultables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "No citar claves inexistentes en el .bib local.",
    "Mantener entradas base unadmSitioWeb y unadmMallaDerecho2024."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y abstractas.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferir redaccion literal y contenidos disciplinares no equivalentes.",
    "Registrar incidencias de parseo como alertas reutilizables inter-materias.",
    "Preservar reglas utiles previas sin eliminacion en ciclos futuros."
  ],
  "open_questions": [
    "Supuesto: falta consigna puntual de actividades locales; confirmar productos exactos por semana.",
    "Confirmar estandar unico de citacion institucional para la licenciatura.",
    "Confirmar si coursecode LDE-S4B2 es definitivo institucional.",
    "Confirmar si la conclusion juridica es obligatoria en todas las actividades de la materia.",
    "Confirmar correccion final de rutas truncadas detectadas en README."
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
        "Integridad academica con trazabilidad.",
        "Entrada canonica por carpeta de materia."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 4, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Antropologia de la cultura en Mexico."
      ]
    },
    "essence": [
      "Problema, conceptos, evidencia, analisis propio y conclusion transferible.",
      "Sincronizacion transversal conservadora y progresiva.",
      "Compresion lossless por deduplicacion sin recorte."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables.",
      "Garantizar coherencia argumentativa y utilidad profesional.",
      "Asegurar continuidad editorial entre nodos no equivalentes."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Cierre con criterio juridico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente verificable -> interpretacion propia.",
      "Pregunta guia -> desarrollo alineado -> respuesta final coherente."
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
          "justification": "La postura se legitima con respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion util surge del razonamiento."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables."
        }
      ],
      "evidence": [
        "README local define identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico local fija ejes problema-conceptos-producto-analisis-cierre.",
        "Bib local contiene unadmSitioWeb y unadmMallaDerecho2024.",
        "Memoria origen aporta gates estables de parseo, estructura y trazabilidad."
      ]
    },
    "reinforcement_log": [
      "Ciclo 28: se consolidan abstracciones estables sin traslado tematico de Filosofia del Derecho.",
      "Ciclo 28: se mantiene regla de bloqueo por JSON no parseable.",
      "Ciclo 28: se refuerza politica de supuestos y fuentes provisionales.",
      "Ciclo 28: se preserva deduplicacion lossless y no regresion."
    ]
  }
}