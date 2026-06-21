{
  "summary": [
    "Memoria local consolidada de Actividad 1 en Filosofía del Derecho con identidad UnADM.",
    "Se mantiene normalización estructurada obligatoria antes de cualquier propagación.",
    "Se preservan ejes editoriales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se confirma compresión lossless por unión y deduplicación sin recorte semántico.",
    "Se preserva TEX reconstruible y trazabilidad de fuentes locales."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Citar malla-curricular-derecho-unadm.pdf como base de ubicación curricular.",
    "Marcar como supuesto cualquier dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
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
    "Compilar sin errores críticos y sin referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Verificar nombres de archivo del README antes de referenciarlos.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar fuentes específicas de la actividad en el .bib de la asignatura.",
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "No asumir que filosofia-del-derecho-clean.bib corresponde a Actividad 1.",
    "Supuesto: filosofia-del-derecho-clean.bib está orientado a Semana 7 (interpretación jurídica)."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Propagar solo reglas generales cuando falte consigna textual.",
    "Aplicar normalización manual en nodos con salidas no estructuradas de ciclos previos."
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
      "Transformar la planeación semanal en productos académicos con fundamento jurídico, evidencia y cierre argumentativo transferible.",
      "Convertir lineamientos institucionales en entregables verificables, citables y técnicamente compilables."
    ],
    "style_markers": [
      "Abrir con problema y objetivo explícito.",
      "Distinguir exposición conceptual de toma de postura.",
      "Sostener cada afirmación relevante con evidencia trazable.",
      "Etiquetar supuestos cuando falte dato en consigna.",
      "Cerrar con conclusión jurídica aplicable."
    ],
    "argumentative_patterns": [
      "Problema inicial -> marco conceptual/normativo -> análisis propio -> conclusión jurídica.",
      "Contrastar doctrina y norma antes de fijar postura.",
      "Evitar resumen lineal sin inferencia jurídica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofía del Derecho",
        "Objeto de estudio del derecho",
        "Justicia",
        "Fundamentos del derecho",
        "Análisis crítico del fenómeno jurídico",
        "Constitución Política de los Estados Unidos Mexicanos",
        "Ley General de Víctimas",
        "Derecho y moral",
        "Hermenéutica e interpretación jurídica"
      ],
      "citations": [
        "ruiz_rodriguez_filosofia_derecho_2009",
        "rojas_gonzalez_filosofia_derecho_2018",
        "noauthor_constitucion_nodate",
        "de_victimas_ley_2013",
        "finnis_estudios_2017",
        "lovon_manual_2020",
        "hernandezManriquezHermeneutica2019",
        "scjnMemoriaArgumentacion2008"
      ],
      "relations": [
        {
          "source": "Filosofía del Derecho",
          "target": "Análisis crítico del fenómeno jurídico",
          "kind": "develops",
          "justification": "El programa analítico define función crítica y fundamento jurídico."
        },
        {
          "source": "Constitución Política de los Estados Unidos Mexicanos",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "Aporta marco normativo para sustento de postura."
        },
        {
          "source": "Ley General de Víctimas",
          "target": "Análisis propio y postura académica",
          "kind": "supports",
          "justification": "Permite conectar teoría con protección de derechos en casos concretos."
        },
        {
          "source": "Derecho y moral",
          "target": "Justicia",
          "kind": "contrasts",
          "justification": "La tensión conceptual fortalece argumentación filosófico-jurídica."
        },
        {
          "source": "Hermenéutica e interpretación jurídica",
          "target": "Análisis crítico del fenómeno jurídico",
          "kind": "depends_on",
          "justification": "La interpretación condiciona la lectura normativa y doctrinal."
        }
      ],
      "evidence": [
        "README.md de la asignatura: identidad, ubicación curricular y pauta editorial.",
        "programa-analitico-filosofia-del-derecho.md: propósito, ejes de trabajo y política bibliográfica.",
        "reporte-filosofia-del-derecho-Actividad-1.tex: estructura y claves de cita usadas.",
        "filosofia-del-derecho-clean.bib: marcado local de uso para Semana 7 (no asumir para Actividad 1)."
      ]
    },
    "reinforcement_log": [
      "Ciclo 9: deduplicación ortográfica y semántica aplicada sin pérdida de reglas útiles.",
      "Ciclo 9: se preserva ADN institucional, curricular y argumentativo completo del nodo.",
      "Ciclo 9: se refuerza regla de supuestos explícitos ante ausencia de consigna textual.",
      "Ciclo 9: se mantiene trazabilidad TEX/.bib y control de tokens Slug sin expandir."
    ]
  }
}