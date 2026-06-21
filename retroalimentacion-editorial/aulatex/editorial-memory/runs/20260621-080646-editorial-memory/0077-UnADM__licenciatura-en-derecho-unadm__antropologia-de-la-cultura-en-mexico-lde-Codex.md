{
  "summary": [
    "Sincronizacion transversal consolidada desde actividad de Filosofia del Derecho hacia materia de Antropologia con union-dedupe lossless.",
    "Se preservan reglas institucionales UnADM, normalizacion estructurada y bloqueo por JSON no parseable.",
    "Se transfieren solo abstracciones estables: objetivo puntual, evidencia verificable, analisis propio, coherencia argumentativa y cierre transferible.",
    "Se evita migrar contenido tematico especifico de Filosofia del Derecho al destino no equivalente.",
    "Se refuerza resolucion de placeholders y tokens dinamicos en README, programa analitico y rutas .bib/.tex."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener ubicacion curricular local del destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar toda fuente heredada no verificada como provisional hasta confirmacion local.",
    "No trasladar metadatos curriculares de otras asignaturas al destino."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco normativo o teorico, analisis propio y cierre.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias canonicas de estructura.",
    "Resolver nombres de archivo con placeholders antes de redactar o compilar."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion transferible a la practica juridica.",
    "Evitar extrapolar fuentes de semanas o materias sin validar pertinencia.",
    "Adaptar conceptos al enfoque antropologico-juridico del destino."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Exigir estructura minima completa del esquema antes de reutilizar memoria.",
    "Revisar y normalizar manualmente respuestas no estructuradas heredadas.",
    "Confirmar que toda afirmacion tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Verificar coherencia entre metadatos de materia y documento final.",
    "No promover reglas provisionales a definitivas sin validacion disciplinar."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener clase y formato base de la materia salvo justificacion academica.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Compilar sin errores criticos ni referencias faltantes.",
    "Corregir rutas con caracteres truncados detectadas en README.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README, programa y archivos."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables y consultables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales pertinentes.",
    "Registrar fuentes especificas de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No citar entradas inexistentes en el .bib local.",
    "Mantener como base verificable: unadmSitioWeb y unadmMallaDerecho2024."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y no literales.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferir contenido tematico exclusivo de nodos no equivalentes.",
    "Mantener compresion lossless por union-dedupe sin eliminar reglas utiles previas.",
    "Registrar incidencias de parseo como alertas transversales reutilizables.",
    "Etiquetar supuestos de forma explicita al cruzar materias."
  ],
  "open_questions": [
    "Supuesto: falta consigna local de actividad especifica en destino; confirmar producto exacto por semana.",
    "Confirmar estandar unico de citacion institucional para la licenciatura.",
    "Confirmar si LDE-S4B2 es clave oficial definitiva o etiqueta local.",
    "Confirmar si toda actividad del destino exige conclusion juridica explicita.",
    "Confirmar que no queden placeholders activos en archivos no inspeccionados."
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
        "Destino: Antropologia de la cultura en Mexico.",
        "Semestre 4, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros, verificables y utiles profesionalmente.",
      "Asegurar coherencia entre consigna, argumento, evidencia y cierre."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados.",
      "Cierre con valor profesional."
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
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion util deriva del razonamiento y no del resumen."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "La pauta institucional exige integridad academica."
        }
      ],
      "evidence": [
        "README destino: identidad UnADM y pauta editorial.",
        "Programa analitico destino: ejes problema, conceptos, producto, analisis y cierre.",
        "Bib local destino: unadmSitioWeb y unadmMallaDerecho2024.",
        "Memoria origen: regla de bloqueo por JSON no parseable y normalizacion previa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 77: se reforzo transferencia de abstracciones estables sin arrastre tematico.",
      "Ciclo 77: se consolidaron gates de calidad y parseo como politicas transversales.",
      "Ciclo 77: se mantuvo estrategia progresiva y conservadora sin regresion."
    ]
  }
}