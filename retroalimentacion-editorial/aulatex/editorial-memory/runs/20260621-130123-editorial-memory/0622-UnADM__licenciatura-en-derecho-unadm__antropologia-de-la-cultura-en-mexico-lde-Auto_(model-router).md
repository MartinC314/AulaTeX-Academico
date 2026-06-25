```json
{
  "summary": [
    "Sincronización transversal consolidada entre actividad origen y materia destino.",
    "Se preservan reglas institucionales UnADM y ejes editoriales comunes.",
    "Transferencia conservadora basada en abstracciones estables, no contenido temático.",
    "Compresión lossless aplicada por unión y deduplicación.",
    "Se refuerza normalización estructurada y validación JSON antes de propagar."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripción a Licenciatura en Derecho.",
    "Respetar ubicación curricular local del destino; no importar metadatos del origen.",
    "Marcar como supuesto todo dato heredado no confirmado en la consigna local.",
    "Tratar fuentes heredadas interdisciplinares como provisionales."
  ],
  "structure_rules": [
    "Usar carpeta de materia como punto de entrada canónico.",
    "Alinear productos a ejes: problema, conceptos, evidencia, análisis propio y conclusión.",
    "Separar artefactos: reporte, presentación y bibliografía.",
    "Usar programa analítico como guía editorial reusable.",
    "Definir objetivo puntual antes del desarrollo."
  ],
  "activity_rules": [
    "Iniciar cada actividad con encuadre del problema social o jurídico.",
    "Incluir postura argumentada del estudiante.",
    "Distinguir evidencia, interpretación y opinión.",
    "Cerrar con conclusión transferible a la práctica jurídica.",
    "Evitar entregas meramente descriptivas."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de reutilizar.",
    "Confirmar consistencia entre citas en texto y archivo .bib.",
    "Marcar supuestos y fuentes provisionales explícitamente.",
    "No propagar reglas no validadas disciplinarmente."
  ],
  "latex_rules": [
    "Usar plantilla base de la materia como referencia inicial.",
    "Mantener codificación correcta en español.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens dinámicos antes de compilar.",
    "Compilar sin errores críticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes verificables.",
    "Priorizar fuentes institucionales UnADM.",
    "Registrar fuentes específicas por actividad en el .bib local.",
    "Conservar metadatos mínimos completos.",
    "Distinguir bibliografía base de bibliografía de actividad."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Evitar transferencia de contenido temático específico.",
    "Aplicar normalización manual si se detecta salida no estructurada.",
    "Registrar alertas de parseo como memoria reutilizable.",
    "Mantener estrategia progresiva y sin regresión."
  ],
  "open_questions": [
    "Confirmar rúbrica y formato específico de actividades en la materia destino.",
    "Validar estándar único de citación institucional.",
    "Confirmar alcance real de reglas heredadas interdisciplinares.",
    "Verificar nombre canónico definitivo del archivo .bib local."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico",
        "Claro y preciso",
        "Argumentativo con criterio propio"
      ],
      "institutional": [
        "Alineación explícita con UnADM",
        "Integridad académica y trazabilidad",
        "Normalización estructurada obligatoria"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Respeto a contexto curricular local",
        "No traslape de metadatos entre materias"
      ]
    },
    "essence": [
      "Problema como detonador académico",
      "Evidencia verificable",
      "Análisis propio",
      "Conclusión con valor profesional"
    ],
    "reason_for_being": [
      "Servir como cerebro editorial persistente y reusable",
      "Garantizar coherencia institucional transversal",
      "Facilitar transferencia sin pérdida de reglas útiles"
    ],
    "style_markers": [
      "Objetivo explícito",
      "Secciones funcionales",
      "Supuestos marcados",
      "Cierre argumentativo"
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> análisis -> conclusión",
      "Afirmación -> fuente -> interpretación propia",
      "Coherencia entre pregunta guía y cierre"
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalización estructurada",
        "Evidencia verificable",
        "Análisis propio",
        "Conclusión transferible"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalización estructurada",
          "target": "Propagación confiable",
          "kind": "supports",
          "justification": "Evita errores y regresiones editoriales."
        },
        {
          "source": "Evidencia verificable",
          "target": "Análisis propio",
          "kind": "supports",
          "justification": "Sustenta la postura académica."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión transferible",
          "kind": "develops",
          "justification": "Genera valor profesional aplicable."
        }
      ],
      "evidence": [
        "README y programa analítico de la materia destino",
        "Reglas institucionales UnADM consolidadas",
        "Gates de validación JSON heredados"
      ]
    },
    "reinforcement_log": [
      "Se preservaron reglas institucionales sin regresión.",
      "Se incorporaron abstracciones estables del origen.",
      "Se evitó transferencia temática indebida.",
      "Se reforzó validación JSON y normalización previa."
    ]
  }
}
```