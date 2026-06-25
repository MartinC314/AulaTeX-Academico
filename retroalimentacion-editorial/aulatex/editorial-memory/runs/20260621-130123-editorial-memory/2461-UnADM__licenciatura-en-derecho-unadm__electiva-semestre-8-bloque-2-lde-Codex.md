{
  "summary": [
    "Se sincroniza memoria transversal desde actividad de Filosofia del Derecho hacia materia electiva sin mover contenido tematico especifico.",
    "Se preservan reglas estables: identidad UnADM, ejes editoriales, normalizacion estructurada, control de supuestos y cierre juridico transferible.",
    "Se refuerza compresion lossless por union-dedupe y politica sin regresion.",
    "Se mantiene alerta operativa por placeholders y nombres truncados detectados en README y programa del destino."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, metadatos y formato.",
    "Alinear entregables con Licenciatura en Derecho, semestre 8, bloque 2, tipo Electiva.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como [supuesto] todo dato no visible o no confirmado.",
    "Mantener autor y matricula confirmados en front matter: Martin Jonathan de la Cruz, ES2611202040.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear el producto al tipo solicitado en la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener consistencia entre README, programa analitico, .tex y .bib."
  ],
  "activity_rules": [
    "Traducir cada consigna semanal a producto concreto.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar resumen descriptivo puro.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Vincular conceptos, normas y doctrina con el problema juridico tratado.",
    "No transferir contenido especifico de otra asignatura sin respaldo local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar memoria.",
    "Revisar manualmente herencias de ciclos con salida no estructurada.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de [supuesto].",
    "Validar trazabilidad entre citas en texto y claves del .bib.",
    "Confirmar ausencia de placeholders o tokens sin expandir en README, programa, .tex y .bib.",
    "Verificar correspondencia del producto con la consigna activa."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en español en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion.",
    "Corregir nombres truncados en estructura de archivos (ej. eporte, eferencias).",
    "Resolver tokens tipo $(@{...}.Slug) a nombres literales antes de compilar.",
    "Actualizar titulo, subtitulo y numero real de actividad antes de entrega.",
    "Completar campos pendientes del front matter solo con datos confirmados; si no, marcar [supuesto]."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas por actividad en electiva-semestre-8-bloque-2.bib.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias.",
    "Conservar metadatos minimos: autor, titulo, año y fuente/URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "No asumir reutilizacion automatica de bibliografia de otra materia."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas abstractas y estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferencia de redaccion literal o contenido tematico local del origen.",
    "Mantener etiqueta de herencia provisional cuando falte verificacion local.",
    "Aplicar normalizacion manual en nodos con historial de salida no estructurada."
  ],
  "open_questions": [
    "[supuesto] Confirmar creditos oficiales de la materia destino.",
    "[supuesto] Confirmar nombre de figura docente para front matter.",
    "[supuesto] Confirmar politica institucional para year y fecha de consulta en @misc.",
    "[supuesto] Confirmar si existe nombre oficial alterno de la electiva.",
    "[supuesto] Confirmar consigna y rubrica de la actividad activa antes de especializar reglas."
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
        "Normalizacion estructurada obligatoria antes de propagar.",
        "Control explicito de supuestos."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 8, bloque 2, tipo Electiva.",
        "[supuesto] Creditos por confirmar."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas y doctrina pertinentes.",
      "Producto alineado a planeacion.",
      "Analisis propio con postura.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables juridico-academicos verificables.",
      "Asegurar coherencia entre identidad institucional, evidencia y argumentacion propia."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones explicitas.",
      "Citas trazables.",
      "Marcado de [supuesto] cuando aplique.",
      "Cierre con aplicacion profesional."
    ],
    "argumentative_patterns": [
      "Problema -> objetivo -> marco conceptual/normativo -> analisis propio -> conclusion.",
      "Afirmacion relevante -> evidencia verificable -> interpretacion juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Integridad academica",
        "Trazabilidad cita-texto-bib",
        "Control de supuestos",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Compresion union-dedupe"
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
          "justification": "Evita heredar memoria no parseable o ambigua."
        },
        {
          "source": "Integridad academica",
          "target": "Trazabilidad cita-texto-bib",
          "kind": "depends_on",
          "justification": "La verificabilidad exige correspondencia explicita entre afirmaciones y fuentes."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La aplicacion profesional surge del razonamiento del estudiante."
        },
        {
          "source": "Control de supuestos",
          "target": "Rigor editorial",
          "kind": "supports",
          "justification": "Distingue hechos confirmados de datos pendientes."
        }
      ],
      "evidence": [
        "README local: identidad UnADM, ubicacion curricular, pauta editorial.",
        "Programa analitico local: proposito y ejes de trabajo.",
        "Destino contiene placeholders y nombres truncados que requieren correccion previa.",
        "Historial institucional: salida no JSON en ciclos previos exige gate de normalizacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 22: deduplicacion de reglas repetidas sin perdida semantica.",
      "Ciclo 22: refuerzo de quality gates JSON + trazabilidad + control de placeholders.",
      "Ciclo 22: transferencia conservadora transversal sin arrastre tematico de Filosofia del Derecho.",
      "Ciclo 22: consolidacion del patron argumentativo reusable para actividades de Derecho UnADM."
    ]
  }
}