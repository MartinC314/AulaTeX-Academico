{
  "summary": [
    "Se sincroniza memoria transversal desde actividad de Filosofia del Derecho hacia materia de Antropologia con estrategia conservadora.",
    "Se preservan reglas utiles vigentes del destino y se agregan solo abstracciones estables reutilizables.",
    "Se refuerza compresion lossless por union-dedupe y no regresion.",
    "Se mantiene alerta institucional: no propagar salidas no estructuradas sin normalizacion.",
    "Se confirma contexto local del destino con README, programa analitico, .bib y plantillas .tex."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No trasladar metadatos curriculares especificos de Filosofia del Derecho al destino."
  ],
  "structure_rules": [
    "Iniciar cada entregable con objetivo puntual y encuadre del problema.",
    "Usar secuencia reusable: problema, conceptos, evidencia, analisis propio, cierre.",
    "Separar artefactos: reporte, presentacion y bibliografia.",
    "Alinear el producto al entregable solicitado en la planeacion semanal.",
    "Usar README y programa analitico como guias canonicas de estructura.",
    "Resolver placeholders y tokens dinamicos en nombres de archivo antes de compilar o citar."
  ],
  "activity_rules": [
    "Sustentar afirmaciones relevantes con fuente verificable y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar resumen solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Cerrar con conclusion transferible a la practica juridica cuando la consigna lo requiera.",
    "Evitar importar contenidos tematicos de otra materia sin puente disciplinar explicito."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Exigir estructura minima completa del esquema antes de reutilizar memoria.",
    "Revisar y normalizar manualmente respuestas no estructuradas detectadas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Verificar correspondencia entre producto entregado y consigna real de la actividad."
  ],
  "latex_rules": [
    "Mantener plantilla base de la materia como referencia inicial.",
    "Usar configuracion en espanol y acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir rutas truncadas y tokens sin expandir tipo $(@{...}.Slug)."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias realmente consultables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales pertinentes.",
    "Registrar fuentes especificas de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No citar entradas inexistentes en el .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y abstractas entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferencia literal de redaccion o contenidos tematicos exclusivos del origen.",
    "Mantener etiquetas de provisionalidad en reglas heredadas no verificadas.",
    "Preservar reglas utiles previas en cada ciclo sin eliminacion regresiva."
  ],
  "open_questions": [
    "Supuesto: falta consigna local de actividades especificas de Antropologia; confirmar formatos exactos por semana.",
    "Confirmar si la conclusion juridica es obligatoria en todas las actividades de la materia o solo en algunas.",
    "Confirmar estandar unico de citacion institucional para la licenciatura.",
    "Confirmar si LDE-S4B2 es clave oficial definitiva o etiqueta operativa local."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con trazabilidad de fuentes.",
        "Entrada canonica por carpeta de materia."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 4, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Antropologia de la cultura en Mexico."
      ]
    },
    "essence": [
      "Problema claro al inicio.",
      "Conceptos pertinentes y delimitados.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Cierre transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos estructurados y verificables.",
      "Sostener coherencia institucional y calidad transversal entre materias."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales sin relleno.",
      "Supuestos marcados de forma visible.",
      "Citas trazables y cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente -> interpretacion propia.",
      "Pregunta guia -> desarrollo coherente -> respuesta final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON parseable",
        "Evidencia verificable",
        "Analisis propio",
        "Coherencia argumentativa",
        "Conclusion transferible",
        "Provisionalidad de fuentes heredadas"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Validacion JSON parseable",
          "target": "Normalizacion estructurada",
          "kind": "depends_on",
          "justification": "Sin parseo valido no hay propagacion confiable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura academica gana validez con respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La transferencia profesional depende del razonamiento propio."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Coherencia argumentativa",
          "kind": "supports",
          "justification": "La pauta institucional exige claridad, orden y sustento."
        }
      ],
      "evidence": [
        "README destino: identidad UnADM, entrada canonica y pauta editorial.",
        "Programa analitico destino: ejes de trabajo y proposito de realizacion.",
        ".bib destino: fuentes base institucionales verificables.",
        "Regla heredada estable: bloquear salida no JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 52: se refuerza regla transversal de normalizacion estructurada antes de propagar.",
      "Ciclo 52: se integra patron estable objetivo-evidencia-postura-coherencia desde origen.",
      "Ciclo 52: se excluyen contenidos tematicos propios de Filosofia del Derecho por no equivalencia de nodo.",
      "Ciclo 52: se mantiene alerta de tokens dinamicos sin expandir en README/programa/.tex/.bib."
    ]
  }
}