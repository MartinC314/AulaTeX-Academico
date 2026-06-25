{
  "summary": [
    "Sincronizacion transversal ciclo 7 aplicada con union-dedupe lossless y sin regresion.",
    "Se conservan reglas institucionales UnADM, estructura canonica y gates de calidad.",
    "Se transfieren solo abstracciones estables desde actividad de Filosofia del Derecho.",
    "Se evita traslado de contenido tematico especifico de Filosofia al nodo de Antropologia.",
    "Se refuerza normalizacion obligatoria de salidas no estructuradas antes de propagar.",
    "Se mantiene alerta historica: salidas previas no JSON parseable (Codex y GPT-Pro)."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Respetar contexto curricular local del destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar toda fuente heredada no verificada como provisional.",
    "No transferir metadatos curriculares de Filosofia del Derecho al destino."
  ],
  "structure_rules": [
    "Iniciar cada entrega con objetivo puntual y encuadre del problema.",
    "Organizar desarrollo en secciones reutilizables: conceptos, marco, analisis propio y cierre.",
    "Alinear el artefacto al producto exigido por la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias canonicas de estructura."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Cerrar con conclusion transferible a practica juridica en clave de la materia destino."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar esquema minimo completo antes de reutilizar memoria.",
    "Normalizar manualmente respuestas no estructuradas detectadas en ciclos previos.",
    "Confirmar consistencia entre metadatos del documento y contexto curricular local.",
    "Confirmar que toda afirmacion tenga respaldo o marca de supuesto.",
    "No consolidar reglas provisionales como definitivas sin validacion local."
  ],
  "latex_rules": [
    "Mantener plantilla .tex local como base sin cambios de clase no justificados.",
    "Usar espanol con acentos correctos en .tex y .bib.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Resolver placeholders tipo $(@{...}.Slug) en README, programa y rutas antes de compilar.",
    "Corregir nombres/rutas truncadas antes de compilacion.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables.",
    "Registrar fuentes especificas de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Mantener metadatos minimos: autor, titulo, anio, fuente o URL.",
    "Validar consistencia entre citas en texto y claves BibTeX.",
    "Priorizar fuentes institucionales UnADM y materiales pertinentes al tema local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y estructuradas.",
    "Propagar transversalmente abstracciones editoriales, no redaccion literal.",
    "Preservar historial de alertas de parseo como control inter-materias.",
    "Aplicar estrategia conservadora: agregar mejoras verificables sin eliminar reglas utiles previas."
  ],
  "open_questions": [
    "Supuesto: falta consigna puntual de actividades especificas en el destino; confirmar productos exactos.",
    "Confirmar estandar unico de citacion institucional para toda la licenciatura.",
    "Confirmar caracter oficial de la clave LDE-S4B2.",
    "Confirmar si la conclusion juridica aplica a todas las actividades de Antropologia."
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
      "Convertir planeacion semanal en productos academicos trazables.",
      "Garantizar coherencia entre forma, contenido y evidencia.",
      "Sostener identidad UnADM en cada entrega."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Supuestos marcados cuando falte dato.",
      "Secciones funcionales y cierre util.",
      "Sin afirmaciones sin respaldo."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente -> interpretacion propia.",
      "Pregunta guia -> respuesta coherente final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Validacion JSON parseable",
        "Normalizacion estructurada",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible"
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
          "justification": "Sin parseo valido no hay memoria reutilizable."
        },
        {
          "source": "Integridad academica",
          "target": "Evidencia verificable",
          "kind": "depends_on",
          "justification": "La integridad exige respaldo trazable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura propia gana solidez con fuentes."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion surge del razonamiento, no del resumen."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional fija estandares de calidad y cita."
        }
      ],
      "evidence": [
        "README de materia destino: identidad UnADM y pauta editorial.",
        "Programa analitico destino: ejes problema, conceptos, producto, analisis y cierre.",
        "Bib local: unadmSitioWeb y unadmMallaDerecho2024.",
        "Historial: incidencias de salida no JSON parseable en ciclos previos."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin perdida semantica.",
      "Se conservaron gates de parseo y normalizacion como nucleo transversal.",
      "Se reforzo transferencia estable: objetivo, evidencia, postura, coherencia.",
      "Se excluyo contenido doctrinal especifico de Filosofia por no equivalencia de nodo.",
      "Se mantuvo marcado de supuestos y provisionalidad de fuentes heredadas."
    ]
  }
}