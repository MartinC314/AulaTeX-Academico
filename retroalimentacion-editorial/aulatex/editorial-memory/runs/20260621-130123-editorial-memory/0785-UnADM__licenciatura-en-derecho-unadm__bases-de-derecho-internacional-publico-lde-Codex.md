{
  "summary": [
    "Se consolida sincronizacion transversal conservadora desde actividad de Filosofia del Derecho hacia materia de Bases de Derecho Internacional Publico.",
    "Se preservan reglas utiles previas del destino y se agregan solo abstracciones estables reutilizables.",
    "Se refuerza normalizacion estructurada obligatoria antes de propagacion recursiva.",
    "Se mantiene separacion entre identidad curricular local y trazabilidad de fuentes provisionales.",
    "Se detectan tokens sin expandir y caracteres anómalos en README/programa; se mantienen como incidencia abierta."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local de la materia en destino.",
    "Usar contexto curricular verificado del destino: semestre 4, bloque 1, obligatoria, 8 creditos.",
    "No mezclar metadatos curriculares entre materias origen y destino.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar Codex/GPT-Pro como procedencia provisional, no como autoridad editorial."
  ],
  "structure_rules": [
    "Usar carpeta de materia como entrada canonica.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el entregable al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, normas, argumentos y criterio propio.",
    "No extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar memoria.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Verificar correspondencia entre consigna, programa analitico y producto entregado."
  ],
  "latex_rules": [
    "Reutilizar plantilla .tex local sin romper identidad institucional.",
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir caracteres anómalos en nombres de archivo antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas por actividad en el .bib local de la materia.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Validar que toda clave citada exista en el .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales verificadas y no duplicadas.",
    "Aplicar compresion lossless por union-dedupe sin recorte de reglas utiles.",
    "No propagar contenido tematico especifico de Filosofia del Derecho a materia no equivalente.",
    "Preservar incidencias historicas de parseo como memoria operativa.",
    "Si falta contexto local, crear cerebro minimo y abrir preguntas en lugar de inventar."
  ],
  "open_questions": [
    "Confirmar criterio final de acentuacion en nombre publico/público para archivos y metadatos.",
    "Confirmar normalizacion de tokens $(@{...}.Slug) en README y programa analitico.",
    "Confirmar reparacion del corte de entorno tabular en plantilla de reporte.",
    "Supuesto: la consigna de actividades futuras seguira estructura reporte/presentacion segun planeacion.",
    "Confirmar si existen fuentes obligatorias adicionales para esta materia no registradas en el .bib local."
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
        "Destino verificado: semestre 4, bloque 1, obligatoria, 8 creditos.",
        "Asignatura destino: Bases de derecho internacional publico.",
        "Codigo local: LDE-S4B1."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas o doctrina pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar la planeacion semanal en productos academicos claros, fundamentados y verificables.",
      "Sostener coherencia entre consigna, estructura argumentativa y evidencia."
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
          "justification": "La conclusion juridica valida requiere respaldo documental."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Consistencia cita-bibliografia",
          "kind": "supports",
          "justification": "La estructura valida permite controles de calidad reproducibles."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura argumentativa juridica",
          "kind": "develops",
          "justification": "La identidad institucional define el marco formal de redaccion."
        }
      ],
      "evidence": [
        "README destino: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico destino: proposito y ejes de trabajo.",
        "Bib local destino: claves institucionales base existentes.",
        "Memoria origen: gates de parseo, supuestos etiquetados y estructura argumentativa reusable."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin perdida semantica.",
      "Se reforzaron gates de parseo JSON y consistencia cita-bibliografia.",
      "Se mantuvo estrategia transversal conservadora sin traslado tematico indebito.",
      "Se conservaron incidencias historicas y se marcaron vacios como preguntas abiertas."
    ]
  }
}