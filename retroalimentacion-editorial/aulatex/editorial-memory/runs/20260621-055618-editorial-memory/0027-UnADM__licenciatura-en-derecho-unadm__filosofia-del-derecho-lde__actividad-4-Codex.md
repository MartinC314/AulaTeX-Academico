{
  "summary": [
    "Se consolida memoria lateral de Actividad 4 con deduplicación lossless y sin recorte útil.",
    "Se preserva identidad UnADM, marco curricular y pauta editorial canónica de la asignatura.",
    "Se refuerza validación JSON estricta por antecedentes de salidas no parseables.",
    "Se transfieren patrones reutilizables de estructura, calidad y argumentación sin copiar conclusiones ni redacción específica de Actividad 1.",
    "Supuesto: la consigna textual de Actividad 4 no está visible; se mantiene plantilla editorial base."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato académico.",
    "Alinear la actividad con Licenciatura en Derecho y asignatura Filosofía del Derecho.",
    "Sostener integridad académica con citas verificables.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validación local.",
    "Vincular ubicación curricular a semestre 1, bloque 2, obligatoria, 8 créditos con fuente institucional."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el producto al formato solicitado por la planeación semanal.",
    "Separar hechos, conceptos, argumentos y postura personal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Adaptar Actividad 4 a los cinco ejes del programa analítico.",
    "Incluir explícitamente problema, conceptos o normas, evidencia y análisis propio.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Confirmar correspondencia entre producto entregado y consigna local de Actividad 4."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas heredadas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No propagar reglas dudosas sin etiqueta de supuesto."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Citar en .tex solo claves existentes en .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Verificar nombres reales de archivos del README antes de referenciarlos.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: el .bib canónico esperado es filosofia-del-derecho.bib por slug observado."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar fuentes específicas de la actividad en el .bib de la asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Usar filosofia-del-derecho-clean.bib solo si coincide con la consigna activa.",
    "Supuesto: filosofia-del-derecho-clean.bib está orientado a interpretación jurídica (Semana 7)."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Reutilizar reglas institucionales sin perder especificidad local de actividad.",
    "Evitar regresiones de reglas útiles previas.",
    "Aplicar unión y deduplicación como método de compresión lossless.",
    "Cuando falte consigna local, propagar plantilla base y preguntas abiertas.",
    "Mantener bandera de normalización manual para ciclos con antecedentes no estructurados."
  ],
  "open_questions": [
    "Confirmar consigna textual de Actividad 4: producto, extensión y criterios de evaluación.",
    "Confirmar rúbrica docente específica para calibrar profundidad argumentativa.",
    "Confirmar si Actividad 4 requiere reporte, presentación u otro formato.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar nombre canónico final del archivo .bib con token de slug resuelto.",
    "Confirmar si la bibliografía de Semana 7 aplica o no a Actividad 4."
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
        "Carpeta de asignatura como entrada canónica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos.",
        "Asignatura: Filosofía del Derecho."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Conceptos, normas o doctrina pertinentes.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Transformar la planeación semanal en productos académicos con fundamento jurídico y utilidad profesional.",
      "Asegurar trazabilidad editorial y técnica en cada entrega."
    ],
    "style_markers": [
      "Definir objetivo al inicio.",
      "Estructurar por secciones funcionales.",
      "Citar de forma explícita y verificable.",
      "Marcar supuestos cuando falte dato local."
    ],
    "argumentative_patterns": [
      "Plantear problema.",
      "Desarrollar marco conceptual y normativo.",
      "Contrastar evidencia con análisis propio.",
      "Emitir postura justificada.",
      "Cerrar con conclusión jurídica aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalización estructurada",
        "Validación JSON estricta",
        "Integridad académica y verificabilidad",
        "Ejes editoriales de Filosofía del Derecho",
        "Relación problema-evidencia-conclusión"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "README.md de la asignatura",
        "programa-analitico-filosofia-del-derecho.md"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Tono y formato académico",
          "kind": "supports",
          "justification": "La pauta editorial exige alineación institucional explícita."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay reutilización segura."
        },
        {
          "source": "Integridad académica y verificabilidad",
          "target": "Conclusión jurídica propia",
          "kind": "supports",
          "justification": "La postura final requiere respaldo trazable."
        },
        {
          "source": "Ejes editoriales de Filosofía del Derecho",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Los ejes definen el orden argumentativo reutilizable."
        }
      ],
      "evidence": [
        "README: identidad UnADM, entrada canónica y exigencia de conclusión jurídica propia.",
        "Programa analítico: cinco ejes de trabajo transferibles.",
        "Antecedentes de salidas no parseables: se mantiene gate de JSON estricto.",
        "Token Slug sin resolver en README/programa: requiere validación de nombres reales."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas en identidad, estructura, calidad y LaTeX.",
      "Se conservaron reglas útiles previas sin eliminar controles institucionales.",
      "Se retiró transferencia de contenido específico de Actividad 1 y se mantuvieron solo patrones reutilizables.",
      "Se reforzó la distinción entre bibliografía base y bibliografía por actividad.",
      "Se mantuvieron supuestos explícitos donde faltan datos locales verificables."
    ]
  }
}