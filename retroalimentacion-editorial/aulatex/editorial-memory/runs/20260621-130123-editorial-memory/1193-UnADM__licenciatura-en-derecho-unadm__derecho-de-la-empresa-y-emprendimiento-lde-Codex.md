{
  "summary": [
    "Se consolida sincronizacion transversal desde actividad de otra materia con transferencia solo de abstracciones estables.",
    "Se preservan reglas utiles previas del destino y se refuerza el marco reusable: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene obligatoria la normalizacion estructurada antes de cualquier propagacion recursiva.",
    "Se conserva alerta local por tokens Slug sin expandir y artefactos de nombres de archivo en README y programa analitico.",
    "Se evita transferir contenido doctrinal especifico de Filosofia del Derecho por no equivalencia disciplinar."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial de la materia destino en todos los artefactos.",
    "Usar Licenciatura en Derecho como programa academico.",
    "Respetar contexto curricular local confirmado: semestre 6, bloque 2, obligatoria, 8 creditos.",
    "Marcar como supuesto todo dato no confirmado por consigna o archivo local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Usar README de materia como entrada canonica.",
    "Definir objetivo puntual antes del desarrollo.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar desarrollo en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el entregable al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Conservar correspondencia entre .tex, presentacion y .bib de la materia."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar entregas solo descriptivas.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir fuentes de semanas posteriores sin confirmacion en consigna.",
    "Agregar fuentes especificas de actividad al .bib local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar memoria.",
    "Revisar y normalizar respuestas no estructuradas antes de propagacion lateral, ascendente o aguas abajo.",
    "No eliminar reglas utiles previas durante fusion por union-dedupe.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Verificar correspondencia del producto con la consigna de la actividad local."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir artefactos de nombres de archivo visibles antes de compilar."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo obras consultables.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales y estables entre nodos no equivalentes.",
    "No propagar contenido doctrinal especifico de Filosofia del Derecho a esta materia.",
    "Mantener estrategia progresiva y conservadora: agregar mejoras verificables sin regresion.",
    "Exigir normalizacion manual en memorias historicas con antecedente de salida no estructurada."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de actividades locales; confirmar producto exacto por semana.",
    "Confirmar si documentauthor de plantilla debe parametrizarse por actividad.",
    "Confirmar valor final expandido del Slug en README y programa analitico.",
    "Confirmar si year=2026 en unadmSitioWeb se mantiene como anio bibliografico o solo fecha de consulta.",
    "Confirmar cierre completo del archivo de reporte local, que aparece truncado."
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
        "Integridad academica con trazabilidad bibliografica.",
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 6, bloque 2, obligatoria, 8 creditos.",
        "Transferencia profesional como criterio de cierre."
      ]
    },
    "essence": [
      "Problema juridico.",
      "Conceptos y marco normativo.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible.",
      "Control explicito de supuestos."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos claros, sustentados y aplicables.",
      "Asegurar consistencia institucional y calidad tecnica en todo entregable."
    ],
    "style_markers": [
      "Frases claras y directas.",
      "Supuestos etiquetados.",
      "Sin afirmaciones sin fuente.",
      "Cierre con aplicacion practica."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis propio -> conclusion.",
      "Marco normativo o doctrinal como soporte de la postura personal.",
      "Coherencia entre pregunta guia y respuesta final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Problema juridico",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Integridad bibliografica",
        "Control de supuestos"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin JSON valido no hay transferencia segura."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion requiere respaldo documental."
        },
        {
          "source": "Control de supuestos",
          "target": "Integridad argumentativa",
          "kind": "supports",
          "justification": "Distingue hechos confirmados de inferencias."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El analisis parte del problema delimitado."
        }
      ],
      "evidence": [
        "README local: ubicacion curricular y pauta editorial.",
        "Programa analitico local: proposito y ejes de trabajo.",
        "Archivo .bib local: fuentes institucionales base.",
        "Memoria origen: reglas estables de estructura, calidad y control de supuestos."
      ]
    },
    "reinforcement_log": [
      "Ciclo 13: se refuerza ADN institucional sin recorte, con deduplicacion.",
      "Ciclo 13: se preservan gates de JSON parseable y normalizacion obligatoria.",
      "Ciclo 13: se consolidan patrones argumentativos reutilizables entre materias.",
      "Ciclo 13: se mantiene vacio doctrinal local abierto para completar con consignas de la materia destino."
    ]
  }
}