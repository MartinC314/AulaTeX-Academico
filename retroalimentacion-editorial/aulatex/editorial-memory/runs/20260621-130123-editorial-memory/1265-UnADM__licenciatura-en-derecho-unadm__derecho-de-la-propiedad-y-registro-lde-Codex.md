{
  "summary": [
    "Se consolida sincronización transversal entre nodos no equivalentes con transferencia de abstracciones estables.",
    "Se preserva identidad UnADM y estructura editorial común sin mover contenido temático específico de Filosofía del Derecho.",
    "Se refuerza política de normalización obligatoria: no propagar salidas no JSON parseables.",
    "Se mantiene estrategia progresiva y conservadora con compresión lossless por unión y deduplicación.",
    "Se corrige como supuesto la resolución de tokens Slug en README y programa analítico del destino."
  ],
  "identity_rules": [
    "Mantener identidad explícita UnADM en tono, portada y metadatos.",
    "Usar nombre exacto de materia: Derecho de la propiedad y registro.",
    "Mantener programa: Licenciatura en Derecho.",
    "Mantener ubicación curricular: semestre 7, bloque 1, obligatoria, 8 créditos.",
    "Usar código local LDE-S7B1 cuando aplique.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el producto al entregable pedido en planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener consistencia con ejes de trabajo del programa analítico local."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Relacionar desarrollo con propiedad y registro cuando la consigna lo exija.",
    "No asumir fuentes de semanas posteriores sin validación de consigna."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar que el producto final corresponda a la actividad solicitada.",
    "Confirmar que no existan placeholders sin resolver antes de entrega."
  ],
  "latex_rules": [
    "Conservar plantilla base .tex de la materia como punto de partida.",
    "Mantener clase article con spanish, letterpaper y oneside salvo instrucción distinta.",
    "Completar metadatos académicos obligatorios antes de compilar.",
    "Actualizar documenttitle y documentsubtitle en cada actividad.",
    "Corregir campos incompletos en authortable antes de entrega.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Verificar nombres de archivo en README y resolver tokens sin expandir tipo $(@{...}.Slug).",
    "[Supuesto] El .bib canónico del destino es derecho-de-la-propiedad-y-registro.bib por Slug local."
  ],
  "bibliography_rules": [
    "Usar archivo BibTeX local de la materia para fuentes específicas.",
    "Priorizar fuentes institucionales UnADM y fuentes jurídicas verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Mantener trazabilidad entre citas del texto y claves BibTeX."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Compartir entre nodos no equivalentes solo abstracciones editoriales estables.",
    "No propagar redacción literal ni contenido temático específico de otra asignatura.",
    "Reutilizar reglas institucionales de calidad sin perder especificidad local.",
    "Evitar regresiones: conservar toda regla útil previa.",
    "Aplicar normalización manual cuando se detecten salidas históricas no parseables."
  ],
  "open_questions": [
    "Confirmar rúbrica formal de evaluación por actividad en la materia destino.",
    "Confirmar estilo de citación jurídica requerido por figura docente.",
    "Confirmar producto principal por actividad: reporte, presentación u otro.",
    "Confirmar sustitución del placeholder 'Figura docente' en plantilla .tex.",
    "Confirmar si existe guía local adicional para fuentes de propiedad y registro."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador en inferencias."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Normalización estructurada obligatoria antes de propagación.",
        "Sin propagación de salidas no parseables."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 7, bloque 1, obligatoria, 8 créditos.",
        "Materia: Derecho de la propiedad y registro.",
        "Código local: LDE-S7B1."
      ]
    },
    "essence": [
      "Problema jurídico.",
      "Conceptos y fundamento normativo.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión transferible."
    ],
    "reason_for_being": [
      "Transformar planeación semanal en productos académicos claros y verificables.",
      "Asegurar trazabilidad entre argumento, evidencia y cierre jurídico."
    ],
    "style_markers": [
      "Frases breves y accionables.",
      "Supuestos marcados de forma explícita.",
      "Sin afirmaciones sin fuente.",
      "Sin placeholders al cierre."
    ],
    "argumentative_patterns": [
      "Del problema al marco conceptual.",
      "Del marco normativo a la evidencia.",
      "De la evidencia al análisis propio.",
      "Del análisis a una conclusión aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad académica",
        "Normalización JSON",
        "Problema jurídico",
        "Marco normativo/doctrinal",
        "Evidencia verificable",
        "Análisis propio",
        "Conclusión transferible",
        "Trazabilidad bibliográfica"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La identidad institucional exige consistencia formal y citas verificables."
        },
        {
          "source": "Normalización JSON",
          "target": "Trazabilidad bibliográfica",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay control consistente de reglas y citas."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis responde al problema delimitado."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica requiere fundamento normativo y doctrinal."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Las afirmaciones se sostienen con fuentes consultables."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión transferible",
          "kind": "develops",
          "justification": "La conclusión deriva del razonamiento del estudiante, no de resumen descriptivo."
        }
      ],
      "evidence": [
        "README local de la materia: pauta editorial y entrada canónica.",
        "Programa analítico local: propósito y ejes de trabajo.",
        "BibTeX local con claves institucionales existentes.",
        "Regla histórica consolidada: bloquear propagación sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 9: deduplicación de reglas repetidas en summary, identidad, estructura y calidad.",
      "Ciclo 9: transferencia transversal limitada a abstracciones estables; sin migrar contenido doctrinal de Filosofía del Derecho.",
      "Ciclo 9: refuerzo de gates críticos de parseo JSON y trazabilidad cita-.bib.",
      "Ciclo 9: conservación de reglas útiles previas del destino sin regresión."
    ]
  }
}