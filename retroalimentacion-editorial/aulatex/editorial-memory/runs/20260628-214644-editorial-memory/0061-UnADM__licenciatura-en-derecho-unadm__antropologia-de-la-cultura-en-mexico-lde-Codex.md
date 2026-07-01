{
  "summary": [
    "Sincronizacion transversal ciclo 2 aplicada con estrategia progresiva y conservadora.",
    "Se preservan reglas utiles previas del destino y del origen sin regresion.",
    "Se incorporan solo abstracciones estables: objetivo, evidencia, analisis propio, coherencia y cierre transferible.",
    "Se evita transferir contenido tematico exclusivo de Filosofia del Derecho.",
    "Se refuerza normalizacion estructurada y validacion JSON antes de propagacion recursiva."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener contexto curricular local del destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como [Supuesto] todo dato no visible en la consigna local.",
    "Tratar toda fuente heredada no verificada como provisional hasta confirmacion local.",
    "No trasladar metadatos curriculares de la materia origen al destino."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones reutilizables: conceptos clave, marco teorico/normativo, analisis propio y cierre.",
    "Alinear el producto al entregable solicitado en la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Resolver placeholders dinamicos en README/programa/.tex/.bib antes de uso.",
    "Corregir rutas truncadas o caracteres anomales antes de compilar."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Cerrar con conclusion transferible a la practica juridica.",
    "No asumir fuentes de otras semanas o materias sin validacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Exigir esquema minimo completo antes de reutilizar memoria.",
    "Revisar y normalizar manualmente respuestas no estructuradas heredadas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de [Supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que no queden tokens sin resolver tipo $(@{...}.Slug).",
    "No promover reglas provisionales a definitivas sin verificacion disciplinar."
  ],
  "latex_rules": [
    "Usar codificacion en espanol y acentos consistentes en .tex y .bib.",
    "Mantener clase y formato base de la plantilla salvo justificacion academica.",
    "Actualizar documenttitle/documentsubtitle por actividad.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Compilar sin errores criticos ni referencias indefinidas.",
    "Verificar nombres reales de archivos antes de referenciarlos."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias consultables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes especificas de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No citar claves ausentes en el .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar propagar redaccion literal o contenido tematico de materia origen.",
    "Mantener compresion lossless por union-dedupe sin eliminar reglas utiles.",
    "Registrar incidencias de parseo como alertas transversales reutilizables.",
    "Mantener etiquetas [Supuesto] en vacios de contexto local."
  ],
  "open_questions": [
    "[Supuesto] Confirmar rubrica oficial de evaluacion de la materia destino.",
    "[Supuesto] Confirmar estandar de citacion institucional unico (APA u otro).",
    "[Supuesto] Confirmar si la conclusion juridica es obligatoria en todas las actividades de antropologia.",
    "[Supuesto] Confirmar vigencia oficial de la clave local LDE-S4B2.",
    "[Supuesto] Confirmar si existe guia local adicional para productos visuales."
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
        "Destino local: semestre 4, bloque 2, obligatoria, 8 creditos.",
        "Asignatura destino: Antropologia de la cultura en Mexico."
      ]
    },
    "essence": [
      "Problema relevante.",
      "Conceptos pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables y utiles.",
      "Asegurar consistencia editorial transversal sin perder contexto local."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados cuando falten datos.",
      "Cierre con valor profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente verificable -> interpretacion propia.",
      "Pregunta guia -> desarrollo coherente -> respuesta final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalizacion estructurada",
        "JSON parseable",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Propagacion transversal conservadora"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "JSON parseable",
          "target": "Normalizacion estructurada",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay reutilizacion segura."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "El argumento personal gana validez con respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion util deriva del razonamiento, no del resumen."
        },
        {
          "source": "Identidad UnADM",
          "target": "Propagacion transversal conservadora",
          "kind": "supports",
          "justification": "La coherencia institucional guia que si se transfiere entre materias."
        }
      ],
      "evidence": [
        "README y programa analitico del destino exigen identidad, evidencia y cierre.",
        "Memoria origen aporta patrones estables de estructura y control de calidad.",
        "Regla transversal vigente: no propagar salidas no estructuradas."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: deduplicacion de reglas repetidas en origen y destino.",
      "Ciclo 2: fortalecida regla de [Supuesto] para datos no visibles.",
      "Ciclo 2: reforzada validacion JSON + esquema antes de propagacion recursiva.",
      "Ciclo 2: consolidada separacion entre abstracciones estables y contenido tematico local."
    ]
  }
}