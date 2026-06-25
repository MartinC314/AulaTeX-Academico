{
  "summary": [
    "Sincronizacion transversal ciclo 4 aplicada con union-dedupe lossless y sin regresion.",
    "Se preservan reglas institucionales UnADM, normalizacion estructurada y validacion JSON parseable.",
    "Se transfieren solo abstracciones estables desde Filosofia del Derecho: objetivo puntual, evidencia verificable, analisis propio y coherencia argumentativa.",
    "Se evita traslado de contenidos tematicos exclusivos del origen al destino de Antropologia.",
    "Se refuerza resolucion de placeholders en README, programa analitico y rutas .bib/.tex."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Respetar contexto curricular local del destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No trasladar metadatos curriculares especificos de Filosofia del Derecho al destino."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco normativo o teorico, analisis propio y cierre.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias canonicas de estructura."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar resumen solo descriptivo.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion transferible a la practica juridica.",
    "En actividades de antropologia, tender puente explicito entre dimension cultural y pertinencia juridica."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar memoria.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que no queden tokens sin resolver tipo $(@{...}.Slug)."
  ],
  "latex_rules": [
    "Mantener plantilla base .tex de la materia destino como referencia inicial.",
    "Usar codificacion en espanol consistente en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir rutas con caracteres truncados detectadas en README antes de referenciarlas."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables y consultables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes especificas por actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Mantener entradas base locales unadmSitioWeb y unadmMallaDerecho2024."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y estructuradas.",
    "Compartir en nodos no equivalentes solo abstracciones editoriales estables.",
    "Evitar redaccion literal o conceptos disciplinares exclusivos del nodo origen.",
    "Mantener compresion por union-dedupe sin eliminar reglas utiles previas.",
    "Registrar incidencias de parseo como alertas reutilizables inter-materias."
  ],
  "open_questions": [
    "Supuesto: falta consigna concreta de actividades de Antropologia; confirmar formatos por semana.",
    "Confirmar si la conclusion juridica es obligatoria en todas las actividades de la materia.",
    "Confirmar estandar de citacion institucional unico para la licenciatura.",
    "Confirmar caracter oficial de la clave local LDE-S4B2.",
    "Confirmar si existen fuentes obligatorias adicionales a la malla curricular y sitio UnADM."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y preciso.",
        "Argumentativo con criterio propio.",
        "Culturalmente sensible y juridicamente pertinente."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con trazabilidad de fuentes.",
        "Normalizacion estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Destino local: Antropologia de la cultura en Mexico.",
        "Semestre 4, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema, conceptos, evidencia, analisis propio y conclusion transferible.",
      "Trazabilidad documental y consistencia institucional.",
      "Sincronizacion transversal conservadora sin contaminar contexto disciplinar."
    ],
    "reason_for_being": [
      "Convertir la planeacion semanal en productos academicos verificables y utiles para la practica juridica.",
      "Preservar memoria editorial persistente con calidad tecnica y coherencia curricular."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Cierre con valor profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente verificable -> interpretacion propia.",
      "Coherencia estricta entre pregunta guia y respuesta final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON parseable",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Pertinencia cultural-juridica"
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
          "justification": "La conclusion util deriva del razonamiento y no del resumen."
        },
        {
          "source": "Pertinencia cultural-juridica",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "En Antropologia, la transferencia profesional exige puente entre cultura y derecho."
        }
      ],
      "evidence": [
        "README local: identidad UnADM, carpeta canonica y conclusion juridica.",
        "Programa analitico local: ejes problema, conceptos, producto, analisis y cierre.",
        "Bib local: unadmSitioWeb y unadmMallaDerecho2024.",
        "Memoria origen: regla estable de objetivo puntual, evidencia verificable y postura propia."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas y se conservaron todas las utiles.",
      "Se reforzaron gates de parseo JSON y estructura minima.",
      "Se agrego control explicito de placeholders dinamicos sin resolver.",
      "Se mantuvo estrategia progresiva y conservadora en propagacion transversal."
    ]
  }
}