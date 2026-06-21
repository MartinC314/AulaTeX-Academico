{
  "summary": [
    "Se mantiene sincronizacion transversal sin mezclar contenido tematico de Filosofia del Derecho.",
    "Se refuerza patron editorial estable: problema, fundamento, evidencia, analisis propio y conclusion juridica.",
    "Se preserva identidad UnADM y estructura canonica del destino.",
    "Se conserva compresion lossless por union-dedupe y sin regresion.",
    "Se mantiene alerta por salidas no parseables heredadas y normalizacion obligatoria."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No sobrescribir reglas validas previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README y programa analitico como canon estructural local.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar desarrollo en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear el formato al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Delimitar problema y pregunta guia al inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta, desarrollo y conclusion.",
    "Relacionar el contenido con seguridad social cuando aplique."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de propagar recursivamente.",
    "Normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar respaldo verificable o marca [supuesto] en cada afirmacion relevante.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que no haya regresion de reglas utiles previas."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificacion correcta para espanol en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, sin referencias rotas y con rutas validas.",
    "Normalizar nombres de archivo con marcadores corruptos antes de usar como canon.",
    "Mantener consistencia entre reporte y presentacion."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente central local.",
    "Priorizar fuentes institucionales UnADM y normatividad vigente verificable.",
    "Agregar solo referencias consultables con metadatos minimos completos.",
    "No inventar fuentes; marcar faltantes como pendientes o [supuesto].",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No transferir citas de Filosofia salvo pertinencia expresa y verificada."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables en saltos transversales.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferencia de redaccion literal o contenido tematico no equivalente.",
    "Mantener bandera de riesgo por antecedentes de salida no parseable.",
    "Aplicar validacion JSON y dedupe antes de propagar a nodos vecinos."
  ],
  "open_questions": [
    "Confirmar norma de citacion obligatoria de la materia [supuesto].",
    "Confirmar si codigo local LDE-S2B1 es oficial en todas las plantillas [supuesto].",
    "Confirmar si la fuente provisional heredada desde ingenieria sigue vigente [supuesto].",
    "Verificar vigencia de fechas DOF en entradas legales antes de entrega final.",
    "Confirmar rubricas de evaluacion por actividad para ajustar profundidad."
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
      "Evidencia pertinente y trazable.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir consignas en productos juridicos verificables y utiles profesionalmente.",
      "Preservar continuidad editorial entre actividades sin perder contexto local.",
      "Garantizar calidad formal, argumentativa y tecnica en LaTeX."
    ],
    "style_markers": [
      "Frases directas y accionables.",
      "Marcado explicito de [supuesto].",
      "Separacion clara entre marco, analisis y cierre.",
      "Cierre con utilidad practica."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo.",
      "Exponer marco normativo y doctrinal.",
      "Contrastar evidencia relevante.",
      "Fijar postura propia con sustento.",
      "Concluir con implicacion juridica concreta."
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
          "justification": "Sin delimitacion del problema no hay analisis juridico valido."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion requiere base legal verificable."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "La consolidacion segura depende de estructura valida."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "La integridad institucional exige trazabilidad de fuentes."
        }
      ],
      "evidence": [
        "README de la materia define estructura canonica y archivos base.",
        "Programa analitico define proposito y ejes de trabajo del destino.",
        "Bib local confirma base normativa e institucional verificable.",
        "Memoria previa reporta necesidad de normalizacion ante salidas no parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 47: se refuerzan reglas transversales estables sin importar contenido disciplinar del origen.",
      "Ciclo 47: se conserva ADN local de seguridad social y se evita arrastre literal desde filosofia.",
      "Ciclo 47: se mantiene control de calidad tecnico (JSON, .bib, compilacion) como nucleo persistente."
    ]
  }
}