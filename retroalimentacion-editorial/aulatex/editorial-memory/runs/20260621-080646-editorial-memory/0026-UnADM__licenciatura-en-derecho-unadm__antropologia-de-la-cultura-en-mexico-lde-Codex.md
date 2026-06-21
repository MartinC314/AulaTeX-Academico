{
  "summary": [
    "Se consolida sincronizacion transversal ciclo 26 con union-dedupe lossless y sin regresion.",
    "Se transfieren solo abstracciones editoriales estables desde actividad de Filosofia del Derecho.",
    "Se preserva identidad UnADM del destino con contexto curricular local de Antropologia.",
    "Se refuerzan gates de JSON parseable, normalizacion estructurada y trazabilidad de fuentes.",
    "Se evita mover contenido tematico especifico de Filosofia del Derecho al nodo destino."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "No trasladar metadatos curriculares de otras materias al destino."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o teorico, analisis propio y cierre.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Evitar afirmaciones culturales o juridicas sin puente argumentativo.",
    "Confirmar que el formato final coincide con la consigna de la actividad."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar esquema minimo completo antes de reutilizar memoria.",
    "Normalizar manualmente respuestas no estructuradas antes de propagar.",
    "Confirmar que todo supuesto este marcado como supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que no existan placeholders sin resolver en README, programa, .tex y rutas."
  ],
  "latex_rules": [
    "Usar configuracion en espanol coherente con la plantilla local.",
    "Mantener clase y formato base salvo justificacion academica.",
    "Actualizar documenttitle y documentsubtitle por actividad real.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Compilar sin errores criticos ni referencias indefinidas.",
    "Corregir rutas con caracteres truncados o tokens dinamicos antes de compilar."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables y consultables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes especificas de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No citar entradas ausentes en el .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferencia literal de redaccion y contenido tematico de otra asignatura.",
    "Preservar reglas utiles previas y agregar solo mejoras verificables.",
    "Mantener registro de incidencias de parseo como alerta transversal reutilizable."
  ],
  "open_questions": [
    "Supuesto: falta consigna local de actividad especifica en Antropologia; confirmar producto exacto.",
    "Confirmar rubrica de evaluacion para ajustar profundidad argumentativa.",
    "Confirmar estandar de citacion institucional unico para la licenciatura.",
    "Confirmar si la clave LDE-S4B2 es oficial institucional o solo operativa local.",
    "Confirmar si la conclusion juridica aplica a todas las actividades de la materia."
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
      "Problema claro, conceptos pertinentes, evidencia verificable, analisis propio y cierre transferible.",
      "Normalizacion estructurada obligatoria antes de propagacion.",
      "Compresion lossless por union-dedupe sin eliminar reglas utiles."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y argumentados.",
      "Sostener consistencia editorial transversal en la suite LaTeX UnADM."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Conclusion con aplicabilidad profesional."
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
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Normalizacion estructurada",
        "Validacion JSON parseable"
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
          "justification": "La norma institucional exige trazabilidad y rigor en citas."
        },
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
          "justification": "La postura personal se legitima con respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "El cierre profesional surge del razonamiento argumentado."
        }
      ],
      "evidence": [
        "README local confirma identidad UnADM, ubicacion curricular y pauta editorial.",
        "Programa analitico local confirma ejes problema, conceptos, producto, analisis y cierre.",
        "Bib local confirma fuentes base institucionales verificables.",
        "Memoria origen refuerza normalizacion y bloqueo por salida no JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 26: se preservan reglas previas del destino sin eliminaciones.",
      "Ciclo 26: se agregan abstracciones estables del origen sin transferir contenido tematico ajeno.",
      "Ciclo 26: se refuerza gate de parseo JSON y resolucion de placeholders como control transversal."
    ]
  }
}