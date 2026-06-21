{
  "summary": [
    "Sincronizacion transversal consolidada con union-dedupe lossless y sin regresion.",
    "Se preservan reglas institucionales UnADM, estructura canonica y gates de calidad.",
    "Se transfieren solo abstracciones estables desde actividad de Filosofia del Derecho.",
    "Se evita transferir contenido tematico exclusivo de Filosofia al nodo de Antropologia.",
    "Se refuerza normalizacion previa cuando existan salidas no JSON parseables.",
    "Se mantiene marcada como provisional toda fuente heredada no verificada.",
    "Se corrigen placeholders dinamicos en README y programa como tarea editorial activa."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Conservar ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar toda fuente heredada no verificada como provisional.",
    "No trasladar metadatos curriculares de Filosofia del Derecho a Antropologia."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos, marco de referencia, analisis propio y cierre.",
    "Alinear el producto con la planeacion semanal y la consigna real.",
    "Mantener artefactos separados: reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guia estructural primaria."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar solo descripcion.",
    "Sustentar afirmaciones relevantes con fuente verificable y cita explicita.",
    "Distinguir evidencia, interpretacion y opinion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion transferible a la practica juridica.",
    "En Antropologia, tender puente explicito entre enfoque cultural y juridico."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar memoria.",
    "Normalizar manualmente respuestas no estructuradas antes de propagar.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Verificar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregado y consigna de actividad."
  ],
  "latex_rules": [
    "Usar configuracion en espanol consistente con la plantilla.",
    "Mantener clase y formato base salvo justificacion academica.",
    "Actualizar documenttitle y documentsubtitle por actividad real.",
    "Conservar claves BibTeX estables para evitar referencias rotas.",
    "Compilar sin errores criticos ni referencias faltantes.",
    "Resolver tokens tipo $(@{...}.Slug) en nombres de archivo antes de compilar.",
    "Corregir rutas truncadas o caracteres anómalos en README y .tex."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y normativas aplicables.",
    "Registrar fuentes especificas de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener entradas base unadmSitioWeb y unadmMallaDerecho2024."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y parseables.",
    "Compartir en nodos transversales solo abstracciones editoriales estables.",
    "No propagar redaccion literal ni contenidos disciplinares no equivalentes.",
    "Mantener estrategia progresiva y conservadora: agregar, no reemplazar.",
    "Registrar alertas de parseo como memoria institucional reutilizable.",
    "Preservar reglas utiles previas durante cada ciclo de consolidacion."
  ],
  "open_questions": [
    "Supuesto: falta consigna puntual de actividades de Antropologia; confirmar formato por semana.",
    "Confirmar estandar unico de citacion institucional para la licenciatura.",
    "Confirmar si LDE-S4B2 es clave oficial o local.",
    "Confirmar si toda actividad de Antropologia exige conclusion juridica explicita.",
    "Confirmar sustitucion definitiva de placeholders .Slug en README y programa."
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
      "Problema claro.",
      "Conceptos pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y utiles.",
      "Sostener coherencia entre identidad institucional y calidad argumentativa."
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
      "Pregunta guia -> desarrollo consistente -> respuesta final."
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
        "Puente cultural-juridico"
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
          "justification": "La integridad exige respaldo trazable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura propia se fortalece con fuentes comprobables."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion aplicable surge del razonamiento argumentado."
        },
        {
          "source": "Puente cultural-juridico",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "Conecta el enfoque antropologico con utilidad juridica."
        }
      ],
      "evidence": [
        "README de materia destino: identidad UnADM y pauta editorial.",
        "Programa analitico destino: ejes problema, conceptos, producto, analisis y cierre.",
        "Bib local: unadmSitioWeb y unadmMallaDerecho2024.",
        "Historial institucional: alerta por salidas no JSON parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 70: se consolidan abstracciones estables del origen sin arrastre tematico.",
      "Ciclo 70: se refuerzan gates de parseo JSON y normalizacion estructurada.",
      "Ciclo 70: se mantienen reglas previas utiles y se deduplican en forma lossless.",
      "Ciclo 70: se preserva identidad local de Antropologia y se marca lo no verificado como supuesto."
    ]
  }
}