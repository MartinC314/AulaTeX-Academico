{
  "summary": [
    "Sincronizacion transversal ciclo 37 aplicada con union-dedupe lossless y sin regresion.",
    "Se preserva identidad UnADM del nodo destino y su contexto curricular local.",
    "Se incorporan del origen solo abstracciones estables: objetivo, evidencia, analisis propio, coherencia y cierre.",
    "Se mantiene bloqueo de propagacion ante salidas no JSON parseable y normalizacion obligatoria.",
    "Se refuerza resolucion de placeholders y rutas corruptas detectadas en README y programa analitico."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Usar materia destino: Antropologia de la cultura en Mexico.",
    "Conservar ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar clave LDE-S4B2 salvo instruccion institucional distinta.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar toda fuente heredada no verificada como provisional."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear el producto al entregable solicitado en la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias canonicas de estructura."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Integrar conceptos antropologicos, culturales y juridicos con puente argumentativo.",
    "Cerrar con conclusion transferible a la practica juridica."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar memoria.",
    "Normalizar manualmente respuestas no estructuradas antes de propagar.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregado y consigna real."
  ],
  "latex_rules": [
    "Mantener plantilla .tex local de la materia como base.",
    "Conservar configuracion en espanol y compatibilidad de acentos en .tex y .bib.",
    "Mantener clase article, letterpaper y oneside salvo justificacion.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README, programa y rutas.",
    "Corregir nombres o rutas truncadas antes de compilar.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes consultables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales pertinentes.",
    "Registrar fuentes de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No citar claves inexistentes en el .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y abstraidas.",
    "No transferir contenido tematico exclusivo de Filosofia del Derecho.",
    "Transferir patrones editoriales estables: estructura, calidad, trazabilidad y argumentacion.",
    "Mantener etiquetas de provisionalidad para herencias no verificadas.",
    "Preservar reglas utiles previas; solo agregar mejoras verificables.",
    "Registrar incidencias de parseo como alerta transversal reutilizable."
  ],
  "open_questions": [
    "Supuesto: falta consigna puntual de actividades locales; confirmar formato exacto por semana.",
    "Confirmar estandar unico de citacion institucional para la licenciatura.",
    "Confirmar si la conclusion juridica es obligatoria en todas las actividades de la materia.",
    "Confirmar si LDE-S4B2 es clave oficial o solo convencion local.",
    "Confirmar limpieza definitiva de placeholders en todos los artefactos del nodo."
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
        "Semestre 4, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Antropologia de la cultura en Mexico."
      ]
    },
    "essence": [
      "Problema.",
      "Conceptos.",
      "Evidencia.",
      "Analisis propio.",
      "Conclusion transferible."
    ],
    "reason_for_being": [
      "Convertir la planeacion semanal en productos academicos verificables y utiles para la practica juridica."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados cuando falte evidencia.",
      "Cierre con valor profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente verificable -> interpretacion propia.",
      "Consigna -> desarrollo alineado -> cierre coherente."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON parseable",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Resolucion de placeholders"
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
          "justification": "Sin parseo valido no hay reutilizacion segura."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura academica requiere respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion util deriva del razonamiento, no del resumen."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "La pauta institucional exige integridad academica."
        },
        {
          "source": "Resolucion de placeholders",
          "target": "Normalizacion estructurada",
          "kind": "supports",
          "justification": "Evita rutas invalidas y errores de compilacion."
        }
      ],
      "evidence": [
        "README de materia destino.",
        "Programa analitico de materia destino.",
        "antropologia-de-la-cultura-en-mexico.bib.",
        "Regla heredada: bloquear salida no JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin perdida semantica.",
      "Se conservaron gates criticos de parseo y estructura.",
      "Se agrego puente transversal de patrones argumentativos desde el origen.",
      "Se excluyo contenido doctrinal especifico de Filosofia del Derecho por no equivalencia de nodo.",
      "Se reforzo control de supuestos y provisionalidad de fuentes heredadas."
    ]
  }
}