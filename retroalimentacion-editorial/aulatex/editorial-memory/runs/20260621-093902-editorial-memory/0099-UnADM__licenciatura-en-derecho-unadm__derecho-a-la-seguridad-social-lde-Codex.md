{
  "summary": [
    "Se consolida sincronizacion transversal entre nodos no equivalentes con union-dedupe sin perdida.",
    "Se preserva identidad UnADM y enfoque juridico del destino.",
    "Se refuerza patron estable: problema, fundamento, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene gate critico de JSON parseable antes de propagacion recursiva.",
    "Se conserva alerta historica de salidas no estructuradas y normalizacion manual cuando aplique."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "No sobrescribir reglas validas previas; aplicar solo union y deduplicacion.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Tomar README y programa analitico del destino como canon estructural local.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Organizar por bloques: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por la planeacion semanal.",
    "Mantener consistencia entre reporte, presentacion y bibliografia local."
  ],
  "activity_rules": [
    "Delimitar problema y pregunta guia al inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Verificar coherencia entre objetivo, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Comprobar que la compresion aplicada sea lossless por union-dedupe."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificacion y acentos correctos en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion tecnica.",
    "Compilar sin errores criticos, sin referencias ni citas rotas.",
    "Normalizar nombres de archivos y corregir tokens o marcadores corruptos antes de compilar.",
    "Usar estructura minima: portada, desarrollo por ejes, conclusion y referencias."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central.",
    "Priorizar fuentes institucionales UnADM y normativas juridicas verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Agregar nuevas entradas solo si son verificables y pertinentes al destino."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo abstracciones editoriales estables.",
    "No transferir redaccion literal ni contenido tematico exclusivo de Filosofia del Derecho.",
    "Mantener reglas locales de Seguridad Social como prioridad de contexto.",
    "Reutilizar gates institucionales de calidad en nodos compatibles.",
    "Si aparece salida no parseable, ejecutar normalizacion manual antes de propagar.",
    "Preservar trazabilidad de reglas provisionales con etiqueta [supuesto]."
  ],
  "open_questions": [
    "Confirmar norma de citacion obligatoria del destino (APA, ISO, institucional o juridica mexicana) [supuesto].",
    "Confirmar si el codigo local LDE-S2B1 es oficial o interno [supuesto].",
    "Confirmar si persiste vigencia de fuente provisional heredada desde ingenieria [supuesto].",
    "Verificar si cada actividad exige reporte, presentacion u otro formato principal.",
    "Validar periodicidad de actualizacion de referencias legales vigentes (CPEUM, LSS, LISSSTE)."
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
      "Resolver consignas con metodo juridico verificable.",
      "Conectar problema, fundamento, evidencia, analisis y cierre.",
      "Preservar memoria editorial persistente sin regresiones."
    ],
    "reason_for_being": [
      "Estandarizar calidad editorial en productos academicos LaTeX.",
      "Permitir propagacion segura entre nodos por reglas estables.",
      "Sostener trazabilidad institucional y tecnica en cada ciclo."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion clara entre marco, analisis y conclusion.",
      "Cierre con utilidad juridica practica."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Presentar marco normativo y doctrinal pertinente.",
      "Contrastar evidencia verificable.",
      "Fijar postura propia sustentada.",
      "Concluir con implicacion juridica transferible."
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
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin delimitacion del problema no hay analisis juridico valido."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion requiere fundamento legal verificable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura propia gana solidez con fuentes comprobables."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion lossless por union-dedupe",
          "kind": "depends_on",
          "justification": "La consolidacion automatizada exige estructura valida."
        }
      ],
      "evidence": [
        "README del destino define estructura canonica y artefactos base.",
        "Programa analitico del destino fija proposito y ejes de trabajo.",
        "Archivo .bib local confirma base normativa e institucional verificable.",
        "Historial institucional registra salidas no parseables y necesidad de normalizacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 99: deduplicadas reglas repetidas en identidad, estructura y calidad.",
      "Ciclo 99: reforzado gate de JSON parseable como condicion de propagacion.",
      "Ciclo 99: transferidas solo abstracciones estables; sin mezclar contenido tematico de Filosofia.",
      "Ciclo 99: preservadas reglas utiles previas del destino sin recorte."
    ]
  }
}