{
  "summary": [
    "Se consolida memoria transversal minima para la materia destino con deduplicacion lossless.",
    "Se preservan reglas institucionales UnADM, normalizacion estructurada y control de supuestos.",
    "Se refuerza el marco reusable: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene alerta de tokens Slug sin expandir y nombres de archivo con artefactos en README/programa.",
    "Se evita transferir contenido doctrinal especifico de Filosofia del Derecho por no equivalencia disciplinar."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial de la materia destino en todos los artefactos.",
    "Usar Licenciatura en Derecho como programa academico.",
    "Respetar contexto curricular local: semestre 6, bloque 2, obligatoria, 8 creditos.",
    "Marcar como supuesto todo dato no confirmado por consigna o archivo local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Usar README de materia como entrada canonica.",
    "Definir objetivo puntual antes del desarrollo.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar desarrollo en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear el entregable al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Incluir el producto exacto solicitado por la actividad.",
    "No asumir fuentes de otras semanas sin confirmacion en la consigna.",
    "Agregar fuentes especificas de actividad al .bib local de la materia."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar memoria.",
    "No eliminar reglas utiles previas durante fusion por union-dedupe.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Corregir placeholders/tokens sin expandir antes de publicar entregables."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion.",
    "Compilar sin errores criticos, entornos truncados ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Actualizar documenttitle/documentsubtitle segun actividad concreta.",
    "Resolver tokens tipo $(@{...}.Slug) en README y programa analitico.",
    "Verificar que los nombres de archivos listados en README existan realmente."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos pertinentes a la actividad.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Distinguir bibliografia base de materia y bibliografia especifica de actividad.",
    "No citar fuentes ausentes en el .bib local."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo abstracciones editoriales estables, no redaccion literal.",
    "No propagar contenidos doctrinales propios de Filosofia del Derecho a otra materia sin evidencia local.",
    "Propagar primero identidad, estructura reusable, gates de calidad y grafo conceptual base.",
    "Mantener estrategia progresiva y conservadora: agregar solo mejoras verificables.",
    "Aplicar normalizacion manual previa cuando haya antecedente de salida no estructurada."
  ],
  "open_questions": [
    "Supuesto: falta consigna puntual de la primera actividad local de la materia destino.",
    "Confirmar formato prioritario por actividad: reporte, presentacion u otro producto.",
    "Confirmar si el autor de plantilla debe parametrizarse por actividad.",
    "Confirmar expansion final del Slug en README y programa analitico.",
    "Confirmar integridad del archivo .tex de reporte (posible truncamiento en entorno tabular)."
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
        "Carpeta de asignatura como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia destino en semestre 6, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica aplicable."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables academicos solidos y verificables.",
      "Asegurar trazabilidad entre consigna, argumentacion, evidencia y cierre juridico."
    ],
    "style_markers": [
      "Frases claras y directas.",
      "Supuestos marcados de forma explicita.",
      "Sin afirmaciones sin fuente.",
      "Cierre con transferencia a practica profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis propio -> conclusion.",
      "Marco normativo y doctrinal como soporte del criterio personal.",
      "Consistencia entre pregunta guia y respuesta final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Problema juridico",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Integridad bibliografica",
        "Control de supuestos"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura de entregables",
          "kind": "supports",
          "justification": "Define tono, formato y trazabilidad academica comunes."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin JSON valido no se propaga memoria de forma segura."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion requiere respaldo normativo y documental."
        },
        {
          "source": "Control de supuestos",
          "target": "Integridad argumentativa",
          "kind": "supports",
          "justification": "Separa hechos confirmados de inferencias provisionales."
        }
      ],
      "evidence": [
        "README local: pauta editorial y ubicacion curricular.",
        "Programa analitico local: ejes de trabajo y proposito de realizacion.",
        "Archivo .bib local: claves base institucionales verificables."
      ]
    },
    "reinforcement_log": [
      "Se preservaron reglas utiles previas del destino sin eliminacion.",
      "Se incorporaron abstracciones estables del origen sin transferir contenido tematico no equivalente.",
      "Se deduplicaron enunciados repetidos manteniendo cobertura funcional completa.",
      "Se abrio cerebro editorial minimo del destino en identity/essence/patterns/grafo."
    ]
  }
}