```json
{
  "summary": [
    "Se sincroniza ADN editorial transversal desde actividad fundacional hacia materia mercantil.",
    "Se preservan reglas institucionales UnADM y estructura academica reusable.",
    "Se refuerza normalizacion previa y control de calidad para propagacion recursiva.",
    "No se transfiere contenido tematico especifico; solo abstracciones editoriales estables."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en todo entregable.",
    "Alinear tono juridico-formal con postura academica propia.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Etiquetar fuentes heredadas no verificadas como provisionales."
  ],
  "structure_rules": [
    "Usar carpeta de materia como nodo canonico.",
    "Estructura minima: problema, conceptos o normas, evidencia, analisis propio y conclusion transferible.",
    "Mantener consistencia entre README, programa, .tex y .bib.",
    "Definir objetivo puntual antes del desarrollo."
  ],
  "activity_rules": [
    "Contextualizar con problema juridico concreto.",
    "Sustentar afirmaciones con fuentes verificables.",
    "Distinguir evidencia citada de interpretacion propia.",
    "Evitar entregas solo descriptivas.",
    "Cerrar con conclusion aplicable a la practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizar.",
    "Verificar trazabilidad entre afirmaciones y fuentes.",
    "Validar estructura minima completa antes de propagar."
  ],
  "latex_rules": [
    "Usar español correcto con acentos consistentes.",
    "Mantener claves BibTeX estables.",
    "Corregir macros truncadas antes de compilar.",
    "Validar compilacion sin errores criticos."
  ],
  "bibliography_rules": [
    "Usar .bib local de la materia como base.",
    "No inventar referencias.",
    "Conservar metadatos minimos completos.",
    "Distinguir bibliografia base de bibliografia por actividad."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables.",
    "Evitar transferencia de redaccion literal.",
    "Aplicar compresion union-dedupe sin perdida.",
    "Mantener estrategia conservadora en nodos no equivalentes."
  ],
  "open_questions": [
    "Confirmar resolucion definitiva de salidas no JSON parseable.",
    "Definir si existen plantillas adicionales por actividad.",
    "Verificar si todos los placeholders de slug fueron resueltos."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico",
        "Juridicamente preciso",
        "Argumentativo con criterio propio"
      ],
      "institutional": [
        "Alineacion explicita con UnADM",
        "Integridad academica con citas verificables",
        "Carpeta canonica como punto de entrada"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Semestre 6, bloque 2, obligatoria",
        "Materia mercantil"
      ]
    },
    "essence": [
      "Problema juridico como detonante.",
      "Marco normativo o doctrinal verificable.",
      "Analisis propio del estudiante.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Servir como cerebro editorial persistente y transversal.",
      "Garantizar coherencia institucional y calidad academica.",
      "Facilitar reutilizacion segura entre nodos."
    ],
    "style_markers": [
      "Apertura breve con problema.",
      "Secciones claras y ordenadas.",
      "Uso explicito de supuestos.",
      "Cierre con implicacion profesional."
    ],
    "argumentative_patterns": [
      "Problema -> marco normativo -> evidencia -> postura propia -> conclusion.",
      "Cada afirmacion requiere respaldo.",
      "Priorizar analisis sobre descripcion."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Problema juridico",
        "Marco normativo",
        "Analisis propio",
        "Conclusion transferible"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La identidad exige citas y trazabilidad."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin problema no hay argumentacion."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "El cierre profesional requiere base normativa."
        }
      ],
      "evidence": [
        "README y programa analitico de la materia.",
        ".bib local institucional."
      ]
    },
    "reinforcement_log": [
      "Se preservan reglas utiles previas sin regresion.",
      "Se refuerza control de calidad previo a propagacion.",
      "Se consolida identidad UnADM como eje transversal."
    ]
  }
}
```