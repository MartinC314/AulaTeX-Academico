{
  "summary": [
    "Se sincroniza memoria transversal desde actividad de Filosofia del Derecho hacia materia de Seguridad Social sin mezclar contenido tematico.",
    "Se preserva identidad UnADM, estructura por ejes y control de calidad institucional.",
    "Se refuerza compresion lossless por union-dedupe y politica de no regresion.",
    "Se mantiene alerta por salidas no parseables heredadas; normalizacion manual sigue obligatoria.",
    "Se actualiza canon de estructura local con plantillas de actividad declaradas en README."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y trazabilidad.",
    "Usar datos curriculares oficiales del destino: Licenciatura en Derecho, semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica editorial.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No sobrescribir reglas validas previas; aplicar solo union y deduplicacion.",
    "No propagar datos personales de plantilla a nodos laterales salvo requerimiento explicito [supuesto]."
  ],
  "structure_rules": [
    "Tomar README y programa analitico del destino como canon estructural.",
    "Alinear cada entrega a ejes estables: problema, conceptos/norma, evidencia, analisis propio y conclusion juridica.",
    "Separar secciones minimas: encuadre, desarrollo, postura propia, cierre y referencias.",
    "Alinear formato final al producto solicitado en planeacion semanal.",
    "Mantener consistencia entre reporte, presentacion y versiones por actividad.",
    "Registrar en memoria solo reglas accionables, verificables y reutilizables."
  ],
  "activity_rules": [
    "Definir objetivo puntual y problema juridico al inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir hechos, marco normativo, doctrina y opinion propia.",
    "Evitar entregas solo descriptivas; exigir postura argumentada del estudiante.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Relacionar el analisis con seguridad social cuando la consigna lo pida."
  ],
  "quality_gates": [
    "Bloquear propagacion si salida no es JSON parseable.",
    "Normalizar manualmente toda respuesta no estructurada antes de reutilizar.",
    "Validar estructura minima completa antes de propagacion recursiva.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Comprobar consistencia entre citas en texto y entradas del .bib local.",
    "Verificar que la compresion aplicada sea lossless por union-dedupe.",
    "Verificar que no exista regresion de reglas utiles previas."
  ],
  "latex_rules": [
    "Conservar plantillas base de materia y actividad; personalizar solo campos variables.",
    "Mantener metadatos institucionales y curriculares consistentes en todos los .tex.",
    "Usar codificacion y acentos en espanol de forma consistente en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion tecnica.",
    "Compilar sin errores criticos, sin referencias rotas y con rutas limpias.",
    "Normalizar nombres de archivo cuando existan marcadores o caracteres corruptos.",
    "Incluir y mantener plantillas de actividad listadas en README como parte del canon local."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como repositorio bibliografico central.",
    "Priorizar fuentes institucionales UnADM y normativa juridica vigente verificable.",
    "Agregar solo referencias realmente consultables con metadatos minimos completos.",
    "No inventar fuentes; marcar faltantes como pendientes o [supuesto].",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo abstracciones editoriales estables, no redaccion literal.",
    "Propagar a laterales compatibles reglas de identidad, calidad JSON y control bibliografico.",
    "Restringir datos curriculares especificos al nodo de la misma materia.",
    "Mantener bandera de riesgo para artefactos de ciclo 1 no parseables.",
    "Aplicar estrategia progresiva y conservadora: agregar mejoras verificables sin recorte."
  ],
  "open_questions": [
    "Confirmar norma de citacion obligatoria de la materia (APA, ISO, institucional o juridica mexicana) [supuesto].",
    "Confirmar si codigo local LDE-S2B1 es oficial en todos los entregables [supuesto].",
    "Confirmar si la fuente provisional heredada desde ingenieria sigue vigente para este nodo [supuesto].",
    "Confirmar datos de figura docente para plantillas de actividad cuando exista fuente oficial.",
    "Verificar integridad del archivo .bib local mostrado de forma truncada en contexto [supuesto]."
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
      "Fundamento normativo y conceptual verificable.",
      "Evidencia pertinente.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir consignas en productos juridicos verificables y evaluables.",
      "Garantizar consistencia editorial entre actividades y materia.",
      "Preservar memoria persistente sin perdida por deduplicacion."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion clara entre marco, analisis y cierre.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo y doctrinal.",
      "Contrastar evidencia.",
      "Fijar postura propia sustentada.",
      "Cerrar con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "JSON parseable",
        "Compresion lossless por union-dedupe",
        "Problema juridico",
        "Marco normativo",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Seguridad social en Mexico"
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
          "source": "JSON parseable",
          "target": "Compresion lossless por union-dedupe",
          "kind": "depends_on",
          "justification": "La propagacion segura requiere estructura valida."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "No hay analisis solido sin delimitacion previa."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida necesita fundamento legal."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura academica exige respaldo contrastable."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Seguridad social en Mexico",
          "kind": "develops",
          "justification": "La materia aplica el marco comun institucional a su dominio tematico."
        }
      ],
      "evidence": [
        "README del destino define estructura canonica y plantillas por actividad.",
        "Programa analitico del destino fija proposito y ejes juridicos.",
        "Archivo .bib local contiene base institucional y normativa vigente.",
        "Memoria origen confirma patron editorial estable y reusable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 6: se conservaron reglas utiles previas sin eliminacion.",
      "Ciclo 6: se deduplicaron reglas repetidas con semantica equivalente.",
      "Ciclo 6: se transfirieron solo abstracciones estables entre nodos no equivalentes.",
      "Ciclo 6: se reforzo gate de JSON parseable y normalizacion manual.",
      "Ciclo 6: se incorporo canon de plantillas de actividad desde README local."
    ]
  }
}