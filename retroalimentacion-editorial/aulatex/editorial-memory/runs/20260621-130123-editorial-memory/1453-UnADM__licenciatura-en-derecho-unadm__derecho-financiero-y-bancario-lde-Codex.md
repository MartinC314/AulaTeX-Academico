{
  "summary": [
    "Se consolida sincronizacion transversal con compresion lossless por union-dedupe.",
    "Se preservan reglas utiles previas sin regresion y sin traslado literal entre nodos no equivalentes.",
    "Se refuerzan abstracciones estables: identidad UnADM, estructura reusable, calidad y trazabilidad.",
    "Se mantiene contexto local de Derecho financiero y bancario: semestre 3, bloque 2, obligatoria, 8 creditos.",
    "Se conserva alerta tecnica: hubo salidas no JSON parseable y se exige normalizacion previa."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Vincular todo producto a Licenciatura en Derecho y datos curriculares verificados del destino.",
    "Usar la carpeta de materia como entrada canonica editorial.",
    "Marcar como supuesto todo dato no confirmado de consigna, docente o grupo.",
    "Tratar fuentes heredadas de motor como provisionales hasta verificacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Mantener coherencia entre README, programa analitico, .tex y .bib."
  ],
  "activity_rules": [
    "Evitar entregas solo descriptivas.",
    "Incluir postura argumentada del estudiante.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir fuentes o materiales de semanas no confirmadas para la actividad."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar memoria.",
    "Confirmar trazabilidad de cada regla a contexto local o memoria heredada.",
    "Bloquear campos obligatorios vacios sin marca de supuesto.",
    "Validar deduplicacion semantica antes de guardar.",
    "No agregar mejoras sin respaldo verificable."
  ],
  "latex_rules": [
    "Mantener codificacion correcta de espanol en .tex y .bib.",
    "Mantener clase y opciones base salvo consigna contraria.",
    "Sincronizar titulo y subtitulo con actividad real antes de entrega.",
    "Completar campos pendientes de portada con dato real o etiqueta de supuesto.",
    "Resolver tokens de plantilla sin expandir en README, programa y rutas.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Usar derecho-financiero-y-bancario.bib como archivo canonico local.",
    "Priorizar fuentes institucionales UnADM y normativas verificables.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/URL.",
    "Incluir fecha de consulta en fuentes web.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y deduplicadas.",
    "Transferir solo abstracciones estables en saltos transversales.",
    "Evitar traslado de redaccion literal o contenido tematico exclusivo de Filosofia del Derecho.",
    "Mantener union-dedupe como mecanismo de compresion lossless.",
    "Aplicar normalizacion manual al detectar salida no estructurada."
  ],
  "open_questions": [
    "Confirmar figura docente real para portada.",
    "Confirmar formato obligatorio de citacion en la materia. [supuesto: no definido]",
    "Confirmar si grupo debe aparecer en tabla de identificacion.",
    "Confirmar planeacion semanal vigente antes de generar actividades concretas.",
    "Confirmar si la localizacion institucional de portada sigue vigente."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Sobrio, verificable y orientado a practica profesional."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Trazabilidad documental entre README, programa, .tex y .bib.",
        "No regresion de reglas utiles previas."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura destino: Derecho financiero y bancario.",
        "Semestre 3, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema delimitado.",
      "Conceptos y normas pertinentes.",
      "Evidencia verificable.",
      "Analisis juridico propio.",
      "Conclusion transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos consistentes y verificables.",
      "Sostener continuidad editorial institucional entre actividades y materias."
    ],
    "style_markers": [
      "Frases directas y accionables.",
      "Supuestos marcados de forma explicita.",
      "Sin fuentes inventadas.",
      "Consistencia entre narrativa, citas y estructura."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Marco conceptual y normativo delimitado.",
      "Analisis propio sustentado.",
      "Cierre con implicacion practica juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Evidencia verificable",
        "Analisis juridico propio",
        "Conclusion transferible",
        "Coherencia README-programa-.tex-.bib"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "La integridad institucional exige respaldo documental."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Coherencia README-programa-.tex-.bib",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay sincronizacion editorial segura."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion profesional debe derivar de fuentes comprobables."
        },
        {
          "source": "Problema delimitado",
          "target": "Analisis juridico propio",
          "kind": "develops",
          "justification": "El problema define el eje argumentativo del analisis."
        }
      ],
      "evidence": [
        "README local: pauta editorial e identidad UnADM.",
        "Programa analitico local: ejes de trabajo y proposito.",
        "Bib local: unadmSitioWeb y unadmMallaDerecho2024.",
        "Historial: salidas no JSON parseable requieren gate de normalizacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 12: se conserva ADN institucional y se deduplican reglas repetidas.",
      "Ciclo 12: se refuerzan gates de parseo JSON y trazabilidad.",
      "Ciclo 12: se mantiene transferencia transversal por abstracciones estables.",
      "Ciclo 12: se preservan vacios locales como preguntas abiertas con [supuesto]."
    ]
  }
}