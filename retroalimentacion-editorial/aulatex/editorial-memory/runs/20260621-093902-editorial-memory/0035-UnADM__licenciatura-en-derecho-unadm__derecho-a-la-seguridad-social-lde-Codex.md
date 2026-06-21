{
  "summary": [
    "Se consolida sincronizacion transversal entre nodos no equivalentes con transferencia de reglas estables.",
    "Se preserva identidad UnADM y contexto local de Derecho a la Seguridad Social sin mezclar contenido tematico de Filosofia del Derecho.",
    "Se refuerza patron editorial comun: problema, conceptos o norma, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene compresion lossless por union-dedupe y sin regresion.",
    "Se confirma control institucional: no propagar salidas no estructuradas sin normalizacion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de materia como punto de entrada canonico.",
    "Conservar trazabilidad de reglas heredadas y marcar provisionales como [supuesto].",
    "No sobrescribir reglas validas previas; solo unir y deduplicar.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Tomar README y programa analitico del destino como canon estructural.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Separar desarrollo en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por planeacion semanal.",
    "Mantener consistencia entre reporte, presentacion y bibliografia local."
  ],
  "activity_rules": [
    "Delimitar problema y pregunta guia desde el inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar solo descripcion.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Verificar coherencia entre objetivo, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar manualmente cualquier salida no estructurada antes de reutilizar.",
    "Validar estructura minima completa antes de propagacion recursiva.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que la compresion aplicada sea union-dedupe sin recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificacion y acentos correctos en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, sin referencias rotas y con rutas limpias.",
    "Normalizar nombres de archivo si aparecen marcadores o tokens sin expandir.",
    "No copiar bloques LaTeX completos entre materias; transferir solo reglas."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente central local.",
    "Priorizar fuentes institucionales UnADM y normativas juridicas vigentes verificables.",
    "No inventar referencias; registrar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente o URL.",
    "Distinguir bibliografia base de materia y bibliografia especifica de actividad.",
    "No asumir que bibliografia de otra materia aplica al destino sin verificacion [supuesto]."
  ],
  "propagation_hints": [
    "Propagar lateral y hacia arriba solo reglas generales ya validadas.",
    "Transferir abstracciones estables de identidad, estructura, calidad y grafo conceptual.",
    "No transferir citas ni conceptos tematicos propios de Filosofia del Derecho al destino.",
    "Mantener bandera de riesgo por antecedentes de salida no parseable en ciclos tempranos.",
    "Aplicar estrategia progresiva y conservadora: agregar mejoras verificables sin eliminar reglas utiles."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida en la materia destino (APA, ISO o institucional) [supuesto].",
    "Confirmar si el codigo local LDE-S2B1 es oficial en todas las plantillas [supuesto].",
    "Confirmar si actividad-1 del destino exige reporte, presentacion o ambos.",
    "Verificar si persiste alguna fuente provisional heredada de nodos no juridicos [supuesto]."
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
        "Materia destino: Derecho a la Seguridad Social.",
        "Semestre 2, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Marco normativo y conceptual pertinente.",
      "Evidencia verificable.",
      "Analisis propio argumentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar consignas en productos juridicos verificables y utiles para practica profesional.",
      "Sostener continuidad editorial entre actividades, materias y ciclos sin perder contexto local."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto] cuando falten datos.",
      "Separacion visible entre marco, analisis y cierre.",
      "Cierre con utilidad juridica practica."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo o doctrinal.",
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
          "justification": "Sin problema delimitado no hay analisis juridico consistente."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida requiere fundamento legal verificable."
        },
        {
          "source": "JSON parseable",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "La reutilizacion segura exige estructura valida."
        },
        {
          "source": "Compresion union-dedupe",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Preserva reglas utiles sin perdida ni duplicacion."
        }
      ],
      "evidence": [
        "README del destino define estructura canonica y artefactos base.",
        "Programa analitico del destino fija proposito y ejes de trabajo.",
        "Archivo .bib local confirma base normativa e institucional verificable.",
        "Memoria origen confirma gate institucional de normalizacion y JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 35: se incorporan reglas transversales estables desde actividad de Filosofia sin trasladar contenido tematico.",
      "Ciclo 35: se refuerzan gates de calidad para parseo JSON, respaldo de afirmaciones y trazabilidad de supuestos.",
      "Ciclo 35: se conserva ADN local de Seguridad Social y se evita regresion editorial."
    ]
  }
}