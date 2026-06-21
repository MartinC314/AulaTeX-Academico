{
  "summary": [
    "Se consolida sincronizacion transversal entre nodos no equivalentes con reglas estables y reutilizables.",
    "Se preserva identidad UnADM y contexto local de Derecho a la Seguridad Social.",
    "Se refuerza patron editorial comun: problema, conceptos o norma, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene compresion lossless por union-dedupe sin regresion.",
    "Se conserva alerta institucional por salidas no parseables heredadas y necesidad de normalizacion previa."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No sobrescribir reglas utiles previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README y programa analitico de la materia como canon estructural local.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Organizar en secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Delimitar problema y pregunta guia desde el inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir hechos, normas, doctrina y postura propia.",
    "Evitar entregas solo descriptivas; incluir argumentacion del estudiante.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Relacionar cada producto con el campo de seguridad social cuando corresponda."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizar aguas abajo.",
    "Validar estructura minima completa antes de propagacion recursiva.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Verificar que no haya regresion de reglas utiles previas."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificacion y acentos correctos en espanol en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Normalizar rutas y nombres de archivo antes de compilar.",
    "Mantener consistencia entre reporte y presentacion."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central.",
    "Priorizar fuentes institucionales UnADM y normativas juridicas vigentes verificables.",
    "Agregar solo referencias realmente consultables.",
    "No inventar fuentes; marcar faltantes como pendientes o [supuesto].",
    "Conservar metadatos minimos: autor, titulo, ano, fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables en saltos transversales.",
    "No transferir contenido tematico especifico de Filosofia del Derecho al destino.",
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Reforzar en laterales reglas de integridad, trazabilidad y control bibliografico.",
    "Mantener bandera de riesgo por antecedentes de salida no parseable en ciclos tempranos."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida en la materia (APA, ISO, institucional o juridica mexicana) [supuesto].",
    "Confirmar si codigo local LDE-S2B1 es oficial en todos los entregables [supuesto].",
    "Confirmar datos de figura docente para plantillas de actividad [supuesto].",
    "Confirmar si actividades iniciales requieren reporte, presentacion o ambos productos."
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
      "Producto juridico verificable orientado a problema, fundamento, evidencia, analisis y cierre.",
      "Transferencia transversal de metodo editorial, no de redaccion literal.",
      "Compresion lossless por deduplicacion y sin recorte."
    ],
    "reason_for_being": [
      "Convertir consignas en entregables juridicos solidos y trazables.",
      "Asegurar coherencia entre identidad institucional, estructura y evidencia.",
      "Permitir propagacion segura entre nodos sin contaminar contexto local."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion clara entre marco, analisis y conclusion.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo o doctrinal pertinente.",
      "Presentar evidencia verificable.",
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
          "justification": "El analisis requiere una pregunta delimitada."
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
          "justification": "La identidad define tono, rigor y utilidad profesional del cierre."
        }
      ],
      "evidence": [
        "README local define estructura canonica de archivos y control editorial.",
        "Programa analitico local define proposito y ejes juridicos.",
        "Archivo .bib local confirma base normativa e institucional.",
        "Memoria origen confirma patron editorial comun reutilizable."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin perdida semantica.",
      "Se conservaron alertas de calidad sobre parseo JSON y normalizacion manual.",
      "Se transfirieron solo abstracciones estables por relacion transversal.",
      "Se preservo contexto curricular y documental especifico del destino.",
      "Se evitaron fuentes inventadas y se mantuvo trazabilidad de supuestos."
    ]
  }
}