{
  "summary": [
    "Se consolida memoria transversal minima para la materia destino con identidad UnADM y enfoque juridico.",
    "Se preservan reglas estables del origen: normalizacion estructurada, ejes editoriales y control de supuestos.",
    "Se mantiene estrategia conservadora: no transferir contenido tematico especifico de Filosofia del Derecho sin validacion local.",
    "Se refuerza correccion de placeholders y nombres de archivo truncados como riesgo operativo transversal.",
    "Se mantiene compresion lossless por union y deduplicacion, sin regresion de reglas utiles."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 8, bloque 2, tipo Electiva.",
    "Usar carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no confirmado en consigna o documentos locales.",
    "Mantener autor y matricula confirmados en front matter: Martin Jonathan de la Cruz, ES2611202040.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto final con la planeacion semanal y la consigna vigente.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener coherencia entre README, programa analitico, .tex y .bib."
  ],
  "activity_rules": [
    "Traducir cada consigna semanal a producto concreto solicitado.",
    "Incluir postura argumentada del estudiante, no solo resumen descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Vincular conceptos, normas, doctrina o datos con el problema tratado.",
    "No trasladar contenidos especificos de otra asignatura sin fuente verificable."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar memoria aguas abajo.",
    "Confirmar trazabilidad entre afirmaciones, citas en texto y .bib.",
    "Confirmar ausencia de placeholders visibles o tokens sin expandir en README, programa, .tex y .bib.",
    "Validar correspondencia del producto con la consigna de la actividad local.",
    "Confirmar que toda afirmacion no verificada este marcada como [supuesto]."
  ],
  "latex_rules": [
    "Conservar plantilla LaTeX base de la materia y metadatos institucionales.",
    "Actualizar titulo, subtitulo y numero real de actividad antes de compilar.",
    "Completar solo campos confirmados; mantener [supuesto] en campos pendientes.",
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens tipo $(@{...}.Slug) a nombres literales de archivo.",
    "Corregir nombres truncados en estructura: eporte -> reporte, eferencias -> referencias."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas por actividad en electiva-semestre-8-bloque-2.bib.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Verificar consistencia entre claves citadas en texto y entradas .bib."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo abstracciones editoriales estables y validadas.",
    "Priorizar transferencia de identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar propagar redaccion literal o contenido tematico no transversal.",
    "Mantener etiqueta provisional para herencias de ciclo 1 hasta revision manual.",
    "Aplicar union-dedupe sin eliminar reglas utiles previas.",
    "Si nodo destino carece de contexto local, mantener cerebro minimo y abrir preguntas."
  ],
  "open_questions": [
    "[supuesto] Confirmar creditos oficiales de la electiva para completar metadatos.",
    "[supuesto] Confirmar nombre oficial de figura docente en plantilla.",
    "[supuesto] Confirmar si el nombre oficial de la materia difiere de Electiva Semestre 8 Bloque 2.",
    "[supuesto] Confirmar politica institucional de year y fecha de consulta para @misc del sitio UnADM.",
    "[supuesto] Confirmar si existen rubricas locales que ajusten profundidad argumentativa.",
    "[supuesto] Confirmar productos permitidos por actividad: reporte, presentacion u otro formato."
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
        "[supuesto] Creditos pendientes de confirmacion."
      ]
    },
    "essence": [
      "Problema juridico o social como punto de partida.",
      "Conceptos y fuentes pertinentes con trazabilidad.",
      "Analisis propio sustentado.",
      "Conclusion juridica aplicable.",
      "Normalizacion estructurada antes de propagar."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables juridicos claros y verificables.",
      "Asegurar continuidad editorial transversal sin perder identidad institucional.",
      "Prevenir errores de forma que comprometan compilacion, trazabilidad o evaluacion."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Secciones explicitas y ordenadas.",
      "Postura propia respaldada.",
      "Cierre con transferencia profesional.",
      "Marcado explicito de [supuesto]."
    ],
    "argumentative_patterns": [
      "Plantear problema -> delimitar objetivo -> desarrollar marco conceptual/normativo -> argumentar postura -> concluir aplicacion.",
      "Usar evidencia verificable para sostener afirmaciones clave.",
      "Evitar descripcion pura; priorizar juicio juridico razonado."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Normalizacion estructurada",
        "Problema juridico",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Trazabilidad cita-texto-bib",
        "Control de supuestos",
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
          "justification": "Evita heredar errores de formato y memoria no parseable."
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
          "justification": "La conclusion profesional surge del razonamiento del estudiante y no del resumen."
        },
        {
          "source": "Control de supuestos",
          "target": "Rigor editorial",
          "kind": "supports",
          "justification": "Distingue datos confirmados de datos pendientes y reduce afirmaciones impropias."
        }
      ],
      "evidence": [
        "README local: identidad UnADM, ubicacion curricular y pauta editorial.",
        "Programa analitico local: proposito y ejes de trabajo reutilizables.",
        "Archivo .bib local: base institucional con claves verificables."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas entre origen y destino sin perdida semantica.",
      "Se conservaron gates criticos: JSON parseable, estructura minima y trazabilidad bibliografica.",
      "Se reforzo regla transversal de resolver placeholders y nombres truncados.",
      "Se limitaron transferencias a abstracciones estables por tratarse de nodos no equivalentes.",
      "Se mantuvieron vacios locales abiertos con marca [supuesto] para cierre posterior."
    ]
  }
}