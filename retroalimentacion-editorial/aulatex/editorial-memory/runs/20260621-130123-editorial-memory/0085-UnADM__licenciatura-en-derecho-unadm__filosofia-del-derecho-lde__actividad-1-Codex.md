{
  "summary": [
    "Memoria local canonizada por unión y deduplicación sin pérdida.",
    "Se preserva identidad institucional UnADM y contexto curricular verificable.",
    "Se mantiene normalización JSON obligatoria antes de toda propagación.",
    "Se consolidan ejes editoriales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se conserva TEX reconstruible y continuidad de claves/citas."
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
    "Validar correspondencia del producto con la consigna de Actividad 1."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar fuentes específicas de la actividad en el .bib de la asignatura.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "No inventar referencias; usar solo obras realmente consultables.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "No asumir que filosofia-del-derecho-clean.bib corresponde a Actividad 1.",
    "Supuesto: filosofia-del-derecho-clean.bib está orientado a Semana 7 (interpretación jurídica)."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Propagar solo reglas generales cuando falte consigna textual.",
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
      "Transformar la planeación semanal en productos académicos con fundamento jurídico, evidencia y transferencia profesional.",
      "Convertir consigna en entrega verificable, argumentada y útil para práctica jurídica."
    ],
    "style_markers": [
      "Abrir con encuadre del problema.",
      "Nombrar objetivo puntual al inicio.",
      "Diferenciar marco conceptual y análisis propio.",
      "Cerrar con conclusión jurídica aplicable.",
      "Marcar supuestos explícitamente cuando falte dato en consigna."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> análisis propio -> conclusión jurídica.",
      "Afirmación jurídica -> respaldo normativo/doctrinal -> interpretación -> toma de postura.",
      "Consigna -> criterios de rúbrica -> verificación final de coherencia."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofía del Derecho",
        "Justicia",
        "Fundamentos del derecho",
        "Interpretación jurídica",
        "Argumentación jurídica",
        "Derecho y moral",
        "Constitución y derechos de víctimas"
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
          "source": "Filosofía del Derecho",
          "target": "Fundamentos del derecho",
          "kind": "develops",
          "justification": "La asignatura estructura bases conceptuales del fenómeno jurídico."
        },
        {
          "source": "Interpretación jurídica",
          "target": "Argumentación jurídica",
          "kind": "depends_on",
          "justification": "La justificación de tesis requiere criterios interpretativos."
        },
        {
          "source": "Constitución y derechos de víctimas",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "El cierre profesional exige anclaje normativo vigente."
        }
      ],
      "evidence": [
        "README y programa analítico confirman identidad, propósito y ejes.",
        "reporte-filosofia-del-derecho-Actividad-1.tex confirma artefacto y citas usadas.",
        "filosofia-del-derecho-clean.bib indica enfoque de Semana 7, no canónico para Actividad 1."
      ]
    },
    "reinforcement_log": [
      "Ciclo 22: deduplicación semántica aplicada sin eliminar reglas útiles.",
      "Ciclo 22: se mantiene continuidad de TEX reconstruible (79 bloques).",
      "Ciclo 22: se refuerza control de supuestos y verificación de consigna.",
      "Ciclo 22: se preserva prioridad de validación JSON antes de propagación."
    ]
  }
}