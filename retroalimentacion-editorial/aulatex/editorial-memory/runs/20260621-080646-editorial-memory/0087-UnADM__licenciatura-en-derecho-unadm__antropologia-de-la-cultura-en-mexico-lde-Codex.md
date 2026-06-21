{
  "summary": [
    "Sincronizacion transversal ciclo 87 aplicada con union-dedupe lossless.",
    "Se preserva identidad UnADM y contexto curricular local de Antropologia.",
    "Se incorporan solo abstracciones estables del origen: objetivo, evidencia, analisis propio y cierre.",
    "Se mantiene regla de normalizacion obligatoria antes de propagacion recursiva.",
    "Se refuerza control de placeholders y rutas corruptas detectadas en README y programa."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener contexto local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "No transferir metadatos especificos de Filosofia del Derecho al nodo de Antropologia."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear el artefacto al producto solicitado por la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias canonicas del nodo."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Evitar extrapolar contenidos tematicos de otras materias sin puente disciplinar.",
    "Cerrar con conclusion transferible a la practica juridica."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa del esquema antes de reutilizar.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar consistencia entre metadatos del documento y contexto curricular local.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "No promover reglas provisionales a definitivas sin evidencia local."
  ],
  "latex_rules": [
    "Mantener plantilla .tex local como base de trabajo.",
    "Usar configuracion de espanol coherente y acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Compilar sin errores criticos ni citas rotas.",
    "Resolver tokens dinamicos tipo $(@{...}.Slug) a nombres literales antes de compilar.",
    "Corregir rutas truncadas o caracteres anomalos en nombres de archivo."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales pertinentes.",
    "Registrar fuentes especificas de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente o URL.",
    "Validar correspondencia entre citas en texto y entradas .bib.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y estables.",
    "Compartir entre nodos no equivalentes solo abstracciones editoriales reutilizables.",
    "Evitar transferencia de redaccion literal y de contenido tematico exclusivo del origen.",
    "Mantener compresion lossless por union-dedupe sin eliminar reglas utiles previas.",
    "Registrar incidencias de parseo como alerta transversal reutilizable.",
    "Si falta contexto local, conservar reglas generales y abrir preguntas explicitas."
  ],
  "open_questions": [
    "Supuesto: falta consigna puntual de actividades de Antropologia; confirmar formato requerido por semana.",
    "Confirmar estandar de citacion oficial de la licenciatura.",
    "Confirmar si coursecode LDE-S4B2 es clave institucional definitiva.",
    "Confirmar politica local sobre conclusion juridica en actividades de enfoque cultural.",
    "Confirmar lista de fuentes obligatorias propias de la materia."
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
      "Problema.",
      "Conceptos.",
      "Evidencia.",
      "Analisis propio.",
      "Conclusion transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables.",
      "Asegurar coherencia argumentativa y utilidad profesional.",
      "Preservar identidad institucional y calidad tecnica documental."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Cierre con valor juridico aplicado."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente -> interpretacion propia.",
      "Pregunta guia -> desarrollo -> respuesta final coherente."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON parseable",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
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
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura academica exige respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "El cierre profesional deriva del razonamiento."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Propagacion transversal conservadora",
          "kind": "supports",
          "justification": "La identidad fija limites de transferencia entre materias."
        }
      ],
      "evidence": [
        "README local con pauta institucional y estructura de archivos.",
        "Programa analitico con ejes problema-conceptos-producto-analisis-conclusion.",
        "Bib local con fuentes base unadmSitioWeb y unadmMallaDerecho2024."
      ]
    },
    "reinforcement_log": [
      "Ciclo 87: se deduplican reglas repetidas sin perdida semantica.",
      "Ciclo 87: se transfieren abstracciones estables desde Filosofia del Derecho.",
      "Ciclo 87: se evita migrar contenido tematico no transversal.",
      "Ciclo 87: se refuerzan gates de parseo, supuestos y trazabilidad bibliografica."
    ]
  }
}