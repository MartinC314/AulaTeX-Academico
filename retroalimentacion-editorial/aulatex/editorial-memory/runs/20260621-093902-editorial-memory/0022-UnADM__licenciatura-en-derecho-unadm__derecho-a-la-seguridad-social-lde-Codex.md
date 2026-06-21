{
  "summary": [
    "Se mantiene identidad UnADM y canon local de materia.",
    "Se refuerza sincronizacion transversal con reglas estables no tematicas.",
    "Se conserva compresion lossless por union-dedupe sin regresion.",
    "Se mantiene alerta por salidas no parseables heredadas y normalizacion manual.",
    "Se preserva patron editorial comun: problema, fundamento, evidencia, analisis y conclusion juridica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "No sobrescribir reglas validas previas; solo unir y deduplicar.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Tomar README y programa analitico como canon estructural local.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Organizar en: conceptos/marco normativo, analisis propio y cierre.",
    "Alinear formato final al producto solicitado en planeacion semanal.",
    "Mantener consistencia entre reporte, presentacion y bibliografia."
  ],
  "activity_rules": [
    "Delimitar problema y pregunta guia al inicio.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas.",
    "Incluir postura argumentada del estudiante.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de propagar recursivamente.",
    "Confirmar soporte verificable o marca [supuesto] en afirmaciones relevantes.",
    "Verificar correspondencia entre consigna, desarrollo y producto final.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Conservar plantilla base local y personalizar solo campos variables.",
    "Mantener codificacion y acentos correctos en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion tecnica.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Normalizar rutas o nombres con marcadores corruptos antes de compilar.",
    "No copiar redaccion literal entre materias; reutilizar solo estructura."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente central local.",
    "Priorizar fuentes institucionales y juridicas verificables.",
    "No inventar referencias; registrar solo fuentes consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente/URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Verificar que toda cita LaTeX tenga su entrada BibTeX."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo abstracciones editoriales estables.",
    "No transferir contenido tematico especifico de Filosofia del Derecho.",
    "Propagar reglas de identidad, estructura reusable y quality gates.",
    "Mantener reglas curriculares especificas solo dentro de la materia destino.",
    "Aplicar estrategia progresiva y conservadora: agregar mejoras verificables sin eliminar reglas utiles."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida por la materia [supuesto].",
    "Confirmar si LDE-S2B1 es codigo oficial o interno [supuesto].",
    "Confirmar si persiste vigencia de fuente provisional heredada desde ingenieria [supuesto].",
    "Confirmar rubrica especifica por actividad para ajustar profundidad argumentativa."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho a la Seguridad Social.",
        "Semestre 2, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico bien delimitado.",
      "Marco normativo y doctrinal pertinente.",
      "Evidencia verificable.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir consignas en productos juridicos verificables y profesionales.",
      "Preservar memoria editorial persistente sin perdida por deduplicacion.",
      "Asegurar calidad estructural y trazabilidad en propagacion transversal."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion clara entre marco, analisis y cierre.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo/doctrinal.",
      "Contrastar evidencia relevante.",
      "Fijar postura propia sustentada.",
      "Concluir con implicacion juridica practica."
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
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "La deduplicacion segura exige estructura valida."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La coherencia institucional orienta calidad de productos academicos."
        }
      ],
      "evidence": [
        "README de materia define estructura canonica local.",
        "Programa analitico define proposito y ejes de trabajo.",
        "Archivo .bib local confirma base normativa verificable.",
        "Regla persistente: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 22: se reforzo patron comun transversal sin mezclar contenido tematico de filosofia.",
      "Ciclo 22: se mantuvo regla de normalizacion previa a propagacion.",
      "Ciclo 22: se consolido cerebro editorial con enfoque en identidad, estructura y calidad."
    ]
  }
}