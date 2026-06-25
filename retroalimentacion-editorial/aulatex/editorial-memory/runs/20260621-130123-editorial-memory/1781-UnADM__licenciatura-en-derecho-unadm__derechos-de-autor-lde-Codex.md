{
  "summary": [
    "Se consolida sincronizacion transversal conservadora para Derechos de autor con identidad UnADM.",
    "Se preservan reglas utiles previas y se deduplican sin perdida.",
    "Se transfieren solo abstracciones estables desde actividad no equivalente.",
    "Se mantiene normalizacion estructurada obligatoria antes de propagar.",
    "Se refuerzan ejes editoriales: problema, conceptos, evidencia, analisis propio y conclusion juridica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar herencia Codex y GPT-Pro como provisional hasta validacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear formato final al producto solicitado por la planeacion semanal.",
    "Corregir tokens de plantilla no resueltos en README y programa analitico.",
    "Corregir nombres de archivo corruptos antes de publicar."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Agregar fuentes especificas por actividad al .bib local.",
    "No asumir fuentes de otras semanas sin confirmacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna de la actividad.",
    "Auditar README y programa analitico por tokens sin expandir y caracteres anómalos."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Declarar metadatos antes de \\input{template}.",
    "Mover paquetes al preambulo efectivo segun plantilla.",
    "Nunca dejar \\usepackage sin argumento.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Mantener claves BibTeX estables para evitar rupturas."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo obras consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y juridicas pertinentes.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Incluir fecha de consulta en fuentes web.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Compartir lateralmente reglas generales de identidad, estructura y calidad.",
    "Evitar transferir redaccion literal o contenido tematico de Filosofia del Derecho.",
    "Mantener bandera de normalizacion manual para herencia de ciclos tempranos.",
    "No propagar datos personales del alumno a otros nodos."
  ],
  "open_questions": [
    "Confirmar si LDE-S5B1 es clave oficial definitiva. [supuesto]",
    "Definir nombre de figura docente en portada.",
    "Confirmar si ubicacion institucional debe permanecer fija en plantilla. [supuesto]",
    "Confirmar sustitucion total de tokens $(@{...}.Slug) por derechos-de-autor.bib.",
    "Confirmar consigna local de actividad para ajustar tipo de producto."
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
        "Entrada canonica por carpeta de asignatura.",
        "Herencia no verificada tratada como provisional."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 5, bloque 1, obligatoria, 8 creditos.",
        "Asignatura: Derechos de autor."
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y utiles para practica juridica.",
      "Asegurar continuidad editorial entre nodos sin perder especificidad local."
    ],
    "style_markers": [
      "Supuestos declarados de forma explicita.",
      "Secciones funcionales y trazables.",
      "Coherencia entre portada, cuerpo y referencias.",
      "Cierre con implicacion practica."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Marco conceptual y normativo.",
      "Analisis con postura propia y evidencia.",
      "Conclusion juridica aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Integridad bibliografica"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion segura",
          "kind": "supports",
          "justification": "Evita heredar salidas no parseables."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Toda afirmacion requiere respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La postura argumentada habilita cierre profesional util."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Coherencia editorial de materia",
          "kind": "depends_on",
          "justification": "Define tono, formato y metadatos."
        }
      ],
      "evidence": [
        "README local define ubicacion curricular y pauta editorial.",
        "Programa analitico local fija ejes de trabajo reutilizables.",
        "derechos-de-autor.bib contiene base institucional verificable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 6: deduplicacion integral sin recorte de reglas utiles.",
      "Ciclo 6: transferencia transversal limitada a abstracciones estables.",
      "Ciclo 6: refuerzo de gates JSON, supuestos y consistencia cita-bib.",
      "Ciclo 6: se mantiene estado provisional para herencias no verificadas."
    ]
  }
}