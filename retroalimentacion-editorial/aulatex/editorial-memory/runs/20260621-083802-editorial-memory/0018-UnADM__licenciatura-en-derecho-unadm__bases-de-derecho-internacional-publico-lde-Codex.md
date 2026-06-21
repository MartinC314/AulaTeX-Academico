{
  "summary": [
    "Se mantiene cerebro editorial de materia con identidad UnADM y contexto curricular local verificado.",
    "Se refuerza sincronización transversal con reglas estables: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se conserva estrategia conservadora: no transferir contenido temático específico de Filosofía del Derecho al DIP.",
    "Se preserva normalización estructurada obligatoria antes de propagación recursiva.",
    "Se incorpora control transversal de supuestos: todo dato no visible en consigna debe etiquetarse."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial de la materia: Bases de derecho internacional publico.",
    "Alinear entregables a Licenciatura en Derecho, semestre 4, bloque 1, obligatoria, 8 créditos.",
    "Usar código de curso LDE-S4B1 en metadatos.",
    "Usar la carpeta de materia como entrada canónica.",
    "Tratar fuentes heredadas no verificadas como procedencia provisional, no como identidad.",
    "Marcar como [Supuesto] cualquier dato no visible en la consigna local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear la forma del entregable al producto solicitado por la planeación semanal.",
    "Distinguir reporte, presentación y producto visual según consigna.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Distinguir hechos, normas, doctrina, argumentos y criterio propio.",
    "No extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de [Supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna de la actividad vigente.",
    "Validar sintaxis LaTeX y cierre de entornos antes de compilar."
  ],
  "latex_rules": [
    "Reutilizar plantilla .tex local sin romper identidad institucional.",
    "Mantener compatibilidad con clase article, spanish, letterpaper y oneside.",
    "Usar acentos y codificación correcta en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar rupturas de compilación.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir caracteres anómalos en nombres de archivo y rutas antes de compilar.",
    "Revisar y reparar entornos tabular incompletos del reporte base."
  ],
  "bibliography_rules": [
    "Registrar fuentes de actividad en bases-de-derecho-internacional-publico.bib.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Validar que toda clave citada exista en el .bib local.",
    "Conservar entradas base institucionales mientras no exista instrucción local en contra."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas, abstractas y no duplicadas.",
    "Aplicar compresión lossless por unión y deduplicación, sin recorte semántico.",
    "Preservar reglas útiles previas aunque cambien de categoría.",
    "No propagar supuestos como reglas definitivas.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual en saltos transversales.",
    "Mantener incidencia histórica de salidas no parseables para auditoría."
  ],
  "open_questions": [
    "[Supuesto] Confirmar criterio ortográfico final: 'publico' vs 'público' en naming editorial.",
    "Confirmar corrección definitiva de tokens $(@{...}.Slug) en README y programa analítico.",
    "Confirmar reparación completa del entorno tabular en reporte-bases-de-derecho-internacional-publico.tex.",
    "Confirmar si hay rúbrica local por actividad para ajustar profundidad argumentativa.",
    "Confirmar catálogo mínimo de fuentes obligatorias por semana en la materia destino."
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
        "Integridad académica con citas verificables.",
        "Carpeta de materia como entrada canónica.",
        "Normalización estructurada obligatoria antes de propagación."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 4, bloque 1, obligatoria, 8 créditos.",
        "Asignatura: Bases de derecho internacional publico."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Conceptos y marco normativo o doctrinal.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en entregables jurídicos claros, verificables y útiles para práctica profesional.",
      "Asegurar trazabilidad editorial y consistencia entre consigna, desarrollo y cierre."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Secciones funcionales sin redundancia.",
      "Supuestos etiquetados.",
      "Cierre con criterio jurídico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> norma/doctrina -> análisis -> conclusión.",
      "Afirmación -> evidencia -> interpretación -> postura propia.",
      "Consigna -> desarrollo alineado -> verificación final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Consigna de actividad",
        "Estructura argumentativa jurídica",
        "Evidencia verificable",
        "Conclusión transferible",
        "Normalización JSON",
        "Consistencia cita-bibliografía",
        "Supuesto etiquetado"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Consigna de actividad",
          "target": "Estructura argumentativa jurídica",
          "kind": "depends_on",
          "justification": "El producto define forma, alcance y profundidad."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica válida requiere respaldo."
        },
        {
          "source": "Normalización JSON",
          "target": "Sincronización transversal",
          "kind": "depends_on",
          "justification": "Sin parseo válido no hay transferencia segura."
        },
        {
          "source": "Consistencia cita-bibliografía",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Evita afirmaciones sin fuente y referencias rotas."
        },
        {
          "source": "Supuesto etiquetado",
          "target": "Rigor editorial",
          "kind": "supports",
          "justification": "Separa hechos verificados de inferencias."
        }
      ],
      "evidence": [
        "README local: identidad, ubicación curricular y pauta editorial.",
        "Programa analítico local: propósito y ejes de trabajo.",
        "Archivo .bib local: base institucional existente.",
        "Memoria origen: ejes editoriales estables y gates transversales verificables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 18: se consolidan abstracciones estables desde actividad de Filosofía del Derecho hacia materia de DIP.",
      "Ciclo 18: se evita traslado de contenido temático no equivalente entre nodos transversales.",
      "Ciclo 18: se refuerza gate de JSON parseable y normalización previa a propagación.",
      "Ciclo 18: se añade regla explícita de etiquetado de [Supuesto] como control transversal."
    ]
  }
}