{
  "summary": [
    "Se consolida sincronizacion transversal entre nodos no equivalentes con compresion lossless por union-dedupe.",
    "Se preserva ADN UnADM del destino sin mezclar contenido tematico especifico de Filosofia del Derecho.",
    "Se refuerza patron editorial estable: problema, fundamento, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene control estricto de parseo JSON y normalizacion previa a propagacion recursiva.",
    "Se actualiza estructura canonica con artefactos de actividad en README del destino."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y trazabilidad.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica editorial.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No sobrescribir reglas validas previas; solo unir y deduplicar sin regresion."
  ],
  "structure_rules": [
    "Tomar README y programa analitico de la materia como canon estructural local.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Organizar por ejes: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato al producto solicitado en planeacion semanal.",
    "Mantener consistencia entre reporte, presentacion y actividad."
  ],
  "activity_rules": [
    "Delimitar problema juridico y pregunta guia al inicio.",
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Verificar coherencia entre objetivo, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizacion aguas abajo.",
    "Validar estructura minima completa antes de propagacion recursiva.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que la compresion aplicada sea union-dedupe y no recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Compilar sin errores criticos ni referencias faltantes.",
    "Evitar comandos no estandar sin justificacion tecnica.",
    "Corregir nombres/rutas con marcadores corruptos antes de compilar."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central.",
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Agregar solo referencias consultables con metadatos minimos completos.",
    "No inventar fuentes; marcar faltantes como pendientes o [supuesto].",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Verificar que toda cita LaTeX tenga entrada BibTeX existente."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo abstracciones editoriales estables, no redaccion literal.",
    "Propagar recursivo solo tras pasar gates de JSON y estructura.",
    "Transferir reglas generales de identidad, calidad, LaTeX y citas a nodos compatibles.",
    "No transferir contenidos doctrinales especificos de Filosofia al destino de Seguridad Social.",
    "Conservar bandera historica: ciclo 1 requirio normalizacion manual."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida en la materia (APA, ISO o juridica mexicana) [supuesto].",
    "Confirmar vigencia de toda fuente provisional heredada de nodos ajenos a Derecho [supuesto].",
    "Confirmar si cada actividad requiere .bib propio o solo el central de materia.",
    "Confirmar datos faltantes de figura docente en plantillas de actividad [supuesto]."
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
      "Problema juridico delimitado.",
      "Fundamento normativo y doctrinal verificable.",
      "Evidencia pertinente y trazable.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir consignas en productos juridicos verificables y utiles profesionalmente.",
      "Preservar coherencia institucional y tecnica en toda entrega.",
      "Permitir propagacion segura de reglas editoriales entre nodos compatibles."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion clara entre marco, analisis y cierre.",
      "Cierre con implicacion juridica practica."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo.",
      "Exponer marco normativo/doctrinal.",
      "Contrastar evidencia.",
      "Fijar postura propia sustentada.",
      "Concluir con efecto practico juridico."
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
          "justification": "Sin delimitacion del problema no hay argumentacion valida."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion requiere fundamento legal verificable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura propia debe sustentarse en fuentes trazables."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "La consolidacion segura requiere estructura valida."
        }
      ],
      "evidence": [
        "README del destino define estructura canonica y artefactos base.",
        "Programa analitico define proposito y ejes de trabajo de Seguridad Social.",
        ".bib local confirma base institucional y normativa vigente.",
        "Historial previo registra riesgo por salida no parseable y exige normalizacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 36: deduplicacion integral sin perdida semantica.",
      "Ciclo 36: se mantiene alerta de parseo y normalizacion manual historica.",
      "Ciclo 36: se refuerzan patrones argumentativos reutilizables transversales.",
      "Ciclo 36: se preserva separacion entre reglas generales y contenido tematico local."
    ]
  }
}