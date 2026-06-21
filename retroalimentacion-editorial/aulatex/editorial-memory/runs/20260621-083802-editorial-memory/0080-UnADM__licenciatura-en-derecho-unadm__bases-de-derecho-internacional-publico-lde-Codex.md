{
  "summary": [
    "Se sincroniza memoria transversal desde actividad de origen hacia materia destino con estrategia conservadora.",
    "Se preservan reglas útiles previas y se deduplican sin recorte semántico.",
    "Se refuerzan ejes editoriales estables: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se mantiene normalización estructurada obligatoria antes de toda propagación recursiva.",
    "Se evita transferir contenido temático específico de Filosofía del Derecho al nodo de Derecho Internacional Público."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local: Bases de derecho internacional publico.",
    "Usar contexto curricular verificado del destino: semestre 4, bloque 1, obligatoria, 8 créditos.",
    "No mezclar metadatos curriculares entre materias origen y destino.",
    "Usar la carpeta de materia como entrada canónica.",
    "Tratar Codex/GPT-Pro como procedencia provisional, no como identidad del entregable.",
    "Marcar como supuesto todo dato no visible en la consigna local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Alinear la estructura al producto solicitado por la planeación semanal.",
    "Distinguir reporte, presentación y producto visual según consigna.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Conservar separación funcional entre README, programa analítico, .bib y plantillas .tex."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar entregas solo descriptivas.",
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
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregado y consigna de actividad.",
    "Mantener auditoría de parseo JSON por ciclo."
  ],
  "latex_rules": [
    "Reutilizar plantilla .tex local sin romper identidad institucional.",
    "Mantener compatibilidad con clase article, spanish, letterpaper y oneside.",
    "Usar acentos y codificación correcta en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Corregir caracteres anómalos en rutas y nombres de archivo.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Revisar cierre correcto de entornos tabular antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar fuentes específicas de cada actividad en bases-de-derecho-internacional-publico.bib.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Validar que toda clave citada exista en el .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas, estables y no duplicadas.",
    "Aplicar compresión lossless por unión-deduplicación, sin recorte de reglas útiles.",
    "No propagar supuestos como reglas definitivas.",
    "Preservar incidencias históricas de salidas no estructuradas para control de calidad.",
    "Transferir abstracciones editoriales, no redacción literal ni contenido temático local del origen."
  ],
  "open_questions": [
    "Confirmar criterio editorial final sobre uso de publico/público en nombres visibles. [supuesto]",
    "Confirmar normalización de nombres con caracteres anómalos detectados en README.",
    "Confirmar reparación completa de tokens $(@{...}.Slug) en archivos de contexto.",
    "Confirmar si habrá rúbrica local por actividad para ajustar profundidad argumentativa. [supuesto]"
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
        "Destino: semestre 4, bloque 1, obligatoria, 8 créditos.",
        "No mezclar contexto curricular de materias distintas."
      ]
    },
    "essence": [
      "Consigna como eje de diseño del entregable.",
      "Problema jurídico y marco conceptual verificable.",
      "Evidencia sustentada y análisis propio.",
      "Cierre con conclusión jurídica aplicable.",
      "Trazabilidad editorial y técnica en cada ciclo."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos, verificables y transferibles.",
      "Sostener coherencia entre identidad institucional, calidad argumentativa y ejecución técnica."
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
          "justification": "El tipo de producto define estructura y profundidad."
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
          "justification": "Sin parseo válido no hay transferencia segura."
        },
        {
          "source": "Consistencia cita-bibliografía",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Evita afirmaciones sin fuente y referencias inválidas."
        }
      ],
      "evidence": [
        "README destino: identidad, ubicación curricular y pauta editorial.",
        "Programa analítico destino: propósito y ejes de trabajo.",
        "Archivo .bib destino con claves institucionales base.",
        "Memoria origen: gates de parseo JSON y estructura mínima obligatoria."
      ]
    },
    "reinforcement_log": [
      "Se mantiene regla crítica: bloquear propagación sin JSON parseable.",
      "Se conserva y refuerza patrón de cinco ejes editoriales transversales.",
      "Se añaden controles técnicos reutilizables: tokens sin expandir y cierre tabular.",
      "Se evita contaminación curricular desde nodo origen no equivalente.",
      "Se consolida transferencia por abstracción estable, no por literalidad."
    ]
  }
}