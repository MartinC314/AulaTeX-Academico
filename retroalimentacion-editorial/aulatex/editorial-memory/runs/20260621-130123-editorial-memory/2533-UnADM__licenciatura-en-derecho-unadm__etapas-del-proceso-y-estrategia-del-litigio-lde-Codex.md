{
  "summary": [
    "Consolidacion transversal ciclo 18 aplicada con union-dedupe sin perdida.",
    "Se preservan reglas estables de identidad UnADM, estructura de cinco ejes y control de calidad.",
    "Se agregan mejoras verificables del contexto local: tokens sin resolver en README/programa y trazabilidad de fuentes provisionales.",
    "No se transfiere redaccion literal de actividad origen; solo abstracciones reutilizables."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Conservar trazabilidad de origen editorial en cada fusion de memoria.",
    "Marcar como [supuesto] todo dato no visible en consigna o documentos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales y fuera de autoridad academica."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear estructura al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Aplicar cinco ejes editoriales: problema, conceptos, producto solicitado, analisis propio, conclusion transferible."
  ],
  "activity_rules": [
    "Verificar instruccion especifica de cada actividad antes de redactar.",
    "Rubricar cada entrega contra los cinco ejes del programa analitico.",
    "Incluir postura argumentada del estudiante; evitar entregas solo descriptivas.",
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Agregar fuentes especificas de actividad al .bib local antes de la version final.",
    "No asumir pertinencia automatica de fuentes de otras semanas o materias."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de fusionar memoria.",
    "Aplicar union-dedupe sin eliminar reglas utiles previas.",
    "Confirmar que cada afirmacion factual tenga fuente o marca de [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas aguas abajo."
  ],
  "latex_rules": [
    "Usar plantilla .tex local de la materia como base.",
    "Conservar macros institucionales de portada y curso.",
    "Mantener compatibilidad con espanol y letterpaper definidos en plantilla.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Mantener claves BibTeX estables para evitar roturas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico antes de referenciar archivos. [supuesto]"
  ],
  "bibliography_rules": [
    "Usar etapas-del-proceso-y-estrategia-del-litigio.bib como repositorio local.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Incluir fecha de consulta en fuentes web o institucionales dinamicas.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales y estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "No propagar metadatos locales especificos de actividad origen.",
    "Mantener advertencia institucional: ciclos con salida no parseable requieren normalizacion manual.",
    "Aplicar estrategia progresiva y conservadora: agregar solo mejoras verificables."
  ],
  "open_questions": [
    "Confirmar si documentauthor en plantilla debe ser fijo o variable por estudiante. [supuesto]",
    "Confirmar estilo de citacion juridica requerido por la asignatura (APA, Chicago, ISO 690 u otro).",
    "Confirmar correccion definitiva de tokens Slug sin resolver en README/programa. [supuesto]",
    "Confirmar checklist minimo por tipo de producto: reporte, presentacion y material visual."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro, verificable y juridicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta de asignatura como entrada canonica.",
        "Fuentes provisionales separadas de autoridad academica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 5, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Etapas del proceso y estrategia del litigio."
      ]
    },
    "essence": [
      "Cinco ejes editoriales como columna vertebral.",
      "Evidencia verificable + analisis propio + conclusion juridica transferible.",
      "Normalizacion estructurada previa a propagacion.",
      "Compresion lossless por union-dedupe sin regresion."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos utiles para practica juridica.",
      "Sostener coherencia institucional y calidad tecnica en LaTeX/BibTeX.",
      "Permitir propagacion transversal segura entre nodos no equivalentes."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Bloques argumentativos visibles.",
      "Citas trazables en cuerpo y .bib.",
      "Cierre juridico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis propio -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> implicacion practica.",
      "Consigna -> estructura -> verificacion por checklist -> entrega."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Cinco ejes editoriales",
        "JSON parseable",
        "Normalizacion estructurada",
        "Union-dedupe sin regresion",
        "Conclusion juridica transferible",
        "Trazabilidad de fuentes"
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
          "target": "Calidad argumentativa de entregas",
          "kind": "supports",
          "justification": "Ordenan problema, sustento, analisis y cierre."
        },
        {
          "source": "Union-dedupe sin regresion",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Preserva reglas utiles y evita perdida."
        },
        {
          "source": "Trazabilidad de fuentes",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Permite verificar afirmaciones y distinguir provisionales."
        },
        {
          "source": "Identidad UnADM",
          "target": "Coherencia institucional transversal",
          "kind": "develops",
          "justification": "Mantiene tono, formato y metadatos comunes."
        }
      ],
      "evidence": [
        "README de materia: ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "Bib local con claves institucionales verificables.",
        "Plantilla .tex local con macros institucionales.",
        "Deteccion local de tokens Slug sin resolver en README/programa. [supuesto]"
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas y se conservaron todas las utiles.",
      "Se reforzo gate de JSON parseable como requisito duro de propagacion.",
      "Se consolido transferencia transversal por abstracciones estables, sin literalidad de actividad origen.",
      "Se incorporo mejora verificable sobre tokens sin resolver como riesgo tecnico local."
    ]
  }
}