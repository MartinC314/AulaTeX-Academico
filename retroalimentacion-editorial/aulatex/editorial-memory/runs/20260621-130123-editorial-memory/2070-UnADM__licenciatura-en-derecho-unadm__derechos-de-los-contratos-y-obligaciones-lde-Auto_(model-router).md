```json
{
  "summary": [
    "Se refuerza sincronización transversal entre actividad y materia sin trasladar redacción literal.",
    "Se preservan ejes editoriales UnADM y se adaptan al enfoque contractual.",
    "Se consolida cerebro editorial mínimo de materia con reglas reutilizables.",
    "Se mantiene compresión lossless por unión y deduplicación.",
    "Se refuerza normalización estructurada previa a toda propagación."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares confirmados de la materia destino.",
    "Marcar como [supuesto] todo dato no visible en la consigna local.",
    "Tratar herencias Codex o GPT-Pro como provisionales hasta verificación.",
    "Usar la carpeta de materia como punto de entrada canónico."
  ],
  "structure_rules": [
    "Aplicar modelo transversal de cinco ejes: problema, conceptos, producto, análisis propio y conclusión jurídica.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Separar secciones en conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear el entregable al producto de la planeación semanal."
  ],
  "activity_rules": [
    "Adaptar cada actividad al enfoque de contratos y obligaciones.",
    "Explicitar postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "No trasladar contenido de otras materias sin adecuación disciplinar."
  ],
  "quality_gates": [
    "Bloquear persistencia o propagación si la salida no es JSON parseable.",
    "Normalizar toda herencia no estructurada antes de reutilizar.",
    "Verificar coherencia entre objetivo, evidencia, argumento y cierre.",
    "Confirmar trazabilidad entre citas en texto y archivo .bib local.",
    "No degradar reglas útiles previas durante unión-dedupe."
  ],
  "latex_rules": [
    "Conservar plantilla LaTeX base de la materia y metadatos completos.",
    "Usar español académico con terminología jurídica precisa.",
    "Verificar que el .bib referenciado sea el canónico de la materia.",
    "Resolver placeholders tipo $(@{...}.Slug) antes de compilar.",
    "Compilar sin errores críticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Usar archivo .bib canónico local de la materia.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales verificables.",
    "No inventar referencias; declarar [supuesto] si falta una fuente.",
    "Distinguir bibliografía base de fuentes específicas por actividad.",
    "Conservar metadatos mínimos completos en cada entrada."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables a nodos laterales.",
    "Evitar transferir redacción literal entre materias no equivalentes.",
    "Aplicar validación disciplinar antes de propagación transversal.",
    "Propagar recursivamente solo tras validar JSON y estructura mínima.",
    "Mantener controles de calidad institucional como reglas transversales."
  ],
  "open_questions": [
    "Confirmar guía formal de citación jurídica obligatoria en la materia.",
    "Precisar alcance de fuentes: federales, locales o mixtas por actividad.",
    "Definir formato mínimo esperado de la conclusión jurídica.",
    "Confirmar rúbrica de evaluación por actividad.",
    "Confirmar si presentación y reporte comparten metadatos completos."
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
        "Carpeta de materia como entrada canónica"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Semestre 4, bloque 1, obligatoria",
        "Enfoque en contratos y obligaciones"
      ]
    },
    "essence": [
      "Modelo transversal de cinco ejes editoriales",
      "Identidad institucional UnADM",
      "Análisis jurídico aplicado",
      "Evidencia verificable",
      "Conclusión transferible a la práctica profesional"
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos trazables",
      "Garantizar coherencia entre problema, análisis y cierre",
      "Asegurar transferencia profesional del razonamiento jurídico"
    ],
    "style_markers": [
      "Supuestos siempre etiquetados",
      "Secciones funcionales y trazables",
      "Cierre jurídico operativo",
      "Normalización estructurada previa a propagación"
    ],
    "argumentative_patterns": [
      "Problema delimitado",
      "Marco conceptual y normativo pertinente",
      "Análisis propio sustentado",
      "Conclusión jurídica aplicable"
    ],
    "knowledge_graph": {
      "concepts": [
        "Problema jurídico",
        "Contratos",
        "Obligaciones",
        "Análisis jurídico propio",
        "Conclusión transferible",
        "Normalización estructurada"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Problema jurídico",
          "target": "Análisis jurídico propio",
          "kind": "depends_on",
          "justification": "El análisis se construye a partir de un conflicto delimitado."
        },
        {
          "source": "Análisis jurídico propio",
          "target": "Conclusión transferible",
          "kind": "develops",
          "justification": "La conclusión deriva del razonamiento sustentado."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación transversal",
          "kind": "supports",
          "justification": "Evita contaminación de memoria con salidas no válidas."
        }
      ],
      "evidence": [
        "README y programa analítico de la materia",
        "Archivo .bib local con fuentes institucionales",
        "Reglas de calidad institucional UnADM"
      ]
    },
    "reinforcement_log": [
      "Se preservan reglas útiles previas sin regresión.",
      "Se refuerza el modelo transversal de cinco ejes.",
      "Se adapta identidad editorial al enfoque contractual.",
      "Se mantiene compresión lossless por deduplicación."
    ]
  }
}
```