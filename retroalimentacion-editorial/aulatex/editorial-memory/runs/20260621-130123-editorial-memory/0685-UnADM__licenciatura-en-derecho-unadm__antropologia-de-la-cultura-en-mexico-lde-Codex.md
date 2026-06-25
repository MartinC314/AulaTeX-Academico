{
  "summary": [
    "Sincronizacion transversal consolidada con union-dedupe lossless y sin regresion.",
    "Se preservan reglas institucionales UnADM, normalizacion estructurada y parseo JSON obligatorio.",
    "Se transfieren solo abstracciones estables desde Filosofia del Derecho hacia Antropologia.",
    "Se evita migrar contenido tematico exclusivo del origen por no equivalencia de nodos.",
    "Se refuerzan ejes comunes: problema, conceptos, evidencia, analisis propio y conclusion transferible.",
    "Se mantiene alerta de fuentes heredadas no verificadas como provisionales."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Respetar contexto curricular local del destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar toda fuente heredada no verificada como provisional hasta confirmacion local.",
    "No trasladar metadatos especificos de Filosofia del Derecho al destino."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco pertinente, analisis propio y cierre.",
    "Alinear el producto al entregable de planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias canonicas."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Evitar conclusiones sin puente argumentativo entre cultura y derecho.",
    "Cerrar con conclusion transferible a practica juridica."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar memoria.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No promover reglas provisionales a definitivas sin validacion disciplinar."
  ],
  "latex_rules": [
    "Mantener plantilla .tex local como base.",
    "Usar espanol y acentos correctos en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver placeholders tipo $(@{...}.Slug) en README, programa y rutas antes de compilar.",
    "Corregir nombres de archivo truncados o corruptos en estructura local."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo obras verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes especificas de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener trazabilidad de activos locales cuando se cite assets-unadm."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y estables.",
    "Transferir abstracciones editoriales, no redaccion literal.",
    "Preservar reglas utiles previas; agregar solo mejoras verificables.",
    "Registrar incidencias de parseo como alertas reutilizables inter-nodos.",
    "Si falta contexto local, mantener cerebro minimo y dejar vacios en preguntas abiertas."
  ],
  "open_questions": [
    "Supuesto: confirmar si LDE-S4B2 es clave institucional definitiva.",
    "Confirmar rubrica de evaluacion propia de Antropologia de la cultura en Mexico.",
    "Confirmar estandar unico de citas de la licenciatura (APA u otro).",
    "Confirmar si conclusion juridica aplica a todas las actividades de la materia o solo algunas.",
    "Confirmar resolucion final de placeholders en archivos de guia."
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
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada obligatoria antes de propagar.",
        "Fuentes heredadas tratadas como provisionales."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura destino: Antropologia de la cultura en Mexico.",
        "Semestre 4, bloque 2, obligatoria, 8 creditos.",
        "No traslape de metadatos entre materias."
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
      "Convertir planeacion semanal en productos academicos trazables y utiles profesionalmente.",
      "Asegurar coherencia entre identidad institucional, estructura argumentativa y evidencia."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Cierre con valor profesional."
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
        "Conclusion juridica transferible",
        "Transferencia transversal conservadora"
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
          "justification": "La conclusion util deriva del razonamiento, no del resumen."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "La pauta institucional exige integridad academica."
        }
      ],
      "evidence": [
        "README local: identidad UnADM, ubicacion curricular y pauta editorial.",
        "Programa analitico local: ejes problema, conceptos, producto, analisis y cierre.",
        "Bib local: fuentes base institucionales verificables.",
        "Memoria origen: regla estable de normalizacion y parseo JSON obligatorio."
      ]
    },
    "reinforcement_log": [
      "Ciclo 18: se refuerza gate de JSON parseable como condicion de propagacion.",
      "Ciclo 18: se integran patrones argumentativos estables del origen sin migrar tematica disciplinar.",
      "Ciclo 18: se conserva politica de supuestos marcados y fuentes provisionales.",
      "Ciclo 18: se refuerza resolucion de placeholders y control de rutas LaTeX/BibTeX."
    ]
  }
}