{
  "summary": [
    "Se mantiene identidad UnADM y enfoque juridico del destino.",
    "Se refuerza patron transversal estable: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se conserva regla critica: no propagar salidas no estructuradas sin normalizacion.",
    "Se consolida compresion lossless por union-dedupe sin regresion.",
    "Se preserva especificidad local de Seguridad Social sin transferir contenido tematico de Filosofia."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de la materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No sobrescribir reglas validas previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README y programa analitico como canon estructural local.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Organizar en secciones: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Delimitar problema y pregunta guia al inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Distinguir hechos, conceptos, normas y opinion propia.",
    "Verificar coherencia entre consigna, desarrollo y conclusion.",
    "Relacionar cada producto con el campo de seguridad social cuando corresponda."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar manualmente respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de propagacion recursiva.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar correspondencia entre citas en texto y archivo .bib local.",
    "Verificar que la compresion aplicada sea union-dedupe y no recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificacion y acentos correctos en espanol en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Normalizar nombres de archivos y resolver marcadores/tokens corruptos antes de compilar.",
    "Mantener consistencia de metadatos institucionales en todos los .tex."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central.",
    "Priorizar fuentes institucionales UnADM y normativa juridica verificable.",
    "No inventar referencias; agregar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Verificar que cada cita LaTeX tenga su entrada BibTeX correspondiente."
  ],
  "propagation_hints": [
    "Propagar lateral y recursivo solo reglas generales validadas.",
    "Transferir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "No transferir redaccion literal ni contenido tematico especifico de Filosofia.",
    "Preservar reglas locales del destino como prioridad contextual.",
    "Mantener bandera historica: ciclo 1 con salida no parseable requiere normalizacion manual.",
    "Evitar regresion de identidad, estructura por ejes y control bibliografico."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida en la materia (APA, ISO, institucional o juridica) [supuesto].",
    "Confirmar si existe rubrica oficial por actividad para calibrar profundidad argumentativa [supuesto].",
    "Confirmar datos faltantes de figura docente en plantillas [supuesto].",
    "Verificar vigencia de reglas heredadas desde nodos no juridicos antes de reutilizacion transversal [supuesto]."
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
      "Problema juridico delimitado.",
      "Marco conceptual y normativo pertinente.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir consignas en productos juridicos verificables y utiles profesionalmente.",
      "Asegurar coherencia entre identidad institucional, rigor argumentativo y trazabilidad tecnica."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Separacion clara entre marco, analisis y cierre.",
      "Etiquetado explicito de [supuesto] cuando falte verificacion.",
      "Cierre con implicacion practica."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo/doctrinal.",
      "Contrastar evidencia relevante.",
      "Fijar postura propia sustentada.",
      "Concluir con efecto juridico practico."
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
          "justification": "Sin pregunta delimitada no hay analisis juridico consistente."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion requiere fundamento legal verificable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura propia debe sostenerse en fuentes trazables."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "La consolidacion segura exige estructura valida."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "El estilo institucional orienta utilidad academica y profesional."
        }
      ],
      "evidence": [
        "README del destino define estructura canonica y control editorial.",
        "Programa analitico del destino define proposito y ejes de trabajo.",
        "Archivo .bib local confirma base normativa e institucional verificable.",
        "Memoria previa registra incidente de salida no parseable y gate de normalizacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 62: se reforzo patron transversal estable sin mezclar contenido tematico entre materias.",
      "Ciclo 62: se mantuvo regla dura de JSON parseable antes de propagacion recursiva.",
      "Ciclo 62: se preservo especificidad curricular y bibliografica del destino.",
      "Ciclo 62: consolidacion realizada por union-dedupe sin eliminacion de reglas utiles."
    ]
  }
}