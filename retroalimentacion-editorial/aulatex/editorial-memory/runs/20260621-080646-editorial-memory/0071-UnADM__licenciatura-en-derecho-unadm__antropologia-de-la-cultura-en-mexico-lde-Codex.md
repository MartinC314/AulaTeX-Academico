{
  "summary": [
    "Sincronizacion transversal consolidada desde actividad de Filosofia del Derecho hacia materia de Antropologia con estrategia conservadora.",
    "Se preservan reglas institucionales UnADM, estructura canonica y control de calidad por JSON parseable.",
    "Se transfieren solo abstracciones estables: objetivo, problema, evidencia, analisis propio y conclusion transferible.",
    "Se evita transferir contenido tematico exclusivo de Filosofia del Derecho al destino.",
    "Se refuerza resolucion de placeholders y rutas corruptas en README, programa analitico y nombres de archivos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Usar nombre canonico de materia: Antropologia de la cultura en Mexico.",
    "Respetar ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar toda fuente heredada no verificada como provisional.",
    "No trasladar metadatos curriculares de otras materias."
  ],
  "structure_rules": [
    "Iniciar cada actividad con objetivo puntual y encuadre breve del problema.",
    "Organizar en secciones: conceptos clave, marco normativo o teorico, analisis propio y cierre.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias editoriales primarias.",
    "Normalizar nombres de archivos antes de compilar o propagar."
  ],
  "activity_rules": [
    "Sustentar afirmaciones relevantes con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Evitar extrapolar bibliografia de semanas o materias distintas sin validacion.",
    "Cerrar con conclusion transferible a la practica juridica."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Exigir estructura minima completa del esquema antes de reutilizar memoria.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregado y consigna local.",
    "No promover reglas provisionales a definitivas sin validacion disciplinar."
  ],
  "latex_rules": [
    "Conservar plantilla base .tex de la materia.",
    "Usar configuracion en espanol y acentos correctos en .tex y .bib.",
    "Mantener clase y formato base salvo justificacion academica.",
    "Actualizar documenttitle y documentsubtitle por actividad real.",
    "Resolver tokens tipo $(@{...}.Slug) a nombres literales antes de compilar.",
    "Corregir rutas con caracteres truncados o anomalos.",
    "Compilar sin errores criticos, referencias rotas ni placeholders sin resolver."
  ],
  "bibliography_rules": [
    "Usar archivo local antropologia-de-la-cultura-en-mexico.bib como canonico del destino.",
    "No inventar fuentes; usar solo referencias verificables y consultables.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Marcar como supuesto cualquier referencia heredada no confirmada localmente."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y abstractas entre nodos no equivalentes.",
    "Mantener compresion lossless por union-dedupe sin eliminar reglas utiles previas.",
    "Registrar incidencias de parseo como alertas transversales reutilizables.",
    "Evitar transferir redaccion literal y contenido tematico no transversal.",
    "Si falta contexto local de actividad, conservar cerebro minimo y abrir preguntas."
  ],
  "open_questions": [
    "Supuesto: falta consigna especifica de actividades de Antropologia; confirmar formato exacto por semana.",
    "Confirmar estandar de citacion institucional unico para la licenciatura.",
    "Confirmar si LDE-S4B2 es clave oficial o local.",
    "Confirmar si toda actividad de la materia exige conclusion juridica explicita.",
    "Confirmar politica final para autoria y matricula en plantillas compartidas."
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
        "Asignatura: Antropologia de la cultura en Mexico."
      ]
    },
    "essence": [
      "Problema, conceptos, evidencia, analisis propio y conclusion transferible.",
      "Normalizacion estructurada antes de propagar.",
      "Sincronizacion transversal sin contaminar contexto disciplinar."
    ],
    "reason_for_being": [
      "Guiar productos academicos consistentes con UnADM y la planeacion semanal.",
      "Asegurar calidad verificable en contenido, estructura y trazabilidad."
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
      "Consigna local -> desarrollo alineado -> verificacion final."
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
          "source": "Integridad academica",
          "target": "Evidencia verificable",
          "kind": "depends_on",
          "justification": "La integridad exige respaldo trazable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "El analisis gana solidez con fuentes comprobables."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion util surge del razonamiento argumentado."
        },
        {
          "source": "Resolucion de placeholders",
          "target": "Normalizacion estructurada",
          "kind": "supports",
          "justification": "Evita errores de rutas y nombres en flujos editoriales."
        }
      ],
      "evidence": [
        "README local confirma identidad UnADM y pauta editorial.",
        "Programa analitico confirma ejes de trabajo reutilizables.",
        ".bib local confirma fuentes base institucionales.",
        "Historial heredado confirma gate obligatorio de JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 71: deduplicacion de reglas repetidas y conservacion de reglas utiles previas.",
      "Ciclo 71: incorporadas abstracciones estables desde Filosofia del Derecho sin traslado tematico.",
      "Ciclo 71: reforzado control de placeholders y rutas corruptas como gate tecnico-editorial.",
      "Ciclo 71: mantenido estado provisional de fuentes heredadas no verificadas."
    ]
  }
}