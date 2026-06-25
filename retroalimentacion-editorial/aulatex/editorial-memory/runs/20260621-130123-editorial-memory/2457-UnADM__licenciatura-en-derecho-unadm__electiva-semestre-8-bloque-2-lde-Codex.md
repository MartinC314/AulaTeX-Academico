{
  "summary": [
    "Se consolida sincronización transversal conservadora entre actividad de origen y materia destino.",
    "Se preservan reglas estables: identidad UnADM, normalización estructurada y compresión por unión-dedupe.",
    "Se refuerzan ejes reutilizables: problema, conceptos/fuentes, análisis propio y conclusión jurídica transferible.",
    "Se mantiene bloqueo de propagación para salidas no JSON parseable.",
    "Se evita transferir contenido temático específico de Filosofía del Derecho al nodo electivo sin validación local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, metadatos y formato.",
    "Usar carpeta de materia como entrada canónica.",
    "Alinear entregables al contexto curricular local del destino: Licenciatura en Derecho, semestre 8, bloque 2, electiva.",
    "Marcar como [supuesto] todo dato no confirmado en consigna o documentos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar desarrollo en conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Alinear el producto final con la consigna semanal vigente.",
    "Cerrar con conclusión jurídica transferible a práctica profesional.",
    "Mantener consistencia entre README, programa analítico, .tex y .bib."
  ],
  "activity_rules": [
    "Traducir cada consigna semanal al producto concreto solicitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Vincular conceptos, normas o doctrina con el problema tratado.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir que bibliografía de otra semana o materia aplica automáticamente."
  ],
  "quality_gates": [
    "Bloquear consolidación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de propagar.",
    "Confirmar ausencia de placeholders y tokens sin expandir en README, programa, .tex y .bib.",
    "Validar trazabilidad entre citas en texto y archivo .bib.",
    "Confirmar que afirmaciones sin respaldo estén marcadas como [supuesto].",
    "Revisar manualmente herencias históricas de ciclo 1/ciclo 2 antes de reutilizar."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver nombres de archivo con tokens tipo $(@{...}.Slug) a literales.",
    "Corregir nombres truncados en README y listados (por ejemplo, eporte/eferencias).",
    "Actualizar en plantilla el número real de actividad antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y jurídicas verificables.",
    "Registrar fuentes específicas por actividad en el .bib local de la materia.",
    "No inventar referencias.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Mantener trazabilidad entre claves citadas y entradas existentes."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables en salto transversal.",
    "No propagar redacción literal ni contenido temático no validado localmente.",
    "Reutilizar gates de calidad como núcleo institucional común UnADM.",
    "Aplicar estrategia progresiva y conservadora: agregar mejoras verificables sin regresión.",
    "Mantener etiqueta provisional en datos heredados no confirmados."
  ],
  "open_questions": [
    "[supuesto] Confirmar créditos oficiales de la materia destino para metadatos.",
    "[supuesto] Confirmar figura docente para front matter.",
    "[supuesto] Confirmar política institucional de actualización de year/fecha de consulta en @misc.",
    "[supuesto] Confirmar si existe nombre oficial alterno de la electiva.",
    "[supuesto] Confirmar consignas reales de actividades del destino para ajustar estructura por tipo de entregable."
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
        "Normalización estructurada previa a propagación."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Destino: semestre 8, bloque 2, electiva.",
        "[supuesto] Créditos pendientes de confirmación."
      ]
    },
    "essence": [
      "Problema jurídico o social como punto de partida.",
      "Fundamento conceptual y normativo verificable.",
      "Análisis propio del estudiante.",
      "Conclusión jurídica aplicable.",
      "Control explícito de supuestos."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en entregables académicos sólidos y trazables.",
      "Asegurar coherencia entre identidad institucional, estructura argumentativa y evidencia."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Secciones explícitas y ordenadas.",
      "Postura propia respaldada con fuentes.",
      "Cierre con transferencia profesional.",
      "Marcado explícito de [supuesto]."
    ],
    "argumentative_patterns": [
      "Problema -> objetivo -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia verificable -> interpretación jurídica propia.",
      "Consigna -> producto solicitado -> validación de coherencia final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalización estructurada",
        "Integridad académica",
        "Problema jurídico",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "Trazabilidad cita-texto-bib",
        "Control de supuestos",
        "Compresión unión-dedupe"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva segura",
          "kind": "supports",
          "justification": "Evita heredar salidas no parseables o ambiguas."
        },
        {
          "source": "Integridad académica",
          "target": "Trazabilidad cita-texto-bib",
          "kind": "depends_on",
          "justification": "La verificabilidad exige correspondencia explícita entre texto y fuentes."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "Delimita el foco argumentativo y orienta la postura."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión profesional deriva del razonamiento y no del resumen."
        }
      ],
      "evidence": [
        "README del destino define identidad UnADM y pauta editorial.",
        "Programa analítico del destino fija ejes de trabajo reutilizables.",
        "Histórico de memoria exige bloqueo por JSON no parseable.",
        "Contexto local confirma riesgo de placeholders y nombres truncados."
      ]
    },
    "reinforcement_log": [
      "Ciclo 21: deduplicación lossless aplicada sin eliminar reglas útiles previas.",
      "Ciclo 21: reforzado gate de JSON parseable y normalización previa.",
      "Ciclo 21: transferidas solo abstracciones estables por relación transversal.",
      "Ciclo 21: preservada estrategia conservadora de no importar contenido temático específico sin validación local."
    ]
  }
}