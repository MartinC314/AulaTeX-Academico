{
  "summary": [
    "Se consolida sincronizacion transversal entre nodos no equivalentes con reglas editoriales estables.",
    "Se preserva identidad UnADM y contexto local de Derecho a la Seguridad Social sin mezclar contenido tematico de Filosofia del Derecho.",
    "Se refuerza patron comun reusable: problema, conceptos o norma, evidencia, analisis propio y conclusion juridica transferible.",
    "Se mantiene compresion lossless por union-dedupe y sin regresion.",
    "Se mantiene alerta institucional: bloquear propagacion de salidas no JSON parseable y normalizar antes de reutilizar."
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
    "Tomar README y programa analitico del destino como canon estructural.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Organizar en secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato y alcance al producto solicitado por la planeacion semanal.",
    "Mantener consistencia entre reporte, presentacion y bibliografia local."
  ],
  "activity_rules": [
    "Delimitar problema juridico desde el inicio.",
    "Distinguir hechos, conceptos, normas y postura propia.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas; incluir argumentacion propia.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica aplicable a practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar manualmente respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar correspondencia entre consigna, producto entregado y estructura final.",
    "Comprobar consistencia entre citas en texto y archivo .bib local."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener metadatos institucionales y curriculares consistentes.",
    "Evitar comandos no estandar sin justificacion tecnica.",
    "Corregir rutas, nombres y tokens sin expandir antes de compilar.",
    "Compilar sin errores criticos, sin referencias rotas y con claves BibTeX estables."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central.",
    "Priorizar fuentes institucionales UnADM y normativa juridica verificable.",
    "Agregar solo referencias consultables con metadatos minimos completos.",
    "No inventar fuentes; registrar faltantes como pendientes o [supuesto].",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Verificar que cada cita tenga entrada BibTeX correspondiente."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales estables ya validadas.",
    "No transferir redaccion literal ni contenido tematico especifico de Filosofia del Derecho.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Conservar reglas locales del destino como autoridad primaria.",
    "Mantener bandera de riesgo por historico de salidas no parseables en ciclos previos.",
    "Aplicar siempre compresion union-dedupe sin perdida."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida en la materia (APA, ISO, juridica mexicana o institucional) [supuesto].",
    "Confirmar si codigo local LDE-S2B1 es oficial o solo operativo [supuesto].",
    "Confirmar si persiste alguna fuente provisional heredada de nodos no juridicos y depurarla [supuesto].",
    "Confirmar campos pendientes de portada (figura docente) para plantillas de actividad [supuesto]."
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
      "Marco normativo y conceptual pertinente.",
      "Evidencia verificable.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir consignas en productos juridicos verificables y profesionalmente utiles.",
      "Preservar coherencia institucional y calidad tecnica en toda entrega.",
      "Permitir reutilizacion transversal segura sin perder contexto local."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion clara entre marco, analisis y cierre.",
      "Trazabilidad de fuentes y decisiones editoriales."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo.",
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
          "justification": "Sin delimitacion del problema no hay argumentacion valida."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion debe descansar en fundamento legal verificable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura personal requiere respaldo contrastable."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "La consolidacion segura exige estructura valida."
        }
      ],
      "evidence": [
        "README del destino define estructura canonica y activos editoriales.",
        "Programa analitico del destino define proposito y ejes de trabajo.",
        "Archivo .bib local confirma base normativa e institucional verificable.",
        "Historico institucional registra incidentes de salida no parseable y necesidad de normalizacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 10: se transfieren solo abstracciones estables del origen.",
      "Ciclo 10: se evita importar contenido disciplinar especifico de Filosofia del Derecho.",
      "Ciclo 10: se refuerzan quality gates de parseo JSON, supuestos y control bibliografico.",
      "Ciclo 10: se preservan reglas utiles previas del destino sin eliminacion."
    ]
  }
}