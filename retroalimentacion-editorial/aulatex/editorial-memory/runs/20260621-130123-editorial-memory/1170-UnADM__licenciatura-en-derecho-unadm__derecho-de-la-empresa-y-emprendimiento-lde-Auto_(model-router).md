```json
{
  "summary": [
    "Se consolida un cerebro editorial transversal UnADM entre actividad origen y materia destino.",
    "Se preserva el marco reusable: problema, conceptos, evidencia, análisis propio y conclusión.",
    "Se evita transferencia doctrinal específica por no equivalencia disciplinar.",
    "Se refuerza normalización estructurada y control de supuestos como reglas núcleo.",
    "Se crea cerebro editorial mínimo para materia destino con vacíos locales abiertos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial de la materia destino en todos los artefactos.",
    "Usar Licenciatura en Derecho como programa académico.",
    "Marcar como supuesto todo dato no confirmado por archivo local.",
    "Tratar fuentes heredadas no verificadas como provisionales."
  ],
  "structure_rules": [
    "Usar README de materia como punto de entrada canónico.",
    "Alinear entregables al esquema: problema, conceptos, evidencia, análisis propio, conclusión.",
    "Separar secciones de forma explícita y consistente.",
    "Cerrar siempre con conclusión jurídica transferible a la práctica.",
    "No reutilizar redacción literal entre nodos no equivalentes."
  ],
  "activity_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Identificar el problema jurídico o social que activa la actividad.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Sustentar afirmaciones con fuentes verificables."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de reutilizar memoria.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "No eliminar reglas útiles previas durante unión-dedupe.",
    "Corregir tokens de plantilla sin expandir antes de generar entregables."
  ],
  "latex_rules": [
    "Mantener compilación sin errores críticos.",
    "Usar codificación correcta en español.",
    "Mantener consistencia entre macros de curso y licenciatura.",
    "Resolver rutas y tokens Slug antes de compilar.",
    "No introducir comandos no estándar sin justificación editorial."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Registrar solo fuentes verificables en el .bib local.",
    "Mantener claves BibTeX estables y sin duplicados.",
    "Distinguir bibliografía base institucional de bibliografía específica.",
    "No citar fuentes no registradas en el .bib."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables entre nodos transversales.",
    "Evitar transferencia de contenido doctrinal específico.",
    "Exigir normalización manual en ciclos tempranos.",
    "Propagar reglas de identidad, estructura y calidad cuando falte consigna local.",
    "Mantener estrategia progresiva y conservadora."
  ],
  "open_questions": [
    "Confirmar consignas específicas de actividades en la materia destino.",
    "Confirmar rúbricas de evaluación locales.",
    "Confirmar archivo .bib canónico final de la materia.",
    "Confirmar autor por actividad en plantillas.",
    "Confirmar corrección definitiva de tokens Slug en README y programa analítico."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico",
        "Claro",
        "Argumentativo"
      ],
      "institutional": [
        "Alineación explícita con UnADM",
        "Integridad académica",
        "Trazabilidad bibliográfica"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Respeto al contexto curricular local",
        "Enfoque en transferencia profesional"
      ]
    },
    "essence": [
      "Problema jurídico como punto de partida",
      "Análisis propio con respaldo",
      "Evidencia verificable",
      "Conclusión jurídica transferible",
      "Control explícito de supuestos"
    ],
    "reason_for_being": [
      "Servir como cerebro editorial persistente reutilizable",
      "Garantizar coherencia académica transversal",
      "Evitar regresiones editoriales entre ciclos",
      "Facilitar producción académica en LaTeX bajo UnADM"
    ],
    "style_markers": [
      "Frases cortas y accionables",
      "Supuestos marcados",
      "Sin afirmaciones sin fuente",
      "Cierre aplicado a la práctica profesional"
    ],
    "argumentative_patterns": [
      "Problema → conceptos → evidencia → análisis propio → conclusión",
      "Marco normativo como soporte del criterio personal",
      "Coherencia entre pregunta guía y cierre"
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
          "justification": "Sin estructura válida no hay reutilización segura."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión requiere respaldo documental."
        },
        {
          "source": "Control de supuestos",
          "target": "Integridad argumentativa",
          "kind": "supports",
          "justification": "Diferencia hechos confirmados de inferencias."
        }
      ],
      "evidence": [
        "README y programa analítico locales",
        "Reglas institucionales UnADM consolidadas",
        "Historial de normalización por salidas no estructuradas"
      ]
    },
    "reinforcement_log": [
      "Se preservan reglas institucionales previas sin eliminación.",
      "Se refuerza el marco reusable transversal.",
      "Se evita transferencia indebida entre disciplinas.",
      "Se mantiene compresión lossless por deduplicación."
    ]
  }
}
```