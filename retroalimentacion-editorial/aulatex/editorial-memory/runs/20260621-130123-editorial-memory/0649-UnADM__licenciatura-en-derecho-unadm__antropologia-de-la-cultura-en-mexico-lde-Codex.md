{
  "summary": [
    "Sincronizacion transversal ciclo 9 aplicada con union-dedupe lossless y sin regresion.",
    "Se preserva ADN UnADM del destino y se incorporan abstracciones estables del origen.",
    "Se transfiere solo estructura reusable: objetivo, problema, evidencia, analisis propio y cierre transferible.",
    "Se excluyen contenidos tematicos propios de Filosofia del Derecho por no equivalencia disciplinar.",
    "Se mantiene alerta institucional: no propagar salidas no JSON sin normalizacion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener contexto curricular local del destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar toda fuente heredada no verificada como provisional.",
    "No trasladar metadatos curriculares de Filosofia del Derecho al destino."
  ],
  "structure_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Organizar en secciones: conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear el artefacto al producto pedido por la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias canonicas de estructura.",
    "Resolver placeholders de nombre de .bib a nombre literal antes de uso."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar solo resumen.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Evitar extrapolar fuentes de otras semanas o materias sin validacion local.",
    "Cerrar con conclusion aplicable a practica juridica o sociojuridica."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar esquema minimo completo antes de reutilizar memoria.",
    "Normalizar manualmente salidas no estructuradas heredadas.",
    "Confirmar que toda afirmacion tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que rutas y nombres no contengan tokens sin expandir."
  ],
  "latex_rules": [
    "Mantener plantilla .tex local de la materia como base.",
    "Usar espanol y acentos consistentes en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Corregir nombres truncados detectados en README.",
    "Resolver tokens tipo $(@{...}.Slug) en README y programa analitico."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes consultables.",
    "Priorizar fuentes institucionales UnADM y oficiales aplicables.",
    "Registrar fuentes especificas por actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Mantener unadmSitioWeb y unadmMallaDerecho2024 como base local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y abstractas.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "No propagar redaccion literal ni contenido tematico de materia origen.",
    "Registrar incidencias de parseo como alertas institucionales reutilizables.",
    "Mantener estrategia conservadora: agregar solo mejoras verificables."
  ],
  "open_questions": [
    "Supuesto: falta consigna puntual de actividades de Antropologia; confirmar productos exactos por semana.",
    "Confirmar si LDE-S4B2 es clave oficial o etiqueta local.",
    "Confirmar estandar unico de citacion institucional (APA u otro).",
    "Confirmar si la conclusion juridica es obligatoria en todas las actividades de esta materia.",
    "Confirmar regla definitiva de nombre canonico del .bib frente a plantillas dinamicas."
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
        "Integridad academica con trazabilidad.",
        "Normalizacion estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura destino: Antropologia de la cultura en Mexico.",
        "Semestre 4, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema claro.",
      "Conceptos pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y utiles.",
      "Sostener coherencia institucional y calidad tecnica en LaTeX."
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
      "Consigna -> desarrollo alineado -> cierre coherente."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON parseable",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion transferible",
        "No traslape de metadatos entre materias"
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
          "justification": "La postura se legitima con respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion util depende del razonamiento propio."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "No traslape de metadatos entre materias",
          "kind": "supports",
          "justification": "La consistencia institucional exige contexto curricular local."
        }
      ],
      "evidence": [
        "README local: identidad UnADM y ubicacion curricular.",
        "Programa analitico: ejes problema, conceptos, producto, analisis y cierre.",
        "Bib local: unadmSitioWeb y unadmMallaDerecho2024.",
        "Memoria origen: gate de JSON parseable y normalizacion previa."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin perdida semantica.",
      "Se reforzo gate de parseo JSON como condicion de propagacion.",
      "Se transfirieron patrones argumentativos estables y no contenido doctrinal de origen.",
      "Se mantuvo politica de supuestos y fuentes provisionales.",
      "Se conservaron reglas utiles previas del destino sin eliminacion."
    ]
  }
}