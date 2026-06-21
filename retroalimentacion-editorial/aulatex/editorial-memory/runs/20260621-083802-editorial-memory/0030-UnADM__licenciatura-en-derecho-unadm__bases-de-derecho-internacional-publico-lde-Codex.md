{
  "summary": [
    "Se consolida sincronización transversal conservadora entre actividad de origen y materia destino.",
    "Se preservan reglas útiles previas y se aplica deduplicación sin pérdida.",
    "Se refuerzan ejes editoriales estables: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se mantiene bloqueo de propagación ante salida no JSON parseable.",
    "Se añade control de supuestos explícitos cuando falte consigna local verificable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local: Bases de derecho internacional publico.",
    "Alinear entregables a Licenciatura en Derecho, semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canónica.",
    "Tratar Codex y GPT-Pro solo como procedencia provisional.",
    "Marcar como supuesto todo dato no visible en consigna o documentos locales.",
    "No mezclar metadatos curriculares del origen con el destino."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear estructura al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a práctica profesional.",
    "Mantener separación entre reporte, presentación, programa analítico y bibliografía."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Distinguir hechos, normas, doctrina y criterio propio.",
    "Evitar extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre consigna, producto y programa analítico."
  ],
  "latex_rules": [
    "Reutilizar plantillas .tex locales sin romper identidad institucional.",
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Corregir caracteres anómalos y tokens sin expandir en README y programa analítico.",
    "Revisar y cerrar correctamente entornos tabular antes de compilar."
  ],
  "bibliography_rules": [
    "Registrar fuentes de actividad en bases-de-derecho-internacional-publico.bib.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Validar que toda clave citada exista en el .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas estables, verificadas y no duplicadas.",
    "Aplicar compresión por unión-deduplicación sin recorte semántico.",
    "No propagar supuestos como reglas definitivas.",
    "Preservar incidencias históricas de salidas no estructuradas.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferir contenido temático específico de Filosofía del Derecho al destino."
  ],
  "open_questions": [
    "Supuesto: falta consigna de actividades concretas en la materia destino; confirmar productos por semana.",
    "Confirmar criterio editorial final sobre 'publico' sin acento frente a 'público' en nombres visibles.",
    "Confirmar reparación definitiva de tokens $(@{...}.Slug) en README y programa analítico.",
    "Confirmar cierre completo del entorno tabular en reporte-bases-de-derecho-internacional-publico.tex.",
    "Confirmar si existe rúbrica formal por actividad para ajustar profundidad argumentativa."
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
        "Destino verificado: semestre 4, bloque 1, obligatoria, 8 creditos.",
        "No mezclar contexto curricular con nodos origen."
      ]
    },
    "essence": [
      "Problema jurídico o social como punto de partida.",
      "Conceptos, normas y doctrina pertinentes al caso.",
      "Evidencia verificable para sostener afirmaciones.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos.",
      "Asegurar trazabilidad, consistencia y reutilización editorial segura.",
      "Sostener calidad jurídica sin invenciones ni ambigüedad estructural."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Secciones funcionales y no redundantes.",
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
        "Consistencia cita-bibliografía",
        "Supuestos etiquetados"
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
          "justification": "El producto y su forma dependen de la consigna semanal."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica válida exige respaldo documental."
        },
        {
          "source": "Normalización JSON",
          "target": "Consistencia cita-bibliografía",
          "kind": "supports",
          "justification": "La estructura parseable habilita validaciones automáticas."
        },
        {
          "source": "Supuestos etiquetados",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Evita presentar inferencias como hechos confirmados."
        }
      ],
      "evidence": [
        "README destino: ubicación curricular y pauta editorial.",
        "Programa analítico destino: propósito y ejes de trabajo.",
        "Archivo .bib local: claves institucionales existentes.",
        "Histórico: incidencias por salidas no JSON parseables en ciclos previos."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas conservando cobertura funcional.",
      "Se reforzó gate de parseo JSON como condición de propagación.",
      "Se transfirieron abstracciones estables y se evitó traslado temático no equivalente.",
      "Se mantuvo estrategia progresiva y conservadora con no regresión."
    ]
  }
}