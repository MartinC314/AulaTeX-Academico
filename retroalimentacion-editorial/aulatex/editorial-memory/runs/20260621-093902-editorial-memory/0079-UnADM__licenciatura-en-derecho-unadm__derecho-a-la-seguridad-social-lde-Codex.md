{
  "summary": [
    "Se mantiene identidad UnADM y enfoque juridico del destino.",
    "Se refuerza patron transversal estable: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se conserva normalizacion estructurada obligatoria antes de propagacion recursiva.",
    "Se preserva compresion lossless por union-dedupe sin regresion.",
    "Se integra estructura canonica local desde README y programa analitico.",
    "Se mantiene alerta por antecedentes de salida no parseable y necesidad de normalizacion manual."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre de materia: Derecho a la Seguridad Social.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No sobrescribir reglas validas previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README de materia como canon estructural.",
    "Alinear cada entrega a ejes: problema, conceptos/norma, producto, analisis y conclusion.",
    "Separar secciones en: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Alinear formato final al producto pedido en planeacion semanal.",
    "Mantener consistencia entre reporte, presentacion y programa analitico."
  ],
  "activity_rules": [
    "Delimitar problema juridico o social al inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, conceptos, normas y opinion propia.",
    "Relacionar contenido con seguridad social cuando corresponda.",
    "Ajustar alcance y formato a la consigna semanal."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar manualmente respuestas no estructuradas antes de reutilizar.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar coherencia entre objetivo, estructura y conclusion.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que no se eliminen reglas utiles previas.",
    "Confirmar compresion lossless por union-dedupe y no por recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base local y personalizar solo campos variables.",
    "Mantener metadatos institucionales y de curso consistentes en .tex.",
    "Usar estructura minima: portada, desarrollo por ejes, conclusion y referencias.",
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Normalizar nombres de archivo con marcadores corruptos antes de compilar."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Agregar solo referencias especificas de actividad con metadatos minimos completos.",
    "No inventar referencias; usar solo obras consultables.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Verificar que cada cita en LaTeX tenga entrada BibTeX correspondiente.",
    "Conservar entradas institucionales cuando se citen."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Compartir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferir redaccion literal o contenido tematico especifico de otra materia.",
    "Mantener bandera de riesgo por ciclos con salida no parseable.",
    "Aplicar normalizacion manual en nodos vecinos con salida no estructurada."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida en la materia [supuesto].",
    "Confirmar rubrica oficial por actividad para calibrar profundidad argumentativa [supuesto].",
    "Confirmar si codigo local LDE-S2B1 es oficial o interno [supuesto].",
    "Confirmar dato de figura docente cuando exista fuente oficial [supuesto].",
    "Confirmar si toda actividad requiere reporte, presentacion o ambos."
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
      "Resolver consignas con problema juridico claro.",
      "Fundamentar con marco normativo y evidencia verificable.",
      "Sostener analisis propio y cerrar con utilidad profesional.",
      "Preservar memoria editorial por union-dedupe sin perdida."
    ],
    "reason_for_being": [
      "Convertir cada consigna en producto juridico verificable y transferible.",
      "Garantizar continuidad editorial institucional entre ciclos.",
      "Permitir propagacion segura entre nodos con validaciones estrictas."
    ],
    "style_markers": [
      "Frases directas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion visible entre marco, analisis y cierre.",
      "Cierre con implicacion juridica practica."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo y doctrinal.",
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
          "justification": "No hay analisis solido sin pregunta juridica delimitada."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida requiere fundamento legal verificable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura gana solidez cuando cita fuentes comprobables."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "La deduplicacion segura requiere estructura valida."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La identidad guia tono, rigor y aplicabilidad profesional."
        }
      ],
      "evidence": [
        "README local define estructura canonica y artefactos base.",
        "Programa analitico local define proposito y ejes de trabajo.",
        "Archivo .bib local confirma base normativa e institucional.",
        "Regla transversal consolidada: normalizar antes de propagar.",
        "Regla transversal consolidada: no inventar fuentes."
      ]
    },
    "reinforcement_log": [
      "Ciclo 79: se transfiere patron editorial estable desde actividad de Filosofia sin mezclar contenido tematico.",
      "Ciclo 79: se refuerzan quality gates de JSON parseable, respaldo y trazabilidad de [supuesto].",
      "Ciclo 79: se preservan reglas locales del destino y se deduplican variantes equivalentes.",
      "Ciclo 79: se mantiene estrategia progresiva y conservadora sin regresion."
    ]
  }
}