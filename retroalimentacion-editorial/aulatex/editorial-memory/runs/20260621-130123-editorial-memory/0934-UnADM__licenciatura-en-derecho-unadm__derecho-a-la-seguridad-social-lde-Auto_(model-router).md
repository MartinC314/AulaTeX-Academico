```json
{
  "summary": [
    "Se sincroniza ADN editorial estable desde actividad de Filosofía del Derecho hacia la materia Derecho a la Seguridad Social.",
    "La transferencia es transversal: solo abstracciones editoriales reutilizables, sin contenido temático ajeno.",
    "Se refuerza el patrón común: problema, marco, evidencia, análisis propio y conclusión jurídica.",
    "Se preserva identidad UnADM, control de calidad y compresión lossless por unión-dedupe.",
    "Se consolida cerebro editorial mínimo y reconstruible para la materia destino."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino; marcar cualquier inferencia como [supuesto].",
    "Conservar trazabilidad de reglas heredadas cuando sean provisionales.",
    "No sobrescribir reglas válidas previas; solo unir y deduplicar.",
    "Usar carpeta de la materia como punto de entrada canónico."
  ],
  "structure_rules": [
    "Iniciar cada producto con encuadre breve del problema jurídico o social.",
    "Organizar desarrollo en secciones claras y separadas.",
    "Usar estructura reusable: conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Alinear siempre el formato al producto solicitado por la planeación.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar solo resumen.",
    "Distinguir hechos, normas, doctrina y opinión propia.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Normalizar manualmente salidas no estructuradas antes de reutilizar.",
    "Validar estructura mínima completa antes de propagar recursivamente.",
    "Confirmar que toda afirmación tenga respaldo o marca de [supuesto].",
    "Verificar consistencia entre citas en texto y archivo .bib local."
  ],
  "latex_rules": [
    "Mantener codificación correcta en español en .tex y .bib.",
    "Conservar plantillas base; personalizar solo campos variables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Normalizar rutas y nombres de archivo antes de compilar."
  ],
  "bibliography_rules": [
    "Usar el archivo .bib local de la materia como fuente central.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Marcar referencias faltantes como pendientes."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable y gates de calidad.",
    "Evitar transferir redacción literal o contenido temático ajeno.",
    "Propagar recursivamente solo tras validación de JSON y estructura.",
    "Evitar regresiones respecto de reglas útiles previas."
  ],
  "open_questions": [
    "Confirmar norma de citación específica requerida por la materia [supuesto].",
    "Verificar rúbricas de evaluación para ajustar profundidad argumentativa.",
    "Confirmar productos exactos solicitados en cada planeación semanal.",
    "Definir si se requieren criterios jurisprudenciales obligatorios por actividad."
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
        "Normalización estructurada obligatoria antes de propagar"
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
      "Evidencia pertinente",
      "Análisis propio",
      "Conclusión jurídica transferible"
    ],
    "reason_for_being": [
      "Convertir consignas en productos jurídicos claros, verificables y útiles profesionalmente.",
      "Garantizar coherencia editorial transversal entre materias.",
      "Preservar identidad institucional y calidad académica."
    ],
    "style_markers": [
      "Frases cortas y accionables",
      "Separación visible entre marco, análisis y cierre",
      "Marcado explícito de [supuesto]",
      "Cierre con utilidad profesional"
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo",
      "Exponer marco normativo y doctrinal",
      "Contrastar evidencia relevante",
      "Fijar postura propia sustentada",
      "Concluir con implicación jurídica práctica"
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
        "README y programa analítico del destino definen estructura y propósito.",
        "Memoria origen aporta patrón editorial reusable sin contenido temático."
      ]
    },
    "reinforcement_log": [
      "Se preservaron reglas útiles previas sin eliminación.",
      "Se deduplicaron patrones editoriales comunes.",
      "Se evitó transferencia de contenido temático de Filosofía del Derecho.",
      "Se reforzó el ADN editorial como cerebro persistente transversal."
    ]
  }
}
```