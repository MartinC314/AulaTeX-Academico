{
  "summary": [
    "Consolidar memoria de materia de Filosofía del Derecho con identidad UnADM.",
    "Elevar desde actividad-1 patrones reutilizables sin copiar redacción literal.",
    "Mantener compresión lossless por unión y deduplicación sin regresión.",
    "Preservar normalización obligatoria de insumos no JSON antes de propagación.",
    "Fijar eje transversal: problema, conceptos, evidencia, análisis propio y conclusión jurídica."
  ],
  "identity_rules": [
    "Mantener tono institucional UnADM en toda salida.",
    "Alinear contenidos con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar carpeta de materia como punto de entrada canónico.",
    "Marcar como [supuesto] todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local. [supuesto]",
    "Usar malla-curricular-derecho-unadm.pdf como respaldo curricular verificado."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en: conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Alinear formato final al producto solicitado en planeación semanal.",
    "Cerrar con conclusión jurídica transferible a práctica profesional.",
    "Mantener trazabilidad entre actividad, .tex y .bib de la materia."
  ],
  "activity_rules": [
    "Evitar entregas solo descriptivas.",
    "Incluir postura argumentada del estudiante.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir fuentes de semanas posteriores para actividad-1. [supuesto]",
    "Confirmar que cada entrega corresponde a la consigna específica."
  ],
  "quality_gates": [
    "Bloquear propagación si salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No eliminar reglas útiles previas en ciclos de consolidación."
  ],
  "latex_rules": [
    "Usar acentos y codificación correcta en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas.",
    "No renombrar claves citadas sin migración completa.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "No adoptar nombres anómalos como canon hasta corrección local. [supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Registrar fuentes de actividad en el .bib de la materia con trazabilidad.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "No completar entradas truncadas sin verificación local. [supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas por README, programa analítico y .bib local.",
    "Elevar patrones argumentativos y de calidad desde actividades al nivel materia.",
    "Propagar lateralmente solo reglas generales, no supuestos locales no confirmados.",
    "Mantener etiqueta de compresión unión-dedupe lossless en cada ciclo.",
    "Registrar incidencias de parseo como riesgo de ingesta sin perder contenido útil.",
    "Conservar trazabilidad de citas recurrentes al subir de actividad a materia."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-1. [supuesto]",
    "Confirmar nombre canónico final del .bib de la asignatura. [supuesto]",
    "Confirmar si filosofia-del-derecho-clean.bib aplica fuera de Semana 7. [supuesto]",
    "Completar y verificar entrada scjnIncapacidadResistencia2019 truncada. [supuesto]",
    "Corregir definitivamente placeholders Slug en README y programa analítico. [supuesto]"
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
        "Carpeta de materia como entrada canónica editorial."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos.",
        "Asignatura: Filosofía del Derecho."
      ]
    },
    "essence": [
      "Resolver problemas jurídicos con base conceptual y normativa.",
      "Sostener análisis propio con evidencia verificable.",
      "Conectar teoría jurídica con transferencia profesional.",
      "Preservar continuidad editorial entre actividades y materia."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos.",
      "Estandarizar calidad argumentativa y trazabilidad de fuentes.",
      "Asegurar consistencia institucional y curricular en LaTeX."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado explícito y estable.",
      "Marcado visible de supuestos.",
      "Cierre con conclusión jurídica aplicable."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer marco conceptual y normativo.",
      "Desarrollar análisis crítico con postura propia.",
      "Concluir con criterio jurídico transferible."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofía del Derecho",
        "Hermenéutica e interpretación jurídica",
        "Argumentación jurídica",
        "Derecho y moral",
        "Justicia",
        "Análisis crítico del fenómeno jurídico",
        "Conclusión jurídica transferible"
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
          "justification": "La interpretación fundamenta razones y criterios argumentativos."
        },
        {
          "source": "Argumentación jurídica",
          "target": "Análisis crítico del fenómeno jurídico",
          "kind": "develops",
          "justification": "Permite evaluar validez, coherencia y consecuencias."
        },
        {
          "source": "Filosofía del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "Integra el debate axiológico en la comprensión del derecho."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusión jurídica transferible",
          "kind": "depends_on",
          "justification": "La conclusión exige sustento verificable."
        }
      ],
      "evidence": [
        "README de materia: pauta editorial y ubicación curricular.",
        "Programa analítico: propósito y cinco ejes de trabajo.",
        "Actividad-1: patrón problema-conceptos-evidencia-análisis-conclusión.",
        "Regla persistente: bloquear propagación sin JSON parseable.",
        "Bibliografía local: claves jurídicas recurrentes y trazables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 82: se eleva ADN editorial de actividad-1 a materia por abstracción ascendente.",
      "Se deduplican reglas y se preservan todas las útiles previas.",
      "Se refuerzan puertas de calidad de parseo, estructura y trazabilidad.",
      "Se mantienen citas recurrentes y relaciones conceptuales transferibles.",
      "Se marcan como [supuesto] los puntos no verificados localmente."
    ]
  }
}