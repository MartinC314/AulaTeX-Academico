```json
{
  "summary": [
    "Se sincroniza memoria editorial transversal desde actividad a materia sin transferir contenido tematico.",
    "Se preserva identidad UnADM y patron comun: problema, fundamento, evidencia, analisis propio y conclusion.",
    "Se refuerza normalizacion JSON, compresion union-dedupe y control de calidad institucional.",
    "Se consolida cerebro editorial minimo para Derecho a la Seguridad Social con reglas estables reutilizables."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Conservar trazabilidad de reglas heredadas provisionales.",
    "No sobrescribir reglas validas previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README de la materia como canon estructural.",
    "Alinear todo producto a cinco ejes: problema, conceptos/norma, evidencia, analisis, conclusion.",
    "Separar marco normativo/doctrinal de analisis propio.",
    "Cerrar con conclusion juridica transferible a la practica.",
    "Mantener consistencia entre reporte, presentacion y programa analitico."
  ],
  "activity_rules": [
    "Definir problema juridico y objetivo antes del desarrollo.",
    "Sustentar afirmaciones con fuentes verificables o marcar [supuesto].",
    "Incluir postura academica propia, no solo descripcion.",
    "Ajustar formato y alcance al producto solicitado en la planeacion.",
    "Relacionar cada actividad con el campo de seguridad social cuando aplique."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar.",
    "Confirmar correspondencia entre consigna, desarrollo y conclusion.",
    "Verificar que toda cita tenga entrada en el .bib local.",
    "Evitar regresion respecto de reglas utiles previas."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener metadatos institucionales consistentes en todos los .tex.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Corregir rutas o nombres corruptos antes de compilar."
  ],
  "bibliography_rules": [
    "Usar el .bib local de la materia como fuente central.",
    "Agregar solo referencias verificables y pertinentes a la actividad.",
    "No inventar fuentes; marcar faltantes como pendientes.",
    "Mantener metadatos minimos completos en cada entrada.",
    "Validar coherencia entre citas en texto y BibTeX."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Evitar transferir redaccion literal o contenido tematico de origen.",
    "Propagar reglas generales de identidad, estructura y calidad.",
    "Requiere normalizacion manual si se detectan salidas no estructuradas.",
    "Aplicar compresion lossless por union-dedupe sin recorte."
  ],
  "open_questions": [
    "Confirmar norma de citacion juridica requerida por la materia [supuesto].",
    "Definir figura docente en plantillas cuando exista dato oficial.",
    "Verificar si existen consignas locales que ajusten la estructura canonica.",
    "Confirmar vigencia de fuentes provisionales heredadas [supuesto]."
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
        "Integridad academica y citas verificables",
        "Normalizacion estructurada obligatoria antes de propagar"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Materia: Derecho a la Seguridad Social",
        "Respeto a semestre y bloque oficiales del destino"
      ]
    },
    "essence": [
      "Problema juridico delimitado",
      "Marco normativo y doctrinal verificable",
      "Evidencia pertinente",
      "Analisis propio sustentado",
      "Conclusion juridica transferible"
    ],
    "reason_for_being": [
      "Convertir consignas en productos juridicos verificables y reutilizables.",
      "Garantizar coherencia editorial transversal entre materias.",
      "Preservar identidad institucional y calidad academica."
    ],
    "style_markers": [
      "Frases cortas y accionables",
      "Separacion visible entre marco y analisis",
      "Etiquetado explicito de [supuesto]",
      "Cierre con utilidad profesional"
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo",
      "Exponer fundamento normativo",
      "Contrastar evidencia",
      "Fijar postura propia",
      "Concluir con implicacion practica"
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema juridico",
        "Marco normativo",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "JSON parseable",
        "Compresion union-dedupe"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024",
        "cpeum2026",
        "lss2026",
        "lissste2026"
      ],
      "relations": [
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere una pregunta juridica clara."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida depende de fundamento legal verificable."
        },
        {
          "source": "JSON parseable",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay reutilizacion segura."
        }
      ],
      "evidence": [
        "README y programa analitico del destino definen estructura y proposito.",
        "Archivo .bib local confirma base normativa e institucional.",
        "Alertas institucionales previas justifican gates de normalizacion."
      ]
    },
    "reinforcement_log": [
      "Se refuerza patron editorial comun sin mezclar contenido tematico.",
      "Se preservan reglas locales del destino y ADN institucional.",
      "Se consolida sincronizacion transversal conservadora en ciclo 17."
    ]
  }
}
```