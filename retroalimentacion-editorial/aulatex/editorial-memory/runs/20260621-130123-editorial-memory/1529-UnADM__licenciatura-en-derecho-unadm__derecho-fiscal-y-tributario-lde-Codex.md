{
  "summary": [
    "Se mantiene sincronizacion transversal sin regresion entre nodos no equivalentes.",
    "Se conservan reglas estables: identidad UnADM, estructura reusable, calidad y trazabilidad.",
    "Se refuerza compresion lossless por union-dedupe y normalizacion previa a propagacion.",
    "Se evita transferir contenido tematico de Filosofia; solo patrones editoriales abstractos.",
    "Supuesto: el destino no tiene consigna de actividad especifica activa en este ciclo."
  ],
  "identity_rules": [
    "Conservar identidad institucional UnADM en tono, portada y metadatos.",
    "Usar contexto curricular local verificado: Derecho fiscal y tributario, semestre 6, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Verificar datos personales y figura docente antes de entrega final."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener separacion operativa entre reporte .tex, presentacion .tex y .bib local.",
    "Corregir rutas y nombres rotos en README y programa analitico antes de publicar."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Vincular el analisis fiscal-tributario con aplicacion profesional concreta.",
    "No asumir fuentes de semanas distintas sin validacion en consigna."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar consistencia entre metadatos de portada y programa analitico.",
    "Revisar placeholders o tokens sin resolver en README, .tex y .bib."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Completar plantilla antes de compilar: titulo, actividad, figura docente, authortable.",
    "Cerrar correctamente entornos truncados.",
    "Resolver tokens dinamicos sin expandir tipo $(@{...}.Slug) en README y programa analitico."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y normativa verificable.",
    "Registrar fuentes especificas por actividad en derecho-fiscal-y-tributario.bib.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Usar malla curricular solo para soporte de ubicacion curricular."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo abstracciones editoriales estables en relaciones transversales.",
    "Evitar mover redaccion literal o bibliografia tematica de otra materia.",
    "Aplicar estrategia conservadora: agregar mejoras verificables sin borrar reglas utiles previas.",
    "Mantener union-dedupe como metodo canonico de compresion."
  ],
  "open_questions": [
    "Confirmar consigna activa de la siguiente actividad en Derecho fiscal y tributario.",
    "Confirmar formato de citacion requerido por la asignatura.",
    "Confirmar si autor y matricula deben permanecer en plantilla compartida.",
    "Confirmar nombre de figura docente para cierre de portada.",
    "Confirmar resolucion definitiva de rutas truncadas en README.",
    "Supuesto: el .bib canonico local permanece como derecho-fiscal-y-tributario.bib."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Sobrio y profesional."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta de asignatura como entrada canonica.",
        "Supuestos etiquetados y trazables."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho fiscal y tributario.",
        "Semestre 6, bloque 1, obligatoria, 8 creditos.",
        "Clave local LDE-S6B1."
      ]
    },
    "essence": [
      "Problema juridico inicial.",
      "Marco conceptual y normativo pertinente.",
      "Analisis propio sustentado.",
      "Conclusion transferible a practica juridica.",
      "Consistencia tecnica entre .tex y .bib."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos evaluables y verificables.",
      "Preservar identidad institucional y calidad metodologica en cada entrega.",
      "Asegurar trazabilidad de fuentes y cierre argumentativo profesional."
    ],
    "style_markers": [
      "Frases directas y verificables.",
      "Sin relleno descriptivo.",
      "Supuestos explicitos cuando falte evidencia local.",
      "Cierre con implicacion juridica concreta."
    ],
    "argumentative_patterns": [
      "Problema breve -> objetivo puntual -> marco normativo -> analisis propio -> conclusion aplicada.",
      "Cada afirmacion relevante con respaldo o marca de supuesto.",
      "Coherencia estricta entre pregunta guia, desarrollo y cierre."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
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
          "justification": "La identidad institucional exige trazabilidad y formato consistente."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis necesita una cuestion juridica delimitada."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion profesional requiere fundamento normativo explicito."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Consistencia .tex/.bib",
          "kind": "develops",
          "justification": "La calidad estructural habilita validaciones tecnicas aguas abajo."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: ejes de trabajo y regla bibliografica local.",
        "Bib local: claves institucionales base verificables.",
        "Supuesto: no se transfiere bibliografia tematica de Filosofia como obligatoria en Fiscal."
      ]
    },
    "reinforcement_log": [
      "Ciclo 9: se consolida transferencia transversal por abstracciones estables.",
      "Ciclo 9: deduplicacion aplicada sin recorte semantico.",
      "Ciclo 9: se refuerzan gates de JSON, supuestos y consistencia cita-.bib.",
      "Ciclo 9: se preserva ADN institucional sin mezclar contenidos tematicos entre materias."
    ]
  }
}