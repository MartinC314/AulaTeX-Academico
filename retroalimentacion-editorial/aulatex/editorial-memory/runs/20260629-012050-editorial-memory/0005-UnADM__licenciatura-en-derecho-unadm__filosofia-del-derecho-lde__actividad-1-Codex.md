{
  "summary": [
    "Memoria local canonizada con preservación total y deduplicación lossless.",
    "Se mantiene identidad UnADM y marco curricular verificable de Filosofía del Derecho.",
    "Se consolidan ejes editoriales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se conserva regla crítica: no propagar salidas no estructuradas sin normalización JSON.",
    "Se mantiene trazabilidad de fuentes locales y marca explícita de supuestos no verificables."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Citar malla-curricular-derecho-unadm.pdf como fuente de ubicación curricular.",
    "Marcar como supuesto cualquier dato no visible en la consigna de Actividad 1.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna."
  ],
  "activity_rules": [
    "Verificar que el producto corresponda a la consigna de Actividad 1.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante, no solo resumen descriptivo.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Evitar entregas solo descriptivas.",
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
    "Verificar y corregir nombres de archivo con caracteres anómalos en README.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar fuentes específicas de la actividad en el .bib de la asignatura.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "No inventar referencias; usar solo obras realmente consultables.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a Semana 7 y no a Actividad 1."
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
    "Confirmar rúbrica de evaluación específica para ajustar profundidad argumentativa.",
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
      "Transformar la planeación semanal en productos académicos con fundamento jurídico, evidencia y cierre argumentativo aplicable."
    ],
    "style_markers": [
      "Encuadre inicial breve y contextualizado.",
      "Desarrollo por bloques conceptuales y normativos.",
      "Postura personal explícita y defendida.",
      "Cierre con utilidad profesional jurídica.",
      "Marcado explícito de supuestos."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> norma/doctrina -> análisis propio -> conclusión jurídica.",
      "Afirmación jurídica -> evidencia verificable -> interpretación -> postura.",
      "Coherencia vertical entre objetivo, desarrollo y cierre."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofía del Derecho",
        "Fundamentos del derecho",
        "Justicia",
        "Derecho y moral",
        "Hermenéutica e interpretación jurídica",
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
          "source": "Filosofía del Derecho",
          "target": "Fundamentos del derecho",
          "kind": "develops",
          "justification": "La asignatura desarrolla bases conceptuales del fenómeno jurídico."
        },
        {
          "source": "Filosofía del Derecho",
          "target": "Justicia",
          "kind": "develops",
          "justification": "La reflexión filosófica orienta criterios de justicia aplicables al análisis jurídico."
        },
        {
          "source": "Hermenéutica e interpretación jurídica",
          "target": "Argumentación jurídica",
          "kind": "supports",
          "justification": "La interpretación sustenta la construcción de argumentos jurídicos válidos."
        },
        {
          "source": "Constitución Política de los Estados Unidos Mexicanos",
          "target": "Análisis propio y postura académica",
          "kind": "supports",
          "justification": "El marco constitucional da base normativa verificable a la postura del estudiante."
        },
        {
          "source": "Ley General de Víctimas",
          "target": "Conclusión transferible a la práctica jurídica",
          "kind": "supports",
          "justification": "Aporta criterios de aplicación práctica en contextos de protección de derechos."
        }
      ],
      "evidence": [
        "README.md de asignatura: identidad, ubicación curricular y pauta editorial.",
        "programa-analitico-filosofia-del-derecho.md: propósito y ejes de trabajo.",
        "reporte-filosofia-del-derecho-Actividad-1.tex: fuente TEX reconstruible.",
        "filosofia-del-derecho.bib y claves citadas en tex_primary.",
        "filosofia-del-derecho-clean.bib: evidencia temática de Semana 7 [supuesto de no correspondencia directa con Actividad 1]."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: deduplicación ortográfica y semántica sin pérdida de reglas útiles.",
      "Ciclo 2: preservación íntegra del ADN editorial y del patrón argumentativo canónico.",
      "Ciclo 2: refuerzo de control de calidad JSON y trazabilidad bibliográfica.",
      "Ciclo 2: se mantiene artefacto principal 'reporte-filosofia-del-derecho-Actividad-1' como referencia operativa."
    ]
  }
}