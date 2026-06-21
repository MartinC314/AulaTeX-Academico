{
  "summary": [
    "Sincronizacion transversal ciclo 43 aplicada con union-dedupe lossless y sin regresion.",
    "Se preservan reglas institucionales UnADM, estructura canonica y gates de calidad ya vigentes en destino.",
    "Se incorporan del origen solo abstracciones estables reutilizables: objetivo puntual, evidencia verificable, postura propia y coherencia argumentativa.",
    "Se evita transferir contenido tematico exclusivo de Filosofia del Derecho al nodo de Antropologia.",
    "Se refuerza normalizacion obligatoria ante salidas no JSON parseable y fuentes heredadas provisionales."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar toda fuente heredada no verificada como provisional hasta validacion local.",
    "No trasladar metadatos curriculares de otra asignatura al destino."
  ],
  "structure_rules": [
    "Iniciar cada entrega con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar secciones en: conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear el formato final al producto pedido por la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias canonicas de estructura."
  ],
  "activity_rules": [
    "Sustentar afirmaciones relevantes con fuente verificable y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Cerrar con conclusion transferible a la practica juridica.",
    "Evitar extrapolar fuentes o consignas de semanas o materias distintas sin confirmacion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar esquema minimo completo antes de reutilizar memoria.",
    "Revisar y normalizar manualmente respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar trazabilidad de afirmaciones o marcarlas como supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No promover reglas provisionales a definitivas sin validacion disciplinar local."
  ],
  "latex_rules": [
    "Usar codificacion en espanol consistente en .tex y .bib.",
    "Mantener clase y configuracion base de la plantilla salvo justificacion academica.",
    "Actualizar documenttitle y documentsubtitle por actividad real.",
    "Conservar claves BibTeX estables.",
    "Compilar sin errores criticos, sin referencias rotas y sin placeholders sin resolver.",
    "Resolver tokens dinamicos tipo $(@{...}.Slug) en README, programa y rutas antes de compilar."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y fuentes pertinentes a la actividad.",
    "Registrar fuentes especificas de cada actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Marcar como supuesto cualquier inferencia bibliografica no confirmada por consigna."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y abstractas entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar propagar redaccion literal o contenido tematico no transversal.",
    "Mantener estrategia progresiva y conservadora: agregar sin eliminar reglas utiles previas.",
    "Registrar incidencias de parseo como alertas reutilizables inter-materias."
  ],
  "open_questions": [
    "Supuesto: falta consigna local de actividad concreta; confirmar producto exacto por semana.",
    "Confirmar estandar unico de citacion para la licenciatura.",
    "Confirmar si LDE-S4B2 es clave institucional fija o clave operativa local.",
    "Confirmar rubrica oficial para calibrar profundidad argumentativa en Antropologia.",
    "Confirmar si toda actividad de la materia exige conclusion juridica explicita."
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
      "Problema juridico o social.",
      "Conceptos pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables.",
      "Garantizar coherencia entre consigna, desarrollo y cierre.",
      "Sostener calidad editorial transversal sin perder contexto local."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> respaldo -> interpretacion propia.",
      "Consigna -> desarrollo alineado -> verificacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON parseable",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Supuestos explicitados"
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
          "justification": "La postura academica se legitima con respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion surge del razonamiento y no del resumen."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Supuestos explicitados",
          "kind": "supports",
          "justification": "La integridad academica exige distinguir hechos de inferencias."
        }
      ],
      "evidence": [
        "README local de la materia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico local: ejes problema, conceptos, producto, analisis y cierre.",
        "Bib local: fuentes base institucionales verificables.",
        "Memoria origen: regla estable de normalizacion previa y coherencia argumentativa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 43: se consolidan abstracciones transversales del origen sin importar contenido doctrinal especifico.",
      "Ciclo 43: se mantiene gate estricto de JSON parseable y normalizacion manual de respuestas no estructuradas.",
      "Ciclo 43: se refuerza marcado de supuestos y estatus provisional de fuentes heredadas no verificadas.",
      "Ciclo 43: sin eliminacion de reglas utiles previas; solo deduplicacion y fortalecimiento."
    ]
  }
}