{
  "summary": [
    "Sincronizacion transversal consolidada entre actividad de Filosofia del Derecho y materia de Antropologia sin trasladar contenido tematico especifico.",
    "Se preservan reglas institucionales UnADM, estructura canonica y control de calidad por JSON parseable.",
    "Se refuerzan ejes estables reutilizables: objetivo, problema, conceptos, evidencia, analisis propio y conclusion transferible.",
    "Se mantiene estrategia progresiva y conservadora con compresion lossless por deduplicacion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Respetar contexto curricular local del destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar toda fuente heredada no verificada como provisional.",
    "No transferir metadatos curriculares especificos de Filosofia del Derecho al destino."
  ],
  "structure_rules": [
    "Iniciar cada producto con objetivo puntual y encuadre del problema juridico o social.",
    "Organizar desarrollo en secciones: conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear formato final con la planeacion semanal: reporte, presentacion u otro producto solicitado.",
    "Mantener separacion entre artefacto principal y bibliografia.",
    "Resolver placeholders de slug en README y programa antes de reutilizar rutas."
  ],
  "activity_rules": [
    "Sustentar afirmaciones relevantes con fuente verificable y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion.",
    "Conectar analisis cultural con implicaciones juridicas mediante puente argumentativo explicito."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar esquema minimo completo antes de aplicar cambios aguas abajo.",
    "Revisar y normalizar manualmente respuestas no estructuradas heredadas.",
    "Confirmar que toda afirmacion sin respaldo quede marcada como supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto generado y consigna real de actividad."
  ],
  "latex_rules": [
    "Mantener configuracion en espanol y codificacion correcta en .tex y .bib.",
    "Conservar clase y formato base salvo justificacion academica.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Compilar sin errores criticos, sin referencias rotas y sin tokens sin expandir.",
    "Corregir rutas corruptas detectadas en README antes de compilar."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales pertinentes.",
    "Registrar fuentes de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo abstracciones editoriales estables y validadas.",
    "Evitar transferencia literal de redaccion o conceptos exclusivos de otra materia.",
    "Mantener union-dedupe sin regresion en ciclos siguientes.",
    "Registrar incidencias de parseo como alertas reutilizables inter-nodos.",
    "Si falta contexto local, conservar cerebro minimo y abrir preguntas."
  ],
  "open_questions": [
    "Supuesto: falta consigna puntual de actividades objetivo en Antropologia; confirmar entregable exacto por semana.",
    "Confirmar estandar de citacion institucional unico para la licenciatura.",
    "Confirmar si la conclusion juridica es obligatoria en todas las actividades de la materia.",
    "Confirmar si LDE-S4B2 es clave oficial o convencion local.",
    "Confirmar que no queden placeholders dinamicos en archivos maestros."
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
        "Semestre 4, bloque 2, obligatoria, 8 creditos.",
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
      "Convertir planeacion semanal en productos academicos con rigor, claridad y utilidad profesional.",
      "Sostener coherencia institucional y calidad tecnica en toda la suite LaTeX."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Cierre con aplicacion juridica."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente -> interpretacion propia.",
      "Pregunta guia -> respuesta consistente en el cierre."
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
          "justification": "Sin parseo valido no hay memoria reutilizable confiable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura personal se legitima con respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion util deriva del razonamiento y no del resumen."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Sincronizacion transversal conservadora",
          "kind": "supports",
          "justification": "La identidad comun permite transferir reglas estables entre nodos no equivalentes."
        }
      ],
      "evidence": [
        "README local confirma identidad UnADM y pauta editorial.",
        "Programa analitico confirma ejes de problema, conceptos, evidencia, analisis y cierre.",
        "Archivo .bib local confirma base institucional verificable.",
        "Historial de alertas confirma necesidad de gate por JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 31: se transfieren solo abstracciones estables desde Filosofia del Derecho.",
      "Ciclo 31: se evita mover contenido doctrinal especifico de la materia origen.",
      "Ciclo 31: se refuerzan gates de parseo, supuestos y trazabilidad bibliografica.",
      "Ciclo 31: persistencia mantenida por union-dedupe lossless sin eliminacion de reglas utiles."
    ]
  }
}