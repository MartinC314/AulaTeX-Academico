{
  "summary": [
    "Memoria local canonizada y deduplicada sin pérdida.",
    "Se preserva identidad institucional UnADM y contexto curricular verificable.",
    "Se mantiene normalización estructurada obligatoria antes de toda propagación.",
    "Se sostienen ejes editoriales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se conserva TEX reconstruible del nodo y trazabilidad de fuentes locales.",
    "Se refuerza manejo de supuestos ante consigna incompleta de Actividad 1."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Citar malla-curricular-derecho-unadm.pdf como fuente de ubicación curricular.",
    "Marcar como supuesto cualquier dato no visible en la consigna de actividad.",
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
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "No asumir que filosofia-del-derecho-clean.bib corresponde a Actividad 1.",
    "Supuesto: filosofia-del-derecho-clean.bib está orientado a Semana 7 (interpretación jurídica)."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Propagar solo reglas generales cuando falte consigna textual.",
    "Aplicar normalización manual si se detecta salida no estructurada en nodos vecinos.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Ciclos 1 y 2 requieren normalización manual si se reutilizan salidas heredadas."
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
      "Problema jurídico o social.",
      "Conceptos y marco normativo o doctrinal.",
      "Evidencia verificable.",
      "Análisis propio con postura.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos útiles y verificables.",
      "Asegurar claridad argumentativa con fundamento jurídico.",
      "Conectar aprendizaje con práctica profesional."
    ],
    "style_markers": [
      "Encuadre inicial breve y preciso.",
      "Secciones explícitas y orden lógico.",
      "Uso de supuestos marcados cuando falte dato.",
      "Citas trazables y consistentes con .bib.",
      "Cierre con criterio jurídico propio."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> análisis -> conclusión.",
      "Afirmación jurídica -> fuente verificable -> interpretación propia.",
      "Consigna -> producto -> validación de correspondencia."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofía del Derecho",
        "Objeto de estudio del derecho",
        "Principios y normas jurídicas",
        "Justicia",
        "Fundamentos del derecho",
        "Análisis crítico del fenómeno jurídico",
        "Hermenéutica e interpretación jurídica",
        "Argumentación jurídica",
        "Derecho y moral",
        "Constitución y derechos de víctimas"
      ],
      "citations": [
        "finnis_estudios_2017",
        "lovon_manual_2020",
        "ruiz_rodriguez_filosofia_derecho_2009",
        "rojas_gonzalez_filosofia_derecho_2018",
        "noauthor_constitucion_nodate",
        "de_victimas_ley_2013",
        "hernandezManriquezHermeneutica2019",
        "scjnMemoriaArgumentacion2008"
      ],
      "relations": [
        {
          "source": "Filosofía del Derecho",
          "target": "Análisis crítico del fenómeno jurídico",
          "kind": "develops",
          "justification": "El programa analítico orienta evaluación crítica del derecho."
        },
        {
          "source": "Hermenéutica e interpretación jurídica",
          "target": "Argumentación jurídica",
          "kind": "supports",
          "justification": "La interpretación sustenta justificación racional de conclusiones."
        },
        {
          "source": "Constitución y derechos de víctimas",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "El marco vigente da base normativa aplicable a casos."
        },
        {
          "source": "Derecho y moral",
          "target": "Filosofía del Derecho",
          "kind": "depends_on",
          "justification": "La asignatura trabaja la tensión y vínculo entre ambos planos."
        }
      ],
      "evidence": [
        "README.md de la asignatura para identidad, estructura y ubicación curricular.",
        "programa-analitico-filosofia-del-derecho.md para propósito y ejes de trabajo.",
        "reporte-filosofia-del-derecho-Actividad-1.tex como TEX reconstruible local.",
        "filosofia-del-derecho-clean.bib marcado localmente como Semana 7."
      ]
    },
    "reinforcement_log": [
      "Ciclo 8: deduplicación integral sin recorte semántico.",
      "Ciclo 8: se preservó trazabilidad de supuestos y fuentes provisionales.",
      "Ciclo 8: se reforzó patrón argumentativo canónico para Actividad 1.",
      "Ciclo 8: se mantuvo compatibilidad con compilación LaTeX y llaves BibTeX estables."
    ]
  }
}