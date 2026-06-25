{
  "summary": [
    "Se sincroniza memoria transversal desde actividad no equivalente con estrategia conservadora.",
    "Se preservan reglas estables de identidad UnADM, estructura reusable y control de calidad.",
    "Se mantiene compresion lossless por union-dedupe sin eliminar reglas utiles previas.",
    "Se refuerza bloqueo de propagacion ante salidas no parseables y necesidad de normalizacion.",
    "Supuesto: la consigna local por actividad en Garantias constitucionales aun no esta incorporada."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en tono, portada y metadatos.",
    "Usar contexto curricular local verificado: Licenciatura en Derecho, semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No transferir contenido disciplinar de Filosofia del Derecho a Garantias constitucionales sin validacion expresa."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Alinear formato final al producto solicitado por la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion, programa analitico y bibliografia.",
    "Corregir placeholders y truncamientos en README, programa y plantilla antes de reutilizar."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante y evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar afirmaciones constitucionales sin fundamento normativo o bibliografico.",
    "Validar que cada entrega corresponda a la consigna real de la actividad local."
  ],
  "quality_gates": [
    "Bloquear propagacion automatica si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar congruencia entre metadatos de portada y datos curriculares locales.",
    "Compilar LaTeX sin errores criticos ni referencias rotas."
  ],
  "latex_rules": [
    "Conservar plantilla local y clase base existente salvo necesidad verificable.",
    "Completar campos de portada: actividad, figura docente y fecha segun consigna.",
    "Mantener codificacion y acentos correctos en .tex y .bib.",
    "No introducir paquetes no estandar sin justificacion editorial o tecnica.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion.",
    "Corregir tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir truncamientos de macros y rutas antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y normas juridicas verificables.",
    "Registrar fuentes especificas por actividad en garantias-constitucionales.bib.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/editorial o URL.",
    "Agregar identificador normativo, emisor y fecha cuando se cite legislacion o jurisprudencia."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas editoriales generales ya validadas.",
    "Evitar trasladar contenido tematico entre materias sin validacion local.",
    "Mantener alerta institucional de riesgo por herencias no estructuradas.",
    "Aplicar union-dedupe sin regresion en cada ciclo.",
    "Etiquetar como provisional toda regla heredada sin evidencia local.",
    "Si falta consigna en destino, conservar cerebro editorial minimo y abrir vacios de contexto."
  ],
  "open_questions": [
    "Confirmar consigna de la primera actividad de Garantias constitucionales.",
    "Confirmar rubrica de evaluacion local para ajustar profundidad argumentativa.",
    "Confirmar estilo de citacion exigido en la materia.",
    "Confirmar si la fecha de portada debe ser automatica o fija por entrega.",
    "Verificar correccion final de truncamientos en reporte-garantias-constitucionales.tex.",
    "Supuesto: garantias-constitucionales.bib es el archivo bibliografico canonico definitivo."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador ante datos no verificados."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada antes de propagar.",
        "Trazabilidad entre consigna, fuentes y producto."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura destino: Garantias constitucionales.",
        "Semestre 2, bloque 1, obligatoria, 8 creditos.",
        "Coursecode local: LDE-S2B1."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible.",
      "Consistencia cita-texto-bib.",
      "Normalizacion estructurada para propagacion segura."
    ],
    "reason_for_being": [
      "Orientar productos academicos con claridad juridica, evidencia y aplicabilidad profesional.",
      "Convertir planeacion semanal en entregables verificables y trazables.",
      "Sostener continuidad editorial entre nodos sin contaminar contenido disciplinar."
    ],
    "style_markers": [
      "Frases breves y verificables.",
      "Separacion clara entre marco normativo y opinion personal.",
      "Marcado explicito de supuestos.",
      "Cierre con aplicacion juridica concreta.",
      "No literalidad heredada; solo abstracciones estables."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Objetivo puntual.",
      "Marco conceptual y normativo delimitado.",
      "Analisis propio sustentado.",
      "Conclusion aplicable a practica juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Normalizacion estructurada",
        "Problema juridico o social",
        "Marco normativo o doctrinal",
        "Analisis propio",
        "Conclusion transferible",
        "Consistencia cita-texto-bib"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La identidad institucional exige verificabilidad y trazabilidad."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Consistencia cita-texto-bib",
          "kind": "supports",
          "justification": "La estructura valida facilita control bibliografico y auditoria."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere una pregunta juridica delimitada."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion profesional necesita sustento legal verificable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La postura argumentada conduce a una salida aplicable."
        }
      ],
      "evidence": [
        "README local con ubicacion curricular y pauta editorial.",
        "Programa analitico con ejes de trabajo reutilizables.",
        "Archivo garantias-constitucionales.bib con base institucional.",
        "Regla institucional persistente: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 3: se consolida transferencia transversal solo de abstracciones editoriales estables.",
      "Ciclo 3: se refuerza union-dedupe sin regresion en identidad, estructura y gates.",
      "Ciclo 3: se mantiene prohibicion de transferir contenido disciplinar entre materias no equivalentes.",
      "Ciclo 3: se preserva alerta de normalizacion manual para herencias no estructuradas."
    ]
  }
}