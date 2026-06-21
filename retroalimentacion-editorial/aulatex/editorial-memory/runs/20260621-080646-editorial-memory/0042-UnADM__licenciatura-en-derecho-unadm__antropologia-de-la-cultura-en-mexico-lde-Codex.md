{
  "summary": [
    "Se consolida sincronizacion transversal entre actividad de origen y materia destino sin recortar reglas utiles.",
    "Se transfieren solo abstracciones editoriales estables: identidad UnADM, estructura argumentativa reusable, gates de calidad y trazabilidad de fuentes.",
    "Se preserva el contexto local del destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Se mantiene compresion lossless por union-dedupe y control de no regresion.",
    "Se refuerza normalizacion obligatoria cuando existan salidas no JSON parseable en memoria heredada."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener contexto curricular local del destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No trasladar metadatos especificos de Filosofia del Derecho al nodo de Antropologia."
  ],
  "structure_rules": [
    "Iniciar cada entrega con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar secciones en: conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear el artefacto al producto pedido por la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias canonicas de estructura."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar solo resumen descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Cerrar con conclusion transferible a la practica juridica.",
    "En contenidos culturales, construir puente argumentativo con dimension juridica."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar esquema minimo completo antes de reutilizar memoria.",
    "Normalizar manualmente respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Verificar consistencia entre citas en texto y archivo .bib.",
    "No promover reglas provisionales a definitivas sin validacion disciplinar."
  ],
  "latex_rules": [
    "Mantener plantilla .tex local como base y no cambiar clase sin justificacion.",
    "Usar configuracion de espanol y acentos coherentes en .tex y .bib.",
    "Mantener campos institucionales completos y actualizados por actividad.",
    "Resolver tokens dinamicos sin expandir en README, programa, rutas y nombres de archivo.",
    "Corregir rutas con caracteres truncados antes de compilar.",
    "Compilar sin errores criticos, sin referencias rotas y con bibliografia enlazada."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes especificas por actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Mantener unadmSitioWeb y unadmMallaDerecho2024 como base local confirmada."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y estables entre nodos no equivalentes.",
    "Compartir abstracciones editoriales, no redaccion literal ni contenido tematico de origen.",
    "Preservar reglas utiles previas y agregar solo mejoras verificables.",
    "Registrar incidencias de parseo como alertas reutilizables inter-materias.",
    "Si falta contexto local en nodos vecinos, iniciar cerebro minimo con supuestos marcados."
  ],
  "open_questions": [
    "Supuesto: falta consigna puntual de actividades concretas en la materia destino; confirmar productos por semana.",
    "Confirmar si conclusion juridica es obligatoria en el 100% de actividades antropologicas.",
    "Confirmar estandar formal unico de citacion para la licenciatura.",
    "Confirmar si LDE-S4B2 es clave oficial institucional o etiqueta operativa local.",
    "Confirmar que todos los placeholders heredados ya fueron resueltos en archivos activos."
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
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 4, bloque 2, obligatoria, 8 creditos.",
        "Asignatura destino: Antropologia de la cultura en Mexico."
      ]
    },
    "essence": [
      "Problema, conceptos, evidencia, analisis propio y conclusion transferible.",
      "Normalizacion estructurada antes de cualquier propagacion.",
      "Compresion lossless por deduplicacion sin perdida de reglas validas."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y utiles profesionalmente.",
      "Sostener coherencia institucional, metodologica y tecnica en toda la suite LaTeX."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Cierre con valor juridico aplicado."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente verificable -> interpretacion propia.",
      "Coherencia interna entre consigna, desarrollo y cierre."
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
          "justification": "Sin parseo valido no hay reutilizacion confiable."
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
          "justification": "La conclusion aplicable surge del razonamiento sustentado."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Propagacion transversal conservadora",
          "kind": "supports",
          "justification": "La identidad comun permite transferir reglas estables entre materias."
        }
      ],
      "evidence": [
        "README y programa analitico del destino fijan ejes y pauta institucional.",
        "Memoria origen valida ejes editoriales generales reutilizables.",
        "Memoria heredada reporta incidentes de parseo y exige normalizacion previa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 42: se reforzo transferencia de abstracciones estables sin arrastre tematico de Filosofia del Derecho.",
      "Ciclo 42: se mantuvo no regresion en gates de parseo JSON y normalizacion estructurada.",
      "Ciclo 42: se consolidaron reglas de trazabilidad bibliografica y resolucion de placeholders."
    ]
  }
}