{
  "summary": [
    "Sincronizacion transversal consolidada con estrategia progresiva y conservadora.",
    "Se preservan reglas institucionales UnADM y normalizacion estructurada obligatoria.",
    "Se transfieren solo abstracciones estables desde actividad de Filosofia del Derecho.",
    "Se evita mover contenido tematico exclusivo de Filosofia al nodo de Antropologia.",
    "Se refuerzan ejes reutilizables: problema, conceptos, evidencia, analisis propio y conclusion transferible.",
    "Se mantiene alerta historica: bloquear propagacion cuando no haya JSON parseable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No trasladar metadatos curriculares de Filosofia del Derecho a Antropologia."
  ],
  "structure_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar secciones en conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear el producto con la planeacion semanal y la consigna real.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias de estructura.",
    "Resolver placeholders en rutas y nombres antes de compilar."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Evitar afirmaciones juridicas sin puente argumentativo cultural.",
    "Confirmar que el entregable coincide con la consigna de la actividad.",
    "No asumir fuentes de otras semanas o materias sin validacion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar memoria.",
    "Revisar y normalizar respuestas no estructuradas antes de propagar.",
    "Confirmar consistencia entre metadatos del documento y metadata curricular local.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No promover reglas provisionales a definitivas sin evidencia local."
  ],
  "latex_rules": [
    "Mantener configuracion en espanol coherente con la plantilla.",
    "Mantener clase article, letterpaper y oneside salvo instruccion valida.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Usar nombres de archivo literales; resolver tokens tipo $(@{...}.Slug).",
    "Corregir rutas truncadas o caracteres anómalos antes de compilar.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Mantener campos institucionales completos en encabezado."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes especificas por actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Conservar claves BibTeX estables para evitar roturas de compilacion.",
    "Mantener unadmSitioWeb y unadmMallaDerecho2024 como base local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y abstractas.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferencia literal de redaccion o contenidos disciplinares no equivalentes.",
    "Mantener compresion lossless por union-dedupe sin eliminar reglas utiles.",
    "Registrar incidencias de parseo como alertas transversales reutilizables.",
    "Si falta contexto local, conservar nucleo minimo y abrir preguntas."
  ],
  "open_questions": [
    "Supuesto: falta consigna puntual de actividades de Antropologia; confirmar formatos exactos por semana.",
    "Confirmar estandar de citacion oficial de la licenciatura (APA u otro).",
    "Confirmar si LDE-S4B2 es clave institucional definitiva o clave local.",
    "Confirmar si toda actividad de Antropologia exige conclusion juridica explicita.",
    "Confirmar fuentes base obligatorias adicionales a malla y sitio UnADM."
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
      "Problema.",
      "Conceptos pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y utiles.",
      "Mantener coherencia institucional y calidad transversal entre nodos."
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
          "justification": "La conclusion surge del razonamiento, no del resumen."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Transferencia transversal conservadora",
          "kind": "supports",
          "justification": "La identidad comun habilita abstracciones reutilizables entre materias."
        }
      ],
      "evidence": [
        "README de Antropologia: identidad UnADM, ubicacion curricular y pauta editorial.",
        "Programa analitico: ejes problema, conceptos, producto, analisis y cierre.",
        "Regla heredada valida: bloquear propagacion sin JSON parseable.",
        "Regla heredada valida: marcar supuestos y fuentes provisionales."
      ]
    },
    "reinforcement_log": [
      "Ciclo 11: se consolida transferencia transversal sin mover contenido tematico de Filosofia.",
      "Ciclo 11: se refuerza gate de JSON parseable como requisito de propagacion.",
      "Ciclo 11: se mantiene union-dedupe lossless sin regresion de reglas utiles.",
      "Ciclo 11: se fortalecen patrones argumentativos comunes en Derecho UnADM."
    ]
  }
}