{
  "summary": [
    "Sincronizacion transversal aplicada con union-dedupe lossless y sin regresion.",
    "Se preserva identidad UnADM del nodo destino y su contexto curricular local.",
    "Se incorporan del origen solo abstracciones estables: objetivo, evidencia, analisis propio y coherencia argumentativa.",
    "Se mantiene bloqueo de propagacion para salidas no JSON parseables y normalizacion previa.",
    "Se refuerza resolucion de placeholders y rutas truncadas detectadas en README y programa analitico."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "No transferir metadatos curriculares especificos de otra asignatura."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco normativo/teorico, analisis propio y cierre.",
    "Alinear el producto al entregable solicitado en la planeacion semanal.",
    "Distinguir artefactos: reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias canonicas de estructura."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Cerrar con conclusion transferible a la practica juridica.",
    "Evitar trasladar contenido tematico exclusivo de Filosofia del Derecho a Antropologia sin puente conceptual."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar esquema minimo completo antes de reutilizar memoria.",
    "Revisar y normalizar manualmente respuestas no estructuradas antes de propagar.",
    "Confirmar que toda afirmacion tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregado y consigna real."
  ],
  "latex_rules": [
    "Usar configuracion en espanol y acentos correctos en .tex y .bib.",
    "Mantener clase y formato base salvo justificacion academica.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Mantener claves BibTeX estables para evitar roturas.",
    "Compilar sin errores criticos, sin referencias rotas y sin tokens sin expandir.",
    "Resolver placeholders tipo $(@{...}.Slug) en README, programa y rutas de archivos.",
    "Corregir nombres truncados de archivo detectados como supuesto en README (ej. lineas con inicial omitida)."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables y consultables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Agregar fuentes especificas por actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Mantener trazabilidad de procedencia para archivos locales en assets-unadm."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y abstraidas.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "No propagar redaccion literal ni contenido tematico dependiente de asignatura origen.",
    "Preservar reglas utiles previas; solo agregar mejoras verificables.",
    "Registrar incidencias de parseo y placeholders como alertas transversales reutilizables."
  ],
  "open_questions": [
    "Supuesto: confirmar si LDE-S4B2 es clave oficial institucional o clave local.",
    "Supuesto: confirmar formato de citacion oficial unico para la licenciatura.",
    "Confirmar rubrica de evaluacion de actividades para calibrar profundidad argumentativa.",
    "Supuesto: confirmar correccion definitiva de nombres truncados en README de la materia.",
    "Confirmar si toda actividad de Antropologia exige conclusion juridica explicita."
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
        "Integridad academica con citas verificables.",
        "Entrada canonica por carpeta de materia."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 4, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Antropologia de la cultura en Mexico."
      ]
    },
    "essence": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Normalizacion estructurada antes de propagacion.",
      "Compresion lossless por union y deduplicacion.",
      "Transferencia transversal de abstracciones estables, no de contenido literal."
    ],
    "reason_for_being": [
      "Guiar productos academicos trazables, coherentes y transferibles a practica juridica.",
      "Asegurar continuidad editorial institucional entre nodos heterogeneos."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Afirmacion -> fuente verificable -> interpretacion propia.",
      "Pregunta guia -> desarrollo coherente -> conclusion.",
      "Analisis propio sustentado, no resumen descriptivo."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Validacion JSON parseable",
        "Normalizacion estructurada",
        "Propagacion transversal conservadora"
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
          "justification": "Sin parseo valido no hay memoria reutilizable confiable."
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
          "justification": "La conclusion deriva del razonamiento, no de la descripcion."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige trazabilidad y rigor."
        }
      ],
      "evidence": [
        "README destino establece identidad UnADM y punto de entrada canonico.",
        "Programa analitico destino fija ejes problema, conceptos, producto, analisis y cierre.",
        "Bibliografia local contiene unadmSitioWeb y unadmMallaDerecho2024.",
        "Origen aporta reglas estables de objetivo puntual, evidencia y coherencia argumentativa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 45: se consolidan reglas transversales estables desde actividad de Filosofia del Derecho.",
      "Ciclo 45: se evita transferir contenido tematico exclusivo del origen.",
      "Ciclo 45: se mantienen alertas de parseo JSON y normalizacion manual como gates permanentes.",
      "Ciclo 45: se refuerza control de placeholders y rutas truncadas como riesgo tecnico-editorial."
    ]
  }
}