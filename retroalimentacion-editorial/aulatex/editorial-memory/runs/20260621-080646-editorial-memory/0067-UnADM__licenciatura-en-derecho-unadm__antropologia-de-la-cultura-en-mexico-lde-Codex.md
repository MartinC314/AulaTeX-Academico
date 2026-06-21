{
  "summary": [
    "Sincronizacion transversal aplicada por union-dedupe lossless y sin regresion.",
    "Se preserva identidad UnADM y contexto curricular local del destino.",
    "Se transfieren solo abstracciones editoriales estables desde actividad de otra materia.",
    "Se evita mover contenido tematico propio de Filosofia del Derecho al nodo destino.",
    "Se refuerza normalizacion previa a propagacion: JSON parseable y estructura completa.",
    "Se mantiene alerta institucional por salidas no estructuradas heredadas (Codex y GPT-Pro).",
    "Se confirma uso de README y programa analitico como base canonica editorial.",
    "Se consolida puente metodologico: problema, conceptos, evidencia, analisis propio y conclusion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener nombre de materia destino: Antropologia de la cultura en Mexico.",
    "Conservar ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales.",
    "No trasladar metadatos curriculares de Filosofia del Derecho a Antropologia."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco teorico/normativo, analisis propio y cierre.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias de estructura reusable.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Evitar entregas solo descriptivas.",
    "Integrar conceptos antropologicos, culturales y juridicos con puente argumentativo explicito.",
    "Marcar supuestos cuando falte contexto de consigna local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Exigir estructura minima completa del esquema antes de reutilizar.",
    "Revisar y normalizar manualmente respuestas no estructuradas heredadas.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto y consigna de actividad local.",
    "No promover reglas provisionales a definitivas sin verificacion disciplinar.",
    "Verificar ausencia de placeholders sin resolver en README, programa y .tex."
  ],
  "latex_rules": [
    "Usar codificacion en espanol y acentos correctos en .tex y .bib.",
    "Mantener clase y formato base salvo justificacion academica.",
    "Actualizar documenttitle y documentsubtitle por actividad real.",
    "Mantener coursename y coursecode locales salvo instruccion institucional distinta.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir rutas truncadas o tokens dinamicos antes de compilar."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes especificas de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener trazabilidad de activos locales como malla curricular en assets-unadm."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y abstractas.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar propagar redaccion literal o temas exclusivos de una materia a otra.",
    "Preservar reglas utiles previas; solo agregar mejoras verificables.",
    "Registrar incidencias de parseo como alerta institucional transversal.",
    "Si falta contexto local, mantener cerebro minimo y abrir preguntas."
  ],
  "open_questions": [
    "Confirmar rubrica oficial de evaluacion para actividades de la materia destino.",
    "Confirmar estandar de citacion institucional unico para la licenciatura.",
    "Confirmar si coursecode LDE-S4B2 es oficial o convencion local. [supuesto]",
    "Confirmar si toda actividad de Antropologia exige conclusion juridica explicita.",
    "Confirmar resolucion definitiva de placeholders en README/programa para evitar ambiguedad."
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
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 4, bloque 2, obligatoria, 8 creditos.",
        "Asignatura destino: Antropologia de la cultura en Mexico."
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
      "Convertir planeacion semanal en productos academicos con rigor y utilidad profesional.",
      "Sostener coherencia institucional y metodologica entre materias no equivalentes."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados cuando falte evidencia local.",
      "Cierre con valor juridico-profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente verificable -> interpretacion propia.",
      "Consigna local -> desarrollo alineado -> cierre coherente."
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
          "justification": "Sin parseo valido no hay memoria confiable."
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
          "justification": "La conclusion surge del razonamiento y no del resumen."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Sincronizacion transversal conservadora",
          "kind": "supports",
          "justification": "La identidad comun permite transferir reglas estables entre nodos."
        }
      ],
      "evidence": [
        "README de materia destino.",
        "Programa analitico de materia destino.",
        "Archivo .bib local con entradas institucionales verificables.",
        "Historial de alertas por salidas no JSON parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 67: deduplicacion total aplicada sin eliminar reglas utiles previas.",
      "Ciclo 67: se agregan solo abstracciones estables del origen transversal.",
      "Ciclo 67: se bloquea transferencia de contenido tematico especifico de Filosofia del Derecho.",
      "Ciclo 67: se refuerzan gates de parseo, supuestos y trazabilidad bibliografica."
    ]
  }
}