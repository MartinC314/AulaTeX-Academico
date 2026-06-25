{
  "summary": [
    "Se consolida sincronizacion transversal conservadora desde actividad de otra materia hacia cerebro de materia destino.",
    "Se preservan reglas utiles previas sin regresion y con deduplicacion lossless.",
    "Se transfieren solo abstracciones estables: identidad UnADM, estructura reusable, gates de calidad y trazabilidad.",
    "Se mantiene exclusion de contenido doctrinal especifico de Filosofia del Derecho por no equivalencia disciplinar.",
    "Se refuerza control de placeholders Slug y artefactos de nombres en README y programa analitico.",
    "Se mantiene alerta de posible truncamiento del .tex principal local como riesgo operativo."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial de la materia destino en todos los entregables.",
    "Usar Licenciatura en Derecho como programa academico comun.",
    "Respetar contexto curricular local confirmado: semestre 6, bloque 2, obligatoria, 8 creditos.",
    "Marcar como supuesto todo dato no visible en consigna o archivos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Usar carpeta de materia como entrada canonica."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar desarrollo en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear producto final a lo pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Mantener correspondencia entre README, .tex de reporte, .tex de presentacion y .bib.",
    "Corregir tokens sin expandir y nombres de archivo con artefactos antes de producir entregables."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante y evitar solo resumen descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Registrar fuentes especificas por actividad en el .bib local.",
    "No asumir fuentes de otras semanas o materias como aplicables automaticamente.",
    "Conectar cierre con aplicacion practica en contexto juridico-profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Exigir estructura minima completa antes de reutilizar memoria.",
    "No eliminar reglas utiles previas durante fusion por union-dedupe.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y claves en .bib.",
    "Revisar y normalizar respuestas no estructuradas antes de propagacion recursiva.",
    "Verificar que el README liste rutas y archivos reales."
  ],
  "latex_rules": [
    "Usar espanol con acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Actualizar documenttitle y documentsubtitle segun actividad real.",
    "Resolver tokens tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir artefactos de salto en nombres de archivo.",
    "Validar cierre de entornos LaTeX en archivo de reporte local. [supuesto: archivo truncado]"
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas pertinentes a la actividad.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente editorial o URL.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "No citar claves ausentes del .bib local.",
    "Conservar claves base locales institucionales sin renombrado innecesario."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo reglas abstractas y estables entre materias no equivalentes.",
    "No propagar contenido doctrinal especifico de una materia a otra.",
    "Priorizar en propagacion: identidad, estructura reusable, quality gates y grafo conceptual.",
    "Aplicar normalizacion manual en ciclos con antecedente de salida no estructurada.",
    "Mantener estrategia progresiva y conservadora: agregar solo mejoras verificables.",
    "Escalar reglas locales solo cuando no exista conflicto curricular."
  ],
  "open_questions": [
    "Confirmar consigna real de la primera actividad de la materia destino para ajustar artefacto requerido.",
    "Confirmar si el autor visible en plantilla debe parametrizarse por actividad.",
    "Confirmar valor final de year en unadmSitioWeb como dato bibliografico vs fecha de consulta.",
    "Confirmar reparacion definitiva de tokens Slug en README y programa analitico.",
    "Confirmar si el .tex principal esta truncado en repositorio o solo en captura local."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico",
        "Claro y juridicamente preciso",
        "Argumentativo con criterio propio"
      ],
      "institutional": [
        "Alineacion explicita con UnADM",
        "Integridad academica con trazabilidad bibliografica",
        "Entrada canonica por carpeta de materia"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Semestre 6 bloque 2 obligatoria 8 creditos",
        "Transferencia profesional como criterio de cierre"
      ]
    },
    "essence": [
      "Problema juridico",
      "Conceptos y marco de soporte",
      "Evidencia verificable",
      "Analisis propio",
      "Conclusion juridica transferible",
      "Control estricto de supuestos"
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables academicos solidos y verificables.",
      "Garantizar coherencia entre identidad institucional, rigor argumentativo y ejecucion tecnica LaTeX."
    ],
    "style_markers": [
      "Frases directas y accionables",
      "Supuestos etiquetados",
      "Sin afirmaciones sin fuente",
      "Cierre aplicado a practica juridica"
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis propio -> conclusion",
      "Marco normativo y doctrinal como soporte del criterio personal",
      "Consistencia integral entre pregunta guia y cierre"
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Control de supuestos",
        "Evidencia verificable",
        "Conclusion juridica transferible",
        "Correspondencia README-tex-bib",
        "Higiene de plantillas y tokens"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin JSON valido no hay transferencia segura."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion exige respaldo documental."
        },
        {
          "source": "Control de supuestos",
          "target": "Integridad argumentativa",
          "kind": "supports",
          "justification": "Diferencia hechos confirmados de inferencias."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura de entregables",
          "kind": "supports",
          "justification": "Fija tono, formato y consistencia editorial."
        },
        {
          "source": "Higiene de plantillas y tokens",
          "target": "Correspondencia README-tex-bib",
          "kind": "supports",
          "justification": "Evita errores operativos y rupturas de compilacion."
        }
      ],
      "evidence": [
        "README local con ubicacion curricular y pauta editorial.",
        "Programa analitico local con ejes de trabajo reutilizables.",
        "Archivo .bib local con claves institucionales base.",
        "Antecedentes de salidas no parseables en ciclos previos."
      ]
    },
    "reinforcement_log": [
      "Ciclo 9: se refuerza marco transversal reusable sin importar disciplina especifica.",
      "Ciclo 9: se conserva regla dura de JSON parseable como gate previo a propagacion.",
      "Ciclo 9: se mantiene exclusion de transferencia doctrinal no equivalente.",
      "Ciclo 9: se refuerza control de Slug sin expandir y artefactos de archivo.",
      "Ciclo 9: se preserva union-dedupe sin recorte y sin borrar reglas utiles previas."
    ]
  }
}