{
  "summary": [
    "Se consolida sincronizacion transversal conservadora para Derechos de autor.",
    "Se preservan reglas utiles previas sin regresion y con deduplicacion lossless.",
    "Se refuerza normalizacion estructurada obligatoria antes de propagacion.",
    "Se mantiene herencia no verificada como provisional hasta validacion local.",
    "Se transfieren solo abstracciones estables entre Filosofia del Derecho y Derechos de autor."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Corregir tokens de plantilla no resueltos en README y programa analitico.",
    "Corregir nombres de archivo corruptos antes de publicar."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Agregar fuentes especificas por actividad al .bib local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Auditar README y programa analitico por marcadores literales y caracteres anomalos.",
    "Corregir campos pendientes en portada como Nombre por definir."
  ],
  "latex_rules": [
    "Mantener codificacion y acentos correctos en espanol.",
    "Declarar metadatos antes de cargar plantilla cuando aplique.",
    "Evitar paquetes incompletos o comandos truncados en preambulo.",
    "No dejar \\usepackage sin argumento.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo materiales verificables.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos pertinentes.",
    "Registrar bibliografia especifica de actividad en derechos-de-autor.bib.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Incluir fecha de consulta en fuentes web.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Propagar lateralmente solo reglas generales estables en nodos no equivalentes.",
    "No propagar redaccion literal ni datos personales.",
    "Mantener bandera de normalizacion manual para herencia de ciclos con salida no estructurada.",
    "Evitar regresiones respecto de reglas utiles previas."
  ],
  "open_questions": [
    "Supuesto: clave LDE-S5B1 es oficial; confirmar en fuente institucional.",
    "Confirmar nombre de figura docente para cerrar metadatos de portada.",
    "Confirmar si ubicacion institucional debe permanecer fija en documentos.",
    "Confirmar orden correcto de paquetes respecto a plantilla en esta materia.",
    "Confirmar retiro o permanencia de herencia Codex y GPT-Pro tras validacion local."
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
        "Asignatura: Derechos de autor.",
        "Supuesto: clave local LDE-S5B1."
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
      "Convertir planeacion semanal en productos academicos trazables.",
      "Sostener consistencia editorial entre actividades y materia.",
      "Asegurar calidad institucional y propagacion segura."
    ],
    "style_markers": [
      "Declarar supuestos de forma explicita.",
      "Usar secciones funcionales y verificables.",
      "Mantener coherencia entre portada, desarrollo y bibliografia.",
      "Normalizar antes de propagar."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Marco conceptual y normativo.",
      "Analisis con postura propia.",
      "Cierre con implicacion practica juridica."
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
          "justification": "La postura argumentada habilita cierre profesional."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Consistencia transversal de la suite",
          "kind": "supports",
          "justification": "Permite transferir reglas estables entre materias."
        }
      ],
      "evidence": [
        "README de Derechos de autor confirma ubicacion curricular y pauta editorial.",
        "Programa analitico confirma ejes problema-conceptos-producto-analisis-cierre.",
        "derechos-de-autor.bib contiene base institucional verificable.",
        "Se detectaron tokens sin expandir y nombres de archivo corruptos en contexto local.",
        "Se detecto \\usepackage sin argumento en reporte LaTeX."
      ]
    },
    "reinforcement_log": [
      "Ciclo 8: deduplicacion integral aplicada sin recorte semantico.",
      "Ciclo 8: se reforzaron gates de JSON parseable y estructura minima.",
      "Ciclo 8: se conservaron reglas institucionales y curriculares validas.",
      "Ciclo 8: se mantuvo herencia provisional Codex/GPT-Pro bajo control de supuestos.",
      "Ciclo 8: se reforzo transferencia transversal por abstracciones estables."
    ]
  }
}