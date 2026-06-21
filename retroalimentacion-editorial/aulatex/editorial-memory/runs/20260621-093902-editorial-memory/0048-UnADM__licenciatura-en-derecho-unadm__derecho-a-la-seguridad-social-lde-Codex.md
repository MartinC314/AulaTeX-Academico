{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre actividad de Filosofia del Derecho y materia de Seguridad Social.",
    "Se preserva identidad UnADM, estructura por ejes y control de calidad sin mezclar contenido tematico no equivalente.",
    "Se refuerza regla de normalizacion: no propagar salidas no parseables.",
    "Se mantiene compresion lossless por union-dedupe y sin regresion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Conservar trazabilidad de reglas heredadas provisionales con etiqueta [supuesto].",
    "No sobrescribir reglas utiles previas; solo unir y deduplicar.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Tomar README y programa analitico del destino como canon estructural.",
    "Alinear entregas a ejes: problema, fundamento/conceptos, evidencia, analisis propio y conclusion juridica.",
    "Separar secciones en encuadre, desarrollo argumentativo, cierre y referencias.",
    "Alinear formato final al producto solicitado por la planeacion semanal.",
    "Mantener consistencia editorial entre reporte y presentacion."
  ],
  "activity_rules": [
    "Definir objetivo puntual y problema juridico al inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir hechos, normas, doctrina y postura propia.",
    "Evitar entregas solo descriptivas.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de propagacion recursiva.",
    "Confirmar respaldo verificable o marca [supuesto] en afirmaciones relevantes.",
    "Validar correspondencia entre citas en texto y archivo .bib local.",
    "Verificar que la compresion aplicada sea union-dedupe sin recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de materia y personalizar solo campos variables.",
    "Mantener codificacion y acentos correctos en .tex y .bib.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Normalizar nombres de archivo y resolver tokens o marcadores corruptos antes de compilar."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central.",
    "Priorizar fuentes institucionales y normativas verificables.",
    "No inventar referencias.",
    "Agregar solo fuentes consultables con metadatos minimos completos.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo abstracciones editoriales estables.",
    "No transferir redaccion literal ni contenido tematico especifico de Filosofia al destino.",
    "Propagar primero identidad, estructura reusable, quality gates y grafo conceptual.",
    "Mantener bandera de riesgo historico por salidas no parseables en ciclos previos.",
    "Aplicar estrategia progresiva y conservadora en cada ciclo."
  ],
  "open_questions": [
    "[supuesto] Confirmar norma de citacion requerida por la materia (APA, ISO o institucional).",
    "[supuesto] Confirmar uso operativo del codigo local LDE-S2B1 en entregables.",
    "Confirmar rubricas de evaluacion por actividad para ajustar profundidad argumentativa.",
    "Confirmar si todas plantillas Actividad-1 del destino ya existen y son canonicas."
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
      "Marco normativo y doctrinal verificable.",
      "Evidencia trazable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir consignas en productos juridicos verificables y evaluables.",
      "Preservar continuidad editorial entre nodos sin perder contexto local.",
      "Garantizar calidad tecnica de salida para propagacion segura."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiqueta explicita de [supuesto].",
      "Separacion visible entre marco, analisis y cierre.",
      "Sin duplicados ni regresiones."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo/doctrinal.",
      "Vincular evidencia verificable.",
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
          "justification": "El analisis exige una pregunta juridica delimitada."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida requiere fundamento legal."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura academica se legitima con respaldo trazable."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay consolidacion segura."
        }
      ],
      "evidence": [
        "README destino define estructura canonica y artefactos base.",
        "Programa analitico destino define proposito y ejes de trabajo.",
        "Archivo .bib destino confirma base normativa e institucional.",
        "Memoria origen aporta patron editorial reusable de cinco ejes."
      ]
    },
    "reinforcement_log": [
      "Ciclo 48: se mantiene regla de no propagar salidas no parseables.",
      "Ciclo 48: se refuerza patron transversal problema-fundamento-evidencia-analisis-conclusion.",
      "Ciclo 48: se conserva contenido local de Seguridad Social sin injerto tematico de Filosofia.",
      "Ciclo 48: deduplicacion aplicada sin eliminar reglas utiles previas."
    ]
  }
}