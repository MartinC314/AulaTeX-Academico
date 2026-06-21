{
  "summary": [
    "Memoria local canonizada por unión y deduplicación sin pérdida.",
    "Se preserva identidad UnADM y ubicación curricular verificable.",
    "Se mantiene normalización estructurada obligatoria antes de propagar.",
    "Se consolidan ejes editoriales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se preserva TEX reconstruible de Actividad 1 y su traza bibliográfica.",
    "Se refuerza regla de marcar supuestos cuando la consigna no sea visible."
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
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "No inventar referencias; usar solo obras realmente consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "No asumir que filosofia-del-derecho-clean.bib corresponde a Actividad 1.",
    "Supuesto: filosofia-del-derecho-clean.bib está orientado a Semana 7 (interpretación jurídica)."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Propagar solo reglas generales cuando falte consigna textual.",
    "Aplicar normalización manual si se detecta salida no estructurada en nodos vecinos.",
    "Ciclos 1 y 2 requieren normalización manual si se reutilizan."
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
      "Transformar la planeación semanal en productos académicos con fundamento jurídico y transferencia profesional.",
      "Estandarizar calidad argumentativa y trazabilidad de fuentes en Actividad 1.",
      "Preservar memoria editorial reutilizable sin pérdida semántica ni técnica."
    ],
    "style_markers": [
      "Abrir con problema y objetivo explícito.",
      "Desarrollar con conceptos y marco normativo/doctrinal.",
      "Sostener cada afirmación con evidencia citada.",
      "Incluir postura propia diferenciada del resumen.",
      "Cerrar con conclusión jurídica aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> análisis propio -> conclusión.",
      "Regla jurídica -> contraste doctrinal -> aplicación al caso -> toma de postura.",
      "Pregunta guía -> respuesta fundada -> implicación práctica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofía del Derecho",
        "Objeto de estudio del derecho",
        "Justicia",
        "Fundamentos del derecho",
        "Derecho y moral",
        "Hermenéutica e interpretación jurídica",
        "Argumentación jurídica",
        "Constitución Política de los Estados Unidos Mexicanos",
        "Ley General de Víctimas",
        "Violencia física en delito de violación",
        "Incapacidad de resistencia y consentimiento"
      ],
      "citations": [
        "finnis_estudios_2017",
        "lovon_manual_2020",
        "ruiz_rodriguez_filosofia_derecho_2009",
        "rojas_gonzalez_filosofia_derecho_2018",
        "noauthor_constitucion_nodate",
        "de_victimas_ley_2013",
        "generales_ley_2021",
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
          "target": "Justicia",
          "kind": "develops",
          "justification": "La asignatura analiza fundamentos y fines del derecho."
        },
        {
          "source": "Hermenéutica e interpretación jurídica",
          "target": "Argumentación jurídica",
          "kind": "depends_on",
          "justification": "La interpretación sustenta la construcción de argumentos jurídicos."
        },
        {
          "source": "Constitución Política de los Estados Unidos Mexicanos",
          "target": "Ley General de Víctimas",
          "kind": "supports",
          "justification": "El marco constitucional fundamenta protección y reparación a víctimas."
        },
        {
          "source": "scjnViolenciaFisica2022",
          "target": "Violencia física en delito de violación",
          "kind": "develops",
          "justification": "Precisa criterio judicial sobre configuración típica sin resistencia física."
        },
        {
          "source": "scjnIncapacidadResistencia2019",
          "target": "Incapacidad de resistencia y consentimiento",
          "kind": "develops",
          "justification": "Descarta incapacidad de resistencia como consentimiento válido."
        }
      ],
      "evidence": [
        "README.md: identidad institucional y ubicación curricular.",
        "programa-analitico-filosofia-del-derecho.md: propósito y ejes de trabajo.",
        "reporte-filosofia-del-derecho-Actividad-1.tex: estructura argumentativa reconstruible.",
        "filosofia-del-derecho-clean.bib: evidencia de enfoque en Semana 7 [supuesto local confirmado por encabezado del archivo]."
      ]
    },
    "reinforcement_log": [
      "Ciclo 44: deduplicación integral aplicada sin eliminar reglas útiles.",
      "Ciclo 44: se conservaron supuestos explícitos y se evitó inventar fuentes.",
      "Ciclo 44: se reforzó patrón argumentativo canónico y control de calidad JSON.",
      "Ciclo 44: se mantiene compatibilidad con TEX primario y claves BibTeX existentes."
    ]
  }
}