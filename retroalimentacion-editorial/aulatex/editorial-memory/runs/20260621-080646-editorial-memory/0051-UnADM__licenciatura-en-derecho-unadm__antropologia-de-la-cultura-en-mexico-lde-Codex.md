{
  "summary": [
    "Sincronizacion transversal ciclo 51 aplicada con union-dedupe lossless y sin regresion.",
    "Se preserva identidad UnADM del destino y se transfieren solo abstracciones estables del origen.",
    "Se refuerzan ejes reutilizables: objetivo, problema, conceptos, evidencia, analisis propio y conclusion transferible.",
    "Se mantiene bloqueo por salida no JSON parseable y normalizacion obligatoria previa a propagacion.",
    "Se conserva alerta de fuentes heredadas no verificadas como provisionales.",
    "Se evita traslado de contenido tematico especifico de Filosofia del Derecho al nodo de Antropologia."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar toda fuente heredada no verificada como provisional.",
    "No trasladar metadatos curriculares de otra asignatura al destino."
  ],
  "structure_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Separar secciones: conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Distinguir artefactos: reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias canonicas de estructura.",
    "Resolver placeholders de nombre de archivos antes de usar rutas."
  ],
  "activity_rules": [
    "Sustentar afirmaciones relevantes con fuente verificable y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Evitar afirmaciones juridicas sin puente argumentativo con el analisis cultural.",
    "Cerrar con conclusion transferible a la practica juridica cuando la consigna lo permita [supuesto]."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa del esquema antes de reutilizar.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregado y consigna local.",
    "No promover reglas provisionales a definitivas sin validacion disciplinar."
  ],
  "latex_rules": [
    "Mantener configuracion en espanol y acentos correctos en .tex y .bib.",
    "Conservar clase y formato base de la plantilla salvo justificacion academica.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Compilar sin errores criticos ni referencias indefinidas.",
    "Corregir rutas truncadas o tokens sin expandir en README, programa y .tex."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales pertinentes.",
    "Registrar fuentes especificas de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener trazabilidad de archivos locales cuando se citen assets-unadm."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y abstractas entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferencia literal de redaccion o doctrina exclusiva de la materia origen.",
    "Registrar incidencias de parseo como alertas institucionales reutilizables.",
    "Preservar union-dedupe lossless en ciclos siguientes sin eliminar reglas utiles."
  ],
  "open_questions": [
    "Confirmar si la conclusion juridica es obligatoria en todas las actividades de Antropologia [supuesto].",
    "Confirmar estandar unico de citacion institucional para la licenciatura.",
    "Confirmar si LDE-S4B2 es clave oficial o convencion local.",
    "Confirmar rubricas locales que definan profundidad argumentativa por actividad.",
    "Confirmar politica final para resolver tokens dinamicos en nombres de archivo."
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
      "Conclusion transferible.",
      "Normalizacion estructurada obligatoria."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros, verificables y argumentados.",
      "Asegurar coherencia entre consigna, desarrollo y cierre.",
      "Preservar continuidad editorial institucional entre nodos."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados de forma explicita.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente verificable -> interpretacion propia.",
      "Consigna -> desarrollo alineado -> verificacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Validacion JSON parseable",
        "Normalizacion estructurada",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion transferible"
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
          "source": "Integridad academica",
          "target": "Evidencia verificable",
          "kind": "depends_on",
          "justification": "La integridad exige respaldo trazable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura argumentada requiere sustento."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion util emerge del razonamiento."
        }
      ],
      "evidence": [
        "README local: identidad UnADM, integridad academica, citas verificables, conclusion juridica.",
        "Programa analitico local: ejes problema, conceptos, producto, analisis y cierre.",
        "Memoria origen: regla de normalizacion estructurada previa a propagacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 51: se consolidan abstracciones transversales estables desde actividad de Filosofia del Derecho.",
      "Ciclo 51: se mantiene politica de bloqueo por JSON invalido.",
      "Ciclo 51: se refuerza resolucion de placeholders en rutas y nombres.",
      "Ciclo 51: se preserva identidad local de Antropologia sin contaminar contenido tematico de origen."
    ]
  }
}