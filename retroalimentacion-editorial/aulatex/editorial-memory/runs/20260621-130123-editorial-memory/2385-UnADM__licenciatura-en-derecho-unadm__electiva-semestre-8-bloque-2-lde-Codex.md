{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre actividad y materia no equivalente.",
    "Se preservan reglas estables de identidad UnADM, normalizacion estructurada y control de supuestos.",
    "Se refuerzan ejes editoriales reutilizables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene bloqueo de propagacion para salidas no JSON parseable.",
    "Se integra riesgo operativo transversal: corregir placeholders y nombres de archivo truncados antes de compilar o propagar.",
    "Se evita transferir contenido tematico especifico de Filosofia del Derecho al nodo electivo sin validacion local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 8, bloque 2, tipo Electiva.",
    "Usar carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no confirmado en consigna o documentos locales.",
    "Mantener autor y matricula confirmados en front matter: Martin Jonathan de la Cruz, ES2611202040.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion manual local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto final con la planeacion semanal y la consigna vigente.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener consistencia entre README, programa analitico, .tex y .bib."
  ],
  "activity_rules": [
    "Traducir cada consigna semanal a producto concreto solicitado.",
    "Incluir postura argumentada del estudiante, no solo resumen descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Vincular conceptos, normas o doctrina con el problema juridico tratado.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No trasladar contenido especifico de otra materia sin fuente verificable."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar y normalizar respuestas no estructuradas heredadas antes de reutilizarlas.",
    "Confirmar ausencia de placeholders visibles o tokens sin expandir en README, programa, .tex y .bib."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Conservar plantilla base de la materia y metadatos institucionales.",
    "Actualizar titulo, subtitulo y numero real de actividad antes de compilar.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en nombres de archivo.",
    "Corregir nombres truncados en listados de estructura (ej. eporte, eferencias).",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas por actividad en electiva-semestre-8-bloque-2.bib.",
    "Priorizar fuentes institucionales UnADM cuando corresponda.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Mantener trazabilidad entre claves citadas y entradas BibTeX."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas transversales estables ya validadas.",
    "Aplicar compresion lossless por union-dedupe sin eliminar reglas utiles previas.",
    "Evitar regresiones: conservar gates institucionales aunque cambie la materia.",
    "No propagar detalle tematico de Filosofia del Derecho a la electiva sin confirmacion local.",
    "Mantener etiqueta de herencia provisional para fuentes no verificadas.",
    "Usar normalizacion manual para artefactos de ciclos con salida no estructurada."
  ],
  "open_questions": [
    "[supuesto] Confirmar creditos oficiales de la materia electiva para completar metadatos.",
    "[supuesto] Confirmar nombre oficial de figura docente en portada.",
    "[supuesto] Confirmar si year=2026 en unadmSitioWeb es dato definitivo o temporal.",
    "[supuesto] Confirmar politica local de fecha de consulta para @misc institucional.",
    "[supuesto] Confirmar si existe nombre oficial alterno para la electiva."
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
        "Semestre 8, bloque 2, tipo Electiva.",
        "[supuesto] Creditos por confirmar."
      ]
    },
    "essence": [
      "Problema juridico claro.",
      "Marco conceptual y normativo pertinente.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables juridicos claros, sustentados y utiles para practica profesional."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones explicitas.",
      "Postura propia respaldada.",
      "Cierre aplicable.",
      "Marcado explicito de [supuesto]."
    ],
    "argumentative_patterns": [
      "Problema -> objetivo -> marco -> argumento propio -> conclusion.",
      "Afirmacion juridica -> evidencia -> interpretacion -> implicacion practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Control de supuestos",
        "Integridad academica",
        "Trazabilidad cita-texto-bib",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Consistencia documental README-programa-tex-bib",
        "Correccion de placeholders"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva segura",
          "kind": "supports",
          "justification": "Reduce herencia de errores de formato y salidas no parseables."
        },
        {
          "source": "Integridad academica",
          "target": "Trazabilidad cita-texto-bib",
          "kind": "depends_on",
          "justification": "La verificabilidad requiere correspondencia explicita entre afirmaciones y fuentes."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion aplicable surge del razonamiento del estudiante."
        },
        {
          "source": "Correccion de placeholders",
          "target": "Consistencia documental README-programa-tex-bib",
          "kind": "supports",
          "justification": "Evita rupturas operativas en rutas, nombres y compilacion."
        }
      ],
      "evidence": [
        "README local de la materia electiva.",
        "Programa analitico local con ejes de trabajo.",
        "Archivo electiva-semestre-8-bloque-2.bib con base institucional.",
        "Regla heredada y vigente: bloquear salida no JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 3: deduplicacion completa de reglas repetidas.",
      "Ciclo 3: preservadas reglas utiles previas sin recorte funcional.",
      "Ciclo 3: reforzado gate de JSON parseable como requisito de propagacion.",
      "Ciclo 3: reforzada separacion entre abstracciones transversales y contenido tematico local.",
      "Ciclo 3: incorporada correccion de tokens Slug/placeholders como control transversal obligatorio."
    ]
  }
}