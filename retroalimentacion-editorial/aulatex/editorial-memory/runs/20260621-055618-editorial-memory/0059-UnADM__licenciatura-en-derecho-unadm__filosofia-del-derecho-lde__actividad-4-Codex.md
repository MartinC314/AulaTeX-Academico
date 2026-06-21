{
  "summary": [
    "Se consolida memoria lateral de Actividad 4 con deduplicación lossless.",
    "Se preserva identidad UnADM y marco curricular verificable.",
    "Se refuerza normalización estructurada y validación JSON estricta.",
    "Se transfieren patrones reutilizables sin copiar conclusiones ni redacción de Actividad 1.",
    "Supuesto: la consigna específica de Actividad 4 no está visible."
  ],
  "identity_rules": [
    "Mantener tono formal académico UnADM.",
    "Alinear contenido a Licenciatura en Derecho y Filosofía del Derecho.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Vincular contexto curricular: semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Marcar como supuesto todo dato no visible en consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el producto al formato pedido por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a práctica profesional.",
    "Separar hechos, conceptos, argumentos y postura personal."
  ],
  "activity_rules": [
    "Adaptar Actividad 4 a los cinco ejes del programa analítico.",
    "Incluir problema, conceptos, evidencia y análisis propio.",
    "Evitar entregas solo descriptivas.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Supuesto: confirmar tipo de producto exacto de Actividad 4."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de reutilizar.",
    "Normalizar respuestas no estructuradas heredadas antes de aplicar aguas abajo.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con consigna local de Actividad 4."
  ],
  "latex_rules": [
    "Usar acentos y codificación correcta en español en .tex y .bib.",
    "Citar en .tex solo claves existentes en .bib.",
    "No renombrar claves BibTeX activas.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Verificar nombres de archivo del README antes de compilar.",
    "Resolver tokens no expandidos tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: nombre canónico esperado del .bib es filosofia-del-derecho.bib."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y jurídicas verificables.",
    "Registrar fuentes específicas de la actividad en el .bib de la asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Usar filosofia-del-derecho-clean.bib solo si coincide con la consigna local.",
    "Supuesto: filosofia-del-derecho-clean.bib está orientado a Semana 7 y puede no aplicar a Actividad 4."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir solo reglas generales reutilizables entre actividades hermanas.",
    "Evitar regresiones de reglas útiles previas.",
    "Conservar banderas de normalización manual para ciclos con salidas no estructuradas.",
    "Cuando falte dato local, propagar plantilla base y pregunta abierta."
  ],
  "open_questions": [
    "Confirmar consigna textual de Actividad 4.",
    "Confirmar producto requerido: reporte, presentación u otro.",
    "Confirmar rúbrica de evaluación específica.",
    "Confirmar fuentes obligatorias de la semana de Actividad 4.",
    "Confirmar nombre canónico final del .bib por token Slug no resuelto.",
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
        "Entrada canónica en carpeta de asignatura."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos.",
        "Asignatura: Filosofía del Derecho."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Conceptos y marco normativo o doctrinal.",
      "Evidencia verificable.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en producto académico sólido.",
      "Asegurar trazabilidad entre problema, fuentes y conclusión.",
      "Mantener consistencia editorial entre actividades de la asignatura."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Secciones funcionales con lógica jurídica.",
      "Supuestos marcados cuando falte evidencia local.",
      "Cierre con aplicabilidad profesional."
    ],
    "argumentative_patterns": [
      "Plantear problema.",
      "Delimitar conceptos y norma aplicable.",
      "Contrastar fuentes con análisis propio.",
      "Sostener postura justificada.",
      "Concluir con implicación jurídica práctica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ejes editoriales de Filosofía del Derecho",
        "Normalización estructurada",
        "Validación JSON",
        "Integridad académica",
        "Conclusión jurídica propia"
      ],
      "citations": [
        "README de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Tono y formato académico",
          "kind": "supports",
          "justification": "La pauta editorial exige alineación institucional explícita."
        },
        {
          "source": "Ejes editoriales de Filosofía del Derecho",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Los ejes ordenan problema, evidencia, análisis y cierre."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay reutilización segura."
        },
        {
          "source": "Integridad académica",
          "target": "Conclusión jurídica propia",
          "kind": "supports",
          "justification": "La conclusión válida depende de respaldo verificable."
        }
      ],
      "evidence": [
        "README: identidad UnADM, entrada canónica, integridad académica.",
        "Programa analítico: cinco ejes de trabajo.",
        "Historial: antecedentes de salidas no parseables en ciclos previos."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas conservando cobertura completa.",
      "Se eliminaron relaciones con tipo no permitido y se normalizaron a esquema válido.",
      "Se preservaron reglas útiles previas sin recorte semántico.",
      "Se añadieron supuestos explícitos donde faltan datos locales verificables."
    ]
  }
}