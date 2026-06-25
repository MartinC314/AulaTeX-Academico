{
  "summary": [
    "Consolidar cerebro editorial transversal para Derechos de autor con identidad UnADM.",
    "Preservar reglas utiles previas sin regresion y con deduplicacion lossless.",
    "Transferir solo abstracciones estables desde Filosofia del Derecho.",
    "Mantener normalizacion estructurada obligatoria antes de propagar.",
    "Tratar herencias Codex y GPT-Pro como provisionales hasta validacion local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Mantener enfoque juridico con criterio propio en la conclusion.",
    "Tratar fuentes heredadas no verificadas como provisionales."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Conservar separacion entre reporte, presentacion y bibliografia local."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Agregar fuentes especificas por actividad al archivo .bib local.",
    "No asumir fuentes de otras semanas o materias sin validacion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Auditar README y programa analitico para eliminar tokens de plantilla sin expandir.",
    "Corregir nombres de archivo corruptos antes de publicar."
  ],
  "latex_rules": [
    "Mantener codificacion y acentos correctos en espanol en .tex y .bib.",
    "Declarar metadatos antes de \\input{template}.",
    "No dejar comandos incompletos de paquetes en el preambulo.",
    "Compilar sin errores criticos, referencias rotas ni tokens sin expandir.",
    "Mantener claves BibTeX estables para evitar roturas.",
    "No propagar datos personales del alumno a otros nodos."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos pertinentes.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Incluir fecha de consulta en fuentes web.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Usar derechos-de-autor.bib como contenedor local canonico."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales validadas.",
    "En enlaces transversales, transferir identidad, estructura reusable, calidad y grafo conceptual.",
    "No transferir redaccion literal ni contenido tematico especifico de otra materia.",
    "Mantener bandera de normalizacion manual para herencia historica no estructurada.",
    "Evitar regresiones: toda regla util previa se conserva si sigue vigente."
  ],
  "open_questions": [
    "Confirmar si la clave LDE-S5B1 es oficial en toda la suite. [supuesto]",
    "Definir nombre de figura docente para eliminar marcador pendiente.",
    "Validar si la ubicacion institucional en portada debe permanecer fija. [supuesto]",
    "Confirmar orden correcto de carga de paquetes respecto a template en esta plantilla.",
    "Confirmar cierre definitivo de herencia provisional Codex y GPT-Pro tras validacion local."
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
        "Normalizacion estructurada previa a propagacion.",
        "Carpeta de asignatura como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 5, bloque 1, obligatoria, 8 creditos.",
        "Asignatura destino: Derechos de autor."
      ]
    },
    "essence": [
      "Problema, conceptos, evidencia, analisis propio y conclusion juridica transferible.",
      "Compresion lossless por union y deduplicacion.",
      "Sincronizacion transversal conservadora y progresiva."
    ],
    "reason_for_being": [
      "Guiar productos academicos trazables, verificables y utiles para practica juridica.",
      "Asegurar continuidad editorial entre nodos sin contaminar contexto local."
    ],
    "style_markers": [
      "Frases claras y accionables.",
      "Supuestos etiquetados de forma explicita.",
      "Consistencia entre portada, desarrollo y bibliografia."
    ],
    "argumentative_patterns": [
      "Delimitar problema inicial.",
      "Construir marco conceptual y normativo.",
      "Desarrollar analisis propio sustentado.",
      "Cerrar con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Integridad bibliografica",
        "Propagacion transversal conservadora"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion transversal conservadora",
          "kind": "supports",
          "justification": "Reduce errores heredados y evita salidas no parseables."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad bibliografica",
          "kind": "supports",
          "justification": "Toda afirmacion exige respaldo trazable en .bib."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La postura argumentada habilita cierre profesional util."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Propagacion transversal conservadora",
          "kind": "depends_on",
          "justification": "La sincronizacion debe conservar marco institucional comun."
        }
      ],
      "evidence": [
        "README local define ubicacion curricular y pauta editorial.",
        "Programa analitico local fija ejes de trabajo reutilizables.",
        "derechos-de-autor.bib contiene base institucional verificable.",
        "Historial confirma necesidad de bloquear salidas no JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 20: se refuerza transferencia de abstracciones estables entre materias no equivalentes.",
      "Ciclo 20: se conserva regla de normalizacion estructurada obligatoria antes de propagar.",
      "Ciclo 20: se mantiene tratamiento provisional de herencias no verificadas.",
      "Ciclo 20: se corrige foco transversal sin arrastrar contenido tematico especifico de Filosofia del Derecho."
    ]
  }
}