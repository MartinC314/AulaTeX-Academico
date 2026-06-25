{
  "summary": [
    "Se sincroniza memoria transversal desde actividad de Filosofia del Derecho a materia de Antropologia con estrategia conservadora.",
    "Se preservan reglas institucionales UnADM, normalizacion estructurada y compresion union-dedupe sin regresion.",
    "Se transfieren solo abstracciones estables: objetivo, evidencia verificable, analisis propio, coherencia y cierre transferible.",
    "Se evita migrar contenido tematico exclusivo de Filosofia del Derecho al nodo destino.",
    "Se refuerza control de placeholders y rutas corruptas detectadas en README y programa analitico."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener contexto local destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear el producto al entregable solicitado en la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Resolver tokens dinamicos tipo $(@{...}.Slug) a nombres literales antes de usar rutas."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante y no solo resumen.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Evitar afirmaciones juridicas o culturales sin puente argumentativo.",
    "Cerrar con conclusion transferible a la practica juridica."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar memoria.",
    "Revisar y normalizar manualmente salidas no estructuradas en ciclo 1.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que no queden placeholders sin resolver en README, programa ni .tex."
  ],
  "latex_rules": [
    "Mantener plantilla .tex local de la materia como base.",
    "Usar codificacion en espanol consistente en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, sin referencias rotas y con metadatos completos.",
    "Corregir nombres o rutas con caracteres truncados antes de compilar."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales pertinentes.",
    "Registrar fuentes especificas por actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, año, fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "No citar claves ausentes del .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y parseables.",
    "Transferir entre nodos no equivalentes solo abstracciones editoriales estables.",
    "No propagar metadatos curriculares especificos de una materia a otra.",
    "Registrar incidencias de parseo como alertas reutilizables inter-materias.",
    "Preservar reglas utiles previas y agregar solo mejoras verificables."
  ],
  "open_questions": [
    "[Supuesto] Falta consigna local de actividades concretas en Antropologia; confirmar productos por semana.",
    "Confirmar estandar de citacion oficial para la licenciatura.",
    "Confirmar si la conclusion juridica es obligatoria en todas las actividades de la materia.",
    "Confirmar si LDE-S4B2 es clave institucional definitiva o clave operativa local.",
    "Confirmar limpieza final de placeholders dinamicos en README y programa analitico."
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
        "Destino local: Antropologia de la cultura en Mexico.",
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
      "Convertir planeacion semanal en productos academicos trazables.",
      "Asegurar coherencia argumentativa y utilidad profesional.",
      "Sostener identidad UnADM en toda entrega."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Cierre con valor juridico aplicado."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente -> interpretacion propia.",
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
        "Resolucion de placeholders"
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
          "justification": "El cierre util deriva del razonamiento argumentado."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "La pauta institucional exige integridad academica."
        },
        {
          "source": "Resolucion de placeholders",
          "target": "Normalizacion estructurada",
          "kind": "supports",
          "justification": "Evita rutas corruptas y errores de compilacion."
        }
      ],
      "evidence": [
        "README destino define identidad UnADM y ubicacion curricular local.",
        "Programa analitico destino fija ejes problema, conceptos, evidencia, analisis y cierre.",
        "Bib local contiene unadmSitioWeb y unadmMallaDerecho2024.",
        "Origen aporta gates estables: JSON parseable, supuestos marcados, respaldo verificable."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin perdida semantica.",
      "Se conservaron gates criticos heredados de calidad y parseo.",
      "Se agrego control explicito de placeholders por evidencia local verificable.",
      "Se mantuvo separacion entre abstracciones transferibles y contenido tematico no equivalente."
    ]
  }
}