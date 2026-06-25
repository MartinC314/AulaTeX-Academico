{
  "summary": [
    "Sincronizacion transversal completada con union-dedupe lossless y sin regresion.",
    "Se preserva identidad UnADM y contexto curricular local de Antropologia.",
    "Se incorporan del origen solo abstracciones estables: objetivo, evidencia, postura propia y coherencia.",
    "Se mantiene bloqueo de propagacion ante salida no JSON parseable.",
    "Se refuerza normalizacion de placeholders y rutas corruptas en README, programa y archivos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar materia destino: Antropologia de la cultura en Mexico.",
    "Conservar adscripcion: Licenciatura en Derecho.",
    "Conservar ubicacion local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna.",
    "Tratar como provisionales las fuentes heredadas no verificadas."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco teorico/normativo, analisis propio y cierre.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias canonicas de estructura."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Evitar trasplante de contenidos tematicos de Filosofia del Derecho sin pertinencia local.",
    "Cerrar con conclusion transferible a la practica juridica con sensibilidad cultural."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que cada afirmacion tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre metadatos del documento y contexto curricular local."
  ],
  "latex_rules": [
    "Usar configuracion en espanol coherente con plantilla local.",
    "Mantener clase article, letterpaper y oneside salvo instruccion valida distinta.",
    "Actualizar documenttitle y documentsubtitle por actividad real.",
    "Conservar coursename y documentsubject segun materia destino.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Resolver tokens tipo $(@{...}.Slug) a nombre literal antes de compilar.",
    "Corregir rutas con caracteres truncados antes de compilar."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Usar solo obras verificables y consultables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales pertinentes.",
    "Registrar fuentes especificas de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y abstractas.",
    "No transferir metadatos curriculares de una materia a otra.",
    "Reusar gates institucionales de parseo, trazabilidad y normalizacion.",
    "Marcar como provisional cualquier regla heredada sin verificacion local.",
    "Mantener estrategia progresiva y conservadora en ciclos siguientes."
  ],
  "open_questions": [
    "Supuesto: falta consigna local de actividades especificas de Antropologia; confirmar productos por semana.",
    "Confirmar si la clave LDE-S4B2 es oficial institucional o solo local.",
    "Confirmar estandar unico de citacion para toda la Licenciatura.",
    "Confirmar si toda actividad exige cierre juridico explicito o puede variar por rubrica.",
    "Confirmar si el nombre final del .bib queda fijo sin plantillas dinamicas."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y preciso.",
        "Argumentativo con criterio propio.",
        "Culturalmente sensible y juridicamente pertinente."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con trazabilidad de fuentes.",
        "Normalizacion estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Antropologia de la cultura en Mexico.",
        "Semestre 4, bloque 2, obligatoria, 8 creditos."
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
      "Transformar planeacion semanal en productos academicos verificables y utiles para la practica juridica.",
      "Asegurar consistencia editorial transversal entre nodos sin perder contexto local."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Cierre con valor profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente verificable -> interpretacion propia.",
      "Coherencia completa entre pregunta guia y respuesta final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON parseable",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Pertinencia cultural en contexto juridico"
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
          "justification": "La postura personal requiere respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion util surge del razonamiento argumentado."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "La pauta institucional exige integridad academica."
        },
        {
          "source": "Pertinencia cultural en contexto juridico",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La aplicacion juridica mejora con lectura cultural contextual."
        }
      ],
      "evidence": [
        "README de materia destino: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico destino: ejes de trabajo y proposito de realizacion.",
        "Bib local destino: unadmSitioWeb y unadmMallaDerecho2024.",
        "Memoria origen: gates de JSON, estructura argumentativa y no invencion de fuentes."
      ]
    },
    "reinforcement_log": [
      "Ciclo 10: se preservan reglas utiles previas sin eliminacion.",
      "Ciclo 10: se deduplican reglas repetidas y se compactan en forma accionable.",
      "Ciclo 10: se transfiere solo capa abstracta estable desde Filosofia del Derecho.",
      "Ciclo 10: se evita traslado de contenidos tematicos no equivalentes entre materias.",
      "Ciclo 10: se refuerzan gates de parseo JSON y consistencia bib/tex."
    ]
  }
}