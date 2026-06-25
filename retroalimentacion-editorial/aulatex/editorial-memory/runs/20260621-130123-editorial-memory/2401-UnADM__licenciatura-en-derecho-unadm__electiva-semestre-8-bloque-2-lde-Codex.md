{
  "summary": [
    "Se sincroniza memoria transversal desde actividad no equivalente sin trasladar contenido tematico especifico.",
    "Se preserva identidad UnADM y enfoque juridico con compresion lossless por union-dedupe.",
    "Se refuerzan gates de normalizacion JSON, trazabilidad de fuentes y control de supuestos.",
    "Se mantiene correccion obligatoria de placeholders y nombres de archivo truncados como riesgo operativo transversal."
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
    "Alinear el producto al tipo solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener consistencia entre README, programa analitico, .tex y .bib."
  ],
  "activity_rules": [
    "Traducir cada consigna semanal a producto concreto.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No importar contenidos especificos de otra materia sin verificacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar.",
    "Confirmar trazabilidad entre afirmaciones, citas en texto y .bib.",
    "Confirmar ausencia de placeholders o tokens sin expandir en README, programa, .tex y .bib.",
    "Validar correspondencia entre producto entregado y consigna vigente.",
    "Mantener normalizacion manual para herencias de ciclo 1 cuando aplique."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Actualizar titulo, subtitulo y numero real de actividad antes de compilar.",
    "Resolver tokens tipo $(@{...}.Slug) a nombres literales.",
    "Corregir nombres truncados en estructura (ej. eporte, eferencias)."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas por actividad en electiva-semestre-8-bloque-2.bib.",
    "Priorizar fuentes institucionales UnADM cuando correspondan.",
    "No inventar referencias.",
    "Usar solo obras consultables y verificables.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones estables en nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates y grafo conceptual.",
    "Evitar transferir redaccion literal y contenido tematico local del origen.",
    "Aplicar estrategia progresiva y conservadora sin regresion de reglas utiles.",
    "Etiquetar como provisional toda herencia no verificada."
  ],
  "open_questions": [
    "[supuesto] Confirmar creditos oficiales de la materia destino.",
    "[supuesto] Confirmar nombre oficial de figura docente.",
    "[supuesto] Confirmar si el year del sitio UnADM en .bib es dato final o temporal.",
    "[supuesto] Confirmar politica local de fecha de consulta para @misc institucional.",
    "[supuesto] Confirmar consignas reales de actividades para ajustar tipos de artefacto."
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
        "Trazabilidad entre documentos locales."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 8, bloque 2, tipo Electiva.",
        "[supuesto] Creditos por confirmar."
      ]
    },
    "essence": [
      "Problema juridico.",
      "Conceptos y fuentes pertinentes.",
      "Analisis propio.",
      "Conclusion juridica transferible.",
      "Control de supuestos."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables juridicos verificables.",
      "Sostener calidad editorial institucional reusable en todo el nodo materia."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones explicitas.",
      "Postura propia sustentada.",
      "Cierre aplicable a practica juridica.",
      "Marcado explicito de [supuesto]."
    ],
    "argumentative_patterns": [
      "Problema -> objetivo -> marco conceptual/normativo -> analisis propio -> conclusion.",
      "Afirmacion -> evidencia verificable -> inferencia juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Integridad academica",
        "Trazabilidad cita-texto-bib",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Control de supuestos",
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
          "justification": "Reduce errores heredados y evita memoria no parseable."
        },
        {
          "source": "Integridad academica",
          "target": "Trazabilidad cita-texto-bib",
          "kind": "depends_on",
          "justification": "La verificabilidad exige correspondencia entre texto y fuentes."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La transferencia profesional surge del razonamiento propio."
        },
        {
          "source": "Control de supuestos",
          "target": "Rigor editorial",
          "kind": "supports",
          "justification": "Diferencia datos confirmados de datos pendientes."
        }
      ],
      "evidence": [
        "README local: pauta editorial e identidad UnADM.",
        "Programa analitico local: ejes de trabajo reutilizables.",
        "Bibliografia local: claves institucionales base.",
        "Herencia institucional: ciclo 1 requiere normalizacion manual."
      ]
    },
    "reinforcement_log": [
      "Ciclo 7: deduplicacion completa de reglas repetidas y variantes ortograficas.",
      "Ciclo 7: se conserva regla historica de bloqueo por JSON no parseable.",
      "Ciclo 7: se incorpora control transversal de tokens sin expandir.",
      "Ciclo 7: no se transfirio contenido doctrinal especifico de Filosofia del Derecho por no equivalencia de nodo."
    ]
  }
}