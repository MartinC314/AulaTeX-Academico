{
  "summary": [
    "Se consolida sincronización transversal conservadora entre actividad origen y materia destino.",
    "Se preservan reglas útiles previas del destino y se deduplican sin recorte.",
    "Se transfieren solo abstracciones estables: identidad, estructura reusable, calidad y trazabilidad.",
    "No se transfiere contenido temático específico de Filosofía del Derecho al destino.",
    "Se refuerza normalización obligatoria de salidas estructuradas antes de propagación recursiva.",
    "Se mantiene contexto curricular verificado del destino: semestre 4, bloque 1, obligatoria, 8 créditos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local: Bases de derecho internacional publico.",
    "Usar código de curso LDE-S4B1 en metadatos.",
    "Usar la carpeta de materia como punto de entrada canónico.",
    "No mezclar metadatos curriculares entre materias.",
    "Usar solo contexto curricular verificado en README y programa analítico del destino.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como procedencia provisional, no como identidad."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por la planeación semanal.",
    "Distinguir reporte, presentación y producto visual según consigna.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Conservar separación entre README, programa analítico, .bib y plantillas .tex."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Distinguir hechos, normas, argumentos y criterio propio.",
    "Evitar extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregable y consigna vigente."
  ],
  "latex_rules": [
    "Reutilizar plantilla .tex local sin romper identidad institucional.",
    "Mantener compatibilidad con article, spanish, letterpaper y oneside.",
    "Usar codificación y acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Corregir caracteres anómalos en rutas y nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir corte de entornos tabular antes de compilar."
  ],
  "bibliography_rules": [
    "Registrar fuentes de actividad en bases-de-derecho-internacional-publico.bib.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Marcar referencias faltantes como pendientes.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Validar que toda clave citada exista en el .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Compartir en nodos no equivalentes solo abstracciones editoriales estables.",
    "Evitar transferencia literal de redacción entre asignaturas.",
    "Preservar reglas útiles previas sin regresión.",
    "Aplicar compresión lossless por unión y deduplicación.",
    "Mantener registro de incidencias históricas de parseo en ciclos previos."
  ],
  "open_questions": [
    "Confirmar criterio editorial final sobre 'publico' sin acento vs 'público'.",
    "Confirmar y corregir nombres con caracteres anómalos en README.",
    "Confirmar resolución definitiva de tokens $(@{...}.Slug) en README y programa analítico.",
    "Confirmar si la plantilla de reporte requiere ajuste estructural por tabular truncado.",
    "Supuesto: no hay consigna local de actividad específica en este ciclo; confirmar al abrir actividad concreta."
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
        "Asignatura: Bases de derecho internacional publico."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable.",
      "Análisis propio y postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en entregables académicos sólidos y verificables.",
      "Garantizar consistencia editorial transversal sin contaminar contexto curricular local.",
      "Asegurar trazabilidad técnica y académica en cada propagación."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Secciones funcionales sin redundancia.",
      "Supuestos etiquetados.",
      "Cierre aplicable a práctica jurídica."
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
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia segura."
        },
        {
          "source": "Consistencia cita-bibliografía",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Evita citas huérfanas y afirmaciones sin fuente."
        }
      ],
      "evidence": [
        "README destino: identidad, estructura y pauta editorial.",
        "Programa analítico destino: propósito y ejes de trabajo.",
        "bases-de-derecho-internacional-publico.bib: base institucional verificable.",
        "Regla heredada transversal: bloquear propagación sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 13: se reforzó núcleo transversal problema-conceptos-evidencia-análisis-conclusión.",
      "Ciclo 13: se mantuvo estrategia conservadora sin traslado temático de Filosofía del Derecho.",
      "Ciclo 13: se preservaron gates de parseo y normalización como condición de recursividad.",
      "Ciclo 13: se añadieron acciones verificables sobre tokens sin expandir y anomalías de archivos."
    ]
  }
}