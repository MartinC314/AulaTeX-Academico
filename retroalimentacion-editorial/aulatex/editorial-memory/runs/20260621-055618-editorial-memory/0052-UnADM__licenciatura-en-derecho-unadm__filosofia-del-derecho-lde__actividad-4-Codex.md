{
  "summary": [
    "Se consolida refuerzo lateral para Actividad 4 con deduplicación lossless.",
    "Se preserva identidad UnADM y contexto curricular verificable.",
    "Se mantienen ejes editoriales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se refuerza validación JSON estricta por antecedentes de salidas no parseables.",
    "Se evita copiar contenido específico de Actividad 1; solo se transfieren patrones reutilizables.",
    "Supuesto: la consigna local completa de Actividad 4 no está visible."
  ],
  "identity_rules": [
    "Mantener tono formal académico y precisión jurídica.",
    "Alinear la actividad con Licenciatura en Derecho y Filosofía del Derecho.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Vincular ubicación curricular a semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Citar malla-curricular-derecho-unadm.pdf para soporte curricular.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Separar hechos, conceptos, argumentos y postura personal.",
    "Alinear el producto al formato solicitado en la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Adaptar Actividad 4 a los cinco ejes del programa analítico.",
    "Incluir explícitamente problema, conceptos, evidencia y análisis propio.",
    "Evitar entrega solo descriptiva o de resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Confirmar que el producto final corresponde a la consigna local de Actividad 4."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de reutilizar.",
    "Normalizar respuestas no estructuradas antes de propagar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No propagar reglas dudosas sin etiqueta de supuesto."
  ],
  "latex_rules": [
    "Usar acentos y codificación correcta en español en .tex y .bib.",
    "Citar en .tex solo claves existentes en .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Verificar nombres reales de archivos en README antes de referenciar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y jurídicas verificables.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Agregar fuentes específicas de Actividad 4 en el .bib de la asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Registrar URL verificable en fuentes digitales.",
    "No asumir que filosofia-del-derecho-clean.bib aplica a Actividad 4 sin confirmación."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Reutilizar reglas institucionales sin perder especificidad local.",
    "Preservar reglas útiles previas y evitar regresiones.",
    "Transferir solo patrones reutilizables entre nodos hermanos.",
    "No transferir redacción literal ni conclusiones específicas de otra actividad.",
    "Mantener bandera de normalización manual para ciclos con salidas no estructuradas."
  ],
  "open_questions": [
    "Confirmar consigna completa de Actividad 4: producto, extensión y criterios.",
    "Confirmar rúbrica docente específica de Actividad 4.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar si Actividad 4 usa .bib existente o incremental.",
    "Confirmar nombre canónico final del .bib si persiste token sin resolver en README.",
    "Supuesto: filosofia-del-derecho-clean.bib está orientado a Semana 7 y puede no corresponder."
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
      "Problema jurídico o social como punto de partida.",
      "Conceptos y marco normativo con evidencia.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Transformar planeación semanal en productos académicos sólidos.",
      "Garantizar trazabilidad entre problema, evidencia y conclusión.",
      "Sostener calidad editorial institucional reusable."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Cita explícita de afirmaciones.",
      "Supuestos marcados cuando falten datos.",
      "Cierre con criterio jurídico propio."
    ],
    "argumentative_patterns": [
      "Plantear problema.",
      "Definir marco conceptual y normativo.",
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
        "Coherencia problema-evidencia-conclusión"
      ],
      "citations": [
        "README.md de asignatura",
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
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin JSON parseable no hay reutilización segura."
        },
        {
          "source": "Ejes editoriales de Filosofía del Derecho",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Los ejes definen secuencia argumentativa reusable."
        },
        {
          "source": "Integridad académica y verificabilidad",
          "target": "Conclusión jurídica propia",
          "kind": "supports",
          "justification": "La conclusión debe estar fundada y no ser solo opinión."
        }
      ],
      "evidence": [
        "README fija identidad UnADM, integridad académica y conclusión jurídica propia.",
        "Programa analítico define cinco ejes de trabajo reutilizables.",
        "Antecedentes de salidas no parseables justifican gate JSON estricto."
      ]
    },
    "reinforcement_log": [
      "Ciclo 52: deduplicación de reglas repetidas y variantes acentuales.",
      "Ciclo 52: eliminación de relaciones con tipo no permitido y normalización a esquema válido.",
      "Ciclo 52: refuerzo lateral sin copiar conclusiones ni bibliografía exclusiva de Actividad 1.",
      "Ciclo 52: conservación de supuestos abiertos por falta de consigna completa local."
    ]
  }
}