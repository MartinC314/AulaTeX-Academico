{
  "summary": [
    "Sincronizacion transversal consolidada por union-dedupe lossless y sin regresion.",
    "Se preserva identidad UnADM y contexto curricular local de Antropologia en Mexico.",
    "Se transfieren solo abstracciones estables desde actividad de Filosofia del Derecho.",
    "Se refuerza normalizacion estructurada y bloqueo por JSON no parseable.",
    "Se mantiene alerta de fuentes heredadas no verificadas como provisionales.",
    "Se refuerza resolucion de placeholders en README, programa y rutas de archivos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No trasladar metadatos curriculares especificos de Filosofia del Derecho al destino."
  ],
  "structure_rules": [
    "Iniciar cada entrega con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar secciones en: conceptos clave, marco normativo o teorico, analisis propio y cierre.",
    "Alinear el producto al entregable real de la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias canonicas de estructura."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Evitar extrapolar contenidos tematicos exclusivos de otra materia.",
    "Cerrar con conclusion transferible a la practica juridica cuando la consigna lo pida."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa del esquema antes de reutilizar.",
    "Normalizar manualmente respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar consistencia entre metadatos del documento y contexto curricular local.",
    "Verificar correspondencia entre citas en texto y archivo .bib.",
    "Confirmar que todo supuesto este marcado de forma explicita."
  ],
  "latex_rules": [
    "Usar codificacion y acentos en espanol consistentes en .tex y .bib.",
    "Mantener plantilla base de la materia salvo justificacion academica.",
    "Actualizar documenttitle y documentsubtitle segun actividad real.",
    "Resolver tokens dinamicos tipo $(@{...}.Slug) a nombres literales antes de compilar.",
    "Corregir rutas con caracteres truncados o anomalias antes de compilar.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes especificas de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No asumir pertinencia automatica de bibliografia heredada de otra asignatura."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y abstractas.",
    "Conservar compresion lossless por union-dedupe sin eliminar reglas utiles previas.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Etiquetar incidencias de parseo como alertas transversales reutilizables.",
    "Si falta contexto local nuevo, mantener cerebro minimo y abrir vacios como preguntas."
  ],
  "open_questions": [
    "Supuesto: confirmar si la conclusion juridica es obligatoria en todas las actividades de Antropologia.",
    "Confirmar rubrica oficial de evaluacion para ajustar profundidad argumentativa.",
    "Confirmar estandar institucional de citacion unico para la licenciatura.",
    "Confirmar si LDE-S4B2 es clave oficial o convencion local.",
    "Supuesto: validar si toda actividad requiere reporte, presentacion o formato mixto."
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
      "Problema, conceptos, evidencia, analisis propio y cierre.",
      "Normalizacion estructurada antes de toda propagacion.",
      "Transferencia transversal por abstracciones estables, no por redaccion literal."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables y utiles.",
      "Sostener coherencia institucional, curricular y metodologica entre nodos."
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
      "Coherencia entre pregunta guia y resultado final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Evidencia verificable",
        "Analisis propio",
        "Normalizacion estructurada",
        "Validacion JSON parseable",
        "Propagacion transversal conservadora"
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
          "justification": "La pauta institucional exige trazabilidad y verificabilidad."
        },
        {
          "source": "Validacion JSON parseable",
          "target": "Normalizacion estructurada",
          "kind": "depends_on",
          "justification": "Sin parseo valido no hay consolidacion confiable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura personal se legitima con respaldo trazable."
        },
        {
          "source": "Propagacion transversal conservadora",
          "target": "Identidad institucional UnADM",
          "kind": "develops",
          "justification": "Permite sincronizar reglas estables sin contaminar contexto local."
        }
      ],
      "evidence": [
        "README local: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: ejes de trabajo y proposito de realizacion.",
        "Bib local: fuentes base institucionales verificables.",
        "Memoria origen: gates de JSON, supuestos y estructura argumentativa reusable."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas en identidad, estructura, actividad y calidad.",
      "Se preservaron reglas utiles previas sin recorte semantico.",
      "Se excluyeron contenidos tematicos no estables de Filosofia del Derecho.",
      "Se reforzo control de placeholders y normalizacion tecnica de rutas."
    ]
  }
}