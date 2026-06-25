{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre actividad de origen y materia destino.",
    "Se preservan reglas utiles previas sin regresion y con deduplicacion lossless.",
    "Se refuerza modelo estable de cinco ejes: problema, conceptos, producto, analisis propio y conclusion juridica.",
    "Se mantiene normalizacion estructurada obligatoria antes de propagacion recursiva.",
    "Se confirma control tecnico de placeholders tipo $(@{...}.Slug) en README y programa analitico."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares confirmados de la materia: semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Conservar enfoque juridico aplicado a contratos y obligaciones.",
    "Usar el codigo de curso LDE-S4B1 cuando la plantilla lo requiera.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como [supuesto] todo dato no visible en la consigna local.",
    "Tratar herencias no verificadas de Codex o GPT-Pro como provisionales."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el entregable al producto solicitado por la planeacion semanal.",
    "Mantener trazabilidad entre objetivo, evidencia, argumento y conclusion.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Explicitar postura argumentada del estudiante y evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y cierre.",
    "Distinguir problema, norma o doctrina, analisis y criterio propio.",
    "Distinguir bibliografia base y fuentes especificas por actividad.",
    "No trasladar contenido de otras materias sin adecuacion contractual."
  ],
  "quality_gates": [
    "Bloquear persistencia o propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "No degradar reglas utiles previas durante union-dedupe."
  ],
  "latex_rules": [
    "Usar plantilla base local de reporte o presentacion segun consigna.",
    "Mantener metadatos completos: curso, autor, universidad, ubicacion y subtitulo de actividad.",
    "Actualizar documentsubtitle segun numero y tipo de actividad.",
    "Ajustar documenttitle cuando deje de ser plantilla base.",
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver placeholders tipo $(@{...}.Slug) en README y programa analitico antes de compilar.",
    "Usar derechos-de-los-contratos-y-obligaciones.bib como archivo canonico local."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y documentos juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente editorial o URL.",
    "Registrar fuentes especificas de cada actividad en el .bib canonico local.",
    "Conservar y reutilizar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Declarar [supuesto] cuando una referencia obligatoria no este disponible."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo abstracciones editoriales estables.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferir redaccion literal o contenido tematico exclusivo de Filosofia del Derecho.",
    "Aplicar compatibilidad disciplinar antes de propagacion lateral.",
    "Mantener estrategia progresiva y conservadora: agregar solo mejoras verificables."
  ],
  "open_questions": [
    "Confirmar guia formal de citacion juridica obligatoria en esta materia.",
    "Confirmar rubrica de evaluacion por actividad para calibrar profundidad argumentativa.",
    "Confirmar si presentacion comparte todos los metadatos del reporte.",
    "Confirmar alcance normativo por actividad: federal, local o mixto.",
    "Supuesto: falta consigna textual de actividades hijas; validar producto exacto por semana."
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
      "Modelo transversal de cinco ejes editoriales.",
      "Normalizacion estructurada previa a toda propagacion.",
      "Analisis juridico propio sustentado en evidencia verificable.",
      "Conclusion juridica transferible a practica profesional."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y verificables.",
      "Asegurar coherencia entre problema, fuentes, argumento y cierre.",
      "Sostener continuidad institucional entre nodos de la suite LaTeX."
    ],
    "style_markers": [
      "Supuestos etiquetados como [supuesto].",
      "Secciones funcionales y trazables.",
      "Cierre juridico operativo.",
      "Sin contenido de relleno ni afirmaciones sin fuente."
    ],
    "argumentative_patterns": [
      "Problema inicial delimitado.",
      "Marco conceptual y normativo pertinente.",
      "Analisis propio con postura.",
      "Conclusion aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalizacion estructurada",
        "Cinco ejes editoriales",
        "Evidencia verificable",
        "Analisis juridico propio",
        "Conclusion transferible",
        "Enfoque contractual"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "La politica institucional exige integridad academica y citas comprobables."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Cinco ejes editoriales",
          "kind": "depends_on",
          "justification": "La propagacion util requiere formato valido y estructura minima completa."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Analisis juridico propio",
          "kind": "develops",
          "justification": "La secuencia problema-conceptos-producto habilita argumentacion propia."
        },
        {
          "source": "Analisis juridico propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "El cierre profesional deriva del razonamiento sustentado."
        },
        {
          "source": "Enfoque contractual",
          "target": "Cinco ejes editoriales",
          "kind": "contrasts",
          "justification": "El metodo es transversal, pero el contenido debe adaptarse a contratos y obligaciones."
        }
      ],
      "evidence": [
        "README de materia: identidad UnADM, ubicacion curricular y carpeta canonica.",
        "Programa analitico: cinco ejes y proposito de realizacion.",
        ".bib local: entradas base institucionales verificables.",
        "Regla tecnica vigente: resolver placeholders $(@{...}.Slug) antes de compilar."
      ]
    },
    "reinforcement_log": [
      "Ciclo 7: deduplicacion completa de reglas repetidas en origen y destino.",
      "Ciclo 7: se transfiere solo abstraccion estable, sin arrastrar contenido tematico no equivalente.",
      "Ciclo 7: se preservan gates de JSON parseable y normalizacion previa como control transversal.",
      "Ciclo 7: se refuerza compatibilidad disciplinar para evitar contaminacion entre materias."
    ]
  }
}