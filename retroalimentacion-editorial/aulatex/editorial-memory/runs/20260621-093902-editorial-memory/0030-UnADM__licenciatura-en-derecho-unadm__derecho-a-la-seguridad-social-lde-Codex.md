{
  "summary": [
    "Se sincronizan reglas transversales estables desde actividad origen hacia materia destino sin mezclar contenido tematico.",
    "Se preserva identidad UnADM y enfoque juridico verificable del destino.",
    "Se refuerza patron editorial comun: problema, conceptos o norma, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene compresion lossless por union-dedupe y sin regresion.",
    "Se conserva gate critico: bloquear propagacion cuando no haya JSON parseable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No sobrescribir reglas utiles previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README y programa analitico del destino como canon estructural.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Separar desarrollo en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato al producto solicitado por la planeacion semanal.",
    "Mantener consistencia entre reporte, presentacion y bibliografia local."
  ],
  "activity_rules": [
    "Delimitar problema y pregunta guia al inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir hechos, normas, doctrina y postura propia.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre objetivo, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de propagar recursivamente.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Verificar que la compresion aplicada sea union-dedupe sin recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificacion y acentos correctos en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion tecnica.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Normalizar rutas y nombres de archivo antes de compilar.",
    "Resolver tokens o marcadores sin expandir en README y programa analitico antes de usarlos como canon."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central.",
    "Priorizar fuentes institucionales UnADM y normativas juridicas vigentes verificables.",
    "No inventar referencias; registrar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Verificar que cada cita del .tex tenga su entrada BibTeX correspondiente."
  ],
  "propagation_hints": [
    "Propagar a nodos laterales solo abstracciones editoriales estables.",
    "No transferir redaccion literal ni contenido tematico propio de Filosofia del Derecho.",
    "Mantener reglas locales del destino como prioridad en conflictos.",
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Reforzar gates de calidad e identidad institucional en cada salto transversal.",
    "Conservar alerta historica de ciclos con salida no parseable para control preventivo."
  ],
  "open_questions": [
    "[supuesto] Confirmar norma de citacion exigida por la materia: APA, ISO o institucional.",
    "[supuesto] Confirmar si LDE-S2B1 es codigo oficial vigente o solo etiqueta interna.",
    "Confirmar rubricas de evaluacion por actividad para calibrar profundidad argumentativa.",
    "Confirmar si todas las plantillas de Actividad-1 ya existen y son canonicas en README.",
    "Confirmar vigencia anual de referencias legales del .bib antes de entrega final."
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
      "Resolver consignas en productos juridicos verificables.",
      "Unir problema, fundamento, evidencia, analisis propio y cierre profesional.",
      "Preservar memoria editorial sin perdida por deduplicacion."
    ],
    "reason_for_being": [
      "Garantizar consistencia editorial transversal entre actividades y materias no equivalentes.",
      "Elevar calidad argumentativa con trazabilidad de supuestos y fuentes.",
      "Asegurar reutilizacion segura mediante estructura parseable."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion visible entre marco, analisis y conclusion.",
      "Cierre con utilidad juridica practica."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo y doctrinal.",
      "Contrastar evidencia relevante.",
      "Fijar postura propia sustentada.",
      "Concluir con implicacion juridica transferible."
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
        "Compresion union-dedupe",
        "Seguridad social como dominio local"
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
          "justification": "Sin pregunta delimitada no hay analisis juridico evaluable."
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
          "justification": "La postura academica debe sostenerse en fuentes trazables."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "La consolidacion lossless requiere estructura valida."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Seguridad social como dominio local",
          "kind": "develops",
          "justification": "La identidad comun permite transferencia transversal sin perder contexto local."
        }
      ],
      "evidence": [
        "README del destino define estructura canonica y artefactos base.",
        "Programa analitico del destino fija proposito y ejes de trabajo.",
        "Archivo .bib local contiene base institucional y normativa vigente.",
        "Memoria previa confirma gate de JSON parseable y normalizacion manual en ciclos con falla."
      ]
    },
    "reinforcement_log": [
      "Ciclo 30: se transfieren solo abstracciones editoriales estables desde nodo no equivalente.",
      "Ciclo 30: se evita migrar contenido tematico especifico de Filosofia del Derecho.",
      "Ciclo 30: se refuerzan identidad, estructura reusable, gates de calidad y grafo conceptual.",
      "Ciclo 30: se mantiene estrategia conservadora de union-dedupe sin regresion."
    ]
  }
}