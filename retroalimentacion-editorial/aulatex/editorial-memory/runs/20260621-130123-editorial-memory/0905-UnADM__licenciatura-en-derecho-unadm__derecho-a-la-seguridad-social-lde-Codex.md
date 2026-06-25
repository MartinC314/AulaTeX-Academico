{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia progresiva y conservadora.",
    "Se preservan reglas utiles del destino y se integran abstracciones estables del origen sin mezclar contenido tematico.",
    "Se refuerza patron editorial comun: problema, conceptos o norma, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene normalizacion estructurada obligatoria antes de propagacion recursiva.",
    "Se conserva alerta institucional por antecedentes de salidas no parseables y necesidad de normalizacion manual en ciclos heredados."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "No sobrescribir reglas validas previas; aplicar union y deduplicacion sin regresion.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Tomar README y programa analitico del destino como canon estructural.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar desarrollo en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato y alcance al producto solicitado en planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Delimitar pregunta guia de la actividad desde el inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Distinguir hechos, conceptos, normas y opinion propia.",
    "Verificar coherencia entre objetivo, desarrollo y conclusion.",
    "Relacionar cada entrega con Derecho a la Seguridad Social cuando corresponda."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Comprobar que la compresion sea lossless por union-dedupe y no por recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de materia y personalizar solo campos variables.",
    "Mantener codificacion correcta para espanol en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, sin referencias rotas y con rutas validas.",
    "Normalizar nombres de archivo y resolver marcadores o tokens no expandidos antes de compilar.",
    "Mantener consistencia entre reporte y presentacion de la materia."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central.",
    "Priorizar fuentes institucionales UnADM y marco juridico verificable.",
    "No inventar referencias; agregar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente editorial o URL.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "Verificar que toda cita en LaTeX tenga entrada BibTeX correspondiente."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y parseables en este ciclo.",
    "Compartir a laterales solo abstracciones editoriales estables, no redaccion literal.",
    "Mantener reglas locales del destino cuando exista potencial conflicto tematico.",
    "Reutilizar reglas institucionales de calidad, trazabilidad y control bibliografico.",
    "Mantener bandera de riesgo para ciclos con salida no parseable hasta su saneamiento."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida por la materia (APA, ISO, institucional o juridica mexicana) [supuesto].",
    "Confirmar vigencia de reglas provisionales heredadas desde nodos no juridicos [supuesto].",
    "Confirmar si todas las actividades de la materia exigen reporte, presentacion o formato mixto.",
    "Verificar si existe rubrica oficial por actividad para ajustar profundidad argumentativa.",
    "Confirmar campos institucionales pendientes en plantilla (figura docente) [supuesto]."
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
      "Marco conceptual y normativo pertinente.",
      "Evidencia verificable y trazable.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar cada consigna en producto juridico verificable y util para la practica profesional.",
      "Conservar memoria editorial persistente sin perdida de reglas utiles.",
      "Habilitar sincronizacion transversal segura entre nodos no equivalentes."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion visible entre marco, analisis y cierre.",
      "Trazabilidad de fuentes y reglas provisionales."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo.",
      "Exponer marco normativo o doctrinal.",
      "Presentar evidencia relevante.",
      "Desarrollar analisis propio.",
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
          "justification": "Sin delimitacion del problema no hay argumentacion consistente."
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
          "justification": "La postura propia se fortalece con fuentes trazables."
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
        "Programa analitico del destino fija proposito y ejes de trabajo.",
        "Archivo .bib local confirma base institucional y normativa verificable.",
        "Memoria heredada exige normalizacion manual para salidas no parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 7: deduplicadas reglas repetidas en identidad, estructura, calidad y bibliografia.",
      "Ciclo 7: transferidas solo abstracciones estables del origen transversal.",
      "Ciclo 7: preservadas reglas locales del destino para seguridad social.",
      "Ciclo 7: reforzado gate de JSON parseable y compresion lossless por union-dedupe."
    ]
  }
}