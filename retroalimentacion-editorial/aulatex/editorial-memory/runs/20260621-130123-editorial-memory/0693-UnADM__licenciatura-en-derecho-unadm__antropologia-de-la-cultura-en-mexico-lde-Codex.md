{
  "summary": [
    "Sincronizacion transversal completada con union-dedupe lossless y sin regresion.",
    "Se preserva identidad UnADM y contexto local de Antropologia de la cultura en Mexico.",
    "Se integran del origen solo abstracciones estables: objetivo, evidencia, analisis propio y coherencia argumentativa.",
    "Se mantiene bloqueo de propagacion ante salida no JSON parseable.",
    "Se refuerza normalizacion de placeholders en README, programa y rutas bibliograficas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener contexto curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar toda fuente heredada no verificada como provisional hasta validacion local.",
    "No trasladar metadatos curriculares especificos de Filosofia del Derecho al destino."
  ],
  "structure_rules": [
    "Iniciar cada entrega con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear el producto al entregable solicitado en la planeacion semanal.",
    "Separar artefactos: reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias canonicas de estructura.",
    "Resolver nombres con placeholders dinamicos a rutas literales antes de compilar."
  ],
  "activity_rules": [
    "Sustentar afirmaciones relevantes con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Evitar extrapolar fuentes o contenidos de semanas no confirmadas.",
    "Cerrar con conclusion transferible a la practica juridica y social del contexto de la materia."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Exigir estructura minima completa del esquema antes de reutilizar memoria.",
    "Normalizar manualmente salidas no estructuradas antes de aplicar aguas abajo.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregado y consigna real de la actividad.",
    "Confirmar que supuestos esten marcados de forma explicita.",
    "No promover reglas provisionales a definitivas sin validacion disciplinar local."
  ],
  "latex_rules": [
    "Mantener plantilla .tex local como base.",
    "Conservar configuracion en espanol y acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir caracteres truncados en rutas o nombres de archivo.",
    "Resolver tokens tipo $(@{...}.Slug) en README, programa y referencias de archivos."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales pertinentes.",
    "Registrar fuentes especificas por actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Mantener trazabilidad de activos locales citados en assets-unadm."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y abstractas entre nodos no equivalentes.",
    "Priorizar identidad, gates de calidad, estructura reusable y grafo conceptual.",
    "Evitar transferir redaccion literal o contenidos tematicos exclusivos de otra asignatura.",
    "Conservar alertas de parseo como conocimiento institucional reutilizable.",
    "Aplicar estrategia progresiva y conservadora: agregar solo mejoras verificables."
  ],
  "open_questions": [
    "Supuesto: falta consigna puntual de actividades locales de Antropologia; confirmar formato exigido por semana.",
    "Confirmar estandar institucional de citacion unico para la licenciatura.",
    "Confirmar si la clave LDE-S4B2 es oficial o convencional local.",
    "Confirmar si toda actividad debe cerrar con conclusion juridica o con cierre interdisciplinario ajustado.",
    "Confirmar si existe rubrica formal de evaluacion para calibrar profundidad argumentativa."
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
        "Asignatura: Antropologia de la cultura en Mexico.",
        "Semestre 4, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema relevante.",
      "Conceptos y marco pertinente.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Cierre transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables, argumentados y utiles para la formacion juridica."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos etiquetados.",
      "Conclusiones con aplicacion practica."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente verificable -> interpretacion propia.",
      "Consigna -> desarrollo alineado -> cierre coherente."
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
          "justification": "La propagacion confiable requiere parseo valido."
        },
        {
          "source": "Integridad academica",
          "target": "Evidencia verificable",
          "kind": "depends_on",
          "justification": "La integridad exige respaldo trazable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "El analisis gana solidez con fuentes comprobables."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion aplicable surge del razonamiento."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige calidad y trazabilidad."
        }
      ],
      "evidence": [
        "README de la materia destino.",
        "Programa analitico de la materia destino.",
        "Archivo antropologia-de-la-cultura-en-mexico.bib.",
        "Regla consolidada de bloqueo por no JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 20: deduplicacion total de reglas repetidas sin perdida semantica.",
      "Ciclo 20: incorporadas abstracciones estables desde actividad de Filosofia del Derecho.",
      "Ciclo 20: excluidos contenidos tematicos no transversales por relacion entre nodos no equivalentes.",
      "Ciclo 20: reforzada politica de supuestos y fuentes provisionales."
    ]
  }
}