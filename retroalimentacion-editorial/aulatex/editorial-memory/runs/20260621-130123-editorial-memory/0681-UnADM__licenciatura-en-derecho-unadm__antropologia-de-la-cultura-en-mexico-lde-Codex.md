{
  "summary": [
    "Sincronizacion transversal consolidada desde actividad de Filosofia del Derecho hacia materia de Antropologia sin traslape tematico.",
    "Se preservan reglas institucionales UnADM, normalizacion estructurada y validacion JSON parseable.",
    "Se refuerzan ejes reutilizables: objetivo, problema, conceptos, evidencia, analisis propio y conclusion transferible.",
    "Se mantiene estrategia progresiva y conservadora con compresion lossless por union-dedupe."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Respetar contexto curricular local del destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "No trasladar metadatos curriculares especificos de Filosofia del Derecho al destino.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Usar README de la materia como entrada canonica.",
    "Usar programa analitico como guia de estructura reusable.",
    "Organizar entregables con secuencia: objetivo, problema, conceptos, evidencia, analisis y cierre.",
    "Alinear cada producto con la planeacion semanal real.",
    "Separar artefactos: reporte, presentacion y bibliografia.",
    "Resolver placeholders y tokens dinamicos antes de reutilizar rutas o nombres."
  ],
  "activity_rules": [
    "Definir objetivo puntual al inicio de cada actividad.",
    "Iniciar con problema juridico o social contextualizado.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir evidencia, interpretacion y opinion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Exigir estructura minima completa del esquema antes de propagar.",
    "Revisar y normalizar manualmente respuestas no estructuradas heredadas.",
    "Confirmar que todo supuesto este marcado como supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No promover reglas provisionales a definitivas sin verificacion local."
  ],
  "latex_rules": [
    "Mantener plantilla base .tex de la materia destino como referencia.",
    "Conservar configuracion en espanol, letterpaper y oneside salvo instruccion distinta.",
    "Actualizar documenttitle y documentsubtitle por actividad real.",
    "Verificar acentos y codificacion consistente en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, sin referencias rotas y sin tokens sin expandir."
  ],
  "bibliography_rules": [
    "Usar solo fuentes consultables y verificables; no inventar referencias.",
    "Priorizar fuentes institucionales UnADM y normativas aplicables.",
    "Registrar bibliografia especifica de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Mantener unadmSitioWeb y unadmMallaDerecho2024 como base local vigente."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferencia de redaccion literal o contenido tematico exclusivo del origen.",
    "Aplicar union-dedupe sin eliminar reglas utiles previas.",
    "Registrar alertas de parseo como memoria institucional reutilizable.",
    "Si falta contexto local, conservar cerebro minimo y abrir vacios como preguntas."
  ],
  "open_questions": [
    "Supuesto: la clave LDE-S4B2 es local; confirmar si es oficial institucional.",
    "Confirmar estandar unico de citacion para la licenciatura.",
    "Confirmar si todas las actividades de Antropologia exigen conclusion juridica explicita.",
    "Confirmar si el nombre literal del .bib queda fijo sin plantilla dinamica.",
    "Supuesto: reglas heredadas desde fuentes no verificadas siguen en estado provisional."
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
        "Destino local: Antropologia de la cultura en Mexico.",
        "Semestre 4, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema contextualizado.",
      "Conceptos pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y utiles para practica profesional.",
      "Asegurar coherencia entre identidad institucional, metodo argumentativo y verificabilidad."
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
        "No traslape de metadatos entre materias"
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
          "justification": "La postura propia gana solidez con respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion util deriva del razonamiento y no del resumen."
        },
        {
          "source": "No traslape de metadatos entre materias",
          "target": "Identidad institucional UnADM",
          "kind": "supports",
          "justification": "Preserva consistencia institucional en sincronizacion transversal."
        }
      ],
      "evidence": [
        "README local fija identidad UnADM y pauta editorial.",
        "Programa analitico local fija ejes de trabajo reutilizables.",
        "Bib local confirma fuentes institucionales base.",
        "Memoria origen exige JSON parseable y normalizacion previa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 17: se incorporan abstracciones estables del origen sin mover contenido tematico de Filosofia.",
      "Ciclo 17: se refuerza gate de parseo JSON como condicion de propagacion recursiva.",
      "Ciclo 17: se mantiene compresion lossless por deduplicacion y sin regresion.",
      "Ciclo 17: se conserva estado provisional para fuentes heredadas no verificadas."
    ]
  }
}