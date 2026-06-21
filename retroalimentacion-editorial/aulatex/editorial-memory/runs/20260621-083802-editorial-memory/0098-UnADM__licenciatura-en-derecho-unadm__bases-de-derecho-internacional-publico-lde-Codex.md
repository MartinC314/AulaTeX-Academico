{
  "summary": [
    "Se mantiene memoria de materia con identidad UnADM y contexto curricular local verificado.",
    "Se refuerza transferencia transversal estable desde actividad origen sin mover contenido tematico propio de Filosofia del Derecho.",
    "Se consolidan ejes reutilizables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se preserva normalizacion estructurada obligatoria antes de propagacion recursiva.",
    "Se agrega incidencia tecnica local: README y programa analitico contienen token Slug sin expandir [supuesto verificado por contexto local].",
    "Se agrega incidencia tecnica local: archivo de reporte presenta corte de entorno tabular pendiente de reparacion [supuesto verificado por contexto local]."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local: Bases de derecho internacional publico.",
    "Alinear entregables a Licenciatura en Derecho, semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Usar codigo de curso LDE-S4B1 en metadatos.",
    "Usar carpeta de materia como entrada canonica.",
    "No mezclar metadatos curriculares del origen con el destino.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar Codex y GPT-Pro solo como procedencia provisional."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el desarrollo al producto solicitado por la planeacion semanal.",
    "Distinguir reporte, presentacion y producto visual segun consigna.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Conservar separacion entre README, programa analitico, .bib y plantillas .tex."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Integrar conceptos, normas, doctrina o datos pertinentes al caso.",
    "Evitar extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre consigna, programa analitico y entregable.",
    "Validar sintaxis LaTeX y cierre de entornos antes de compilar."
  ],
  "latex_rules": [
    "Reutilizar plantilla .tex local sin romper identidad institucional.",
    "Mantener compatibilidad con clase article, spanish, letterpaper y oneside.",
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Corregir tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir caracteres anomalos en nombres de archivo listados en README.",
    "Reparar cierre de entorno tabular en reporte-bases-de-derecho-internacional-publico.tex."
  ],
  "bibliography_rules": [
    "Registrar fuentes de actividad en bases-de-derecho-internacional-publico.bib.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Validar que toda clave citada exista en el .bib local.",
    "Conservar entradas institucionales base: unadmSitioWeb y unadmMallaDerecho2024."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas abstractas estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "No propagar redaccion literal ni contenido tematico especifico del origen.",
    "Mantener compresion lossless por union y deduplicacion.",
    "Preservar reglas utiles previas sin regresion.",
    "Propagar correcciones tecnicas locales solo tras verificar archivos afectados."
  ],
  "open_questions": [
    "Confirmar consigna real de la siguiente actividad del destino para ajustar profundidad.",
    "Confirmar criterio editorial final sobre publico sin acento frente a publico con acento.",
    "Confirmar si la nomenclatura con token Slug debe reemplazarse automaticamente en todo el nodo.",
    "Confirmar si el reporte base requiere plantilla de tabla de autor completa o simplificada."
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
      "Consigna orienta estructura.",
      "Evidencia sostiene conclusion.",
      "Analisis propio evita descriptivismo.",
      "Transferencia transversal conserva metodo, no temario."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos solidos y verificables.",
      "Garantizar coherencia juridica entre problema, fuentes, analisis y conclusion."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales no redundantes.",
      "Supuestos etiquetados.",
      "Cierre con criterio juridico aplicable."
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
        "Analisis propio",
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
          "justification": "El tipo de producto define forma y alcance del desarrollo."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica valida requiere respaldo documental."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Consistencia cita-bibliografia",
          "kind": "supports",
          "justification": "La estructura valida permite auditar trazabilidad editorial."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La postura argumentada conecta evidencia con aplicacion profesional."
        }
      ],
      "evidence": [
        "README destino confirma identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico destino confirma proposito y ejes de trabajo.",
        "Bib local contiene claves institucionales verificables.",
        "Contexto local muestra token Slug sin expandir en README/programa [supuesto].",
        "Contexto local muestra corte de entorno tabular en reporte .tex [supuesto]."
      ]
    },
    "reinforcement_log": [
      "Se refuerza regla transversal de normalizacion estructurada previa a propagacion.",
      "Se refuerza patron argumentativo comun sin transferir contenido tematico del origen.",
      "Se refuerzan quality gates de evidencia y trazabilidad bibliografica.",
      "Se agregan incidencias tecnicas locales verificables para correccion progresiva y conservadora."
    ]
  }
}