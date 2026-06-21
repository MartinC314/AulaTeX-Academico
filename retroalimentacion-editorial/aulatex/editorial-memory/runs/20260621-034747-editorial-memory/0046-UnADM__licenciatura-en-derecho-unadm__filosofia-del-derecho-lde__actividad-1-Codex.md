{
  "summary": [
    "Memoria local canonizada sin pérdidas por unión y deduplicación.",
    "Se preserva identidad UnADM para Actividad 1 de Filosofía del Derecho.",
    "Se mantienen ejes editoriales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se conserva regla crítica: no propagar salidas no estructuradas sin normalización JSON.",
    "Se refuerza trazabilidad a README y programa analítico como fuentes locales verificables.",
    "Se mantiene TEX reconstruible y continuidad del artefacto reporte-filosofia-del-derecho-Actividad-1."
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
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar fuentes específicas de la actividad en el .bib de la asignatura.",
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "No asumir que filosofia-del-derecho-clean.bib corresponde a Actividad 1.",
    "Supuesto: filosofia-del-derecho-clean.bib está orientado a Semana 7 (interpretación jurídica)."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Aplicar normalización manual si se detecta salida no estructurada en nodos vecinos.",
    "Evitar regresiones respecto de reglas útiles previas.",
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
      "Marco conceptual y normativo pertinente.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica aplicable a práctica profesional.",
      "Trazabilidad entre consigna, desarrollo y evidencia."
    ],
    "reason_for_being": [
      "Convertir la planeación semanal en productos académicos sólidos.",
      "Asegurar claridad, fundamento jurídico, evidencia y transferencia profesional.",
      "Preservar memoria editorial estable y reutilizable sin pérdida."
    ],
    "style_markers": [
      "Enunciados breves, verificables y accionables.",
      "Marcado explícito de supuestos cuando falte evidencia local.",
      "Prioridad a fuentes locales del nodo antes de extrapolar.",
      "Consistencia terminológica entre secciones, citas y cierre."
    ],
    "argumentative_patterns": [
      "Problematizar primero, definir objetivo y alcance después.",
      "Desarrollar conceptos y marco normativo con citas verificables.",
      "Contrastar doctrina/norma con caso o evidencia.",
      "Cerrar con toma de postura y conclusión jurídica transferible."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofía del Derecho",
        "Problema jurídico o social",
        "Conceptos jurídicos fundamentales",
        "Marco normativo",
        "Análisis propio",
        "Conclusión jurídica",
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
        "scjnMemoriaArgumentacion2008"
      ],
      "relations": [
        {
          "source": "Problema jurídico o social",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis inicia desde un problema delimitado."
        },
        {
          "source": "Conceptos jurídicos fundamentales",
          "target": "Marco normativo",
          "kind": "supports",
          "justification": "Los conceptos ordenan la lectura de normas y doctrina."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusión jurídica",
          "kind": "supports",
          "justification": "La conclusión debe sustentarse en derecho vigente y fuentes."
        },
        {
          "source": "Hermenéutica e interpretación jurídica",
          "target": "Argumentación jurídica",
          "kind": "develops",
          "justification": "La interpretación fortalece la justificación de la postura."
        }
      ],
      "evidence": [
        "README.md: identidad institucional, ubicación curricular y pauta editorial.",
        "programa-analitico-filosofia-del-derecho.md: propósito y ejes de trabajo.",
        "reporte-filosofia-del-derecho-Actividad-1.tex: fuente reconstruible y claves citadas.",
        "filosofia-del-derecho-clean.bib: evidencia de enfoque Semana 7 (supuesto explícito para A1)."
      ]
    },
    "reinforcement_log": [
      "Ciclo 46: deduplicación semántica aplicada sin eliminar reglas útiles.",
      "Ciclo 46: normalización de acentos y variantes duplicadas.",
      "Ciclo 46: conservación de reglas de bloqueo JSON y control de supuestos.",
      "Ciclo 46: reforzada conexión entre ejes editoriales y patrón argumentativo."
    ]
  }
}