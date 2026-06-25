```json
{
  "summary": [
    "Se sincroniza ADN editorial transversal desde actividad filosofica a materia aplicada.",
    "Se preservan reglas institucionales UnADM y normalizacion estructurada.",
    "Se refuerza marco reusable: problema, conceptos, evidencia, analisis propio y conclusion.",
    "No se transfiere doctrina especifica por no equivalencia disciplinar.",
    "Se consolida cerebro editorial minimo para materia destino."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar Licenciatura en Derecho como programa academico.",
    "Marcar como supuesto cualquier dato no confirmado por archivos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales."
  ],
  "structure_rules": [
    "Usar README de materia como punto de entrada canonico.",
    "Alinear entregables al esquema: problema, conceptos, evidencia, analisis propio y conclusion.",
    "Separar claramente marco conceptual, analisis y cierre.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Identificar problema juridico o social relevante para la materia.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar memoria.",
    "Confirmar que no existan afirmaciones sin fuente o sin marca de supuesto.",
    "No eliminar reglas utiles previas durante fusion por union-dedupe."
  ],
  "latex_rules": [
    "Mantener compilacion sin errores criticos.",
    "Verificar resolucion de tokens Slug sin expandir.",
    "Usar codificacion correcta en español.",
    "Mantener consistencia entre .tex, presentacion y .bib."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo fuentes verificables y consultables.",
    "Mantener claves BibTeX estables.",
    "Distinguir bibliografia base de bibliografia especifica de actividad."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables.",
    "Evitar transferir contenido doctrinal especifico entre materias no equivalentes.",
    "Exigir normalizacion manual en ciclos con antecedente de salida no estructurada.",
    "Propagar recursivamente solo tras validacion de JSON y estructura."
  ],
  "open_questions": [
    "Confirmar consignas especificas de actividades de la materia destino.",
    "Confirmar rubricas locales de evaluacion.",
    "Confirmar fuentes obligatorias por semana."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico",
        "Claro y juridicamente preciso",
        "Argumentativo con criterio propio"
      ],
      "institutional": [
        "Alineacion explicita con UnADM",
        "Integridad academica",
        "Trazabilidad bibliografica"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Materia en semestre avanzado",
        "Enfoque de transferencia profesional"
      ]
    },
    "essence": [
      "Normalizacion estructurada",
      "Problema juridico como eje",
      "Analisis propio sustentado",
      "Conclusion juridica transferible"
    ],
    "reason_for_being": [
      "Asegurar coherencia editorial entre materias de la licenciatura.",
      "Facilitar reutilizacion de estructura sin perder contexto disciplinar.",
      "Garantizar calidad academica y trazabilidad."
    ],
    "style_markers": [
      "Frases cortas y accionables",
      "Supuestos explicitamente marcados",
      "Cierre orientado a practica profesional"
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis propio -> conclusion",
      "Marco normativo como soporte del criterio personal",
      "Consistencia entre pregunta guia y conclusion"
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Problema juridico",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Control de supuestos"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion segura",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay sincronizacion confiable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion requiere respaldo documental."
        },
        {
          "source": "Control de supuestos",
          "target": "Integridad argumentativa",
          "kind": "supports",
          "justification": "Diferencia hechos confirmados de inferencias."
        }
      ],
      "evidence": [
        "README y programa analitico locales.",
        "Reglas institucionales UnADM heredadas.",
        "Bibliografia base institucional."
      ]
    },
    "reinforcement_log": [
      "Se refuerza marco reusable transversal.",
      "Se evita regresion y perdida de reglas previas.",
      "Se consolida cerebro editorial minimo en destino."
    ]
  }
}
```