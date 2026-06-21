{
  "summary": [
    "Se refuerza actividad-2 con patrones reutilizables validados desde actividad-1.",
    "Se mantiene compresion lossless por union y deduplicacion sin recorte.",
    "Se conserva identidad UnADM, estructura argumentativa y controles de calidad.",
    "Se evita transferir conclusiones o bibliografia exclusiva del hermano.",
    "Se mantiene normalizacion obligatoria antes de propagacion recursiva."
  ],
  "identity_rules": [
    "Mantener tono institucional UnADM en redaccion y formato.",
    "Anclar la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato al producto solicitado en la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Ajustar actividad-2 a instruccion docente disponible.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir tema, semana o formato sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que cada afirmacion sustantiva tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar compilaciones rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Confirmar nombre canonico del .bib de asignatura antes de cierre."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No inventar referencias ni metadatos.",
    "Registrar en .bib solo obras consultables y pertinentes a la consigna local.",
    "Tratar filosofia-del-derecho-clean.bib como complemento tematico [supuesto] cuando la consigna lo requiera."
  ],
  "propagation_hints": [
    "Propagar lateral y recursivo solo tras validar JSON y estructura.",
    "Transferir solo patrones reutilizables, no redaccion ni conclusiones del hermano.",
    "Mantener reglas utiles previas sin regresion.",
    "Aplicar union-dedupe como mecanismo de compresion lossless.",
    "Si falta dato local, propagar estructura base y preguntas abiertas."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-2: tema, semana y producto.",
    "Confirmar plantilla obligatoria de secciones definida por docente.",
    "Confirmar estilo de citacion institucional obligatorio [supuesto: no confirmado].",
    "Confirmar si actividad-2 usa .bib propio o reutiliza el canonico de asignatura.",
    "Confirmar resolucion final de nombres de archivo con caracteres anomalos en README."
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
        "Carpeta de asignatura como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Filosofia del Derecho."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y fuentes pertinentes.",
      "Analisis propio.",
      "Evidencia verificable.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos trazables.",
      "Asegurar coherencia entre consigna, argumentacion y evidencia.",
      "Preservar continuidad editorial entre actividades hermanas sin contaminar contenido especifico."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales y trazables.",
      "Diferenciacion clara entre postura propia, cita y parafrasis.",
      "Marcado explicito de supuestos."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/fuentes -> analisis -> conclusion.",
      "Afirmacion juridica -> evidencia -> interpretacion propia.",
      "Consigna local -> adecuacion de formato -> verificacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion de salidas",
        "Ejes editoriales troncales",
        "Trazabilidad cita-bibliografia",
        "Transferencia lateral controlada"
      ],
      "citations": [
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/programa-analitico-filosofia-del-derecho.md",
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Ejes editoriales troncales",
          "kind": "supports",
          "justification": "Define tono, objetivo y consistencia academica."
        },
        {
          "source": "Normalizacion de salidas",
          "target": "Transferencia lateral controlada",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay propagacion segura."
        },
        {
          "source": "Trazabilidad cita-bibliografia",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Permite verificar respaldo de afirmaciones."
        },
        {
          "source": "Ejes editoriales troncales",
          "target": "Actividad 2",
          "kind": "develops",
          "justification": "Son patrones reutilizables aplicables al nuevo nodo."
        }
      ],
      "evidence": [
        "README fija identidad UnADM y conclusion juridica con criterio propio.",
        "Programa analitico define ejes: problema, conceptos, producto, analisis, conclusion.",
        "Regla historica valida: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 71: refuerzo lateral por analogia controlada aplicado sin copiar contenido exclusivo.",
      "Se deduplicaron reglas repetidas y se preservo cobertura util previa.",
      "Se mantuvo estado provisional de fuentes no verificadas.",
      "Se reforzo gate de normalizacion estructurada previa a propagacion recursiva."
    ]
  }
}