{
  "summary": [
    "Se sincroniza memoria transversal con abstracciones estables desde actividad de origen.",
    "Se preserva identidad UnADM y contexto curricular local del destino.",
    "Se refuerza normalizacion estructurada obligatoria antes de propagacion recursiva.",
    "Se consolidan ejes reutilizables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene estrategia conservadora: sin traslado de contenido tematico especifico de Filosofia del Derecho.",
    "Se incorpora mejora verificable: reparar tokens sin expandir y nombres anómalos en README/programa."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local: Bases de derecho internacional publico.",
    "Usar contexto curricular verificado del destino: semestre 4, bloque 1, obligatoria, 8 creditos.",
    "No mezclar metadatos curriculares entre materias.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como procedencia provisional, no como identidad."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeacion semanal.",
    "Distinguir reporte, presentacion y producto visual segun consigna.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, argumentos, normas y criterio propio.",
    "No extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Validar sintaxis LaTeX, cierre de entornos y referencias sin ruptura antes de compilar.",
    "Verificar correspondencia del producto con la consigna de la actividad activa."
  ],
  "latex_rules": [
    "Reutilizar plantilla .tex local sin romper identidad institucional.",
    "Mantener compatibilidad con clase article, spanish, letterpaper y oneside.",
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo con caracteres anómalos antes de referenciarlos.",
    "Reparar cierre de entornos tabular truncados en plantillas antes de compilar."
  ],
  "bibliography_rules": [
    "Registrar fuentes de actividad en bases-de-derecho-internacional-publico.bib.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Validar que toda clave citada exista en el .bib local."
  ],
  "propagation_hints": [
    "Propagar solo reglas generales estables entre nodos no equivalentes.",
    "Evitar traslado de contenido tematico propio de la materia origen.",
    "Mantener compresion lossless por union y deduplicacion.",
    "No eliminar reglas utiles previas; solo consolidar y reforzar.",
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Conservar incidencias historicas de parseo como control de calidad."
  ],
  "open_questions": [
    "Confirmar criterio editorial final sobre publico sin acento vs público con acento en nombres visibles.",
    "Confirmar si se normalizan de inmediato tokens $(@{...}.Slug) en README y programa.",
    "Confirmar cierre completo del entorno tabular en reporte-bases-de-derecho-internacional-publico.tex.",
    "Supuesto: no hay consigna de actividad especifica del destino en este ciclo.",
    "Confirmar formato minimo de conclusion juridica por tipo de evidencia en la materia destino."
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
        "Destino verificado: semestre 4, bloque 1, obligatoria, 8 creditos.",
        "Asignatura: Bases de derecho internacional publico."
      ]
    },
    "essence": [
      "Problema juridico o social que activa la asignatura.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion transferible a la practica juridica."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos con fundamento juridico y evidencia.",
      "Asegurar consistencia entre consigna, desarrollo y cierre argumentativo.",
      "Preservar trazabilidad editorial y calidad tecnica de artefactos LaTeX/BibTeX."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales sin redundancia.",
      "Supuestos etiquetados cuando falte evidencia local.",
      "Cierre con criterio juridico aplicable."
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
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo valido no hay transferencia segura."
        },
        {
          "source": "Consistencia cita-bibliografia",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita afirmaciones sin fuente y referencias rotas."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura argumentativa juridica",
          "kind": "develops",
          "justification": "La identidad se expresa en tono, formato y rigor argumentativo."
        }
      ],
      "evidence": [
        "README destino: ubicacion curricular y pauta editorial.",
        "Programa analitico destino: proposito y ejes de trabajo.",
        "bases-de-derecho-internacional-publico.bib: fuentes institucionales base.",
        "Plantilla .tex destino: metadatos y estructura tecnica a validar."
      ]
    },
    "reinforcement_log": [
      "Ciclo 81: se transfirieron solo abstracciones estables del origen transversal.",
      "Ciclo 81: se preservaron reglas previas utiles sin regresion.",
      "Ciclo 81: se reforzaron gates de parseo JSON y normalizacion estructurada.",
      "Ciclo 81: se agrego mejora verificable sobre tokens Slug no expandidos y nombres anómalos.",
      "Ciclo 81: se mantuvo separacion entre identidad editorial y procedencia provisional."
    ]
  }
}