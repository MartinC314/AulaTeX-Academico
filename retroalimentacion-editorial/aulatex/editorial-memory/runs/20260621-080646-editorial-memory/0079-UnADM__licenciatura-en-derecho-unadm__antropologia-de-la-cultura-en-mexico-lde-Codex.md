{
  "summary": [
    "Sincronizacion transversal aplicada desde actividad de otra materia con transferencia solo de abstracciones estables.",
    "Se preserva identidad UnADM y contexto curricular local de Antropologia de la cultura en Mexico.",
    "Se refuerzan ejes reutilizables: problema, conceptos, evidencia, analisis propio y conclusion transferible.",
    "Se mantiene regla dura de normalizacion estructurada y JSON parseable antes de propagar.",
    "Se evita trasladar contenido tematico especifico de Filosofia del Derecho al nodo destino."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Usar datos curriculares locales del destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de la materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar toda fuente heredada no verificada como provisional."
  ],
  "structure_rules": [
    "Iniciar cada producto con objetivo puntual y encuadre del problema juridico o social.",
    "Organizar desarrollo en secciones: conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear siempre el formato de entrega con la planeacion semanal.",
    "Separar artefactos de reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias de estructura reusable."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Evitar extrapolar fuentes de otras semanas o materias sin justificacion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar esquema minimo completo antes de reutilizar memoria.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Verificar consistencia entre citas en texto y archivo .bib local.",
    "No promover reglas provisionales a definitivas sin validacion local disciplinar."
  ],
  "latex_rules": [
    "Mantener plantilla base .tex de la materia y metadatos institucionales completos.",
    "Usar configuracion en espanol y acentos correctos en .tex y .bib.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver placeholders y tokens dinamicos en README, programa y rutas de archivos.",
    "Evitar comandos no estandar sin justificacion editorial."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias consultables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales pertinentes.",
    "Registrar fuentes especificas de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y abstraidas.",
    "Transferir patrones editoriales, no redaccion literal ni temas exclusivos de otra materia.",
    "Mantener estrategia conservadora: agregar mejoras verificables sin borrar reglas utiles previas.",
    "Registrar incidencias de parseo como alertas reutilizables inter-nodos.",
    "Si falta contexto local en nodos hijos, crear memoria minima y dejar vacios como preguntas abiertas."
  ],
  "open_questions": [
    "Supuesto: falta consigna puntual de la siguiente actividad del destino; confirmar producto exacto.",
    "Confirmar rubrica de evaluacion vigente para ajustar profundidad argumentativa.",
    "Confirmar estandar de citacion oficial de la licenciatura.",
    "Confirmar si la conclusion juridica es obligatoria en todas las actividades de esta materia.",
    "Confirmar si la clave LDE-S4B2 es institucional o solo operativa local."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con trazabilidad de fuentes.",
        "Entrada canonica por carpeta de materia."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Antropologia de la cultura en Mexico.",
        "Semestre 4, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema relevante.",
      "Conceptos pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento, evidencia y criterio propio.",
      "Sostener coherencia institucional y calidad tecnica en cada entrega."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados cuando falte evidencia directa.",
      "Cierre con utilidad academica y profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente verificable -> interpretacion propia.",
      "Pregunta guia -> desarrollo coherente -> respuesta final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON parseable",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion transferible",
        "Transferencia transversal conservadora"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Validacion JSON parseable",
          "target": "Normalizacion estructurada",
          "kind": "depends_on",
          "justification": "La memoria solo se propaga con estructura confiable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura academica requiere respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "El cierre util surge del razonamiento argumentado."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Transferencia transversal conservadora",
          "kind": "supports",
          "justification": "La identidad fija los limites de lo que puede heredarse."
        }
      ],
      "evidence": [
        "README local confirma identidad UnADM y pauta editorial.",
        "Programa analitico confirma ejes de trabajo reutilizables.",
        "Bib local confirma fuentes base institucionales verificables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 79: se consolidan patrones estables del origen sin importar contenido tematico ajeno.",
      "Ciclo 79: se mantiene politica de no regresion y union-dedupe lossless.",
      "Ciclo 79: se refuerza gate de JSON parseable como condicion previa de propagacion."
    ]
  }
}