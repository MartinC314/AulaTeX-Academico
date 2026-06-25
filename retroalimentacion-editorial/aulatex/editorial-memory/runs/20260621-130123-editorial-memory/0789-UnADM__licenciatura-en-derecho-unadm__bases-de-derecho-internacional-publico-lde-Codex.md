{
  "summary": [
    "Se mantiene cerebro editorial de materia con identidad UnADM y contexto curricular local verificado.",
    "Se refuerza transferencia transversal de abstracciones estables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se conserva regla de normalizacion estructurada obligatoria antes de propagacion recursiva.",
    "Se evita traslado de contenido tematico especifico de Filosofia del Derecho por no equivalencia de nodos.",
    "Se detectan y conservan incidencias locales verificables: tokens sin expandir en README/programa y corte de entorno tabular en plantilla de reporte."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local: Bases de derecho internacional publico.",
    "Usar contexto curricular verificado del destino: semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Usar codigo de curso local LDE-S4B1 en metadatos.",
    "No mezclar metadatos curriculares del origen con el destino.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como procedencia provisional, no como autoridad editorial."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por la planeacion semanal.",
    "Distinguir reporte, presentacion y producto visual segun consigna.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Integrar normas, doctrina o datos pertinentes al caso de actividad.",
    "Evitar extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna de la actividad.",
    "Verificar consistencia entre README, programa analitico, .bib y plantillas locales."
  ],
  "latex_rules": [
    "Reutilizar plantilla .tex local sin romper identidad institucional.",
    "Mantener compatibilidad con article, spanish, letterpaper y oneside.",
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Corregir tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir caracteres anomalos en nombres de archivos listados en README.",
    "Reparar cierre de entornos tabular en reporte-bases-de-derecho-internacional-publico.tex."
  ],
  "bibliography_rules": [
    "Registrar fuentes de actividad en bases-de-derecho-internacional-publico.bib.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Validar que toda clave citada exista en el .bib local.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas, generales y no duplicadas.",
    "Aplicar compresion lossless por union-dedupe sin recorte semantico.",
    "Preservar reglas utiles previas y evitar regresiones.",
    "No propagar supuestos como reglas definitivas.",
    "Si falta contexto local, transferir solo identidad, estructura reusable, gates y grafo conceptual minimo."
  ],
  "open_questions": [
    "Confirmar criterio editorial final sobre publico vs publico con acento en nombres visibles.",
    "Confirmar reparacion de tokens $(@{...}.Slug) en README y programa analitico.",
    "Confirmar cierre completo del entorno tabular en la plantilla de reporte.",
    "Confirmar si existe rubrica local por actividad para modular profundidad argumentativa.",
    "Supuesto: no se incorporan fuentes tematicas de derecho internacional publico adicionales en este ciclo."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador ante evidencia incompleta."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada obligatoria antes de propagacion.",
        "Trazabilidad de fuentes provisionales sin convertirlas en autoridad."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Bases de derecho internacional publico.",
        "Semestre 4, bloque 1, obligatoria, 8 creditos.",
        "Codigo local: LDE-S4B1."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo/doctrinal pertinente.",
      "Evidencia verificable.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables juridicos claros, verificables y utiles para la practica.",
      "Mantener coherencia entre consigna, desarrollo, evidencia y cierre argumentativo."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales sin redundancia.",
      "Supuestos etiquetados de forma visible.",
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
          "justification": "La conclusion juridica valida requiere respaldo documental."
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
          "justification": "Evita afirmaciones sin fuente y referencias rotas."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura argumentativa juridica",
          "kind": "develops",
          "justification": "El formato y tono institucional guian la presentacion del argumento."
        }
      ],
      "evidence": [
        "README destino: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico destino: proposito y ejes de trabajo.",
        "Bib local destino: claves institucionales base.",
        "Regla heredada estable: bloquear propagacion si no hay JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 22: deduplicacion completa de reglas repetidas y variantes ortograficas.",
      "Ciclo 22: transferencia conservadora solo de abstracciones editoriales estables del origen.",
      "Ciclo 22: no se traslado contenido tematico especifico de Filosofia del Derecho al destino.",
      "Ciclo 22: se reforzaron gates de parseo JSON, respaldo de afirmaciones y consistencia cita-bib.",
      "Ciclo 22: se mantuvieron incidencias locales abiertas para correccion verificable."
    ]
  }
}