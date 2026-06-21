{
  "summary": [
    "Sincronizacion transversal consolidada desde actividad de Filosofia del Derecho hacia materia de Antropologia.",
    "Se preservan reglas estables: identidad UnADM, estructura canonica, evidencia verificable y cierre con criterio juridico.",
    "Se aplica compresion lossless por union-dedupe sin recorte y sin regresion.",
    "Se mantiene alerta institucional: no propagar salidas no JSON parseables sin normalizacion.",
    "Se evita transferir contenido tematico especifico de Filosofia del Derecho al destino no equivalente."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener contexto curricular local del destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar toda fuente heredada no verificada como provisional.",
    "No trasladar metadatos curriculares de otra asignatura al destino."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Distinguir artefactos: reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias canonicamente prioritarias."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Evitar extrapolar fuentes de otras semanas o materias sin validacion local.",
    "Cerrar con conclusion transferible a practica juridica cuando la consigna lo permita."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar memoria.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que cada afirmacion tenga respaldo o marca explicita de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna vigente del destino."
  ],
  "latex_rules": [
    "Mantener plantilla .tex local como base de trabajo.",
    "Usar codificacion en español y acentos correctos en .tex y .bib.",
    "Mantener clase article, letterpaper y oneside salvo instruccion oficial distinta.",
    "Actualizar documenttitle y documentsubtitle por actividad real.",
    "Resolver placeholders tipo $(@{...}.Slug) en README, programa y rutas.",
    "Corregir rutas con caracteres truncados antes de compilar.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales pertinentes.",
    "Registrar fuentes especificas de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, año, fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "No propagar redaccion literal ni contenidos tematicos exclusivos del origen.",
    "Etiquetar incidencias de parseo como alertas reutilizables inter-materias.",
    "Aplicar estrategia progresiva y conservadora: agregar solo mejoras verificables.",
    "Si falta contexto local, mantener cerebro editorial minimo y abrir vacios como preguntas."
  ],
  "open_questions": [
    "Supuesto: confirmar si la conclusion juridica es obligatoria en todas las actividades de Antropologia.",
    "Confirmar rubrica oficial de evaluacion para ajustar profundidad argumentativa.",
    "Confirmar estandar unico de citacion de la licenciatura (APA u otro).",
    "Confirmar si la clave LDE-S4B2 es institucional o solo local.",
    "Confirmar si existe lista de fuentes obligatorias por unidad en la materia destino."
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
        "Destino: Antropologia de la cultura en Mexico.",
        "Semestre 4, bloque 2, obligatoria, 8 creditos."
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
      "Convertir planeacion semanal en productos academicos verificables.",
      "Sostener coherencia institucional y calidad editorial entre actividades y materias."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Citas trazables y consistentes con .bib.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente -> interpretacion propia.",
      "Pregunta guia -> desarrollo coherente -> respuesta final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON parseable",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion transferible",
        "Supuestos explicitados",
        "Separacion de artefactos editoriales"
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
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La utilidad profesional surge del razonamiento."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Supuestos explicitados",
          "kind": "supports",
          "justification": "La integridad academica exige transparencia de incertidumbre."
        }
      ],
      "evidence": [
        "README destino: pauta editorial con identidad UnADM, citas verificables y conclusion juridica.",
        "Programa analitico destino: ejes problema, conceptos, producto, analisis y cierre.",
        "Bibliografia local: unadmSitioWeb y unadmMallaDerecho2024.",
        "Memoria origen: gate estricto de JSON parseable y normalizacion previa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 23: se reforzo gate JSON parseable como condicion dura de propagacion.",
      "Ciclo 23: se incorporaron patrones argumentativos estables del origen sin contenido tematico especifico.",
      "Ciclo 23: se mantuvo compresion union-dedupe lossless y sin eliminacion de reglas utiles.",
      "Ciclo 23: se reforzo resolucion de placeholders y limpieza de rutas antes de compilar."
    ]
  }
}