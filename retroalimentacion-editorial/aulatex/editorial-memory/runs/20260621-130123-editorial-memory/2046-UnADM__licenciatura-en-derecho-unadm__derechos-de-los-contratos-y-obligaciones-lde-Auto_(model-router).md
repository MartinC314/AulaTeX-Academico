```json
{
  "summary": [
    "Se refuerza el cerebro editorial de la materia con abstracciones estables heredadas transversalmente.",
    "Se consolida el modelo de cinco ejes como ADN común entre materias jurídicas UnADM.",
    "Se preserva normalización estricta y deduplicación lossless sin regresión.",
    "Se refuerza la identidad UnADM con enfoque contractual aplicado.",
    "Se mantienen gates de calidad y controles LaTeX/bibliográficos reutilizables."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares confirmados de la materia; marcar [supuesto] lo no visible.",
    "Conservar enfoque jurídico aplicado a contratos y obligaciones.",
    "Tratar herencias Codex o GPT-Pro como provisionales hasta validación local.",
    "Usar la carpeta de materia como punto de entrada canónico."
  ],
  "structure_rules": [
    "Aplicar el modelo transversal de cinco ejes en toda entrega.",
    "Iniciar con encuadre breve del problema jurídico.",
    "Separar secciones: conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Alinear el producto al solicitado por la planeación semanal.",
    "Mantener trazabilidad entre objetivo, evidencia, argumento y conclusión."
  ],
  "activity_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Explicitar postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "No trasladar contenido de otras materias sin adecuación contractual."
  ],
  "quality_gates": [
    "Bloquear persistencia o propagación si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Validar coherencia entre objetivo, desarrollo y cierre.",
    "Confirmar trazabilidad entre citas en texto y archivo .bib local.",
    "No degradar reglas útiles previas durante unión-dedupe."
  ],
  "latex_rules": [
    "Conservar plantilla LaTeX base y metadatos institucionales completos.",
    "Usar español académico claro y terminología jurídica precisa.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver placeholders tipo $(@{...}.Slug) antes de compilar.",
    "Compilar sin errores críticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Usar el .bib canónico local de la materia.",
    "Distinguir bibliografía base de fuentes específicas por actividad.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales verificables.",
    "No inventar referencias; marcar [supuesto] si falta disponibilidad.",
    "Conservar metadatos mínimos completos en cada entrada."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo abstracciones editoriales estables.",
    "Evitar transferir redacción literal entre nodos no equivalentes.",
    "Validar compatibilidad disciplinar antes de propagación lateral.",
    "Reutilizar gates de calidad y estructura transversal en actividades hijas.",
    "Aplicar normalización manual en ciclos tempranos si se detecta herencia no estructurada."
  ],
  "open_questions": [
    "Confirmar rúbrica de evaluación específica por actividad.",
    "Definir estilo de citación jurídica obligatorio en la materia.",
    "Confirmar alcance de fuentes: federales, locales o mixtas según actividad.",
    "Precisar formato mínimo esperado de la conclusión jurídica."
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
        "Carpeta de materia como entrada canónica"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Semestre 4, bloque 1, obligatoria, 8 créditos",
        "Enfoque en contratos y obligaciones"
      ]
    },
    "essence": [
      "Modelo transversal de cinco ejes editoriales.",
      "Análisis jurídico propio sustentado.",
      "Transferencia profesional del razonamiento jurídico.",
      "Normalización estructurada como requisito previo."
    ],
    "reason_for_being": [
      "Asegurar coherencia editorial entre materias jurídicas UnADM.",
      "Facilitar productos académicos claros, verificables y transferibles.",
      "Evitar contaminación por herencias no estructuradas."
    ],
    "style_markers": [
      "Supuestos siempre etiquetados como [supuesto].",
      "Secciones funcionales y trazables.",
      "Cierre jurídico operativo y aplicado."
    ],
    "argumentative_patterns": [
      "Problema delimitado.",
      "Marco conceptual y normativo pertinente.",
      "Análisis propio con evidencia.",
      "Conclusión jurídica aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Contratos",
        "Obligaciones",
        "Modelo de cinco ejes",
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
          "source": "Modelo de cinco ejes",
          "target": "Análisis jurídico propio",
          "kind": "supports",
          "justification": "Estructura el razonamiento académico."
        },
        {
          "source": "Análisis jurídico propio",
          "target": "Conclusión transferible",
          "kind": "develops",
          "justification": "La conclusión surge del razonamiento sustentado."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "supports",
          "justification": "Evita errores y contaminación editorial."
        }
      ],
      "evidence": [
        "README y programa analítico de la materia.",
        "Bibliografía institucional UnADM.",
        "Reglas heredadas validadas sin regresión."
      ]
    },
    "reinforcement_log": [
      "Se preservan reglas útiles previas mediante unión-dedupe.",
      "Se refuerza identidad UnADM y modelo transversal.",
      "Se agregan mejoras verificables sin eliminar controles existentes."
    ]
  }
}
```