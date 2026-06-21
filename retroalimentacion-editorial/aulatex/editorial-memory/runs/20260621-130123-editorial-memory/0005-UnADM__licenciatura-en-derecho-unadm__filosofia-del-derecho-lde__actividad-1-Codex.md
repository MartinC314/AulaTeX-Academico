{
  "summary": [
    "Memoria local canonizada para Actividad 1 de Filosofía del Derecho con identidad UnADM.",
    "Se conserva normalización estructurada obligatoria antes de propagar.",
    "Se mantienen ejes editoriales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se preserva compresión lossless por unión y deduplicación.",
    "Se mantiene alerta: salidas no JSON parseable heredadas deben normalizarse antes de reutilizar."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto cualquier dato no visible en la consigna de actividad.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Citar malla-curricular-derecho-unadm.pdf como fuente de ubicación curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Definir objetivo puntual de la actividad antes del desarrollo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Verificar que el producto corresponda a la consigna de Actividad 1.",
    "No asumir que fuentes de semanas posteriores corresponden a Actividad 1."
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
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar fuentes específicas de la actividad en el .bib de la asignatura.",
    "No inventar referencias; usar solo obras realmente consultables.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "No asumir que filosofia-del-derecho-clean.bib corresponde a Actividad 1.",
    "Supuesto: filosofia-del-derecho-clean.bib está orientado a Semana 7 (interpretación jurídica)."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Propagar solo reglas generales cuando falte consigna textual.",
    "Ciclo 1 y ciclo 2 requieren normalización manual si se reutilizan salidas no estructuradas."
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
      "Problema jurídico o social como detonante.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable con citas.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible a la práctica."
    ],
    "reason_for_being": [
      "Convertir la planeación semanal en productos académicos evaluables y útiles profesionalmente.",
      "Preservar coherencia entre consigna, argumentación y cierre jurídico.",
      "Asegurar trazabilidad editorial entre texto, citas y .bib."
    ],
    "style_markers": [
      "Frases claras y directas.",
      "Secciones explícitas por función argumentativa.",
      "Supuestos marcados cuando falte evidencia local.",
      "Sin afirmaciones categóricas sin fuente."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo.",
      "Definir conceptos y marco doctrinal o normativo.",
      "Aplicar análisis propio sobre evidencia.",
      "Contrastar postura personal con fuentes.",
      "Cerrar con conclusión jurídica accionable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofía del Derecho",
        "Problema jurídico o social",
        "Análisis crítico del fenómeno jurídico",
        "Derecho y moral",
        "Justicia",
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
        "generales_ley_2021",
        "de_victimas_ley_2013",
        "franzoni_acevedo_ley_2017",
        "rojas_gonzalez_filosofia_derecho_2018",
        "gandara_ley_2015",
        "hernandezManriquezHermeneutica2019",
        "scjnMemoriaArgumentacion2008",
        "scjnViolenciaFisica2022",
        "scjnIncapacidadResistencia2019"
      ],
      "relations": [
        {
          "source": "Problema jurídico o social",
          "target": "Análisis crítico del fenómeno jurídico",
          "kind": "develops",
          "justification": "El programa analítico fija el problema como eje de desarrollo argumentativo."
        },
        {
          "source": "Conceptos y marco normativo",
          "target": "Postura académica propia",
          "kind": "supports",
          "justification": "La postura debe estar sustentada por doctrina y normas verificables."
        },
        {
          "source": "Interpretación jurídica",
          "target": "Argumentación jurídica",
          "kind": "depends_on",
          "justification": "La calidad argumentativa depende de la interpretación de fuentes jurídicas."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "develops",
          "justification": "La conclusión válida surge del análisis y no del resumen descriptivo."
        }
      ],
      "evidence": [
        "README.md: pauta editorial de identidad UnADM, citas verificables y conclusión jurídica.",
        "programa-analitico-filosofia-del-derecho.md: ejes de trabajo y propósito de realización.",
        "reporte-filosofia-del-derecho-Actividad-1.tex: fuente reconstruible con 79 bloques.",
        "filosofia-del-derecho-clean.bib: marcado explícito de Semana 7, no asumir para Actividad 1."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: deduplicación semántica aplicada sin pérdida de reglas útiles.",
      "Ciclo 2: se preserva ADN editorial completo del mismo nodo.",
      "Ciclo 2: se refuerza control de supuestos por ausencia de consigna textual.",
      "Ciclo 2: se mantiene trazabilidad entre reglas, citas y estructura LaTeX reconstruible."
    ]
  }
}