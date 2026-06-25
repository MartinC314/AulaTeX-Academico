{
  "summary": [
    "Se consolida sincronizacion transversal ciclo 5 entre actividad y materia sin copiar contenido tematico.",
    "Se preservan reglas utiles previas y se aplica deduplicacion lossless por union.",
    "Se refuerzan ejes estables: identidad UnADM, estructura en cinco ejes, calidad JSON, trazabilidad bibliografica.",
    "Se mantiene criterio conservador: transferir solo abstracciones editoriales verificables.",
    "Se conserva alerta historica de salidas no JSON parseables y normalizacion obligatoria."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y formato.",
    "Usar nombre oficial local de materia: Historia del Derecho en Mexico [supuesto: acentuacion institucional pendiente].",
    "Conservar contexto curricular local: semestre 1, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como supuesto cualquier dato no visible en consigna o no verificado localmente.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Alinear cada entrega a cinco ejes: problema, conceptos/fuentes, producto, analisis propio, conclusion transferible.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar secciones en: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado en planeacion semanal.",
    "Mantener coherencia entre README, programa analitico, .tex y .bib.",
    "No mezclar contenido tematico de otras materias sin evidencia local verificable."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica aplicable a la practica profesional.",
    "Adaptar salida a reporte, presentacion o producto visual segun consigna.",
    "No asumir fuentes de semanas o materias distintas sin validacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de propagacion recursiva.",
    "Confirmar que toda afirmacion sustantiva tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar union-dedupe sin recortar reglas utiles previas."
  ],
  "latex_rules": [
    "Usar plantilla local de reporte o presentacion segun tipo de entrega.",
    "Conservar metadatos institucionales: documenttitle, documentsubtitle, documentsubject, coursename y coursecode.",
    "Actualizar documentsubtitle con numero y nombre real de actividad.",
    "Mantener tabla de autor con alumno, matricula, figura docente, semestre/bloque y tipo/creditos.",
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Resolver placeholders tipo $(@{...}.Slug) en README y programa antes de compilar o citar.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Usar historia-del-derecho-en-mexico.bib como repositorio local canonico.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Agregar solo fuentes realmente consultadas; no inventar referencias.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No propagar bibliografia tematica de otra materia sin consulta efectiva."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas transversales y verificables.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferencia de redaccion literal entre nodos no equivalentes.",
    "Mantener alerta de salidas no parseables en niveles superiores y laterales.",
    "No propagar datos curriculares especificos de esta materia a materias hermanas."
  ],
  "open_questions": [
    "Confirmar acentuacion oficial en nombre de materia: Mexico/México [supuesto].",
    "Confirmar si LDE-S1B1 es codigo oficial o local de plantilla.",
    "Definir nombre oficial de figura docente en plantillas.",
    "Corregir en README saltos anómalos de render en nombres de archivo [supuesto].",
    "Confirmar fuente operativa definitiva para consolidacion de memoria (Codex/GPT-Pro u otra)."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador en inferencias no verificadas."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada obligatoria antes de propagar.",
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Historia del Derecho en Mexico.",
        "Semestre 1, bloque 1, obligatoria, 8 creditos.",
        "Fuente curricular local: malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y fuentes pertinentes.",
      "Producto alineado a planeacion.",
      "Analisis propio.",
      "Conclusion juridica transferible.",
      "Control de calidad estructural y bibliografico."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables claros, verificables y utiles para formacion juridica.",
      "Preservar continuidad editorial institucional entre actividades, materias y ciclos."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Bloques seccionales trazables.",
      "Cita explicita de fuentes.",
      "Cierre con criterio juridico propio.",
      "Marcado expreso de supuestos."
    ],
    "argumentative_patterns": [
      "Problema -> objetivo -> marco conceptual/normativo -> analisis -> conclusion aplicada.",
      "Afirmacion -> evidencia verificable -> interpretacion propia -> implicacion practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Cinco ejes editoriales",
        "Integridad academica",
        "Normalizacion JSON",
        "Trazabilidad bibliografica",
        "Coherencia consigna-producto",
        "Propagacion transversal conservadora"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La identidad institucional exige verificabilidad y forma academica consistente."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Coherencia consigna-producto",
          "kind": "supports",
          "justification": "Los cinco ejes ordenan el desarrollo y evitan entregas desalineadas."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion transversal conservadora",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia segura entre nodos."
        },
        {
          "source": "Trazabilidad bibliografica",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Las fuentes verificables sostienen afirmaciones y conclusiones."
        },
        {
          "source": "Coherencia consigna-producto",
          "target": "Integridad academica",
          "kind": "develops",
          "justification": "La adecuacion al encargo mejora validez academica del entregable."
        }
      ],
      "evidence": [
        "README local de materia: identidad y pauta editorial.",
        "Programa analitico local: proposito y cinco ejes.",
        "historia-del-derecho-en-mexico.bib: base institucional verificable.",
        "Plantillas .tex locales: metadatos y estructura institucional."
      ]
    },
    "reinforcement_log": [
      "Ciclo 5: deduplicacion completa de reglas repetidas en origen y destino.",
      "Ciclo 5: transferencia transversal limitada a abstracciones estables, sin arrastre tematico de Filosofia del Derecho.",
      "Ciclo 5: se mantiene regla critica de bloqueo por JSON no parseable.",
      "Ciclo 5: se refuerza marcado de supuestos y tratamiento provisional de fuentes heredadas."
    ]
  }
}