{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia conservadora y sin regresion.",
    "Se preserva identidad UnADM y enfoque juridico del destino.",
    "Se refuerza patron estable: problema, fundamento, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene regla dura: no propagar salidas no parseables sin normalizacion.",
    "Compresion aplicada por union-dedupe lossless."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No sobrescribir reglas validas previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README de materia como canon estructural local.",
    "Alinear cada entrega a ejes: problema, conceptos/norma, producto, analisis y conclusion.",
    "Separar desarrollo en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Ajustar formato al producto pedido en planeacion semanal.",
    "Mantener consistencia entre reporte, presentacion y programa analitico."
  ],
  "activity_rules": [
    "Delimitar el problema juridico o social al inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar solo descripcion.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar manualmente respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que la compresion sea union-dedupe y no recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de materia y personalizar solo campos variables.",
    "Mantener codificacion y acentos correctos en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Normalizar rutas y nombres de archivo antes de compilar.",
    "Resolver tokens sin expandir en README y programa analitico cuando aparezcan."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente central local.",
    "Priorizar fuentes institucionales UnADM y normativas vigentes verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Agregar solo referencias nuevas con verificacion previa."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales ya validadas.",
    "Transferir abstracciones estables, no redaccion literal ni contenido tematico de filosofia.",
    "Conservar reglas locales de seguridad social como prioridad de destino.",
    "Mantener bandera de riesgo por antecedente de salida no parseable en ciclo 1.",
    "Evitar regresiones sobre identidad, estructura y control bibliografico."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida por la materia (APA, ISO o institucional) [supuesto].",
    "Confirmar si codigo local LDE-S2B1 es oficial en todos los entregables [supuesto].",
    "Confirmar si Actividad 1 de la materia exige reporte, presentacion o ambos.",
    "Verificar vigencia de cualquier fuente provisional heredada de nodos no juridicos [supuesto]."
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
      "Producto juridico verificable con estructura estable.",
      "Prioridad en fundamento normativo y evidencia.",
      "Analisis propio con cierre profesional transferible."
    ],
    "reason_for_being": [
      "Convertir consignas en entregables juridicos claros, verificables y utiles para practica.",
      "Preservar memoria editorial persistente sin perdida por deduplicacion."
    ],
    "style_markers": [
      "Frases directas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion visible entre marco, analisis y cierre.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo y doctrinal.",
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
          "justification": "Sin problema delimitado no hay argumentacion valida."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion exige fundamento legal verificable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura debe sostenerse con fuentes trazables."
        },
        {
          "source": "JSON parseable",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "La reutilizacion segura requiere estructura valida."
        },
        {
          "source": "Compresion union-dedupe",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Preserva reglas utiles sin duplicar ni recortar."
        }
      ],
      "evidence": [
        "README de la materia define estructura canonica y artefactos.",
        "Programa analitico define proposito y ejes de trabajo.",
        "Archivo .bib local confirma base normativa e institucional."
      ]
    },
    "reinforcement_log": [
      "Ciclo 89: se refuerza ADN transversal sin mezclar contenido tematico no equivalente.",
      "Ciclo 89: se preservan reglas duras de parseo JSON y normalizacion previa.",
      "Ciclo 89: se mantiene compresion lossless por union-dedupe y sin regresion."
    ]
  }
}