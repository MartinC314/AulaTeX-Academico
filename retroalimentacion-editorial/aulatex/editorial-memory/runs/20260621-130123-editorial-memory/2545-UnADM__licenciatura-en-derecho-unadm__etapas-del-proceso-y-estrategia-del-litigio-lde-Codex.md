{
  "summary": [
    "Se consolida sincronizacion transversal desde actividad de origen hacia materia destino con estrategia conservadora.",
    "Se preservan reglas estables: identidad UnADM, cinco ejes editoriales, validacion JSON, union-dedupe sin regresion.",
    "Se refuerza transferencia por abstracciones reutilizables y no por redaccion literal.",
    "Se mantiene trazabilidad de fuentes provisionales como notas tecnicas, no autoridad academica.",
    "Se detectan tokens sin resolver y caracteres corruptos en README; se mantiene gate de normalizacion previa."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables a Licenciatura en Derecho, semestre 5, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Sostener tono academico-juridico formal, claro y verificable.",
    "Exigir postura propia sustentada en cada producto.",
    "Marcar como [supuesto] todo dato no visible en consigna o documentos locales.",
    "Mantener trazabilidad de origen editorial en cada consolidacion.",
    "Registrar fuentes heredadas no verificadas como provisionales."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Estructurar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Aplicar cinco ejes editoriales: problema, conceptos, producto solicitado, analisis propio, conclusion transferible.",
    "Alinear estructura al tipo de producto solicitado en planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Verificar instruccion especifica de cada actividad antes de redactar.",
    "Rubricar cada entrega contra los cinco ejes del programa analitico.",
    "Evitar entregas solo descriptivas.",
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Agregar fuentes especificas de actividad al .bib local antes de version final.",
    "No asumir fuentes de semanas distintas sin validacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de fusionar memoria.",
    "Aplicar compresion lossless por union-dedupe sin eliminar reglas utiles previas.",
    "Confirmar que toda afirmacion factual tenga fuente o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregado y consigna local.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Detectar y corregir tokens sin resolver en nombres de archivo antes de compilar."
  ],
  "latex_rules": [
    "Usar plantilla .tex local de la materia como base.",
    "Conservar macros institucionales de portada.",
    "Mantener documentclass compatible con spanish y letterpaper segun plantilla.",
    "No eliminar campos de portada; completar faltantes segun actividad.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir caracteres anomalos en rutas o nombres antes de compilar.",
    "Resolver tokens tipo $(@{...}.Slug) en README y programa analitico antes de referenciar archivos.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion."
  ],
  "bibliography_rules": [
    "Usar etapas-del-proceso-y-estrategia-del-litigio.bib como repositorio local.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "No inventar referencias.",
    "Registrar solo obras consultables y realmente usadas.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente o URL.",
    "Incluir fecha de consulta en fuentes web o institucionales dinamicas.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No citar bibliografia base si no fue usada en el argumento."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "No propagar metadatos hiperlocales de actividad origen.",
    "Mantener advertencia institucional: ciclos con salida no parseable requieren normalizacion manual.",
    "Reforzar en nodos vecinos la regla JSON parseable y union-dedupe sin regresion."
  ],
  "open_questions": [
    "Confirmar si documentauthor es fijo de plantilla o variable por estudiante. [supuesto]",
    "Confirmar estilo de citacion juridica requerido por la asignatura.",
    "Confirmar si coursecode LDE-S5B2 es definitivo institucionalmente. [supuesto]",
    "Confirmar checklist minimo por tipo de producto: reporte, presentacion, visual.",
    "Corregir en README entradas con caracteres corruptos en nombres de archivo. [supuesto]"
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
        "Semestre 5, bloque 2.",
        "Asignatura obligatoria de 8 creditos.",
        "Asignatura: Etapas del proceso y estrategia del litigio."
      ]
    },
    "essence": [
      "Problema juridico claro.",
      "Fundamento conceptual y normativo pertinente.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible.",
      "Persistencia editorial con normalizacion estructurada."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos consistentes y verificables.",
      "Asegurar calidad juridica aplicada en cada entrega.",
      "Mantener memoria editorial reutilizable sin perdida."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Bloques argumentativos visibles.",
      "Afirmacion con evidencia y cita.",
      "Cierre juridico aplicable.",
      "Marcado explicito de [supuesto] cuando falte dato."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis propio -> conclusion juridica.",
      "Afirmacion -> evidencia verificable -> interpretacion -> implicacion practica.",
      "Objetivo puntual -> desarrollo por ejes -> cierre transferible."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Cinco ejes editoriales",
        "JSON parseable",
        "Normalizacion estructurada",
        "Union-dedupe sin regresion",
        "Conclusion juridica transferible",
        "Trazabilidad de fuentes provisionales"
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
          "justification": "Preserva reglas utiles sin recorte."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Estructura de entrega",
          "kind": "develops",
          "justification": "Guian construccion de reportes y presentaciones."
        },
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica con citas verificables",
          "kind": "supports",
          "justification": "La pauta institucional exige verificabilidad."
        },
        {
          "source": "Trazabilidad de fuentes provisionales",
          "target": "Rigor academico",
          "kind": "supports",
          "justification": "Separa notas tecnicas de autoridad academica."
        }
      ],
      "evidence": [
        "README local: ubicacion curricular y pauta editorial.",
        "Programa analitico local: proposito y cinco ejes.",
        "Bib local: claves institucionales existentes.",
        "Plantilla tex local: macros y coursecode visibles.",
        "Historial de salidas no parseables: gate de normalizacion obligatorio."
      ]
    },
    "reinforcement_log": [
      "Ciclo 21: deduplicacion completa de reglas repetidas.",
      "Ciclo 21: refuerzo de transferencia transversal por abstracciones estables.",
      "Ciclo 21: preservacion de gates criticos de JSON, evidencia y no regresion.",
      "Ciclo 21: mantenimiento de vacios locales en open_questions sin inferencias no verificadas."
    ]
  }
}