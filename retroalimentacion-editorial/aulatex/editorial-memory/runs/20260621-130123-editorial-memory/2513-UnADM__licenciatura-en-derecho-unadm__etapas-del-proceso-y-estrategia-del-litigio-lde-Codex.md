{
  "summary": [
    "Consolidar memoria transversal minima para materia destino con identidad UnADM.",
    "Preservar compresion lossless por union-dedupe sin regresion.",
    "Transferir solo abstracciones estables desde actividad origen.",
    "Mantener validacion JSON parseable previa a propagacion recursiva.",
    "Reforzar cinco ejes editoriales comunes: problema, conceptos, producto, analisis, conclusion juridica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear la materia a Licenciatura en Derecho, semestre 5, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Conservar trazabilidad de origen editorial en cada consolidacion.",
    "Marcar como [supuesto] todo dato no visible en consigna o documentos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales y no como autoridad academica."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar desarrollo en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato solicitado en planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Aplicar siempre los cinco ejes editoriales del programa analitico."
  ],
  "activity_rules": [
    "Verificar instruccion especifica de cada actividad antes de redactar.",
    "Rubricar cada entrega contra los cinco ejes editoriales.",
    "Exigir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Agregar fuentes especificas de actividad al .bib local antes de version final.",
    "No asumir fuentes de semanas distintas sin confirmacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la memoria no es JSON parseable.",
    "Revisar estructura minima completa antes de fusionar.",
    "Comprobar que cada afirmacion factual tenga fuente o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar union-dedupe sin eliminar reglas utiles previas.",
    "Normalizar manualmente cualquier herencia no estructurada antes de reutilizar."
  ],
  "latex_rules": [
    "Usar plantilla .tex local de la materia como base.",
    "Conservar macros institucionales de portada y curso.",
    "Mantener compatibilidad con espanol y letterpaper definidos en plantilla.",
    "No eliminar campos de portada; completar segun actividad.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo con caracteres corruptos antes de compilar.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Usar etapas-del-proceso-y-estrategia-del-litigio.bib como repositorio local.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "No inventar referencias; registrar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Incluir fecha de consulta en fuentes web o institucionales dinamicas.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar lateral y recursivo solo reglas generales estables.",
    "No propagar redaccion literal ni metadatos especificos de actividad origen.",
    "Priorizar en nodos vecinos: identidad, estructura reusable, quality gates y grafo conceptual.",
    "Mantener advertencia de herencias no parseables de ciclos tempranos.",
    "Si un nodo destino esta vacio, crear cerebro editorial minimo con vacios abiertos."
  ],
  "open_questions": [
    "Confirmar si documentauthor de plantilla es fijo o variable por estudiante. [supuesto]",
    "Confirmar estilo de citacion juridica requerido por la asignatura.",
    "Confirmar si coursecode LDE-S5B2 es definitivo institucionalmente. [supuesto]",
    "Confirmar checklist minimo por tipo de producto: reporte, presentacion y visual.",
    "Confirmar correccion final de rutas con caracteres corruptos en README."
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
      "Problema juridico o social claro.",
      "Fundamento conceptual, normativo o doctrinal pertinente.",
      "Producto alineado a planeacion.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos solidos y verificables.",
      "Asegurar coherencia entre consigna, argumentacion y evidencia.",
      "Sostener identidad UnADM en todo entregable."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Bloques argumentativos visibles.",
      "Citas trazables.",
      "Cierre juridico aplicable.",
      "Uso explicito de [supuesto] cuando falte dato verificable."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis propio -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> implicacion practica.",
      "Objetivo puntual -> desarrollo seccionado -> verificacion contra rubrica."
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
          "source": "Identidad UnADM",
          "target": "Cinco ejes editoriales",
          "kind": "supports",
          "justification": "La identidad institucional se operacionaliza con estructura editorial estable."
        },
        {
          "source": "JSON parseable",
          "target": "Normalizacion estructurada",
          "kind": "depends_on",
          "justification": "Sin formato parseable no hay fusion confiable."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Union-dedupe sin regresion",
          "kind": "supports",
          "justification": "La deduplicacion lossless requiere estructura consistente."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion surge del recorrido completo problema-conceptos-analisis."
        }
      ],
      "evidence": [
        "README de materia: identidad y ubicacion curricular.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "Bib local: fuentes institucionales base verificables.",
        "Plantilla tex local: macros institucionales y estructura de portada."
      ]
    },
    "reinforcement_log": [
      "Ciclo 13: se mantiene nucleo estable y se deduplica sin perdida.",
      "Ciclo 13: se transfiere solo abstraccion transversal desde actividad no equivalente.",
      "Ciclo 13: se refuerzan gates de JSON parseable, supuestos y no invencion de fuentes.",
      "Ciclo 13: se preserva advertencia sobre tokens Slug sin resolver y rutas corruptas."
    ]
  }
}