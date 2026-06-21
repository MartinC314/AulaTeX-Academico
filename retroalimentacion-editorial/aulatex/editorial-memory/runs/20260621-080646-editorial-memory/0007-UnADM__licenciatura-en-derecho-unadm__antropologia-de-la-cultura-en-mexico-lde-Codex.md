{
  "summary": [
    "Sincronizacion transversal ciclo 7 aplicada con union-dedupe lossless y sin regresion.",
    "Se preserva identidad UnADM del destino y se incorporan solo abstracciones estables del origen.",
    "Se refuerzan ejes reutilizables: objetivo, problema, conceptos, evidencia, analisis propio y cierre transferible.",
    "Se mantiene regla critica: no propagar contenido no estructurado sin normalizacion JSON.",
    "Se confirma contexto local del destino: semestre 4, bloque 2, obligatoria, 8 creditos [verificado en README].",
    "Se mantiene vacio local de consignas por actividad como pendiente controlado."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener materia destino: Antropologia de la cultura en Mexico.",
    "Conservar ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar toda fuente heredada no verificada como provisional.",
    "No trasladar metadatos especificos de Filosofia del Derecho al destino."
  ],
  "structure_rules": [
    "Iniciar con objetivo puntual y encuadre breve del problema juridico o social.",
    "Organizar en secciones: conceptos clave, marco normativo o teorico, analisis propio y cierre.",
    "Alinear el producto al entregable semanal definido en planeacion.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias canonicas de estructura.",
    "Resolver placeholders y tokens dinamicos a nombres literales antes de compilar."
  ],
  "activity_rules": [
    "Definir objetivo de actividad antes del desarrollo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Incluir postura argumentada del estudiante; evitar solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion transferible a la practica juridica.",
    "Evitar trasladar contenidos tematicos exclusivos de otra materia sin puente argumentativo."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Exigir estructura minima completa del esquema antes de reutilizar.",
    "Normalizar manualmente toda salida no estructurada heredada.",
    "Validar consistencia entre metadatos de documento y contexto curricular local.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar correspondencia entre citas en texto y archivo .bib local.",
    "No promover reglas provisionales a definitivas sin validacion local."
  ],
  "latex_rules": [
    "Mantener plantilla .tex base de la materia como referencia.",
    "Conservar configuracion en espanol y clase article salvo instruccion formal distinta.",
    "Mantener campos institucionales completos y coherentes con destino.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Corregir rutas y nombres truncados detectados en README.",
    "Resolver tokens tipo $(@{...}.Slug) en README y programa analitico.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Usar archivo local antropologia-de-la-cultura-en-mexico.bib como canonico [verificado].",
    "No inventar fuentes; incluir solo referencias consultables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales pertinentes.",
    "Agregar entradas especificas por actividad en el .bib local.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas estables y validadas.",
    "Compartir entre nodos no equivalentes solo abstracciones editoriales, no redaccion literal.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Registrar incidencias de parseo como alerta transversal reutilizable.",
    "Mantener estrategia conservadora: agregar sin eliminar reglas utiles previas."
  ],
  "open_questions": [
    "Confirmar rubricas oficiales por actividad en la materia destino.",
    "Confirmar si conclusion juridica es obligatoria en todas las actividades de antropologia [supuesto].",
    "Confirmar estandar unico de citacion para la licenciatura.",
    "Confirmar si LDE-S4B2 es clave oficial institucional o clave operativa local [supuesto]."
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
      "Problema juridico o social.",
      "Conceptos y marco pertinente.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros, fundados y utiles.",
      "Asegurar consistencia editorial transversal en la suite LaTeX."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Cierre con valor profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> respaldo verificable -> interpretacion propia.",
      "Coherencia entre pregunta guia y cierre final."
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
          "justification": "Sin parseo valido no hay memoria reutilizable."
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
          "justification": "La conclusion util deriva del razonamiento."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Propagacion transversal conservadora",
          "kind": "supports",
          "justification": "La identidad comun habilita reglas compartidas estables."
        }
      ],
      "evidence": [
        "README destino confirma identidad y ubicacion curricular.",
        "Programa analitico confirma ejes editoriales reutilizables.",
        "Bib local confirma fuentes base institucionales existentes."
      ]
    },
    "reinforcement_log": [
      "Ciclo 7: deduplicacion completa de reglas repetidas.",
      "Ciclo 7: transferencia solo de abstracciones estables desde actividad de otra materia.",
      "Ciclo 7: preservadas alertas de parseo y normalizacion manual.",
      "Ciclo 7: reforzada resolucion de placeholders en rutas y nombres."
    ]
  }
}