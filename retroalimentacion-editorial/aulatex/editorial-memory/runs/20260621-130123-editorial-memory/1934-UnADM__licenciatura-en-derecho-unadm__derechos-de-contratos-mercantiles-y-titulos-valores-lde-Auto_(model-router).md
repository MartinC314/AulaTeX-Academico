```json
{
  "summary": [
    "Se sincroniza ADN editorial transversal desde actividad filosofica hacia materia mercantil.",
    "Se preservan reglas institucionales UnADM y estructura argumentativa reusable.",
    "No se transfiere contenido tematico; solo abstracciones editoriales estables.",
    "Se refuerza normalizacion previa, calidad y grafo conceptual comun."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear todo entregable a Licenciatura en Derecho y a la materia destino.",
    "Cerrar siempre con postura academica propia y criterio juridico.",
    "Marcar como supuesto cualquier dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como nodo canonico.",
    "Estructurar actividades con: problema, conceptos o normas, evidencia, analisis propio y conclusion.",
    "Alinear formato final al producto solicitado en planeacion.",
    "Mantener consistencia entre README, programa, .tex y .bib."
  ],
  "activity_rules": [
    "Contextualizar con problema juridico concreto y delimitado.",
    "Sustentar afirmaciones con normas, doctrina o datos verificables.",
    "Distinguir evidencia citada de interpretacion propia.",
    "Evitar entregas meramente descriptivas."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar.",
    "Confirmar trazabilidad entre afirmaciones y fuentes.",
    "No permitir fuentes inventadas."
  ],
  "latex_rules": [
    "Mantener plantillas base y completar metadatos del curso.",
    "Usar español correcto con acentos consistentes.",
    "Mantener claves BibTeX estables.",
    "Corregir macros truncadas antes de compilar."
  ],
  "bibliography_rules": [
    "Usar el .bib local confirmado de la materia.",
    "Agregar solo fuentes realmente consultables.",
    "Conservar metadatos minimos completos.",
    "Distinguir bibliografia base de bibliografia por actividad."
  ],
  "propagation_hints": [
    "Propagar solo reglas generales y estables entre nodos transversales.",
    "Aplicar compresion union-dedupe sin regresion.",
    "Normalizar manualmente si se detecta salida no estructurada."
  ],
  "open_questions": [
    "Confirmar resolucion definitiva de incidencias de salida no JSON parseable.",
    "Definir plantillas finales de presentacion si difieren del reporte.",
    "Verificar resolucion total de placeholders de slug en README y programa."
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
        "Normalizacion estructurada obligatoria antes de propagar"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Asignaturas obligatorias con enfoque profesional",
        "Uso de carpeta canonica por materia"
      ]
    },
    "essence": [
      "Problema juridico como detonante.",
      "Marco conceptual y normativo verificable.",
      "Analisis propio diferenciado.",
      "Conclusion juridica transferible a la practica."
    ],
    "reason_for_being": [
      "Servir como cerebro editorial persistente y reusable.",
      "Garantizar coherencia academica transversal.",
      "Evitar regresiones y salidas no normalizadas."
    ],
    "style_markers": [
      "Apertura breve con problema.",
      "Secciones claras y ordenadas.",
      "Uso explicito de supuestos.",
      "Cierre con implicacion profesional."
    ],
    "argumentative_patterns": [
      "Problema -> marco normativo -> evidencia -> analisis propio -> conclusion.",
      "Afirmacion juridica siempre respaldada.",
      "Priorizar justificacion sobre descripcion."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
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
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere un problema delimitado."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion profesional exige base normativa."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "JSON parseable",
          "kind": "depends_on",
          "justification": "La propagacion segura requiere estructura valida."
        }
      ],
      "evidence": [
        "README y programa analitico de la materia.",
        ".bib local confirmado.",
        "Reglas institucionales UnADM heredadas."
      ]
    },
    "reinforcement_log": [
      "Se refuerza estrategia conservadora y progresiva.",
      "Se preservan reglas utiles sin eliminacion.",
      "Se consolida ADN editorial transversal estable."
    ]
  }
}
```