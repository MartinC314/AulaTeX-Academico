{
  "summary": [
    "Se preserva base editorial UnADM del destino y se refuerza con abstracciones transversales estables del origen.",
    "Se mantiene normalizacion estructurada obligatoria antes de propagacion recursiva.",
    "Se consolida el modelo reusable de cinco ejes: problema, conceptos, producto, analisis propio y conclusion juridica.",
    "Se confirma la carpeta de materia como punto de entrada canonico para .tex y .bib.",
    "Se refuerza control tecnico de placeholders tipo $(@{...}.Slug) en README y programa analitico."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares confirmados de la materia: semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Conservar enfoque juridico aplicado a contratos y obligaciones.",
    "Usar LDE-S4B1 cuando la plantilla solicite codigo de curso.",
    "Marcar como [supuesto] todo dato no visible en la consigna local.",
    "Tratar herencias no verificadas de Codex o GPT-Pro como provisionales."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como entrada canonica.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el entregable al producto solicitado en la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Explicitar postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir bibliografia base de fuentes especificas por actividad.",
    "No trasladar contenido de otras materias sin adecuacion contractual."
  ],
  "quality_gates": [
    "Bloquear persistencia o propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No degradar reglas utiles previas durante union-dedupe."
  ],
  "latex_rules": [
    "Mantener plantilla LaTeX local de reporte o presentacion segun consigna.",
    "Mantener metadatos completos: curso, autor, universidad, ubicacion y subtitulo de actividad.",
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver placeholders tipo $(@{...}.Slug) en nombres de archivo antes de compilar."
  ],
  "bibliography_rules": [
    "Usar derechos-de-los-contratos-y-obligaciones.bib como archivo canonico local.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Registrar fuentes especificas de cada actividad en el .bib local.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente editorial o URL."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas transversales estables y disciplinares compatibles.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Excluir redaccion literal y metadatos hiperlocales al salto lateral.",
    "Aplicar normalizacion manual cuando un ciclo previo reporte salida no estructurada.",
    "Mantener estrategia progresiva y conservadora sin regresiones."
  ],
  "open_questions": [
    "[supuesto] Falta consigna textual de actividades especificas de esta materia; confirmar producto exacto por semana.",
    "Confirmar rubrica de evaluacion por actividad para calibrar profundidad argumentativa.",
    "Confirmar guia formal de citacion obligatoria en la materia.",
    "Confirmar si el uso de fuentes debe ser federal, local o mixto segun actividad.",
    "Confirmar si presentacion comparte todos los metadatos del reporte."
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
      "Modelo de cinco ejes como columna editorial transversal.",
      "Normalizacion estructurada como requisito de memoria persistente.",
      "Analisis juridico propio con cierre aplicable a practica profesional."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y verificables.",
      "Asegurar continuidad institucional UnADM entre actividades y formatos.",
      "Sostener calidad editorial sin perdida de reglas utiles previas."
    ],
    "style_markers": [
      "Supuestos etiquetados como [supuesto].",
      "Secciones funcionales y trazables.",
      "Cierre juridico operativo y no solo descriptivo."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Marco conceptual y normativo.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalizacion estructurada",
        "Problema juridico",
        "Marco normativo o doctrinal",
        "Analisis juridico propio",
        "Conclusion transferible",
        "Contratos",
        "Obligaciones",
        "Integridad academica",
        "Trazabilidad cita-bib"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige evidencia verificable y formato consistente."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis juridico propio",
          "kind": "depends_on",
          "justification": "El razonamiento inicia con conflicto delimitado."
        },
        {
          "source": "Analisis juridico propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion valida surge de argumentacion sustentada."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Trazabilidad cita-bib",
          "kind": "supports",
          "justification": "La estructura consistente permite control editorial y tecnico."
        },
        {
          "source": "Contratos",
          "target": "Obligaciones",
          "kind": "develops",
          "justification": "Son ejes disciplinares acoplados en la materia de destino."
        }
      ],
      "evidence": [
        "README de materia confirma identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico confirma cinco ejes transversales.",
        "Archivo .bib local confirma entradas institucionales base.",
        "Historial de ciclos confirma riesgo de salidas no parseables y necesidad de normalizacion previa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 4: deduplicacion lossless aplicada sin eliminar reglas utiles.",
      "Ciclo 4: transferidas solo abstracciones estables desde Filosofia del Derecho.",
      "Ciclo 4: reforzado gate de JSON parseable y normalizacion previa.",
      "Ciclo 4: mantenido enfoque local contractual del destino."
    ]
  }
}