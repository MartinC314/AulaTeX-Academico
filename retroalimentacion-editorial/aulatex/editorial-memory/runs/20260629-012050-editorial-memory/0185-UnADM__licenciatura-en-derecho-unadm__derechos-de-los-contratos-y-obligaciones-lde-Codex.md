{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia conservadora y sin regresion.",
    "Se preservan reglas estables institucionales, estructurales y de calidad de UnADM.",
    "Se refuerza normalizacion obligatoria de salidas no estructuradas antes de propagar.",
    "Se mantiene compresion lossless por union-dedupe sin recorte de reglas utiles.",
    "Se agregan mejoras verificables del contexto local: resolucion de tokens Slug y rutas con caracteres anómalos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares verificados de la materia: semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Conservar enfoque juridico aplicado a contratos y obligaciones.",
    "Usar codigo de curso LDE-S4B1 cuando la plantilla lo requiera.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como [supuesto] todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al tipo solicitado por la planeacion semanal.",
    "Mantener trazabilidad entre objetivo, evidencia, argumento y conclusion.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Distinguir bibliografia base de fuentes especificas de actividad."
  ],
  "activity_rules": [
    "Adaptar cada actividad al producto solicitado por la consigna.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y cierre.",
    "Evitar traslado literal desde otras materias sin adecuacion disciplinar.",
    "No asumir fuentes de semanas posteriores sin validacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Validar compatibilidad disciplinar en propagacion lateral.",
    "No degradar reglas utiles previas durante fusion por deduplicacion."
  ],
  "latex_rules": [
    "Conservar plantilla LaTeX base de la materia y metadatos institucionales completos.",
    "Usar español academico con acentos correctos en .tex y .bib.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver placeholders tipo $(@{...}.Slug) en README y programa analitico antes de compilar.",
    "Corregir caracteres anomalos en rutas o nombres de archivo antes de compilar.",
    "Actualizar documentsubtitle y documenttitle segun actividad real antes de entrega."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas por actividad en derechos-de-los-contratos-y-obligaciones.bib.",
    "Priorizar fuentes institucionales UnADM, normas, doctrina y jurisprudencia verificables.",
    "No inventar referencias.",
    "Conservar metadatos minimos: autor, titulo, año y fuente/editorial o URL.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Declarar [supuesto] cuando una referencia requerida no este disponible."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas transversales estables entre nodos no equivalentes.",
    "Excluir metadatos especificos de materia al propagar lateralmente a otras asignaturas.",
    "Reutilizar gates de calidad institucional como control transversal.",
    "Aplicar normalizacion manual en ciclos tempranos cuando haya herencia no estructurada.",
    "Mantener estrategia progresiva y conservadora: sumar, deduplicar, no recortar."
  ],
  "open_questions": [
    "[supuesto] Falta consigna textual de actividades destino; confirmar producto exacto por semana.",
    "Confirmar rubrica de evaluacion por actividad para calibrar profundidad argumentativa.",
    "Confirmar guia formal de citacion juridica obligatoria de la materia.",
    "Confirmar si presentacion y reporte comparten metadatos obligatorios exactos.",
    "Confirmar uso esperado de legislacion federal, local o mixta segun actividad."
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
        "Semestre 4, bloque 1, obligatoria, 8 creditos.",
        "Asignatura centrada en contratos y obligaciones."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo/doctrinal pertinentes.",
      "Evidencia verificable.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir la planeacion semanal en productos academicos trazables y verificables.",
      "Asegurar coherencia entre identidad institucional, evidencia y argumentacion juridica.",
      "Garantizar reutilizacion transversal sin perder especificidad local."
    ],
    "style_markers": [
      "Frases claras y accionables.",
      "Supuestos explicitados cuando falte contexto.",
      "Cierre con utilidad profesional juridica.",
      "Sin literalidad transferida entre materias."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Marco conceptual-normativo.",
      "Analisis propio sustentado.",
      "Cierre juridico aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "JSON parseable",
        "Trazabilidad objetivo-evidencia-conclusion",
        "Contratos",
        "Obligaciones",
        "Bibliografia verificable",
        "Supuestos explicitados"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Bibliografia verificable",
          "kind": "supports",
          "justification": "La pauta institucional exige integridad academica con citas verificables."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "JSON parseable",
          "kind": "depends_on",
          "justification": "La propagacion solo procede con estructura valida."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio con postura academica",
          "kind": "develops",
          "justification": "El analisis deriva de una pregunta juridica concreta."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion debe fundarse en normas y doctrina verificables."
        },
        {
          "source": "Contratos",
          "target": "Obligaciones",
          "kind": "depends_on",
          "justification": "El nucleo disciplinar de la materia articula ambas categorias."
        }
      ],
      "evidence": [
        "README de materia: identidad UnADM, carpeta canonica, conclusion juridica con criterio propio.",
        "Programa analitico: cinco ejes de trabajo y proposito editorial.",
        "Archivo .bib local: entradas institucionales verificables."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin perdida semantica.",
      "Se conservaron controles heredados de calidad y normalizacion.",
      "Se incorporo control transversal de placeholders Slug por evidencia local.",
      "Se mantuvo separacion entre abstracciones estables y detalles locales no transferibles."
    ]
  }
}