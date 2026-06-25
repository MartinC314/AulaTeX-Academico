{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia conservadora y sin regresion.",
    "Se preserva identidad UnADM y enfoque juridico del destino.",
    "Se refuerza patron estable: problema, fundamento, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene compresion lossless por union-dedupe.",
    "Se conserva alerta por salidas no parseables en ciclos previos y normalizacion manual obligatoria."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No sobrescribir reglas validas previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README y programa analitico del destino como canon estructural.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Organizar desarrollo en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato y alcance al producto solicitado en planeacion semanal.",
    "Mantener consistencia editorial entre reporte, presentacion y actividad."
  ],
  "activity_rules": [
    "Delimitar problema juridico desde el inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar manualmente respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de propagacion recursiva.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Verificar que cada cita en texto exista en el .bib local.",
    "Confirmar compresion por union-dedupe sin recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificacion y acentos correctos en espanol en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, sin referencias rotas y con rutas validas.",
    "Normalizar nombres de archivo con marcadores corruptos antes de usarlos.",
    "Mantener estructura minima: portada, desarrollo por ejes, conclusion y referencias."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente central local.",
    "Priorizar fuentes institucionales UnADM y normas juridicas verificables.",
    "Agregar solo referencias realmente consultables y pertinentes a la actividad.",
    "No inventar fuentes.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar lateral y recursivamente solo reglas editoriales estables y abstractas.",
    "No transferir contenido tematico especifico de Filosofia del Derecho al destino.",
    "Propagar gates de calidad, identidad y estructura reusable como nucleo transversal.",
    "Mantener bandera de riesgo por antecedentes de no parseable en ciclo 1.",
    "Si falta contexto local en subnodos, crear cerebro minimo y abrir preguntas."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida en la materia (APA, ISO o institucional) [supuesto].",
    "Confirmar si codigo local LDE-S2B1 es oficial en todos los entregables [supuesto].",
    "Confirmar datos faltantes de figura docente para portada [supuesto].",
    "Verificar vigencia de cualquier fuente provisional heredada de nodos no juridicos [supuesto]."
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
        "Normalizacion estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho a la Seguridad Social.",
        "Semestre 2, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Resolver consignas con trazabilidad juridica verificable.",
      "Sostener cada entrega en problema, fundamento, evidencia, analisis y conclusion.",
      "Preservar memoria editorial sin perdida por deduplicacion."
    ],
    "reason_for_being": [
      "Convertir planeaciones en productos academicos solidos y evaluables.",
      "Garantizar coherencia institucional y calidad tecnica en LaTeX.",
      "Habilitar propagacion segura entre nodos no equivalentes."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Separacion clara entre marco, analisis y cierre.",
      "Marcado explicito de [supuesto] cuando falte verificacion."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo.",
      "Exponer marco normativo y doctrinal pertinente.",
      "Contrastar evidencia verificable.",
      "Fijar postura propia sustentada.",
      "Concluir con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema juridico",
        "Marco normativo",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "JSON parseable",
        "Compresion union-dedupe"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024",
        "cpeum2026",
        "lss2026",
        "lissste2026"
      ],
      "relations": [
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin problema delimitado no hay argumentacion juridica util."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida requiere fundamento legal verificable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura propia debe sostenerse con fuentes trazables."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "La persistencia lossless requiere estructura valida."
        }
      ],
      "evidence": [
        "README del destino define estructura canonica y artefactos base.",
        "Programa analitico del destino fija proposito y ejes de trabajo.",
        "Archivo .bib local confirma base institucional y normativa verificable.",
        "Memoria previa registra alertas de no parseable y normalizacion manual obligatoria."
      ]
    },
    "reinforcement_log": [
      "Ciclo 9: se preservan reglas utiles previas sin eliminacion.",
      "Ciclo 9: se deduplican variantes repetidas de identidad, estructura y calidad.",
      "Ciclo 9: se transfiere solo abstraccion estable desde nodo transversal.",
      "Ciclo 9: se evita mezclar contenido tematico especifico de Filosofia en Seguridad Social."
    ]
  }
}