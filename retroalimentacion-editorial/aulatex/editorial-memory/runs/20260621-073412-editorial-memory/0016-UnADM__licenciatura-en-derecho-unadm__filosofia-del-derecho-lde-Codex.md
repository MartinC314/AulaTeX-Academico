{
  "summary": [
    "Se consolida la memoria de materia con abstracción ascendente desde Actividad 1.",
    "Se preservan reglas útiles previas sin regresión y con deduplicación lossless.",
    "Se refuerza identidad UnADM, ubicación curricular y trazabilidad entre README, programa analítico, .tex y .bib.",
    "Se mantiene la normalización obligatoria de insumos no parseables antes de propagación.",
    "Se elevan patrones transferibles: problema, conceptos, evidencia, análisis propio y conclusión jurídica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, redacción y formato.",
    "Alinear entregables con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de materia como entrada canónica de la asignatura.",
    "Marcar como [supuesto] todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local. [supuesto]",
    "Conservar trazabilidad de fuente curricular: malla-curricular-derecho-unadm.pdf."
  ],
  "structure_rules": [
    "Iniciar cada producto con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Alinear el tipo de entrega a la planeación semanal.",
    "Mantener trazabilidad entre actividad, archivo .tex y archivo .bib."
  ],
  "activity_rules": [
    "Delimitar problema y pregunta guía al inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar solo descripción.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir que bibliografía de semanas posteriores aplica a Actividad 1. [supuesto]",
    "Validar que el producto final corresponda a la consigna específica."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de [supuesto].",
    "Validar consistencia entre citas en texto y entradas del .bib.",
    "Confirmar no regresión: no eliminar reglas útiles heredadas."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar sin migración completa.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Separar entregables por tipo en archivos .tex dedicados.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) antes de fijar nombres canónicos. [supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Distinguir bibliografía base de materia y bibliografía específica por actividad.",
    "Registrar fuentes de actividad en el .bib de la asignatura con metadatos mínimos.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar y deduplicar entradas sin pérdida de información.",
    "Tratar entradas truncadas como pendientes hasta verificación local. [supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Elevar a nodos ancestro reglas generales, identidad y patrones argumentativos reutilizables.",
    "No propagar literalidad de redacción de hijos; sintetizar patrones.",
    "Reusar puertas de calidad como filtro previo en nodos laterales.",
    "Mantener etiqueta de compresión union-dedupe lossless en cada ciclo.",
    "Registrar incidencias de parseo como riesgo de ingesta sin perder contenido válido."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 1 para cerrar supuestos de formato.",
    "Confirmar nombre canónico final del .bib de la materia.",
    "Resolver definitivamente placeholders $(@{...}.Slug) en README y programa analítico.",
    "Verificar si filosofia-del-derecho-clean.bib es auxiliar de semana o base general de materia. [supuesto]",
    "Completar y validar la entrada scjnIncapacidadResistencia2019 en .bib. [supuesto]"
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
      "Problema jurídico o social.",
      "Conceptos y marco normativo-doctrinal.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos y trazables.",
      "Asegurar coherencia entre identidad institucional, método argumentativo y práctica jurídica."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable.",
      "Marcado explícito de supuestos.",
      "Cierre con criterio jurídico propio."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Desarrollar marco conceptual y normativo.",
      "Contrastar fuentes y aplicar análisis crítico.",
      "Fijar postura propia fundada.",
      "Concluir con aplicabilidad profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofía del Derecho",
        "Hermenéutica e interpretación jurídica",
        "Argumentación jurídica",
        "Derecho y moral",
        "Justicia",
        "Análisis crítico del fenómeno jurídico",
        "Trazabilidad editorial UnADM"
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
          "justification": "La interpretación aporta criterios para construir argumentos."
        },
        {
          "source": "Argumentación jurídica",
          "target": "Análisis crítico del fenómeno jurídico",
          "kind": "develops",
          "justification": "Permite evaluar validez, razones y consecuencias."
        },
        {
          "source": "Filosofía del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "Integra debate axiológico y normativo."
        },
        {
          "source": "Marco normativo-doctrinal",
          "target": "Conclusión jurídica transferible",
          "kind": "depends_on",
          "justification": "La conclusión exige base normativa verificable."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicación curricular y pauta editorial.",
        "Programa analítico: propósito y cinco ejes de trabajo.",
        "Bibliografía local: claves jurídicas recurrentes verificables.",
        "Actividad 1: patrón estable problema-conceptos-evidencia-análisis-conclusión."
      ]
    },
    "reinforcement_log": [
      "Ciclo 16: se eleva memoria de actividad a materia con síntesis no literal.",
      "Ciclo 16: se consolidan puertas de calidad parseo+estructura+no regresión.",
      "Ciclo 16: se refuerza trazabilidad conceptual y bibliográfica reusable en propagación recursiva."
    ]
  }
}