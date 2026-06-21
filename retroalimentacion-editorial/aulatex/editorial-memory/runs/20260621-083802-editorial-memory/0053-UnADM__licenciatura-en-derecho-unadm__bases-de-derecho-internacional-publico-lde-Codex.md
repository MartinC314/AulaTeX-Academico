{
  "summary": [
    "Se consolida sincronizacion transversal con reglas estables y deduplicadas.",
    "Se preserva identidad UnADM y contexto curricular local del destino.",
    "Se refuerza normalizacion estructurada obligatoria antes de propagacion recursiva.",
    "Se transfieren ejes reutilizables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se evita traslado de contenido tematico especifico de Filosofia del Derecho por ser nodo no equivalente.",
    "Se incorpora correccion de incidencias locales verificables: tokens sin expandir y rutas con caracteres anómalos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local: Bases de derecho internacional publico.",
    "Usar contexto curricular verificado del destino: semestre 4, bloque 1, obligatoria, 8 creditos.",
    "No mezclar metadatos curriculares entre materias.",
    "Usar la carpeta de materia como entrada canonica.",
    "Tratar Codex y GPT-Pro como procedencia provisional, no como identidad del entregable.",
    "Marcar como supuesto cualquier dato no visible en la consigna local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Distinguir reporte, presentacion y producto visual segun consigna.",
    "Conservar separacion entre README, programa analitico, .bib y plantillas .tex."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, argumentos, normas y criterio propio.",
    "Evitar extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna de la actividad vigente.",
    "Mantener auditoria de parseo JSON antes de nueva propagacion."
  ],
  "latex_rules": [
    "Reutilizar plantilla .tex local sin romper identidad institucional.",
    "Mantener compatibilidad con article, spanish, letterpaper y oneside.",
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Cerrar correctamente entornos LaTeX antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres/rutas con caracteres anómalos antes de referenciar archivos."
  ],
  "bibliography_rules": [
    "Registrar fuentes de actividad en bases-de-derecho-internacional-publico.bib.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente editorial o URL.",
    "Validar que toda clave citada exista en el .bib local.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables en saltos transversales.",
    "No propagar contenido tematico especifico del nodo origen a materia no equivalente.",
    "Aplicar union-dedupe lossless y evitar regresiones.",
    "Preservar reglas utiles previas aunque cambien de categoria.",
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "No promover supuestos a reglas definitivas sin verificacion local."
  ],
  "open_questions": [
    "Confirmar criterio editorial final: publico vs público en nombres visibles. [supuesto]",
    "Confirmar correccion definitiva de tokens $(@{...}.Slug) en README y programa analitico.",
    "Confirmar reparacion completa del entorno tabular truncado en reporte .tex.",
    "Confirmar rubrica local por actividad para ajustar profundidad argumentativa. [supuesto]"
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
      "Consigna valida la forma del entregable.",
      "Evidencia valida la conclusion juridica.",
      "Analisis propio convierte informacion en criterio profesional.",
      "Estructura estable mejora trazabilidad editorial."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos verificables y transferibles.",
      "Asegurar coherencia entre identidad institucional, argumento juridico y soporte documental."
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
          "justification": "El producto define forma y alcance del desarrollo."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "Sin soporte documental no hay cierre juridico solido."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Consistencia cita-bibliografia",
          "kind": "develops",
          "justification": "La estructura valida permite control de calidad automatizable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La postura razonada conecta teoria con practica profesional."
        }
      ],
      "evidence": [
        "README destino: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico destino: proposito y ejes de trabajo.",
        "Archivo .bib destino: claves institucionales base.",
        "Incidencias locales verificadas: token Slug sin expandir y rutas con caracteres anómalos."
      ]
    },
    "reinforcement_log": [
      "Ciclo 53: se refuerza gate de JSON parseable y normalizacion previa.",
      "Ciclo 53: se consolidan ejes transversales sin importar tematica origen.",
      "Ciclo 53: se mantiene estrategia conservadora y sin regresion.",
      "Ciclo 53: se priorizan correcciones locales verificables en README/programa/.tex."
    ]
  }
}