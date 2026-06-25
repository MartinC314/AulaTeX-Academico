{
  "summary": [
    "Se consolida sincronizacion transversal con transferencia solo de abstracciones editoriales estables.",
    "Se preserva identidad UnADM y contexto curricular local de Derecho fiscal y tributario.",
    "Se refuerza compresion lossless por union-deduplicacion sin recorte de reglas utiles.",
    "Se mantiene bloqueo de propagacion para salidas no JSON parseables y exigencia de normalizacion previa.",
    "Se priorizan ejes reutilizables: problema, conceptos o normas, evidencia, analisis propio y conclusion juridica."
  ],
  "identity_rules": [
    "Conservar identidad institucional UnADM en tono, portada y metadatos.",
    "Mantener contexto curricular local verificado: Derecho fiscal y tributario, semestre 6, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica editorial.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No transferir identidad tematica de Filosofia del Derecho como contenido obligatorio en Fiscal."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto con la planeacion semanal y la consigna vigente.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Corregir rutas y nombres rotos en README y programa analitico antes de publicar."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante y evitar resumen meramente descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Vincular analisis fiscal-tributario con aplicacion profesional concreta.",
    "No asumir fuentes de otras semanas o materias como obligatorias sin validacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar placeholders o tokens sin expandir en README, .tex y .bib.",
    "Verificar consistencia entre portada, programa analitico y malla curricular local."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas.",
    "Compilar sin errores criticos, entornos truncados ni referencias rotas.",
    "Completar campos de plantilla antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "No introducir comandos no estandar sin justificacion editorial."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y normas juridicas verificables.",
    "Registrar fuentes especificas por actividad en derecho-fiscal-y-tributario.bib.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Usar la malla curricular solo para sustento de ubicacion curricular."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales y estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferencia de redaccion literal o contenido tematico especifico de Filosofia.",
    "Mantener estrategia progresiva y conservadora: agregar mejoras verificables sin regresion.",
    "Aplicar normalizacion manual cuando la entrada heredada sea ambigua o no estructurada."
  ],
  "open_questions": [
    "Supuesto: falta consigna local de actividad especifica en Fiscal; confirmar producto exacto solicitado.",
    "Confirmar formato de citacion requerido por la asignatura.",
    "Confirmar figura docente y datos personales que deben permanecer en plantilla.",
    "Confirmar correccion definitiva de rutas truncadas en README.",
    "Confirmar si existe rubrica local que ajuste profundidad argumentativa."
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
        "Trazabilidad de supuestos y fuentes."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia destino: Derecho fiscal y tributario.",
        "Semestre 6, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico bien delimitado.",
      "Marco conceptual y normativo pertinente.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos solidos y verificables.",
      "Asegurar coherencia entre identidad institucional, metodo argumentativo y salida tecnica."
    ],
    "style_markers": [
      "Supuestos etiquetados.",
      "Sin afirmaciones sin fuente.",
      "Secciones funcionales con cierre profesional.",
      "Consistencia entre .tex, .bib y metadatos."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Objetivo explicito.",
      "Desarrollo por conceptos y norma aplicable.",
      "Contraste de fuentes con postura propia.",
      "Cierre con implicacion practica juridica."
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
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La identidad institucional exige evidencia verificable y formato consistente."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin delimitacion del problema no hay argumentacion sustantiva."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion profesional requiere fundamento normativo explicito."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "La transferencia segura entre nodos depende de estructura parseable."
        }
      ],
      "evidence": [
        "README local de la materia.",
        "Programa analitico local.",
        "derecho-fiscal-y-tributario.bib."
      ]
    },
    "reinforcement_log": [
      "Ciclo 11: deduplicacion integral aplicada sin perdida de reglas utiles.",
      "Ciclo 11: transferencia transversal limitada a patrones estables, sin arrastre tematico indebido.",
      "Ciclo 11: se refuerzan gates de parseo JSON, supuestos y trazabilidad bibliografica."
    ]
  }
}