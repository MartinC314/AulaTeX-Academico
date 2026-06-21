{
  "summary": [
    "Se consolida refuerzo lateral para Actividad 4 con deduplicación lossless.",
    "Se preservan reglas institucionales UnADM, estructura editorial y control de calidad.",
    "Se transfiere solo patrón reusable desde Actividad 1, sin copiar conclusiones ni bibliografía exclusiva.",
    "Se mantiene validación JSON estricta por antecedentes de salidas no parseables.",
    "Supuesto: la consigna específica de Actividad 4 no está visible; se deja estructura base verificable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato académico.",
    "Alinear la actividad a Licenciatura en Derecho y asignatura Filosofía del Derecho.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Vincular ubicación curricular a semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeación semanal.",
    "Separar hechos, conceptos, argumentos y postura personal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Adaptar Actividad 4 a los cinco ejes del programa analítico.",
    "Incluir explícitamente problema, conceptos, evidencia y análisis propio.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Confirmar formato final solicitado antes de cerrar versión (reporte, presentación u otro)."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas heredadas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar correspondencia del producto con la consigna de Actividad 4.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Citar en .tex solo claves existentes en .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir nombres con caracteres dañados antes de referenciar archivos."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y jurídicas verificables (UnADM, SCJN, UNAM-IIJ).",
    "Registrar fuentes específicas de Actividad 4 en el .bib canónico de asignatura.",
    "No inventar referencias ni metadatos faltantes.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a Semana 7; verificar pertinencia para Actividad 4 antes de reutilizar."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Reutilizar reglas institucionales sin reducir especificidad local.",
    "Transferir patrones, no redacción literal ni conclusiones entre hermanos.",
    "Preservar reglas útiles previas y evitar regresiones.",
    "Si falta consigna local, propagar estructura base y abrir preguntas.",
    "Mantener bandera de normalización manual para ciclos con salidas no estructuradas."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 4.",
    "Confirmar producto requerido y extensión.",
    "Confirmar rúbrica de evaluación específica.",
    "Confirmar fuentes obligatorias de la semana de Actividad 4.",
    "Confirmar nombre canónico final del archivo .bib de la asignatura.",
    "Confirmar si Actividad 4 reutiliza bibliografía existente o requiere bloque .bib propio."
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
      "Conceptos y marco normativo/doctrinal pertinentes.",
      "Producto alineado a planeación.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en entregables académicos verificables.",
      "Asegurar trazabilidad entre problema, evidencia y conclusión.",
      "Sostener estándar institucional UnADM en cada actividad."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Cita explícita en afirmaciones sustantivas.",
      "Supuestos marcados cuando faltan datos locales."
    ],
    "argumentative_patterns": [
      "Plantear problema.",
      "Definir conceptos y marco.",
      "Contrastar fuentes con análisis propio.",
      "Emitir postura justificada.",
      "Cerrar con conclusión aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalización estructurada",
        "Validación JSON estricta",
        "Ejes editoriales de Filosofía del Derecho",
        "Integridad académica y verificabilidad",
        "Relación problema-evidencia-conclusión"
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
          "justification": "Los ejes definen secuencia mínima reusable."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia segura."
        },
        {
          "source": "Integridad académica y verificabilidad",
          "target": "Conclusión jurídica propia",
          "kind": "supports",
          "justification": "La conclusión válida requiere evidencia trazable."
        }
      ],
      "evidence": [
        "README: identidad UnADM, entrada canónica, integridad académica y conclusión propia.",
        "Programa analítico: cinco ejes de trabajo estables.",
        "Antecedentes de salida no parseable: se mantiene gate de JSON estricto.",
        "Token Slug sin resolver en README/programa: requiere normalización documental."
      ]
    },
    "reinforcement_log": [
      "Ciclo 47: deduplicación semántica aplicada sin recorte de reglas útiles.",
      "Ciclo 47: se reforzó transferencia lateral por patrones reutilizables.",
      "Ciclo 47: se bloquearon elementos no transferibles entre hermanos (redacción/conclusiones/bibliografía específica).",
      "Ciclo 47: se preservó trazabilidad de supuestos y controles de calidad."
    ]
  }
}