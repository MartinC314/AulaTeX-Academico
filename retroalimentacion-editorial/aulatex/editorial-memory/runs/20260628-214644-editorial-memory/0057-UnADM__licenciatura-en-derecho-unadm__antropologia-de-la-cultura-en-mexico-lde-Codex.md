{
  "summary": [
    "Sincronizacion transversal aplicada desde actividad de Filosofia del Derecho hacia materia de Antropologia con estrategia conservadora.",
    "Se transfieren solo abstracciones editoriales estables: objetivo, estructura argumentativa, evidencia verificable y cierre transferible.",
    "Se preserva identidad UnADM y contexto curricular local del destino sin mezclar metadatos de la materia origen.",
    "Se refuerza regla de normalizacion: no propagar memoria no parseable o no estructurada.",
    "Se mantiene compresion lossless por union-dedupe sin eliminar reglas utiles previas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion local: Licenciatura en Derecho.",
    "Mantener contexto local del destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "No trasladar datos curriculares especificos de Filosofia del Derecho al destino.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Usar carpeta de materia como entrada canonica.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Ordenar desarrollo en: conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear el artefacto al producto solicitado por la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias de estructura reusable."
  ],
  "activity_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Incluir postura argumentada del estudiante; evitar resumen descriptivo puro.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion transferible a la practica juridica cuando la consigna lo permita [supuesto]."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Exigir esquema minimo completo antes de reutilizar memoria.",
    "Normalizar manualmente respuestas no estructuradas en ciclo 1.",
    "Validar consistencia entre metadatos del documento y contexto curricular local.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "No convertir reglas provisionales en definitivas sin validacion disciplinar."
  ],
  "latex_rules": [
    "Mantener plantilla LaTeX local de la materia como base.",
    "Usar configuracion de espanol coherente y acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver placeholders tipo $(@{...}.Slug) en README, programa y rutas antes de compilar.",
    "Corregir nombres de archivo truncados o con caracteres anómalos antes de referenciar."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Agregar entradas especificas por actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Validar correspondencia entre citas en texto y entradas del .bib.",
    "Distinguir bibliografia base de bibliografia especifica de actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y abstractas entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferir contenido tematico literal de Filosofia del Derecho a Antropologia.",
    "Registrar incidencias de parseo como alertas transversales reutilizables.",
    "Mantener estrategia progresiva y conservadora: agregar mejoras verificables sin regresion."
  ],
  "open_questions": [
    "Confirmar si la conclusion juridica es obligatoria en todas las actividades de Antropologia o depende de la consigna.",
    "Confirmar estandar unico de citacion de la licenciatura (APA u otro).",
    "Confirmar si LDE-S4B2 es clave oficial o convencion local.",
    "Confirmar que todos los placeholders de Slug fueron resueltos en archivos de control.",
    "Confirmar rubricas locales para calibrar profundidad argumentativa por actividad."
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
        "Destino local: semestre 4, bloque 2, obligatoria, 8 creditos.",
        "Materia destino: Antropologia de la cultura en Mexico."
      ]
    },
    "essence": [
      "Problema, conceptos, evidencia, analisis propio y cierre transferible.",
      "Normalizacion estructurada previa a toda propagacion.",
      "Compresion lossless por deduplicacion sin recorte."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables academicos trazables y utiles profesionalmente.",
      "Sostener coherencia transversal entre materias sin perder contexto local."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Conclusiones con utilidad practica."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente verificable -> interpretacion propia.",
      "Coherencia completa entre guia, desarrollo y cierre."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion estructurada",
        "Validacion JSON parseable",
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
          "justification": "La postura academica gana solidez con respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion util deriva del razonamiento y no del resumen."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y consistencia formal."
        },
        {
          "source": "Transferencia transversal conservadora",
          "target": "Identidad institucional UnADM",
          "kind": "supports",
          "justification": "Permite sincronizar reglas estables sin contaminar contexto local."
        }
      ],
      "evidence": [
        "README local define identidad UnADM, ubicacion curricular y pauta editorial.",
        "Programa analitico local fija ejes: problema, conceptos, producto, analisis y cierre.",
        "Bib local contiene fuentes base institucionales verificables.",
        "Memoria origen aporta reglas estables de estructura, evidencia y control de calidad."
      ]
    },
    "reinforcement_log": [
      "Se reforzo bloqueo por JSON no parseable.",
      "Se reforzo uso de supuestos para datos no confirmados.",
      "Se reforzo separacion entre abstracciones transferibles y contenido tematico local.",
      "Se reforzo resolucion de placeholders en rutas y nombres.",
      "Se mantuvo union-dedupe sin eliminar reglas utiles previas."
    ]
  }
}