{
  "summary": [
    "Se consolida refuerzo lateral para Actividad 5 con deduplicación lossless.",
    "Se preserva identidad UnADM y contexto curricular de Filosofía del Derecho.",
    "Se mantiene regla crítica: no propagar sin JSON parseable y estructura mínima completa.",
    "Se transfieren patrones reutilizables de Actividad 1 sin copiar redacción, conclusiones ni bibliografía exclusiva.",
    "Se conserva eje editorial troncal: problema, conceptos, evidencia, análisis propio y conclusión jurídica transferible.",
    "Supuesto: falta consigna local completa de Actividad 5; se mantiene estructura base y preguntas abiertas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y encuadre.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Conservar enfoque jurídico-académico con claridad, fundamento y transferencia profesional.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas de modelos como provisionales hasta verificación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir afirmaciones, evidencia y conclusión en bloques claros.",
    "Alinear el entregable al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica aplicable a práctica profesional."
  ],
  "activity_rules": [
    "Adaptar el producto al enunciado real de Actividad 5 sin romper reglas de asignatura.",
    "Incluir postura argumentada del estudiante y evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar bibliografía de otra semana sin confirmar pertinencia.",
    "Registrar supuesto operativo si hay duda de alcance."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en cada afirmación relevante.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que el producto responda al problema y no solo resuma conceptos.",
    "Aplicar revisión manual extra en memoria afectada por incidentes de parseo previos."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: el .bib canónico esperado es filosofia-del-derecho.bib; confirmar en repositorio local."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Registrar en .bib solo fuentes realmente citadas en el texto.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Supuesto: filosofia-del-derecho-clean.bib está orientado a Semana 7; confirmar pertinencia para Actividad 5 antes de reutilizar."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Reutilizar reglas institucionales de calidad sin perder especificidad local.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Propagar solo patrones generales cuando falte consigna textual.",
    "No propagar fuentes no verificadas como bibliografía académica.",
    "Mantener bandera de riesgo histórico por salidas no parseables en ciclos previos."
  ],
  "open_questions": [
    "Confirmar consigna textual completa de Actividad 5.",
    "Confirmar rúbrica de evaluación específica de Actividad 5.",
    "Confirmar si el producto principal es reporte, presentación o recurso visual.",
    "Confirmar nombre canónico final del archivo .bib de la asignatura.",
    "Confirmar si Actividad 5 requiere bibliografía propia distinta de Semana 7.",
    "Confirmar si persisten marcadores de plantilla en README y programa analítico."
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
      "Problema jurídico o social delimitado.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable y trazable.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir la planeación semanal en productos argumentativos con utilidad profesional.",
      "Asegurar consistencia entre consigna, desarrollo, evidencia y cierre.",
      "Sostener continuidad editorial entre actividades hermanas sin copiar contenido específico."
    ],
    "style_markers": [
      "Encuadre inicial breve y funcional.",
      "Secciones con propósito explícito.",
      "Inferencias jurídicas sustentadas.",
      "Supuestos marcados cuando falte dato local.",
      "Cierre aplicado a práctica profesional."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> inferencia jurídica.",
      "Contraste doctrinal breve -> toma de postura.",
      "Conclusión -> transferencia a práctica jurídica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Problema jurídico",
        "Marco normativo/doctrinal",
        "Evidencia verificable",
        "Análisis propio",
        "Conclusión transferible",
        "Normalización JSON",
        "Consistencia cita-.bib"
      ],
      "citations": [
        "README.md",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Estructura de actividad",
          "kind": "supports",
          "justification": "Define tono, forma y criterios mínimos del entregable."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis requiere una pregunta jurídica delimitada."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión válida depende de respaldo trazable."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia confiable."
        },
        {
          "source": "Bibliografía específica de actividad",
          "target": "Bibliografía base",
          "kind": "contrasts",
          "justification": "La base orienta; la específica responde a la consigna concreta."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "El marco sustenta la argumentación y evita opinión aislada."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad académica, citas verificables y conclusión jurídica propia.",
        "Programa analítico: ejes problema-conceptos-fuentes-análisis-cierre.",
        "Historial de ciclos: incidentes de parseo justifican gate estricto de JSON.",
        "Regla de transferencia: solo patrones reutilizables entre nodos hermanos."
      ]
    },
    "reinforcement_log": [
      "Ciclo 19: deduplicación semántica de reglas repetidas sin pérdida funcional.",
      "Ciclo 19: se refuerza separación entre bibliografía base y bibliografía específica de actividad.",
      "Ciclo 19: se mantiene bloqueo de propagación ante salida no parseable.",
      "Ciclo 19: se preserva ADN argumentativo común y se evita arrastre de contenido exclusivo de Actividad 1.",
      "Ciclo 19: se agregan supuestos explícitos donde falta consigna local verificable."
    ]
  }
}