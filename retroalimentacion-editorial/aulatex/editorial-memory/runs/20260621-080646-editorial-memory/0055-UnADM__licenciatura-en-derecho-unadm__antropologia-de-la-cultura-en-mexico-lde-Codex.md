{
  "summary": [
    "Sincronizacion transversal consolidada entre actividad y materia con estrategia conservadora.",
    "Se preservan reglas utiles vigentes y se deduplican sin perdida.",
    "Se transfieren solo abstracciones estables no tematicas de Filosofia del Derecho.",
    "Se refuerza identidad UnADM, estructura reusable y gates de calidad.",
    "Se mantiene alerta por salidas no JSON parseables como riesgo operativo reutilizable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener ubicacion curricular local de destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar toda fuente heredada no verificada como provisional.",
    "No trasladar metadatos curriculares especificos de otra asignatura."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar por secciones: conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear el producto al entregable solicitado en la planeacion semanal.",
    "Distinguir artefactos: reporte, presentacion y bibliografia.",
    "Usar README y programa analitico locales como fuentes de estructura.",
    "Resolver placeholders y tokens dinamicos en rutas y nombres antes de usar."
  ],
  "activity_rules": [
    "Sustentar afirmaciones relevantes con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Evitar extrapolar contenidos de semanas o materias no confirmadas para la actividad.",
    "Cerrar con conclusion transferible a la practica juridica cuando la consigna lo permita."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa del esquema antes de reutilizar.",
    "Revisar y normalizar respuestas no estructuradas antes de propagar.",
    "Confirmar que cada afirmacion tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto final y consigna local.",
    "No promover reglas provisionales a definitivas sin validacion local."
  ],
  "latex_rules": [
    "Mantener plantilla .tex local como base.",
    "Conservar codificacion y convenciones en español en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Mantener claves BibTeX estables.",
    "Corregir rutas con caracteres truncados o placeholders sin resolver.",
    "Actualizar documenttitle y documentsubtitle segun actividad real."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales pertinentes.",
    "Registrar fuentes especificas por actividad en el .bib local de la materia.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "No citar claves inexistentes en el .bib."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y abstractas entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferir redaccion literal o contenido tematico exclusivo de otra materia.",
    "Mantener compresion por union-dedupe lossless sin regresion.",
    "Registrar incidencias de parseo como alertas transversales reutilizables.",
    "Si falta contexto local, conservar cerebro editorial minimo y abrir preguntas."
  ],
  "open_questions": [
    "Supuesto: falta consigna puntual de actividades especificas en destino; confirmar formato esperado.",
    "Confirmar estandar de citacion institucional unificado para la licenciatura.",
    "Confirmar si la conclusion juridica es obligatoria en todas las actividades de la materia.",
    "Confirmar si la clave de curso LDE-S4B2 es oficial o local.",
    "Confirmar si existen fuentes obligatorias adicionales a README, programa y malla."
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
        "Materia destino: Antropologia de la cultura en Mexico.",
        "Semestre 4, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema, conceptos, evidencia, analisis propio y cierre.",
      "Normalizacion estructurada antes de cualquier propagacion.",
      "Compresion por deduplicacion sin perdida.",
      "Transferencia transversal por abstracciones estables."
    ],
    "reason_for_being": [
      "Guiar productos academicos consistentes, verificables y reutilizables en LaTeX.",
      "Preservar continuidad editorial entre nodos sin contaminar contexto disciplinar.",
      "Asegurar calidad tecnica y argumentativa antes de escalar memoria."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados cuando falte evidencia directa.",
      "Cierre con utilidad academica o profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente verificable -> interpretacion propia.",
      "Consigna local -> desarrollo alineado -> verificacion final."
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
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion solida surge del razonamiento sustentado."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Transferencia transversal conservadora",
          "kind": "supports",
          "justification": "La identidad comun habilita reglas compartidas entre materias."
        }
      ],
      "evidence": [
        "README de destino confirma identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico confirma ejes problema, conceptos, fuentes, analisis y cierre.",
        "Bib local incluye unadmSitioWeb y unadmMallaDerecho2024.",
        "Memoria origen aporta gates de parseo, normalizacion y estructura argumentativa reutilizable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 55: dedupe de reglas repetidas en summary, identidad, estructura y calidad.",
      "Ciclo 55: se excluyen contenidos tematicos especificos de Filosofia del Derecho por no equivalencia de nodo.",
      "Ciclo 55: se conserva alerta historica de salida no parseable como gate transversal.",
      "Ciclo 55: se refuerza politica de supuestos y fuentes provisionales no verificadas."
    ]
  }
}