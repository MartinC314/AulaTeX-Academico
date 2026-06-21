{
  "summary": [
    "Se consolida sincronizacion transversal entre nodos no equivalentes con union-dedupe sin perdida.",
    "Se preserva identidad UnADM y enfoque juridico del destino.",
    "Se refuerza patron estable: problema, fundamento, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene normalizacion estructurada obligatoria antes de propagar.",
    "Se conserva alerta historica: ciclos con salida no parseable requieren normalizacion manual."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar carpeta de materia destino como entrada canonica.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Vincular entregas a Licenciatura en Derecho y a Derecho a la Seguridad Social.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No sobrescribir reglas validas previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README y programa analitico del destino como canon estructural.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar desarrollo en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto solicitado por la planeacion semanal.",
    "Mantener consistencia editorial entre reporte, presentacion y actividad."
  ],
  "activity_rules": [
    "Delimitar problema y pregunta guia al inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Incluir postura argumentada del estudiante; evitar resumen solo descriptivo.",
    "Verificar coherencia entre objetivo, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar aguas abajo.",
    "Normalizar manualmente respuestas no estructuradas de ciclos con incidencias.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Confirmar compresion lossless por union-dedupe y sin regresion."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener metadatos institucionales y de curso consistentes en .tex.",
    "Usar estructura minima: portada, desarrollo, conclusion y referencias.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, citas rotas ni referencias rotas.",
    "Corregir rutas, nombres corruptos o tokens sin expandir antes de compilar."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central.",
    "Priorizar fuentes institucionales UnADM y normas juridicas vigentes verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Agregar solo fuentes especificas de actividad con metadatos minimos completos.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Verificar que cada clave citada exista en el .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales estables y verificadas.",
    "No transferir contenido tematico literal de Filosofia del Derecho al destino.",
    "Priorizar identidad, gates de calidad, estructura reusable y grafo conceptual comun.",
    "Mantener reglas locales del destino como capa superior de especificidad.",
    "Conservar trazabilidad de reglas provisionales con etiqueta [supuesto]."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida por la materia (APA, ISO o institucional) [supuesto].",
    "Confirmar si LDE-S2B1 es codigo oficial operativo en todas las plantillas [supuesto].",
    "Confirmar datos faltantes de figura docente para portada cuando exista fuente oficial.",
    "Verificar vigencia de reglas provisionales heredadas de nodos no juridicos [supuesto]."
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
      "Fundamento normativo y doctrinal verificable.",
      "Evidencia trazable.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir consignas en productos juridicos verificables y profesionalmente utiles.",
      "Preservar memoria editorial persistente sin perdida ni regresion.",
      "Permitir reutilizacion transversal segura entre nodos no equivalentes."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion visible entre marco, analisis y cierre.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo.",
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
          "justification": "Sin delimitacion del problema no hay analisis juridico consistente."
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
          "justification": "La postura academica exige sustento objetivo."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "La consolidacion automatizable requiere estructura valida."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "Orienta el producto a pertinencia academica y profesional."
        }
      ],
      "evidence": [
        "README del destino define estructura canonica y artefactos.",
        "Programa analitico del destino define proposito y ejes de trabajo.",
        "Archivo .bib local confirma base normativa e institucional vigente.",
        "Historial institucional reporta ciclos con salida no parseable y necesidad de normalizacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 21: se transfieren solo abstracciones editoriales estables por relacion transversal.",
      "Ciclo 21: se evita mezclar contenido tematico especifico de Filosofia en Seguridad Social.",
      "Ciclo 21: se refuerzan gates de JSON parseable, evidencia verificable y union-dedupe.",
      "Ciclo 21: se conserva ADN del destino y se agregan mejoras verificables sin eliminar reglas utiles."
    ]
  }
}