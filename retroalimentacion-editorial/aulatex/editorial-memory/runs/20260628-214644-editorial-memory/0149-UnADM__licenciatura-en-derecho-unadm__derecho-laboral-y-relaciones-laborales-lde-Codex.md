{
  "summary": [
    "Sincronizacion transversal ciclo 2 aplicada con estrategia conservadora.",
    "Se preservan reglas utiles previas y se deduplican sin recorte.",
    "Se refuerza ADN UnADM con enfoque juridico-laboral del destino.",
    "Se mantiene normalizacion obligatoria antes de propagacion recursiva.",
    "Se consolidan ejes estables: problema, conceptos, evidencia, analisis propio y conclusion juridica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar contexto curricular del destino: Licenciatura en Derecho, semestre 7, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social laboral.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto pedido en planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Contextualizar cada actividad en pregunta guia verificable.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar resumen descriptivo puro.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No trasladar contenido de otra materia sin validar pertinencia laboral."
  ],
  "quality_gates": [
    "Bloquear propagacion si salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver marcadores sin expandir tipo $(@{...}.Slug) en README, programa y nombres de archivo.",
    "Completar entornos truncados de plantilla antes de compilar.",
    "Verificar nombres canonicos reales de archivos antes de referenciarlos."
  ],
  "bibliography_rules": [
    "Centralizar fuentes de materia en derecho-laboral-y-relaciones-laborales.bib.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Agregar solo entradas BibTeX consultables y pertinentes a actividad.",
    "No inventar referencias, normas, jurisprudencia ni URLs.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Compartir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferencia de redaccion literal entre materias.",
    "Preservar reglas utiles previas y agregar solo mejoras verificables."
  ],
  "open_questions": [
    "Confirmar formato de cita juridica exigido por docente (supuesto: no definido).",
    "Confirmar si autor de plantilla es fijo o variable por alumno (supuesto: variable).",
    "Confirmar rubrica oficial por actividad para convertirla en checklist.",
    "Confirmar nombres canonicos finales de artefactos y carpeta de referencias.",
    "Confirmar si cada actividad requiere .bib propio o uso exclusivo del .bib de materia."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Explicito al marcar supuestos."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada antes de propagacion.",
        "Carpeta de asignatura como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Derecho laboral y relaciones laborales.",
        "Semestre 7, bloque 1, obligatoria, 8 creditos.",
        "Fuente curricular local: malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Problema juridico o social como detonante.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable y trazable.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible a practica profesional."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros y verificables.",
      "Asegurar coherencia entre consigna, desarrollo y cierre juridico.",
      "Garantizar trazabilidad editorial y tecnica para reutilizacion segura."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Sin duplicados semanticos.",
      "Supuestos etiquetados cuando falte evidencia local.",
      "Sin invencion de fuentes.",
      "Sin copia literal transversal."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Marco conceptual y normativo pertinente.",
      "Analisis propio con contraste de fuentes.",
      "Cierre con criterio juridico aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema juridico laboral",
        "Marco normativo y doctrinal",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion estructurada",
        "Trazabilidad de citas"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Trazabilidad de citas",
          "kind": "supports",
          "justification": "La integridad academica institucional exige citas verificables."
        },
        {
          "source": "Problema juridico laboral",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis parte de una pregunta guia contextualizada."
        },
        {
          "source": "Marco normativo y doctrinal",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion profesional requiere sustento juridico verificable."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Trazabilidad de citas",
          "kind": "develops",
          "justification": "La salida estructurada permite validar coherencia entre texto y .bib."
        }
      ],
      "evidence": [
        "README de materia: identidad UnADM, citas verificables y conclusion juridica propia.",
        "Programa analitico: ejes problema-conceptos-producto-analisis-conclusion.",
        "Bibliografia local: claves institucionales base disponibles.",
        "Regla estable: bloquear propagacion de salida no parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: se consolida union-dedupe lossless sin eliminar reglas utiles.",
      "Ciclo 2: se transfiere patron argumentativo estable sin contenido literal de Filosofia del Derecho.",
      "Ciclo 2: se refuerza gate de JSON parseable y normalizacion previa.",
      "Ciclo 2: se mantiene enfoque juridico-laboral del destino con identidad UnADM."
    ]
  }
}