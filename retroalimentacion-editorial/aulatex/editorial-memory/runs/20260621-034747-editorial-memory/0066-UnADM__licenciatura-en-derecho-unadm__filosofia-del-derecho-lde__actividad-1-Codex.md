{
  "summary": [
    "Memoria local de Actividad 1 consolidada y deduplicada sin pérdida.",
    "Se mantiene identidad UnADM y ubicación curricular verificable.",
    "Se preserva normalización estructurada obligatoria antes de propagación.",
    "Se sostienen ejes editoriales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se conserva trazabilidad TEX reconstruible y control de citas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar carpeta de asignatura como punto de entrada canónico.",
    "Citar malla-curricular-derecho-unadm.pdf para ubicación curricular.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear entrega al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Transformar planeación en reporte, presentación o producto visual según consigna."
  ],
  "activity_rules": [
    "Verificar que el producto corresponda a la consigna de Actividad 1.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir que fuentes de semanas posteriores aplican a Actividad 1."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Validar correspondencia del producto con la consigna de Actividad 1."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Verificar nombres de archivo contra README y programa analítico.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar fuentes específicas de la actividad en el .bib de la asignatura.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "No asumir que filosofia-del-derecho-clean.bib corresponde a Actividad 1.",
    "Supuesto: filosofia-del-derecho-clean.bib está orientado a Semana 7 (interpretación jurídica)."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Aplicar normalización manual si se detecta salida no estructurada en nodos vecinos.",
    "Propagar solo reglas generales cuando falte consigna textual."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 1; confirmar producto exacto solicitado.",
    "Confirmar si la actividad requiere reporte, presentación u otro formato principal.",
    "Confirmar rúbrica de evaluación específica.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar nombre canónico final del archivo .bib de la asignatura.",
    "Confirmar si Actividad 1 reutiliza bibliografía existente o requiere .bib propio."
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
      "Problema jurídico o social que activa la asignatura.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeación.",
      "Análisis propio y postura académica.",
      "Conclusión transferible a la práctica jurídica."
    ],
    "reason_for_being": [
      "Transformar planeación semanal en productos académicos con fundamento jurídico y transferencia profesional.",
      "Convertir contenidos en entregables evaluables con evidencia y criterio propio.",
      "Asegurar trazabilidad entre consigna, desarrollo y cierre."
    ],
    "style_markers": [
      "Apertura con problema delimitado.",
      "Desarrollo por capas: concepto, norma/doctrina, análisis.",
      "Uso explícito de fuentes en afirmaciones sustantivas.",
      "Cierre con conclusión jurídica aplicable.",
      "Marcado explícito de supuestos."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual -> sustento normativo/doctrinal -> postura propia -> conclusión.",
      "Comparar enfoques cuando existan tensiones entre derecho y moral.",
      "Derivar implicaciones prácticas desde conceptos filosófico-jurídicos.",
      "Evitar enumeración sin hilo argumental."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofía del Derecho",
        "Justicia",
        "Fundamentos del derecho",
        "Derecho y moral",
        "Interpretación jurídica",
        "Argumentación jurídica",
        "Constitución Política de los Estados Unidos Mexicanos",
        "Ley General de Víctimas"
      ],
      "citations": [
        "finnis_estudios_2017",
        "lovon_manual_2020",
        "ruiz_rodriguez_filosofia_derecho_2009",
        "noauthor_constitucion_nodate",
        "de_victimas_ley_2013",
        "hernandezManriquezHermeneutica2019",
        "scjnMemoriaArgumentacion2008"
      ],
      "relations": [
        {
          "source": "Filosofía del Derecho",
          "target": "Fundamentos del derecho",
          "kind": "develops",
          "justification": "La asignatura define bases conceptuales del fenómeno jurídico."
        },
        {
          "source": "Derecho y moral",
          "target": "Justicia",
          "kind": "supports",
          "justification": "El análisis axiológico orienta criterios de justicia en argumentación."
        },
        {
          "source": "Interpretación jurídica",
          "target": "Argumentación jurídica",
          "kind": "depends_on",
          "justification": "La justificación de decisiones requiere métodos interpretativos."
        },
        {
          "source": "Constitución Política de los Estados Unidos Mexicanos",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "Aporta marco normativo vigente para cierre aplicable."
        }
      ],
      "evidence": [
        "README.md: identidad UnADM y pauta editorial canónica.",
        "programa-analitico-filosofia-del-derecho.md: ejes de trabajo y propósito.",
        "reporte-filosofia-del-derecho-Actividad-1.tex: estructura y claves citadas.",
        "filosofia-del-derecho-clean.bib: alcance explícito a Semana 7."
      ]
    },
    "reinforcement_log": [
      "Ciclo 66: deduplicación total sin recorte semántico.",
      "Ciclo 66: se preserva TEX reconstruible y reglas de compilación.",
      "Ciclo 66: se refuerza separación entre bibliografía de actividad y bibliografía de Semana 7.",
      "Ciclo 66: se mantiene bloqueo de propagación ante JSON inválido."
    ]
  }
}