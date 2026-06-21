{
  "summary": [
    "Se consolida sincronizacion transversal sin mezclar contenido tematico entre materias.",
    "Se preserva identidad UnADM, estructura por ejes y control de calidad parseable.",
    "Se refuerza patron estable: problema, fundamento, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene compresion lossless por union-dedupe y sin regresion.",
    "Se integra la estructura canonica local del README y programa analitico del destino."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Conservar trazabilidad de reglas heredadas provisionales con etiqueta [supuesto].",
    "No sobrescribir reglas validas previas; solo unir y deduplicar.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Tomar README de materia como canon de estructura editorial local.",
    "Tomar programa analitico como guia de proposito y ejes de trabajo.",
    "Alinear cada entrega a ejes: problema, conceptos o norma, evidencia, analisis y conclusion.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar desarrollo en marco conceptual-normativo, analisis propio y cierre.",
    "Alinear formato final al producto solicitado en planeacion semanal.",
    "Mantener consistencia entre reporte, presentacion y actividad."
  ],
  "activity_rules": [
    "Delimitar el problema juridico o social desde el inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar solo resumen descriptivo.",
    "Distinguir hechos, conceptos, normas y opinion propia.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Relacionar el desarrollo con seguridad social cuando corresponda al encargo."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de propagar recursivamente.",
    "Normalizar manualmente respuestas no estructuradas antes de reutilizar.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Verificar que la compresion aplicada sea union-dedupe sin recorte.",
    "Verificar que no se eliminen reglas utiles previas."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener metadatos institucionales y de curso consistentes en archivos .tex.",
    "Usar estructura minima: portada, desarrollo, conclusion y referencias.",
    "Evitar comandos no estandar sin justificacion editorial o tecnica.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Corregir nombres de archivo o rutas corruptas antes de compilar.",
    "Verificar nombres canonicos contra README antes de referenciar archivos."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central.",
    "Priorizar fuentes institucionales UnADM y normativas juridicas vigentes verificables.",
    "Agregar solo referencias realmente consultables y pertinentes a la actividad.",
    "No inventar fuentes; marcar faltantes como pendientes o [supuesto].",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad."
  ],
  "propagation_hints": [
    "Propagar lateral y arriba solo reglas generales ya validadas.",
    "Transferir solo abstracciones estables; no transferir redaccion literal.",
    "No mover contenido tematico de Filosofia del Derecho a Seguridad Social.",
    "Reutilizar gates institucionales de JSON, respaldo y normalizacion.",
    "Mantener bandera de riesgo historico por ciclos con salida no parseable.",
    "Si falta contexto local, crear cerebro minimo y abrir vacios en preguntas."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida por la materia (APA, ISO, institucional o juridica mexicana) [supuesto].",
    "Confirmar si codigo local LDE-S2B1 es oficial en toda la documentacion [supuesto].",
    "Verificar vigencia de cualquier fuente provisional heredada de nodos no juridicos [supuesto].",
    "Confirmar campos obligatorios de portada para cada actividad especifica [supuesto]."
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
      "Evidencia trazable en fuentes reales.",
      "Analisis propio con postura argumentada.",
      "Conclusion juridica aplicable."
    ],
    "reason_for_being": [
      "Transformar consignas en productos juridicos verificables y utiles profesionalmente.",
      "Preservar memoria editorial persistente con compresion lossless.",
      "Permitir propagacion segura entre nodos no equivalentes mediante reglas estables."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Separacion explicita entre marco, analisis y cierre.",
      "Etiqueta [supuesto] para datos no confirmados.",
      "Cierre con transferencia a practica juridica."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo.",
      "Exponer marco normativo-doctrinal pertinente.",
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
          "justification": "No hay analisis solido sin delimitacion previa del problema."
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
          "justification": "La postura personal gana validez cuando se respalda en fuentes."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "La deduplicacion segura exige estructura valida."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La coherencia institucional orienta el cierre hacia utilidad academica y profesional."
        }
      ],
      "evidence": [
        "README local define estructura canonica y artefactos base.",
        "Programa analitico define proposito y ejes de trabajo de la materia.",
        "Archivo .bib local contiene base institucional y normativa verificable.",
        "Historial de ciclos exige gate de JSON parseable y normalizacion previa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 74: se preservan reglas utiles previas sin eliminacion.",
      "Ciclo 74: se deduplican variantes semanticas repetidas.",
      "Ciclo 74: se transfiere solo abstraccion estable desde nodo transversal.",
      "Ciclo 74: se evita importar contenido tematico no equivalente de Filosofia del Derecho.",
      "Ciclo 74: se refuerzan gates de calidad, trazabilidad y compilacion LaTeX."
    ]
  }
}