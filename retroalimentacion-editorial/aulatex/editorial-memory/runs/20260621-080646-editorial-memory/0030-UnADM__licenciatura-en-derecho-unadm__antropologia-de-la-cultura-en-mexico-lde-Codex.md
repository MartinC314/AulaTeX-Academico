{
  "summary": [
    "Se consolida sincronizacion transversal desde actividad de Filosofia del Derecho hacia materia de Antropologia con union-dedupe lossless.",
    "Se preservan reglas institucionales UnADM y se evitan traslados tematicos no equivalentes.",
    "Se refuerzan gates de JSON parseable, normalizacion estructurada y trazabilidad de fuentes.",
    "Se mantiene pauta base: problema, conceptos, evidencia, analisis propio y conclusion transferible.",
    "Se confirma contexto local del destino con semestre 4, bloque 2, obligatoria, 8 creditos [verificado en README]."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener datos curriculares del destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "No transferir metadatos curriculares especificos de Filosofia del Derecho al destino."
  ],
  "structure_rules": [
    "Abrir cada entrega con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones reutilizables: conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear el artefacto al producto solicitado por la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Resolver placeholders de nombres de archivo en README y programa antes de usar rutas."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar solo resumen.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion.",
    "Evitar extrapolar fuentes de otras semanas o materias sin justificacion.",
    "Cerrar con conclusion transferible a la practica juridica cuando la consigna lo permita [supuesto]."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar esquema minimo completo antes de reutilizar memoria.",
    "Normalizar manualmente respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que afirmaciones no verificadas esten marcadas como supuesto.",
    "Verificar consistencia entre citas en texto y archivo .bib.",
    "Comprobar que el producto final corresponda a la consigna activa."
  ],
  "latex_rules": [
    "Mantener plantilla .tex local de la materia como base.",
    "Usar configuracion en espanol con acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir rutas con caracteres truncados y tokens dinamicos sin expandir."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo materiales consultables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales pertinentes.",
    "Registrar fuentes especificas por actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "No citar entradas ausentes del .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas estables y validadas.",
    "Transferir abstracciones editoriales, no redaccion literal ni contenido tematico de otra asignatura.",
    "Preservar reglas utiles previas sin regresion en cada ciclo.",
    "Mantener estrategia conservadora: marcar provisional todo elemento heredado no confirmado.",
    "Registrar incidencias de parseo como alertas reutilizables inter-nodos."
  ],
  "open_questions": [
    "Confirmar rubrica oficial de evaluacion para la materia destino.",
    "Confirmar estandar unico de citacion institucional (APA u otro).",
    "Confirmar si toda actividad de la materia exige conclusion juridica explicita [supuesto].",
    "Confirmar si LDE-S4B2 es clave oficial o convencion local.",
    "Confirmar si hay fuentes base obligatorias adicionales a unadmSitioWeb y unadmMallaDerecho2024."
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
        "Asignatura destino: Antropologia de la cultura en Mexico.",
        "Semestre 4, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema.",
      "Conceptos.",
      "Evidencia.",
      "Analisis propio.",
      "Conclusion transferible.",
      "Normalizacion estructurada previa a propagacion."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables y utiles profesionalmente.",
      "Sostener coherencia institucional y calidad transversal entre nodos."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales estables.",
      "Supuestos marcados.",
      "Cierre con valor aplicado."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente verificable -> interpretacion propia.",
      "Coherencia entre pregunta guia y respuesta final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Validacion JSON parseable",
        "Normalizacion estructurada",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion transferible"
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
          "justification": "Sin parseo valido no hay propagacion confiable."
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
          "justification": "La conclusion aplicada deriva del razonamiento y no del resumen."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y consistencia formal."
        }
      ],
      "evidence": [
        "README destino confirma identidad UnADM y datos curriculares.",
        "Programa analitico confirma ejes de trabajo reutilizables.",
        "Bib local confirma fuentes base institucionales verificables.",
        "Memoria origen confirma gate de JSON parseable y normalizacion obligatoria."
      ]
    },
    "reinforcement_log": [
      "Ciclo 30: deduplicacion completa sin eliminar reglas utiles previas.",
      "Ciclo 30: transferencia limitada a abstracciones estables por relacion transversal.",
      "Ciclo 30: se excluye contenido tematico especifico de Filosofia del Derecho por no equivalencia de nodo."
    ]
  }
}