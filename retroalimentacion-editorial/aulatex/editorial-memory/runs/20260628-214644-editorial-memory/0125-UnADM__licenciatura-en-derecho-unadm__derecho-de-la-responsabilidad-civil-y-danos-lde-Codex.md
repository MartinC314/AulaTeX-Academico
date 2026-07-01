{
  "summary": [
    "Sincronización transversal ciclo 2 aplicada con estrategia conservadora.",
    "Se preservan reglas institucionales UnADM y estructura reusable sin regresión.",
    "Se transfiere solo abstracción estable desde actividad de origen.",
    "Se mantiene prioridad del contexto local: semestre 6, bloque 1, obligatoria, 8 créditos.",
    "Se refuerza control técnico: JSON parseable, normalización y detección de placeholders."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Usar contexto local de Licenciatura en Derecho y materia de responsabilidad civil y daños.",
    "Marcar como supuesto todo dato no confirmado en consigna o documento oficial.",
    "Tratar memorias heredadas no verificadas como provisionales hasta validación local.",
    "No declarar oficial el código LDE-S6B1 sin confirmación documental.",
    "No cambiar convención danos/daños sin confirmación documental."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como entrada canónica.",
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, fundamento normativo/doctrinal, análisis propio y cierre.",
    "Alinear el formato final al producto solicitado por la planeación semanal.",
    "Mantener separación entre reporte, presentación, programa analítico y .bib."
  ],
  "activity_rules": [
    "Formular problema jurídico pertinente a responsabilidad civil y daños.",
    "Sustentar afirmaciones con fuentes verificables o marcar análisis propio.",
    "Exigir postura argumentada del estudiante, no solo descripción.",
    "Cerrar con conclusión jurídica transferible a práctica profesional.",
    "No arrastrar contenido temático de Filosofía del Derecho si no aplica al destino.",
    "Adaptar solo patrones metodológicos reutilizables entre nodos."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de reutilización recursiva.",
    "Revisar no regresión de reglas útiles heredadas.",
    "Verificar que toda afirmación jurídica tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Detectar y corregir rutas truncadas y placeholders sin resolver."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver tokens tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir nombres truncados de archivos antes de compilar.",
    "Supuesto: plantilla .tex local está truncada en authortable y requiere cierre."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y material jurídico verificable.",
    "Registrar fuentes específicas por actividad en el .bib local.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Mantener como base confirmada: unadmSitioWeb y unadmMallaDerecho2024."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas estables, no contenido temático puntual.",
    "Aplicar compresión lossless por unión y deduplicación.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Mantener alerta de normalización manual por antecedentes de salida no estructurada.",
    "Propagar control de placeholders y truncamientos como regla técnica general."
  ],
  "open_questions": [
    "Confirmar guía oficial de formato para actividades de la materia.",
    "Confirmar convención final de nombres con danos versus daños en todo el árbol.",
    "Confirmar si LDE-S6B1 es código oficial.",
    "Corregir en README los nombres truncados de reporte y referencias.",
    "Resolver placeholder del .bib en README y programa analítico.",
    "Completar sección authortable truncada en plantilla .tex."
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
        "Normalización estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho de la responsabilidad civil y daños.",
        "Semestre 6, bloque 1, obligatoria, 8 créditos [verificado local]."
      ]
    },
    "essence": [
      "Problema jurídico delimitado.",
      "Fundamento conceptual y normativo verificable.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible.",
      "Disciplina técnica editorial sin regresión."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos y trazables.",
      "Asegurar coherencia entre identidad institucional, método jurídico y evidencia.",
      "Permitir propagación segura entre nodos no equivalentes."
    ],
    "style_markers": [
      "Frases directas y secciones explícitas.",
      "Supuestos siempre marcados.",
      "Citas trazables al .bib local.",
      "Prioridad al contexto local sobre herencias no verificadas."
    ],
    "argumentative_patterns": [
      "Problema jurídico -> marco normativo/doctrinal -> análisis propio -> conclusión aplicable.",
      "Pregunta guía explícita antes del desarrollo.",
      "Cierre con criterio jurídico y transferencia práctica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalización estructurada",
        "Problema jurídico",
        "Fundamento normativo/doctrinal",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "Responsabilidad civil y daños",
        "Integridad de citación"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin JSON parseable y estructura mínima no hay reutilización segura."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis requiere una pregunta jurídica delimitada."
        },
        {
          "source": "Fundamento normativo/doctrinal",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión válida exige sustento verificable."
        },
        {
          "source": "Reglas de Filosofía del Derecho",
          "target": "Responsabilidad civil y daños",
          "kind": "contrasts",
          "justification": "Se transfieren métodos editoriales, no contenido temático literal."
        }
      ],
      "evidence": [
        "README local con ubicación curricular y pauta editorial.",
        "Programa analítico local con ejes de trabajo.",
        "Bib local con fuentes institucionales confirmadas.",
        "Memoria origen con patrón argumentativo estable y control de normalización."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: deduplicación completa de reglas repetidas.",
      "Ciclo 2: refuerzo de gates técnicos heredados sin recorte semántico.",
      "Ciclo 2: consolidación de patrón argumentativo reusable transversal.",
      "Ciclo 2: preservación de vacíos locales como preguntas abiertas."
    ]
  }
}