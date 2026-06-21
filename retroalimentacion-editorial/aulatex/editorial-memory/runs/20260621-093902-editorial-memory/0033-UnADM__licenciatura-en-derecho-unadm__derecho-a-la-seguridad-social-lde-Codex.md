{
  "summary": [
    "Se consolida sincronizacion transversal entre nodos no equivalentes con enfoque conservador.",
    "Se preservan reglas validas del destino y se agregan abstracciones estables del origen.",
    "Se refuerza patron comun: problema, conceptos o norma, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene control estricto de JSON parseable y normalizacion previa a propagacion.",
    "Se evita transferencia de contenido tematico literal de Filosofia del Derecho hacia Seguridad Social."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Conservar trazabilidad de reglas heredadas provisionales con etiqueta [supuesto].",
    "No sobrescribir reglas validas previas; aplicar union-dedupe sin regresion."
  ],
  "structure_rules": [
    "Tomar README y programa analitico como canon estructural local.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Organizar en secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por la planeacion semanal.",
    "Mantener consistencia entre reporte, presentacion y evidencias de apoyo."
  ],
  "activity_rules": [
    "Vincular cada actividad con el campo de seguridad social cuando corresponda.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir hechos, conceptos, normas y opinion propia.",
    "Evitar entregas solo descriptivas; incluir postura argumentada del estudiante.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar manualmente cualquier salida no estructurada antes de reutilizar.",
    "Validar estructura minima completa antes de propagacion recursiva.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Verificar compresion lossless por union-dedupe, no por recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener metadatos institucionales y de curso consistentes en todos los .tex.",
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Compilar sin errores criticos, sin referencias rotas y con rutas validas.",
    "Resolver marcadores o tokens sin expandir en nombres de archivo antes de compilar.",
    "No introducir comandos no estandar sin justificacion editorial."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central local.",
    "Priorizar fuentes institucionales UnADM y normativas juridicas vigentes verificables.",
    "No inventar referencias; registrar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar lateral y hacia arriba solo reglas generales ya validadas.",
    "Transferir entre materias solo abstracciones editoriales estables, no contenido disciplinar literal.",
    "Mantener alertas historicas de no parseable de ciclo 1 como riesgo operativo.",
    "Aplicar estrategia progresiva: primero identidad y quality gates, luego estructura y estilo.",
    "Aplicar estrategia conservadora: preservar reglas locales del destino como prioridad."
  ],
  "open_questions": [
    "Confirmar norma formal de citacion exigida en la materia (APA, ISO, institucional o juridica mexicana) [supuesto].",
    "Confirmar si el codigo local LDE-S2B1 es oficial en todos los entregables [supuesto].",
    "Confirmar si todas las actividades iniciales requieren reporte y presentacion o solo uno de los dos formatos.",
    "Confirmar dato oficial de figura docente para plantilla cuando exista."
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
      "Evidencia trazable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar consignas en productos juridicos verificables y evaluables.",
      "Conservar memoria editorial persistente sin perdida de reglas utiles.",
      "Asegurar coherencia institucional, tecnica y argumentativa entre entregables."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto] cuando falte evidencia local.",
      "Separacion visible entre marco, analisis y cierre.",
      "Cierre con implicacion profesional."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo y doctrinal.",
      "Contrastar evidencia relevante.",
      "Fijar postura propia sustentada.",
      "Concluir con aplicabilidad juridica practica."
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
          "justification": "Sin delimitacion del problema no hay analisis juridico consistente."
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
          "justification": "La postura del estudiante debe sostenerse con fuentes trazables."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "La consolidacion automatizable requiere estructura valida."
        }
      ],
      "evidence": [
        "README local define estructura canonica y artefactos base.",
        "Programa analitico local define proposito y ejes de trabajo.",
        "Archivo .bib local confirma base institucional y normativa verificable.",
        "Memorias previas registran riesgo historico por salidas no parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 33: se deduplican reglas repetidas sin eliminar contenido util.",
      "Ciclo 33: se incorporan solo abstracciones estables del origen transversal.",
      "Ciclo 33: se refuerzan quality gates de parseo JSON y trazabilidad de supuestos.",
      "Ciclo 33: se preserva prioridad del contexto local de Seguridad Social."
    ]
  }
}