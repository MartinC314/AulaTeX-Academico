{
  "summary": [
    "Se consolida sincronizacion transversal entre nodos no equivalentes con reglas estables reutilizables.",
    "Se preserva identidad UnADM y contexto curricular del destino sin mezclar contenido tematico de Filosofia del Derecho.",
    "Se refuerza patron comun de entrega juridica: problema, fundamento, evidencia, analisis propio y conclusion transferible.",
    "Se mantiene compresion lossless por union-dedupe y politica de no regresion.",
    "Se conserva alerta institucional de salidas no parseables heredadas y normalizacion manual obligatoria cuando aplique."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y formato.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "No sobrescribir reglas validas previas; solo unir y deduplicar.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Tomar README y programa analitico del destino como canon estructural.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por la planeacion semanal.",
    "Mantener consistencia editorial entre reporte, presentacion y bibliografia local."
  ],
  "activity_rules": [
    "Delimitar problema y pregunta guia desde el inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir hechos, normas, doctrina y postura propia.",
    "Evitar entregas solo descriptivas; incluir argumentacion propia.",
    "Verificar coherencia entre objetivo, desarrollo y conclusion.",
    "Cerrar con conclusion juridica aplicable a practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar manualmente respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de propagacion recursiva.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Verificar que la compresion aplicada sea union-dedupe sin recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener metadatos institucionales y de curso consistentes en todo .tex.",
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Normalizar rutas y nombres de archivo con marcadores corruptos antes de compilar."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central.",
    "Priorizar fuentes institucionales UnADM y normatividad vigente verificable.",
    "Agregar solo referencias consultables con metadatos minimos completos.",
    "No inventar fuentes; marcar faltantes como pendientes o [supuesto].",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Verificar que cada clave citada exista en el .bib local."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo abstracciones editoriales estables.",
    "No transferir redaccion literal ni contenido tematico especifico de Filosofia del Derecho.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual comun.",
    "Conservar reglas locales del destino cuando exista conflicto semantico.",
    "Mantener bandera de riesgo para ciclos con antecedente no parseable.",
    "Aplicar estrategia progresiva y conservadora: agregar mejoras verificables sin eliminar reglas utiles."
  ],
  "open_questions": [
    "Confirmar si LDE-S2B1 es codigo oficial o interno [supuesto].",
    "Confirmar norma de citacion requerida por la materia (APA, ISO o institucional) [supuesto].",
    "Confirmar rubrica de evaluacion por actividad para ajustar profundidad argumentativa.",
    "Confirmar si todas plantillas de Actividad-1 del README ya existen en repositorio local.",
    "Confirmar vigencia de cualquier fuente provisional heredada desde nodos no juridicos [supuesto]."
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
      "Problema juridico delimitado.",
      "Fundamento normativo verificable.",
      "Evidencia pertinente y trazable.",
      "Analisis propio no descriptivo.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir consignas en productos juridicos verificables con utilidad profesional.",
      "Sostener coherencia editorial entre identidad institucional, estructura y evidencia."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion visible entre marco, analisis y cierre.",
      "Sincronizacion entre TEX, README, programa analitico y .bib."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo.",
      "Exponer marco normativo y conceptual.",
      "Contrastar evidencia.",
      "Fijar postura sustentada.",
      "Concluir con implicacion practica."
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
          "justification": "El analisis requiere una pregunta juridica delimitada."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion necesita fundamento legal verificable."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "La consolidacion segura requiere estructura valida."
        },
        {
          "source": "Identidad UnADM",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La identidad institucional orienta rigor, formato y utilidad profesional."
        }
      ],
      "evidence": [
        "README de la materia destino como canon de estructura.",
        "Programa analitico destino con ejes y proposito verificable.",
        "Archivo derecho-a-la-seguridad-social.bib con base normativa e institucional.",
        "Regla persistente: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 52: se transfirieron solo abstracciones estables desde actividad de Filosofia.",
      "Ciclo 52: se reforzo gate de JSON parseable y normalizacion manual previa a propagacion.",
      "Ciclo 52: se mantuvo no regresion y deduplicacion lossless.",
      "Ciclo 52: se preservo especificidad local de Seguridad Social sin contaminacion tematica."
    ]
  }
}