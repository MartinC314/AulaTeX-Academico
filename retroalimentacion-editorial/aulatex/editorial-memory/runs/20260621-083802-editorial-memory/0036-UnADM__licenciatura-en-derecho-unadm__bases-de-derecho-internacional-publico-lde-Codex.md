{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre actividad y materia sin mezclar contenido tematico.",
    "Se preservan reglas utiles previas y se deduplican formulaciones equivalentes.",
    "Se refuerzan ejes estables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene bloqueo de propagacion para salidas no JSON parseable.",
    "Se incorpora incidencia local verificable: tokens sin expandir y nombres de archivo anómalos en README/programa."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local: Bases de derecho internacional publico.",
    "Alinear entregables a Licenciatura en Derecho, semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "No mezclar metadatos curriculares del origen con el destino.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como procedencia provisional, no como identidad del entregable."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear la estructura al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Distinguir reporte, presentacion y producto visual segun consigna."
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
    "Verificar correspondencia entre consigna, programa analitico y producto final."
  ],
  "latex_rules": [
    "Reutilizar plantilla .tex local sin romper identidad institucional.",
    "Mantener compatibilidad con article, spanish, letterpaper y oneside.",
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Mantener claves BibTeX estables.",
    "Corregir nombres de archivo anómalos en README.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: el .bib canonico local es bases-de-derecho-internacional-publico.bib."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas de actividad en bases-de-derecho-internacional-publico.bib.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Validar que toda clave citada exista en el .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales estables entre nodos no equivalentes.",
    "Aplicar compresion lossless por union y deduplicacion sin recorte semantico.",
    "Preservar reglas utiles previas aunque cambien de categoria.",
    "No propagar supuestos como hechos definitivos.",
    "Ejecutar normalizacion manual cuando reaparezca salida no estructurada.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual."
  ],
  "open_questions": [
    "Confirmar si se normaliza oficialmente publico/publico con acento en nombres editoriales.",
    "Confirmar correccion de rutas con caracteres anómalos en README.",
    "Confirmar eliminacion de tokens $(@{...}.Slug) en README y programa analitico.",
    "Confirmar rubrica local por actividad para calibrar profundidad argumentativa.",
    "Supuesto: no hay consigna de actividad concreta en este salto transversal."
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
        "No mezclar contexto curricular del origen con el destino."
      ]
    },
    "essence": [
      "Consigna guia la forma del producto.",
      "Argumentacion juridica con evidencia verificable.",
      "Analisis propio obligatorio.",
      "Conclusion transferible a practica juridica.",
      "Trazabilidad tecnica en JSON, LaTeX y bibliografia."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables juridicos consistentes.",
      "Garantizar calidad editorial reproducible entre actividades y materias.",
      "Mantener continuidad institucional sin contaminar contexto local."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales sin redundancia.",
      "Supuestos siempre etiquetados.",
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
        "Consistencia cita-bibliografia",
        "Trazabilidad de procedencia provisional"
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
          "justification": "El tipo de producto define la estructura final."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica valida requiere respaldo comprobable."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Trazabilidad de procedencia provisional",
          "kind": "supports",
          "justification": "Permite propagar memoria con control de calidad y origen."
        },
        {
          "source": "Consistencia cita-bibliografia",
          "target": "Evidencia verificable",
          "kind": "depends_on",
          "justification": "Sin claves validas no hay verificabilidad academica."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura argumentativa juridica",
          "kind": "develops",
          "justification": "La pauta institucional define tono y forma del desarrollo."
        }
      ],
      "evidence": [
        "README destino confirma contexto curricular y pauta editorial.",
        "Programa analitico destino define proposito y ejes de trabajo.",
        ".bib local contiene claves institucionales base verificables.",
        "Se detectan tokens sin expandir en README/programa; requiere normalizacion."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas entre origen y destino.",
      "Se conservaron quality gates historicos de parseo JSON.",
      "Se transfirieron solo abstracciones estables, no contenido tematico de Filosofia del Derecho.",
      "Se reforzo control de supuestos y procedencia provisional.",
      "Se añadieron mejoras verificables por contexto local: tokens sin expandir y rutas anómalas."
    ]
  }
}