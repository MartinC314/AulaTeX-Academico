{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre actividad de origen y materia destino.",
    "Se preservan reglas estables: identidad UnADM, normalizacion estructurada y cierre juridico con criterio propio.",
    "Se transfieren solo abstracciones reutilizables y no redaccion literal de Filosofia del Derecho.",
    "Se refuerza compresion lossless por union-dedupe sin regresion.",
    "Se mantiene control de herencias no verificadas como provisionales.",
    "Se prioriza grafo conceptual comun: problema, conceptos, evidencia, analisis propio y conclusion juridica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar datos curriculares verificados del destino: Licenciatura en Derecho, semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Conservar enfoque disciplinar en contratos y obligaciones.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como [supuesto] todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Usar LDE-S4B1 cuando la plantilla lo requiera."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al tipo solicitado en la planeacion semanal.",
    "Mantener trazabilidad entre objetivo, evidencia, argumento y conclusion.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Distinguir bibliografia base de fuentes especificas por actividad."
  ],
  "activity_rules": [
    "Adaptar cada entrega al producto requerido por la actividad.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y cierre.",
    "Evitar traslado literal desde otras materias sin adecuacion contractual.",
    "No asumir fuentes de semanas o materias distintas sin verificacion local.",
    "Marcar [supuesto] cuando falte instruccion especifica."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar toda herencia no estructurada antes de reutilizar.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar compatibilidad disciplinar antes de propagacion lateral.",
    "No degradar reglas utiles previas durante fusion por deduplicacion."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y metadatos institucionales completos.",
    "Usar espanol academico con acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir caracteres anomalos en rutas o nombres antes de compilar.",
    "Actualizar documentsubtitle por numero real de actividad."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM, normas y doctrina verificables.",
    "Registrar fuentes especificas por actividad en derechos-de-los-contratos-y-obligaciones.bib.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/editorial o URL.",
    "Mantener unadmSitioWeb y unadmMallaDerecho2024 como base institucional.",
    "Declarar [supuesto] si una referencia requerida no esta disponible localmente.",
    "Separar bibliografia base de bibliografia especifica de actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas transversales estables.",
    "Excluir detalles tematicos propios de Filosofia del Derecho en saltos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual comun.",
    "Aplicar union-dedupe sin eliminar reglas utiles previas.",
    "Mantener etiqueta provisional en herencias de Codex o GPT-Pro no verificadas.",
    "Ejecutar normalizacion manual si se reutiliza memoria de ciclos previos con ruido."
  ],
  "open_questions": [
    "[supuesto] Falta consigna textual de actividades concretas del destino; confirmar producto exacto por semana.",
    "Confirmar rubrica de evaluacion por actividad para calibrar profundidad argumentativa.",
    "Confirmar guia formal de citacion juridica obligatoria en la materia.",
    "Confirmar si presentacion y reporte comparten metadatos obligatorios exactos.",
    "Confirmar uso esperado de legislacion federal, local o mixta segun actividad."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 4, bloque 1, obligatoria, 8 creditos.",
        "Asignatura centrada en contratos y obligaciones."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y utiles para practica juridica.",
      "Sostener coherencia institucional, argumentativa y bibliografica en toda entrega."
    ],
    "style_markers": [
      "Frases claras y verificables.",
      "Supuestos explicitados cuando falte contexto.",
      "Cierre con utilidad profesional juridica.",
      "Sin traslado literal entre materias no equivalentes."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Objetivo puntual.",
      "Marco conceptual y normativo.",
      "Analisis propio sustentado.",
      "Conclusion juridica aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema juridico",
        "Marco normativo y doctrinal",
        "Evidencia verificable",
        "Analisis argumentativo propio",
        "Conclusion transferible",
        "Contratos",
        "Obligaciones",
        "Normalizacion estructurada",
        "JSON parseable"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica con citas verificables",
          "kind": "supports",
          "justification": "La pauta institucional exige verificabilidad y formato consistente."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis argumentativo propio",
          "kind": "develops",
          "justification": "El analisis parte de una pregunta o conflicto definido."
        },
        {
          "source": "Marco normativo y doctrinal",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica debe derivar de fundamento verificable."
        },
        {
          "source": "Contratos",
          "target": "Obligaciones",
          "kind": "depends_on",
          "justification": "La materia articula ambas categorias como nucleo disciplinar."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "JSON parseable",
          "kind": "depends_on",
          "justification": "La propagacion segura requiere formato valido y verificable."
        }
      ],
      "evidence": [
        "README de materia: identidad UnADM y carpeta canonica.",
        "Programa analitico: ejes problema-conceptos-evidencia-analisis-conclusion.",
        "Bib local: unadmSitioWeb y unadmMallaDerecho2024 como base verificable.",
        "Regla persistente: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: deduplicacion aplicada sin perdida semantica.",
      "Ciclo 2: se preservan gates criticos de parseo JSON y normalizacion.",
      "Ciclo 2: se refuerza separacion entre reglas transversales y contenido disciplinar especifico.",
      "Ciclo 2: se mantiene control de supuestos y herencias provisionales.",
      "Ciclo 2: se consolida patron argumentativo reusable en actividades hijas."
    ]
  }
}