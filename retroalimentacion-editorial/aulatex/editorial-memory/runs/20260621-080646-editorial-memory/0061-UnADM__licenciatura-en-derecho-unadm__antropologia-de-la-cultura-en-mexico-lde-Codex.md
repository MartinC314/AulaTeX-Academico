{
  "summary": [
    "Sincronizacion transversal aplicada por union-dedupe lossless y sin regresion.",
    "Se preservan reglas institucionales UnADM, estructura canonica y validacion JSON.",
    "Se transfieren solo abstracciones estables desde Filosofia del Derecho.",
    "Se evita mover contenido tematico especifico de Filosofia al nodo de Antropologia.",
    "Se refuerza marcado de supuestos para datos no confirmados por consigna local.",
    "Se mantiene alerta por salidas no estructuradas heredadas y normalizacion obligatoria."
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
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco teorico-normativo, analisis propio y cierre.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias canonicas de estructura."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Integrar conceptos antropologicos, culturales y juridicos con puente argumentativo.",
    "Cerrar con conclusion transferible a la practica juridica."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa del esquema antes de reutilizar.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Verificar consistencia entre citas en texto y archivo .bib.",
    "No promover reglas provisionales a definitivas sin validacion local."
  ],
  "latex_rules": [
    "Usar configuracion en espanol coherente con la plantilla local.",
    "Mantener clase y formato base salvo necesidad academica justificada.",
    "Actualizar documenttitle y documentsubtitle por actividad real.",
    "Resolver placeholders tipo $(@{...}.Slug) en README, programa y rutas.",
    "Corregir rutas con caracteres truncados antes de compilar.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes especificas de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener trazabilidad de procedencia cuando la fuente sea archivo local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas ya validadas por calidad y parseo.",
    "Compartir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates y grafo conceptual.",
    "Evitar propagar redaccion literal o contenidos disciplinares exclusivos.",
    "Registrar incidencias de parseo como alertas reutilizables inter-materia.",
    "Mantener estrategia progresiva y conservadora sin eliminar reglas utiles previas."
  ],
  "open_questions": [
    "Supuesto: falta consigna puntual de actividades locales de Antropologia; confirmar formatos exigidos.",
    "Confirmar estandar de citacion oficial de la licenciatura.",
    "Confirmar si LDE-S4B2 es clave institucional definitiva o clave local.",
    "Confirmar si la conclusion juridica aplica en todas las actividades de la materia.",
    "Confirmar politica definitiva para nombres de .bib cuando existan placeholders en documentos."
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
      "Problema, conceptos, evidencia, analisis propio y conclusion transferible.",
      "Normalizacion estructurada antes de propagacion.",
      "Compresion lossless por deduplicacion sin recorte."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros, verificables y utiles profesionalmente.",
      "Sostener continuidad editorial transversal sin contaminar contexto disciplinar local."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Cierre con valor profesional y juridico."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente verificable -> interpretacion propia.",
      "Coherencia interna entre guia, desarrollo y cierre."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON parseable",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Supuestos marcados",
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
          "source": "Identidad institucional UnADM",
          "target": "Sincronizacion transversal conservadora",
          "kind": "supports",
          "justification": "La identidad comun permite reglas estables entre materias."
        }
      ],
      "evidence": [
        "README local de Antropologia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico local: ejes problema, conceptos, producto, analisis y cierre.",
        "Bibliografia local: unadmSitioWeb y unadmMallaDerecho2024.",
        "Memoria origen: regla estable de normalizacion y JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 61: se reforzo gate de parseo JSON como requisito duro de propagacion.",
      "Ciclo 61: se consolidaron patrones argumentativos transferibles sin contenido tematico de Filosofia.",
      "Ciclo 61: se reforzo resolucion de placeholders y control de rutas en .tex/.bib.",
      "Ciclo 61: se mantuvo politica de supuestos y fuentes provisionales no verificadas."
    ]
  }
}