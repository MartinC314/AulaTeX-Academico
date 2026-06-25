{
  "summary": [
    "Se consolida sincronizacion transversal con reglas estables reutilizables entre nodos no equivalentes.",
    "Se preserva identidad UnADM, cinco ejes editoriales y control de calidad estructural.",
    "Se mantiene compresion lossless por union-dedupe sin regresion.",
    "Se refuerza validacion JSON parseable y normalizacion previa a propagacion recursiva.",
    "Se evita transferencia de redaccion literal de actividad origen hacia materia destino."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Conservar trazabilidad de origen editorial en cada consolidacion.",
    "Marcar como [supuesto] todo dato no visible en consigna o documentos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales y no como autoridad academica."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en bloques: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear estructura al producto solicitado en planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Aplicar cinco ejes: problema, conceptos, producto solicitado, analisis propio, conclusion transferible."
  ],
  "activity_rules": [
    "Verificar instruccion especifica de cada actividad antes de redactar.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Exigir postura argumentada del estudiante en cada entrega.",
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Comprobar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Agregar fuentes especificas de actividad al .bib local antes de version final."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de fusionar memoria.",
    "Confirmar que cada afirmacion factual tenga fuente o marca de [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar union-dedupe sin eliminar reglas utiles previas.",
    "Normalizar manualmente salidas no estructuradas heredadas antes de reutilizarlas."
  ],
  "latex_rules": [
    "Usar plantilla .tex local de la materia como base.",
    "Conservar macros institucionales de portada y curso.",
    "Mantener compatibilidad con espanol y letterpaper definida en plantilla.",
    "No eliminar campos de portada; completar faltantes segun actividad.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README o rutas antes de compilar.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Usar etapas-del-proceso-y-estrategia-del-litigio.bib como repositorio local.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; registrar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Incluir fecha de consulta en fuentes web o institucionales dinamicas.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales y estables.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "No propagar metadatos o redactados literales de actividades de otra asignatura.",
    "Mantener advertencia de normalizacion manual para herencias no parseables de ciclos iniciales.",
    "Reforzar transversalmente regla de JSON parseable antes de cualquier fusion."
  ],
  "open_questions": [
    "Confirmar si documentauthor debe ser fijo de plantilla o variable por estudiante. [supuesto]",
    "Confirmar estilo de citacion juridica requerido por la asignatura.",
    "Confirmar si coursecode LDE-S5B2 es definitivo institucionalmente. [supuesto]",
    "Verificar y corregir nombres con caracteres corruptos en README. [supuesto]",
    "Confirmar checklist minimo por tipo de producto: reporte, presentacion, material visual."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Verificable y orientado a practica profesional."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta de asignatura como entrada canonica.",
        "Trazabilidad editorial en consolidaciones."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 5, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Etapas del proceso y estrategia del litigio."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y fundamento normativo/doctrinal.",
      "Producto alineado a planeacion.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos juridicos claros, verificables y aplicables.",
      "Sostener consistencia institucional y calidad tecnica en toda entrega."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Bloques argumentativos visibles.",
      "Citas trazables.",
      "Cierre juridico aplicable.",
      "Marcado explicito de [supuesto] cuando falte verificacion."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis propio -> conclusion juridica.",
      "Afirmacion -> evidencia verificable -> interpretacion -> implicacion practica.",
      "Objetivo puntual -> desarrollo estructurado -> cierre transferible."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Cinco ejes editoriales",
        "JSON parseable",
        "Normalizacion estructurada",
        "Union-dedupe sin regresion",
        "Conclusion juridica transferible",
        "Integridad academica con citas verificables"
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
          "source": "Union-dedupe sin regresion",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Conserva reglas utiles sin perdida."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Estructura de entrega",
          "kind": "develops",
          "justification": "Definen secuencia reusable para cualquier actividad."
        },
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica con citas verificables",
          "kind": "supports",
          "justification": "La identidad institucional exige verificabilidad documental."
        }
      ],
      "evidence": [
        "README de materia: ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "Bib local: claves institucionales existentes.",
        "Plantilla tex local: macros y metadatos institucionales."
      ]
    },
    "reinforcement_log": [
      "Ciclo 19: se transfieren solo abstracciones estables desde actividad origen.",
      "Ciclo 19: se preservan reglas previas utiles y se deduplican variantes redundantes.",
      "Ciclo 19: se refuerzan gates de JSON parseable, normalizacion y no regresion.",
      "Ciclo 19: se mantiene separacion entre fuentes provisionales y autoridad academica."
    ]
  }
}