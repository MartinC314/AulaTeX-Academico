{
  "summary": [
    "Sincronizacion transversal consolidada con union-dedupe lossless y sin regresion.",
    "Se preservan reglas institucionales UnADM, estructura canonica y gates de parseo JSON.",
    "Se transfieren solo abstracciones estables desde actividad de Filosofia del Derecho.",
    "Se evita transferir contenido tematico exclusivo de Filosofia al nodo de Antropologia.",
    "Se refuerza resolucion de placeholders en README, programa analitico y rutas de archivos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener contexto curricular local del destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar toda fuente heredada no verificada como provisional.",
    "No trasladar metadatos curriculares de materias distintas al destino."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias estructurales primarias."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Cerrar con conclusion transferible a la practica juridica.",
    "Evitar extrapolar fuentes de otras semanas o materias sin justificacion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar memoria.",
    "Revisar y normalizar respuestas no estructuradas antes de propagar.",
    "Confirmar que toda afirmacion tenga respaldo o marca de supuesto.",
    "Verificar consistencia entre citas en texto y archivo .bib local.",
    "No promover reglas provisionales a definitivas sin validacion local."
  ],
  "latex_rules": [
    "Usar configuracion en espanol y acentos correctos en .tex y .bib.",
    "Mantener clase y formato base de la materia salvo justificacion academica.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Compilar sin errores criticos ni referencias indefinidas.",
    "Resolver tokens dinamicos tipo $(@{...}.Slug) a nombres literales antes de compilar.",
    "Corregir rutas con caracteres truncados en README o fuentes antes de uso."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales pertinentes.",
    "Registrar fuentes especificas de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Marcar como supuesto cualquier correspondencia bibliografica no confirmada."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y abstractas entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar propagar redaccion literal o contenido tematico de otra asignatura.",
    "Mantener compresion por union-dedupe sin eliminar reglas utiles previas.",
    "Registrar incidencias de parseo como alertas transversales reutilizables."
  ],
  "open_questions": [
    "Supuesto: falta consigna local de actividades especificas; confirmar formatos por semana.",
    "Confirmar estandar institucional unico de citacion para la licenciatura.",
    "Confirmar si LDE-S4B2 es clave oficial o solo clave local.",
    "Confirmar si toda actividad de la materia exige conclusion juridica explicita.",
    "Confirmar resolucion definitiva del nombre .bib cuando existan placeholders en documentos."
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
        "Materia destino: Antropologia de la cultura en Mexico.",
        "Semestre 4, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema",
      "Conceptos",
      "Evidencia",
      "Analisis propio",
      "Conclusion transferible",
      "Normalizacion estructurada previa a propagacion"
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables y argumentados.",
      "Asegurar continuidad editorial institucional entre actividades y materias.",
      "Preservar calidad tecnica y academica en LaTeX y bibliografia."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados cuando falte evidencia.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente verificable -> interpretacion propia.",
      "Pregunta guia -> desarrollo coherente -> respuesta final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Validacion JSON parseable",
        "Normalizacion estructurada",
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
          "justification": "La identidad institucional exige trazabilidad y rigor."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura personal gana validez con respaldo."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion util deriva del razonamiento argumentado."
        },
        {
          "source": "Validacion JSON parseable",
          "target": "Normalizacion estructurada",
          "kind": "depends_on",
          "justification": "Sin parseo valido no hay consolidacion confiable."
        },
        {
          "source": "Propagacion transversal conservadora",
          "target": "Identidad institucional UnADM",
          "kind": "supports",
          "justification": "La transferencia estable protege coherencia intermaterias."
        }
      ],
      "evidence": [
        "README de materia destino: pauta institucional y entrada canonica.",
        "Programa analitico destino: ejes problema, conceptos, producto, analisis y cierre.",
        "Bibliografia local: unadmSitioWeb y unadmMallaDerecho2024.",
        "Regla persistente: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 44: se consolidan abstracciones estables del origen sin arrastre tematico.",
      "Ciclo 44: se mantiene gate critico de parseo JSON y normalizacion previa.",
      "Ciclo 44: se refuerza marcado de supuestos y provisionalidad de fuentes heredadas.",
      "Ciclo 44: se preserva compresion lossless por deduplicacion sin recorte."
    ]
  }
}