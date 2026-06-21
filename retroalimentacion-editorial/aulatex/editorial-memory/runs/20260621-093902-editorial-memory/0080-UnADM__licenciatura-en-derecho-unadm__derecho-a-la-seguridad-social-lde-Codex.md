{
  "summary": [
    "Se consolida sincronizacion transversal entre nodos no equivalentes con reglas editoriales estables.",
    "Se preserva identidad UnADM y enfoque juridico del destino sin mezclar contenido tematico de Filosofia del Derecho.",
    "Se refuerza patron comun reusable: problema, conceptos o norma, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene compresion lossless por union-dedupe y politica de no regresion.",
    "Se conserva gate critico: bloquear propagacion cuando no haya JSON parseable y normalizar antes de reutilizar."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y trazabilidad.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "No sobrescribir reglas validas previas; unir y deduplicar.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Tomar README y programa analitico de la materia como canon estructural local.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Separar desarrollo en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por la planeacion semanal.",
    "Mantener consistencia entre reporte, presentacion y referencias."
  ],
  "activity_rules": [
    "Delimitar problema juridico y pregunta guia al inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Verificar coherencia entre objetivo, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Validar estructura minima completa antes de propagacion recursiva.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que no se eliminen reglas utiles previas."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificacion y acentos correctos en espanol en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion tecnica.",
    "Compilar sin errores criticos, sin referencias rotas y con rutas limpias.",
    "Normalizar nombres de archivo con marcadores corruptos o tokens sin expandir antes de compilar.",
    "Usar estructura minima: portada, desarrollo por ejes, conclusion y referencias."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica local central.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas oficiales verificables.",
    "Agregar solo referencias consultables y pertinentes a la actividad.",
    "No inventar referencias.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente o URL.",
    "Distinguir bibliografia base de materia y bibliografia especifica de actividad."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables a nodos transversales.",
    "No transferir redaccion literal ni contenido tematico especifico de otra asignatura.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Mantener reglas curriculares especificas dentro de la misma materia.",
    "Aplicar compresion union-dedupe sin perdida en cada ciclo.",
    "Conservar bandera de riesgo historico por salidas no parseables en ciclos previos."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida en la materia (APA, ISO, institucional o juridica mexicana) [supuesto].",
    "Confirmar si el codigo local LDE-S2B1 es oficial o interno [supuesto].",
    "Confirmar si la fuente provisional heredada desde ingenieria debe retirarse por no pertinencia disciplinar [supuesto].",
    "Confirmar rubricas de evaluacion por actividad para calibrar profundidad argumentativa [supuesto]."
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
      "Producto juridico verificable con problema, fundamento, evidencia, analisis propio y cierre profesional.",
      "Sincronizacion transversal basada en reglas estables y no en contenido literal.",
      "Persistencia editorial con compresion lossless y sin regresion."
    ],
    "reason_for_being": [
      "Garantizar entregas consistentes, verificables y transferibles en la suite academica LaTeX.",
      "Convertir consignas en productos evaluables con trazabilidad institucional y tecnica."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion visible entre marco, analisis y cierre.",
      "Cierre con utilidad juridica practica."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo y doctrinal.",
      "Integrar evidencia verificable.",
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
          "justification": "El analisis requiere una pregunta juridica delimitada."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida depende de fundamento legal verificable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La argumentacion solida necesita respaldo comprobable."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "La consolidacion segura requiere estructura valida."
        }
      ],
      "evidence": [
        "README de la materia define estructura canonica y control editorial.",
        "Programa analitico define proposito y ejes de trabajo verificables.",
        "Archivo .bib local confirma base normativa e institucional."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas y se conservaron todas las utiles.",
      "Se agrego patron transversal de cinco ejes sin arrastrar contenido tematico de Filosofia.",
      "Se reforzo gate de JSON parseable como condicion de propagacion recursiva.",
      "Se mantuvo trazabilidad de supuestos y fuentes provisionales."
    ]
  }
}