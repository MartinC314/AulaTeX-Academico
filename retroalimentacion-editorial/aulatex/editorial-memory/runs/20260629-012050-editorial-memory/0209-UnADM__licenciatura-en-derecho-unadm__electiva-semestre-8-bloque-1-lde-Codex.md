{
  "summary": [
    "Se sincroniza memoria transversal desde Actividad 1 de Filosofía del Derecho hacia materia Electiva S8B1 sin transferir contenido temático específico.",
    "Se preservan reglas estables de identidad UnADM, estructura argumentativa, trazabilidad y control de calidad.",
    "Se refuerza normalización obligatoria: solo propagar salidas JSON parseables y estructuradas.",
    "Se mantiene compresión lossless por unión y deduplicación semántica, sin recorte de reglas útiles.",
    "Se incorporan mejoras verificables del contexto local: placeholders y nombres corruptos en README/programa."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar tono jurídico formal, claro, verificable y sin ambigüedad.",
    "Conservar contexto curricular del destino: Licenciatura en Derecho, semestre 8, bloque 1, tipo Electiva.",
    "No mezclar metadatos curriculares de nodos no equivalentes.",
    "Marcar como supuesto todo dato no confirmado en consigna o documentos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Usar la carpeta de materia como punto de entrada canónico."
  ],
  "structure_rules": [
    "Aplicar secuencia reusable: problema, conceptos o fuentes, análisis propio, cierre jurídico.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear cada entrega al producto solicitado en la planeación semanal.",
    "Separar síntesis de fuentes y postura propia del estudiante.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener consistencia entre README, programa analítico, plantilla y producto final."
  ],
  "activity_rules": [
    "Declarar objetivo de actividad al inicio.",
    "Vincular el producto con un problema jurídico o social concreto.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir fuentes de semanas distintas sin evidencia local.",
    "No transferir redacción literal entre nodos transversales."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de reutilizar memoria.",
    "Confirmar respaldo o marca de supuesto en toda afirmación.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Corregir placeholders de automatización antes de entrega final.",
    "Corregir nombres de archivo corruptos en README y programa antes de propagar."
  ],
  "latex_rules": [
    "Mantener plantilla LaTeX base de materia y consistencia de metadatos.",
    "Usar codificación compatible con español académico.",
    "Mantener clase y configuración documental estables salvo justificación.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README, programa y referencias.",
    "Completar portada con datos confirmados; marcar pendientes como supuesto si falta dato."
  ],
  "bibliography_rules": [
    "Usar electiva-semestre-8-bloque-1.bib como archivo bibliográfico local canónico.",
    "Registrar fuentes específicas por actividad en el .bib local.",
    "No inventar referencias; usar solo fuentes consultables y verificables.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Mantener claves BibTeX estables y descriptivas.",
    "Distinguir bibliografía base institucional de bibliografía específica de actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas editoriales estables y transversales.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar propagar contenido temático específico de Filosofía del Derecho a la electiva.",
    "Aplicar unión-dedupe lossless en cada ciclo para evitar duplicados semánticos.",
    "Mantener ciclo 1 en modo conservador con normalización manual cuando falte insumo local."
  ],
  "open_questions": [
    "Confirmar créditos oficiales de la electiva para portada y README.",
    "Confirmar nombre oficial de la asignatura si difiere de la etiqueta actual.",
    "Confirmar figura docente para completar plantilla.",
    "Confirmar si existe consigna local de actividades para reforzar reglas específicas.",
    "Supuesto: el código LDE-S8B1 sigue provisional hasta validación institucional."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Verificable y sobrio."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Normalización estructurada obligatoria antes de propagar.",
        "Carpeta de materia como entrada canónica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 8, bloque 1, tipo Electiva.",
        "Transferencia transversal conservadora entre nodos no equivalentes."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Conceptos y fuentes pertinentes.",
      "Análisis jurídico propio.",
      "Conclusión transferible.",
      "Trazabilidad de evidencia.",
      "Normalización JSON antes de propagación."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos y verificables.",
      "Asegurar coherencia editorial transversal sin contaminación temática entre materias.",
      "Preservar memoria útil con deduplicación lossless y sin regresión."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Supuestos explícitos cuando falte evidencia.",
      "Separación clara entre fuente y postura propia.",
      "Consistencia terminológica institucional."
    ],
    "argumentative_patterns": [
      "Delimitación del problema.",
      "Marco conceptual o normativo breve.",
      "Análisis crítico propio con evidencia.",
      "Conclusión jurídica aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalización JSON",
        "Trazabilidad de evidencia",
        "Análisis jurídico propio",
        "Conclusión transferible",
        "Transferencia transversal conservadora"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Trazabilidad de evidencia",
          "kind": "supports",
          "justification": "La integridad académica exige respaldo verificable."
        },
        {
          "source": "Normalización JSON",
          "target": "Transferencia transversal conservadora",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay propagación confiable."
        },
        {
          "source": "Análisis jurídico propio",
          "target": "Conclusión transferible",
          "kind": "develops",
          "justification": "La postura argumentada habilita aplicación profesional."
        },
        {
          "source": "Transferencia transversal conservadora",
          "target": "Identidad institucional UnADM",
          "kind": "supports",
          "justification": "Permite compartir reglas estables sin mezclar contexto temático."
        }
      ],
      "evidence": [
        "README de electiva: pauta editorial y ubicación curricular.",
        "Programa analítico de electiva: ejes de trabajo reutilizables.",
        "Regla institucional heredada: bloquear salidas no JSON parseables.",
        "Archivo .bib local con fuentes institucionales verificables."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas por forma y significado.",
      "Se conservaron reglas útiles previas sin eliminación regresiva.",
      "Se reforzaron gates de parseo JSON y trazabilidad de citas.",
      "Se mantuvo separación entre abstracciones estables y contenido temático local.",
      "Se marcaron supuestos activos de créditos, código y figura docente."
    ]
  }
}