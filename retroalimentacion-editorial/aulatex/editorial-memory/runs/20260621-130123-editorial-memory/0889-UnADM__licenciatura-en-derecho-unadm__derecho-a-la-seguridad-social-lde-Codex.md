{
  "summary": [
    "Sincronizacion transversal ciclo 3 consolidada con estrategia progresiva y conservadora.",
    "Se preserva identidad UnADM y enfoque juridico de la materia destino.",
    "Se refuerzan ejes estables reutilizables: problema, fundamento, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene compresion lossless por union-dedupe sin regresion.",
    "Se conserva alerta institucional por antecedentes de salida no parseable y necesidad de normalizacion previa."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local [supuesto].",
    "No sobrescribir reglas validas previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README y programa analitico de la materia como canon estructural.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar desarrollo en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear el formato al producto solicitado por la planeacion semanal.",
    "Mantener consistencia entre reporte, presentacion y referencias."
  ],
  "activity_rules": [
    "Delimitar desde el inicio problema y alcance de la actividad.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar entregas solo descriptivas.",
    "Distinguir hechos, conceptos, normas y opinion propia.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizar aguas abajo.",
    "Validar estructura minima completa antes de propagacion recursiva.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregado y consigna vigente."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificacion y acentos correctos en .tex y .bib.",
    "Mantener metadatos institucionales y curriculares consistentes.",
    "Evitar comandos no estandar sin justificacion tecnica.",
    "Corregir rutas, nombres corruptos o tokens sin expandir antes de compilar.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central.",
    "Priorizar fuentes institucionales UnADM y normas juridicas vigentes verificables.",
    "Agregar solo referencias consultables con metadatos minimos completos.",
    "No inventar referencias; marcar faltantes como pendientes [supuesto].",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion."
  ],
  "propagation_hints": [
    "Propagar lateral y arriba solo reglas generales validadas y abstractas.",
    "No transferir contenido tematico especifico de Filosofia del Derecho al destino.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Mantener bandera de riesgo por ciclos con salida no parseable.",
    "Aplicar union-dedupe en cada ciclo para evitar duplicados y regresiones.",
    "Si falta contexto local, mantener cerebro minimo y abrir preguntas verificables."
  ],
  "open_questions": [
    "Confirmar si la materia exige norma de citacion especifica (APA, ISO, institucional o juridica mexicana) [supuesto].",
    "Confirmar datos oficiales faltantes de figura docente para portada [supuesto].",
    "Confirmar si persiste alguna fuente provisional heredada de nodos no juridicos y depurarla [supuesto].",
    "Confirmar rubricas por actividad para ajustar profundidad argumentativa [supuesto]."
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
      "Producto juridico verificable con estructura estable.",
      "Problema, fundamento, evidencia, analisis propio y conclusion transferible.",
      "Persistencia editorial sin perdida por union-dedupe."
    ],
    "reason_for_being": [
      "Convertir consignas en entregables juridicos claros, sustentados y evaluables.",
      "Preservar identidad institucional y calidad tecnica de produccion LaTeX.",
      "Habilitar reutilizacion transversal segura entre nodos no equivalentes."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion visible entre marco, analisis y cierre.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo y doctrinal.",
      "Contrastar evidencia verificable.",
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
          "justification": "El analisis requiere una pregunta juridica delimitada."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida depende de fundamento legal verificable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura academica exige respaldo comprobable."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "La consolidacion lossless requiere estructura valida."
        },
        {
          "source": "Compresion union-dedupe",
          "target": "Identidad institucional UnADM",
          "kind": "supports",
          "justification": "Evita regresion de reglas nucleares entre ciclos."
        }
      ],
      "evidence": [
        "README de materia define estructura canonica y artefactos base.",
        "Programa analitico define proposito y ejes juridicos de trabajo.",
        "Archivo .bib local confirma base normativa e institucional vigente.",
        "Regla estable: bloquear propagacion si no hay JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 3: se refuerza patron comun transversal sin mover contenido tematico entre materias.",
      "Ciclo 3: se preservan gates criticos de parseo, normalizacion y trazabilidad de supuestos.",
      "Ciclo 3: se consolida ADN minimo persistente del destino con enfoque en calidad y reutilizacion segura."
    ]
  }
}