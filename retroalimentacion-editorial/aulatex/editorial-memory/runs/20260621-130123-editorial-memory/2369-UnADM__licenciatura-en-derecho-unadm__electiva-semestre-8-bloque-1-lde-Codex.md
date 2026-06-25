{
  "summary": [
    "Se sincroniza ADN editorial transversal desde actividad de Filosofia del Derecho hacia materia Electiva S8 B1 sin traslado tematico literal.",
    "Se conserva union-dedupe lossless y no regresion de reglas utiles previas.",
    "Se refuerzan ejes estables: problema, conceptos/fuentes, analisis propio y conclusion juridica transferible.",
    "Se mantiene control estricto de salida estructurada JSON antes de propagacion recursiva.",
    "Se incorpora mejora verificable local: corregir placeholders Slug y nombres corruptos en README/programa."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y formato.",
    "Usar tono juridico formal, claro, verificable y sobrio en inferencias.",
    "Conservar contexto curricular del destino: Licenciatura en Derecho, semestre 8, bloque 1, tipo Electiva.",
    "No renombrar asignatura ni codigo LDE-S8B1 sin confirmacion oficial.",
    "Marcar como supuesto todo dato no visible o no confirmado.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Declarar objetivo puntual antes del desarrollo.",
    "Organizar secciones en secuencia reusable: conceptos/fuentes, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Usar carpeta de materia como punto de entrada canonico."
  ],
  "activity_rules": [
    "Diferenciar resumen de fuentes y postura propia del estudiante.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Relacionar el producto con al menos un problema juridico o social delimitado.",
    "No extrapolar contenidos tematicos de Filosofia del Derecho sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar aguas abajo.",
    "Confirmar trazabilidad de afirmaciones con respaldo o marca de supuesto.",
    "Validar consistencia entre portada, metadatos y nombre de asignatura.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Corregir placeholders y caracteres corruptos en rutas y nombres antes de compilar o entregar."
  ],
  "latex_rules": [
    "Mantener plantilla LaTeX base de la materia.",
    "Mantener consistentes documenttitle, documentsubtitle, documentsubject, coursename y coursecode.",
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Completar campos pendientes de portada con dato oficial o marca de supuesto."
  ],
  "bibliography_rules": [
    "Usar electiva-semestre-8-bloque-1.bib como archivo bibliografico local canonico.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas por actividad en el .bib local.",
    "No inventar referencias; incluir solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Mantener claves BibTeX estables y descriptivas."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo abstracciones editoriales estables.",
    "No propagar metadatos o contenido tematico especifico entre nodos no equivalentes.",
    "Priorizar propagacion de identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Aplicar union-dedupe lossless en cada ciclo para evitar duplicados semanticos.",
    "Si falta consigna local, conservar cerebro editorial minimo y abrir vacios como preguntas."
  ],
  "open_questions": [
    "Supuesto: creditos oficiales de la electiva aun no confirmados.",
    "Supuesto: figura docente aun no confirmada en portada.",
    "Confirmar nombre oficial final de la asignatura electiva.",
    "Confirmar si existe rubrica especifica por actividad para ajustar profundidad argumentativa.",
    "Confirmar que README y programa queden sin placeholders Slug tras normalizacion."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Juridicamente preciso.",
        "Claro y verificable.",
        "Sobrio ante datos no confirmados."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta de materia como entrada canonica.",
        "Supuestos etiquetados sin ambiguedad."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 8, bloque 1, tipo Electiva.",
        "Transferencia profesional como criterio de cierre."
      ]
    },
    "essence": [
      "Problema juridico o social que activa la actividad.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos con fundamento juridico y evidencia.",
      "Garantizar coherencia entre consigna, desarrollo y cierre argumentativo."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones estables y reutilizables.",
      "Afirmaciones con cita verificable.",
      "Postura propia sustentada.",
      "Cierre juridico aplicable.",
      "Supuestos marcados."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/fuentes -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> inferencia juridica.",
      "Descripcion breve -> posicion critica -> implicacion practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Estructura argumentativa juridica",
        "Trazabilidad de fuentes",
        "Normalizacion JSON",
        "Control de placeholders editoriales"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura argumentativa juridica",
          "kind": "supports",
          "justification": "Define tono, formato y estandar de entrega."
        },
        {
          "source": "Trazabilidad de fuentes",
          "target": "Estructura argumentativa juridica",
          "kind": "supports",
          "justification": "Sostiene afirmaciones con evidencia verificable."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Control de placeholders editoriales",
          "kind": "depends_on",
          "justification": "La reutilizacion confiable exige estructura parseable y limpia."
        },
        {
          "source": "Control de placeholders editoriales",
          "target": "Estructura argumentativa juridica",
          "kind": "supports",
          "justification": "Evita fallas tecnicas que degradan la entrega academica."
        }
      ],
      "evidence": [
        "README local con placeholders Slug sin expandir.",
        "Programa analitico local con ejes estables de trabajo.",
        "Bib local con claves institucionales ya registradas.",
        "Plantilla LaTeX local con campos pendientes identificados."
      ]
    },
    "reinforcement_log": [
      "Ciclo 21: deduplicacion semantica completada sin recorte de reglas utiles.",
      "Ciclo 21: reforzada regla de no extrapolar contenido tematico entre nodos no equivalentes.",
      "Ciclo 21: reforzados gates de JSON parseable, trazabilidad y consistencia bib/tex.",
      "Ciclo 21: consolidado cerebro editorial minimo con vacios locales abiertos como supuestos."
    ]
  }
}