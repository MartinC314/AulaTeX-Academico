```json
{
  "summary": [
    "Se consolida memoria editorial transversal desde actividad a materia no equivalente.",
    "Se preservan reglas estables de identidad UnADM y estructura academica reusable.",
    "Se refuerza estrategia conservadora: no transferir contenido tematico de Filosofia del Derecho.",
    "Se sincronizan gates de calidad, normalizacion y grafo conceptual aplicables a Contratos Mercantiles."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables a Licenciatura en Derecho y a la materia destino.",
    "Usar tono juridico-formal con criterio academico propio.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como nodo canonico.",
    "Estructurar cada actividad con: problema, conceptos o normas, evidencia, analisis propio y conclusion.",
    "Alinear el producto final a la planeacion semanal.",
    "Mantener consistencia entre README, programa analitico, .tex y .bib."
  ],
  "activity_rules": [
    "Contextualizar cada actividad con un problema juridico concreto.",
    "Sustentar afirmaciones con normas, doctrina o datos verificables.",
    "Distinguir evidencia citada de interpretacion propia.",
    "Evitar entregas solo descriptivas.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar trazabilidad entre afirmaciones y fuentes.",
    "Evitar regresion de reglas utiles heredadas."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y completar metadatos.",
    "Usar español correcto con acentos consistentes en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Corregir macros truncadas o placeholders antes de compilar.",
    "Validar compilacion sin referencias rotas."
  ],
  "bibliography_rules": [
    "Usar el .bib local confirmado de la materia.",
    "Registrar solo fuentes realmente consultables.",
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Evitar transferir redaccion literal o contenido tematico especifico.",
    "Aplicar compresion union-dedupe lossless en cada ciclo.",
    "Mantener alerta institucional sobre normalizacion previa."
  ],
  "open_questions": [
    "Confirmar resolucion definitiva de incidencias de salida no JSON parseable.",
    "Verificar consignas especificas de actividades de la materia.",
    "Confirmar plantillas oficiales de presentacion si difieren del reporte.",
    "Validar nombres finales de archivos sin placeholders."
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
        "Normalizacion estructurada obligatoria"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Semestre 6, bloque 2",
        "Asignatura mercantil obligatoria con enfoque profesional"
      ]
    },
    "essence": [
      "Problema juridico como punto de partida",
      "Marco normativo y doctrinal verificable",
      "Analisis propio con postura academica",
      "Conclusion juridica transferible",
      "Identidad institucional UnADM"
    ],
    "reason_for_being": [
      "Orientar productos academicos claros, fundamentados y aplicables.",
      "Garantizar coherencia editorial transversal en la suite LaTeX.",
      "Asegurar transferencia profesional del analisis juridico."
    ],
    "style_markers": [
      "Apertura breve con encuadre del problema",
      "Secciones explicitas y ordenadas",
      "Uso explicito de supuestos cuando falte evidencia",
      "Cierre con implicacion practica"
    ],
    "argumentative_patterns": [
      "Problema -> marco normativo -> evidencia -> analisis propio -> conclusion",
      "Afirmaciones siempre respaldadas",
      "Priorizar justificacion sobre descripcion"
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico",
        "Marco normativo",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion estructurada",
        "JSON parseable"
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
          "justification": "La identidad institucional exige trazabilidad y citas verificables."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere un problema delimitado."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La aplicabilidad profesional depende del sustento normativo."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "JSON parseable",
          "kind": "depends_on",
          "justification": "La propagacion segura requiere estructura valida."
        }
      ],
      "evidence": [
        "README y programa analitico de la materia destino",
        ".bib local confirmado",
        "Reglas institucionales heredadas UnADM"
      ]
    },
    "reinforcement_log": [
      "Se preservan reglas estructurales estables.",
      "Se evita transferencia tematica indebida.",
      "Se refuerza normalizacion previa a propagacion.",
      "Se consolida cerebro editorial minimo para la materia destino."
    ]
  }
}
```