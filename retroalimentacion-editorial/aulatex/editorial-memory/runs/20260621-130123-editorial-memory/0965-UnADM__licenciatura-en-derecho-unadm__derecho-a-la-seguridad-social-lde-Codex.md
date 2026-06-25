{
  "summary": [
    "Se consolida sincronizacion transversal entre nodos no equivalentes con transferencia de reglas estables.",
    "Se preserva identidad UnADM y contexto curricular local de Derecho a la Seguridad Social.",
    "Se refuerza patron comun reusable: problema, fundamento, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene compresion lossless por union-dedupe sin recorte ni regresion.",
    "Se mantiene gate critico: no propagar si la salida no es JSON parseable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, metadatos y estructura.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar toda fuente heredada no verificada como provisional hasta confirmacion local.",
    "No sobrescribir reglas utiles previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar por secciones: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato pedido en planeacion semanal.",
    "Mantener consistencia entre README, programa analitico, reporte y presentacion.",
    "Usar estructura minima verificable: portada, desarrollo, conclusion y referencias."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Relacionar cada entrega con seguridad social cuando aplique.",
    "No asumir fuentes de otras semanas o materias sin validacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizar aguas abajo.",
    "Validar estructura minima completa antes de propagacion recursiva.",
    "Confirmar que cada afirmacion relevante tenga respaldo o [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que la compresion sea union-dedupe y no recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener metadatos institucionales y curriculares consistentes en .tex.",
    "Usar acentos y codificacion correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Evitar comandos no estandar sin justificacion tecnica.",
    "Corregir rutas, marcadores o tokens sin expandir antes de compilar."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente central local.",
    "Priorizar fuentes institucionales UnADM y normativas juridicas verificables.",
    "No inventar referencias; registrar solo obras consultables.",
    "Agregar solo referencias especificas de actividad con metadatos minimos completos.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Marcar como [supuesto] cualquier referencia heredada no confirmada."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo abstracciones editoriales estables.",
    "No transferir contenido tematico literal de Filosofia del Derecho al destino.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Mantener reglas locales del destino como capa superior de especificidad.",
    "Conservar alerta historica: ciclos con salida no parseable requieren normalizacion manual.",
    "Aplicar estrategia progresiva y conservadora en cada ciclo."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida en la materia (APA, ISO u otra) [supuesto].",
    "Confirmar si se usara codigo local LDE-S2B1 en todos los entregables [supuesto].",
    "Confirmar si la figura docente debe fijarse en plantilla base o por actividad [supuesto].",
    "Confirmar criterios de rubrica para ponderar analisis propio vs. marco normativo [supuesto]."
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
      "Producto juridico verificable con utilidad profesional.",
      "Patron estable: problema, fundamento, evidencia, analisis y conclusion.",
      "Control de calidad estructural antes de toda propagacion."
    ],
    "reason_for_being": [
      "Convertir consignas en entregables juridicos claros, sustentados y transferibles.",
      "Preservar memoria editorial persistente sin perdida ni regresion.",
      "Habilitar sincronizacion transversal segura entre nodos."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Separacion explicita entre marco, analisis y cierre.",
      "Etiquetado explicito de [supuesto] cuando falte verificacion.",
      "Cierre con implicacion juridica practica."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo y doctrinal.",
      "Contrastar evidencia verificable.",
      "Sostener postura propia.",
      "Concluir con efecto juridico aplicable."
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
          "justification": "La conclusion valida depende del fundamento legal."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura gana solidez con respaldo comprobable."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay consolidacion segura."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La identidad orienta tono, rigor y aplicabilidad profesional."
        }
      ],
      "evidence": [
        "README del destino define estructura canonica y control editorial.",
        "Programa analitico define proposito y ejes juridicos de trabajo.",
        "Archivo .bib local confirma base normativa e institucional.",
        "Historial previo confirma necesidad de normalizacion ante salidas no parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 22: se transfiere solo capa transversal estable desde actividad de Filosofia.",
      "Ciclo 22: se preservan reglas locales de Seguridad Social sin mezclar contenido tematico ajeno.",
      "Ciclo 22: se refuerzan gates de JSON parseable, evidencia verificable y union-dedupe lossless."
    ]
  }
}