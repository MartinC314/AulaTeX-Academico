{
  "summary": [
    "Se sincroniza ADN editorial transversal sin mezclar contenido tematico de Filosofia del Derecho.",
    "Se preserva identidad UnADM, estructura por ejes y cierre juridico transferible.",
    "Se mantiene compresion lossless por union-dedupe y sin regresion.",
    "Se refuerza gate critico: bloquear propagacion si no hay JSON parseable.",
    "Se incorpora canon local confirmado por README: incluye plantillas de Actividad 1 en reporte y presentacion.",
    "Se conserva alerta historica de normalizacion manual para salidas no estructuradas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Mantener trazabilidad de reglas heredadas provisionales con etiqueta [supuesto].",
    "No sobrescribir reglas validas previas; solo unir y deduplicar.",
    "No transferir datos personales entre nodos salvo instruccion explicita [supuesto]."
  ],
  "structure_rules": [
    "Tomar README y programa analitico locales como canon estructural.",
    "Alinear toda entrega a ejes: problema, fundamento, evidencia, analisis propio y conclusion.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar desarrollo en conceptos clave, marco normativo/doctrinal, analisis y cierre.",
    "Cerrar con conclusion juridica aplicable a practica profesional.",
    "Ajustar formato al producto pedido en planeacion semanal."
  ],
  "activity_rules": [
    "Distinguir hechos, normas, doctrina y postura propia.",
    "Evitar entregas solo descriptivas.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Relacionar cada actividad con derecho a la seguridad social cuando corresponda."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar manualmente respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de propagacion recursiva.",
    "Confirmar respaldo verificable o marca [supuesto] en afirmaciones relevantes.",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Verificar correspondencia entre producto final y consigna de actividad."
  ],
  "latex_rules": [
    "Conservar plantilla base de materia y personalizar solo campos variables.",
    "Mantener codificacion correcta en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estandar sin justificacion tecnica.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir rutas o nombres de archivo corruptos antes de compilar.",
    "Usar estructura minima: portada, desarrollo por ejes, conclusion y referencias."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente central local.",
    "Priorizar fuentes institucionales UnADM y normas juridicas vigentes verificables.",
    "Agregar solo referencias consultables y pertinentes a la actividad.",
    "No inventar fuentes.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad."
  ],
  "propagation_hints": [
    "Propagar lateral y arriba solo reglas generales validadas.",
    "No propagar contenido tematico especifico de Filosofia a Seguridad Social.",
    "Propagar identidad, gates de calidad, patron argumentativo y control bibliografico.",
    "Mantener bandera de riesgo por historial de salidas no parseables en ciclos tempranos.",
    "Aplicar compresion union-dedupe en cada ciclo para evitar regresion."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida por la materia (APA, ISO, institucional o juridica mexicana) [supuesto].",
    "Confirmar si codigo local LDE-S2B1 es oficial en todos los entregables [supuesto].",
    "Confirmar si la figura docente debe quedar como pendiente en plantillas de Actividad 1.",
    "Verificar vigencia de toda fuente provisional heredada desde nodos no juridicos [supuesto]."
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
      "Evidencia pertinente.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir cada consigna en producto juridico verificable y util para practica profesional.",
      "Sostener coherencia editorial entre reporte, presentacion y actividad."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Separacion explicita entre marco, analisis y cierre.",
      "Marcado visible de [supuesto] cuando falte verificacion.",
      "Cierre con utilidad juridica practica."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo y doctrinal.",
      "Contrastar evidencia.",
      "Fijar postura propia.",
      "Concluir con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "JSON parseable",
        "Compresion union-dedupe",
        "Problema juridico",
        "Marco normativo",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Derecho a la seguridad social"
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
          "source": "JSON parseable",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay reutilizacion segura."
        },
        {
          "source": "Compresion union-dedupe",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Conserva reglas utiles sin perdida."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere pregunta delimitada."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida exige fundamento legal."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Coherencia transversal de entregas",
          "kind": "supports",
          "justification": "Mantiene estandar comun entre nodos."
        }
      ],
      "evidence": [
        "README local confirma estructura canonica y plantillas de Actividad 1.",
        "Programa analitico local define proposito y ejes de trabajo.",
        "Bib local confirma base normativa institucional y legal verificable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 95: se transfieren solo abstracciones estables transversales.",
      "Ciclo 95: se preservan reglas locales del destino y se evita mezcla tematica no equivalente.",
      "Ciclo 95: se refuerzan gates JSON, trazabilidad [supuesto] y consistencia cita-bib."
    ]
  }
}