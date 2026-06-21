{
  "summary": [
    "Memoria local canonizada sin pérdida por unión y deduplicación.",
    "Se preserva identidad UnADM y contexto curricular verificable.",
    "Se mantiene normalización JSON obligatoria antes de propagar.",
    "Se conservan ejes editoriales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se refuerza que la Actividad 1 usa artefacto base tipo reporte.",
    "Se mantiene trazabilidad a README, programa analítico y .tex reconstruible."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto cualquier dato no visible en la consigna de la actividad.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Citar malla-curricular-derecho-unadm.pdf como fuente de ubicación curricular."
  ],
  "structure_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema jurídico o social.",
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
    "Aplicar normalización manual si se detecta salida no estructurada en nodos vecinos."
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
      "Transformar la planeación semanal en productos académicos con fundamento jurídico y transferencia profesional.",
      "Estructurar entregas con evidencia verificable y criterio propio.",
      "Sostener consistencia entre consigna, desarrollo y cierre jurídico."
    ],
    "style_markers": [
      "Apertura breve con problema jurídico.",
      "Secciones explícitas y progresión lógica.",
      "Uso de supuestos marcados cuando falte evidencia local.",
      "Cierre con implicación práctica para el ejercicio profesional."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo.",
      "Definir conceptos y marco normativo/doctrinal.",
      "Contrastar fuentes y desarrollar análisis propio.",
      "Sostener postura personal con citas verificables.",
      "Concluir con criterio jurídico aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofía del Derecho",
        "Problema jurídico-social",
        "Marco normativo y doctrinal",
        "Argumentación jurídica",
        "Hermenéutica e interpretación jurídica",
        "Derecho y moral",
        "Conclusión jurídica transferible"
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
          "source": "Problema jurídico-social",
          "target": "Marco normativo y doctrinal",
          "kind": "depends_on",
          "justification": "El análisis parte del problema y requiere sustento jurídico verificable."
        },
        {
          "source": "Marco normativo y doctrinal",
          "target": "Análisis propio",
          "kind": "supports",
          "justification": "La postura del estudiante debe apoyarse en normas y doctrina citadas."
        },
        {
          "source": "Hermenéutica e interpretación jurídica",
          "target": "Argumentación jurídica",
          "kind": "develops",
          "justification": "La interpretación fortalece la justificación de conclusiones jurídicas."
        },
        {
          "source": "Derecho y moral",
          "target": "Filosofía del Derecho",
          "kind": "develops",
          "justification": "Es eje conceptual recurrente en la construcción del marco teórico."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "El cierre profesional deriva de la argumentación desarrollada."
        }
      ],
      "evidence": [
        "README.md: identidad UnADM y ubicación curricular.",
        "programa-analitico-filosofia-del-derecho.md: propósito y ejes de trabajo.",
        "reporte-filosofia-del-derecho-Actividad-1.tex: fuente reconstruible con 79 bloques.",
        "filosofia-del-derecho-clean.bib: evidencia de Semana 7, no canónica para Actividad 1."
      ]
    },
    "reinforcement_log": [
      "Ciclo 20: deduplicación semántica aplicada sin pérdida de reglas útiles.",
      "Ciclo 20: se preserva ADN editorial completo del mismo nodo.",
      "Ciclo 20: se refuerza separación entre bibliografía base y específica de actividad.",
      "Ciclo 20: se mantiene bloqueo de propagación ante JSON inválido."
    ]
  }
}