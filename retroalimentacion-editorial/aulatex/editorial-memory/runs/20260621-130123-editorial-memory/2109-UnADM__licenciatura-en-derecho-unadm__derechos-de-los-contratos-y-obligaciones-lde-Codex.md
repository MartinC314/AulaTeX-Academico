{
  "summary": [
    "Se mantiene identidad UnADM y enfoque juridico contractual del nodo destino.",
    "Se refuerza normalizacion obligatoria de salidas no estructuradas antes de propagacion.",
    "Se conserva el modelo transversal de cinco ejes: problema, conceptos, producto, analisis y conclusion.",
    "Se agrega regla tecnica estable: resolver placeholders tipo $(@{...}.Slug) en README y programa analitico.",
    "Se mantiene compresion lossless por union-dedupe sin regresion de reglas utiles."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares confirmados: semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Conservar enfoque disciplinar en derechos de los contratos y obligaciones.",
    "Usar LDE-S4B1 cuando la plantilla solicite codigo de curso.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como [supuesto] todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por la planeacion semanal.",
    "Mantener trazabilidad entre objetivo, evidencia, argumento y conclusion.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Explicitar postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y cierre.",
    "Distinguir bibliografia base de fuentes especificas por actividad.",
    "No trasladar contenido de otras materias sin adecuacion contractual.",
    "Marcar [supuesto] cuando falten instrucciones especificas de actividad."
  ],
  "quality_gates": [
    "Bloquear persistencia y propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar toda herencia no estructurada antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "No degradar reglas utiles previas durante union-dedupe."
  ],
  "latex_rules": [
    "Usar plantilla base local de reporte o presentacion segun consigna.",
    "Mantener metadatos completos: curso, autor, universidad, ubicacion y subtitulo de actividad.",
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Resolver placeholders tipo $(@{...}.Slug) en README y programa analitico antes de compilar.",
    "Verificar que el .bib referenciado sea derechos-de-los-contratos-y-obligaciones.bib.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Usar derechos-de-los-contratos-y-obligaciones.bib como archivo canonico local.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Priorizar fuentes institucionales UnADM, normas y doctrina verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Agregar fuentes especificas por actividad sin mezclarlas con base institucional."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo abstracciones editoriales estables.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Excluir metadatos hiperlocales al propagar lateralmente a nodos no equivalentes.",
    "Mantener control transversal de normalizacion JSON en todo salto.",
    "Aplicar estrategia progresiva y conservadora: agregar solo mejoras verificables."
  ],
  "open_questions": [
    "[supuesto] Falta consigna puntual de actividades de esta materia; confirmar formato por semana.",
    "Confirmar guia formal de citacion obligatoria para la materia.",
    "Confirmar alcance normativo por actividad: federal, local o mixto.",
    "Confirmar si presentacion comparte todos los metadatos del reporte.",
    "Confirmar rubrica de evaluacion para calibrar profundidad argumentativa."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 4, bloque 1, obligatoria, 8 creditos.",
        "Asignatura: Derechos de los contratos y obligaciones."
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Fundamento normativo o doctrinal verificable.",
      "Analisis juridico propio.",
      "Conclusion transferible a practica profesional.",
      "Disciplina enfocada en contratos y obligaciones."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y utiles.",
      "Asegurar coherencia entre consigna, evidencia y argumento.",
      "Sostener calidad institucional reusable en actividades hijas."
    ],
    "style_markers": [
      "Supuestos etiquetados como [supuesto].",
      "Secciones funcionales y auditables.",
      "Cierre juridico operativo.",
      "Sin redaccion literal heredada entre materias."
    ],
    "argumentative_patterns": [
      "Plantear problema concreto.",
      "Exponer marco conceptual y normativo.",
      "Contrastar fuentes y hechos del caso.",
      "Fijar postura propia sustentada.",
      "Concluir con criterio aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalizacion estructurada",
        "Problema juridico",
        "Marco normativo/doctrinal",
        "Analisis propio",
        "Conclusion transferible",
        "Contratos",
        "Obligaciones"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "supports",
          "justification": "Evita contaminar memoria con salidas no parseables."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El razonamiento exige una cuestion delimitada."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion valida deriva del argumento sustentado."
        },
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige verificabilidad y consistencia formal."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Contratos",
          "kind": "develops",
          "justification": "El contenido disciplinar se concreta en relaciones contractuales."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Obligaciones",
          "kind": "develops",
          "justification": "La materia exige analizar fuentes aplicables a obligaciones juridicas."
        }
      ],
      "evidence": [
        "README de materia: identidad UnADM, ubicacion curricular y carpeta canonica.",
        "Programa analitico: cinco ejes de trabajo y proposito editorial.",
        "Bibliografia local: unadmSitioWeb y unadmMallaDerecho2024 verificables.",
        "Deteccion local de placeholder $(@{...}.Slug) en README y programa analitico."
      ]
    },
    "reinforcement_log": [
      "Ciclo 22: deduplicacion completa de reglas repetidas sin perdida funcional.",
      "Ciclo 22: se conserva regla transversal de JSON parseable como gate duro.",
      "Ciclo 22: se transfiere patron estable de cinco ejes desde nodo de actividad origen.",
      "Ciclo 22: no se propagan contenidos tematicos de Filosofia del Derecho no reutilizables en contratos.",
      "Ciclo 22: se refuerza correccion tecnica de placeholders en rutas y nombres de .bib."
    ]
  }
}