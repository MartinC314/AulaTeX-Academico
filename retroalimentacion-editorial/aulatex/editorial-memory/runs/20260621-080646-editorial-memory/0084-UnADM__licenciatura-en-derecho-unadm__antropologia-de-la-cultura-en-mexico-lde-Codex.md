{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia progresiva y conservadora.",
    "Se preservan reglas utiles previas sin regresion.",
    "Se transfieren solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Se mantiene identidad UnADM con contexto curricular local del destino.",
    "Se refuerza normalizacion estructurada y validacion JSON parseable antes de propagar.",
    "Se consolida compresion lossless por union-dedupe.",
    "Se evita mover contenido tematico especifico de Filosofia del Derecho hacia Antropologia.",
    "Se mantiene alerta por salidas heredadas no estructuradas como evidencia de riesgo."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Usar contexto local del destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar toda fuente heredada no verificada como provisional.",
    "No trasladar metadatos curriculares de otras materias al destino."
  ],
  "structure_rules": [
    "Abrir cada entrega con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar secciones en: conceptos clave, marco de referencia, analisis propio y cierre.",
    "Alinear el producto al entregable solicitado en la planeacion semanal.",
    "Separar artefactos: reporte, presentacion y bibliografia.",
    "Usar README y programa analitico locales como guia estructural.",
    "Resolver placeholders en rutas y nombres antes de compilar."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion.",
    "Evitar afirmaciones generales sin puente argumentativo disciplinar.",
    "Cerrar con conclusion transferible a la practica juridica cuando la consigna lo permita."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar memoria.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que no queden tokens dinamicos sin resolver en README, programa y .tex.",
    "No promover reglas provisionales a definitivas sin validacion local."
  ],
  "latex_rules": [
    "Mantener plantilla base .tex de la materia destino.",
    "Conservar configuracion en espanol y acentos correctos en .tex y .bib.",
    "Mantener clase y formato salvo justificacion academica.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Compilar sin errores criticos, sin referencias rotas y sin rutas corruptas.",
    "Mantener claves BibTeX estables.",
    "Resolver tokens tipo $(@{...}.Slug) a nombres literales antes de uso."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Usar solo referencias verificables y consultables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales pertinentes.",
    "Registrar fuentes de cada actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener como base local: unadmSitioWeb y unadmMallaDerecho2024."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y estables.",
    "Priorizar identidad, estructura reusable, gates y grafo conceptual.",
    "Evitar transferencia literal de redaccion o contenidos tematicos de origen.",
    "Registrar incidencias de parseo como alerta transversal reutilizable.",
    "Aplicar union-dedupe lossless en cada ciclo sin borrar reglas utiles.",
    "Si falta contexto local en nodos vecinos, crear memoria minima y abrir vacios."
  ],
  "open_questions": [
    "Supuesto: la conclusion juridica aplica a todas las actividades de Antropologia; confirmar por consigna.",
    "Confirmar rubrica oficial de evaluacion para calibrar profundidad argumentativa.",
    "Confirmar estandar institucional unico de citas en la licenciatura.",
    "Confirmar si LDE-S4B2 es clave oficial o convencion local.",
    "Confirmar politica final para placeholders en archivos fuente."
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
        "Materia destino: Antropologia de la cultura en Mexico.",
        "Semestre 4, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema, conceptos, evidencia, analisis propio y cierre.",
      "Normalizacion estructurada antes de propagacion.",
      "Compresion lossless por deduplicacion.",
      "Sincronizacion transversal sin contaminacion tematica."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos consistentes y verificables.",
      "Preservar identidad institucional y calidad editorial entre nodos.",
      "Asegurar transferencias estables entre materias no equivalentes."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y trazables.",
      "Supuestos marcados de forma visible.",
      "Cierre aplicable al contexto profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> respaldo verificable -> interpretacion propia.",
      "Consigna -> desarrollo alineado -> cierre coherente."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON parseable",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion transferible",
        "Compresion union-dedupe lossless",
        "Supuestos explicitados"
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
          "justification": "Sin parseo valido no hay reutilizacion confiable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "El argumento gana validez con respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion util surge del razonamiento y no del resumen."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "La pauta institucional exige integridad academica."
        }
      ],
      "evidence": [
        "README y programa analitico del destino fijan identidad y ejes.",
        "El .bib local contiene fuentes institucionales base verificables.",
        "Historial heredado reporta salidas no JSON parseables y exige normalizacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 84: se consolidan abstracciones estables del origen sin traslado tematico literal.",
      "Ciclo 84: se refuerzan gates de parseo JSON, estructura minima y trazabilidad.",
      "Ciclo 84: se mantiene regla de fuentes heredadas como provisionales hasta validacion local.",
      "Ciclo 84: se preserva union-dedupe lossless sin eliminar reglas utiles previas."
    ]
  }
}