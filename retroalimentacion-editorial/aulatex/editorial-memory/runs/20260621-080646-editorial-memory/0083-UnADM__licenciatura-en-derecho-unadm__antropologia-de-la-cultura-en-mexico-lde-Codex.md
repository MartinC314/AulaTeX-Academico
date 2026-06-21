{
  "summary": [
    "Sincronizacion transversal consolidada con union-dedupe lossless y sin regresion.",
    "Se preservan reglas institucionales UnADM y estructura canonica de materia.",
    "Se incorporan abstractions estables del origen: objetivo, evidencia, postura y coherencia.",
    "No se transfieren contenidos tematicos exclusivos de Filosofia del Derecho.",
    "Se mantiene alerta por salidas no JSON parseable y normalizacion previa obligatoria."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar toda fuente heredada no verificada como provisional hasta confirmacion local.",
    "No trasladar metadatos curriculares de Filosofia del Derecho al destino."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias canonicas de estructura."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Evitar afirmaciones sin puente entre analisis cultural y enfoque juridico.",
    "Confirmar formato solicitado por actividad antes de redactar."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar memoria.",
    "Normalizar manualmente respuestas no estructuradas heredadas.",
    "Confirmar consistencia entre metadatos de materia y documento final.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No promover reglas provisionales a definitivas sin verificacion disciplinar."
  ],
  "latex_rules": [
    "Conservar plantilla base .tex de la materia.",
    "Mantener configuracion en espanol y compatibilidad de acentos en .tex y .bib.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Mantener coursename y coursecode locales salvo instruccion institucional.",
    "Compilar sin errores criticos, referencias rotas ni placeholders sin resolver.",
    "Resolver tokens dinamicos tipo $(@{...}.Slug) a nombres literales antes de compilar."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes especificas por actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Marcar como supuesto cualquier correspondencia bibliografica no confirmada."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas estables y validadas.",
    "Priorizar identidad, gates de calidad, estructura reusable y grafo conceptual.",
    "Evitar transferencia literal de redaccion entre nodos no equivalentes.",
    "Mantener compresion lossless por deduplicacion, sin recorte semantico.",
    "Registrar incidencias de parseo como alertas transversales reutilizables."
  ],
  "open_questions": [
    "Supuesto: falta consigna puntual de actividades locales; confirmar productos exactos por semana.",
    "Confirmar estandar unico de citacion para la licenciatura.",
    "Confirmar si conclusion juridica aplica a todas las actividades de antropologia.",
    "Confirmar si LDE-S4B2 es clave oficial institucional o clave operativa local."
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
      "Problema claro.",
      "Conceptos pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Cierre transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables.",
      "Sostener consistencia institucional y calidad transversal entre nodos."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Citas verificables en cada afirmacion relevante."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente -> interpretacion propia.",
      "Pregunta guia -> desarrollo consistente -> respuesta final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON parseable",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible"
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
          "justification": "El analisis gana validez cuando cada afirmacion es trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion util deriva del razonamiento y no del resumen."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "La pauta institucional exige integridad academica y citas comprobables."
        }
      ],
      "evidence": [
        "README local fija identidad UnADM y pauta editorial.",
        "Programa analitico local define ejes problema-conceptos-producto-analisis-cierre.",
        "Bib local contiene fuentes base institucionales verificables.",
        "Memoria origen aporta patrones argumentativos reutilizables no tematicos."
      ]
    },
    "reinforcement_log": [
      "Se reforzo gate de JSON parseable como condicion de propagacion.",
      "Se reforzo regla de marcar supuestos en datos no visibles.",
      "Se reforzo separacion entre abstracciones transferibles y contenido disciplinar especifico.",
      "Se reforzo resolucion de placeholders en rutas y nombres de archivo."
    ]
  }
}