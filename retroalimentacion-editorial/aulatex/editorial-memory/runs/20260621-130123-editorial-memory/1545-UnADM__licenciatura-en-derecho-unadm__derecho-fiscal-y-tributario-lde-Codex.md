{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia conservadora y sin regresion.",
    "Se preserva ADN UnADM y se transfiere solo metodologia editorial estable.",
    "Se mantiene compresion lossless por union y deduplicacion.",
    "Se refuerza normalizacion JSON obligatoria antes de propagacion recursiva.",
    "Se evita transferir contenido tematico especifico de Filosofia del Derecho al campo fiscal."
  ],
  "identity_rules": [
    "Conservar identidad UnADM en tono, portada y metadatos.",
    "Usar contexto local verificado: Derecho fiscal y tributario, semestre 6, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica editorial.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto con la consigna y la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar entregas solo descriptivas.",
    "Vincular analisis fiscal-tributario con aplicacion profesional concreta."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Corregir placeholders, rutas rotas y tokens sin expandir antes de publicar."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Completar campos de plantilla antes de compilar.",
    "Cerrar correctamente entornos truncados, incluido authortable y tabular."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y normas juridicas verificables.",
    "Registrar fuentes especificas por actividad en derecho-fiscal-y-tributario.bib.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Compartir a nodos no equivalentes solo abstracciones editoriales estables.",
    "No lateralizar datos tematicos o bibliografia especializada sin verificacion local.",
    "Mantener union-dedupe y regla de no regresion en ciclos siguientes.",
    "Aplicar normalizacion manual cuando aparezca salida heredada ambigua o no estructurada."
  ],
  "open_questions": [
    "Supuesto: falta consigna puntual de primeras actividades de la materia destino.",
    "Confirmar formato de citacion exigido por la asignatura.",
    "Confirmar nombre de figura docente para portada.",
    "Confirmar si autor y matricula deben permanecer en plantillas compartidas.",
    "Resolver token Slug sin expandir en README y programa analitico."
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
        "Supuestos etiquetados y trazables."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia destino: Derecho fiscal y tributario.",
        "Semestre 6, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico inicial.",
      "Marco conceptual y normativo verificable.",
      "Analisis propio sustentado.",
      "Cierre juridico transferible.",
      "Control de calidad estructural y bibliografico."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables academicos verificables.",
      "Preservar coherencia institucional y rigor juridico en cada actividad.",
      "Permitir propagacion segura entre nodos sin perdida editorial."
    ],
    "style_markers": [
      "Frases directas y verificables.",
      "Sin relleno descriptivo.",
      "Fuente o supuesto en cada afirmacion sensible.",
      "Secciones funcionales con cierre profesional."
    ],
    "argumentative_patterns": [
      "Problema concreto -> objetivo -> marco normativo -> analisis propio -> conclusion.",
      "Afirmacion juridica -> evidencia verificable -> implicacion practica.",
      "Consigna local como criterio de pertinencia final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion JSON",
        "Integridad academica",
        "Problema juridico",
        "Marco normativo",
        "Analisis propio",
        "Conclusion transferible",
        "Consistencia .tex/.bib"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia segura."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "La argumentacion se ordena desde un conflicto definido."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La validez del cierre juridico requiere fundamento expreso."
        },
        {
          "source": "Integridad academica",
          "target": "Consistencia .tex/.bib",
          "kind": "supports",
          "justification": "La trazabilidad de citas exige concordancia entre texto y bibliografia."
        }
      ],
      "evidence": [
        "README local: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico local: proposito, ejes y regla bibliografica.",
        "derecho-fiscal-y-tributario.bib: base institucional verificable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 13: deduplicacion completa de reglas repetidas y equivalentes.",
      "Ciclo 13: transferidos patrones metodologicos estables desde nodo de actividad transversal.",
      "Ciclo 13: excluida transferencia de contenido doctrinal especifico de Filosofia por no equivalencia tematica.",
      "Ciclo 13: reforzado gate de compilacion LaTeX por deteccion de bloque truncado en reporte local.",
      "Ciclo 13: preservada regla historica de no propagar salidas no estructuradas."
    ]
  }
}