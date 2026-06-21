{
  "summary": [
    "Memoria local canonizada por unión y deduplicación sin pérdida.",
    "Se preserva identidad UnADM y ubicación curricular verificable.",
    "Se mantiene normalización estructurada obligatoria antes de propagación.",
    "Se refuerzan ejes editoriales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se conserva TEX reconstruible y trazabilidad de fuentes locales.",
    "Se mantiene control de fuentes provisionales con marca de supuesto."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Citar malla-curricular-derecho-unadm.pdf como fuente de ubicación curricular.",
    "Marcar como supuesto cualquier dato no visible en la consigna de actividad.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Registrar fuente provisional GPT-Pro y Codex solo como antecedentes no canónicos."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Adaptar salida a reporte, presentación o producto visual solo según consigna."
  ],
  "activity_rules": [
    "Definir objetivo puntual de la Actividad 1 antes del desarrollo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante y evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Validar que el producto final corresponda exactamente a la consigna de Actividad 1.",
    "No asumir fuentes de semanas posteriores como obligatorias para Actividad 1."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar toda respuesta no estructurada antes de reutilizarla.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Validar correspondencia entre tipo de producto y consigna vigente."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Verificar nombres de archivos desde README antes de referenciarlos.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar fuentes específicas de la actividad en el .bib canónico de la asignatura.",
    "No inventar referencias; usar solo obras realmente consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "No asumir que filosofia-del-derecho-clean.bib corresponda a Actividad 1.",
    "Supuesto: filosofia-del-derecho-clean.bib está orientado a Semana 7 (interpretación jurídica)."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Aplicar normalización manual en nodos con salidas no estructuradas.",
    "Propagar solo reglas generales cuando falte consigna textual."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 1; confirmar producto exacto solicitado.",
    "Confirmar si el formato principal es reporte, presentación u otro.",
    "Confirmar rúbrica de evaluación específica para calibrar profundidad argumentativa.",
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
      "Transformar la planeación semanal en productos académicos con fundamento jurídico y evidencia.",
      "Garantizar trazabilidad editorial entre consigna, desarrollo y cierre jurídico.",
      "Conservar memoria técnica y argumentativa reutilizable sin pérdida."
    ],
    "style_markers": [
      "Declarar supuestos cuando falten datos de consigna.",
      "Sostener afirmaciones con cita explícita.",
      "Usar secciones funcionales y cierre aplicable a práctica profesional.",
      "Evitar ambigüedad en formato y alcance del entregable."
    ],
    "argumentative_patterns": [
      "Problematizar contexto jurídico-social al inicio.",
      "Definir objetivo y marco conceptual antes del análisis.",
      "Conectar doctrina y norma con evidencia verificable.",
      "Formular postura propia sustentada.",
      "Cerrar con conclusión jurídica operable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofía del Derecho",
        "Problema jurídico-social",
        "Marco normativo y doctrinal",
        "Análisis argumentativo",
        "Conclusión jurídica transferible",
        "Hermenéutica e interpretación jurídica",
        "Derecho y moral",
        "Justicia",
        "Fundamentos del derecho"
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
          "target": "Análisis argumentativo",
          "kind": "supports",
          "justification": "El encuadre inicial define pertinencia y dirección del desarrollo."
        },
        {
          "source": "Marco normativo y doctrinal",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión exige respaldo normativo y conceptual verificable."
        },
        {
          "source": "Hermenéutica e interpretación jurídica",
          "target": "Análisis argumentativo",
          "kind": "develops",
          "justification": "Fortalece la justificación de la postura y la lectura del caso."
        },
        {
          "source": "Derecho y moral",
          "target": "Justicia",
          "kind": "contrasts",
          "justification": "Permite distinguir validez formal y evaluación axiológica."
        },
        {
          "source": "Producto solicitado por planeación",
          "target": "Estructura del documento",
          "kind": "depends_on",
          "justification": "El tipo de entrega condiciona forma y extensión argumentativa."
        }
      ],
      "evidence": [
        "README.md: identidad UnADM, ubicación curricular y pauta editorial.",
        "programa-analitico-filosofia-del-derecho.md: propósito y ejes de trabajo.",
        "reporte-filosofia-del-derecho-Actividad-1.tex: fuente TEX reconstruible con 79 bloques.",
        "tex_primary.all_cited_keys: conjunto verificable de claves citadas."
      ]
    },
    "reinforcement_log": [
      "Ciclo 75: deduplicación semántica aplicada sin eliminar reglas útiles.",
      "Ciclo 75: se mantiene control estricto de JSON parseable para propagación.",
      "Ciclo 75: se refuerza separación entre bibliografía base y específica de actividad.",
      "Ciclo 75: se preserva supuesto sobre .bib canónico y token Slug sin fijarlo como hecho.",
      "Ciclo 75: se conserva ADN argumentativo centrado en problema-evidencia-postura-conclusión."
    ]
  }
}