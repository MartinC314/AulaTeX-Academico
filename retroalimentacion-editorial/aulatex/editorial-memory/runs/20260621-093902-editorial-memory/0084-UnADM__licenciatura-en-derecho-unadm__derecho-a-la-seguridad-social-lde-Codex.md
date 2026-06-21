{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre actividad de Filosofia del Derecho y materia de Seguridad Social.",
    "Se preserva identidad UnADM, estructura por ejes y control de calidad sin mezclar contenido tematico no equivalente.",
    "Se refuerza compresion lossless por union-dedupe y no regresion de reglas utiles previas.",
    "Se mantiene alerta institucional por salidas no parseables historicas y normalizacion manual obligatoria cuando aplique.",
    "Se confirma que el destino ya tiene cerebro editorial minimo; se agregan solo abstracciones estables reutilizables."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No sobrescribir reglas validas previas; aplicar solo union-dedupe sin regresion.",
    "No propagar datos personales de plantilla a nodos laterales salvo requerimiento explicito [supuesto]."
  ],
  "structure_rules": [
    "Tomar README y programa analitico del destino como canon estructural local.",
    "Definir objetivo puntual antes del desarrollo.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Organizar el desarrollo en: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato y alcance al producto solicitado por la planeacion semanal.",
    "Mantener consistencia entre reporte, presentacion y referencias."
  ],
  "activity_rules": [
    "Distinguir hechos, conceptos, normas y opinion propia.",
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Evitar entregas solo descriptivas; exigir postura argumentada del estudiante.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Relacionar cada actividad con el campo de seguridad social cuando corresponda."
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
    "Mantener compatibilidad de compilacion; evitar comandos no estandar sin justificacion.",
    "Usar acentos y codificacion correcta en español en .tex y .bib.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Normalizar rutas y nombres de archivo antes de compilar.",
    "Resolver tokens o marcadores sin expandir en README y programa analitico si aparecen."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central del destino.",
    "Priorizar fuentes institucionales y juridicas verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente/URL.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "No asumir que bibliografia de otra materia aplica automaticamente al destino [supuesto]."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo abstracciones editoriales estables, no redaccion literal.",
    "Propagar a nodos no equivalentes solo reglas de identidad, estructura reusable y gates de calidad.",
    "Conservar reglas locales del destino sobre seguridad social sin contaminar con contenido disciplinar de filosofia.",
    "Mantener bandera de riesgo por historico de no-parseable en ciclos tempranos.",
    "Aplicar estrategia progresiva y conservadora: agregar mejoras verificables, sin recorte."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida en la materia (APA, ISO, institucional o juridica mexicana) [supuesto].",
    "Confirmar si el codigo local de curso LDE-S2B1 es oficial o solo operativo [supuesto].",
    "Confirmar si persiste alguna fuente provisional heredada de ingenieria y depurarla si no aplica [supuesto].",
    "Confirmar rubrica vigente por actividad para ajustar profundidad argumentativa."
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
      "Fundamento normativo y doctrinal verificable.",
      "Evidencia trazable.",
      "Analisis propio no descriptivo.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir consignas en productos juridicos verificables y utiles profesionalmente.",
      "Preservar memoria editorial persistente con compresion lossless por deduplicacion.",
      "Habilitar sincronizacion transversal sin perder contexto local."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion visible entre marco, analisis y cierre.",
      "Cierre con utilidad practica."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo/doctrinal.",
      "Contrastar evidencia relevante.",
      "Sostener postura propia.",
      "Concluir con implicacion juridica aplicada."
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
        "Conclusion juridica transferible"
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
          "justification": "La conclusion requiere fundamento legal verificable."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "La deduplicacion segura exige estructura valida."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "La integridad academica institucional exige trazabilidad de fuentes."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La transferencia profesional surge de razonamiento propio sustentado."
        }
      ],
      "evidence": [
        "README del destino define estructura canonica y control editorial.",
        "Programa analitico del destino fija proposito y ejes de trabajo.",
        "Archivo .bib local confirma base institucional y normativa verificable.",
        "Historico institucional reporta salidas no parseables; se mantiene gate de normalizacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 84: se integran reglas estables transversales desde actividad de filosofia sin importar contenido tematico.",
      "Ciclo 84: se deduplican reglas repetidas y se preservan todas las utiles del destino.",
      "Ciclo 84: se refuerzan gates de JSON parseable, trazabilidad de supuestos y control bibliografico.",
      "Ciclo 84: se mantiene estrategia progresiva-conservadora y sincronizacion transversal."
    ]
  }
}