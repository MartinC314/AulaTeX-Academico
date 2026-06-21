{
  "summary": [
    "Se consolida sincronizacion transversal ciclo 5 con compresion lossless por union-dedupe.",
    "Se preserva identidad UnADM y enfoque juridico del destino sin mezclar contenido tematico de Filosofia del Derecho.",
    "Se refuerza patron editorial estable: problema, conceptos/norma, evidencia, analisis propio y conclusion juridica transferible.",
    "Se mantiene alerta institucional por antecedentes de salidas no parseables; normalizacion estructurada sigue obligatoria."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No sobrescribir reglas utiles previas; solo unir y deduplicar sin regresion."
  ],
  "structure_rules": [
    "Tomar README y programa analitico de la materia como canon estructural.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar desarrollo en: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por la planeacion semanal.",
    "Mantener consistencia entre reporte, presentacion y bibliografia local."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar entregas solo descriptivas.",
    "Distinguir hechos, conceptos, normas y opinion propia.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica aplicable a la practica profesional.",
    "Relacionar el contenido con seguridad social cuando corresponda."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que la compresion aplicada sea union-dedupe y no recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificacion y acentos correctos en espanol en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Normalizar rutas y nombres de archivo con marcadores corruptos antes de compilar.",
    "Mantener estructura minima: portada, desarrollo, conclusion y referencias."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central local.",
    "Priorizar fuentes institucionales UnADM y normas juridicas vigentes verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Registrar nuevas fuentes solo si son verificables y pertinentes a la consigna."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas estables y abstractas entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferir redaccion literal o contenido tematico especifico de Filosofia del Derecho.",
    "Mantener bandera de riesgo por historico de salida no parseable en ciclos previos.",
    "Si falta contexto local, preservar cerebro editorial minimo y abrir vacios como preguntas."
  ],
  "open_questions": [
    "Confirmar norma de citacion obligatoria de la materia (APA, ISO, institucional o juridica mexicana) [supuesto].",
    "Confirmar si LDE-S2B1 es codigo oficial o etiqueta interna [supuesto].",
    "Confirmar si la traza heredada desde ingenieria sigue vigente o debe desactivarse en Derecho [supuesto].",
    "Confirmar rubricas especificas por actividad en planeaciones locales.",
    "Verificar si hay fuentes obligatorias adicionales para jurisprudencia reciente en seguridad social."
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
      "Resolver consignas con fundamento juridico verificable.",
      "Sostener analisis propio con evidencia.",
      "Cerrar con utilidad profesional transferible."
    ],
    "reason_for_being": [
      "Convertir cada consigna en producto juridico claro, verificable y evaluable.",
      "Preservar memoria editorial persistente sin perdida ni regresion.",
      "Garantizar coherencia transversal entre nodos compatibles."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion visible entre marco, analisis y cierre.",
      "Control estricto de trazabilidad de fuentes."
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
          "justification": "El analisis exige una pregunta juridica delimitada."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida requiere fundamento legal verificable."
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
          "justification": "Evita duplicados y conserva reglas utiles sin perdida."
        }
      ],
      "evidence": [
        "README de materia define estructura canonica y artefactos base.",
        "Programa analitico define ejes juridicos y proposito verificable.",
        "Archivo .bib local confirma base institucional y normativa vigente.",
        "Historico institucional reporta casos de salida no parseable; se mantiene gate de normalizacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 5: se reforzo gate JSON parseable como condicion de propagacion.",
      "Ciclo 5: se consolidaron ejes editoriales comunes sin trasladar contenido tematico no equivalente.",
      "Ciclo 5: se mantuvo compresion lossless por union-dedupe sin eliminar reglas utiles previas.",
      "Ciclo 5: se preservo prioridad del canon local del destino (README, programa, .bib)."
    ]
  }
}