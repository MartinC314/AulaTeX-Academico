```json
{
  "summary": [
    "Se sincroniza ADN editorial transversal UnADM desde actividad de Filosofía del Derecho hacia materia de Contratos y Obligaciones.",
    "Se preservan ejes editoriales estables y controles de calidad reutilizables.",
    "La transferencia es abstracta, conservadora y sin redacción literal.",
    "Se refuerza el cerebro editorial mínimo del destino para propagación recursiva."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Marcar como [supuesto] cualquier dato no confirmado localmente.",
    "Tratar herencias no verificadas como provisionales hasta validación.",
    "Usar carpeta de materia como punto de entrada canónico."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Alinear siempre el producto al tipo solicitado en la planeación."
  ],
  "activity_rules": [
    "Incluir postura argumentada propia; evitar solo descripción.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Adaptar contenidos heredados al enfoque contractual y obligacional."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Normalizar herencias no estructuradas antes de reutilizar.",
    "Confirmar trazabilidad entre objetivo, evidencia, argumento y cierre.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No eliminar reglas útiles previas durante unión-dedupe."
  ],
  "latex_rules": [
    "Conservar plantilla LaTeX base de la materia y metadatos completos.",
    "Usar español académico con acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables y referencias sin romper.",
    "Resolver placeholders tipo $(@{...}.Slug) antes de compilar."
  ],
  "bibliography_rules": [
    "No inventar referencias; declarar [supuesto] si falta fuente.",
    "Separar bibliografía base de fuentes específicas por actividad.",
    "Priorizar fuentes institucionales UnADM y normas verificables.",
    "Registrar fuentes de actividad en el .bib local de la materia."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables entre nodos transversales.",
    "Evitar transferir redacción literal o ejemplos contextuales.",
    "Propagar recursivamente tras validar estructura y JSON.",
    "Aplicar normalización manual en ciclo 1 si se reutiliza."
  ],
  "open_questions": [
    "Confirmar guía institucional de citación jurídica para la materia.",
    "Definir formato mínimo esperado de la conclusión jurídica.",
    "Confirmar planeación semanal específica de cada actividad.",
    "Confirmar uso requerido de legislación federal, local o mixta."
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
        "Carpeta como entrada canónica"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Semestre 4, bloque 1",
        "Asignatura centrada en contratos y obligaciones"
      ]
    },
    "essence": [
      "Problema jurídico como punto de partida",
      "Marco normativo y doctrinal verificable",
      "Análisis argumentativo propio",
      "Conclusión jurídica transferible"
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, fundamento y utilidad profesional.",
      "Garantizar coherencia institucional y calidad editorial transversal."
    ],
    "style_markers": [
      "Frases cortas y verificables",
      "Supuestos explicitados",
      "Cierre con utilidad profesional jurídica"
    ],
    "argumentative_patterns": [
      "Problema definido → marco normativo → análisis propio → conclusión aplicable",
      "Trazabilidad explícita entre objetivo, evidencia y cierre"
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema jurídico",
        "Marco normativo",
        "Análisis argumentativo",
        "Conclusión transferible",
        "Contratos",
        "Obligaciones"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Problema jurídico",
          "target": "Análisis argumentativo",
          "kind": "develops",
          "justification": "El análisis se construye desde un conflicto definido."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión deriva de fundamento jurídico verificable."
        },
        {
          "source": "Contratos",
          "target": "Obligaciones",
          "kind": "depends_on",
          "justification": "Ambas categorías forman el núcleo disciplinar de la materia."
        }
      ],
      "evidence": [
        "README y programa analítico de la materia",
        "Bibliografía institucional UnADM",
        "Reglas de calidad y normalización heredadas"
      ]
    },
    "reinforcement_log": [
      "Se preservan ejes editoriales comunes entre materias jurídicas.",
      "Se refuerzan controles de calidad y normalización transversal.",
      "No se eliminan reglas útiles; solo se deduplican."
    ]
  }
}
```