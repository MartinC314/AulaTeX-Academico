{
  "summary": [
    "Se mantiene cerebro editorial de materia con identidad UnADM y contexto curricular local verificado.",
    "Se refuerza transferencia transversal estable desde actividad origen: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se conserva regla crítica: no propagar salidas no estructuradas sin normalización JSON.",
    "Se confirma estrategia conservadora: no trasladar contenido temático específico de Filosofía del Derecho al destino.",
    "Se detectan tokens sin expandir y caracteres anómalos en README/programa; quedan como pendiente técnico local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local: Bases de derecho internacional publico.",
    "Alinear entregables a Licenciatura en Derecho, semestre 4, bloque 1, obligatoria, 8 créditos.",
    "Usar código de curso LDE-S4B1 en metadatos.",
    "Usar carpeta de materia como entrada canónica.",
    "Tratar Codex/GPT-Pro como procedencia provisional, no como identidad del entregable.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "No mezclar metadatos curriculares del origen con el destino."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear la estructura al producto solicitado por la planeación semanal.",
    "Distinguir reporte, presentación y producto visual según consigna.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Conservar separación entre README, programa analítico, .bib y plantillas .tex."
  ],
  "activity_rules": [
    "Adaptar cada actividad al producto exacto solicitado.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Distinguir hechos, normas, argumentos y criterio propio.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Evitar extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Validar sintaxis LaTeX y cierre de entornos antes de compilar.",
    "Verificar correspondencia entre consigna de actividad y producto final."
  ],
  "latex_rules": [
    "Reutilizar plantilla .tex local de la materia sin romper identidad institucional.",
    "Mantener compatibilidad con article, spanish, letterpaper, oneside.",
    "Completar metadatos de portada según actividad en curso.",
    "Usar acentos y codificación correcta en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Corregir caracteres anómalos en rutas y nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Revisar y cerrar correctamente entornos tabular antes de compilar."
  ],
  "bibliography_rules": [
    "Registrar fuentes específicas de actividad en bases-de-derecho-internacional-publico.bib.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Validar que toda clave citada exista en el .bib local.",
    "Mantener unadmSitioWeb y unadmMallaDerecho2024 como base institucional."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales, verificadas y no duplicadas.",
    "Aplicar compresión lossless por unión y deduplicación.",
    "Preservar reglas útiles previas sin regresión.",
    "No propagar supuestos como reglas definitivas.",
    "Transferir abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Registrar incidencias históricas de salidas no parseables para auditoría."
  ],
  "open_questions": [
    "Confirmar criterio editorial final sobre 'publico' sin acento frente a 'público'.",
    "Confirmar corrección de nombres con caracteres anómalos en README.",
    "Confirmar resolución de tokens $(@{...}.Slug) en README y programa analítico.",
    "Confirmar cierre correcto del entorno tabular en reporte-bases-de-derecho-internacional-publico.tex.",
    "Supuesto: no hay consigna de actividad específica activa en este ciclo; confirmar si se incorpora una."
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
        "Normalización estructurada obligatoria antes de propagación."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Destino verificado: semestre 4, bloque 1, obligatoria, 8 créditos.",
        "No mezclar contexto curricular de materias distintas."
      ]
    },
    "essence": [
      "Consigna de actividad como eje de diseño.",
      "Problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
      "Trazabilidad técnica y académica sin invenciones."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en entregables jurídicos sólidos y verificables.",
      "Garantizar continuidad editorial transversal con control de calidad estricto."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Secciones funcionales sin redundancia.",
      "Supuestos siempre etiquetados.",
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
        "Consistencia cita-bibliografía"
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
          "justification": "La forma del entregable depende del producto solicitado."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica válida requiere respaldo documental."
        },
        {
          "source": "Normalización JSON",
          "target": "Consistencia cita-bibliografía",
          "kind": "supports",
          "justification": "La estructura estable facilita validación cruzada y propagación segura."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura argumentativa jurídica",
          "kind": "develops",
          "justification": "El marco institucional orienta forma, tono y rigor del desarrollo."
        }
      ],
      "evidence": [
        "README de la materia destino: identidad y ubicación curricular.",
        "Programa analítico destino: propósito y ejes de trabajo.",
        "bases-de-derecho-internacional-publico.bib: base institucional verificable.",
        "Histórico de ciclos: incidencias de salida no parseable y regla de normalización."
      ]
    },
    "reinforcement_log": [
      "Ciclo 94: se consolidan reglas transversales estables sin arrastrar contenido temático del origen.",
      "Ciclo 94: se deduplican reglas repetidas y se preserva cobertura funcional completa.",
      "Ciclo 94: se refuerzan quality gates de parseo JSON, supuestos y consistencia cita-.bib.",
      "Ciclo 94: se mantiene estrategia progresiva y conservadora con propagación recursiva controlada."
    ]
  }
}