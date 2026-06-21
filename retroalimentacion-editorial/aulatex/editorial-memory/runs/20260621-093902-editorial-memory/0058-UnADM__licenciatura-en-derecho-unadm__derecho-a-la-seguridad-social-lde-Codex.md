{
  "summary": [
    "Se mantiene identidad UnADM y enfoque juridico del destino.",
    "Se refuerza sincronizacion transversal con reglas estables no tematicas.",
    "Se conserva compresion lossless por union-dedupe sin regresion.",
    "Se mantiene alerta por salidas no parseables historicas y normalizacion manual.",
    "Se consolida patron comun: problema, fundamento, evidencia, analisis propio y conclusion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "No sobrescribir reglas validas previas; solo unir y deduplicar.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta verificacion local.",
    "No transferir contenido tematico de Filosofia del Derecho al destino."
  ],
  "structure_rules": [
    "Tomar README y programa analitico del destino como canon estructural.",
    "Definir objetivo puntual antes del desarrollo.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Organizar en: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato al producto pedido por planeacion semanal.",
    "Mantener consistencia entre reporte, presentacion y bibliografia local.",
    "Registrar en memoria solo reglas accionables y verificables."
  ],
  "activity_rules": [
    "Delimitar problema y pregunta guia al inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Incluir postura argumentada del estudiante; evitar resumen descriptivo puro.",
    "Verificar coherencia entre objetivo, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Relacionar el analisis con seguridad social cuando corresponda."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de propagar recursivamente.",
    "Confirmar respaldo verificable o marca [supuesto] en cada afirmacion relevante.",
    "Validar correspondencia entre citas en texto y archivo .bib local.",
    "Verificar que la compresion aplicada sea union-dedupe, no recorte.",
    "Verificar que no se eliminen reglas utiles previas."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificacion y acentos correctos en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Usar estructura minima: portada, desarrollo, conclusion y referencias.",
    "Normalizar nombres/rutas de archivo antes de compilar.",
    "Resolver tokens sin expandir en README o programa analitico antes de canonizar rutas."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente central.",
    "Priorizar fuentes institucionales UnADM y normativas verificables.",
    "Agregar solo referencias consultables con metadatos minimos completos.",
    "No inventar fuentes.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Verificar que toda cita LaTeX tenga entrada BibTeX correspondiente."
  ],
  "propagation_hints": [
    "Propagar lateral y arriba solo reglas validadas en este ciclo.",
    "Compartir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates y grafo conceptual.",
    "Evitar transferencia de redaccion literal o contenido tematico de origen.",
    "Mantener bandera de riesgo historico por salidas no parseables de ciclos tempranos."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida por la materia [supuesto].",
    "Confirmar si codigo local LDE-S2B1 se usa oficialmente en portadas [supuesto].",
    "Verificar si persiste alguna fuente provisional heredada de otros dominios [supuesto].",
    "Confirmar rubrica de evaluacion por actividad para ajustar profundidad argumentativa [supuesto]."
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
      "Identidad institucional consistente.",
      "Problema juridico bien delimitado.",
      "Fundamento normativo verificable.",
      "Evidencia y citas trazables.",
      "Analisis propio con postura.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir consignas en productos juridicos verificables y utiles profesionalmente.",
      "Preservar memoria editorial persistente sin perdida por deduplicacion.",
      "Asegurar reutilizacion segura mediante reglas parseables y auditables."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion visible entre marco, analisis y cierre.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo.",
      "Exponer marco normativo y doctrinal.",
      "Contrastar evidencia pertinente.",
      "Sostener postura propia con razones.",
      "Concluir con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
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
          "justification": "Sin delimitacion del problema no hay analisis riguroso."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida requiere base legal verificable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura academica necesita respaldo comprobable."
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
          "justification": "Conserva reglas utiles sin duplicar ni recortar."
        }
      ],
      "evidence": [
        "README del destino define estructura canonica de archivos y control editorial.",
        "Programa analitico del destino fija proposito y ejes de trabajo verificables.",
        "Archivo .bib local del destino confirma base normativa e institucional.",
        "Historico institucional reporta salidas no parseables en ciclos previos."
      ]
    },
    "reinforcement_log": [
      "Se preservaron todas las reglas utiles previas del destino.",
      "Se agregaron solo abstracciones transversales estables del origen.",
      "Se evitó mezclar contenido tematico especifico de Filosofia del Derecho.",
      "Se reforzaron gates de parseabilidad, trazabilidad y respaldo de afirmaciones.",
      "Se mantuvo estrategia progresiva y conservadora en ciclo 58."
    ]
  }
}