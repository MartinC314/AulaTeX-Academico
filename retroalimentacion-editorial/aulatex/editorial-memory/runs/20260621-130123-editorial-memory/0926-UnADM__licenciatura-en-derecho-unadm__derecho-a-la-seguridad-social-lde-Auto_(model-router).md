```json
{
  "summary": [
    "Se sincroniza ADN editorial estable desde actividad de Filosofía del Derecho hacia la materia Derecho a la Seguridad Social.",
    "La transferencia es transversal: se heredan abstracciones editoriales, no contenido temático.",
    "Se preserva identidad UnADM, estructura por ejes y control de calidad institucional.",
    "Se refuerza patrón común: problema, fundamento, evidencia, análisis propio y conclusión jurídica.",
    "La compresión aplicada es lossless por unión y deduplicación, sin regresión."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en todo producto.",
    "Usar datos curriculares oficiales del destino; marcar herencias como [supuesto] si no verificadas.",
    "No sobrescribir reglas válidas previas; solo unir y deduplicar.",
    "Conservar trazabilidad de reglas heredadas desde nodos no equivalentes."
  ],
  "structure_rules": [
    "Alinear toda entrega a ejes editoriales reutilizables: problema, conceptos/norma, análisis propio y conclusión.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Separar claramente marco normativo/doctrinal y análisis propio.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Incluir postura argumentada del estudiante; evitar solo descripción.",
    "Sustentar afirmaciones con fuentes verificables o marcar como [supuesto].",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de [supuesto].",
    "Verificar correspondencia entre producto final y consigna local."
  ],
  "latex_rules": [
    "Mantener compilación sin errores críticos ni referencias rotas.",
    "Usar codificación correcta en español y rutas limpias.",
    "Evitar comandos no estándar sin justificación editorial.",
    "No copiar plantillas completas entre materias; reutilizar solo estructura abstracta."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes consultables.",
    "Conservar metadatos mínimos completos en cada entrada.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Validar correspondencia entre citas en texto y archivo .bib local."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferencia de redacción literal o contenido temático ajeno.",
    "Aplicar normalización manual si se detectan salidas no estructuradas."
  ],
  "open_questions": [
    "Confirmar consignas específicas de actividades de Derecho a la Seguridad Social.",
    "Definir rúbrica local para ajustar profundidad argumentativa.",
    "Confirmar norma de citación jurídica requerida por la materia."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico",
        "Claro",
        "Jurídicamente preciso",
        "Argumentativo con criterio propio"
      ],
      "institutional": [
        "Alineación explícita con UnADM",
        "Integridad académica con citas verificables",
        "Normalización estructurada obligatoria antes de propagar"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Respeto a datos curriculares oficiales del destino",
        "Uso del programa analítico como guía editorial"
      ]
    },
    "essence": [
      "Resolver consignas mediante productos jurídicos verificables.",
      "Conectar problema jurídico con fundamento normativo.",
      "Exigir análisis propio y postura académica.",
      "Cerrar con utilidad profesional transferible."
    ],
    "reason_for_being": [
      "Servir como cerebro editorial persistente y reutilizable.",
      "Garantizar coherencia institucional entre materias.",
      "Evitar regresiones editoriales en ciclos sucesivos."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Separación visible entre marco, análisis y cierre.",
      "Marcado explícito de [supuesto] cuando aplique.",
      "Cierre con implicación jurídica práctica."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo o doctrinal pertinente.",
      "Contrastar evidencia.",
      "Fijar postura propia sustentada.",
      "Concluir con implicación jurídica aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema jurídico",
        "Marco normativo",
        "Evidencia verificable",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "JSON parseable",
        "Compresión union-dedupe"
      ],
      "citations": [],
      "relations": [
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis requiere una pregunta jurídica delimitada."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión válida depende de fundamento legal verificable."
        },
        {
          "source": "JSON parseable",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura válida no hay reutilización segura."
        }
      ],
      "evidence": [
        "Programa analítico del destino define ejes y propósito.",
        "README del destino fija estructura canónica.",
        "Reglas heredadas consolidadas por unión-dedupe."
      ]
    },
    "reinforcement_log": [
      "Se refuerza patrón editorial común sin mezclar contenido temático.",
      "Se preservan reglas útiles previas sin eliminación.",
      "Se consolida sincronización transversal en ciclo 12."
    ]
  }
}
```