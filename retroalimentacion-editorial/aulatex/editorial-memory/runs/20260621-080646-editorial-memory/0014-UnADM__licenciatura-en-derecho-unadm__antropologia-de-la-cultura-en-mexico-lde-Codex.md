{
  "summary": [
    "Sincronizacion transversal ciclo 14 aplicada con union-dedupe lossless y sin regresion.",
    "Se preservan reglas institucionales UnADM, estructura canonica y control de calidad por JSON parseable.",
    "Se incorporan abstracciones estables del origen: objetivo puntual, evidencia verificable, postura propia y coherencia entre pregunta, desarrollo y cierre.",
    "Se evita transferir contenido tematico especifico de Filosofia del Derecho al nodo de Antropologia.",
    "Se refuerza resolucion de placeholders en README y programa analitico antes de compilar o propagar.",
    "Se mantiene estado provisional para fuentes heredadas no verificadas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "No transferir metadatos curriculares de otras materias al destino."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear el producto al entregable solicitado en la planeacion semanal.",
    "Distinguir artefactos: reporte, presentacion y bibliografia.",
    "Cerrar con conclusion transferible a la practica juridica.",
    "Usar README y programa analitico como guias operativas."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Evitar afirmaciones culturales o juridicas sin puente argumentativo.",
    "Validar que el producto final corresponda a la consigna activa.",
    "No asumir fuentes de semanas o materias distintas sin confirmacion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Exigir esquema minimo completo antes de reutilizar memoria.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en toda afirmacion relevante.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre metadatos de materia y documento final.",
    "No promover reglas provisionales a definitivas sin validacion disciplinar."
  ],
  "latex_rules": [
    "Mantener plantilla base .tex de la materia como referencia.",
    "Conservar configuracion en espanol y acentos correctos en .tex y .bib.",
    "Mantener clase y formato base salvo justificacion academica.",
    "Compilar sin errores criticos, sin referencias rotas y sin tokens sin resolver.",
    "Resolver placeholders tipo $(@{...}.Slug) a nombres literales antes de citar rutas.",
    "Verificar rutas y nombres del README y programa analitico antes de compilar.",
    "Actualizar documenttitle y documentsubtitle segun actividad real."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables y consultables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes especificas de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No citar claves inexistentes en el .bib local.",
    "Mantener trazabilidad de procedencia para archivos locales."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y parseables.",
    "Transferir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar propagar redaccion literal o contenido tematico exclusivo del origen.",
    "Mantener union-dedupe lossless como metodo de consolidacion.",
    "Registrar incidencias de parseo como alertas institucionales reutilizables.",
    "Preservar reglas utiles previas sin eliminacion."
  ],
  "open_questions": [
    "Supuesto: confirmar si LDE-S4B2 es clave oficial institucional o clave local.",
    "Supuesto: confirmar rubrica formal de evaluacion para actividades de la materia destino.",
    "Confirmar estandar unico de citacion para la licenciatura (APA u otro).",
    "Confirmar si toda actividad de Antropologia exige conclusion juridica explicita.",
    "Confirmar politica final para resolver y persistir placeholders en nombres de archivo."
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
      "Normalizacion estructurada antes de propagacion.",
      "Sincronizacion transversal conservadora sin contaminar contexto local."
    ],
    "reason_for_being": [
      "Convertir la planeacion semanal en productos academicos verificables y coherentes.",
      "Sostener identidad UnADM con calidad tecnica, argumentativa y documental."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente verificable -> interpretacion propia.",
      "Consigna -> desarrollo alineado -> cierre consistente."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Validacion JSON parseable",
        "Normalizacion estructurada",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Resolucion de placeholders",
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
          "justification": "Sin parseo valido no hay memoria confiable."
        },
        {
          "source": "Integridad academica",
          "target": "Evidencia verificable",
          "kind": "depends_on",
          "justification": "La integridad requiere respaldo trazable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura se fortalece con fuentes comprobables."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "El cierre util deriva del razonamiento argumentado."
        },
        {
          "source": "Resolucion de placeholders",
          "target": "Normalizacion estructurada",
          "kind": "supports",
          "justification": "Evita rutas rotas y errores de compilacion."
        },
        {
          "source": "Propagacion transversal conservadora",
          "target": "Identidad institucional UnADM",
          "kind": "supports",
          "justification": "Permite compartir reglas estables sin perder contexto local."
        }
      ],
      "evidence": [
        "README de materia destino: identidad UnADM y pauta editorial.",
        "Programa analitico destino: ejes de trabajo y proposito editorial.",
        "Archivo .bib local con fuentes base institucionales.",
        "Regla heredada estable: bloquear si no hay JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 14: se refuerzan gates de parseo JSON y normalizacion previa.",
      "Ciclo 14: se agregan patrones argumentativos transferibles desde actividad origen.",
      "Ciclo 14: se mantiene exclusion de contenido tematico no equivalente entre materias.",
      "Ciclo 14: se consolida manejo de placeholders como control tecnico transversal."
    ]
  }
}