{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia conservadora y deduplicacion lossless.",
    "Se preservan reglas institucionales UnADM, estructura reusable y gates de calidad ya validados.",
    "Se incorporan abstracciones estables desde Filosofia del Derecho sin transferir contenido tematico especifico.",
    "Se refuerza control de normalizacion JSON, trazabilidad de fuentes y marcado de supuestos.",
    "Se mantiene cerebro editorial minimo de materia con vacios locales explicitados."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y formato.",
    "Usar tono juridico formal, claro, verificable y sobrio en inferencias.",
    "Conservar contexto curricular del destino: Licenciatura en Derecho, semestre 8, bloque 1, tipo Electiva.",
    "No renombrar asignatura ni codigo provisional sin confirmacion oficial.",
    "Marcar como supuesto todo dato no visible en consigna o documentos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "Conservar autor y matricula de plantilla mientras no exista instruccion institucional en contrario."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Declarar objetivo puntual antes del desarrollo.",
    "Organizar secciones en secuencia estable: problema, conceptos o fuentes, analisis propio, cierre.",
    "Alinear el producto al tipo de entrega solicitado por planeacion semanal.",
    "Diferenciar resumen de fuentes y postura propia.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Vincular cada actividad con al menos un problema juridico o social delimitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No extrapolar contenidos tematicos de otras materias sin evidencia local.",
    "Registrar supuestos cuando falte consigna especifica."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar aguas abajo.",
    "Confirmar consistencia entre portada, metadatos y nombre de asignatura.",
    "Confirmar trazabilidad de afirmaciones con respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Corregir placeholders y literales corruptos en README, programa y rutas antes de entrega."
  ],
  "latex_rules": [
    "Mantener plantilla LaTeX base de materia para reporte y presentacion.",
    "Mantener consistencia entre documenttitle, documentsubtitle, documentsubject, coursename y coursecode.",
    "Usar codificacion y paquetes compatibles con espanol academico.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en nombres de archivo y referencias.",
    "Completar campos pendientes de portada cuando exista dato oficial."
  ],
  "bibliography_rules": [
    "Usar electiva-semestre-8-bloque-1.bib como archivo local canonico.",
    "Priorizar fuentes institucionales UnADM y materiales verificables.",
    "Agregar fuentes especificas por actividad en el .bib local.",
    "No inventar referencias; incluir solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente o URL.",
    "Mantener claves BibTeX estables y descriptivas."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas abstractas y estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "No propagar redaccion literal ni contenidos tematicos especificos sin evidencia local.",
    "Aplicar union-dedupe lossless en cada ciclo para evitar regresiones.",
    "Mantener registro de fuentes provisionales heredadas hasta confirmacion."
  ],
  "open_questions": [
    "Supuesto: creditos oficiales de la electiva siguen sin confirmar.",
    "Supuesto: figura docente sigue sin confirmar en plantilla.",
    "Confirmar si existe nombre oficial distinto para la electiva.",
    "Confirmar si presentacion-electiva-semestre-8-bloque-1.tex mantiene misma portada canonica.",
    "Confirmar correccion completa de nombres corruptos en README y programa."
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
      "Problema juridico o social como punto de partida.",
      "Conceptos y fuentes verificables como base.",
      "Analisis propio con criterio juridico.",
      "Conclusion transferible a practica profesional.",
      "Normalizacion estructurada obligatoria antes de propagar."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y defendibles.",
      "Sostener continuidad editorial entre actividades y materia sin perder identidad local."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones estables y reutilizables.",
      "Postura propia sustentada.",
      "Cierre juridico transferible.",
      "Supuestos marcados."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/fuentes -> analisis -> conclusion.",
      "Afirmacion -> evidencia verificable -> inferencia juridica.",
      "Descripcion breve -> postura critica -> implicacion practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Estructura argumentativa juridica",
        "Trazabilidad de fuentes",
        "Normalizacion JSON",
        "Control de placeholders editoriales",
        "Marcado de supuestos"
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
          "justification": "Define tono, formato y criterio academico comun."
        },
        {
          "source": "Trazabilidad de fuentes",
          "target": "Estructura argumentativa juridica",
          "kind": "supports",
          "justification": "Sostiene afirmaciones y evita contenido descriptivo sin respaldo."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay reutilizacion confiable."
        },
        {
          "source": "Control de placeholders editoriales",
          "target": "Calidad de compilacion LaTeX",
          "kind": "supports",
          "justification": "Previene rutas rotas y errores por tokens sin expandir."
        },
        {
          "source": "Marcado de supuestos",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Distingue dato verificado de inferencia provisional."
        }
      ],
      "evidence": [
        "README local con placeholders Slug y nombres corruptos detectados.",
        "Programa analitico local con ejes editoriales estables.",
        "Archivo .bib local con fuentes institucionales base.",
        "Regla heredada valida: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 16: se consolida transferencia transversal estable sin mover contenido tematico especifico.",
      "Ciclo 16: se refuerzan gates de parseo JSON, trazabilidad y consistencia bib.",
      "Ciclo 16: se mantiene politica conservadora de supuestos y fuentes provisionales.",
      "Ciclo 16: deduplicacion semantica aplicada sin eliminar reglas utiles previas."
    ]
  }
}