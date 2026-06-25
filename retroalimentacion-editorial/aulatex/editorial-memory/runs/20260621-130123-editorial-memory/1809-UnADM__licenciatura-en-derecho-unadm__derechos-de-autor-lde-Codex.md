{
  "summary": [
    "Se consolida sincronizacion transversal conservadora hacia Derechos de autor con abstracciones estables.",
    "Se preserva normalizacion estructurada obligatoria antes de cualquier propagacion.",
    "Se mantiene compresion lossless por union y deduplicacion sin recorte semantico.",
    "Se refuerzan ejes editoriales reutilizables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se confirma README como entrada canonica y se detectan tokens/errores de plantilla pendientes de resolver."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar herencia Codex y GPT-Pro como provisional hasta validacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
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
    "Auditar y normalizar salidas no estructuradas antes de reutilizarlas."
  ],
  "latex_rules": [
    "Mantener codificacion y acentos correctos en espanol en .tex y .bib.",
    "Declarar metadatos antes de cargar plantilla segun convencion local.",
    "Evitar comandos no estandar o incompletos sin justificacion editorial.",
    "Compilar sin errores criticos, sin referencias rotas y sin paquetes truncados.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) y corregir nombres corruptos en README/programa."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo materiales consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y marco juridico pertinente.",
    "Registrar bibliografia especifica por actividad en derechos-de-autor.bib.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/editorial o URL.",
    "Incluir fecha de consulta en fuentes web cuando aplique."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "No transferir redaccion literal ni datos personales entre materias.",
    "Mantener bandera de normalizacion manual para herencia historica no estructurada.",
    "Evitar regresiones: toda regla util previa se conserva."
  ],
  "open_questions": [
    "Supuesto: confirmar si LDE-S5B1 es clave oficial transversal en la suite.",
    "Confirmar nombre de figura docente para reemplazar marcador pendiente.",
    "Confirmar si ubicacion institucional en portada debe ser fija o variable por actividad.",
    "Confirmar orden correcto de paquetes respecto a \\input{template} en esta plantilla.",
    "Confirmar cierre definitivo de herencia provisional Codex/GPT-Pro tras validacion local."
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
        "Normalizacion estructurada previa a propagacion."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 5, bloque 1, obligatoria, 8 creditos.",
        "Asignatura destino: Derechos de autor."
      ]
    },
    "essence": [
      "Problema juridico o social delimitado.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable trazable.",
      "Analisis propio con postura.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos validos y transferibles.",
      "Sostener coherencia entre identidad institucional, argumentacion y evidencia."
    ],
    "style_markers": [
      "Declarar supuestos de forma explicita.",
      "Usar secciones funcionales y trazables.",
      "Mantener consistencia entre portada, contenido y referencias."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Marco conceptual-normativo.",
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
          "justification": "Evita heredar salidas no parseables y reduce ruido editorial."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Toda afirmacion debe tener respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La postura argumentada habilita aplicacion profesional."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura editorial reusable",
          "kind": "depends_on",
          "justification": "La consistencia institucional guía forma y validacion."
        }
      ],
      "evidence": [
        "README de Derechos de autor fija ubicacion curricular y pauta editorial.",
        "Programa analitico define ejes problema-conceptos-producto-analisis-cierre.",
        "derechos-de-autor.bib contiene base institucional verificable.",
        "Se detectan tokens de plantilla sin expandir y nombres de archivo corruptos en contexto local."
      ]
    },
    "reinforcement_log": [
      "Ciclo 13: se refuerza transferencia transversal por abstracciones estables.",
      "Ciclo 13: se conserva regla dura de JSON parseable como gate de propagacion.",
      "Ciclo 13: se mantiene herencia no verificada como provisional.",
      "Ciclo 13: se incorpora control explicito de tokens de plantilla no resueltos."
    ]
  }
}