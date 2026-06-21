{
  "summary": [
    "Se refuerza sincronizacion transversal entre nodos no equivalentes con reglas estables y reutilizables.",
    "Se preserva identidad UnADM del destino sin mezclar contenido tematico de Filosofia del Derecho.",
    "Se consolida patron comun de entrega: problema, fundamento, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene compresion lossless por union-dedupe y sin regresion.",
    "Se mantiene alerta institucional por salidas no parseables historicas y normalizacion obligatoria."
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
    "Tomar README de materia como canon de estructura editorial local.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Separar desarrollo en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato y alcance al producto solicitado por la planeacion semanal.",
    "Mantener consistencia entre reporte, presentacion y programa analitico."
  ],
  "activity_rules": [
    "Delimitar problema juridico desde el inicio.",
    "Distinguir hechos, conceptos, normas y postura propia.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar compresion por union-dedupe y no por recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener metadatos institucionales y curriculares consistentes en archivos .tex.",
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Normalizar nombres de archivo y resolver tokens o marcadores corruptos antes de compilar."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central.",
    "Priorizar fuentes institucionales UnADM y normativas juridicas verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Verificar que cada cita tenga entrada BibTeX correspondiente."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales estables ya validadas.",
    "No transferir redaccion literal ni contenido tematico especifico de otra materia.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Conservar reglas locales del destino como precedencia operativa.",
    "Mantener bandera de riesgo por antecedentes de salida no parseable en ciclos tempranos."
  ],
  "open_questions": [
    "Confirmar si la referencia provisional heredada desde ingenieria sigue vigente en este nodo [supuesto].",
    "Confirmar norma de citacion requerida por la materia (APA, ISO, institucional o juridica mexicana) [supuesto].",
    "Confirmar datos oficiales de figura docente para plantilla.",
    "Confirmar si Actividad 1 del destino exige reporte, presentacion o ambos."
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
        "Materia destino: Derecho a la seguridad social.",
        "Semestre 2, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Fundamento normativo verificable.",
      "Evidencia pertinente.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir cada consigna en producto juridico verificable y util profesionalmente.",
      "Preservar continuidad editorial entre actividades, materia y nivel institucional."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion visible entre marco, analisis y cierre.",
      "Cierre con utilidad profesional."
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
          "justification": "La conclusion requiere base legal verificable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura academica exige sustento comprobable."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "La deduplicacion segura requiere estructura valida."
        }
      ],
      "evidence": [
        "README local define estructura canonica y control editorial.",
        "Programa analitico local fija proposito y ejes de trabajo.",
        ".bib local confirma base institucional y normativa vigente.",
        "Regla historica: normalizar salidas no parseables antes de propagar."
      ]
    },
    "reinforcement_log": [
      "Ciclo 9: se consolidan abstracciones editoriales transversales sin transferencia tematica literal.",
      "Ciclo 9: se preservan reglas utiles previas del destino y se eliminan duplicados semanticos.",
      "Ciclo 9: se refuerzan gates de calidad de parseo JSON, respaldo de afirmaciones y trazabilidad de supuestos."
    ]
  }
}