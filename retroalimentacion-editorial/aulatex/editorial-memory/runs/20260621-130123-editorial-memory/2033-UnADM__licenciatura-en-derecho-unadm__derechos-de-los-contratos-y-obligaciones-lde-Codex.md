{
  "summary": [
    "Se mantiene base institucional UnADM con enfoque juridico contractual.",
    "Se refuerza normalizacion estructurada obligatoria antes de propagar.",
    "Se preserva modelo transversal de cinco ejes como patron reusable.",
    "Se incorpora control tecnico estable: resolver placeholders Slug en README y programa.",
    "Se evita transferencia de contenido tematico de Filosofia del Derecho no compatible."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares confirmados de la materia: semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Conservar enfoque disciplinar en contratos y obligaciones.",
    "Usar codigo de curso LDE-S4B1 cuando la plantilla lo pida.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como [supuesto] todo dato no visible en la consigna local.",
    "Tratar herencias no verificadas de Codex o GPT-Pro como provisionales."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear entregable al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Mantener trazabilidad entre objetivo, evidencia, argumento y conclusion.",
    "Distinguir bibliografia base y fuentes especificas por actividad."
  ],
  "activity_rules": [
    "Explicitar postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y cierre.",
    "Adecuar contenido heredado a contexto contractual antes de usarlo.",
    "No trasladar contenido de otras materias sin adaptacion disciplinar.",
    "Marcar supuestos cuando falte instruccion especifica."
  ],
  "quality_gates": [
    "Bloquear persistencia o propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar compatibilidad disciplinar antes de propagacion lateral.",
    "No degradar reglas utiles previas durante union-dedupe."
  ],
  "latex_rules": [
    "Usar plantilla base local de reporte o presentacion segun consigna.",
    "Mantener metadatos completos: curso, autor, universidad, ubicacion y subtitulo.",
    "Actualizar documentsubtitle con numero real de actividad antes de compilar.",
    "Ajustar documenttitle al producto final y no dejar texto de plantilla.",
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver placeholders tipo $(@{...}.Slug) en README y programa analitico antes de referenciar archivos.",
    "Usar derechos-de-los-contratos-y-obligaciones.bib como nombre canonico local [supuesto hasta validar en todos los artefactos]."
  ],
  "bibliography_rules": [
    "Usar derechos-de-los-contratos-y-obligaciones.bib como archivo canonico de materia.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Agregar fuentes especificas por actividad en el .bib local.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "No inventar referencias.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Separar bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas abstractas estables.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Excluir metadatos hiperlocales al propagar a nodos no equivalentes.",
    "Aplicar union-dedupe sin regresion de reglas utiles previas.",
    "Mantener control transversal de normalizacion JSON en todo salto lateral.",
    "Abrir preguntas locales cuando falte consigna de actividad destino."
  ],
  "open_questions": [
    "Confirmar guia formal de citacion obligatoria en la materia.",
    "Confirmar rubrica por actividad para calibrar profundidad argumentativa.",
    "Confirmar si presentacion comparte todos los metadatos del reporte.",
    "Confirmar alcance de fuentes por actividad: federales, locales o mixtas.",
    "Confirmar en archivos auxiliares que el .bib canonico coincide con el Slug resuelto."
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
      "Conceptos y marco normativo pertinentes.",
      "Producto alineado a planeacion.",
      "Analisis juridico propio sustentado.",
      "Conclusion transferible a practica profesional."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos juridicos verificables.",
      "Sostener coherencia entre identidad institucional y ejecucion tecnica LaTeX.",
      "Permitir propagacion transversal segura sin contaminar contexto disciplinar."
    ],
    "style_markers": [
      "Supuestos etiquetados como [supuesto].",
      "Secciones funcionales y trazables.",
      "Cierre juridico operativo.",
      "Sin redaccion literal heredada entre materias distintas."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Marco conceptual y normativo.",
      "Analisis propio con evidencia.",
      "Cierre con criterio juridico aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalizacion estructurada",
        "Cinco ejes editoriales",
        "Integridad academica",
        "Analisis juridico propio",
        "Conclusion transferible",
        "Compatibilidad disciplinar",
        "Control de placeholders Slug"
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
          "justification": "La pauta institucional exige citas verificables y formato consistente."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "supports",
          "justification": "Evita reutilizar salidas no parseables."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Analisis juridico propio",
          "kind": "develops",
          "justification": "El eje de analisis se activa tras problema, conceptos y evidencia."
        },
        {
          "source": "Analisis juridico propio",
          "target": "Conclusion transferible",
          "kind": "depends_on",
          "justification": "La conclusion valida deriva del razonamiento sustentado."
        },
        {
          "source": "Compatibilidad disciplinar",
          "target": "Propagacion recursiva",
          "kind": "supports",
          "justification": "Filtra contenido no contractual en saltos transversales."
        },
        {
          "source": "Control de placeholders Slug",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Reduce errores de archivo y trazabilidad bibliografica."
        }
      ],
      "evidence": [
        "README de materia confirma ubicacion curricular y pauta editorial.",
        "Programa analitico confirma proposito y cinco ejes.",
        "Bib local confirma entradas base institucionales.",
        "Se detectan placeholders Slug en README y programa; requieren resolucion tecnica."
      ]
    },
    "reinforcement_log": [
      "Ciclo 3: deduplicacion lossless aplicada sin eliminar reglas utiles previas.",
      "Ciclo 3: se transfiere solo abstraccion estable desde actividad origen.",
      "Ciclo 3: se bloquea transferencia de contenido tematico no equivalente.",
      "Ciclo 3: se refuerzan gates JSON, trazabilidad bibliografica y compatibilidad disciplinar."
    ]
  }
}