{
  "summary": [
    "Sincronizacion transversal ciclo 5 aplicada con union-dedupe lossless y sin regresion.",
    "Se preserva identidad UnADM y contexto curricular local de Antropologia de la cultura en Mexico.",
    "Se transfieren solo abstracciones estables desde Filosofia del Derecho: objetivo, evidencia, analisis propio y cierre transferible.",
    "Se mantiene bloqueo de propagacion ante salidas no JSON parseables.",
    "Se refuerza normalizacion de placeholders y tokens dinamicos en README, programa y rutas de archivos.",
    "Supuesto: destino sin consigna por actividad especifica; se conserva cerebro editorial minimo reusable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Conservar ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "No trasladar metadatos curriculares de otra asignatura al destino."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Distinguir artefactos: reporte, presentacion y bibliografia.",
    "Cerrar con conclusion transferible a la practica juridica.",
    "Usar README y programa analitico como guias canonicas de estructura."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Integrar conceptos antropologicos, culturales y juridicos pertinentes.",
    "Evitar puentes argumentativos implicitos entre cultura y derecho; explicarlos."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa del esquema antes de reutilizar.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No promover reglas provisionales a definitivas sin validacion disciplinar."
  ],
  "latex_rules": [
    "Usar codificacion en español consistente en .tex y .bib.",
    "Mantener plantilla base de la materia salvo instruccion academica valida.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Mantener claves BibTeX estables.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) antes de compilar.",
    "Corregir nombres de archivo truncados o rutas corruptas del README."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo obras consultables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes de cada actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener trazabilidad de recursos locales en assets-unadm cuando se citen."
  ],
  "propagation_hints": [
    "Propagar solo reglas validadas y abstractas entre nodos no equivalentes.",
    "Evitar transferencia de contenido tematico literal desde Filosofia del Derecho.",
    "Preservar reglas utiles previas sin eliminarlas; solo deduplicar.",
    "Registrar alertas de parseo como conocimiento transversal reutilizable.",
    "Aplicar estrategia conservadora: primero identidad y gates, despues ajustes locales.",
    "Si falta contexto local de actividad, mantener preguntas abiertas y no forzar supuestos."
  ],
  "open_questions": [
    "Confirmar rubrica oficial de evaluacion de la materia para calibrar profundidad.",
    "Confirmar estandar de citacion institucional unico para la licenciatura.",
    "Confirmar si LDE-S4B2 es clave oficial o clave operativa local.",
    "Confirmar si toda actividad debe cerrar con conclusion juridica explicita.",
    "Confirmar si persisten placeholders en otros archivos fuera de README y programa."
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
        "Asignatura: Antropologia de la cultura en Mexico."
      ]
    },
    "essence": [
      "Problema, conceptos, evidencia, analisis propio y conclusion transferible.",
      "Normalizacion estructurada antes de cualquier propagacion.",
      "Compresion lossless por deduplicacion sin recorte semantico."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables y utiles.",
      "Sostener consistencia editorial transversal sin perder contexto local."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos etiquetados.",
      "Cierre con valor profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente verificable -> interpretacion propia.",
      "Coherencia integral entre consigna, desarrollo y cierre."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON parseable",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Sincronizacion transversal conservadora"
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
          "justification": "Sin parseo valido no hay memoria confiable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura academica requiere respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion util surge del razonamiento propio."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Sincronizacion transversal conservadora",
          "kind": "supports",
          "justification": "La identidad comun habilita transferencia de reglas estables."
        }
      ],
      "evidence": [
        "README y programa analitico del destino confirman ejes editoriales.",
        "Memoria origen aporta patrones argumentativos reutilizables no tematicos.",
        "Historial mantiene alerta por salidas no JSON parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 5: deduplicadas reglas repetidas de identidad, estructura y calidad.",
      "Ciclo 5: retenidos gates criticos de parseo y normalizacion.",
      "Ciclo 5: excluida transferencia de contenido doctrinal especifico de Filosofia del Derecho.",
      "Ciclo 5: reforzada trazabilidad bibliografica local y resolucion de placeholders.",
      "Ciclo 5: conservada politica de supuestos para datos no visibles."
    ]
  }
}