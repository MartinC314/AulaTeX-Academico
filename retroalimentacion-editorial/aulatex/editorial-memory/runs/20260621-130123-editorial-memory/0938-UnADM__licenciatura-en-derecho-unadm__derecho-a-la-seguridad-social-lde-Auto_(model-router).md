```json
{
  "summary": [
    "Se sincroniza memoria editorial transversal desde actividad no equivalente.",
    "Se preserva identidad UnADM y estructura por ejes reutilizables.",
    "Se refuerza control de calidad, JSON parseable y compresión union-dedupe.",
    "No se transfiere contenido temático de Filosofía al destino.",
    "Se consolida cerebro editorial mínimo para la materia."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en todo artefacto.",
    "Usar datos curriculares oficiales del destino; marcar cambios como [supuesto].",
    "Conservar trazabilidad de reglas heredadas provisionales.",
    "No sobrescribir reglas válidas previas; solo unir y deduplicar.",
    "Usar carpeta de materia como punto de entrada canónico."
  ],
  "structure_rules": [
    "Alinear entregas a cinco ejes: problema, conceptos/norma, producto, análisis, conclusión.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Separar marco normativo/doctrinal de análisis propio.",
    "Cerrar con conclusión jurídica transferible a la práctica.",
    "Tomar README y programa analítico como canon local."
  ],
  "activity_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Incluir postura académica propia, no solo descripción.",
    "Sustentar afirmaciones con fuentes verificables o marcar [supuesto].",
    "Ajustar formato al producto solicitado en la planeación.",
    "Relacionar la actividad con el campo de seguridad social cuando aplique."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizar.",
    "Verificar coherencia entre objetivo, desarrollo y conclusión.",
    "Confirmar correspondencia entre citas en texto y .bib local.",
    "Garantizar compresión lossless por unión-dedupe sin regresión."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia; personalizar solo campos variables.",
    "Mantener idioma español y codificación correcta.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Normalizar rutas y nombres de archivo antes de compilar."
  ],
  "bibliography_rules": [
    "Usar el .bib local de la materia como fuente central.",
    "No inventar referencias; marcar faltantes como pendientes.",
    "Conservar metadatos mínimos completos y verificables.",
    "Distinguir bibliografía base de la específica de actividad.",
    "Verificar vigencia normativa antes de citar textos legales."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Evitar transferencia de redacción literal o contenido temático.",
    "Priorizar identidad, estructura reusable y gates de calidad.",
    "Mantener bandera de riesgo por antecedentes no parseables.",
    "Propagar recursivamente solo tras validación completa."
  ],
  "open_questions": [
    "Confirmar norma de citación requerida por la materia [supuesto].",
    "Verificar si existen rúbricas específicas por actividad.",
    "Confirmar productos obligatorios por semana en planeaciones.",
    "Validar vigencia de fuentes normativas locales antes de cierre."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico",
        "Claro y jurídicamente preciso",
        "Argumentativo con criterio propio"
      ],
      "institutional": [
        "Alineación explícita con UnADM",
        "Integridad académica con citas verificables",
        "Normalización estructurada obligatoria"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Respeto a semestre y bloque oficiales del destino",
        "Uso del programa analítico como guía editorial"
      ]
    },
    "essence": [
      "Problema jurídico delimitado",
      "Marco normativo verificable",
      "Análisis propio sustentado",
      "Evidencia y citas controladas",
      "Conclusión jurídica transferible"
    ],
    "reason_for_being": [
      "Garantizar coherencia editorial transversal sin pérdida de identidad local.",
      "Facilitar reutilización segura de reglas entre materias.",
      "Asegurar productos académicos verificables y profesionales."
    ],
    "style_markers": [
      "Frases cortas y accionables",
      "Separación visible entre marco y análisis",
      "Etiquetado explícito de [supuesto]",
      "Cierre con utilidad profesional"
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo",
      "Exponer fundamento normativo",
      "Contrastar evidencia",
      "Fijar postura propia",
      "Concluir con implicación práctica"
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema jurídico",
        "Marco normativo",
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
          "justification": "La conclusión válida depende del fundamento legal."
        },
        {
          "source": "JSON parseable",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura válida no hay reutilización segura."
        }
      ],
      "evidence": [
        "README y programa analítico del destino definen canon editorial.",
        "Historial institucional exige normalización previa a propagación."
      ]
    },
    "reinforcement_log": [
      "Se preservan reglas útiles previas sin eliminación.",
      "Se refuerza patrón editorial común entre materias.",
      "Se evita contaminación temática entre nodos no equivalentes."
    ]
  }
}
```