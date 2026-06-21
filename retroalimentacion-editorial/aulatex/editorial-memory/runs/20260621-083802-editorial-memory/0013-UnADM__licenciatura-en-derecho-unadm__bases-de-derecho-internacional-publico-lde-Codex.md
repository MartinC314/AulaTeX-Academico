{
  "summary": [
    "Se refuerza sincronizacion transversal conservadora entre actividad y materia sin trasladar contenido tematico de Filosofia del Derecho.",
    "Se preserva identidad UnADM y contexto curricular local del destino: semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Se consolidan ejes editoriales estables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene normalizacion estructurada obligatoria antes de propagacion recursiva.",
    "Se integra control de supuestos: todo dato no visible en consigna se marca como supuesto."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local: Bases de derecho internacional publico.",
    "Alinear entregables a Licenciatura en Derecho, semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Tratar Codex y GPT-Pro como procedencia provisional, no como identidad del entregable.",
    "Marcar como supuesto cualquier dato no visible en la consigna local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeacion semanal.",
    "Conservar separacion entre reporte, presentacion, programa analitico y bibliografia.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, normas, argumentos y criterio propio.",
    "Evitar extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna de la actividad."
  ],
  "latex_rules": [
    "Reutilizar plantilla .tex local sin romper identidad institucional.",
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Mantener compatibilidad con clase article, spanish, letterpaper y oneside.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo con caracteres anomalos antes de compilar."
  ],
  "bibliography_rules": [
    "Registrar fuentes de actividad en bases-de-derecho-internacional-publico.bib.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente editorial o URL.",
    "Validar que las claves citadas existan en el .bib local.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Compartir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "No propagar supuestos como reglas definitivas.",
    "Evitar regresiones respecto de reglas utiles previas.",
    "Aplicar compresion lossless por union y deduplicacion.",
    "Si falta consigna local, propagar solo reglas generales verificables."
  ],
  "open_questions": [
    "Confirmar criterio editorial final sobre publico sin acento o publico con acento.",
    "Confirmar reparacion de tokens Slug sin expandir en README y programa analitico.",
    "Confirmar cierre correcto del entorno tabular en reporte-bases-de-derecho-internacional-publico.tex.",
    "Confirmar si se fija formato minimo de conclusion juridica por tipo de evidencia.",
    "Supuesto: no hay rubrica local detallada por actividad; confirmar cuando exista.",
    "Supuesto: curso mantiene LDE-S4B1 como codigo oficial en todas las plantillas."
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
        "Asignatura: Bases de derecho internacional publico."
      ]
    },
    "essence": [
      "Consigna determina forma del entregable.",
      "Problema activa analisis juridico.",
      "Evidencia verificable sostiene postura propia.",
      "Conclusion debe ser transferible a practica juridica.",
      "Normalizacion estructurada habilita memoria reutilizable."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables y utiles.",
      "Asegurar consistencia institucional, argumentativa y tecnica en cada entrega.",
      "Permitir propagacion transversal segura sin contaminar con contenido no equivalente."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales sin redundancia.",
      "Supuestos etiquetados de forma visible.",
      "Cierre con criterio juridico aplicable.",
      "Rastreabilidad de fuentes y claves BibTeX."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> norma/doctrina -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> posicion propia.",
      "Consigna -> desarrollo alineado -> verificacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Consigna de actividad",
        "Estructura argumentativa juridica",
        "Evidencia verificable",
        "Conclusion transferible",
        "Normalizacion JSON",
        "Consistencia cita-bibliografia",
        "Control de supuestos"
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
          "justification": "El producto define forma, extension y secciones."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "Sin respaldo documental no hay cierre juridico solido."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Control de supuestos",
          "kind": "supports",
          "justification": "Estructura explicita evita mezclar hechos con inferencias."
        },
        {
          "source": "Consistencia cita-bibliografia",
          "target": "Identidad institucional UnADM",
          "kind": "supports",
          "justification": "La integridad academica es rasgo institucional obligatorio."
        },
        {
          "source": "Control de supuestos",
          "target": "Estructura argumentativa juridica",
          "kind": "develops",
          "justification": "Mejora precision y transparencia del razonamiento."
        }
      ],
      "evidence": [
        "README destino: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico destino: proposito y ejes de trabajo.",
        "bases-de-derecho-internacional-publico.bib: claves institucionales base.",
        "Memoria origen: regla estable de normalizacion estructurada previa a propagacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 13: se deduplican reglas repetidas sin perdida semantica.",
      "Ciclo 13: se transfiere patron argumentativo general, no contenido tematico de Filosofia del Derecho.",
      "Ciclo 13: se refuerza gate de JSON parseable como condicion de propagacion recursiva.",
      "Ciclo 13: se añade control explicito de supuestos para datos no visibles en consigna.",
      "Ciclo 13: se refuerza correccion de tokens Slug sin expandir como riesgo tecnico transversal."
    ]
  }
}