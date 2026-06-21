{
  "summary": [
    "Se consolida memoria lateral de Actividad 4 con transferencia reusable desde Actividad 1.",
    "Se preserva identidad UnADM y marco curricular verificado: semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Se mantiene compresión lossless por deduplicación y normalización estructurada obligatoria.",
    "Se refuerzan ejes editoriales comunes: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se bloquea propagación si no hay JSON parseable o si faltan marcas de supuesto."
  ],
  "identity_rules": [
    "Mantener tono formal académico y precisión jurídica.",
    "Alinear toda entrega a UnADM, Licenciatura en Derecho y Filosofía del Derecho.",
    "Usar la carpeta de asignatura como entrada canónica documental.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Sostener integridad académica con citas verificables."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Alinear estructura al producto solicitado en planeación semanal.",
    "Cerrar con conclusión jurídica transferible a práctica profesional."
  ],
  "activity_rules": [
    "Adaptar Actividad 4 a los cinco ejes del programa analítico.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Incluir postura argumentada del estudiante con respaldo.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No trasladar conclusiones específicas de Actividad 1 a Actividad 4."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de reutilizar.",
    "Confirmar que toda afirmación tenga evidencia o marca de supuesto.",
    "Verificar correspondencia entre consigna local y producto final.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Normalizar cualquier salida no estructurada heredada antes de propagar."
  ],
  "latex_rules": [
    "Usar codificación correcta para español en .tex y .bib.",
    "Citar solo claves existentes en .bib.",
    "Mantener claves BibTeX estables para no romper compilación.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver tokens sin expandir en README y programa analítico antes de referenciar archivos.",
    "Supuesto: archivo .bib canónico esperado por slug es filosofia-del-derecho.bib; confirmar localmente."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y jurídicas verificables.",
    "Registrar fuentes específicas de Actividad 4 en el .bib de la asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a Semana 7; usar solo si la consigna de Actividad 4 coincide."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir solo patrones reutilizables, no redacción literal entre hermanos.",
    "Preservar reglas útiles previas y evitar regresiones.",
    "Aplicar unión y deduplicación semántica en cada ciclo.",
    "Mantener bandera de normalización manual para ciclos con antecedentes no estructurados."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 4.",
    "Confirmar formato requerido: reporte, presentación u otro.",
    "Confirmar rúbrica específica de evaluación.",
    "Confirmar fuentes obligatorias de la semana de Actividad 4.",
    "Confirmar nombre final del .bib canónico cuando se resuelva el token de slug en README."
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
      "Conceptos y marco normativo relevantes.",
      "Evidencia verificable y análisis propio.",
      "Cierre con conclusión jurídica aplicable."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos.",
      "Conectar teoría jurídica con práctica profesional.",
      "Asegurar trazabilidad editorial y técnica en LaTeX."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Secciones funcionales y orden argumentativo.",
      "Citas explícitas en afirmaciones sustantivas.",
      "Supuestos etiquetados cuando falte dato local."
    ],
    "argumentative_patterns": [
      "Problematizar contexto.",
      "Definir conceptos y norma aplicable.",
      "Contrastar fuentes.",
      "Formular postura propia.",
      "Concluir con transferencia profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ejes editoriales de Filosofía del Derecho",
        "Normalización estructurada",
        "Validación JSON estricta",
        "Relación problema-evidencia-conclusión"
      ],
      "citations": [
        "README.md de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Tono y formato académico",
          "kind": "supports",
          "justification": "Define consistencia editorial transversal."
        },
        {
          "source": "Ejes editoriales de Filosofía del Derecho",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Ordenan problema, conceptos, análisis y cierre."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia segura."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión jurídica propia",
          "kind": "supports",
          "justification": "Evita conclusiones sin fundamento."
        }
      ],
      "evidence": [
        "README exige identidad UnADM, citas verificables y conclusión jurídica propia.",
        "Programa analítico fija cinco ejes de trabajo reutilizables.",
        "Antecedentes de salidas no parseables justifican gate de JSON estricto."
      ]
    },
    "reinforcement_log": [
      "Ciclo 9: deduplicación semántica aplicada sin recorte de reglas útiles.",
      "Ciclo 9: reforzada separación entre patrones transferibles y contenido específico.",
      "Ciclo 9: añadida cautela explícita sobre token de slug no resuelto en rutas .bib."
    ]
  }
}