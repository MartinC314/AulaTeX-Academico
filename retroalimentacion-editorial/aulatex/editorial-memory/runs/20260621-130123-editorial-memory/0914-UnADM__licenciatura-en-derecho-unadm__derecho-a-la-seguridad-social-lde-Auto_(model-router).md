```json
{
  "summary": [
    "Se consolida sincronización transversal entre actividad y materia no equivalente.",
    "Se preserva ADN editorial UnADM con estructura por ejes y control institucional.",
    "Se refuerzan reglas estables reutilizables sin transferir contenido temático.",
    "Se aplica compresión lossless por unión y deduplicación.",
    "Se mantiene alerta por salidas no parseables en ciclos previos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "No sobrescribir reglas válidas previas; unir y deduplicar.",
    "Conservar trazabilidad de reglas heredadas provisionales."
  ],
  "structure_rules": [
    "Usar README de la materia como canon estructural.",
    "Alinear entregas a cinco ejes: problema, conceptos/norma, producto, análisis y conclusión.",
    "Separar claramente marco, análisis propio y cierre.",
    "Transformar planeación semanal en producto verificable.",
    "Normalizar nombres de archivos antes de propagación."
  ],
  "activity_rules": [
    "Definir objetivo y problema jurídico desde el inicio.",
    "Vincular desarrollo con normas y doctrina pertinentes.",
    "Incluir postura académica propia sustentada.",
    "Evitar entregas solo descriptivas.",
    "Cerrar con conclusión jurídica transferible."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Normalizar manualmente salidas no estructuradas heredadas.",
    "Confirmar estructura mínima completa antes de reutilizar.",
    "Verificar respaldo o marca [supuesto] en toda afirmación relevante.",
    "Validar correspondencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificación correcta en español.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Corregir rutas y nombres corruptos antes de compilar."
  ],
  "bibliography_rules": [
    "Usar el archivo .bib local de la materia como fuente central.",
    "No inventar referencias; usar solo fuentes verificables.",
    "Conservar metadatos mínimos completos.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Marcar fuentes faltantes como pendientes."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables.",
    "Evitar transferencia de redacción literal o contenido temático.",
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Mantener bandera de riesgo por antecedentes de no parseable.",
    "Aplicar compresión union-dedupe sin regresión."
  ],
  "open_questions": [
    "Confirmar rúbrica específica de evaluación del destino.",
    "Confirmar norma de citación requerida por la materia [supuesto].",
    "Verificar si existen consignas especiales por actividad.",
    "Confirmar datos faltantes de plantilla institucional."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico",
        "Claro",
        "Jurídicamente preciso",
        "Argumentativo"
      ],
      "institutional": [
        "Alineación explícita con UnADM",
        "Integridad académica",
        "Normalización estructurada obligatoria"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Uso de datos curriculares oficiales del destino"
      ]
    },
    "essence": [
      "Problema jurídico delimitado",
      "Marco normativo verificable",
      "Evidencia sustentada",
      "Análisis propio",
      "Conclusión jurídica transferible"
    ],
    "reason_for_being": [
      "Crear productos académicos verificables y transferibles.",
      "Garantizar coherencia institucional transversal.",
      "Permitir reutilización segura de reglas editoriales."
    ],
    "style_markers": [
      "Frases cortas y accionables",
      "Separación visible entre secciones",
      "Uso explícito de [supuesto]",
      "Cierre con utilidad profesional"
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo",
      "Exponer marco normativo",
      "Analizar evidencia",
      "Fijar postura propia",
      "Concluir con implicación práctica"
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
          "justification": "El análisis requiere una pregunta delimitada."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión depende de fundamento legal."
        },
        {
          "source": "JSON parseable",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura válida no hay reutilización segura."
        }
      ],
      "evidence": [
        "README y programa analítico del destino",
        "Reglas institucionales UnADM",
        "Control editorial AulaTeX"
      ]
    },
    "reinforcement_log": [
      "Se refuerza patrón editorial común entre materias.",
      "Se preserva identidad UnADM sin mezclar contenidos.",
      "Se consolida cerebro editorial mínimo reutilizable."
    ]
  }
}
```