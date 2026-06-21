{
  "summary": [
    "Sincronizacion transversal consolidada con union-dedupe lossless y sin regresion.",
    "Se preservan reglas institucionales UnADM, estructura canonica y gates de parseo JSON.",
    "Se transfieren solo abstracciones estables desde actividad de Filosofia del Derecho.",
    "Se evita transferir contenido tematico exclusivo de Filosofia del Derecho al nodo de Antropologia.",
    "Se mantiene estado provisional para fuentes heredadas no verificadas.",
    "Se refuerza resolucion de placeholders y rutas truncadas detectadas en README y programa analitico."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar toda fuente heredada no verificada como provisional.",
    "No trasladar metadatos curriculares de otra materia al destino."
  ],
  "structure_rules": [
    "Iniciar cada entrega con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear el producto al entregable solicitado en la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias de estructura reutilizable."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar resumen solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Cerrar con conclusion transferible a la practica juridica.",
    "Integrar conceptos antropologicos, culturales y juridicos con puente argumentativo explicito."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar memoria.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No propagar reglas provisionales como definitivas sin validacion local."
  ],
  "latex_rules": [
    "Usar configuracion en espanol coherente con la plantilla de la materia.",
    "Mantener clase y formato base salvo justificacion academica.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Corregir caracteres truncados en nombres y rutas antes de compilar.",
    "Resolver tokens dinamicos tipo $(@{...}.Slug) a nombres literales de archivos.",
    "Compilar sin errores criticos y sin referencias rotas."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes especificas por actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Mantener trazabilidad de activos locales cuando se cite material en assets-unadm."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y abstractas entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferencia literal de redaccion o contenidos tematicos de otra asignatura.",
    "Mantener compresion lossless por union-dedupe en ciclos futuros.",
    "Registrar incidencias de parseo como alerta transversal reutilizable.",
    "Si falta contexto local, conservar nucleo minimo y dejar vacios abiertos."
  ],
  "open_questions": [
    "Supuesto: falta consigna concreta de actividades actuales en Antropologia; confirmar productos por semana.",
    "Confirmar estandar unico de citacion institucional para la licenciatura.",
    "Confirmar si coursecode LDE-S4B2 es oficial o solo convencion local.",
    "Confirmar si la conclusion juridica es obligatoria en todas las actividades de la materia.",
    "Confirmar resolucion definitiva de placeholders en README y programa analitico."
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
        "Semestre 4, bloque 2, obligatoria, 8 creditos.",
        "Asignatura destino: Antropologia de la cultura en Mexico."
      ]
    },
    "essence": [
      "Problema inicial claro.",
      "Conceptos pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y utiles.",
      "Sostener coherencia institucional y calidad editorial entre actividades y materias."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Cierre con aplicacion profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente verificable -> interpretacion propia.",
      "Consigna -> desarrollo alineado -> cierre coherente."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Validacion JSON parseable",
        "Normalizacion estructurada",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Sincronizacion transversal"
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
          "justification": "La identidad institucional exige trazabilidad y rigor."
        },
        {
          "source": "Validacion JSON parseable",
          "target": "Normalizacion estructurada",
          "kind": "depends_on",
          "justification": "Sin parseo valido no hay memoria reusable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "El analisis gana solidez cuando tiene respaldo."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion util depende del razonamiento argumentado."
        }
      ],
      "evidence": [
        "README de materia destino establece identidad UnADM y pauta editorial.",
        "Programa analitico destino define ejes: problema, conceptos, producto, analisis y cierre.",
        "Bib local contiene unadmSitioWeb y unadmMallaDerecho2024.",
        "Memoria origen aporta abstracciones estables de calidad y argumentacion."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas manteniendo cobertura total.",
      "Se conservaron alertas historicas de salida no estructurada.",
      "Se reforzaron gates de parseo JSON y normalizacion previa a propagacion.",
      "Se incorporaron patrones argumentativos estables sin importar contenido tematico de origen.",
      "Se dejaron abiertos vacios locales que requieren verificacion institucional."
    ]
  }
}