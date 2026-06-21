{
  "summary": [
    "Sincronizacion transversal consolidada con union-dedupe sin perdida ni regresion.",
    "Se preserva identidad UnADM y enfoque juridico del destino.",
    "Se refuerza patron estable: problema, fundamento, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene regla critica: no propagar salidas no parseables sin normalizacion.",
    "Se prioriza estructura reusable sobre contenido tematico de Filosofia del Derecho."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "No sobrescribir reglas validas previas; solo unir y deduplicar.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales [supuesto].",
    "No propagar datos personales de plantilla a nodos laterales [supuesto]."
  ],
  "structure_rules": [
    "Tomar README y programa analitico como canon estructural local.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Organizar desarrollo en: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto pedido en planeacion semanal.",
    "Mantener consistencia editorial entre reporte, presentacion y actividad.",
    "Usar estructura minima: portada, desarrollo por ejes, conclusion y referencias."
  ],
  "activity_rules": [
    "Definir al inicio problema y objetivo de cada actividad.",
    "Distinguir hechos, conceptos, normas y opinion propia.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas; incluir postura argumentada.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Relacionar el contenido con derecho a la seguridad social cuando corresponda.",
    "Cerrar con conclusion juridica aplicable a la practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de propagar recursivamente.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Comprobar consistencia entre citas en texto y archivo .bib local.",
    "Verificar correspondencia del producto con la consigna vigente.",
    "Confirmar compresion lossless por union-dedupe, no por recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener metadatos institucionales y de curso consistentes en .tex.",
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Normalizar rutas y nombres de archivo con marcadores corruptos antes de compilar.",
    "Verificar nombres canonicos desde README antes de referenciar archivos."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central.",
    "Priorizar fuentes institucionales UnADM y normativas juridicas verificables.",
    "Agregar solo referencias de actividad con metadatos minimos completos.",
    "No inventar fuentes; marcar faltantes como pendientes [supuesto].",
    "Conservar trazabilidad entre cita en LaTeX y entrada BibTeX.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo abstracciones editoriales estables.",
    "No transferir redaccion literal ni contenido tematico especifico de Filosofia.",
    "Mantener reglas locales de seguridad social como prioridad del destino.",
    "Propagar recursivamente solo despues de validar JSON y gates de calidad.",
    "Conservar bandera historica: ciclo 1 con salida no parseable requiere normalizacion manual."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida en la materia (APA, ISO o institucional) [supuesto].",
    "Confirmar si el codigo local LDE-S2B1 es oficial en todos los artefactos [supuesto].",
    "Confirmar figura docente oficial para plantillas de actividad [supuesto].",
    "Verificar si persiste alguna fuente provisional heredada ajena a Derecho [supuesto]."
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
      "Problema y objetivo delimitados desde el inicio.",
      "Marco normativo y evidencia comprobable.",
      "Analisis propio con postura argumentada.",
      "Conclusion juridica transferible a la practica."
    ],
    "reason_for_being": [
      "Convertir consignas en entregables juridicos consistentes y auditables.",
      "Preservar memoria editorial persistente sin perdida de reglas utiles.",
      "Habilitar propagacion segura entre nodos no equivalentes."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion visible entre marco, analisis y cierre.",
      "Control estricto de trazabilidad bibliografica."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo y doctrinal aplicable.",
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
          "justification": "La postura argumentada exige respaldo comprobable."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay consolidacion segura."
        },
        {
          "source": "Compresion union-dedupe",
          "target": "Identidad institucional UnADM",
          "kind": "supports",
          "justification": "Evita regresion y conserva reglas nucleares."
        }
      ],
      "evidence": [
        "README del destino define estructura canonica y artefactos.",
        "Programa analitico del destino fija proposito y ejes de trabajo.",
        ".bib local confirma base normativa e institucional verificable.",
        "Memoria historica confirma gate de JSON parseable y normalizacion manual."
      ]
    },
    "reinforcement_log": [
      "Ciclo 82: se deduplican reglas repetidas en summary, identidad, estructura y calidad.",
      "Ciclo 82: se transfiere patron argumentativo estable desde actividad origen sin mezclar tematica.",
      "Ciclo 82: se mantiene prioridad del contexto local de seguridad social.",
      "Ciclo 82: se conserva alerta institucional de no parseable en ciclo 1.",
      "Ciclo 82: se refuerza compresion lossless por union-dedupe."
    ]
  }
}