{
  "summary": [
    "Se sincroniza ADN editorial transversal desde actividad de Filosofia del Derecho hacia materia de Derecho financiero y bancario.",
    "Se preservan reglas institucionales validas de UnADM sin regresion.",
    "Se deduplican reglas por union semantica con compresion lossless.",
    "Se transfieren solo abstracciones estables: identidad, estructura reusable, gates y grafo conceptual.",
    "Se mantienen vacios de contexto local como preguntas abiertas con marca de supuesto."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Vincular entregas a Licenciatura en Derecho y datos curriculares locales verificados.",
    "Usar la carpeta de la materia como entrada canonica.",
    "Marcar como supuesto cualquier dato no visible en la consigna o no confirmado.",
    "Tratar fuentes heredadas de motor como provisionales hasta verificacion local.",
    "Sostener integridad academica con citas verificables."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener coherencia entre README, programa analitico, .tex y .bib."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar asumir fuentes o instrucciones de semanas distintas.",
    "Confirmar que el producto final corresponde a la consigna vigente."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar cualquier respuesta no estructurada antes de reutilizar.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar trazabilidad de cada regla a contexto local o memoria heredada.",
    "Bloquear si hay campos obligatorios vacios sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Evitar duplicados semanticos antes de guardar memoria."
  ],
  "latex_rules": [
    "Usar espanol con acentos correctos en .tex y .bib.",
    "Mantener documentclass y macros institucionales salvo instruccion contraria.",
    "Sincronizar titulo, subtitulo y materia con la actividad real.",
    "Reemplazar tokens de plantilla sin expandir en README y programa analitico.",
    "Usar slug literal derecho-financiero-y-bancario.bib como archivo canonico.",
    "Completar campos pendientes con dato real o etiqueta explicita de supuesto.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias ni metadatos.",
    "Registrar fuentes especificas por actividad en el .bib canonico de la materia.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Incluir fecha de consulta en referencias web.",
    "Distinguir bibliografia base de bibliografia especifica de actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y deduplicadas.",
    "Compartir lateralmente solo abstracciones editoriales estables.",
    "Evitar transferir redaccion literal de actividades no equivalentes.",
    "Aplicar estrategia progresiva y conservadora: agregar mejoras verificables sin borrar reglas utiles.",
    "Si reaparece salida no estructurada, aplicar normalizacion manual antes del siguiente ciclo."
  ],
  "open_questions": [
    "Confirmar formato de citacion obligatorio en Derecho financiero y bancario. [Supuesto: no definido]",
    "Confirmar figura docente y grupo para portada. [Supuesto: pendiente]",
    "Confirmar planeacion semanal vigente antes de generar actividades nuevas. [Supuesto: no disponible]",
    "Validar si la localizacion institucional de portada debe actualizarse por lineamiento oficial. [Supuesto: se mantiene]"
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
        "Entrada canonica por carpeta de materia."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura destino: Derecho financiero y bancario.",
        "Semestre 3, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos con fundamento juridico, evidencia y criterio propio.",
      "Estandarizar calidad editorial transversal entre nodos de la suite LaTeX."
    ],
    "style_markers": [
      "Frases directas y verificables.",
      "Supuestos marcados de forma explicita.",
      "No inventar fuentes.",
      "Consistencia entre narrativa, citas y estructura."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Marco conceptual y normativo delimitado.",
      "Analisis propio con soporte de evidencia.",
      "Cierre con implicacion practica juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Evidencia verificable",
        "Analisis juridico propio",
        "Conclusion transferible",
        "Normalizacion estructurada",
        "Consistencia .tex-.bib"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La identidad institucional exige trazabilidad y citas verificables."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin JSON parseable no hay transferencia segura de memoria."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis juridico propio",
          "kind": "develops",
          "justification": "El problema delimita el eje argumentativo del desarrollo."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion profesional debe derivar de fuentes comprobables."
        }
      ],
      "evidence": [
        "README de materia: pauta editorial y ubicacion curricular.",
        "Programa analitico: ejes de trabajo y proposito de realizacion.",
        "derecho-financiero-y-bancario.bib: fuentes base institucionales."
      ]
    },
    "reinforcement_log": [
      "Se reforzo regla de normalizacion JSON como gate critico transversal.",
      "Se reforzo flujo argumentativo reusable problema-conceptos-evidencia-analisis-conclusion.",
      "Se reforzo uso canonico de derecho-financiero-y-bancario.bib.",
      "Se mantuvieron supuestos abiertos donde falta contexto local verificable."
    ]
  }
}