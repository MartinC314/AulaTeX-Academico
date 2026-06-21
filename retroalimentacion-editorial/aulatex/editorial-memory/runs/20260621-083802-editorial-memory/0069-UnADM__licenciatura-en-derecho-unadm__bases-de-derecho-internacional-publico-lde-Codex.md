{
  "summary": [
    "Se consolida sincronizacion transversal con transferencia de abstracciones editoriales estables.",
    "Se preserva identidad UnADM y contexto curricular local del destino.",
    "Se refuerzan ejes reutilizables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene estrategia conservadora: no transferir contenido tematico especifico de Filosofia del Derecho.",
    "Se mantiene regla de normalizacion estructurada obligatoria antes de propagacion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local: Bases de derecho internacional publico.",
    "Alinear entregables a Licenciatura en Derecho, semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Usar codigo de curso LDE-S4B1 en metadatos cuando aplique.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como procedencia provisional, no como identidad del entregable."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear la estructura al producto solicitado por la planeacion semanal.",
    "Distinguir reporte, presentacion y producto visual segun consigna.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, normas, doctrina, argumentos y criterio propio.",
    "Evitar extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre consigna, producto entregable y programa analitico local."
  ],
  "latex_rules": [
    "Reutilizar plantilla .tex local sin romper identidad institucional.",
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Corregir caracteres anomalos y tokens sin expandir en README y programa analitico antes de automatizar referencias.",
    "Revisar y cerrar correctamente entornos LaTeX truncados antes de compilar."
  ],
  "bibliography_rules": [
    "Registrar fuentes de actividad en bases-de-derecho-internacional-publico.bib.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Validar que toda clave citada exista en el .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas, estables y no duplicadas.",
    "Aplicar compresion lossless por union-dedupe sin recortar reglas utiles.",
    "No propagar contenido tematico de materias no equivalentes.",
    "Propagar primero identidad, estructura reusable, quality gates y grafo conceptual.",
    "Conservar incidencias historicas de parseo como controles preventivos.",
    "No elevar supuestos a reglas definitivas sin verificacion local."
  ],
  "open_questions": [
    "Confirmar criterio editorial final sobre publico sin acento vs publico con acento en nombres visibles. [supuesto]",
    "Confirmar si se normalizaran tokens $(@{...}.Slug) en README y programa analitico mediante regla automatica local.",
    "Confirmar rubrica de evaluacion por actividad para ajustar profundidad argumentativa.",
    "Confirmar formato minimo de conclusion juridica por tipo de evidencia (normativa, doctrinal, jurisprudencial).",
    "Confirmar si el entorno tabular truncado del reporte base ya fue reparado en el archivo fuente."
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
        "Normalizacion estructurada obligatoria antes de propagacion."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Destino: semestre 4, bloque 1, obligatoria, 8 creditos.",
        "No mezclar metadatos curriculares del origen con el destino."
      ]
    },
    "essence": [
      "Consigna como eje de forma del entregable.",
      "Problema-juridico a conclusion-transferible como columna editorial.",
      "Evidencia verificable como condicion de validez argumentativa.",
      "Postura propia sustentada como marca de autoria academica."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos trazables y evaluables.",
      "Mantener calidad formal y juridica sin perder adaptacion por actividad.",
      "Permitir propagacion segura entre nodos con control de supuestos y parseo."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y no redundantes.",
      "Cierre con criterio juridico aplicable.",
      "Supuestos etiquetados de forma visible."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> norma/doctrina -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> posicion propia.",
      "Consigna -> desarrollo alineado -> verificacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Consigna de actividad",
        "Estructura argumentativa juridica",
        "Evidencia verificable",
        "Conclusion transferible",
        "Normalizacion JSON",
        "Consistencia cita-bibliografia",
        "Identidad institucional UnADM"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Consigna de actividad",
          "target": "Estructura argumentativa juridica",
          "kind": "depends_on",
          "justification": "El tipo de producto define secciones y profundidad."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica requiere respaldo documental."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia segura."
        },
        {
          "source": "Consistencia cita-bibliografia",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita referencias rotas y afirmaciones sin fuente."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Calidad editorial transversal",
          "kind": "develops",
          "justification": "Estandariza tono, formato y trazabilidad entre actividades."
        }
      ],
      "evidence": [
        "README destino: ubicacion curricular, estructura y pauta editorial.",
        "Programa analitico destino: proposito y ejes de trabajo.",
        "bases-de-derecho-internacional-publico.bib: fuentes institucionales base.",
        "Memoria origen: gates de parseo, normalizacion y patron argumentativo reusable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 69: se integran reglas transversales estables desde actividad no equivalente sin arrastrar contenido tematico.",
      "Ciclo 69: se mantiene union-dedupe y no regresion de reglas utiles previas.",
      "Ciclo 69: se refuerza gate de JSON parseable como prerequisito de propagacion recursiva."
    ]
  }
}