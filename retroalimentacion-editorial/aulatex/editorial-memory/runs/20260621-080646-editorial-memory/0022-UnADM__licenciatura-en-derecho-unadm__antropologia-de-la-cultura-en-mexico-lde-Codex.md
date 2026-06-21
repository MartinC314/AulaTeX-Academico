{
  "summary": [
    "Sincronizacion transversal consolidada desde actividad de Filosofia del Derecho hacia materia de Antropologia con estrategia progresiva y conservadora.",
    "Se preservan reglas utiles previas y se aplica deduplicacion lossless sin recorte semantico.",
    "Se transfieren solo abstracciones estables: identidad UnADM, estructura reusable, gates de calidad y patrones argumentativos.",
    "Se evita migrar contenido tematico exclusivo de Filosofia del Derecho al destino no equivalente.",
    "Se refuerza normalizacion obligatoria de salidas no estructuradas antes de propagacion recursiva."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener ubicacion curricular local del destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar toda fuente heredada no verificada como provisional.",
    "No trasladar metadatos curriculares especificos de otra asignatura."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear cada entrega al producto solicitado en la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias canonicas de estructura."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Evitar extrapolar fuentes de otras semanas o materias sin justificacion.",
    "Cerrar con conclusion transferible a la practica juridica con criterio propio."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa del esquema antes de reutilizar.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No promover reglas provisionales a definitivas sin verificacion local disciplinar."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens dinamicos sin expandir en README, programa, rutas y nombres de archivo.",
    "Corregir rutas con caracteres truncados antes de compilar."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes especificas por actividad en el .bib local de la materia destino.",
    "Conservar metadatos minimos: autor, titulo, año, fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Marcar como supuesto cualquier inferencia sobre archivo .bib no confirmada en consigna."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y normalizadas.",
    "Priorizar transferencia de identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferencia literal de redaccion y de contenido tematico no transversal.",
    "Registrar incidencias de parseo como alertas reutilizables inter-materias.",
    "Conservar compresion por union-dedupe y sin regresion en ciclos siguientes."
  ],
  "open_questions": [
    "Confirmar rubrica oficial de evaluacion para Antropologia de la cultura en Mexico.",
    "Confirmar estandar institucional unico de citas para la licenciatura.",
    "Confirmar si la conclusion juridica es obligatoria en todas las actividades de la materia.",
    "Supuesto: la clave LDE-S4B2 es local; validar si existe clave institucional alterna.",
    "Confirmar resolucion definitiva de placeholders de Slug en README y programa analitico."
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
      "Problema juridico o social.",
      "Conceptos pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos estructurados y verificables.",
      "Asegurar consistencia institucional y calidad editorial transversal.",
      "Sostener decisiones argumentativas con evidencia y criterio propio."
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
      "Coherencia entre consigna, desarrollo y cierre."
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
          "justification": "Sin parseo valido no hay memoria reutilizable confiable."
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
          "justification": "La conclusion util deriva del razonamiento argumentado."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Propagacion transversal conservadora",
          "kind": "supports",
          "justification": "La identidad comun permite transferir reglas estables entre nodos no equivalentes."
        }
      ],
      "evidence": [
        "README de materia destino con pauta editorial institucional.",
        "Programa analitico con ejes de trabajo estables.",
        "Regla historica: bloquear propagacion sin JSON parseable.",
        "Bibliografia local con entradas institucionales verificables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 22: deduplicacion integral aplicada sin eliminar reglas utiles previas.",
      "Ciclo 22: se reforzo gate de JSON parseable y normalizacion previa obligatoria.",
      "Ciclo 22: se transfirieron patrones argumentativos estables sin arrastrar temario de Filosofia del Derecho.",
      "Ciclo 22: se mantuvo estado provisional para fuentes heredadas no verificadas."
    ]
  }
}