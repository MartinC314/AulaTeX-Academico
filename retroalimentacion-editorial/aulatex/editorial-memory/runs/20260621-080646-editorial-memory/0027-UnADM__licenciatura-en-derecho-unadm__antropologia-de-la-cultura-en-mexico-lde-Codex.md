{
  "summary": [
    "Sincronizacion transversal ciclo 27 aplicada con union-dedupe lossless y sin regresion.",
    "Se preservan reglas estables de identidad UnADM, estructura reusable, calidad y LaTeX.",
    "Se transfieren solo abstracciones editoriales desde actividad de Filosofia del Derecho a materia de Antropologia.",
    "Se evita trasladar contenido tematico exclusivo de Filosofia del Derecho al destino.",
    "Se mantiene alerta historica: salidas no JSON parseable deben normalizarse antes de propagar.",
    "Se refuerza resolucion de placeholders $(@{...}.Slug) en README y programa analitico."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Conservar ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar toda fuente heredada no verificada como provisional.",
    "No trasladar metadatos curriculares de otras materias al destino.",
    "Mantener coursecode LDE-S4B2 salvo instruccion institucional distinta."
  ],
  "structure_rules": [
    "Iniciar cada entrega con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear el artefacto al producto solicitado en la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias canonicas de estructura.",
    "Cerrar con conclusion transferible a la practica juridica."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Integrar conceptos antropologicos, culturales, juridicos o sociales pertinentes.",
    "Evitar afirmaciones juridicas sin puente argumentativo cultural."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar esquema minimo completo antes de reutilizar memoria.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que no queden placeholders sin resolver en README, programa y .tex.",
    "No promover reglas provisionales a definitivas sin validacion local."
  ],
  "latex_rules": [
    "Usar codificacion en español coherente en .tex y .bib.",
    "Mantener clase article, letterpaper y oneside salvo justificacion academica.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Mantener campos institucionales completos y consistentes.",
    "Mantener claves BibTeX estables para evitar rupturas.",
    "Compilar sin errores criticos, sin referencias rotas y sin tokens sin expandir.",
    "Corregir rutas truncadas o caracteres anómalos antes de compilar."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes especificas por actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, año y fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Mantener entradas base unadmSitioWeb y unadmMallaDerecho2024."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y parseables.",
    "Compartir entre nodos no equivalentes solo abstracciones editoriales estables.",
    "Evitar redaccion literal y contenido disciplinar especifico del origen.",
    "Mantener compresion union-dedupe sin eliminar reglas utiles previas.",
    "Registrar incidencias de parseo como alerta reutilizable inter-materias.",
    "Si falta contexto local, conservar cerebro minimo y abrir preguntas."
  ],
  "open_questions": [
    "Supuesto: falta confirmacion del estandar de citas unico para la licenciatura.",
    "Confirmar si la conclusion juridica es obligatoria en todas las actividades de Antropologia.",
    "Confirmar si LDE-S4B2 es clave oficial institucional o clave local.",
    "Confirmar rubricas de evaluacion por actividad para ajustar profundidad.",
    "Supuesto: fuentes heredadas desde GPT-Pro y Codex siguen en estado provisional."
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
      "Problema claro.",
      "Conceptos pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y utiles.",
      "Garantizar consistencia editorial transversal sin perder contexto local."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados cuando falte evidencia.",
      "Cierre con aplicacion profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente verificable -> interpretacion propia.",
      "Coherencia entre consigna, desarrollo y cierre."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Normalizacion estructurada",
        "Validacion JSON parseable",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Resolucion de placeholders en rutas y nombres"
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
          "justification": "La postura academica requiere respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion deriva del razonamiento y no del resumen."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y consistencia formal."
        }
      ],
      "evidence": [
        "README de Antropologia: identidad UnADM y pauta editorial.",
        "Programa analitico: ejes problema, conceptos, producto, analisis y cierre.",
        "Bibliografia local: unadmSitioWeb y unadmMallaDerecho2024.",
        "Memoria origen: regla de bloqueo por salida no JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 27: se consolidan reglas transversales estables sin arrastrar contenido tematico de Filosofia.",
      "Ciclo 27: se mantiene guardrail de JSON parseable como gate duro de propagacion.",
      "Ciclo 27: se refuerza politica de supuestos y fuentes provisionales no verificadas.",
      "Ciclo 27: se preserva compresion lossless por deduplicacion."
    ]
  }
}