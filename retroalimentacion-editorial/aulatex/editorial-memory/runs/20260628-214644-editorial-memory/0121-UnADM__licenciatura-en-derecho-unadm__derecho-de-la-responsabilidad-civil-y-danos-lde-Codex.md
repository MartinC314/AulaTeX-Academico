{
  "summary": [
    "Se consolida sincronización transversal conservadora entre actividad de origen y materia destino.",
    "Se preserva identidad institucional UnADM y contexto local del destino: Licenciatura en Derecho, semestre 6, bloque 1, obligatoria, 8 créditos.",
    "Se refuerza patrón editorial estable: problema, conceptos/fuentes, análisis propio y conclusión jurídica transferible.",
    "Se mantiene control técnico: normalización previa, JSON parseable, detección de truncamientos y placeholders sin resolver.",
    "Se evita transferir contenido temático específico de Filosofía del Derecho no aplicable a responsabilidad civil y daños."
  ],
  "identity_rules": [
    "Mantener tono formal académico UnADM en toda entrega.",
    "Usar la carpeta de materia como entrada canónica editorial.",
    "Aplicar contexto local del destino antes que metadatos heredados de otros nodos.",
    "Marcar como supuesto todo dato no confirmado en consigna o documento oficial.",
    "Tratar memorias heredadas no verificadas como provisionales hasta validación local.",
    "No declarar oficial el código de curso LDE-S6B1 sin confirmación documental."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, fundamento normativo/doctrinal, análisis propio y cierre.",
    "Alinear formato final al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica aplicable a práctica profesional.",
    "Mantener separación explícita entre reporte, presentación, programa analítico y bibliografía."
  ],
  "activity_rules": [
    "Exigir postura argumentada del estudiante, no solo descripción.",
    "Sustentar afirmaciones con fuentes verificables o marcar análisis propio.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Adaptar reglas heredadas solo si son compatibles con responsabilidad civil y daños.",
    "Evitar arrastre literal de ejemplos o casos del nodo origen sin pertinencia temática.",
    "Incluir transferencia práctica en el cierre de cada actividad."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de reutilizar memoria.",
    "Revisar no regresión de reglas útiles previas.",
    "Detectar y corregir rutas truncadas y placeholders sin resolver antes de compilar.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar que cada afirmación jurídica tenga respaldo o etiqueta de supuesto."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver tokens tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir truncamientos locales en nombres de archivos y bloques LaTeX.",
    "Supuesto: la plantilla de reporte está truncada en authortable y debe completarse antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y material jurídico verificable.",
    "No inventar referencias.",
    "Registrar fuentes específicas por actividad en el .bib local de la materia.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Mantener como base confirmada: unadmSitioWeb y unadmMallaDerecho2024."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo abstracciones editoriales estables.",
    "No propagar redacción literal ni contenido temático puntual del origen.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Aplicar estrategia progresiva: consolidar primero reglas comunes, luego ampliar con evidencia local.",
    "Mantener estrategia conservadora: no eliminar reglas útiles previas.",
    "Ciclo 1: mantener normalización manual por antecedentes de salidas no estructuradas."
  ],
  "open_questions": [
    "Confirmar guía oficial de formato de actividades para esta materia.",
    "Confirmar convención final de nombres con danos/daños en todo el árbol.",
    "Confirmar si LDE-S6B1 es código oficial.",
    "Corregir y validar truncamientos en README (eporte/eferencias).",
    "Resolver placeholder de .bib en README y programa analítico.",
    "Validar y completar bloque authortable de la plantilla .tex."
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
        "Materia destino: Derecho de la responsabilidad civil y daños.",
        "Semestre 6, bloque 1, obligatoria, 8 créditos [verificado en README local]."
      ]
    },
    "essence": [
      "Problema jurídico o social pertinente.",
      "Conceptos, normas y doctrina aplicables.",
      "Evidencia verificable.",
      "Análisis propio del estudiante.",
      "Conclusión jurídica transferible a práctica profesional."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos y verificables.",
      "Sostener continuidad editorial transversal sin contaminar especificidad temática local."
    ],
    "style_markers": [
      "Frases directas y secciones explícitas.",
      "Supuestos siempre marcados.",
      "Citas verificables y trazables al .bib local."
    ],
    "argumentative_patterns": [
      "Planteamiento del problema.",
      "Marco conceptual y normativo.",
      "Análisis crítico con postura propia.",
      "Cierre con criterio jurídico aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema jurídico",
        "Fundamento normativo/doctrinal",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "Responsabilidad civil y daños",
        "Normalización estructurada",
        "Integridad de citación"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura de entrega",
          "kind": "supports",
          "justification": "La pauta institucional fija tono, formato y criterios de integridad."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis se construye desde una pregunta guía delimitada."
        },
        {
          "source": "Fundamento normativo/doctrinal",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión válida requiere soporte normativo y doctrinal verificable."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin JSON parseable y estructura mínima, no hay reutilización segura."
        },
        {
          "source": "Reglas heredadas de Filosofía del Derecho",
          "target": "Responsabilidad civil y daños",
          "kind": "contrasts",
          "justification": "Solo se transfieren abstracciones; se excluye contenido temático no equivalente."
        }
      ],
      "evidence": [
        "README local: ubicación curricular y pauta editorial.",
        "Programa analítico local: propósito y ejes de trabajo.",
        "Bib local: unadmSitioWeb y unadmMallaDerecho2024.",
        "Memoria origen: regla estable de normalización y patrón argumentativo reusable."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin pérdida semántica.",
      "Se conservaron gates críticos de parseo JSON y normalización manual.",
      "Se reforzó separación entre abstracción editorial transferible y contenido temático local.",
      "Se mantuvieron alertas técnicas locales como control transversal reusable."
    ]
  }
}