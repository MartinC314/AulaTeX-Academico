{
  "summary": [
    "Se sincroniza memoria transversal con reglas estables de estructura argumentativa y control de calidad.",
    "Se conserva identidad local del destino: UnADM, Licenciatura en Derecho, semestre 4, bloque 1, obligatoria, 8 créditos.",
    "Se refuerza normalización estructurada obligatoria antes de propagación recursiva.",
    "Se mantiene estrategia conservadora: sin traslado de contenido temático específico de Filosofía del Derecho.",
    "Se consolida cerebro editorial mínimo lossless por unión y deduplicación."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local: Bases de derecho internacional publico.",
    "Usar código local LDE-S4B1 en metadatos.",
    "Usar la carpeta de materia como entrada canónica.",
    "No mezclar metadatos curriculares entre materias.",
    "Marcar como [supuesto] todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como procedencia provisional, no como identidad del entregable."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear la estructura al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Distinguir reporte, presentación y producto visual según consigna."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Distinguir hechos, normas, doctrina, argumentos y criterio propio.",
    "No extrapolar fuentes de semanas no confirmadas para la actividad vigente.",
    "Marcar faltantes de consigna o evidencia como pendientes."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre consigna, programa analítico y producto entregado."
  ],
  "latex_rules": [
    "Reutilizar plantillas .tex locales sin romper identidad institucional.",
    "Mantener compatibilidad con article, spanish, letterpaper y oneside.",
    "Usar acentos y codificación correcta en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir nombres de archivo con caracteres anómalos antes de compilar.",
    "Revisar y cerrar entornos LaTeX incompletos antes de compilar."
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
    "Propagar solo abstracciones editoriales estables en saltos transversales.",
    "Preservar reglas útiles previas y deduplicar sin recorte semántico.",
    "No propagar supuestos como reglas definitivas.",
    "Aplicar normalización manual a memorias históricas no estructuradas de ciclos tempranos.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual."
  ],
  "open_questions": [
    "Confirmar y corregir en README/programa los tokens $(@{...}.Slug) aún no resueltos.",
    "Confirmar nombre editorial final: publico vs público para títulos visibles.",
    "Confirmar si existe rúbrica local por actividad para afinar profundidad argumentativa.",
    "Confirmar si la plantilla de reporte tiene corte de entorno tabular pendiente de reparación."
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
        "Semestre 4, bloque 1, obligatoria, 8 créditos.",
        "Asignatura destino: Bases de derecho internacional publico."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Conceptos y marco normativo/doctrinal pertinente.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir la planeación semanal en productos académicos sólidos y verificables.",
      "Asegurar coherencia entre consigna, argumentación y evidencia.",
      "Sostener una práctica editorial jurídica reusable entre actividades."
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
        "Consigna de actividad",
        "Estructura argumentativa jurídica",
        "Evidencia verificable",
        "Conclusión transferible",
        "Normalización JSON",
        "Consistencia cita-bibliografía",
        "Identidad institucional UnADM"
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
          "justification": "La estructura normalizada habilita validaciones editoriales automáticas."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura argumentativa jurídica",
          "kind": "develops",
          "justification": "La identidad define tono, formato y estándar académico."
        }
      ],
      "evidence": [
        "README destino: ubicación curricular y pauta editorial.",
        "Programa analítico destino: propósito y ejes de trabajo.",
        ".bib local: claves institucionales base.",
        "Regla persistente: bloquear propagación sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 18: se refuerzan gates de parseo JSON y normalización previa.",
      "Ciclo 18: se transfieren patrones argumentativos generales sin contenido temático de origen.",
      "Ciclo 18: se preserva contexto curricular del destino y se evita contaminación entre materias.",
      "Ciclo 18: se añade control técnico sobre tokens Slug sin expandir y entornos LaTeX incompletos."
    ]
  }
}