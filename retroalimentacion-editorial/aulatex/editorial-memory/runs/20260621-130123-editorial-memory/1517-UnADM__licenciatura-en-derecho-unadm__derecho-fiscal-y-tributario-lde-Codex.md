{
  "summary": [
    "Se sincroniza memoria transversal desde actividad de Filosofia del Derecho hacia la materia Derecho fiscal y tributario sin traslado literal.",
    "Se conserva identidad UnADM y compresion lossless por union-dedupe sin regresion.",
    "Se refuerzan ejes editoriales estables: problema, conceptos o normas, evidencia, analisis propio y conclusion juridica transferible.",
    "Se mantiene regla de normalizacion obligatoria para toda salida no JSON parseable antes de propagar.",
    "Se prioriza reutilizacion de estructura argumentativa y gates de calidad sobre contenido tematico de origen.",
    "Supuesto: no hay consigna local de actividad especifica en este ciclo; se consolidan reglas marco de materia."
  ],
  "identity_rules": [
    "Conservar identidad UnADM en tono, portada y metadatos.",
    "Usar contexto curricular verificado del destino: Derecho fiscal y tributario, semestre 6, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica editorial.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No trasladar datos personales de plantilla a entregables finales sin verificacion previa."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear cada producto con la planeacion semanal y la consigna vigente.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener separacion funcional entre reporte .tex, presentacion .tex y .bib local."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar entregas solo descriptivas.",
    "Vincular argumentos fiscal-tributarios con aplicacion profesional concreta.",
    "No asumir fuentes de otras semanas o materias como obligatorias sin validacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna local de la actividad.",
    "Corregir placeholders, rutas truncadas y tokens sin expandir antes de publicar."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar quiebres de compilacion.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Completar campos de portada y authortable antes de compilar.",
    "No introducir comandos no estandar sin justificacion editorial."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y normas juridicas verificables.",
    "Registrar fuentes especificas por actividad en derecho-fiscal-y-tributario.bib.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Usar malla curricular solo para respaldo de datos curriculares."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Compartir entre nodos no equivalentes solo abstracciones editoriales estables.",
    "Evitar transferencia de redaccion literal o bibliografia tematica no homologable.",
    "Mantener estrategia conservadora: agregar solo mejoras verificables.",
    "Aplicar union-dedupe en cada ciclo para compresion lossless.",
    "Registrar supuestos abiertos cuando falte contexto local."
  ],
  "open_questions": [
    "Confirmar consigna activa de la primera actividad de la materia destino.",
    "Confirmar formato de citacion exigido por la asignatura.",
    "Confirmar si se mantiene derecho-fiscal-y-tributario.bib como archivo canonico unico.",
    "Resolver definitivamente tokens de slug sin expandir en README y programa analitico.",
    "Confirmar datos finales de figura docente y datos de portada para uso publico.",
    "Supuesto: la plantilla actual del reporte requiere cierre completo de authortable y revision final de compilacion."
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
        "Materia: Derecho fiscal y tributario.",
        "Semestre 6, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico inicial claro.",
      "Marco conceptual y normativo pertinente.",
      "Evidencia verificable con citas trazables.",
      "Analisis propio con postura.",
      "Conclusion juridica aplicable a la practica."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con rigor juridico.",
      "Garantizar consistencia editorial entre actividades de la materia.",
      "Permitir propagacion transversal segura sin perdida de reglas utiles."
    ],
    "style_markers": [
      "Apertura breve y enfocada.",
      "Secciones funcionales sin relleno.",
      "Cierre profesional transferible.",
      "Sin afirmaciones sin fuente o sin etiqueta de supuesto."
    ],
    "argumentative_patterns": [
      "Problema -> objetivo -> marco normativo -> analisis propio -> conclusion.",
      "Pregunta guia explicita y respuesta coherente.",
      "Contraste de fuentes y toma de posicion justificada."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion JSON",
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
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica con trazabilidad de fuentes",
          "kind": "supports",
          "justification": "La identidad institucional exige evidencia verificable y formato consistente."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "La postura argumentativa depende de una pregunta o conflicto definido."
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
          "justification": "Sin estructura parseable no hay transferencia editorial segura."
        }
      ],
      "evidence": [
        "README de la materia destino con ubicacion curricular y pauta editorial.",
        "Programa analitico local con ejes de trabajo reutilizables.",
        "Archivo derecho-fiscal-y-tributario.bib con base institucional verificable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 6: se conserva ADN institucional y argumentativo sin recorte.",
      "Ciclo 6: se deduplican reglas repetidas y se unifican formulaciones equivalentes.",
      "Ciclo 6: se transfiere solo abstraccion metodologica estable desde origen filosofico.",
      "Ciclo 6: se mantienen abiertos vacios de contexto local para validacion posterior."
    ]
  }
}