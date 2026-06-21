{
  "summary": [
    "Se sincroniza memoria transversal desde actividad de Filosofía del Derecho hacia materia de Bases de derecho internacional publico con estrategia conservadora.",
    "Se preservan reglas estables reutilizables: identidad UnADM, estructura argumentativa, evidencia verificable, postura propia y conclusión jurídica transferible.",
    "Se refuerza normalización estructurada obligatoria antes de propagación recursiva.",
    "Se evita transferencia de contenido temático específico del origen por no equivalencia de nodos.",
    "Se mantiene compresión lossless por unión y deduplicación sin regresión."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local de la materia: Bases de derecho internacional publico.",
    "Usar contexto curricular verificado del destino: semestre 4, bloque 1, obligatoria, 8 creditos.",
    "No mezclar metadatos curriculares entre materias distintas.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como procedencia provisional, no como identidad del entregable."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como entrada canonica.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear cada entrega al producto solicitado en la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante y evitar resumen solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, normas, argumentos y criterio propio.",
    "No extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna local de actividad."
  ],
  "latex_rules": [
    "Reutilizar plantillas .tex locales de la materia sin romper identidad institucional.",
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo con caracteres anomalos antes de referenciarlos."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas de cada actividad en bases-de-derecho-internacional-publico.bib.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Validar que toda clave citada exista en el .bib local."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables en saltos transversales no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "No propagar redaccion literal ni contenido tematico especifico del origen.",
    "Preservar reglas utiles previas aunque se reubiquen por categoria.",
    "No convertir supuestos en reglas definitivas sin verificacion local.",
    "Aplicar compresion union-dedupe con criterio lossless en cada ciclo."
  ],
  "open_questions": [
    "Confirmar criterio editorial final para publico sin acento frente a publico con acento.",
    "Confirmar correccion en README de rutas con caracteres anomalos y lineas truncadas.",
    "Confirmar resolucion de tokens $(@{...}.Slug) en README y programa analitico.",
    "Confirmar cierre correcto del entorno tabular en reporte-bases-de-derecho-internacional-publico.tex.",
    "Supuesto: no hay consigna local de actividad especifica en este nodo de materia."
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
        "Semestre 4, bloque 1, obligatoria, 8 creditos.",
        "Asignatura: Bases de derecho internacional publico."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo pertinente.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar la planeacion semanal en entregables juridicos claros, sustentados y aplicables.",
      "Mantener continuidad editorial institucional entre actividades, materia y propagacion recursiva."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales sin redundancia.",
      "Supuestos etiquetados.",
      "Cierre con criterio juridico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> norma/doctrina -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> postura propia.",
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
        "Consistencia cita-bibliografia"
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
          "justification": "La forma del entregable depende del producto solicitado."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica valida requiere respaldo comprobable."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Consistencia cita-bibliografia",
          "kind": "supports",
          "justification": "La estructura valida facilita auditoria editorial y trazabilidad."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura argumentativa juridica",
          "kind": "develops",
          "justification": "La identidad define tono, formato y estandar academico."
        }
      ],
      "evidence": [
        "README de la materia destino: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico destino: proposito y ejes de trabajo.",
        "bases-de-derecho-internacional-publico.bib: fuentes institucionales base.",
        "Regla transversal consolidada: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 56: se reforzo gate de JSON parseable como condicion de propagacion recursiva.",
      "Ciclo 56: se consolidaron ejes editoriales transferibles sin mover contenido tematico de Filosofia del Derecho.",
      "Ciclo 56: se incorporo control de supuestos como requisito de integridad editorial.",
      "Ciclo 56: se reforzo higiene LaTeX en tokens sin expandir y rutas con caracteres anomalos."
    ]
  }
}