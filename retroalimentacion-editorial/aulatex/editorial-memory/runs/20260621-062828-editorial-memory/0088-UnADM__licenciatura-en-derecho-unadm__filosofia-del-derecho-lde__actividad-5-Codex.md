{
  "summary": [
    "Se refuerza continuidad editorial entre actividades hermanas sin copiar redacción específica.",
    "Se preservan reglas troncales UnADM: identidad, estructura, evidencia verificable y cierre jurídico propio.",
    "Se consolida deduplicación lossless y se eliminan redundancias formales en la memoria destino.",
    "Se mantiene control estricto: no propagar si la salida no es JSON parseable.",
    "Supuesto: falta consigna local de Actividad 5; se conserva estructura base y preguntas abiertas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y encuadre.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Conservar enfoque jurídico-académico con claridad y precisión.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas de modelos como provisionales hasta verificación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir afirmación, evidencia e inferencia en bloques claros.",
    "Alinear el entregable al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Adaptar el producto al enunciado real de Actividad 5.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar bibliografía de otra semana sin confirmar pertinencia.",
    "Registrar supuesto operativo cuando exista ambigüedad de alcance."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en cada afirmación relevante.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que el producto responda al problema y no solo resuma conceptos.",
    "Aplicar revisión manual extra en memoria con incidentes previos de parseo."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables ya usadas en .tex.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver tokens sin expandir en README y programa analítico antes de automatizar rutas.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib, sujeto a verificación local."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar en .bib solo fuentes realmente citadas en el texto.",
    "No inventar referencias ni metadatos bibliográficos.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a Semana 7 y requiere validación de pertinencia para Actividad 5."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir solo patrones reutilizables: identidad, estructura, calidad y relaciones conceptuales.",
    "No transferir conclusiones específicas ni bibliografía exclusiva de un hermano.",
    "Preservar reglas útiles previas y agregar solo mejoras verificables.",
    "Aplicar unión y deduplicación sin pérdida semántica.",
    "Mantener bandera histórica de riesgo por salidas no parseables en ciclos previos."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 5.",
    "Confirmar rúbrica de evaluación específica de Actividad 5.",
    "Confirmar formato requerido: reporte, presentación o recurso visual.",
    "Confirmar nombre canónico final del archivo .bib de la asignatura.",
    "Confirmar si la bibliografía de Semana 7 es pertinente para Actividad 5.",
    "Confirmar fuentes obligatorias de la semana correspondiente."
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
      "Conceptos, normas o doctrina pertinentes.",
      "Producto solicitado por la planeación.",
      "Análisis propio y postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos.",
      "Asegurar trazabilidad entre consigna, evidencia y conclusión.",
      "Garantizar continuidad editorial institucional entre actividades."
    ],
    "style_markers": [
      "Encuadre inicial breve y funcional.",
      "Secciones con propósito argumentativo claro.",
      "Postura propia sustentada en evidencia.",
      "Uso explícito de supuestos cuando falte dato local."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> inferencia jurídica.",
      "Contraste doctrinal breve -> toma de postura -> transferencia práctica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalización JSON",
        "Problema jurídico",
        "Evidencia verificable",
        "Análisis propio",
        "Conclusión transferible",
        "Consistencia cita-.bib",
        "Bibliografía base",
        "Bibliografía específica de actividad"
      ],
      "citations": [
        "README.md",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Estructura de actividad",
          "kind": "supports",
          "justification": "La pauta institucional define tono, forma y exigencia académica."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis requiere una pregunta o conflicto delimitado."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica debe ser trazable y sustentada."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo válido no hay transferencia confiable."
        },
        {
          "source": "Bibliografía específica de actividad",
          "target": "Bibliografía base",
          "kind": "contrasts",
          "justification": "La base orienta la asignatura; la específica responde a la consigna."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión transferible",
          "kind": "develops",
          "justification": "La postura razonada madura en una conclusión aplicable."
        }
      ],
      "evidence": [
        "README exige identidad UnADM, citas verificables y conclusión jurídica propia.",
        "Programa analítico fija ejes: problema, conceptos, fuentes, análisis y cierre.",
        "Historial de parseo justifica compuerta estricta de estructura.",
        "Tokens sin expandir en rutas requieren verificación antes de compilar."
      ]
    },
    "reinforcement_log": [
      "Ciclo 88: deduplicación integral sin pérdida de reglas útiles previas.",
      "Ciclo 88: refuerzo lateral hermano->hermano aplicado por patrones reutilizables.",
      "Ciclo 88: se conserva separación entre bibliografía base y específica.",
      "Ciclo 88: se mantiene política de supuestos explícitos ante faltantes locales."
    ]
  }
}