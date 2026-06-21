{
  "summary": [
    "Se consolida sincronizacion transversal entre actividad de Filosofia del Derecho y materia de Seguridad Social.",
    "Se preservan reglas utiles previas del destino sin regresion.",
    "Se refuerza patron estable: problema, fundamento, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene control estricto de JSON parseable y normalizacion previa a propagacion.",
    "Se conserva separacion entre abstracciones editoriales transferibles y contenido tematico local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No sobrescribir reglas validas previas; aplicar union-dedupe sin recorte."
  ],
  "structure_rules": [
    "Tomar README y programa analitico del destino como canon estructural.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar desarrollo en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas; exigir postura argumentada del estudiante.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Relacionar actividad con seguridad social cuando corresponda al objetivo local.",
    "No asumir fuentes de otras semanas sin validacion de consigna."
  ],
  "quality_gates": [
    "Bloquear propagacion si salida no es JSON parseable.",
    "Revisar y normalizar manualmente toda salida no estructurada antes de reutilizar.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo verificable o marca [supuesto] en toda afirmacion relevante.",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Verificar que la compresion aplicada sea lossless por union-dedupe."
  ],
  "latex_rules": [
    "Conservar plantilla base de materia y personalizar solo campos variables.",
    "Mantener codificacion y acentos correctos en espanol en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Normalizar nombres de archivo y resolver marcadores corruptos o tokens sin expandir antes de compilar.",
    "Mantener consistencia de metadatos institucionales entre reporte y presentacion."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central.",
    "Priorizar fuentes institucionales UnADM y normas juridicas vigentes verificables.",
    "No inventar referencias; registrar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente editorial o URL.",
    "Distinguir bibliografia base de materia y bibliografia especifica de actividad.",
    "Agregar nuevas fuentes solo si son pertinentes a la consigna local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales validadas y parseables.",
    "Compartir a laterales no equivalentes solo abstracciones estables de identidad, estructura y calidad.",
    "No transferir redaccion literal ni contenido tematico especifico de Filosofia del Derecho.",
    "Mantener bandera de riesgo historico por ciclos con salida no parseable.",
    "Aplicar estrategia progresiva y conservadora: reforzar sin sustituir."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida en la materia (APA, ISO, institucional o juridica mexicana) [supuesto].",
    "Confirmar rubrica oficial de evaluacion por actividad para ajustar profundidad argumentativa [supuesto].",
    "Confirmar si el codigo local LDE-S2B1 es oficial en todos los entregables [supuesto].",
    "Confirmar vigencia de cualquier fuente provisional heredada de nodos no juridicos [supuesto]."
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
      "Resolver consignas con trazabilidad juridica y estructura verificable.",
      "Sostener toda conclusion en problema delimitado, norma aplicable y evidencia.",
      "Preservar memoria editorial sin perdida por deduplicacion."
    ],
    "reason_for_being": [
      "Convertir cada actividad en producto juridico util, verificable y evaluable.",
      "Asegurar continuidad editorial entre nodos con identidad institucional comun.",
      "Reducir riesgo de errores de forma mediante gates tecnicos y documentales."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Separacion visible entre marco, analisis y cierre.",
      "Etiquetado explicito de [supuesto].",
      "Cierre con implicacion profesional."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo y doctrinal pertinente.",
      "Contrastar evidencia y criterios aplicables.",
      "Fijar postura propia sustentada.",
      "Concluir con efecto juridico practico."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema juridico delimitado",
        "Marco normativo verificable",
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
          "justification": "Sin problema claro no hay argumentacion consistente."
        },
        {
          "source": "Marco normativo verificable",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La validez de la conclusion depende del fundamento legal."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura academica requiere respaldo comprobable."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion lossless por union-dedupe",
          "kind": "depends_on",
          "justification": "La consolidacion segura exige estructura valida."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "El sello institucional orienta claridad, rigor y utilidad profesional."
        }
      ],
      "evidence": [
        "README del destino define estructura canonica y control editorial.",
        "Programa analitico del destino fija proposito y ejes juridicos de trabajo.",
        ".bib local del destino confirma base normativa e institucional verificable.",
        "Memoria historica exige normalizacion de salidas no parseables antes de propagacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 31: se transfirieron solo abstracciones estables desde nodo transversal no equivalente.",
      "Ciclo 31: se reforzaron gates de parseo JSON, evidencia y consistencia bib sin eliminar reglas locales.",
      "Ciclo 31: se mantuvo separacion entre contenido tematico de Filosofia y marco local de Seguridad Social.",
      "Ciclo 31: consolidacion realizada con union-dedupe lossless y sin regresion."
    ]
  }
}