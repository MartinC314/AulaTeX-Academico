{
  "summary": [
    "Se sincroniza memoria transversal desde actividad de Filosofía del Derecho hacia materia destino sin mezclar contenido temático específico.",
    "Se preservan reglas útiles previas del destino y se deduplican en formato accionable.",
    "Se refuerza ADN editorial estable: identidad UnADM, estructura argumentativa jurídica, evidencia verificable y cierre transferible.",
    "Se mantiene estrategia conservadora: transferir abstracciones editoriales, no redacción literal ni bibliografía ajena.",
    "Se mantiene bloqueo de propagación ante salidas no parseables y obligación de normalización estructurada."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial de la materia: Bases de derecho internacional publico.",
    "Usar contexto curricular verificado del destino: semestre 4, bloque 1, obligatoria, 8 créditos.",
    "No mezclar metadatos curriculares entre materias.",
    "Usar la carpeta de materia como entrada canónica.",
    "Tratar Codex/GPT-Pro como procedencia provisional, no como identidad del entregable.",
    "Marcar como supuesto todo dato no visible en consigna local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear la estructura al producto solicitado por la planeación semanal.",
    "Distinguir reporte, presentación y producto visual según consigna.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Conservar separación entre README, programa analítico, .tex y .bib."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Distinguir hechos, argumentos, normas y criterio propio.",
    "Evitar extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre consigna de actividad y producto final.",
    "Validar sintaxis LaTeX y cierre de entornos antes de compilar."
  ],
  "latex_rules": [
    "Reutilizar plantilla .tex local de la materia sin romper identidad institucional.",
    "Mantener compatibilidad con clase article, spanish, letterpaper y oneside.",
    "Usar acentos y codificación correcta en .tex y .bib.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Corregir caracteres anómalos en README y rutas de archivos antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "No cambiar estructura base de portada sin instrucción editorial."
  ],
  "bibliography_rules": [
    "Registrar fuentes de actividad en bases-de-derecho-internacional-publico.bib.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Validar que todas las claves citadas existan en el .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas, generales y deduplicadas.",
    "Preservar reglas útiles previas sin regresión.",
    "No propagar supuestos como reglas definitivas.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Si falta consigna local, transferir solo abstracciones editoriales estables.",
    "Mantener compresión lossless por unión y deduplicación."
  ],
  "open_questions": [
    "Confirmar criterio editorial final sobre 'publico' vs 'público' en nombres visibles. [supuesto]",
    "Confirmar reparación completa de tokens $(@{...}.Slug) en README y programa analítico. [supuesto]",
    "Confirmar reparación del entorno tabular truncado en reporte .tex.",
    "Confirmar formato mínimo de conclusión jurídica por tipo de evidencia en esta materia."
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
        "No mezclar contexto curricular de nodos origen."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Conceptos y marco normativo/doctrinal.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en entregables jurídicos claros, fundamentados y aplicables.",
      "Asegurar consistencia entre consigna, argumentación y evidencia.",
      "Sostener una memoria editorial persistente, reutilizable y sin regresiones."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Secciones funcionales no redundantes.",
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
          "justification": "La forma del entregable se define por el producto solicitado."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica válida requiere respaldo documental."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia segura."
        },
        {
          "source": "Consistencia cita-bibliografía",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Evita afirmaciones sin fuente y referencias rotas."
        }
      ],
      "evidence": [
        "README destino: identidad, ubicación curricular y pauta editorial.",
        "Programa analítico destino: propósito y ejes de trabajo.",
        "bases-de-derecho-internacional-publico.bib: claves institucionales base.",
        "Histórico de incidencias: salidas no estructuradas requieren normalización previa."
      ]
    },
    "reinforcement_log": [
      "Se refuerza regla transversal de normalización JSON antes de propagar.",
      "Se refuerzan ejes editoriales estables compartidos entre materias.",
      "Se conserva contexto curricular local del destino sin contaminación del origen.",
      "Se agrega control explícito de tokens sin expandir y anomalías en rutas.",
      "Se mantiene estrategia progresiva-conservadora en ciclo 1."
    ]
  }
}