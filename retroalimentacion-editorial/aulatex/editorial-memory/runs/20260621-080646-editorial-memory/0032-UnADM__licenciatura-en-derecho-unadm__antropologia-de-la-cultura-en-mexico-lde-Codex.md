{
  "summary": [
    "Sincronizacion transversal aplicada con union-dedupe lossless entre actividad de origen y materia destino.",
    "Se preservan reglas utiles previas del destino y se agregan abstracciones estables del origen sin arrastrar contenido tematico ajeno.",
    "Se refuerza ADN editorial UnADM: problema, conceptos, evidencia, analisis propio y cierre transferible.",
    "Se mantiene bloqueo de propagacion ante salida no JSON parseable y normalizacion estructurada obligatoria.",
    "Se conserva contexto curricular local del destino: semestre 4, bloque 2, obligatoria, 8 creditos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Usar la carpeta de materia como entrada canonica.",
    "Conservar ubicacion curricular local del destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar nombre de materia exacto: Antropologia de la cultura en Mexico.",
    "Usar clave local LDE-S4B2 salvo confirmacion institucional distinta.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar toda fuente heredada no verificada como provisional.",
    "No transferir metadatos curriculares especificos de Filosofia del Derecho al destino."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias de estructura reusable.",
    "Cerrar con conclusion transferible a la practica juridica."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Evitar analisis meramente descriptivo.",
    "Integrar conceptos antropologicos y juridicos con puente argumentativo claro.",
    "No asumir fuentes de otras semanas o materias sin validacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa del esquema antes de reutilizar.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Comprobar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna real de la actividad.",
    "No promover reglas provisionales a definitivas sin verificacion disciplinar."
  ],
  "latex_rules": [
    "Mantener plantilla .tex local como base de la materia destino.",
    "Usar codificacion en espanol con acentos consistentes en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver placeholders y tokens dinamicos tipo $(@{...}.Slug) en README, programa y rutas.",
    "Corregir nombres de archivo truncados o corruptos antes de compilar."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales pertinentes.",
    "Registrar fuentes especificas por actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "No citar fuentes ausentes en el .bib local.",
    "Mantener unadmSitioWeb y unadmMallaDerecho2024 como base institucional."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y parseables.",
    "Transferir entre nodos no equivalentes solo abstracciones editoriales estables.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferencia literal de redaccion o contenidos tematicos exclusivos del origen.",
    "Registrar incidencias de parseo como alerta transversal reutilizable.",
    "Aplicar estrategia conservadora: agregar solo mejoras verificables sin borrar reglas utiles."
  ],
  "open_questions": [
    "Supuesto: falta consigna puntual de actividades concretas en destino; confirmar producto exacto por semana.",
    "Confirmar estandar institucional unico de citacion para la licenciatura.",
    "Confirmar si LDE-S4B2 es clave oficial o convenio local.",
    "Confirmar si toda actividad del destino exige cierre juridico explicito.",
    "Confirmar si persisten reglas heredadas desde ingenieria con alcance vigente en Derecho."
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
        "Asignatura destino: Antropologia de la cultura en Mexico."
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
      "Convertir planeacion semanal en productos academicos solidos y verificables.",
      "Sostener coherencia institucional y calidad editorial entre actividades y materias."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos siempre marcados.",
      "Cierre con valor profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente -> interpretacion propia.",
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
        "Sincronizacion transversal conservadora"
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
          "justification": "Sin parseo valido no hay reutilizacion confiable."
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
          "justification": "El cierre util deriva del razonamiento, no del resumen."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Sincronizacion transversal conservadora",
          "kind": "supports",
          "justification": "La identidad comun permite reglas reusables entre nodos distintos."
        }
      ],
      "evidence": [
        "README de materia destino con pauta editorial UnADM.",
        "Programa analitico destino con ejes problema-conceptos-evidencia-analisis-cierre.",
        "Regla heredada estable de bloqueo por JSON no parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 32: deduplicacion completa de reglas repetidas.",
      "Ciclo 32: transferencia transversal limitada a abstracciones estables.",
      "Ciclo 32: preservadas reglas de parseo, supuestos y trazabilidad sin regresion.",
      "Ciclo 32: excluidos contenidos tematicos especificos de Filosofia del Derecho por no equivalencia de nodo."
    ]
  }
}