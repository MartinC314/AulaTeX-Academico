{
  "summary": [
    "Se sincroniza memoria transversal con reglas estables y sin mezclar contenido tematico de Filosofia del Derecho.",
    "Se conserva identidad UnADM y enfoque juridico de la materia destino.",
    "Se refuerza patron comun: problema, fundamento, evidencia, analisis propio y conclusion juridica transferible.",
    "Se mantiene compresion lossless por union-dedupe y politica de no regresion.",
    "Se mantiene alerta por salidas no parseables heredadas y normalizacion manual obligatoria cuando aparezcan."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local [supuesto].",
    "No sobrescribir reglas validas previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README y programa analitico como canon estructural local.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar desarrollo en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto pedido en planeacion semanal.",
    "Mantener consistencia entre reporte, presentacion y referencias."
  ],
  "activity_rules": [
    "Delimitar problema y pregunta guia al inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Incluir postura argumentada del estudiante; evitar entregas solo descriptivas.",
    "Verificar coherencia entre objetivo, desarrollo y conclusion.",
    "Cerrar con conclusion juridica aplicable a practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizar aguas abajo.",
    "Validar estructura minima completa antes de propagacion recursiva.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que la compresion aplicada sea union-dedupe sin recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener compatibilidad de compilacion sin errores criticos ni referencias rotas.",
    "Usar codificacion y acentos correctos en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Normalizar nombres de archivos y resolver tokens no expandidos antes de compilar.",
    "Verificar rutas canonicas contra README antes de referenciar."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central local.",
    "Priorizar fuentes institucionales UnADM y normativas juridicas verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Agregar solo fuentes especificas de actividad con metadatos minimos completos.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener claves BibTeX estables para evitar rupturas."
  ],
  "propagation_hints": [
    "Propagar lateral y arriba solo reglas generales ya validadas.",
    "No transferir redaccion literal ni contenido tematico propio de otra materia.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Aplicar normalizacion manual en nodos con historial de salida no parseable.",
    "Mantener trazabilidad de reglas provisionales con etiqueta [supuesto].",
    "Preservar reglas locales del destino como prioridad contextual."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida en la materia (APA, ISO, institucional o juridica mexicana) [supuesto].",
    "Confirmar si el codigo local LDE-S2B1 es oficial en todas las plantillas [supuesto].",
    "Confirmar si la fuente provisional heredada desde ingenieria sigue vigente para este nodo [supuesto].",
    "Confirmar rubrica de evaluacion por actividad para ajustar profundidad argumentativa.",
    "Confirmar si Actividad 1 requiere reporte, presentacion o ambos en esta materia."
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
        "Materia destino: Derecho a la Seguridad Social.",
        "Semestre 2, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Identidad institucional estable.",
      "Problema juridico bien delimitado.",
      "Fundamento normativo verificable.",
      "Evidencia trazable.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir consignas en productos juridicos verificables y utiles para practica profesional.",
      "Asegurar continuidad editorial entre nodos con compresion lossless y sin regresion."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion visible entre marco, analisis y cierre.",
      "Cierre con implicacion profesional concreta."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo.",
      "Exponer marco normativo y doctrinal.",
      "Contrastar evidencia relevante.",
      "Fijar postura propia sustentada.",
      "Concluir con efecto juridico practico."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
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
          "justification": "Sin delimitacion del problema no hay argumentacion focalizada."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida requiere fundamento legal verificable."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "La deduplicacion segura exige estructura valida."
        },
        {
          "source": "Identidad UnADM",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "La integridad institucional exige trazabilidad de fuentes."
        }
      ],
      "evidence": [
        "README de la materia define estructura canonica y archivos oficiales.",
        "Programa analitico define proposito y ejes de trabajo del destino.",
        "Archivo .bib local confirma base normativa e institucional verificable.",
        "Memoria previa registra gate obligatorio de JSON parseable y normalizacion manual."
      ]
    },
    "reinforcement_log": [
      "Ciclo 3: se preservan reglas utiles previas y se eliminan duplicados semanticos.",
      "Ciclo 3: se transfiere solo abstraccion editorial estable desde nodo no equivalente.",
      "Ciclo 3: se refuerzan gates de calidad y grafo conceptual sin importar contenido literal."
    ]
  }
}