{
  "summary": [
    "Se consolida memoria transversal minima para materia destino con identidad UnADM y enfoque juridico aplicado.",
    "Se preservan reglas estables transferibles: normalizacion, JSON parseable, union-dedupe sin regresion y cinco ejes editoriales.",
    "Se refuerza que la transferencia entre nodos no equivalentes usa abstracciones, no redaccion literal de actividades.",
    "Se confirma contexto local verificable: semestre 5, bloque 2, obligatoria, 8 creditos y carpeta de asignatura como entrada canonica.",
    "Se mantienen fuentes heredadas no verificadas como provisionales y fuera de autoridad academica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 2, obligatoria, 8 creditos.",
    "Usar tono academico-juridico formal, claro y argumentativo.",
    "Exigir postura propia sustentada en cada producto.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o documentos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear estructura al producto solicitado en planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Aplicar cinco ejes editoriales: problema, conceptos, producto, analisis propio, conclusion."
  ],
  "activity_rules": [
    "Verificar instruccion especifica de cada actividad antes de redactar.",
    "Rubricar la entrega contra los cinco ejes del programa analitico.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Comprobar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Agregar al .bib local solo fuentes realmente usadas."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de fusionar memoria.",
    "Aplicar union-dedupe sin eliminar reglas utiles previas.",
    "Confirmar que toda afirmacion factual tenga fuente o marca de [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Normalizar manualmente herencias no estructuradas antes de reutilizar."
  ],
  "latex_rules": [
    "Usar plantilla .tex local de la materia como base.",
    "Conservar macros institucionales de curso y universidad.",
    "Mantener compatibilidad con español y letterpaper.",
    "No eliminar campos de portada; completar segun actividad.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo con caracteres corruptos visibles en README. [supuesto]",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Usar etapas-del-proceso-y-estrategia-del-litigio.bib como repositorio local.",
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "No inventar referencias.",
    "Registrar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Incluir fecha de consulta en fuentes web o institucionales dinamicas.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales y estables.",
    "No propagar metadatos especificos de una actividad origen a materia destino.",
    "Priorizar en saltos transversales: identidad, estructura reusable, quality gates y grafo conceptual.",
    "Mantener trazabilidad de reglas provisionales hasta verificacion local.",
    "Aplicar estrategia progresiva y conservadora: agregar mejoras verificables sin recortes."
  ],
  "open_questions": [
    "Confirmar si documentauthor en plantilla es fijo o variable por estudiante. [supuesto]",
    "Confirmar estilo de citacion juridica requerido por docente o asignatura.",
    "Confirmar correccion definitiva de rutas con caracteres corruptos en README.",
    "Confirmar si coursecode LDE-S5B2 es codigo institucional oficial o solo de plantilla. [supuesto]",
    "Confirmar checklist minimo por tipo de producto: reporte, presentacion, visual."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Juridicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta de asignatura como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 5, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Etapas del proceso y estrategia del litigio."
      ]
    },
    "essence": [
      "Problema juridico o social que activa la asignatura.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion transferible a la practica juridica."
    ],
    "reason_for_being": [
      "Transformar la planeacion semanal en productos academicos claros, fundamentados y utiles para la practica juridica.",
      "Estandarizar calidad editorial sin perder pertinencia de cada actividad."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Bloques argumentativos visibles.",
      "Citas trazables.",
      "Cierre juridico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis propio -> conclusion juridica.",
      "Afirmacion -> evidencia verificable -> interpretacion -> implicacion practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Cinco ejes editoriales",
        "Normalizacion estructurada",
        "JSON parseable",
        "Union-dedupe sin regresion",
        "Concluson juridica transferible"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica y citas verificables",
          "kind": "supports",
          "justification": "La pauta editorial local exige identidad institucional y verificabilidad."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Estructura de entrega",
          "kind": "develops",
          "justification": "El programa analitico define los ejes como guia de construccion de productos."
        },
        {
          "source": "JSON parseable",
          "target": "Propagacion recursiva segura",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay fusion confiable aguas abajo."
        },
        {
          "source": "Union-dedupe sin regresion",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Permite compresion lossless sin borrar reglas utiles previas."
        }
      ],
      "evidence": [
        "README de materia: ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "Bib local: unadmSitioWeb y unadmMallaDerecho2024.",
        "Plantilla tex local: macros institucionales y coursecode visible."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas manteniendo contenido util.",
      "Se transfirieron solo abstracciones estables desde actividad origen.",
      "Se evito traslado de redaccion literal y de contenido tematico no transversal.",
      "Se reforzaron gates de calidad y trazabilidad de supuestos."
    ]
  }
}