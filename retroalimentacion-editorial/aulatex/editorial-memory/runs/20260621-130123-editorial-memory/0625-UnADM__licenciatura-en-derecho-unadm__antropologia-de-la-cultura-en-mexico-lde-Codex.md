{
  "summary": [
    "Se consolida sincronizacion transversal ciclo 3 con estrategia progresiva y conservadora.",
    "Se preservan reglas utiles previas sin regresion y con deduplicacion lossless.",
    "Se transfieren solo abstracciones editoriales estables desde actividad de Filosofia del Derecho.",
    "Se evita mover contenido tematico especifico de Filosofia al nodo de Antropologia.",
    "Se refuerzan identidad UnADM, estructura reusable, calidad de parseo y trazabilidad de fuentes.",
    "Se mantiene alerta por salidas no JSON parseable heredadas y se exige normalizacion previa."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Respetar contexto curricular local del destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar toda fuente heredada no verificada como provisional.",
    "No trasladar metadatos curriculares de Filosofia del Derecho a Antropologia."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco normativo o teorico, analisis propio y cierre.",
    "Alinear el producto al entregable real de la planeacion semanal.",
    "Separar artefactos: reporte, presentacion y bibliografia.",
    "Cerrar con conclusion transferible a practica juridica.",
    "Resolver placeholders de nombre de archivo antes de compilar o citar rutas."
  ],
  "activity_rules": [
    "Sustentar cada afirmacion relevante con fuente verificable.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Evitar puentes argumentativos debiles entre analisis cultural y pertinencia juridica.",
    "No asumir fuentes de otras semanas o materias sin confirmacion local.",
    "Marcar supuestos cuando falte consigna especifica."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Exigir estructura minima completa del esquema antes de reutilizar.",
    "Normalizar manualmente respuestas no estructuradas antes de aplicar aguas abajo.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregado y consigna local.",
    "Comprobar que no queden tokens sin resolver en README, programa, .tex y rutas.",
    "No promover reglas provisionales a definitivas sin validacion disciplinar."
  ],
  "latex_rules": [
    "Usar configuracion de espanol y acentos consistentes en .tex y .bib.",
    "Mantener clase y formato base salvo justificacion academica.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Mantener claves BibTeX estables para evitar rupturas.",
    "Corregir rutas con caracteres truncados antes de compilar.",
    "Resolver tokens dinamicos tipo $(@{...}.Slug) a nombre literal.",
    "Actualizar documenttitle y documentsubtitle por actividad real."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo fuentes consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes especificas de actividad en el .bib local de la materia.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener trazabilidad de procedencia cuando se use archivo local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y estructuradas.",
    "Compartir entre nodos no equivalentes solo abstracciones editoriales estables.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar propagar redaccion literal o contenido tematico exclusivo del origen.",
    "Mantener compresion por union-dedupe sin borrar reglas utiles previas.",
    "Registrar incidencias de parseo como alertas reutilizables entre materias."
  ],
  "open_questions": [
    "Supuesto: falta confirmar estandar unico de citacion para la licenciatura.",
    "Supuesto: falta confirmar si LDE-S4B2 es clave institucional definitiva o local.",
    "Confirmar si toda actividad de Antropologia exige cierre juridico explicito.",
    "Confirmar rubrica local para ajustar profundidad argumentativa por actividad.",
    "Confirmar si existe regla institucional para nombre canonico del .bib frente a tokens dinamicos."
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
        "Antropologia de la cultura en Mexico.",
        "Semestre 4, bloque 2, obligatoria, 8 creditos.",
        "No traslape de metadatos entre materias."
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
      "Sostener criterio propio con evidencia y forma institucional consistente."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales.",
      "Supuestos marcados.",
      "Citas verificables.",
      "Cierre profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente -> interpretacion propia.",
      "Coherencia entre pregunta guia y respuesta final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad academica",
        "Validacion JSON parseable",
        "Normalizacion estructurada",
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
          "source": "Integridad academica",
          "target": "Evidencia verificable",
          "kind": "depends_on",
          "justification": "La integridad exige respaldo trazable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura personal gana solidez con fuentes."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La utilidad profesional surge del razonamiento."
        },
        {
          "source": "Transferencia transversal conservadora",
          "target": "Identidad UnADM",
          "kind": "supports",
          "justification": "Se comparten reglas estables sin contaminar contexto local."
        }
      ],
      "evidence": [
        "README local de Antropologia define identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico local define ejes de trabajo reutilizables.",
        "Bib local contiene entradas institucionales verificables.",
        "Memoria origen aporta gates de parseo JSON y normalizacion estructurada."
      ]
    },
    "reinforcement_log": [
      "Ciclo 3: se refuerza gate de JSON parseable como condicion de propagacion.",
      "Ciclo 3: se consolida patron objetivo-evidencia-analisis-conclusion como transversal.",
      "Ciclo 3: se mantiene regla de marcar supuestos y fuentes provisionales.",
      "Ciclo 3: se evita transferencia de contenido tematico exclusivo de Filosofia del Derecho.",
      "Ciclo 3: se refuerza resolucion de placeholders y rutas antes de compilacion."
    ]
  }
}