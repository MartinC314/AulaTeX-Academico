```json
{
  "summary": [
    "Se sincroniza ADN editorial estable desde una actividad teórica hacia una materia aplicada.",
    "Se preservan reglas institucionales UnADM y ejes editoriales comunes.",
    "La transferencia es transversal, conservadora y sin redacción literal.",
    "Se refuerza normalización estructurada y control de calidad.",
    "Se consolida un cerebro editorial mínimo para la materia destino."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en todo entregable.",
    "Usar nombre oficial y contexto curricular local confirmado.",
    "Marcar como supuesto cualquier dato no visible en archivos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales.",
    "No propagar datos curriculares específicos fuera del nodo destino."
  ],
  "structure_rules": [
    "Usar README de materia como punto de entrada canónico.",
    "Alinear entregables al eje: problema, conceptos, evidencia, análisis, conclusión.",
    "Separar secciones de forma explícita y reutilizable.",
    "Cerrar con conclusión jurídica transferible a la práctica.",
    "Conservar correspondencia entre .tex, presentación y .bib."
  ],
  "activity_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Identificar problema jurídico o social relevante.",
    "Incluir análisis propio; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables.",
    "Conectar conclusión con aplicación profesional."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Normalizar manualmente salidas no estructuradas en ciclo 1.",
    "Verificar coherencia entre consigna, desarrollo y conclusión.",
    "Confirmar trazabilidad entre citas en texto y .bib.",
    "No eliminar reglas útiles previas durante fusión."
  ],
  "latex_rules": [
    "Mantener codificación correcta en español.",
    "Usar plantillas institucionales sin comandos no estándar.",
    "Verificar compilación sin errores ni referencias rotas.",
    "Resolver tokens de plantilla sin expandir antes de compilar.",
    "Actualizar títulos y metadatos por actividad."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Registrar solo fuentes realmente consultables.",
    "Priorizar fuentes institucionales UnADM.",
    "Mantener claves BibTeX estables y únicas.",
    "Distinguir bibliografía base de bibliografía específica."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables.",
    "Evitar transferencia de redacción literal.",
    "Exigir validación estructural antes de propagar recursivamente.",
    "Propagar alertas de calidad a nodos con plantillas similares.",
    "Mantener estrategia progresiva y conservadora."
  ],
  "open_questions": [
    "Confirmar consignas específicas de actividades de la materia destino.",
    "Confirmar rúbricas locales de evaluación.",
    "Confirmar fuentes obligatorias por semana.",
    "Confirmar parametrización definitiva de autor por actividad."
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
        "Integridad académica y trazabilidad",
        "Normalización estructurada obligatoria"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Materia aplicada con enfoque teoría–práctica",
        "Respeto al contexto curricular local"
      ]
    },
    "essence": [
      "Problema jurídico como punto de partida",
      "Conceptos y marco normativo pertinentes",
      "Evidencia verificable",
      "Análisis propio del estudiante",
      "Conclusión jurídica transferible"
    ],
    "reason_for_being": [
      "Unificar criterios editoriales entre materias de la Licenciatura en Derecho",
      "Garantizar calidad, coherencia y transferencia profesional",
      "Permitir reutilización estructural sin pérdida de identidad"
    ],
    "style_markers": [
      "Frases cortas y accionables",
      "Uso explícito de supuestos",
      "Cierre con aplicación práctica",
      "Estructura visible y consistente"
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión",
      "Afirmación -> evidencia -> interpretación -> postura",
      "Consigna -> desarrollo focalizado -> verificación"
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
          "justification": "Evita heredar salidas no verificables."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "Sustenta la validez práctica del cierre."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Consistencia transversal",
          "kind": "develops",
          "justification": "Unifica tono y criterios entre nodos."
        }
      ],
      "evidence": [
        "README y programa analítico de la materia destino",
        "Bibliografía institucional UnADM",
        "Reglas editoriales consolidadas del origen"
      ]
    },
    "reinforcement_log": [
      "Se preservan ejes editoriales comunes.",
      "Se refuerza control de calidad y normalización.",
      "Se evita propagación de ruido estructural.",
      "Se consolida identidad UnADM transversal."
    ]
  }
}
```