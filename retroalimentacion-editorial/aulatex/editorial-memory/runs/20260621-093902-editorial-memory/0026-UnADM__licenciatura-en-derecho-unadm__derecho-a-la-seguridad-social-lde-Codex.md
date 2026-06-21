{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre nodos no equivalentes.",
    "Se preservan reglas utiles del destino y se integran abstracciones estables del origen.",
    "Se mantiene compresion lossless por union y deduplicacion sin regresion.",
    "Se refuerza patron editorial comun: problema, fundamento, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene alerta institucional por antecedentes de salida no parseable y necesidad de normalizacion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Mantener trazabilidad de reglas heredadas provisionales con etiqueta [supuesto].",
    "No sobrescribir reglas validas previas; solo unir y deduplicar.",
    "No transferir contenido tematico literal de Filosofia del Derecho a Seguridad Social."
  ],
  "structure_rules": [
    "Tomar README y programa analitico del destino como canon estructural local.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar desarrollo en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear formato y alcance al producto solicitado por la planeacion semanal."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Marcar como [supuesto] cualquier dato no visible en consigna o fuente local.",
    "Relacionar cada actividad con Derecho a la Seguridad Social cuando corresponda."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizar aguas abajo.",
    "Validar estructura minima completa antes de propagacion recursiva.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Verificar que no se eliminen reglas utiles previas durante consolidacion."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificacion correcta en espanol en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, referencias rotas ni rutas corruptas.",
    "Normalizar nombres de archivo y resolver marcadores o tokens sin expandir antes de compilar.",
    "Usar estructura minima: portada, desarrollo por ejes, conclusion y referencias."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central.",
    "Priorizar fuentes institucionales y normativas verificables.",
    "Agregar solo referencias consultables con metadatos minimos completos.",
    "No inventar fuentes; registrar faltantes como pendientes o [supuesto].",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "Verificar correspondencia uno a uno entre claves citadas y entradas BibTeX."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo abstracciones estables, no redaccion literal.",
    "Propagar reglas generales de identidad, calidad JSON y control bibliografico a laterales compatibles.",
    "Mantener reglas curriculares especificas dentro de la materia destino.",
    "Aplicar estrategia progresiva y conservadora: agregar mejoras verificables sin borrar legado util.",
    "Si un nodo receptor esta vacio, crear cerebro editorial minimo con vacios abiertos.",
    "Registrar en log cada refuerzo para auditoria de no regresion."
  ],
  "open_questions": [
    "Confirmar norma de citacion obligatoria de la materia (APA, ISO, institucional o juridica mexicana) [supuesto].",
    "Confirmar rubricas oficiales por actividad para ajustar profundidad argumentativa [supuesto].",
    "Verificar vigencia semestral de enlaces normativos en el .bib local.",
    "Confirmar datos faltantes de plantilla (figura docente) antes de cierre final.",
    "Validar si persiste o se descarta la fuente provisional heredada de otro programa academico [supuesto]."
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
      "Transformar cada consigna en producto juridico verificable y util profesionalmente.",
      "Sostener continuidad editorial entre actividades sin perder contexto local.",
      "Garantizar calidad tecnica y argumentativa en flujos LaTeX y bibliografia."
    ],
    "style_markers": [
      "Frases directas y accionables.",
      "Separacion visible entre marco, analisis y cierre.",
      "Marcado explicito de [supuesto] cuando falte verificacion.",
      "Trazabilidad de fuentes y decisiones editoriales."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Presentar marco normativo y doctrinal.",
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
          "justification": "El analisis requiere una pregunta juridica delimitada."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida exige fundamento legal verificable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura propia debe sustentarse con fuentes trazables."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "La consolidacion lossless requiere estructura valida."
        }
      ],
      "evidence": [
        "README del destino define estructura canonica y artefactos base.",
        "Programa analitico del destino define proposito y ejes de trabajo.",
        "Archivo .bib local confirma base normativa e institucional verificable.",
        "Memoria origen aporta patron estable de argumentacion transferible sin contenido literal."
      ]
    },
    "reinforcement_log": [
      "Ciclo 26: se refuerza gate de JSON parseable como condicion de propagacion.",
      "Ciclo 26: se integra patron comun de cinco ejes argumentativos como abstraccion transversal.",
      "Ciclo 26: se preservan reglas locales de Seguridad Social y se evita mezcla tematica con Filosofia.",
      "Ciclo 26: se consolida deduplicacion semantica en identidad, estructura, calidad y bibliografia."
    ]
  }
}