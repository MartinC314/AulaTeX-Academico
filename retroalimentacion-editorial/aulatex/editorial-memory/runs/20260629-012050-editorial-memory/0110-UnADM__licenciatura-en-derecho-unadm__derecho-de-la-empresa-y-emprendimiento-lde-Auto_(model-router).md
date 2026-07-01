```json
{
  "summary": [
    "Se consolida ADN editorial transversal desde actividad de Filosofía del Derecho hacia la materia Derecho de la empresa y emprendimiento.",
    "Se preservan ejes editoriales estables: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "La transferencia es conservadora y abstracta; no se propaga redacción ni contenido temático específico.",
    "Se refuerza la normalización estructurada como condición previa a cualquier propagación.",
    "Se establece un cerebro editorial mínimo del destino con vacíos locales explícitos como supuestos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, metadatos y formato.",
    "Usar siempre el nombre oficial de la materia destino.",
    "Vincular toda entrega a la Licenciatura en Derecho.",
    "Marcar como supuesto cualquier dato no confirmado por archivos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales."
  ],
  "structure_rules": [
    "Usar la carpeta de la materia como punto de entrada canónico.",
    "Alinear toda actividad al flujo: problema, conceptos, producto, análisis propio y conclusión.",
    "Separar claramente marco conceptual o normativo del análisis propio.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Alinear el formato final al producto solicitado en la planeación semanal."
  ],
  "activity_rules": [
    "Definir objetivo puntual de cada actividad antes del desarrollo.",
    "Identificar explícitamente el problema jurídico o social.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y citas explícitas.",
    "Verificar coherencia entre consigna, desarrollo y conclusión."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Normalizar manualmente cualquier salida no estructurada antes de reutilizar.",
    "No eliminar reglas útiles previas durante fusión por deduplicación.",
    "Validar correspondencia entre citas en texto y archivo .bib.",
    "No propagar datos curriculares locales sin confirmación documental."
  ],
  "latex_rules": [
    "Mantener consistencia de macros institucionales y de curso.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Usar codificación correcta en español en .tex y .bib.",
    "Actualizar títulos y subtítulos por actividad.",
    "Resolver tokens de plantilla sin expandir antes de compilar."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes consultables.",
    "Priorizar fuentes institucionales UnADM y documentos jurídicos verificables.",
    "Mantener claves BibTeX estables y sin duplicados.",
    "Registrar fuentes específicas de cada actividad en el .bib local.",
    "Distinguir bibliografía base de bibliografía específica de actividad."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Evitar transferencia de redacción literal o ejemplos temáticos.",
    "Propagar transversalmente solo después de validar estructura y JSON.",
    "Mantener estrategia progresiva y conservadora en ciclos posteriores.",
    "Reforzar alertas sobre salidas no estructuradas en nodos vecinos."
  ],
  "open_questions": [
    "Confirmar consignas específicas de las actividades de la materia destino.",
    "Confirmar rúbricas de evaluación locales.",
    "Confirmar fuentes obligatorias por semana en la materia destino.",
    "Confirmar nombre canónico final del archivo .bib de la materia.",
    "Confirmar si el autor en plantilla se parametriza por actividad."
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
        "Integridad académica y trazabilidad de fuentes",
        "Normalización estructurada obligatoria"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Materia aplicada con enfoque teoría–práctica",
        "Respeto al contexto curricular local confirmado"
      ]
    },
    "essence": [
      "Problema jurídico como detonante del análisis",
      "Uso disciplinado de conceptos y normas",
      "Análisis propio sustentado en evidencia",
      "Conclusión jurídica con transferencia profesional",
      "Identidad institucional consistente"
    ],
    "reason_for_being": [
      "Garantizar coherencia editorial transversal entre materias",
      "Evitar propagación de ruido estructural o datos no verificados",
      "Facilitar reutilización segura de patrones editoriales",
      "Elevar calidad argumentativa de los productos académicos"
    ],
    "style_markers": [
      "Frases directas y accionables",
      "Uso explícito de supuestos cuando falta información",
      "Separación clara entre fuente y postura propia",
      "Cierre con aplicación práctica"
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión",
      "Afirmación -> evidencia -> interpretación -> postura",
      "Consigna -> desarrollo focalizado -> verificación de cumplimiento"
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalización estructurada",
        "Problema jurídico",
        "Evidencia verificable",
        "Análisis propio",
        "Conclusión jurídica transferible"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalización estructurada",
          "target": "Propagación segura",
          "kind": "supports",
          "justification": "Evita heredar salidas no estructuradas o ruido editorial."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La validez práctica depende del respaldo documental."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Consistencia transversal",
          "kind": "develops",
          "justification": "Unifica criterios de calidad entre materias."
        }
      ],
      "evidence": [
        "Programa analítico de la materia destino",
        "README institucional de la materia",
        "Memoria editorial consolidada del origen"
      ]
    },
    "reinforcement_log": [
      "Se preservaron reglas institucionales sin regresión.",
      "Se deduplicaron ejes editoriales comunes entre origen y destino.",
      "Se reforzó la alerta de no propagar salidas no estructuradas.",
      "Se consolidó un cerebro editorial mínimo con supuestos explícitos."
    ]
  }
}
```