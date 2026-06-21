{
  "summary": [
    "Se consolida sincronizacion transversal con reglas estables y sin regresion.",
    "Se preserva identidad UnADM y contexto curricular local del destino.",
    "Se refuerza normalizacion JSON obligatoria antes de propagacion recursiva.",
    "Se transfieren ejes reutilizables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se evita traslado de contenido tematico especifico de Filosofia del Derecho.",
    "Se agrega correccion verificable: tokens Slug sin expandir en README y programa analitico del destino.",
    "Se agrega correccion verificable: nombres de archivo con caracter inicial anomalo en README del destino.",
    "Se mantiene estrategia progresiva y conservadora con compresion union-dedupe lossless."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local de la materia en todos los entregables.",
    "Alinear entregables al contexto curricular verificado del destino: semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como procedencia provisional, no como identidad.",
    "No mezclar metadatos curriculares entre materias origen y destino."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear estructura al producto solicitado por la planeacion semanal.",
    "Distinguir reporte, presentacion y producto visual segun consigna.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Conservar separacion entre README, programa analitico, .bib y plantillas .tex."
  ],
  "activity_rules": [
    "Adaptar cada actividad al producto exacto solicitado.",
    "Incluir postura argumentada del estudiante y evitar solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, normas, doctrina, argumentos y criterio propio.",
    "No extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregado y consigna local.",
    "Verificar consistencia entre README, programa analitico, .bib y plantillas."
  ],
  "latex_rules": [
    "Reutilizar plantilla .tex local sin romper identidad institucional.",
    "Mantener compatibilidad con clase article, spanish, letterpaper y oneside.",
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Revisar y cerrar entornos tabular antes de compilar.",
    "Corregir nombres de archivo anómalos en README antes de referenciar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico."
  ],
  "bibliography_rules": [
    "Registrar fuentes de actividad en el .bib local de la materia.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Validar que toda clave citada exista en el .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas y no duplicadas.",
    "Aplicar compresion lossless por union-dedupe sin recorte semantico.",
    "Preservar reglas utiles previas aunque cambien de categoria.",
    "No propagar supuestos como reglas definitivas.",
    "Mantener incidencias historicas de salida no estructurada como control de calidad.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual en saltos transversales."
  ],
  "open_questions": [
    "Confirmar criterio editorial final sobre uso de publico/publico con acento en nombre visible de la materia.",
    "Confirmar si el destino requiere plantilla adicional para productos visuales distintos de reporte y presentacion.",
    "Confirmar si existe rubrica local por actividad para ajustar profundidad argumentativa.",
    "Supuesto: la correccion de tokens Slug en README y programa analitico aun esta pendiente de aplicacion en archivos.",
    "Supuesto: el entorno tabular del reporte .tex local sigue truncado y requiere reparacion tecnica."
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
        "No mezclar contexto curricular con materias origen."
      ]
    },
    "essence": [
      "Consigna local como eje.",
      "Problema, conceptos, evidencia, analisis y conclusion.",
      "Trazabilidad verificable en JSON, LaTeX y bibliografia."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables juridicos claros y verificables.",
      "Asegurar calidad editorial reproducible en propagacion transversal.",
      "Mantener continuidad institucional sin contaminar contexto tematico entre materias."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales sin redundancia.",
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
        "Conclusion juridica transferible",
        "Normalizacion JSON",
        "Consistencia cita-bibliografia",
        "Integridad de plantillas LaTeX"
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
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida requiere respaldo documental."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Sincronizacion transversal",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay propagacion segura."
        },
        {
          "source": "Consistencia cita-bibliografia",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita afirmaciones sin fuente y claves rotas."
        },
        {
          "source": "Integridad de plantillas LaTeX",
          "target": "Calidad de entrega",
          "kind": "supports",
          "justification": "Compilacion estable reduce errores editoriales."
        }
      ],
      "evidence": [
        "README destino: contexto curricular y pauta editorial.",
        "Programa analitico destino: proposito y ejes de trabajo.",
        "bases-de-derecho-internacional-publico.bib: claves institucionales base.",
        "Deteccion verificable de tokens $(@{...}.Slug) sin expandir en README y programa analitico.",
        "Deteccion verificable de nombres de archivo con caracter inicial anomalo en README.",
        "Incidencias historicas: salidas no parseables en ciclos previos."
      ]
    },
    "reinforcement_log": [
      "Ciclo 73: deduplicacion completa de reglas repetidas en origen y destino.",
      "Ciclo 73: preservadas reglas institucionales y gates historicos sin eliminaciones utiles.",
      "Ciclo 73: reforzada regla transversal de no mezclar metadatos curriculares entre materias.",
      "Ciclo 73: añadidas mejoras verificables de higiene editorial en README/programa (tokens y nombres anómalos).",
      "Ciclo 73: mantenida estrategia conservadora, sin transferir contenido doctrinal especifico del origen."
    ]
  }
}