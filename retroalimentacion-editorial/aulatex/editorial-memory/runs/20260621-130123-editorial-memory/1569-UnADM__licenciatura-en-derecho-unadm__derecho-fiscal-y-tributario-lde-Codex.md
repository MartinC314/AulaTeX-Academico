{
  "summary": [
    "Se sincroniza memoria transversal con enfoque conservador y sin regresión.",
    "Se transfieren solo abstracciones editoriales estables desde actividad origen a materia destino.",
    "Se preserva identidad UnADM y contexto curricular local del destino.",
    "Se refuerza compresión lossless por unión y deduplicación.",
    "Se mantiene bloqueo de propagación ante salidas no JSON parseables.",
    "Se consolida ADN argumentativo reusable: problema, marco, análisis propio y conclusión jurídica."
  ],
  "identity_rules": [
    "Conservar identidad institucional UnADM en tono, portada y metadatos.",
    "Usar contexto curricular del destino: Derecho fiscal y tributario, semestre 6, bloque 1, obligatoria, 8 créditos.",
    "Usar carpeta de asignatura como entrada canónica editorial.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Verificar datos personales y figura docente antes de entrega final."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el producto con la planeación semanal y la consigna.",
    "Cerrar con conclusión jurídica transferible a práctica profesional.",
    "Mantener separación entre reporte .tex, presentación .tex y .bib local.",
    "Corregir rutas y nombres rotos en README y programa analítico antes de publicar."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Evitar entregas solo descriptivas.",
    "Vincular argumentos fiscal-tributarios con aplicación profesional concreta.",
    "No transferir contenido temático literal de Filosofía del Derecho al destino."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar consistencia entre metadatos de portada, README y programa analítico.",
    "Revisar placeholders y tokens sin resolver en README, .tex y .bib.",
    "Verificar compilación sin errores críticos y sin entornos truncados."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Actualizar título, subtítulo y actividad real antes de entrega.",
    "Cerrar correctamente todos los entornos tabular y el documento.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir rutas truncadas detectadas en README."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y normas jurídicas verificables.",
    "Registrar fuentes específicas por actividad en derecho-fiscal-y-tributario.bib.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Usar malla curricular solo para respaldo de ubicación curricular."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar transversalmente identidad, estructura reusable y gates de calidad.",
    "Evitar propagar datos específicos de una actividad a nodos no equivalentes.",
    "Aplicar normalización manual si la entrada heredada es no estructurada.",
    "Mantener estrategia progresiva y conservadora sin recorte de reglas útiles."
  ],
  "open_questions": [
    "Supuesto: falta consigna específica de la próxima actividad del destino.",
    "Confirmar formato de citación exigido por la asignatura.",
    "Confirmar si autor y matrícula deben permanecer en plantillas compartidas.",
    "Confirmar nombre definitivo de figura docente en portada.",
    "Confirmar si se requiere bibliografía fiscal base adicional por unidad."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con trazabilidad de fuentes.",
        "Supuestos etiquetados y verificables."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia destino: Derecho fiscal y tributario.",
        "Semestre 6, bloque 1, obligatoria, 8 créditos."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Marco conceptual y normativo.",
      "Análisis propio sustentado.",
      "Conclusión jurídica transferible.",
      "Trazabilidad editorial y técnica."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos y verificables.",
      "Asegurar consistencia institucional, argumentativa y técnica en toda entrega."
    ],
    "style_markers": [
      "Inicio con problema concreto.",
      "Secciones funcionales sin relleno.",
      "Citas verificables en cada afirmación relevante.",
      "Cierre profesional con implicación práctica."
    ],
    "argumentative_patterns": [
      "Problema inicial breve y delimitado.",
      "Marco normativo o doctrinal pertinente.",
      "Contraste de fuentes y postura propia.",
      "Conclusión aplicable al ejercicio jurídico."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema jurídico",
        "Marco normativo",
        "Análisis propio",
        "Conclusión transferible",
        "Normalización JSON",
        "Consistencia .tex/.bib"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La identidad institucional exige evidencia verificable y formato consistente."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "La postura argumentativa requiere una pregunta o conflicto delimitado."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica válida depende de fundamento explícito."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia segura entre nodos."
        }
      ],
      "evidence": [
        "README local de la materia.",
        "Programa analítico local.",
        "Archivo derecho-fiscal-y-tributario.bib.",
        "Supuesto: la transferencia es metodológica y no temática."
      ]
    },
    "reinforcement_log": [
      "Ciclo 19: deduplicación completa de reglas repetidas.",
      "Ciclo 19: se preservan reglas válidas previas sin eliminación útil.",
      "Ciclo 19: se refuerzan gates de calidad y normalización estructurada.",
      "Ciclo 19: se mantiene transferencia transversal por abstracciones estables."
    ]
  }
}