{
  "summary": [
    "Memoria local canonizada y deduplicada sin pérdida de reglas útiles.",
    "Se mantiene identidad UnADM para Actividad 1 de Filosofía del Derecho.",
    "Se preserva normalización JSON obligatoria antes de cualquier propagación.",
    "Se consolidan ejes editoriales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se conserva trazabilidad de fuentes provisionales y supuestos explícitos.",
    "Se preserva TEX reconstruible y continuidad del artefacto reporte-filosofia-del-derecho-Actividad-1."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto cualquier dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Citar malla-curricular-derecho-unadm.pdf como fuente de ubicación curricular."
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
    "Verificar que el producto corresponda a la consigna de Actividad 1.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir que fuentes de semanas posteriores correspondan a Actividad 1."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna de Actividad 1."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Verificar nombres de archivo en README y programa analítico antes de referenciarlos.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en nombres de archivo.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar fuentes específicas de la actividad en el .bib de la asignatura.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib está orientado a Semana 7 y no define por sí solo Actividad 1."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Aplicar normalización manual si se detecta salida no estructurada en nodos vecinos.",
    "Propagar solo reglas generales cuando falte consigna textual."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual completa de Actividad 1; confirmar producto exacto.",
    "Confirmar si el formato principal es reporte, presentación u otro.",
    "Confirmar rúbrica de evaluación específica.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar nombre canónico final del archivo .bib.",
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
      "Evidencia verificable y citas trazables.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica aplicable a la práctica."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos y verificables.",
      "Sostener claridad argumentativa con fundamento jurídico.",
      "Garantizar transferencia profesional del aprendizaje."
    ],
    "style_markers": [
      "Supuestos explícitos cuando falte dato en consigna.",
      "Trazabilidad de fuentes y claves de cita.",
      "Estructura estable por secciones funcionales.",
      "Cierre con criterio jurídico propio."
    ],
    "argumentative_patterns": [
      "Del problema al concepto y del concepto al criterio.",
      "Del marco normativo a la interpretación aplicada.",
      "De la evidencia a la postura personal justificada.",
      "De la postura a una conclusión transferible."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofía del Derecho",
        "Objeto de estudio del derecho",
        "Principios y normas jurídicas",
        "Justicia",
        "Fundamentos del derecho",
        "Derecho y moral",
        "Hermenéutica e interpretación jurídica",
        "Argumentación jurídica",
        "Constitución y derechos",
        "Víctimas y acceso a la justicia"
      ],
      "citations": [
        "finnis_estudios_2017",
        "lovon_manual_2020",
        "ruiz_rodriguez_filosofia_derecho_2009",
        "rojas_gonzalez_filosofia_derecho_2018",
        "noauthor_constitucion_nodate",
        "generales_ley_2021",
        "de_victimas_ley_2013",
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
          "justification": "La asignatura desarrolla bases conceptuales y críticas del fenómeno jurídico."
        },
        {
          "source": "Hermenéutica e interpretación jurídica",
          "target": "Argumentación jurídica",
          "kind": "supports",
          "justification": "La interpretación sustenta la construcción de razones jurídicas."
        },
        {
          "source": "Constitución y derechos",
          "target": "Víctimas y acceso a la justicia",
          "kind": "supports",
          "justification": "El marco constitucional y legal orienta protección y reparación."
        },
        {
          "source": "Derecho y moral",
          "target": "Justicia",
          "kind": "contrasts",
          "justification": "Permite discutir tensiones entre validez normativa y valoración ética."
        }
      ],
      "evidence": [
        "README.md: identidad institucional y ubicación curricular.",
        "programa-analitico-filosofia-del-derecho.md: propósito y ejes de trabajo.",
        "reporte-filosofia-del-derecho-Actividad-1.tex: estructura argumentativa reconstruible.",
        "filosofia-del-derecho.bib y claves citadas en tex_primary: trazabilidad bibliográfica.",
        "filosofia-del-derecho-clean.bib: evidencia de foco en Semana 7 (marcado como supuesto para no extrapolar)."
      ]
    },
    "reinforcement_log": [
      "Ciclo 43: deduplicación semántica aplicada sin recorte de reglas válidas.",
      "Ciclo 43: se preserva obligación de JSON parseable como puerta de calidad.",
      "Ciclo 43: se refuerza separación entre bibliografía base y bibliografía por actividad.",
      "Ciclo 43: se mantiene supuesto explícito sobre falta de consigna textual completa.",
      "Ciclo 43: se conserva compatibilidad con TEX reconstruible y claves BibTeX estables."
    ]
  }
}