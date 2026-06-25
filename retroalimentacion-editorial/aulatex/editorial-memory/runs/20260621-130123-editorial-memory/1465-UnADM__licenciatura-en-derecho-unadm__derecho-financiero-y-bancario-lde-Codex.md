{
  "summary": [
    "Se consolida sincronizacion transversal desde actividad origen a materia destino sin regresion.",
    "Se preservan reglas institucionales UnADM, normalizacion JSON y compresion union-dedupe lossless.",
    "Se transfieren solo abstracciones estables: identidad, estructura reusable, gates y grafo conceptual.",
    "Se mantiene contexto curricular local de Derecho financiero y bancario: semestre 3, bloque 2, obligatoria, 8 creditos.",
    "Se conserva evidencia local de artefactos de plantilla en README y programa analitico con accion correctiva."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar Licenciatura en Derecho como programa academico del destino.",
    "Mantener datos curriculares verificados: semestre 3, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no confirmado en consigna local.",
    "Tratar fuentes heredadas de motor como provisionales hasta verificacion local.",
    "Conservar autoria y matricula segun .tex local salvo instruccion oficial contraria."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear producto al formato solicitado por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Mantener coherencia entre README, programa analitico, .tex y .bib.",
    "Corregir tokens de plantilla sin expandir en nombres de archivo documentados."
  ],
  "activity_rules": [
    "Delimitar problema inicial de cada actividad.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Separar descripcion conceptual de analisis propio.",
    "No asumir fuentes de semanas distintas sin confirmacion local.",
    "Adaptar artefacto a consigna real: reporte, presentacion u otro formato."
  ],
  "quality_gates": [
    "Bloquear propagacion si salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar cualquier respuesta no estructurada antes de reutilizar.",
    "Confirmar trazabilidad de cada regla a contexto local o memoria heredada.",
    "Bloquear guardado si hay campos obligatorios vacios sin marca de supuesto.",
    "Validar deduplicacion semantica previa a persistencia.",
    "Comprobar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Mantener documentclass article en spanish, letterpaper, oneside salvo instruccion contraria.",
    "Usar acentos y codificacion correcta en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Reemplazar titulo y subtitulo de plantilla por actividad real antes de entrega.",
    "Completar Figura docente con dato real o etiqueta [Supuesto].",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico."
  ],
  "bibliography_rules": [
    "Usar derecho-financiero-y-bancario.bib como archivo canonico de la materia.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias ni metadatos.",
    "Agregar entradas BibTeX solo con fuente consultable.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Incluir fecha de consulta en fuentes web.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas, parseables y deduplicadas.",
    "Compartir lateralmente solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Evitar transferencia de redaccion literal o contenido tematico exclusivo de Filosofia del Derecho.",
    "Mantener no regresion: no eliminar reglas utiles previas.",
    "Si reaparece salida no estructurada, aplicar normalizacion manual como contingencia.",
    "Etiquetar supuestos y origen de regla para auditoria transversal."
  ],
  "open_questions": [
    "Confirmar nombre real de figura docente en portada.",
    "Confirmar formato obligatorio de citacion de la materia [Supuesto: no definido].",
    "Confirmar si grupo debe aparecer en tabla de identificacion.",
    "Confirmar si localizacion institucional de portada debe actualizarse [Supuesto].",
    "Confirmar planeacion semanal vigente antes de generar actividades especificas.",
    "Confirmar si correccion de nombres en README sera manual o por regeneracion automatica."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Sobrio y verificable.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Trazabilidad documental entre README, programa, .tex y .bib.",
        "Supuestos marcados de forma explicita."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Derecho financiero y bancario.",
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
      "Convertir planeacion semanal en productos academicos solidos.",
      "Asegurar coherencia editorial institucional.",
      "Garantizar calidad argumentativa y verificabilidad de fuentes."
    ],
    "style_markers": [
      "Frases directas y auditables.",
      "Separacion clara entre hecho, analisis y conclusion.",
      "Marca explicita de supuestos.",
      "Consistencia entre narrativa y citas."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Marco conceptual-normativo delimitado.",
      "Analisis propio con evidencia.",
      "Cierre con implicacion practica juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
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
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion profesional debe derivar de fuentes comprobables."
        },
        {
          "source": "Problema juridico delimitado",
          "target": "Analisis juridico propio",
          "kind": "develops",
          "justification": "El problema define el eje argumentativo."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La identidad exige trazabilidad y rigor de citas."
        }
      ],
      "evidence": [
        "README local: pauta editorial y ubicacion curricular.",
        "Programa analitico local: proposito y ejes de trabajo.",
        "Bib local: unadmSitioWeb y unadmMallaDerecho2024.",
        "Memoria heredada: bloqueo por salida no parseable y normalizacion obligatoria."
      ]
    },
    "reinforcement_log": [
      "Ciclo 15: deduplicacion semantica aplicada sin eliminar reglas utiles.",
      "Ciclo 15: se reforzo gate de JSON parseable como condicion de propagacion.",
      "Ciclo 15: se mantuvo transferencia transversal solo en abstracciones estables.",
      "Ciclo 15: se conservaron vacios locales como preguntas abiertas marcadas [Supuesto]."
    ]
  }
}