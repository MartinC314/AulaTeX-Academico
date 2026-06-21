{
  "summary": [
    "Memoria local canonizada por unión y deduplicación sin pérdida.",
    "Se preserva identidad UnADM y contexto curricular verificado en README.",
    "Se mantiene normalización estructurada obligatoria antes de propagar.",
    "Se consolidan ejes editoriales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se conserva TEX reconstruible y trazabilidad de fuentes locales.",
    "Se mantiene estado provisional de fuentes heredadas no verificadas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Citar malla-curricular-derecho-unadm.pdf como fuente de ubicación curricular.",
    "Marcar como supuesto cualquier dato no visible en la consigna de actividad.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Fuente provisional: GPT-Pro desde Actividad 1.",
    "Tratar la fuente heredada Codex como provisional hasta verificarla."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeación semanal.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Definir objetivo puntual de la actividad antes del desarrollo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Verificar que el producto corresponda a la consigna de Actividad 1.",
    "No asumir que fuentes de semanas posteriores correspondan a Actividad 1."
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
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "No asumir que filosofia-del-derecho-clean.bib corresponde a Actividad 1.",
    "Supuesto: filosofia-del-derecho-clean.bib está orientado a Semana 7 (interpretación jurídica)."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar solo reglas generales cuando falte consigna textual.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Aplicar normalización manual si se detecta salida no estructurada en nodos vecinos.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Ciclo 1 y ciclo 2 requieren normalización manual si se reutilizan."
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
      "Conceptos, normas, doctrina y datos pertinentes.",
      "Evidencia verificable y trazable.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica aplicable a la práctica."
    ],
    "reason_for_being": [
      "Convertir la planeación semanal en productos académicos sólidos.",
      "Asegurar claridad argumentativa y fundamento jurídico.",
      "Mantener continuidad editorial entre actividad, asignatura y programa."
    ],
    "style_markers": [
      "Apertura breve con encuadre del problema.",
      "Desarrollo por secciones funcionales.",
      "Uso explícito de supuestos cuando falte dato.",
      "Cierre con conclusión jurídica transferible."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> marco normativo/doctrinal -> análisis propio -> conclusión.",
      "Afirmación -> evidencia/cita -> interpretación -> postura del estudiante.",
      "Consigna -> producto -> verificación de correspondencia final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofía del Derecho",
        "Problema jurídico o social",
        "Marco normativo y doctrinal",
        "Análisis crítico del fenómeno jurídico",
        "Justicia",
        "Derecho y moral",
        "Hermenéutica e interpretación jurídica",
        "Argumentación jurídica",
        "Conclusión transferible a la práctica jurídica"
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
          "kind": "supports",
          "justification": "El problema activa el desarrollo argumentativo de la actividad."
        },
        {
          "source": "Marco normativo y doctrinal",
          "target": "Análisis crítico del fenómeno jurídico",
          "kind": "depends_on",
          "justification": "El análisis exige fundamento en normas y doctrina."
        },
        {
          "source": "Hermenéutica e interpretación jurídica",
          "target": "Argumentación jurídica",
          "kind": "develops",
          "justification": "La interpretación robustece la justificación de la postura."
        },
        {
          "source": "Análisis crítico del fenómeno jurídico",
          "target": "Conclusión transferible a la práctica jurídica",
          "kind": "develops",
          "justification": "La conclusión deriva del análisis propio sustentado."
        }
      ],
      "evidence": [
        "README.md: identidad UnADM, ubicación curricular y pauta editorial.",
        "programa-analitico-filosofia-del-derecho.md: propósito y ejes de trabajo.",
        "reporte-filosofia-del-derecho-Actividad-1.tex: estructura y citas activas.",
        "filosofia-del-derecho-clean.bib: marcado local de Semana 7, no canónico para Actividad 1."
      ]
    },
    "reinforcement_log": [
      "Ciclo 9: deduplicación total aplicada sin recorte semántico.",
      "Ciclo 9: se preserva reconstruibilidad TEX y continuidad del nodo.",
      "Ciclo 9: se refuerza regla de supuestos explícitos ante consigna ausente.",
      "Ciclo 9: se mantiene separación entre bibliografía base y bibliografía por actividad."
    ]
  }
}