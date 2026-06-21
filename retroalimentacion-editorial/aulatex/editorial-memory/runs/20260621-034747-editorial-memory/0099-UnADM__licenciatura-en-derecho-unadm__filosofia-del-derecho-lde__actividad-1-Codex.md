{
  "summary": [
    "Memoria local canonizada para Actividad 1 de Filosofía del Derecho con identidad UnADM.",
    "Se conserva la normalización estructurada obligatoria antes de cualquier propagación.",
    "Se preservan ejes editoriales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se mantiene compresión lossless por unión y deduplicación.",
    "Se mantiene estado provisional de salidas heredadas no parseables hasta validación local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto cualquier dato no visible en la consigna de actividad.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Citar malla-curricular-derecho-unadm.pdf como base de ubicación curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna."
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
    "Verificar nombres de archivo del README antes de referenciarlos.",
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
      "Problema jurídico o social como punto de partida.",
      "Conceptos, normas y doctrina pertinentes.",
      "Producto alineado a la planeación semanal.",
      "Análisis propio con postura académica.",
      "Conclusión transferible a la práctica jurídica."
    ],
    "reason_for_being": [
      "Convertir la planeación en entregables académicos verificables.",
      "Asegurar fundamento jurídico, evidencia y criterio propio en cada actividad.",
      "Preservar coherencia entre consigna, desarrollo y cierre."
    ],
    "style_markers": [
      "Apertura con encuadre del problema.",
      "Desarrollo por bloques conceptuales y normativos.",
      "Citas explícitas y verificables.",
      "Cierre con conclusión jurídica aplicada."
    ],
    "argumentative_patterns": [
      "Plantear problema, delimitar objetivo y justificar relevancia.",
      "Exponer conceptos y marco normativo/doctrinal con fuentes.",
      "Contrastar o desarrollar ideas con análisis propio.",
      "Concluir con postura jurídica sustentada y transferible."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofía del Derecho",
        "Problema jurídico o social",
        "Marco normativo",
        "Doctrina jurídica",
        "Análisis propio",
        "Conclusión jurídica",
        "Hermenéutica e interpretación jurídica",
        "Derecho y moral",
        "Justicia",
        "Argumentación jurídica"
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
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "El encuadre inicial orienta la postura del estudiante."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusión jurídica",
          "kind": "supports",
          "justification": "La conclusión debe estar fundada en normas vigentes."
        },
        {
          "source": "Doctrina jurídica",
          "target": "Análisis propio",
          "kind": "supports",
          "justification": "La argumentación usa teoría para justificar criterio personal."
        },
        {
          "source": "Hermenéutica e interpretación jurídica",
          "target": "Argumentación jurídica",
          "kind": "develops",
          "justification": "La interpretación fortalece la justificación de tesis y casos."
        },
        {
          "source": "Derecho y moral",
          "target": "Justicia",
          "kind": "contrasts",
          "justification": "Permite distinguir validez normativa y valoración ética."
        }
      ],
      "evidence": [
        "README.md: ubicación curricular y pauta editorial canónica.",
        "programa-analitico-filosofia-del-derecho.md: propósito y ejes de trabajo.",
        "reporte-filosofia-del-derecho-Actividad-1.tex: fuente TEX reconstruible del nodo.",
        "filosofia-del-derecho-clean.bib: marcado como Semana 7, no asumible para Actividad 1."
      ]
    },
    "reinforcement_log": [
      "Ciclo 99: deduplicación semántica aplicada sin pérdida de reglas útiles.",
      "Ciclo 99: se preservó ADN editorial completo y conexiones argumentativas clave.",
      "Ciclo 99: se reforzó distinción entre bibliografía base y bibliografía específica de actividad.",
      "Ciclo 99: se mantuvo criterio de supuestos explícitos ante falta de consigna textual."
    ]
  }
}