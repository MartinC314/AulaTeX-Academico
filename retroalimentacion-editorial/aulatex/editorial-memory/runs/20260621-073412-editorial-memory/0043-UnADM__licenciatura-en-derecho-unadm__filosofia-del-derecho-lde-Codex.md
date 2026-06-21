{
  "summary": [
    "Consolidar memoria de materia desde actividad-1 con abstracción ascendente y deduplicación lossless.",
    "Preservar identidad UnADM, trazabilidad curricular y reglas útiles sin regresión.",
    "Mantener normalización obligatoria para insumos no JSON parseable antes de propagar.",
    "Reforzar patrón editorial estable: problema, conceptos, evidencia, análisis propio y conclusión jurídica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en redacción y formato.",
    "Alinear entregables con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de materia como entrada canónica.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local. [supuesto]",
    "Conservar referencias provisionales heredadas (Codex, GPT-Pro) con etiqueta de riesgo de ingesta. [supuesto]",
    "Usar malla-curricular-derecho-unadm.pdf como respaldo curricular verificado."
  ],
  "structure_rules": [
    "Iniciar cada producto con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Alinear el producto al tipo solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener trazabilidad entre actividad, .tex y .bib de la materia."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante y evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir que fuentes de semanas posteriores aplican a actividad-1. [supuesto]",
    "Confirmar que cada entrega corresponde a la consigna específica de la actividad."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Evitar eliminación de reglas útiles previas en cada ciclo."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar sin migración completa.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir nombres/rutas anómalas antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar fuentes específicas por actividad en el .bib de la asignatura.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de materia y bibliografía específica de actividad.",
    "Mantener entradas truncadas como pendientes hasta verificación local (ej. scjnIncapacidadResistencia2019). [supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Elevar al ancestro reglas reutilizables de identidad, calidad, trazabilidad y argumentación.",
    "No propagar literalidad de una actividad; sintetizar patrones transferibles.",
    "Registrar incidencias de ingesta no parseable sin perder contenido útil.",
    "Aplicar unión-deduplicación lossless en cada salto para evitar regresiones."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-1 para fijar plantilla final.",
    "Confirmar nombre canónico definitivo del .bib de la materia.",
    "Definir si filosofia-del-derecho-clean.bib es temporal o canónico. [supuesto]",
    "Completar y verificar campos faltantes de scjnIncapacidadResistencia2019.",
    "Confirmar rúbrica de evaluación para ajustar profundidad argumentativa."
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
        "Carpeta de materia como entrada canónica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos.",
        "Asignatura: Filosofía del Derecho."
      ]
    },
    "essence": [
      "Problema jurídico o social delimitado.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable y trazable.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica aplicable."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en entregables académicos sólidos y verificables.",
      "Garantizar coherencia entre identidad institucional, método argumentativo y práctica jurídica."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable.",
      "Marcado explícito de [supuesto].",
      "Cierre con criterio jurídico propio."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer marco conceptual y normativo.",
      "Contrastar fuentes y construir análisis crítico.",
      "Defender postura propia.",
      "Concluir con transferencia profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofía del Derecho",
        "Hermenéutica e interpretación jurídica",
        "Argumentación jurídica",
        "Derecho y moral",
        "Justicia",
        "Análisis crítico del fenómeno jurídico",
        "Trazabilidad actividad-.tex-.bib"
      ],
      "citations": [
        "hernandezManriquezHermeneutica2019",
        "scjnMemoriaArgumentacion2008",
        "scjnViolenciaFisica2022",
        "scjnIncapacidadResistencia2019",
        "ruiz_rodriguez_filosofia_derecho_2009",
        "rojas_gonzalez_filosofia_derecho_2018",
        "noauthor_constitucion_nodate",
        "de_victimas_ley_2013"
      ],
      "relations": [
        {
          "source": "Hermenéutica e interpretación jurídica",
          "target": "Argumentación jurídica",
          "kind": "supports",
          "justification": "La interpretación aporta criterios para justificar argumentos."
        },
        {
          "source": "Argumentación jurídica",
          "target": "Análisis crítico del fenómeno jurídico",
          "kind": "develops",
          "justification": "Permite evaluar razones, normas y consecuencias."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusión jurídica transferible",
          "kind": "depends_on",
          "justification": "La conclusión válida exige soporte normativo verificable."
        },
        {
          "source": "Filosofía del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "La materia integra el debate entre validez normativa y contenido axiológico."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicación curricular y pauta editorial.",
        "Programa analítico: propósito y cinco ejes de trabajo.",
        "Regla persistente: bloquear propagación sin JSON parseable.",
        "Actividad-1: patrón problema-conceptos-evidencia-análisis-conclusión."
      ]
    },
    "reinforcement_log": [
      "Ciclo 43: se elevan reglas transferibles del nodo actividad al nodo materia sin copia literal.",
      "Ciclo 43: se preservan controles de calidad heredados y se refuerza normalización previa.",
      "Ciclo 43: se mantiene compresión lossless por unión-deduplicación y sin regresión."
    ]
  }
}