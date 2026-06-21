{
  "summary": [
    "Sincronizacion transversal consolidada con union-dedupe lossless y sin regresion.",
    "Se preserva identidad UnADM y marco curricular local del destino.",
    "Se transfieren solo abstracciones estables desde actividad de Filosofia del Derecho.",
    "Se refuerza normalizacion estructurada y bloqueo por JSON no parseable.",
    "Se evita migrar contenido tematico especifico de Filosofia del Derecho al nodo de Antropologia.",
    "Se mantiene alerta de fuentes heredadas no verificadas como provisionales.",
    "Se corrige a nivel editorial el uso de placeholders Slug en README y programa analitico."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Conservar ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Usar nombre de materia: Antropologia de la cultura en Mexico.",
    "Usar clave local LDE-S4B2 salvo instruccion institucional distinta.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar toda fuente heredada no verificada como provisional."
  ],
  "structure_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Organizar en secciones: conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias editoriales activas.",
    "Resolver placeholders tipo $(@{...}.Slug) a nombres literales antes de usar rutas."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Integrar conceptos antropologicos, culturales, juridicos o sociales pertinentes.",
    "Evitar afirmaciones juridicas sin puente argumentativo cultural."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa del esquema antes de reutilizar.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No propagar reglas provisionales como definitivas sin validacion local disciplinar."
  ],
  "latex_rules": [
    "Mantener plantilla .tex base de la materia como referencia.",
    "Usar configuracion en espanol consistente con la plantilla.",
    "Mantener clase article, letterpaper y oneside salvo consigna distinta.",
    "Actualizar documenttitle y documentsubtitle por actividad real.",
    "Mantener coursename y documentsubject coherentes con la materia destino.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, sin referencias rotas y sin tokens sin expandir."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes especificas de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener trazabilidad de archivos locales usados como evidencia."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y parseables.",
    "Transferir entre nodos no equivalentes solo abstracciones editoriales estables.",
    "No transferir redaccion literal ni metadatos curriculares de otra materia.",
    "Preservar reglas utiles previas y agregar solo mejoras verificables.",
    "Registrar incidencias de parseo como alertas reutilizables inter-materias."
  ],
  "open_questions": [
    "Supuesto: falta consigna puntual de actividades de Antropologia; confirmar formatos por semana.",
    "Confirmar estandar unico de citacion de la licenciatura.",
    "Confirmar si LDE-S4B2 es clave oficial o local.",
    "Confirmar si la conclusion juridica aplica a todas las actividades de la materia.",
    "Confirmar si existen fuentes obligatorias adicionales a unadmSitioWeb y unadmMallaDerecho2024."
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
      "Normalizacion estructurada obligatoria antes de propagar.",
      "Compresion lossless por union y deduplicacion."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables.",
      "Asegurar calidad editorial institucional reusable entre actividades.",
      "Mantener coherencia argumentativa y valor profesional del cierre."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Citas verificables y cierre aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente verificable -> interpretacion propia.",
      "Consigna -> desarrollo alineado -> validacion de coherencia final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON parseable",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Separacion de artefactos editoriales",
        "Marcado de supuestos"
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
          "justification": "La postura argumentativa requiere respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion util deriva del razonamiento y no del resumen."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Separacion de artefactos editoriales",
          "kind": "supports",
          "justification": "La consistencia institucional exige orden entre reporte, presentacion y bibliografia."
        }
      ],
      "evidence": [
        "README local confirma identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico confirma ejes problema-conceptos-producto-analisis-cierre.",
        "Archivo .bib local contiene fuentes institucionales base verificables.",
        "Memoria origen refuerza gates de parseo JSON y normalizacion previa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 15: se consolida transferencia transversal conservadora sin contenido tematico ajeno.",
      "Ciclo 15: se deduplican reglas repetidas y se preservan todas las utiles.",
      "Ciclo 15: se refuerza gate de JSON parseable como condicion de propagacion.",
      "Ciclo 15: se mantiene estado provisional de fuentes heredadas no verificadas.",
      "Ciclo 15: se refuerza resolucion de placeholders Slug en rutas editoriales."
    ]
  }
}