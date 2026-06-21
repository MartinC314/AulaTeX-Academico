{
  "summary": [
    "Memoria de Actividad 1 consolidada y deduplicada sin pérdida.",
    "Se preserva identidad UnADM y ubicación curricular verificable.",
    "Se mantiene normalización JSON obligatoria antes de propagar.",
    "Se refuerzan ejes editoriales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se preserva TEX reconstruible y trazabilidad de fuentes locales."
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
    "Transformar la planeación en reporte, presentación o producto visual según consigna.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Definir objetivo puntual de la actividad antes del desarrollo.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Evitar entregas solo descriptivas.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
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
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
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
      "Problema jurídico o social.",
      "Conceptos y marco normativo o doctrinal.",
      "Evidencia verificable.",
      "Análisis propio con postura.",
      "Conclusión jurídica aplicable."
    ],
    "reason_for_being": [
      "Transformar planeación semanal en productos académicos sólidos.",
      "Asegurar fundamento jurídico, claridad argumentativa y transferencia profesional.",
      "Mantener trazabilidad entre consigna, desarrollo, evidencia y cierre."
    ],
    "style_markers": [
      "Apertura con encuadre del problema.",
      "Secciones explícitas y jerarquía lógica.",
      "Citas verificables y consistentes con .bib.",
      "Declaración explícita de supuestos.",
      "Cierre con criterio jurídico propio."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> norma/doctrina -> análisis -> conclusión.",
      "Pregunta guía -> desarrollo probado -> respuesta final.",
      "Descripción mínima y valoración crítica máxima."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofía del Derecho",
        "Problema jurídico o social",
        "Marco normativo/doctrinal",
        "Argumentación jurídica",
        "Hermenéutica e interpretación jurídica",
        "Derechos de víctimas",
        "Derecho y moral",
        "Conclusión transferible a la práctica"
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
          "target": "Marco normativo/doctrinal",
          "kind": "depends_on",
          "justification": "El análisis exige ubicar normas y doctrina aplicables."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Análisis propio",
          "kind": "supports",
          "justification": "La postura se legitima con base normativa y teórica."
        },
        {
          "source": "Hermenéutica e interpretación jurídica",
          "target": "Argumentación jurídica",
          "kind": "develops",
          "justification": "Mejora la justificación de premisas y conclusiones."
        },
        {
          "source": "Constitución y leyes de víctimas",
          "target": "Conclusión transferible a la práctica",
          "kind": "supports",
          "justification": "Permiten cerrar con aplicabilidad profesional."
        }
      ],
      "evidence": [
        "README.md: identidad, ubicación curricular y pauta editorial.",
        "programa-analitico-filosofia-del-derecho.md: propósito y ejes de trabajo.",
        "reporte-filosofia-del-derecho-Actividad-1.tex: estructura y claves citadas.",
        "filosofia-del-derecho-clean.bib: evidencia de foco en Semana 7 (supuesto para no mezclar Actividad 1)."
      ]
    },
    "reinforcement_log": [
      "Ciclo 4: deduplicación semántica aplicada sin recorte de reglas útiles.",
      "Ciclo 4: se preservó compatibilidad con TEX reconstruible y claves BibTeX existentes.",
      "Ciclo 4: se reforzó trazabilidad entre identidad institucional, estructura y control de calidad.",
      "Ciclo 4: se mantuvieron supuestos explícitos por falta de consigna textual completa."
    ]
  }
}