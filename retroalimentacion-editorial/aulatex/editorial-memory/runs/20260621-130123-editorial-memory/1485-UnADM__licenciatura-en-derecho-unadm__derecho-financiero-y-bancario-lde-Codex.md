{
  "summary": [
    "Sincronizacion transversal consolidada con compresion lossless por union-dedupe.",
    "Se preservan reglas utiles previas y se eliminan duplicados semanticos.",
    "Se transfieren solo abstracciones estables desde actividad origen hacia materia destino.",
    "Se refuerzan identidad UnADM, estructura reusable, gates de calidad y grafo conceptual.",
    "Se mantienen vacios locales con marca de supuesto y preguntas abiertas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar programa academico Licenciatura en Derecho en todo artefacto.",
    "Usar datos curriculares verificados del destino: semestre 3, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Conservar autoria y matricula locales ya verificadas en .tex.",
    "Marcar como supuesto todo dato no confirmado de docente, grupo o consigna.",
    "Tratar fuentes heredadas de motor como provisionales hasta verificacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener coherencia entre README, programa analitico, .tex y .bib."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar afirmaciones sin respaldo o sin marca de supuesto.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Adaptar reporte o presentacion segun consigna confirmada.",
    "No asumir fuentes de semanas distintas sin validacion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar toda salida no estructurada antes de reutilizar.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar trazabilidad de cada regla a contexto local o memoria heredada.",
    "Validar deduplicacion semantica antes de guardar memoria.",
    "Comprobar que toda mejora agregada sea verificable y sin fuentes inventadas.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Mantener documentclass article en spanish, letterpaper, oneside salvo instruccion contraria.",
    "Usar acentos y codificacion correcta en espanol en .tex y .bib.",
    "Reemplazar titulos de plantilla por titulos reales de actividad antes de entrega.",
    "Completar 'Figura docente' con dato real o etiqueta de supuesto.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Usar nombre canonico de .bib: derecho-financiero-y-bancario.bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas por actividad en derecho-financiero-y-bancario.bib.",
    "Mantener entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente o URL.",
    "Incluir fecha de consulta en referencias web.",
    "Distinguir bibliografia base de bibliografia especifica de actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Compartir lateralmente solo reglas independientes de actividad especifica.",
    "Evitar transferencia de redaccion literal entre nodos no equivalentes.",
    "Preservar no regresion: no eliminar reglas utiles previas.",
    "Aplicar normalizacion manual si reaparece salida no estructurada en ciclos siguientes."
  ],
  "open_questions": [
    "Confirmar nombre real de la figura docente.",
    "Confirmar si el grupo debe figurar en tabla de identificacion.",
    "Confirmar formato obligatorio de citacion para la materia. [Supuesto: no definido]",
    "Confirmar planeacion semanal vigente antes de generar actividades.",
    "Confirmar si la localizacion de portada debe mantenerse por lineamiento institucional."
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
        "Supuestos marcados de forma explicita."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho financiero y bancario.",
        "Semestre 3, bloque 2, obligatoria, 8 creditos.",
        "Fuente curricular institucional: malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Problema delimitado.",
      "Conceptos y norma pertinente.",
      "Evidencia verificable.",
      "Analisis juridico propio.",
      "Conclusion transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos solidos y verificables.",
      "Asegurar consistencia editorial transversal en la suite LaTeX.",
      "Proteger continuidad institucional sin regresion."
    ],
    "style_markers": [
      "Frases directas y accionables.",
      "Separacion clara entre descripcion y postura.",
      "Cierre con implicacion practica juridica.",
      "Sin fuentes inventadas."
    ],
    "argumentative_patterns": [
      "Problema inicial breve -> marco conceptual/normativo -> analisis propio -> conclusion practica.",
      "Objetivo explicito al inicio y verificacion de coherencia al cierre.",
      "Cada afirmacion relevante con respaldo o marca de supuesto."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Integridad academica",
        "Evidencia verificable",
        "Analisis juridico propio",
        "Conclusion transferible",
        "Consistencia .tex-.bib"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin JSON parseable no hay transferencia segura."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La identidad institucional exige trazabilidad y verificabilidad."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion profesional debe derivar de respaldo comprobable."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis juridico propio",
          "kind": "develops",
          "justification": "El problema delimita el eje argumentativo."
        }
      ],
      "evidence": [
        "README local: pauta editorial e identidad institucional.",
        "Programa analitico local: proposito y ejes de trabajo.",
        "derecho-financiero-y-bancario.bib: fuentes base institucionales.",
        "Regla historica: bloqueo por JSON no parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 20: deduplicacion semantica completada sin perdida de reglas utiles.",
      "Ciclo 20: se reforzo gate de JSON parseable como condicion de propagacion.",
      "Ciclo 20: se consolidaron ejes argumentativos transferibles entre materias.",
      "Ciclo 20: se mantuvieron vacios locales como preguntas abiertas con supuesto."
    ]
  }
}