{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia conservadora y sin regresion.",
    "Se preserva ADN UnADM y se transfiere solo abstraccion metodologica reusable.",
    "Se mantiene compresion lossless por union y deduplicacion.",
    "Se refuerza normalizacion obligatoria de salidas no estructuradas antes de propagar.",
    "Se evita traslado de contenido tematico especifico de Filosofia del Derecho a Fiscal."
  ],
  "identity_rules": [
    "Conservar identidad UnADM en tono, portada y metadatos.",
    "Usar contexto curricular local verificado: semestre 6, bloque 1, obligatoria, 8 creditos.",
    "Mantener carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No trasladar datos curriculares de nodos no equivalentes."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear siempre el producto final con la consigna semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia local."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar entregas descriptivas sin analisis juridico.",
    "Vincular argumentos fiscal-tributarios con aplicacion profesional concreta.",
    "No asumir fuentes de otras semanas o materias como obligatorias del destino."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregable y consigna local.",
    "Corregir placeholders, slugs y rutas truncadas antes de publicar."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Completar portada y tabla de autor antes de compilar.",
    "Cerrar todos los entornos LaTeX truncados.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y normas juridicas verificables.",
    "Registrar fuentes especificas por actividad en derecho-fiscal-y-tributario.bib.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Usar la malla curricular solo para soporte de datos curriculares."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Compartir entre nodos no equivalentes solo reglas editoriales estables.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar propagar redaccion literal y bibliografia tematica no homologable.",
    "Aplicar normalizacion manual cuando existan salidas heredadas ambiguas."
  ],
  "open_questions": [
    "Confirmar consigna real de la actividad activa en Derecho fiscal y tributario.",
    "Confirmar formato de citacion exigido por la asignatura.",
    "Confirmar figura docente y si datos personales permanecen en plantillas base.",
    "Confirmar si el .bib local sera unico para toda la materia. [supuesto]",
    "Confirmar correccion definitiva de rutas truncadas en README."
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
        "Integridad academica con trazabilidad de fuentes.",
        "Supuestos etiquetados y verificables."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia destino: Derecho fiscal y tributario.",
        "Semestre 6, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico inicial claro.",
      "Marco conceptual y normativo delimitado.",
      "Analisis propio sustentado en evidencia.",
      "Cierre juridico transferible a practica profesional.",
      "Normalizacion estructural antes de propagacion."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos consistentes y verificables.",
      "Sostener continuidad editorial entre actividades sin perder contexto local.",
      "Asegurar calidad tecnica y argumentativa en LaTeX y bibliografia."
    ],
    "style_markers": [
      "Frases directas y accionables.",
      "Sin afirmaciones sin fuente o sin etiqueta de supuesto.",
      "Secciones funcionales con cierre profesional.",
      "Sin relleno descriptivo."
    ],
    "argumentative_patterns": [
      "Problema -> objetivo -> marco normativo -> analisis propio -> conclusion.",
      "Cada afirmacion relevante se apoya en fuente verificable.",
      "La conclusion responde a la pregunta guia y propone aplicacion practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema juridico",
        "Marco normativo",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion JSON",
        "Consistencia .tex/.bib"
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
          "justification": "La identidad institucional exige evidencia verificable y formato consistente."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "No hay argumentacion solida sin pregunta o conflicto definido."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica valida requiere fundamento normativo explicito."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia segura."
        }
      ],
      "evidence": [
        "README de la materia destino.",
        "Programa analitico de Derecho fiscal y tributario.",
        "Archivo derecho-fiscal-y-tributario.bib.",
        "Reglas institucionales consolidadas de ciclos previos."
      ]
    },
    "reinforcement_log": [
      "Ciclo 22: transferencia transversal sin mover contenido tematico no equivalente.",
      "Ciclo 22: deduplicacion completa de reglas repetidas y conservacion de reglas utiles previas.",
      "Ciclo 22: refuerzo de gates JSON, supuestos, trazabilidad y consistencia .tex/.bib.",
      "Ciclo 22: mantenimiento de cerebro editorial minimo del destino con vacios locales abiertos."
    ]
  }
}