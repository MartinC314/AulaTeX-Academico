```json
{
  "summary": [
    "Se consolida cerebro editorial transversal UnADM entre actividad origen y materia destino.",
    "Se preserva marco reusable: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "No se transfiere contenido doctrinal específico por no equivalencia disciplinar.",
    "Se refuerzan reglas de normalización, control de supuestos y calidad institucional.",
    "Se crea cerebro editorial mínimo estable para la materia destino."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial de la materia destino en todos los artefactos.",
    "Respetar contexto curricular local confirmado del destino.",
    "Marcar como supuesto todo dato no confirmado por archivos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales."
  ],
  "structure_rules": [
    "Usar carpeta de materia como punto de entrada canónico.",
    "Alinear entregables al esquema reusable: problema, conceptos, evidencia, análisis propio, conclusión.",
    "Separar claramente secciones editoriales; evitar mezclas implícitas.",
    "Cerrar siempre con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Identificar explícitamente el problema jurídico o social.",
    "Incluir postura argumentada propia; evitar solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Conectar la conclusión con aplicación práctica en contexto empresarial."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Normalizar manualmente respuestas no estructuradas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin fuente o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "No eliminar reglas útiles previas durante fusión por deduplicación."
  ],
  "latex_rules": [
    "Mantener consistencia de metadatos institucionales en macros LaTeX.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver tokens de plantilla sin expandir antes de compilar.",
    "Actualizar títulos y subtítulos por actividad concreta.",
    "Verificar cierre correcto de entornos y tablas."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables.",
    "Priorizar fuentes institucionales UnADM y normatividad aplicable.",
    "Registrar fuentes específicas de cada actividad en el .bib de la materia.",
    "Mantener claves BibTeX estables y sin duplicados.",
    "Distinguir bibliografía base de bibliografía específica."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Evitar transferir redacción literal o doctrina específica.",
    "Propagar recursivamente solo tras validación de JSON y estructura.",
    "Alertar sobre placeholders y tokens Slug a nodos con plantillas similares.",
    "Requerir normalización manual en ciclos tempranos."
  ],
  "open_questions": [
    "Confirmar consignas específicas de actividades en la materia destino.",
    "Confirmar rúbrica de evaluación local para ajustar profundidad argumentativa.",
    "Confirmar autoría final en plantillas por actividad.",
    "Confirmar nombre canónico definitivo del archivo .bib local."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico",
        "Claro",
        "Argumentativo con criterio propio"
      ],
      "institutional": [
        "Alineación explícita con UnADM",
        "Integridad académica",
        "Trazabilidad bibliográfica"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Semestre avanzado",
        "Enfoque de transferencia profesional"
      ]
    },
    "essence": [
      "Identidad institucional UnADM",
      "Normalización estructurada",
      "Problema jurídico",
      "Evidencia verificable",
      "Análisis propio",
      "Conclusión jurídica transferible",
      "Control de supuestos"
    ],
    "reason_for_being": [
      "Garantizar coherencia editorial transversal en la suite académica LaTeX.",
      "Asegurar productos académicos con fundamento jurídico y transferencia práctica.",
      "Evitar regresiones editoriales entre nodos no equivalentes."
    ],
    "style_markers": [
      "Frases cortas y precisas",
      "Supuestos explícitos",
      "Sin afirmaciones sin fuente",
      "Cierre con aplicación práctica"
    ],
    "argumentative_patterns": [
      "Problema → conceptos → evidencia → análisis propio → conclusión",
      "Marco normativo como soporte del criterio personal",
      "Consistencia entre pregunta guía y cierre"
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalización estructurada",
        "Problema jurídico",
        "Evidencia verificable",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "Control de supuestos"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura válida no se propaga memoria de forma segura."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión requiere respaldo normativo y documental."
        },
        {
          "source": "Control de supuestos",
          "target": "Integridad argumentativa",
          "kind": "supports",
          "justification": "Diferencia hechos confirmados de inferencias provisionales."
        }
      ],
      "evidence": [
        "README y programa analítico locales",
        "Bibliografía institucional UnADM",
        "Reglas editoriales consolidadas por deduplicación"
      ]
    },
    "reinforcement_log": [
      "Se preservan reglas institucionales UnADM.",
      "Se refuerza el marco reusable transversal.",
      "Se evita transferencia doctrinal indebida.",
      "Se mantiene estrategia progresiva y conservadora."
    ]
  }
}
```