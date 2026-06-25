{
  "summary": [
    "Se consolida sincronizacion transversal desde actividad de Filosofia del Derecho hacia materia de Antropologia con estrategia conservadora.",
    "Se preservan reglas utiles previas del destino y se agregan solo abstracciones estables reutilizables.",
    "Se refuerza normalizacion estructurada, validacion JSON y trazabilidad de fuentes como nucleos persistentes.",
    "No se transfieren contenidos tematicos propios de Filosofia del Derecho al destino por no equivalencia de nodo.",
    "Se mantiene compresion lossless por union-dedupe y sin regresion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener contexto local del destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar toda fuente heredada no verificada como provisional hasta validacion local.",
    "No trasladar metadatos curriculares de Filosofia del Derecho a Antropologia."
  ],
  "structure_rules": [
    "Iniciar cada entrega con objetivo puntual y encuadre breve del problema juridico o social.",
    "Usar secuencia reusable: conceptos clave, marco pertinente, analisis propio y cierre.",
    "Alinear siempre el formato final al producto solicitado en la planeacion semanal.",
    "Mantener separacion de artefactos: reporte, presentacion y bibliografia.",
    "Resolver placeholders y tokens dinamicos en README, programa y rutas antes de usar."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Evitar extrapolar bibliografia de semanas o materias distintas sin justificacion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa del esquema antes de reutilizar.",
    "Confirmar que cada afirmacion relevante tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No promover reglas provisionales a definitivas sin validacion disciplinar local."
  ],
  "latex_rules": [
    "Usar codificacion en español coherente en .tex y .bib.",
    "Mantener compilacion sin errores criticos ni referencias rotas.",
    "Mantener claves BibTeX estables para evitar quiebres de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Corregir rutas con caracteres truncados y resolver tokens $(@{...}.Slug) a nombre literal."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables y consultables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes especificas de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, año y fuente/editorial o URL.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y abstractas entre nodos transversales.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferencia literal de redaccion o contenido tematico disciplinar no equivalente.",
    "Mantener registro de incidencias de parseo como alerta reutilizable inter-materias.",
    "Aplicar union-dedupe sin eliminar reglas utiles previas."
  ],
  "open_questions": [
    "Supuesto: confirmar si LDE-S4B2 es clave oficial institucional o local.",
    "Confirmar estandar unico de citacion para la licenciatura.",
    "Confirmar si la conclusion juridica es obligatoria en todas las actividades de Antropologia.",
    "Confirmar rubrica oficial de evaluacion para ajustar profundidad argumentativa.",
    "Confirmar que el nombre canonico del .bib quede fijo sin plantilla dinamica."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y preciso.",
        "Argumentativo con criterio propio.",
        "Culturalmente sensible y juridicamente pertinente."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con trazabilidad.",
        "Normalizacion estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Antropologia de la cultura en Mexico.",
        "Semestre 4, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema claro.",
      "Conceptos pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos con rigor y trazabilidad.",
      "Asegurar coherencia entre identidad institucional, metodo argumentativo y evidencia."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente verificable -> interpretacion propia.",
      "Pregunta guia -> desarrollo coherente -> cierre consistente."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON parseable",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Compresion union-dedupe sin regresion"
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
          "justification": "La postura se legitima con respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion util deriva del razonamiento."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "La pauta institucional exige integridad academica."
        }
      ],
      "evidence": [
        "README local de materia con pauta editorial y ubicacion curricular.",
        "Programa analitico local con ejes problema-conceptos-evidencia-analisis-cierre.",
        "Archivo .bib local con fuentes base institucionales.",
        "Memoria origen con reglas estables de calidad, estructura y trazabilidad."
      ]
    },
    "reinforcement_log": [
      "Ciclo 16: se reforzo gate de JSON parseable como bloqueo duro de propagacion.",
      "Ciclo 16: se incorporo objetivo puntual al inicio como patron transversal estable.",
      "Ciclo 16: se preservaron reglas locales de Antropologia sin mezclar metadatos de Filosofia.",
      "Ciclo 16: se reforzo resolucion de placeholders en rutas y nombres de archivo.",
      "Ciclo 16: consolidacion realizada por union-dedupe lossless y sin regresion."
    ]
  }
}