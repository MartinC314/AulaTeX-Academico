{
  "summary": [
    "Memoria local canonizada con preservación total y deduplicación lossless.",
    "Se mantiene identidad UnADM y ubicación curricular verificable de Filosofía del Derecho.",
    "Se sostienen ejes editoriales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se conserva regla de normalización estructurada previa a cualquier propagación.",
    "Se preserva TEX reconstruible del nodo y consistencia con artefacto de Actividad 1."
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
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
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
    "Aplicar normalización manual si se detecta salida no estructurada en nodos vecinos.",
    "Ciclos previos 1 y 2 requieren normalización manual si se reutilizan."
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
      "Transformar la planeación semanal en productos académicos con fundamento jurídico, evidencia y cierre argumentativo transferible.",
      "Conservar coherencia entre consigna, estructura y evidencia verificable."
    ],
    "style_markers": [
      "Apertura con problema jurídico concreto.",
      "Desarrollo por capas: concepto, norma/doctrina, análisis propio.",
      "Uso explícito de citas trazables en texto y .bib.",
      "Cierre con conclusión jurídica aplicable."
    ],
    "argumentative_patterns": [
      "Problematizar antes de definir.",
      "Definir conceptos antes de evaluar posturas.",
      "Conectar norma y doctrina con el caso o eje de la actividad.",
      "Sostener tesis propia con evidencia verificable.",
      "Cerrar con implicación profesional concreta."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofía del Derecho",
        "Objeto de estudio",
        "Principios y normas jurídicas",
        "Justicia",
        "Fundamentos del derecho",
        "Análisis crítico del fenómeno jurídico",
        "Hermenéutica e interpretación jurídica",
        "Argumentación jurídica",
        "Derecho y moral"
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
        "scjnMemoriaArgumentacion2008"
      ],
      "relations": [
        {
          "source": "Filosofía del Derecho",
          "target": "Análisis crítico del fenómeno jurídico",
          "kind": "develops",
          "justification": "El programa analítico define enfoque crítico y fundamento conceptual."
        },
        {
          "source": "Principios y normas jurídicas",
          "target": "Justicia",
          "kind": "depends_on",
          "justification": "La valoración de justicia requiere interpretación de principios y normas."
        },
        {
          "source": "Hermenéutica e interpretación jurídica",
          "target": "Argumentación jurídica",
          "kind": "supports",
          "justification": "La interpretación provee criterios para justificar tesis jurídicas."
        },
        {
          "source": "Derecho y moral",
          "target": "Fundamentos del derecho",
          "kind": "contrasts",
          "justification": "El debate iuspositivismo/iusnaturalismo estructura el análisis filosófico."
        }
      ],
      "evidence": [
        "README.md de la asignatura: identidad, ubicación curricular y pauta editorial.",
        "programa-analitico-filosofia-del-derecho.md: propósito y ejes de trabajo.",
        "reporte-filosofia-del-derecho-Actividad-1.tex: estructura y claves citadas reconstruibles.",
        "filosofia-del-derecho-clean.bib: evidencia de archivo orientado a Semana 7 [supuesto ya marcado]."
      ]
    },
    "reinforcement_log": [
      "Ciclo 56: deduplicación integral de reglas sin pérdida semántica.",
      "Ciclo 56: preservación explícita de normalización JSON como puerta de calidad crítica.",
      "Ciclo 56: refuerzo de vínculo entre estructura argumentativa y trazabilidad bibliográfica.",
      "Ciclo 56: mantenimiento de supuestos abiertos sin inventar fuentes nuevas."
    ]
  }
}