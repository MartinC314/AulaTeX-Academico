{
  "summary": [
    "Se consolida sincronizacion transversal con reglas estables entre nodos no equivalentes.",
    "Se preserva identidad UnADM y enfoque juridico del destino.",
    "Se refuerza patron comun: problema, fundamento, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene compresion lossless por union-dedupe sin regresion.",
    "Se conserva alerta institucional por antecedentes de salidas no parseables y normalizacion manual."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "No sobrescribir reglas validas previas; solo unir y deduplicar.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar trazabilidad de origen en reglas provisionales."
  ],
  "structure_rules": [
    "Tomar README y programa analitico de la materia como canon estructural.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Separar desarrollo en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato y alcance al producto solicitado por la planeacion semanal.",
    "Mantener consistencia entre reporte, presentacion y referencias."
  ],
  "activity_rules": [
    "Delimitar problema juridico desde el inicio.",
    "Vincular el desarrollo con normas, doctrina o datos verificables.",
    "Incluir postura propia argumentada; evitar resumen solo descriptivo.",
    "Distinguir hechos, conceptos, normas y opinion propia.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar manualmente respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo verificable o marca [supuesto] en cada afirmacion relevante.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que la compresion aplicada sea union-dedupe y no recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener metadatos institucionales y de curso consistentes en .tex y .bib.",
    "Usar codificacion correcta para espanol y acentos.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, sin referencias rotas y con rutas validas.",
    "Resolver marcadores o tokens sin expandir en nombres de archivo antes de compilar."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica local central.",
    "Priorizar fuentes institucionales UnADM y normativas juridicas verificables.",
    "Agregar solo referencias consultables y pertinentes a la actividad.",
    "No inventar fuentes; marcar faltantes como [supuesto] o pendiente.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales validadas y estables.",
    "No transferir contenido tematico especifico de Filosofia del Derecho al destino.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Mantener reglas locales de seguridad social como capa dominante del destino.",
    "Preservar bandera de riesgo historico por ciclos con salida no parseable."
  ],
  "open_questions": [
    "Confirmar norma de citacion requerida en la materia [supuesto].",
    "Confirmar si codigo local LDE-S2B1 es oficial o solo interno [supuesto].",
    "Confirmar si se mantiene vigente la referencia heredada desde ingenieria [supuesto].",
    "Confirmar rubricas por actividad para ajustar profundidad argumentativa [supuesto]."
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
      "Fundamento normativo verificable.",
      "Evidencia pertinente.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir consignas en productos juridicos verificables y utiles profesionalmente.",
      "Garantizar coherencia editorial, trazabilidad y calidad tecnica en LaTeX."
    ],
    "style_markers": [
      "Frases directas y accionables.",
      "Etiqueta explicita de [supuesto].",
      "Separacion visible entre marco, analisis y cierre.",
      "Cierre con implicacion practica."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo.",
      "Exponer marco normativo/doctrinal.",
      "Contrastar evidencia.",
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
          "justification": "No hay analisis solido sin pregunta juridica delimitada."
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
          "justification": "La postura gana validez con respaldo comprobable."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "La consolidacion segura requiere estructura valida."
        }
      ],
      "evidence": [
        "README de materia define estructura canonica y archivos base.",
        "Programa analitico define proposito y ejes de trabajo del destino.",
        "Archivo .bib local confirma base institucional y normativa verificable.",
        "Memoria origen confirma patron editorial reusable y gates de calidad."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin perdida semantica.",
      "Se transfirieron solo abstracciones estables de valor transversal.",
      "Se evito mezclar contenido tematico especifico de filosofia en seguridad social.",
      "Se reforzaron controles de parseo JSON, trazabilidad y soporte bibliografico."
    ]
  }
}