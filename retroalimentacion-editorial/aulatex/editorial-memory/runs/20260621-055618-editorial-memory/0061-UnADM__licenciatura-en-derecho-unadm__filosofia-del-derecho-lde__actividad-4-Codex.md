{
  "summary": [
    "Se consolida memoria lateral de Actividad 4 con deduplicación lossless.",
    "Se preserva identidad UnADM, marco curricular y pauta editorial común.",
    "Se refuerza validación JSON estricta por antecedentes de salida no parseable.",
    "Se transfieren patrones reutilizables de estructura, calidad y argumentación sin copiar conclusiones de Actividad 1.",
    "Supuesto: la consigna específica de Actividad 4 sigue no visible y debe confirmarse."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato académico.",
    "Alinear contenido con Licenciatura en Derecho y asignatura Filosofía del Derecho.",
    "Vincular ubicación curricular a semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar carpeta de asignatura como entrada canónica.",
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
    "Adaptar Actividad 4 a los cinco ejes del programa analítico.",
    "Incluir explícitamente problema, conceptos o fuentes, evidencia y análisis propio.",
    "Evitar entregas solo descriptivas.",
    "Sustentar afirmaciones con cita explícita y verificable.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Supuesto: confirmar producto exacto, extensión y rúbrica de Actividad 4."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas heredadas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Validar correspondencia del producto con la consigna local de Actividad 4."
  ],
  "latex_rules": [
    "Usar acentos y codificación correcta en .tex y .bib.",
    "Citar en .tex solo claves existentes en .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Verificar nombres reales de archivos en README antes de referenciar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y jurídicas verificables.",
    "Registrar fuentes específicas de la actividad en el .bib canónico de asignatura.",
    "No inventar referencias ni metadatos faltantes.",
    "Conservar metadatos mínimos: autor, título, año, editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a Semana 7; verificar aplicabilidad a Actividad 4."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Reutilizar reglas institucionales de calidad sin perder especificidad local.",
    "Propagar solo patrones generales cuando falte consigna textual.",
    "Evitar regresiones y no eliminar reglas útiles previas.",
    "Mantener bandera de normalización manual para ciclos con salidas no estructuradas."
  ],
  "open_questions": [
    "Confirmar consigna textual de Actividad 4.",
    "Confirmar producto requerido: reporte, presentación u otro formato.",
    "Confirmar rúbrica de evaluación específica.",
    "Confirmar fuentes obligatorias de la semana de Actividad 4.",
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
      "Conceptos y marco normativo o doctrinal.",
      "Evidencia verificable.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Transformar planeación semanal en productos académicos sólidos.",
      "Conectar fundamento jurídico, evidencia y criterio propio.",
      "Garantizar trazabilidad editorial y técnica en LaTeX."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Secciones funcionales y orden lógico.",
      "Citas verificables por afirmación relevante.",
      "Supuestos marcados cuando falte dato local."
    ],
    "argumentative_patterns": [
      "Plantear problema.",
      "Construir marco conceptual y normativo.",
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
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "README.md de la asignatura",
        "programa-analitico-filosofia-del-derecho.md"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad académica y verificabilidad",
          "kind": "supports",
          "justification": "La pauta editorial exige citas verificables y criterio propio."
        },
        {
          "source": "Normalización estructurada",
          "target": "Validación JSON estricta",
          "kind": "depends_on",
          "justification": "La propagación recursiva requiere salida parseable y completa."
        },
        {
          "source": "Ejes editoriales de Filosofía del Derecho",
          "target": "Relación problema-evidencia-conclusión",
          "kind": "develops",
          "justification": "Los ejes ordenan el argumento hasta una conclusión jurídica transferible."
        }
      ],
      "evidence": [
        "README define identidad UnADM y entrada canónica.",
        "Programa analítico define cinco ejes reutilizables.",
        "Antecedentes registran salidas no parseables; se justifica gate JSON estricto.",
        "Supuesto: falta consigna textual local de Actividad 4."
      ]
    },
    "reinforcement_log": [
      "Ciclo 61: deduplicación integral de reglas repetidas.",
      "Ciclo 61: preservadas reglas útiles heredadas sin recorte.",
      "Ciclo 61: reforzada transferencia lateral por patrones, no por contenido específico.",
      "Ciclo 61: mantenida alerta sobre tokens Slug sin resolver en documentos base."
    ]
  }
}