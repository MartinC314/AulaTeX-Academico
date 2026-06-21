{
  "summary": [
    "Se consolida sincronizacion transversal entre nodos no equivalentes con union-dedupe sin perdida.",
    "Se preserva identidad UnADM, estructura por ejes y control de calidad parseable.",
    "Se transfiere patron estable: problema, conceptos/norma, evidencia, analisis propio y conclusion juridica.",
    "Se evita migrar contenido tematico especifico de Filosofia del Derecho al destino de Seguridad Social.",
    "Se mantiene alerta institucional por salidas no parseables heredadas y necesidad de normalizacion manual."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar carpeta de materia destino como punto de entrada canonico.",
    "Aplicar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No sobrescribir reglas validas previas; solo unir y deduplicar sin regresion."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar desarrollo en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato al producto solicitado por la planeacion semanal.",
    "Mantener consistencia entre README, programa analitico, reporte y presentacion.",
    "Usar estructura minima: portada, desarrollo, conclusion y referencias."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Relacionar cada actividad con el campo de seguridad social cuando corresponda.",
    "No asumir fuentes de otras semanas o materias sin validacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Verificar que la compresion sea lossless por union-dedupe y no por recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener acentos y codificacion correcta en espanol en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Corregir rutas, nombres y marcadores corruptos antes de compilar.",
    "Resolver tokens sin expandir en README y programa analitico antes de canonizar archivos."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central.",
    "Priorizar fuentes institucionales UnADM y normativas juridicas vigentes verificables.",
    "No inventar referencias; agregar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/URL.",
    "Distinguir bibliografia base de materia y bibliografia especifica de actividad.",
    "Verificar que cada clave citada exista en el .bib local."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables en saltos transversales.",
    "No propagar redaccion literal ni contenido doctrinal especifico de otra materia.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Mantener bandera de riesgo por antecedentes de salida no parseable en ciclos iniciales.",
    "Aplicar propagacion recursiva solo tras validar JSON y estructura completa."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida por la materia destino (APA, ISO, institucional o juridica mexicana) [supuesto].",
    "Confirmar si la regla provisional heredada desde ingenieria sigue vigente en este nodo [supuesto].",
    "Confirmar rubrica oficial por actividad para calibrar profundidad argumentativa.",
    "Confirmar si cada actividad requiere reporte, presentacion o ambos formatos.",
    "Verificar vigencia periodica de URLs normativas en el .bib local."
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
      "Resolver consignas en productos juridicos verificables.",
      "Sostener todo analisis en problema delimitado y fundamento normativo.",
      "Cerrar con conclusion juridica transferible a practica profesional.",
      "Preservar memoria por union-dedupe sin regresion."
    ],
    "reason_for_being": [
      "Servir como cerebro editorial persistente y reutilizable de la materia.",
      "Garantizar calidad formal, trazabilidad y consistencia institucional.",
      "Permitir propagacion segura entre nodos con control de supuestos."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion clara entre marco, analisis y cierre.",
      "No invencion de fuentes.",
      "Sincronizacion transversal sin contaminar contenido disciplinar local."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo.",
      "Exponer marco normativo y doctrinal pertinente.",
      "Integrar evidencia verificable.",
      "Fijar postura propia sustentada.",
      "Concluir con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema juridico delimitado",
        "Marco normativo/doctrinal",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "JSON parseable",
        "Compresion lossless por union-dedupe"
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
          "source": "Problema juridico delimitado",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin pregunta delimitada no hay analisis juridico riguroso."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida requiere fundamento legal verificable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura academica necesita respaldo trazable."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion lossless por union-dedupe",
          "kind": "depends_on",
          "justification": "La deduplicacion segura exige estructura valida."
        }
      ],
      "evidence": [
        "README del destino define estructura canonica de archivos.",
        "Programa analitico del destino define proposito y ejes de trabajo.",
        "Archivo .bib local confirma base institucional y normativa verificable.",
        "Memoria heredada confirma gate de normalizacion para salidas no parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 81: se refuerza patron transversal estable sin transferir contenido tematico de Filosofia.",
      "Ciclo 81: se mantiene gate estricto de JSON parseable y normalizacion manual cuando aplique.",
      "Ciclo 81: se consolida ADN editorial minimo reconstruible para propagacion recursiva conservadora."
    ]
  }
}