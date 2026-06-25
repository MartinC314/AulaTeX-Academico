```json
{
  "summary": [
    "Se sincroniza memoria editorial transversal desde una actividad hacia una materia no equivalente.",
    "Se preservan reglas validas del destino y se integran abstracciones editoriales estables del origen.",
    "Se refuerza patron comun UnADM: problema, fundamento, evidencia, analisis propio y conclusion juridica.",
    "La compresion aplicada es lossless por union y deduplicacion, sin regresion.",
    "Se mantiene alerta institucional por antecedentes de salida no parseable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino; marcar divergencias como [supuesto].",
    "No sobrescribir reglas validas previas; solo unir y deduplicar.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Usar README de la materia como canon estructural local.",
    "Alinear cada entrega a ejes reutilizables: problema, conceptos/norma, evidencia, analisis, conclusion.",
    "Separar claramente marco normativo/doctrinal de analisis propio.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Normalizar estructura antes de cualquier propagacion."
  ],
  "activity_rules": [
    "Definir objetivo puntual y problema juridico desde el inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura academica propia; evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Ajustar formato y alcance al producto solicitado por la planeacion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar.",
    "Confirmar que toda afirmacion tenga respaldo o marca de [supuesto].",
    "Verificar consistencia entre citas en texto y archivo .bib.",
    "Evitar regresion respecto de reglas utiles previas."
  ],
  "latex_rules": [
    "Mantener plantilla base de la materia; personalizar solo campos variables.",
    "Usar codificacion correcta en español y compilar sin errores.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Corregir rutas o nombres corruptos antes de compilar.",
    "Mantener claves BibTeX estables."
  ],
  "bibliography_rules": [
    "Usar el .bib local de la materia como fuente central.",
    "No inventar referencias; usar solo obras verificables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Verificar correspondencia entre citas y entradas BibTeX."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Validar JSON y estructura antes de propagacion recursiva.",
    "Propagar reglas generales de identidad, estructura y calidad a laterales compatibles.",
    "Evitar transferir redaccion literal o contenido tematico ajeno.",
    "Aplicar compresion union-dedupe sin perdida."
  ],
  "open_questions": [
    "Confirmar norma de citacion requerida para la materia destino [supuesto].",
    "Verificar si persiste alguna fuente provisional heredada no validada [supuesto].",
    "Confirmar consignas especificas de actividades para ajustar profundidad argumentativa.",
    "Definir figuras docentes pendientes cuando exista dato oficial."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico",
        "Claro",
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
        "Respeto a semestre y bloque oficiales del destino",
        "Uso del programa analitico como guia editorial"
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
      "Crear productos academicos juridicos verificables y reutilizables.",
      "Garantizar coherencia institucional y calidad transversal.",
      "Facilitar transferencia profesional del aprendizaje."
    ],
    "style_markers": [
      "Frases cortas y accionables",
      "Etiquetado explicito de [supuesto]",
      "Separacion visible entre marco y analisis",
      "Cierre con utilidad profesional"
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo",
      "Exponer marco normativo",
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
          "justification": "El analisis requiere una pregunta juridica delimitada."
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
        "README y programa analitico del destino",
        "Archivo .bib local verificado",
        "Reglas institucionales UnADM heredadas"
      ]
    },
    "reinforcement_log": [
      "Se refuerza patron editorial comun sin mezclar contenido tematico.",
      "Se mantiene identidad UnADM y control de calidad.",
      "Se consolida cerebro editorial minimo reconstruible."
    ]
  }
}
```