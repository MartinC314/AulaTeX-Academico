{
  "summary": [
    "Se consolida sincronizacion transversal desde actividad de Filosofia del Derecho hacia materia de litigio con estrategia conservadora.",
    "Se preservan reglas estables: identidad UnADM, cinco ejes editoriales, normalizacion estructurada y compresion union-dedupe sin regresion.",
    "Se refuerza gate critico: bloquear propagacion si no hay JSON parseable.",
    "Se mantiene separacion entre fuentes verificadas y fuentes provisionales como nota tecnica.",
    "Se agrega cerebro editorial minimo reusable para nodos no equivalentes sin transferir redaccion literal."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables a Licenciatura en Derecho, semestre 5, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Mantener trazabilidad de origen editorial en cada consolidacion.",
    "Marcar como [supuesto] todo dato no visible en consigna o documentos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Registrar fuentes provisionales como nota tecnica y no como autoridad academica."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear estructura al producto solicitado en planeacion semanal.",
    "Aplicar cinco ejes: problema, conceptos, producto, analisis propio, conclusion transferible.",
    "Cerrar con conclusion juridica aplicable a practica profesional."
  ],
  "activity_rules": [
    "Verificar instruccion especifica de cada actividad antes de redactar.",
    "Rubricar cada entrega contra los cinco ejes del programa analitico.",
    "Exigir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Evitar reutilizar fuentes de otras semanas sin verificar pertinencia.",
    "Agregar fuentes especificas de actividad al .bib local antes de version final."
  ],
  "quality_gates": [
    "Bloquear propagacion si la memoria no es JSON parseable.",
    "Validar estructura minima completa antes de fusionar memoria.",
    "Confirmar que toda afirmacion factual tenga fuente o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar union-dedupe sin eliminar reglas utiles previas.",
    "Normalizar manualmente salidas heredadas no estructuradas antes de reutilizar."
  ],
  "latex_rules": [
    "Usar plantilla .tex local de la materia como base.",
    "Conservar macros institucionales de portada y curso.",
    "Mantener compatibilidad con espanol y letterpaper segun plantilla.",
    "No eliminar campos de portada; completar segun actividad.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y referencias.",
    "Corregir nombres de archivo corruptos antes de compilar.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Usar etapas-del-proceso-y-estrategia-del-litigio.bib como repositorio local.",
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "No inventar referencias; incluir solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Incluir fecha de consulta en fuentes web o institucionales dinamicas.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas abstractas estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "No propagar redaccion literal ni metadatos hiperlocales de actividades.",
    "Mantener advertencia de normalizacion para ciclos con herencia no parseable.",
    "Conservar politica de no regresion en cada fusion futura."
  ],
  "open_questions": [
    "Confirmar si documentauthor es fijo de plantilla o variable por estudiante. [supuesto]",
    "Confirmar estilo de citacion juridica requerido por la asignatura.",
    "Confirmar si coursecode LDE-S5B2 es definitivo institucionalmente. [supuesto]",
    "Corregir definitivamente rutas con caracteres corruptos en README. [supuesto]",
    "Confirmar checklist minimo por tipo de producto: reporte, presentacion y visual."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Juridicamente preciso.",
        "Claro y verificable.",
        "Argumentativo con criterio propio."
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
      "Conceptos y fundamento normativo.",
      "Producto alineado a planeacion.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible.",
      "Normalizacion estructurada antes de propagar."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos juridicos verificables.",
      "Mantener coherencia institucional y calidad tecnica en LaTeX y bibliografia."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Bloques argumentativos explicitos.",
      "Citas trazables.",
      "Cierre juridico aplicable.",
      "Uso explicito de [supuesto] cuando falte evidencia local."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis propio -> conclusion juridica.",
      "Afirmacion -> evidencia -> interpretacion -> implicacion practica.",
      "Objetivo puntual al inicio -> verificacion de cumplimiento al cierre."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Cinco ejes editoriales",
        "JSON parseable",
        "Normalizacion estructurada",
        "Union-dedupe sin regresion",
        "Conclusion juridica transferible"
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
          "justification": "Permite compresion lossless sin perder reglas utiles."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Calidad del entregable",
          "kind": "supports",
          "justification": "Estandariza estructura y profundidad argumentativa."
        },
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Exige verificabilidad y consistencia institucional."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "Bib local: claves institucionales existentes.",
        "Plantilla tex local: macros institucionales y coursecode visible."
      ]
    },
    "reinforcement_log": [
      "Ciclo 12: deduplicacion completa de reglas repetidas entre origen y destino.",
      "Ciclo 12: se preservan reglas utiles previas; no se eliminan gates criticos.",
      "Ciclo 12: se refuerza transferencia por abstracciones estables en salto transversal.",
      "Ciclo 12: se mantienen vacios locales como preguntas abiertas sin inventar fuentes."
    ]
  }
}