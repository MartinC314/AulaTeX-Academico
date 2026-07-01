{
  "summary": [
    "Se consolida memoria lateral para Actividad 4 con deduplicación lossless.",
    "Se preserva identidad institucional UnADM y contexto curricular verificable.",
    "Se mantienen ejes editoriales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se refuerza validación JSON estricta y normalización estructurada antes de propagar.",
    "Supuesto: la consigna específica de Actividad 4 no está visible y requiere confirmación local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato académico.",
    "Alinear contenido con Licenciatura en Derecho y asignatura Filosofía del Derecho.",
    "Vincular ubicación curricular a semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Sostener integridad académica con citas verificables.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Separar hechos, conceptos, argumentos y postura personal.",
    "Alinear la entrega al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Adaptar Actividad 4 a los ejes del programa analítico.",
    "Incluir explícitamente problema, conceptos, evidencia y análisis propio.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Confirmar que el producto final coincida con la consigna de Actividad 4."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas heredadas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No propagar reglas dudosas sin marcarlas como supuesto."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Citar en el .tex solo claves existentes en el .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Agregar fuentes específicas de la actividad en el .bib de la asignatura.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "No inventar referencias ni metadatos faltantes.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Registrar URL verificable cuando la fuente sea digital.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a interpretación jurídica (Semana 7) y puede no aplicar a Actividad 4."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir solo patrones reutilizables, no redacción literal ni conclusiones específicas.",
    "Reutilizar reglas institucionales de calidad sin perder especificidad local.",
    "Preservar reglas útiles previas y evitar regresiones.",
    "Aplicar normalización manual en ciclo 1 y ciclo 2 si reaparecen salidas no estructuradas."
  ],
  "open_questions": [
    "Confirmar consigna textual de Actividad 4: producto, extensión y criterios de evaluación.",
    "Confirmar si Actividad 4 exige reporte, presentación u otro formato.",
    "Confirmar rúbrica docente específica para ajustar profundidad argumentativa.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar nombre canónico final del archivo .bib de la asignatura.",
    "Confirmar si Actividad 4 reutiliza bibliografía existente o requiere .bib incremental."
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
        "Normalización estructurada obligatoria antes de propagar.",
        "Carpeta de asignatura como entrada canónica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Filosofía del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos."
      ]
    },
    "essence": [
      "Problema jurídico o social que activa la actividad.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeación.",
      "Análisis propio y postura académica.",
      "Conclusión transferible a la práctica jurídica."
    ],
    "reason_for_being": [
      "Transformar la planeación semanal en entregables académicos con fundamento jurídico y evidencia verificable.",
      "Asegurar trazabilidad entre consigna, argumentación, fuentes y cierre jurídico."
    ],
    "style_markers": [
      "Definir objetivo antes del desarrollo.",
      "Separar secciones funcionales con lógica jurídica.",
      "Sostener afirmaciones con cita explícita.",
      "Marcar supuestos cuando falte evidencia local."
    ],
    "argumentative_patterns": [
      "Plantear problema inicial.",
      "Desarrollar marco conceptual y normativo.",
      "Contrastar fuentes con análisis propio.",
      "Emitir postura justificada.",
      "Cerrar con conclusión jurídica aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ejes editoriales de Filosofía del Derecho",
        "Integridad académica y verificabilidad",
        "Normalización estructurada",
        "Validación JSON para propagación",
        "Relación entre problema, evidencia y conclusión jurídica"
      ],
      "citations": [
        "README de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad académica y verificabilidad",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y formato académico."
        },
        {
          "source": "Ejes editoriales de Filosofía del Derecho",
          "target": "Relación entre problema, evidencia y conclusión jurídica",
          "kind": "develops",
          "justification": "Los ejes ordenan el flujo argumentativo de cada actividad."
        },
        {
          "source": "Normalización estructurada",
          "target": "Validación JSON para propagación",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay reutilización segura."
        }
      ],
      "evidence": [
        "README: identidad UnADM, entrada canónica y conclusión jurídica con criterio propio.",
        "Programa analítico: cinco ejes de trabajo reutilizables.",
        "Antecedentes de salida no parseable: aplicar gate JSON estricto."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas con variaciones ortográficas.",
      "Se conservaron reglas útiles previas sin recorte semántico.",
      "Se reforzó separación entre patrones transferibles y contenido específico de hermano.",
      "Se mantuvieron supuestos explícitos donde faltan datos locales."
    ]
  }
}