{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia progresiva y conservadora.",
    "Se transfieren solo abstracciones editoriales estables desde actividad de Filosofia del Derecho.",
    "Se preserva identidad UnADM y estructura canonica de la materia destino.",
    "Se refuerzan ejes comunes: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene regla de normalizacion obligatoria para salidas no JSON parseables.",
    "Se evita transferencia de contenido tematico especifico de Filosofia del Derecho no equivalente al destino."
  ],
  "identity_rules": [
    "Mantener identidad explicita UnADM en tono, portada y metadatos.",
    "Conservar materia exacta: Derecho de la propiedad y registro.",
    "Conservar programa: Licenciatura en Derecho.",
    "Conservar ubicacion curricular local: semestre 7, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar desarrollo en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear siempre el contenido al producto pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Adaptar formato final a reporte, presentacion o producto visual segun consigna."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Relacionar el desarrollo con propiedad y registro cuando aplique.",
    "No asumir fuentes de semanas posteriores sin validacion de consigna."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregado y consigna local."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Mantener clase base y metadatos institucionales de la plantilla local.",
    "Evitar placeholders sin resolver antes de entrega.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico antes de automatizar rutas."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Registrar fuentes especificas de cada actividad en el .bib local de la materia.",
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "Conservar metadatos minimos: autor, titulo, año, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Propagar solo reglas generales cuando falte consigna textual local.",
    "Evitar regresiones frente a reglas utiles previas.",
    "No propagar contenido tematico especifico de una materia no equivalente.",
    "Mantener compresion por union y deduplicacion sin recorte semantico."
  ],
  "open_questions": [
    "Supuesto: falta rubrica local detallada por actividad; confirmar criterios de evaluacion.",
    "Confirmar si cada actividad exige reporte, presentacion u otro producto.",
    "Confirmar estilo de citacion juridica requerido por figura docente.",
    "Supuesto: persisten tokens corruptos en README/programa; confirmar nombres canonicos finales de archivos.",
    "Confirmar sustitucion del placeholder de figura docente en plantilla .tex."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador en inferencias.",
        "Accionable y verificable."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta de asignatura como entrada canonica.",
        "Normalizacion estructurada obligatoria antes de propagacion.",
        "Sin propagacion de salidas no parseables."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho de la propiedad y registro.",
        "Semestre 7, bloque 1, obligatoria, 8 creditos.",
        "Codigo local: LDE-S7B1."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible.",
      "Trazabilidad bibliografica.",
      "Normalizacion estructurada."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros y verificables.",
      "Asegurar fundamento juridico y postura propia en cada entrega.",
      "Garantizar reutilizacion segura de memoria editorial entre nodos."
    ],
    "style_markers": [
      "Frases breves y accionables.",
      "Supuestos siempre marcados.",
      "Sin afirmaciones sin fuente.",
      "Sin placeholders al cierre.",
      "Separacion explicita por secciones funcionales."
    ],
    "argumentative_patterns": [
      "Del problema al marco conceptual.",
      "Del marco normativo a la evidencia.",
      "De la evidencia al analisis propio.",
      "Del analisis a la conclusion aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad academica",
        "Problema juridico",
        "Marco normativo o doctrinal",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion JSON",
        "Trazabilidad bibliografica"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La identidad institucional exige verificabilidad y formato consistente."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis debe responder a una pregunta juridica concreta."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion profesional requiere fundamento juridico."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La trazabilidad evita afirmaciones no sustentadas."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Trazabilidad bibliografica",
          "kind": "depends_on",
          "justification": "La estructura parseable facilita control de consistencia y propagacion."
        }
      ],
      "evidence": [
        "README local: pauta editorial e identidad UnADM.",
        "Programa analitico local: proposito y ejes de trabajo.",
        "Regla heredada valida: bloquear propagacion sin JSON parseable.",
        "Regla heredada valida: marcar supuestos cuando falte evidencia local."
      ]
    },
    "reinforcement_log": [
      "Ciclo 18: deduplicacion de reglas repetidas sin perdida semantica.",
      "Ciclo 18: transferencia transversal limitada a abstracciones estables.",
      "Ciclo 18: exclusion conservadora de contenido tematico especifico de Filosofia del Derecho.",
      "Ciclo 18: refuerzo de gates de calidad, estructura argumentativa y control bibliografico."
    ]
  }
}