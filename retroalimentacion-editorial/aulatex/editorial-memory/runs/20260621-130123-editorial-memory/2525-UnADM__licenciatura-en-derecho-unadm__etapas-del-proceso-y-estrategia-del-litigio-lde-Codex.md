{
  "summary": [
    "Se consolida sincronizacion transversal con reglas estables y deduplicadas.",
    "Se preserva identidad UnADM y enfoque juridico aplicado del nodo materia.",
    "Se refuerza transferencia por abstracciones editoriales, no por redaccion literal.",
    "Se mantiene compresion lossless por union-dedupe sin regresion.",
    "Se conserva bloqueo de propagacion ante salidas no JSON parseable.",
    "Se integra control de supuestos para datos no visibles en consigna o fuentes locales."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Conservar trazabilidad del origen editorial en cada consolidacion.",
    "Usar tono academico-juridico formal, claro y argumentativo.",
    "Exigir postura propia sustentada en evidencia verificable.",
    "Marcar como [supuesto] todo dato no visible en consigna o documento local.",
    "Tratar fuentes heredadas no verificadas como provisionales y no autoritativas."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear estructura al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Aplicar cinco ejes: problema, conceptos, producto solicitado, analisis propio, conclusion."
  ],
  "activity_rules": [
    "Verificar instruccion especifica de actividad antes de redactar.",
    "Rubricar cada entrega contra los cinco ejes del programa analitico.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Agregar fuentes especificas de actividad al .bib local antes de version final."
  ],
  "quality_gates": [
    "Bloquear propagacion si la memoria no es JSON parseable.",
    "Validar estructura minima completa antes de fusionar aguas abajo.",
    "Comprobar union-dedupe sin eliminar reglas utiles previas.",
    "Confirmar que toda afirmacion factual tenga fuente o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar y normalizar salidas no estructuradas antes de reutilizar."
  ],
  "latex_rules": [
    "Usar plantilla .tex local de la materia como base.",
    "Conservar macros institucionales de portada y curso.",
    "Mantener compatibilidad con espanol y letterpaper definidos.",
    "No eliminar campos de portada; completar faltantes segun actividad.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir nombres de archivo con caracteres corruptos antes de compilar. [supuesto]",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico."
  ],
  "bibliography_rules": [
    "Usar etapas-del-proceso-y-estrategia-del-litigio.bib como repositorio local.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "No inventar referencias; registrar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Incluir fecha de consulta en fuentes web o institucionales dinamicas.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No citar bibliografia no usada en el argumento."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales y estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "No propagar metadatos locales sensibles de esta materia a otras materias.",
    "Mantener advertencia historica: ciclos con salida no parseable requieren normalizacion manual.",
    "Reforzar en nodos vecinos la regla de JSON parseable previo a fusion."
  ],
  "open_questions": [
    "Confirmar si documentauthor debe ser fijo de plantilla o variable por estudiante. [supuesto]",
    "Confirmar estilo de citacion juridica exigido por docente (APA, Chicago, ISO 690 u otro).",
    "Confirmar si coursecode LDE-S5B2 es definitivo institucionalmente. [supuesto]",
    "Confirmar checklist minimo por tipo de producto: reporte, presentacion y visual.",
    "Confirmar correccion de rutas con caracteres truncados en README. [supuesto]"
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
        "Fuentes provisionales separadas de autoridad academica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 5, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Etapas del proceso y estrategia del litigio."
      ]
    },
    "essence": [
      "Cinco ejes editoriales como columna vertebral de toda entrega.",
      "Estructura argumentativa reusable con cierre juridico aplicable.",
      "Normalizacion estructurada antes de cualquier propagacion.",
      "Compresion lossless por deduplicacion sin recorte de reglas utiles."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos juridicos de calidad verificable.",
      "Asegurar continuidad editorial entre actividades, materia y niveles superiores.",
      "Permitir propagacion transversal segura sin contaminar con literalidad local."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Bloques argumentativos visibles.",
      "Citas trazables.",
      "Postura propia explicita.",
      "Conclusion juridica transferible."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis propio -> conclusion juridica.",
      "Afirmacion -> evidencia -> interpretacion -> implicacion practica.",
      "Objetivo puntual -> desarrollo por ejes -> cierre verificable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Cinco ejes editoriales",
        "JSON parseable",
        "Normalizacion estructurada",
        "Union-dedupe sin regresion",
        "Conclusion juridica transferible",
        "Fuentes verificables",
        "Supuestos marcados"
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
          "justification": "Sin estructura valida no hay consolidacion confiable."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Union-dedupe sin regresion",
          "kind": "supports",
          "justification": "Permite fusionar sin perdida ni contradiccion."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La secuencia editorial conduce al cierre aplicable."
        },
        {
          "source": "Fuentes verificables",
          "target": "Identidad UnADM",
          "kind": "supports",
          "justification": "La integridad academica institucional depende de verificabilidad."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "Bib local: fuentes institucionales minimas verificables.",
        "Plantilla tex local: macros institucionales y coursecode visible.",
        "Historial de ciclos: necesidad de JSON parseable y normalizacion manual en salidas no estructuradas."
      ]
    },
    "reinforcement_log": [
      "Ciclo 16: se deduplican reglas repetidas sin recortar contenido util.",
      "Ciclo 16: se conserva ADN institucional y gates de calidad heredados.",
      "Ciclo 16: se refuerza transferencia transversal por abstracciones estables.",
      "Ciclo 16: se mantienen supuestos explicitos en vacios de contexto local."
    ]
  }
}