{
  "summary": [
    "Memoria local canonizada con compresión lossless por unión y deduplicación.",
    "Se preserva identidad UnADM y ubicación curricular verificable: semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Se mantiene normalización estructurada obligatoria antes de toda propagación.",
    "Se sostienen ejes editoriales: problema, conceptos, evidencia, análisis propio y conclusión jurídica transferible.",
    "Se conserva TEX reconstruible del nodo con fuente primaria de Actividad 1."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Citar malla-curricular-derecho-unadm.pdf como fuente de ubicación curricular.",
    "Marcar como supuesto cualquier dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local."
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
    "Incluir postura argumentada del estudiante, no solo resumen descriptivo.",
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
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "No inventar referencias; usar solo obras realmente consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "No asumir que filosofia-del-derecho-clean.bib corresponde a Actividad 1.",
    "Supuesto: filosofia-del-derecho-clean.bib está orientado a Semana 7 (interpretación jurídica)."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Propagar solo reglas generales cuando falte consigna textual.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Aplicar normalización manual si se detecta salida no estructurada en nodos vecinos."
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
      "Transformar la planeación semanal en productos académicos con fundamento jurídico, evidencia y cierre argumentativo.",
      "Asegurar transferencia profesional del análisis al contexto jurídico real."
    ],
    "style_markers": [
      "Inicio con encuadre del problema.",
      "Desarrollo por secciones funcionales.",
      "Postura personal explícita y sustentada.",
      "Cierre con conclusión jurídica aplicable.",
      "Marcado explícito de supuestos."
    ],
    "argumentative_patterns": [
      "Problema inicial -> conceptos clave -> marco normativo/doctrinal -> análisis propio -> conclusión.",
      "Cada afirmación relevante se acompaña con evidencia verificable.",
      "La conclusión responde a la pregunta guía y no introduce tesis nuevas sin soporte."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofía del Derecho",
        "Objeto de estudio",
        "Principios y normas jurídicas",
        "Justicia",
        "Fundamentos del derecho",
        "Análisis crítico del fenómeno jurídico",
        "Derecho y moral",
        "Hermenéutica e interpretación jurídica"
      ],
      "citations": [
        "finnis_estudios_2017",
        "lovon_manual_2020",
        "ruiz_rodriguez_filosofia_derecho_2009",
        "rojas_gonzalez_filosofia_derecho_2018",
        "noauthor_constitucion_nodate",
        "generales_ley_2021",
        "de_victimas_ley_2013",
        "franzoni_acevedo_ley_2017",
        "gandara_ley_2015",
        "hernandezManriquezHermeneutica2019",
        "scjnMemoriaArgumentacion2008",
        "scjnViolenciaFisica2022",
        "scjnIncapacidadResistencia2019"
      ],
      "relations": [
        {
          "source": "Filosofía del Derecho",
          "target": "Análisis crítico del fenómeno jurídico",
          "kind": "develops",
          "justification": "El programa analítico define función crítica y fundamento jurídico."
        },
        {
          "source": "Principios y normas jurídicas",
          "target": "Justicia",
          "kind": "supports",
          "justification": "La estructura conceptual del curso vincula norma con valoración de justicia."
        },
        {
          "source": "Hermenéutica e interpretación jurídica",
          "target": "Argumentación jurídica",
          "kind": "depends_on",
          "justification": "Las fuentes SCJN y UNAM aportan base metodológica interpretativa."
        },
        {
          "source": "Constitución y leyes generales",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión debe anclarse en marco normativo vigente."
        }
      ],
      "evidence": [
        "README.md: pauta editorial y ubicación curricular verificable.",
        "programa-analitico-filosofia-del-derecho.md: propósito y ejes de trabajo.",
        "reporte-filosofia-del-derecho-Actividad-1.tex: fuente TEX reconstruible con 79 bloques.",
        "filosofia-del-derecho-clean.bib: evidencia de que corresponde a Semana 7, no necesariamente a Actividad 1."
      ]
    },
    "reinforcement_log": [
      "Ciclo 12: deduplicación semántica aplicada sin pérdida de reglas útiles.",
      "Ciclo 12: se preserva ADN editorial completo del mismo nodo.",
      "Ciclo 12: se refuerza control de supuestos y verificación local de fuentes.",
      "Ciclo 12: se mantiene compatibilidad con TEX primario y claves BibTeX existentes."
    ]
  }
}