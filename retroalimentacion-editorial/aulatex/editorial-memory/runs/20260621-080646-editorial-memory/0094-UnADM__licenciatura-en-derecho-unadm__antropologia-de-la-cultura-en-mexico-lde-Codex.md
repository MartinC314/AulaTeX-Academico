{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia conservadora y union-dedupe lossless.",
    "Se preservan reglas institucionales UnADM, estructura canonica y control de calidad JSON.",
    "Se transfieren solo abstracciones estables del origen: objetivo, evidencia, analisis propio y cierre.",
    "Se evita migrar contenido tematico especifico de Filosofia del Derecho al nodo de Antropologia.",
    "Se mantiene alerta por salidas no parseables heredadas y normalizacion manual cuando aplique."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Usar nombre de materia: Antropologia de la cultura en Mexico.",
    "Conservar ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales.",
    "No transferir metadatos curriculares de otras materias."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear producto al entregable solicitado por la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias de estructura reusable.",
    "Cerrar con conclusion transferible a la practica juridica."
  ],
  "activity_rules": [
    "Sustentar afirmaciones relevantes con fuente verificable y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion.",
    "Evitar entregas solo descriptivas.",
    "Integrar conceptos culturales y juridicos con puente argumentativo explicito."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa del esquema antes de reutilizar.",
    "Revisar y normalizar respuestas no estructuradas antes de propagar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Verificar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto final y consigna real."
  ],
  "latex_rules": [
    "Usar configuracion en espanol coherente con plantilla local.",
    "Mantener clase y formato base salvo justificacion academica.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Mantener coursename y coursecode locales salvo instruccion institucional.",
    "Resolver tokens dinamicos sin expandir en README, programa y rutas.",
    "Corregir rutas con caracteres truncados antes de compilar.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes especificas de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No citar claves ausentes en .bib."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y abstractas.",
    "Mantener union-dedupe sin eliminar reglas utiles previas.",
    "Etiquetar incidencias de parseo como alertas reutilizables inter-nodos.",
    "No propagar contenido tematico de una materia a otra no equivalente.",
    "Transferir identidad, patrones argumentativos, gates y grafo conceptual estable.",
    "Si falta contexto local, conservar cerebro minimo y abrir vacios como preguntas."
  ],
  "open_questions": [
    "Supuesto: confirmar si LDE-S4B2 es clave oficial o local.",
    "Confirmar rubrica de evaluacion por actividad en la materia destino.",
    "Confirmar estandar de citacion institucional unico para la licenciatura.",
    "Confirmar si toda actividad de la materia exige conclusion juridica explicita.",
    "Supuesto: validar si persiste necesidad de normalizacion manual en nodos heredados con historial no estructurado."
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
        "Integridad academica con trazabilidad.",
        "Entrada canonica por carpeta de materia."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 4, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Antropologia de la cultura en Mexico."
      ]
    },
    "essence": [
      "Problema claro.",
      "Conceptos pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables academicos trazables.",
      "Asegurar coherencia entre consigna, desarrollo y cierre.",
      "Preservar calidad institucional en cada actividad."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados cuando falte evidencia.",
      "Cierre con valor profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente -> interpretacion propia.",
      "Consigna -> desarrollo alineado -> verificacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Validacion JSON parseable",
        "Normalizacion estructurada",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Supuestos marcados"
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
          "source": "Integridad academica",
          "target": "Evidencia verificable",
          "kind": "depends_on",
          "justification": "La integridad exige trazabilidad de fuentes."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "El criterio personal se fortalece con respaldo."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion util deriva del razonamiento."
        },
        {
          "source": "Supuestos marcados",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita presentar inferencias como hechos."
        }
      ],
      "evidence": [
        "README local confirma identidad UnADM y punto de entrada canonico.",
        "Programa analitico local fija ejes: problema, conceptos, producto, analisis y cierre.",
        "Bib local contiene fuentes base institucionales verificables.",
        "Historial heredado confirma necesidad de gate JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 94: se consolidan reglas transversales estables sin regresion.",
      "Ciclo 94: se refuerza bloqueo por JSON no parseable y normalizacion previa.",
      "Ciclo 94: se preserva separacion entre identidad curricular local y transferencia abstracta.",
      "Ciclo 94: se mantiene politica de no inventar fuentes y marcar supuestos."
    ]
  }
}