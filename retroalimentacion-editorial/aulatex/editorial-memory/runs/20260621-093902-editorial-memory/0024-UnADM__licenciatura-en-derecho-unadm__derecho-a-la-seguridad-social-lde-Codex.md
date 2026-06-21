{
  "summary": [
    "Se consolida sincronizacion transversal entre nodos no equivalentes con transferencia de abstracciones estables.",
    "Se preserva identidad UnADM y enfoque juridico del destino sin mezclar contenido tematico de Filosofia del Derecho.",
    "Se refuerza patron editorial comun: problema, conceptos o norma, evidencia, analisis propio y conclusion juridica transferible.",
    "Se mantiene compresion lossless por union-dedupe y politica de no regresion.",
    "Se conserva control de riesgo por antecedentes de salidas no parseables y normalizacion obligatoria."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local [supuesto].",
    "No sobrescribir reglas validas previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README y programa analitico de la materia como canon estructural.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones reutilizables: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Alinear formato final al producto solicitado en planeacion semanal."
  ],
  "activity_rules": [
    "Definir problema y objetivo de actividad desde el inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir hechos, conceptos, normas y opinion propia.",
    "Incluir postura argumentada del estudiante; evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Ajustar alcance y formato al producto solicitado por la consigna."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizar aguas abajo.",
    "Validar estructura minima completa antes de propagacion recursiva.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Verificar que la compresion aplicada sea union-dedupe sin recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificacion y acentos correctos en espanol en .tex y .bib.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Normalizar rutas y nombres con tokens o caracteres corruptos antes de compilar.",
    "Mantener consistencia de metadatos institucionales y curriculares en archivos .tex."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central local.",
    "Priorizar fuentes institucionales UnADM y normativas juridicas verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Agregar nuevas fuentes solo si son verificables y pertinentes a la consigna."
  ],
  "propagation_hints": [
    "Propagar lateral y recursivamente solo reglas generales validadas en este ciclo.",
    "Transferir abstracciones editoriales estables; no transferir redaccion literal ni contenido tematico ajeno.",
    "Mantener reglas locales del destino como prioridad sobre heredadas transversales.",
    "Conservar bandera de riesgo historica: ciclo 1 requiere normalizacion manual si se reutiliza.",
    "Reforzar gates de JSON, trazabilidad de supuestos y control bibliografico en nodos compatibles."
  ],
  "open_questions": [
    "Confirmar norma de citacion requerida por la materia (APA, ISO, institucional o juridica mexicana) [supuesto].",
    "Confirmar si sigue vigente una fuente provisional heredada desde ingenieria para este destino [supuesto].",
    "Verificar nombres canonicos de plantillas de Actividad 1 en README contra archivos reales.",
    "Confirmar dato oficial de figura docente para completar portada cuando aplique.",
    "Confirmar si hay rubrica especifica por actividad para ajustar profundidad argumentativa [supuesto]."
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
      "Producto juridico verificable con problema, fundamento, evidencia, analisis, postura y cierre.",
      "Sincronizacion transversal por patrones editoriales estables.",
      "Conservacion de identidad institucional y trazabilidad de supuestos."
    ],
    "reason_for_being": [
      "Estandarizar calidad editorial entre actividades y materias sin perder contexto local.",
      "Garantizar entregables consistentes, verificables y utiles para practica juridica.",
      "Permitir memoria persistente con compresion lossless y sin regresion."
    ],
    "style_markers": [
      "Frases directas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion visible entre marco, analisis y cierre.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo o doctrinal.",
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
          "justification": "El analisis requiere una pregunta delimitada."
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
          "justification": "La postura se fortalece con respaldo comprobable."
        },
        {
          "source": "JSON parseable",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay reutilizacion segura."
        },
        {
          "source": "Compresion union-dedupe",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Evita duplicados y conserva reglas utiles sin recorte."
        }
      ],
      "evidence": [
        "README de materia define estructura canonica y plantillas base.",
        "Programa analitico define proposito y ejes juridicos verificables.",
        "Archivo .bib local confirma base normativa e institucional.",
        "Historial institucional registra riesgo por salidas no parseables y exige normalizacion."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas de identidad, estructura, calidad y bibliografia.",
      "Se transfirieron solo abstracciones estables desde actividad de Filosofia del Derecho.",
      "Se evito transferir contenido doctrinal especifico de Filosofia al destino de Seguridad Social.",
      "Se reforzaron gates criticos: JSON parseable, respaldo verificable y marca de [supuesto].",
      "Se mantuvo politica de no regresion y compresion lossless por union-dedupe."
    ]
  }
}