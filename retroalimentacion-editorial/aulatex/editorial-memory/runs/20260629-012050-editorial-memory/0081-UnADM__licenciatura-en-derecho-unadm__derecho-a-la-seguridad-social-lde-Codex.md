{
  "summary": [
    "Se consolida sincronizacion transversal entre nodos no equivalentes con reglas estables y reutilizables.",
    "Se preserva identidad UnADM y contexto curricular local de Derecho a la Seguridad Social.",
    "Se refuerza patron comun: problema, conceptos/norma, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene compresion lossless por union-dedupe sin recorte ni regresion.",
    "Se conserva gate critico: no propagar sin JSON parseable y estructura minima valida."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica editorial.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No sobrescribir reglas validas previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README y programa analitico de la materia como canon estructural.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Organizar secciones en: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por planeacion semanal.",
    "Mantener consistencia entre reporte, presentacion y fuentes de la materia."
  ],
  "activity_rules": [
    "Delimitar problema y pregunta guia desde el inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir hechos, normas, doctrina y postura propia.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre objetivo, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar manualmente salidas no estructuradas antes de reutilizar.",
    "Confirmar respaldo verificable o marca [supuesto] en afirmaciones relevantes.",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Comprobar que la compresion aplicada sea union-dedupe sin perdida."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificacion correcta para espanol en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion tecnica.",
    "Compilar sin errores criticos, referencias rotas ni rutas corruptas.",
    "Normalizar nombres de archivo y resolver tokens sin expandir antes de compilar.",
    "Mantener metadatos institucionales y curriculares consistentes en todos los .tex."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central.",
    "Priorizar fuentes institucionales UnADM y normativas juridicas vigentes verificables.",
    "No inventar referencias; registrar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Agregar nuevas referencias solo cuando correspondan al producto solicitado."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales validadas en este ciclo.",
    "Compartir transversalmente abstracciones estables, no redaccion literal.",
    "No transferir contenido tematico propio de Filosofia del Derecho al destino.",
    "Mantener alerta de riesgo por historial de salida no parseable en ciclo 1.",
    "Aplicar estrategia progresiva y conservadora: reforzar sin desplazar reglas locales.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual."
  ],
  "open_questions": [
    "[supuesto] Confirmar norma de citacion exigida por la materia (APA, ISO, institucional o juridica mexicana).",
    "[supuesto] Confirmar si existe rubrica oficial por actividad para calibrar profundidad argumentativa.",
    "[supuesto] Confirmar datos faltantes de plantilla (figura docente) para metadatos finales.",
    "[supuesto] Verificar si la referencia provisional heredada desde ingenieria debe retirarse por irrelevante local.",
    "[supuesto] Confirmar si todas las plantillas de actividad listadas en README ya existen fisicamente."
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
      "Marco normativo y conceptual verificable.",
      "Evidencia citada y trazable.",
      "Analisis propio no descriptivo.",
      "Conclusion juridica aplicable."
    ],
    "reason_for_being": [
      "Convertir consignas en productos juridicos verificables y transferibles.",
      "Preservar identidad institucional sin perder adaptacion a cada actividad.",
      "Garantizar calidad reproducible mediante reglas parseables y trazables."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Uso explicito de etiqueta [supuesto] cuando falte evidencia local.",
      "Separacion clara entre marco, analisis y cierre.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo.",
      "Exponer marco normativo/doctrinal pertinente.",
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
          "justification": "Sin pregunta delimitada no hay analisis juridico riguroso."
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
          "justification": "La postura propia gana solidez con respaldo documental."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "La deduplicacion lossless exige estructura valida."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "Orienta el producto hacia utilidad academica y profesional."
        }
      ],
      "evidence": [
        "README de la materia define estructura canonica y artefactos base.",
        "Programa analitico define proposito y ejes de trabajo juridicos.",
        "Archivo .bib local concentra fuentes institucionales y normativas verificables.",
        "Historial institucional exige normalizacion manual ante salidas no parseables."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin perdida semantica.",
      "Se preservaron gates criticos de parseabilidad y trazabilidad.",
      "Se incorporo patron transversal estable desde origen sin mezclar contenido tematico especifico.",
      "Se mantuvieron reglas locales del destino como prioridad contextual.",
      "Se marcaron vacios de contexto como [supuesto] para validacion posterior."
    ]
  }
}