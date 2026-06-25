{
  "summary": [
    "Consolidacion transversal ciclo 3 completada con union-dedupe sin perdida.",
    "Se preservan reglas estables de identidad UnADM, estructura por ejes y control de calidad.",
    "Se refuerza transferencia por abstracciones editoriales entre nodos no equivalentes.",
    "Se mantiene bloqueo de propagacion para salidas no JSON parseable.",
    "Se normaliza contexto local verificable de la materia destino: semestre 5, bloque 2, obligatoria, 8 creditos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Conservar trazabilidad de origen editorial en cada fusion de memoria.",
    "Marcar como [supuesto] todo dato no visible en consigna o documentos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales y no como autoridad academica."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en bloques: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Aplicar cinco ejes editoriales: problema, conceptos, producto, analisis, conclusion transferible.",
    "Alinear formato final al producto solicitado: reporte, presentacion o visual.",
    "Cerrar con conclusion juridica aplicable a la practica profesional."
  ],
  "activity_rules": [
    "Verificar instruccion especifica de cada actividad antes de redactar.",
    "Rubricar cada entrega contra los ejes del programa analitico.",
    "Exigir postura propia sustentada; evitar entregas solo descriptivas.",
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Validar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Agregar fuentes especificas de actividad al .bib local antes de version final."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de fusionar memoria.",
    "Aplicar compresion lossless por union-dedupe sin eliminar reglas utiles previas.",
    "Confirmar que cada afirmacion factual tenga fuente o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Corregir respuestas no estructuradas antes de reutilizacion recursiva."
  ],
  "latex_rules": [
    "Usar plantilla .tex local de la materia como base.",
    "Conservar macros institucionales de portada y curso.",
    "Mantener compatibilidad con espanol y letterpaper de la plantilla.",
    "No eliminar campos de portada; completar faltantes segun consigna.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y referencias.",
    "Verificar nombres reales de archivos antes de compilar."
  ],
  "bibliography_rules": [
    "Usar etapas-del-proceso-y-estrategia-del-litigio.bib como repositorio local.",
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "No inventar referencias; registrar solo fuentes consultables.",
    "Mantener metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Incluir fecha de consulta en fuentes web o institucionales dinamicas.",
    "No citar bibliografia base si no fue usada en el argumento."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales y estables.",
    "No propagar redaccion literal ni metadatos especificos de actividad origen.",
    "Priorizar en saltos transversales: identidad, estructura reusable, quality gates y grafo conceptual.",
    "Mantener advertencia de normalizacion manual para herencias de ciclos no parseables.",
    "Reforzar regla institucional de no regresion en cada ciclo de fusion."
  ],
  "open_questions": [
    "Confirmar si documentauthor debe ser fijo de plantilla o variable por estudiante. [supuesto]",
    "Confirmar estilo de citacion juridica requerido por la asignatura.",
    "Confirmar si coursecode LDE-S5B2 es definitivo en todos los entregables. [supuesto]",
    "Confirmar checklist minimo por tipo de producto: reporte, presentacion, visual.",
    "Confirmar si persisten caracteres corruptos en README y rutas de archivos. [supuesto]"
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Juridicamente preciso.",
        "Claro, verificable y argumentativo."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Entrada canonica en carpeta de asignatura."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 5, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Etapas del proceso y estrategia del litigio."
      ]
    },
    "essence": [
      "Problema juridico activador.",
      "Fundamento conceptual y normativo.",
      "Analisis propio con criterio.",
      "Evidencia verificable.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con rigor juridico y utilidad profesional.",
      "Preservar memoria editorial institucional estable y reusable entre actividades y materias."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Bloques argumentativos visibles.",
      "Citas trazables.",
      "Cierre juridico aplicable.",
      "Marcado explicito de [supuesto] cuando falte evidencia local."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis propio -> conclusion juridica.",
      "Afirmacion -> evidencia -> interpretacion -> implicacion practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Cinco ejes editoriales",
        "JSON parseable",
        "Union-dedupe sin regresion",
        "Conclusión juridica transferible",
        "Fuentes provisionales no autoritativas"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "JSON parseable",
          "target": "Propagacion recursiva segura",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay fusion confiable."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Calidad argumentativa de entregables",
          "kind": "supports",
          "justification": "Dan estructura reusable para cualquier actividad."
        },
        {
          "source": "Union-dedupe sin regresion",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Permite compresion lossless sin perder reglas utiles."
        },
        {
          "source": "Identidad UnADM",
          "target": "Coherencia institucional de la materia",
          "kind": "develops",
          "justification": "Asegura tono, formato y trazabilidad comunes."
        }
      ],
      "evidence": [
        "README de materia: ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y cinco ejes.",
        "Bib local: fuentes institucionales base.",
        "Plantilla tex: macros institucionales y coursecode visible."
      ]
    },
    "reinforcement_log": [
      "Ciclo 3: se deduplican reglas repetidas y se conserva cobertura completa.",
      "Ciclo 3: se refuerza transferencia transversal por abstracciones, no por literalidad.",
      "Ciclo 3: se mantiene gate estricto de JSON parseable y no regresion.",
      "Ciclo 3: se preserva separacion entre fuente provisional y autoridad academica."
    ]
  }
}