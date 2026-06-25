{
  "summary": [
    "Se mantiene base institucional UnADM con enfoque juridico contractual.",
    "Se refuerza normalizacion estructurada obligatoria antes de propagacion recursiva.",
    "Se conserva modelo transversal de cinco ejes sin traslado literal entre materias.",
    "Se agrega control tecnico estable para resolver placeholders tipo $(@{...}.Slug) en README y programa analitico."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares confirmados de la materia: semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Conservar enfoque disciplinar en contratos y obligaciones en todo entregable.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como [supuesto] todo dato no visible en consigna local.",
    "Tratar herencias no verificadas de Codex o GPT-Pro como provisionales."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el entregable al producto solicitado en la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener trazabilidad entre objetivo, evidencia, argumento y conclusion."
  ],
  "activity_rules": [
    "Explicitar postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y cierre.",
    "Distinguir bibliografia base de fuentes especificas por actividad.",
    "No trasladar contenido de otras materias sin adecuacion contractual."
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
    "Actualizar documenttitle y documentsubtitle al producto final antes de compilar.",
    "Verificar que el .bib canonico sea derechos-de-los-contratos-y-obligaciones.bib.",
    "Resolver placeholders tipo $(@{...}.Slug) en README y programa analitico antes de compilar.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Usar derechos-de-los-contratos-y-obligaciones.bib como archivo canonico local.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Agregar doctrina, normas y jurisprudencia solo si son verificables.",
    "No inventar referencias.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Declarar [supuesto] cuando una fuente no pueda verificarse localmente."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo abstracciones editoriales estables.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Excluir metadatos especificos cuando el nodo destino no sea equivalente.",
    "Aplicar compatibilidad disciplinar antes de propagacion lateral.",
    "Mantener estrategia conservadora: agregar solo mejoras verificables y sin regresion."
  ],
  "open_questions": [
    "[supuesto] Falta guia formal de citacion juridica obligatoria para la materia.",
    "[supuesto] Falta rubrica por actividad para calibrar profundidad argumentativa.",
    "[supuesto] Falta confirmar si toda actividad exige fuentes federales, locales o mixtas.",
    "[supuesto] Falta confirmar si presentacion replica todos los metadatos del reporte."
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
      "Evidencia verificable.",
      "Analisis juridico propio.",
      "Conclusion transferible."
    ],
    "reason_for_being": [
      "Convertir la planeacion semanal en productos academicos trazables y utiles para practica juridica.",
      "Asegurar consistencia editorial entre reporte, presentacion y bibliografia."
    ],
    "style_markers": [
      "Supuestos etiquetados como [supuesto].",
      "Secciones funcionales y trazables.",
      "Cierre juridico operativo.",
      "Sin redaccion literal heredada entre nodos transversales."
    ],
    "argumentative_patterns": [
      "Problema breve inicial.",
      "Marco conceptual y normativo.",
      "Analisis propio sustentado.",
      "Cierre con criterio juridico aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalizacion estructurada",
        "Cinco ejes editoriales",
        "Contratos",
        "Obligaciones",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion transferible"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica con citas verificables",
          "kind": "supports",
          "justification": "La pauta institucional exige evidencia trazable."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva segura",
          "kind": "supports",
          "justification": "Reduce contaminacion por salidas no parseables."
        },
        {
          "source": "Problema juridico delimitado",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere objeto de estudio claro."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion valida deriva del razonamiento sustentado."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Consistencia entre entregables",
          "kind": "supports",
          "justification": "Funciona como marco comun reusable."
        }
      ],
      "evidence": [
        "README de materia confirma identidad, ubicacion curricular y carpeta canonica.",
        "Programa analitico confirma proposito y cinco ejes de trabajo.",
        "Archivo .bib local confirma fuentes institucionales base.",
        "Se detectan placeholders tipo $(@{...}.Slug) que deben resolverse tecnicamente."
      ]
    },
    "reinforcement_log": [
      "Ciclo 13: deduplicacion lossless aplicada sin eliminar reglas utiles previas.",
      "Ciclo 13: se reforzo transferencia transversal por abstracciones estables.",
      "Ciclo 13: se preservo separacion entre identidad institucional y contexto disciplinar local."
    ]
  }
}