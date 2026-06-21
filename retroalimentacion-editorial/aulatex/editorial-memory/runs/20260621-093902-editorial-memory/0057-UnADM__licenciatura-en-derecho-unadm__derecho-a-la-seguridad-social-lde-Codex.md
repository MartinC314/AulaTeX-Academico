{
  "summary": [
    "Se consolida sincronizacion transversal entre nodos no equivalentes con transferencia de reglas estables.",
    "Se preserva identidad UnADM y contexto curricular local de Derecho a la Seguridad Social.",
    "Se refuerza patron comun: problema, fundamento normativo, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene compresion lossless por union-dedupe sin recorte ni regresion.",
    "Se conserva alerta institucional por antecedentes de salidas no parseables y normalizacion manual obligatoria."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica editorial.",
    "Conservar trazabilidad de reglas heredadas provisionales con etiqueta [supuesto].",
    "No sobrescribir reglas validas previas; solo unir y deduplicar.",
    "No transferir contenido tematico especifico de Filosofia del Derecho al destino."
  ],
  "structure_rules": [
    "Tomar README y programa analitico del destino como canon estructural local.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Organizar en secciones: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato y alcance al producto solicitado en planeacion semanal.",
    "Mantener consistencia entre reporte, presentacion y bibliografia local."
  ],
  "activity_rules": [
    "Delimitar problema juridico desde el inicio.",
    "Distinguir hechos, conceptos, normas y postura propia.",
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Evitar entregas solo descriptivas.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizar aguas abajo.",
    "Validar estructura minima completa antes de propagacion recursiva.",
    "Confirmar respaldo verificable o marca [supuesto] en cada afirmacion relevante.",
    "Verificar correspondencia entre consigna, desarrollo y conclusion.",
    "Confirmar que compresion aplicada sea union-dedupe y no recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener metadatos institucionales y de curso consistentes en archivos .tex.",
    "Usar estructura minima: portada, desarrollo, conclusion y referencias.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Corregir nombres o rutas corruptas antes de compilar."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central.",
    "No inventar referencias; usar solo fuentes consultables.",
    "Conservar metadatos minimos: autor, titulo, año, fuente o URL.",
    "Verificar que cada cita en texto exista en el .bib local.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Priorizar fuentes institucionales y normativas vigentes aplicables al destino."
  ],
  "propagation_hints": [
    "Propagar a nodos laterales solo reglas generales de identidad, estructura y calidad.",
    "Restringir reglas curriculares especificas al nodo de la misma materia.",
    "Aplicar transferencia transversal por abstracciones editoriales, no por redaccion literal.",
    "Mantener bandera de riesgo por ciclo 1 no parseable hasta cierre de verificacion.",
    "Si un nodo destino esta vacio, crear cerebro minimo con identidad, estructura y gates."
  ],
  "open_questions": [
    "Confirmar si existe norma de citacion obligatoria adicional para la materia [supuesto].",
    "Confirmar si codigo local LDE-S2B1 debe mantenerse en todas las plantillas [supuesto].",
    "Confirmar si la fuente provisional heredada desde ingenieria sigue vigente para Derecho [supuesto].",
    "Validar periodicamente vigencia de enlaces normativos en .bib local."
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
      "Resolver consignas en productos juridicos verificables.",
      "Sostener toda conclusion en problema, norma, evidencia y analisis propio.",
      "Proteger continuidad editorial con compresion lossless y sin regresion."
    ],
    "reason_for_being": [
      "Garantizar coherencia institucional y calidad tecnica en toda entrega LaTeX.",
      "Permitir propagacion segura entre nodos mediante reglas estables y verificables.",
      "Convertir memoria editorial en criterio operativo reutilizable."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiqueta explicita de [supuesto].",
      "Separacion visible entre marco, analisis y cierre.",
      "Cierre con utilidad juridica profesional."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo y doctrinal pertinente.",
      "Contrastar evidencia relevante.",
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
          "justification": "El analisis exige una pregunta delimitada."
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
          "justification": "La postura academica debe ser comprobable."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay consolidacion segura."
        }
      ],
      "evidence": [
        "README del destino define estructura canonica y control editorial.",
        "Programa analitico del destino define proposito y ejes de trabajo.",
        "Archivo .bib local confirma base institucional y normativa vigente.",
        "Memoria heredada exige normalizacion manual ante salidas no parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 57: se transfiere solo abstraccion estable desde actividad de Filosofia.",
      "Ciclo 57: se refuerzan gates JSON, respaldo de afirmaciones y union-dedupe lossless.",
      "Ciclo 57: se evita mezclar contenido tematico de origen con destino.",
      "Ciclo 57: se mantiene ADN institucional UnADM y patron argumentativo comun."
    ]
  }
}