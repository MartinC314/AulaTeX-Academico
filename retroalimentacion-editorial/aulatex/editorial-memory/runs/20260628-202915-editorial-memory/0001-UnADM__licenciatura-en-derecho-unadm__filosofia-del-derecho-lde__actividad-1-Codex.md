{
  "summary": [
    "Memoria local canonizada por unión y deduplicación sin pérdida.",
    "Se preserva identidad UnADM y contexto curricular de Filosofía del Derecho.",
    "Se mantiene normalización obligatoria antes de propagación recursiva.",
    "Se consolidan ejes editoriales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se preserva TEX reconstruible y trazabilidad de fuentes locales verificables."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto cualquier dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Citar malla-curricular-derecho-unadm.pdf como base de ubicación curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear la entrega al producto solicitado en la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Verificar que el producto corresponda a la consigna de Actividad 1.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir que fuentes de semanas posteriores corresponden a Actividad 1."
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
    "Compilar sin errores críticos y sin referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
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
      "Transformar la planeación semanal en productos académicos con fundamento jurídico y cierre argumentativo.",
      "Convertir consigna en entrega verificable, citada y profesionalmente transferible."
    ],
    "style_markers": [
      "Abrir con encuadre del problema.",
      "Ordenar por secciones explícitas y funcionales.",
      "Diferenciar marco conceptual de postura propia.",
      "Usar marcas de supuesto cuando falte evidencia local."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos y marco normativo -> análisis propio -> conclusión jurídica.",
      "Afirmación -> respaldo verificable -> interpretación -> implicación práctica.",
      "Síntesis doctrinal breve seguida de toma de postura."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofía del Derecho",
        "Problema jurídico o social",
        "Marco normativo y doctrinal",
        "Análisis crítico del fenómeno jurídico",
        "Conclusión jurídica transferible",
        "Hermenéutica e interpretación jurídica",
        "Argumentación jurídica"
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
          "justification": "El encuadre del problema activa el desarrollo argumentativo."
        },
        {
          "source": "Marco normativo y doctrinal",
          "target": "Análisis crítico del fenómeno jurídico",
          "kind": "depends_on",
          "justification": "La postura propia requiere base conceptual y jurídica verificable."
        },
        {
          "source": "Análisis crítico del fenómeno jurídico",
          "target": "Conclusión jurídica transferible",
          "kind": "develops",
          "justification": "La conclusión deriva de la evaluación razonada de fuentes y conceptos."
        },
        {
          "source": "Hermenéutica e interpretación jurídica",
          "target": "Argumentación jurídica",
          "kind": "supports",
          "justification": "La interpretación fundamenta la justificación de tesis y contra tesis."
        }
      ],
      "evidence": [
        "README.md: identidad UnADM, ubicación curricular y pauta editorial.",
        "programa-analitico-filosofia-del-derecho.md: propósito y ejes de trabajo.",
        "reporte-filosofia-del-derecho-Actividad-1.tex: fuente TEX reconstruible con 79 bloques.",
        "filosofia-del-derecho.bib y filosofia-del-derecho-clean.bib: claves y trazabilidad bibliográfica local."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas con variantes ortográficas mínimas.",
      "Se conservaron todos los supuestos críticos y alertas de verificación.",
      "Se reforzó patrón argumentativo canónico sin eliminar memoria previa útil.",
      "Se mantuvo compatibilidad con propagación recursiva y control de calidad JSON."
    ]
  }
}