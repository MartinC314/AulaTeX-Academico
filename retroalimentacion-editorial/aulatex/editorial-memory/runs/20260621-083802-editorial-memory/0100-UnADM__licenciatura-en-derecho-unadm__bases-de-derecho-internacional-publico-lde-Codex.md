{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre actividad origen y materia destino.",
    "Se preservan reglas utiles vigentes del destino y se refuerzan abstracciones estables del origen.",
    "Se mantiene politica de normalizacion estructurada obligatoria antes de propagacion recursiva.",
    "Se transfiere patron editorial reusable: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se evita traslado de contenido tematico especifico de Filosofia del Derecho al destino de Derecho Internacional Publico.",
    "Se detectan tokens sin expandir y caracteres anómalos en README/programa; se marcan como pendientes tecnicos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local de la materia destino.",
    "Usar contexto curricular verificado del destino: semestre 4, bloque 1, obligatoria, 8 creditos.",
    "No mezclar metadatos curriculares entre materias no equivalentes.",
    "Usar la carpeta de materia como entrada canonica.",
    "Tratar fuentes heredadas no verificadas como procedencia provisional.",
    "Marcar como supuesto todo dato no visible en consigna local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear cada entrega al producto solicitado en planeacion semanal.",
    "Distinguir reporte, presentacion y producto visual segun consigna.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar resumen solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, normas, argumentos y criterio propio.",
    "Evitar extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre consigna, producto y programa analitico local."
  ],
  "latex_rules": [
    "Reutilizar plantillas .tex locales sin romper identidad institucional.",
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Corregir caracteres anómalos en nombres/rutas antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas de actividad en el .bib local de la materia.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Validar que cada clave citada exista en el .bib local."
  ],
  "propagation_hints": [
    "Propagar solo reglas generales estables entre nodos no equivalentes.",
    "Aplicar compresion lossless por union-dedupe sin recorte semantico.",
    "Preservar reglas utiles previas y evitar regresiones.",
    "No propagar supuestos como reglas definitivas.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Ejecutar propagacion recursiva solo tras validacion JSON y estructura."
  ],
  "open_questions": [
    "Confirmar criterio editorial final sobre publico/publico con acento en nombres visibles. [supuesto]",
    "Confirmar correccion de tokens $(@{...}.Slug) en README y programa analitico local.",
    "Confirmar reparacion del corte de entorno tabular en plantilla de reporte .tex.",
    "Confirmar si existe rubrica especifica por actividad para ajustar profundidad argumentativa. [supuesto]",
    "Confirmar si la materia requiere reglas adicionales por tipo de evidencia internacional publica. [supuesto]"
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
      "Consigna primero.",
      "Estructura argumentativa juridica estable.",
      "Evidencia verificable.",
      "Postura propia sustentada.",
      "Conclusion transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables claros, verificables y juridicamente utiles.",
      "Sostener continuidad editorial entre actividades y materias sin contaminar contextos."
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
        "Analisis propio",
        "Conclusion juridica transferible",
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
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida exige respaldo documental."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Sincronizacion transversal",
          "kind": "depends_on",
          "justification": "Sin parseo valido no hay propagacion segura."
        },
        {
          "source": "Consistencia cita-bibliografia",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita referencias rotas y afirmaciones sin fuente."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura argumentativa juridica",
          "kind": "develops",
          "justification": "La forma editorial institucional orienta la redaccion academica."
        }
      ],
      "evidence": [
        "README destino: ubicacion curricular y pauta editorial.",
        "Programa analitico destino: proposito y ejes de trabajo.",
        "Bibliografia local destino: claves institucionales existentes.",
        "Memoria origen: regla de normalizacion estructurada y ejes editoriales transferibles."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas y se conservaron todas las utiles.",
      "Se reforzo gate de JSON parseable como condicion de propagacion recursiva.",
      "Se mantuvo estrategia conservadora: sin traslado de contenido tematico especifico del origen.",
      "Se incorporo alerta tecnica por tokens sin expandir y caracteres anómalos.",
      "Se consolido patron argumentativo transversal reusable en la materia destino."
    ]
  }
}