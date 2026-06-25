{
  "summary": [
    "Sincronizacion transversal ciclo 11 aplicada con union-dedupe lossless y sin regresion.",
    "Se preservan reglas institucionales UnADM, estructura canonica y gates de calidad ya validados en destino.",
    "Se agregan solo abstracciones estables del origen: objetivo puntual, coherencia pregunta-desarrollo-conclusion, postura propia y evidencia verificable.",
    "No se transfieren contenidos tematicos exclusivos de Filosofia del Derecho al nodo de Antropologia.",
    "Se refuerza control de placeholders y rutas corruptas detectadas en README y programa analitico."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Respetar contexto local de la materia destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar toda fuente heredada no verificada como provisional hasta validacion local.",
    "No trasladar metadatos curriculares de Filosofia del Derecho a Antropologia."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear cada entrega al producto solicitado en la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Resolver tokens dinamicos tipo $(@{...}.Slug) a nombres literales antes de compilar o citar."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Evitar afirmaciones juridicas o culturales sin puente argumentativo.",
    "Cerrar con conclusion transferible a la practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa del esquema antes de reutilizar.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que README, programa analitico y rutas .tex/.bib no contengan placeholders sin resolver."
  ],
  "latex_rules": [
    "Mantener plantilla base de la materia destino como referencia primaria.",
    "Usar configuracion en espanol con acentos correctos en .tex y .bib.",
    "Mantener clase y formato institucional salvo justificacion academica.",
    "Compilar sin errores criticos, sin referencias rotas y sin tokens sin expandir.",
    "Corregir nombres de archivo truncados o con caracteres anomales antes de compilar."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes realmente consultables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales pertinentes.",
    "Registrar fuentes especificas de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y abstraidas.",
    "Transferir solo patrones editoriales estables entre nodos transversales no equivalentes.",
    "Evitar transferir redaccion literal o contenido doctrinal especifico de otra materia.",
    "Mantener estrategia conservadora: agregar mejoras verificables sin borrar reglas utiles previas.",
    "Registrar alertas de parseo y placeholders como incidencias reutilizables inter-materias."
  ],
  "open_questions": [
    "[Supuesto] Confirmar si LDE-S4B2 es clave oficial institucional o clave local.",
    "[Supuesto] Confirmar estandar unico de citacion para la licenciatura.",
    "[Supuesto] Confirmar si toda actividad de Antropologia exige conclusion juridica explicita.",
    "[Supuesto] Confirmar si existe rubrica oficial por actividad para calibrar profundidad argumentativa."
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
        "Integridad academica con trazabilidad.",
        "Normalizacion estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia destino: Antropologia de la cultura en Mexico.",
        "Contexto local: semestre 4, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema",
      "Conceptos",
      "Evidencia",
      "Analisis propio",
      "Conclusion transferible"
    ],
    "reason_for_being": [
      "Convertir la planeacion semanal en productos academicos verificables, argumentados y utiles para la practica profesional."
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
      "Pregunta guia -> desarrollo coherente -> cierre consistente."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON parseable",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "No transferencia de contenido tematico no equivalente"
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
          "justification": "La postura academica se legitima con respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion util deriva del razonamiento, no del resumen."
        },
        {
          "source": "No transferencia de contenido tematico no equivalente",
          "target": "Sincronizacion-transversal",
          "kind": "supports",
          "justification": "Preserva pertinencia disciplinar entre nodos distintos."
        }
      ],
      "evidence": [
        "README local de materia: identidad UnADM y pauta editorial.",
        "Programa analitico local: ejes problema-conceptos-producto-analisis-conclusion.",
        "Memoria origen actividad: patrones estables de objetivo, evidencia, postura y coherencia."
      ]
    },
    "reinforcement_log": [
      "Ciclo 11: deduplicacion semantica aplicada sin eliminar reglas utiles previas.",
      "Ciclo 11: reforzado gate de JSON parseable y normalizacion previa a propagacion.",
      "Ciclo 11: incorporadas abstracciones estables del origen sin arrastre doctrinal de Filosofia del Derecho.",
      "Ciclo 11: reforzada higiene de placeholders y nombres de archivo en rutas editoriales."
    ]
  }
}