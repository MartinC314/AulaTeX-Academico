{
  "summary": [
    "Sincronizacion transversal completada con union-dedupe lossless y sin regresion.",
    "Se preserva identidad UnADM y contexto curricular local de la materia destino.",
    "Se incorporan abstractions estables del origen: objetivo, evidencia, analisis propio y cierre transferible.",
    "Se mantiene regla critica: bloquear propagacion si no hay JSON parseable.",
    "Se refuerza normalizacion de placeholders y rutas corruptas en README, programa y archivos LaTeX/BibTeX.",
    "Se evita transferir contenido tematico especifico de Filosofia del Derecho al nodo de Antropologia."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener contexto curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de la materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "No mover metadatos curriculares de otra asignatura al destino."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos, marco teorico-normativo, analisis propio y cierre.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias operativas de estructura."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuente verificable y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar resumen descriptivo.",
    "Distinguir evidencia, interpretacion y opinion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion transferible a la practica juridica.",
    "En Antropologia, conectar lo cultural con lo juridico mediante puente argumentativo explicito."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar esquema minimo completo antes de reutilizar memoria.",
    "Normalizar manualmente respuestas no estructuradas en ciclo 1.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Verificar consistencia entre citas en texto y archivo .bib.",
    "Comprobar que rutas y nombres no contengan placeholders sin resolver.",
    "No elevar reglas provisionales a definitivas sin validacion disciplinar."
  ],
  "latex_rules": [
    "Mantener plantilla .tex local como base.",
    "Conservar configuracion en espanol y metadatos institucionales completos.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens tipo $(@{...}.Slug) a nombres literales antes de compilar.",
    "Corregir caracteres truncados o anomalias en rutas y nombres de archivo."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes consultables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales pertinentes.",
    "Registrar fuentes de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener trazabilidad de activos locales cuando se cite material de assets-unadm."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y estables.",
    "Compartir entre nodos no equivalentes solo abstracciones editoriales reutilizables.",
    "Preservar union-dedupe lossless sin borrar reglas utiles previas.",
    "Registrar incidencias de parseo como alertas transversales reutilizables.",
    "Mantener enfoque progresivo y conservador: reforzar primero identidad, estructura y gates."
  ],
  "open_questions": [
    "Supuesto: falta consigna especifica de actividades locales de Antropologia; confirmar formatos exactos por semana.",
    "Confirmar estandar unico de citacion para la licenciatura.",
    "Confirmar si la clave LDE-S4B2 es oficial institucional o local.",
    "Confirmar politica sobre mantener autor y matricula prellenados en plantillas.",
    "Confirmar si toda actividad de la materia exige conclusion juridica explicita."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y preciso.",
        "Argumentativo con criterio propio.",
        "Sensible al contexto cultural mexicano."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con trazabilidad de fuentes.",
        "Carpeta de materia como entrada canonica.",
        "Uso de supuestos marcados cuando falta evidencia local."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Antropologia de la cultura en Mexico.",
        "Semestre 4, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema claro.",
      "Conceptos pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos estructurados y trazables.",
      "Sostener coherencia institucional entre materias sin mezclar contenidos disciplinares."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Citas verificables en cada afirmacion clave.",
      "Cierre con utilidad profesional.",
      "Supuestos siempre etiquetados."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente -> interpretacion propia.",
      "Consigna -> desarrollo alineado -> verificacion final de coherencia."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "JSON parseable",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Puente cultural-juridico"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "JSON parseable",
          "target": "Normalizacion estructurada",
          "kind": "depends_on",
          "justification": "Sin parseo valido no hay propagacion confiable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "El analisis gana validez cuando tiene respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion util surge del razonamiento y no del resumen."
        },
        {
          "source": "Puente cultural-juridico",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "En Antropologia evita reduccionismos y mejora aplicabilidad."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "La pauta institucional exige integridad academica y citas comprobables."
        }
      ],
      "evidence": [
        "README local de la materia destino.",
        "Programa analitico local con ejes de trabajo.",
        "Archivo antropologia-de-la-cultura-en-mexico.bib con fuentes base institucionales.",
        "Regla heredada estable de bloqueo por no-JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin perdida semantica.",
      "Se conservaron gates criticos de parseo y normalizacion.",
      "Se transfirieron patrones argumentativos estables, no redaccion literal.",
      "Se mantuvo separacion entre identidad transversal y contenido disciplinar local.",
      "Se abrieron vacios contextuales que requieren confirmacion local."
    ]
  }
}