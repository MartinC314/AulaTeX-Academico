{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre nodos no equivalentes.",
    "Se preserva identidad UnADM y enfoque juridico del destino sin mezclar contenido tematico de Filosofia del Derecho.",
    "Se refuerza patron editorial estable: problema, conceptos o norma, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene compresion lossless por union-dedupe y sin regresion.",
    "Se conserva alerta de normalizacion manual para salidas no parseables de ciclos previos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No sobrescribir reglas validas previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README y programa analitico como canon estructural local.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar desarrollo en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear formato al producto solicitado por la planeacion semanal."
  ],
  "activity_rules": [
    "Delimitar problema juridico desde el inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Relacionar cada actividad con seguridad social cuando corresponda."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar manualmente respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de propagar recursivamente.",
    "Confirmar respaldo verificable o marca [supuesto] en toda afirmacion relevante.",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Verificar que la compresion aplicada sea union-dedupe sin recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener consistencia de metadatos institucionales y de curso en todos los .tex.",
    "Usar estructura minima: portada, desarrollo por ejes, conclusion y referencias.",
    "Evitar comandos no estandar sin justificacion editorial o tecnica.",
    "Compilar sin errores criticos, sin referencias rotas y con rutas limpias.",
    "Corregir nombres con marcadores o tokens no expandidos antes de compilar."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central.",
    "Priorizar fuentes institucionales UnADM y normativas juridicas vigentes verificables.",
    "No inventar referencias; registrar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Verificar que toda clave citada exista en el .bib local."
  ],
  "propagation_hints": [
    "Propagar lateral y hacia arriba solo reglas generales estables y validadas.",
    "No transferir redaccion literal ni contenido tematico especifico de Filosofia del Derecho.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Mantener reglas locales del destino como capa principal.",
    "Conservar bandera de riesgo historica: ciclo 1 requiere normalizacion manual si se reutiliza.",
    "Aplicar estrategia progresiva y conservadora: sumar mejoras verificables sin borrar reglas utiles."
  ],
  "open_questions": [
    "Confirmar si el codigo local LDE-S2B1 es oficial o interno [supuesto].",
    "Confirmar norma de citacion exigida por materia (APA, ISO, institucional o juridica mexicana) [supuesto].",
    "Confirmar nombre de figura docente para portada cuando exista dato oficial.",
    "Confirmar vigencia de cualquier fuente provisional heredada desde nodos no juridicos [supuesto]."
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
      "Marco normativo y doctrinal pertinente.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar consignas en productos juridicos verificables con utilidad profesional.",
      "Asegurar consistencia editorial entre reporte, presentacion y evidencias.",
      "Preservar memoria institucional reusable sin perdida semantica."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion visible entre marco, analisis y cierre.",
      "Cierre con implicacion juridica practica."
    ],
    "argumentative_patterns": [
      "Encuadre del problema.",
      "Objetivo puntual.",
      "Marco normativo o doctrinal.",
      "Contraste de evidencia.",
      "Postura propia sustentada.",
      "Conclusion aplicable."
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
          "justification": "La postura argumentada exige respaldo documental."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "La deduplicacion lossless requiere estructura valida."
        }
      ],
      "evidence": [
        "README local define estructura canonica y control editorial.",
        "Programa analitico local define proposito y ejes juridicos.",
        "Archivo .bib local confirma base institucional y normativa vigente.",
        "Regla transversal heredada valida: normalizar salidas no estructuradas antes de propagar."
      ]
    },
    "reinforcement_log": [
      "Ciclo 7: se reforzo patron comun de cinco ejes sin trasladar contenido disciplinar de Filosofia.",
      "Ciclo 7: se mantuvo gate duro de JSON parseable para propagacion recursiva.",
      "Ciclo 7: se conservaron reglas locales de seguridad social y control bibliografico.",
      "Ciclo 7: se deduplico memoria con estrategia lossless y sin regresion."
    ]
  }
}