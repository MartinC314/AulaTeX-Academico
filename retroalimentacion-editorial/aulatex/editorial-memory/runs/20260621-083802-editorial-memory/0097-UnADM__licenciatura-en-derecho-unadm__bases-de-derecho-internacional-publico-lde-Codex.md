{
  "summary": [
    "Se consolida sincronización transversal desde actividad de Filosofía del Derecho hacia materia destino sin mover contenido temático específico.",
    "Se preserva identidad UnADM y contexto curricular local verificado: Licenciatura en Derecho, semestre 4, bloque 1, obligatoria, 8 créditos.",
    "Se refuerzan ejes editoriales estables: problema, conceptos, evidencia, análisis propio y conclusión jurídica transferible.",
    "Se mantiene política de normalización estructurada obligatoria antes de cualquier propagación recursiva.",
    "Se detectan y mantienen pendientes locales: tokens sin expandir en README/programa y corte de entorno tabular en reporte .tex."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local: Bases de derecho internacional publico.",
    "Usar código de curso LDE-S4B1 en metadatos.",
    "Usar carpeta de materia como punto de entrada canónico.",
    "No mezclar metadatos curriculares del nodo origen con el destino.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar Codex/GPT-Pro como procedencia provisional, no como identidad del entregable."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeación semanal.",
    "Distinguir reporte, presentación y producto visual según consigna.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener separación entre README, programa analítico, .bib y plantillas .tex."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Distinguir hechos, argumentos, normas y criterio propio.",
    "Evitar extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes.",
    "Adaptar cada actividad al producto exacto solicitado."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre consigna de actividad y producto entregado.",
    "Validar sintaxis LaTeX y cierre de entornos antes de compilar."
  ],
  "latex_rules": [
    "Reutilizar plantilla .tex local de la materia sin romper identidad institucional.",
    "Mantener compatibilidad con clase article, spanish, letterpaper y oneside.",
    "Usar codificación y acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar rupturas de compilación.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Corregir tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir corte de entorno tabular en reporte-bases-de-derecho-internacional-publico.tex [supuesto: persiste el corte visto en contexto local]."
  ],
  "bibliography_rules": [
    "Registrar fuentes de actividad en bases-de-derecho-internacional-publico.bib.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Validar que cada clave citada exista en el .bib local.",
    "Mantener unadmSitioWeb y unadmMallaDerecho2024 como base institucional."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas estables, abstractas y no temáticas.",
    "Aplicar unión-deduplicación lossless; no recortar reglas útiles previas.",
    "No propagar supuestos como reglas definitivas.",
    "Conservar incidencias históricas de salida no estructurada para auditoría.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Si falta consigna local, propagar solo marco editorial general y abrir vacíos.",
    "Verificar archivos afectados antes de propagar correcciones locales."
  ],
  "open_questions": [
    "Confirmar criterio editorial final sobre 'publico' vs 'público' en nombres visibles.",
    "Confirmar corrección definitiva de tokens $(@{...}.Slug) en README y programa analítico.",
    "Confirmar reparación del entorno tabular truncado en el reporte base.",
    "Definir formato mínimo de conclusión jurídica por tipo de actividad.",
    "Confirmar rúbricas locales de evaluación para ajustar profundidad argumentativa."
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
        "Asignatura: Bases de derecho internacional publico."
      ]
    },
    "essence": [
      "Consigna clara.",
      "Problema jurídico delimitado.",
      "Fundamento normativo/doctrinal verificable.",
      "Análisis propio.",
      "Conclusión jurídica aplicable."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en entregables académicos consistentes y verificables.",
      "Garantizar trazabilidad entre consigna, evidencia y conclusión.",
      "Sostener una memoria editorial reusable entre actividades y nodos."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Secciones funcionales sin redundancia.",
      "Supuestos etiquetados.",
      "Cierre con criterio jurídico transferible."
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
          "justification": "La forma y profundidad del entregable dependen del producto solicitado."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica válida requiere respaldo documental y normativo."
        },
        {
          "source": "Normalización JSON",
          "target": "Consistencia cita-bibliografía",
          "kind": "supports",
          "justification": "La estructura parseable permite validar integridad y trazabilidad."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura argumentativa jurídica",
          "kind": "develops",
          "justification": "La institución define estándares formales y académicos del entregable."
        }
      ],
      "evidence": [
        "README de la materia destino.",
        "Programa analítico editorial de la materia destino.",
        "bases-de-derecho-internacional-publico.bib.",
        "Reglas heredadas validadas de normalización y control de calidad."
      ]
    },
    "reinforcement_log": [
      "Ciclo 97: se transfieren solo abstracciones editoriales estables desde nodo transversal no equivalente.",
      "Ciclo 97: se conserva estrategia conservadora; no se migra contenido doctrinal específico de Filosofía del Derecho.",
      "Ciclo 97: se refuerza gate de JSON parseable y normalización previa a propagación recursiva.",
      "Ciclo 97: se consolidan reglas de estructura argumentativa reusable y verificación cita-bibliografía.",
      "Ciclo 97: se preservan pendientes técnicos locales como preguntas abiertas, sin convertirlos en hechos."
    ]
  }
}