{
  "summary": [
    "Se consolida sincronizacion transversal entre nodos no equivalentes con compresion lossless por union-dedupe.",
    "Se preserva identidad UnADM, estructura por ejes y control de calidad sin regresion.",
    "Se transfiere patron estable: problema, conceptos/norma, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene regla de normalizacion obligatoria ante salidas no parseables.",
    "Se evita trasladar contenido tematico literal de Filosofia del Derecho al destino de Seguridad Social."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de materia como punto de entrada canonico.",
    "Conservar trazabilidad de reglas heredadas provisionales con etiqueta [supuesto].",
    "No sobrescribir reglas validas previas; solo unir y deduplicar.",
    "No propagar datos personales de plantilla a nodos laterales salvo requerimiento explicito [supuesto]."
  ],
  "structure_rules": [
    "Tomar README y programa analitico del destino como canon estructural local.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar desarrollo en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado en la planeacion semanal.",
    "Mantener consistencia entre reporte, presentacion y bibliografia."
  ],
  "activity_rules": [
    "Delimitar problema y pregunta guia al inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Verificar coherencia entre objetivo, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de propagar recursivamente.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que la compresion aplicada sea union-dedupe sin recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificacion y acentos correctos en espanol en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, citas rotas ni referencias indefinidas.",
    "Normalizar nombres de archivo y resolver marcadores/tokens sin expandir antes de compilar.",
    "Mantener metadatos institucionales consistentes en todos los artefactos."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central del destino.",
    "Priorizar fuentes institucionales UnADM y normatividad vigente verificable.",
    "Agregar solo referencias consultables con metadatos minimos completos.",
    "No inventar fuentes; marcar faltantes como pendientes o [supuesto].",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Verificar que cada clave citada exista en el .bib local."
  ],
  "propagation_hints": [
    "Propagar a laterales solo abstracciones editoriales estables, no redaccion literal.",
    "Transferir reglas generales de identidad, estructura, calidad y trazabilidad.",
    "Preservar reglas locales tematicas del destino sin contaminacion disciplinar.",
    "Aplicar estrategia progresiva y conservadora: agregar mejoras verificables y evitar cambios bruscos.",
    "Mantener bandera de riesgo historico por salidas no parseables en ciclos iniciales.",
    "Registrar refuerzos en ADN para facilitar reconstruccion futura del nodo."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida en la materia (APA, ISO, institucional o juridica mexicana) [supuesto].",
    "Confirmar si LDE-S2B1 es codigo oficial o interno [supuesto].",
    "Verificar vigencia de reglas heredadas desde nodos no juridicos antes de nueva propagacion [supuesto].",
    "Confirmar si cada actividad de Seguridad Social requiere .tex propio o reutiliza plantilla base.",
    "Validar si existe rubrica oficial por actividad para ajustar profundidad argumentativa."
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
      "Resolver consignas en productos juridicos verificables.",
      "Integrar problema, fundamento, evidencia, analisis propio y cierre.",
      "Sostener trazabilidad, consistencia tecnica y utilidad profesional."
    ],
    "reason_for_being": [
      "Convertir planeaciones semanales en entregas evaluables sin perder identidad institucional.",
      "Asegurar calidad reproducible mediante reglas accionables y gates verificables.",
      "Permitir propagacion transversal segura entre nodos academicos."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto] cuando falte confirmacion.",
      "Separacion visible entre marco, analisis y conclusion.",
      "Cierre con implicacion juridica practica."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo y doctrinal pertinente.",
      "Contrastar evidencia verificable.",
      "Fijar postura propia sustentada.",
      "Concluir con efecto juridico transferible."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema juridico",
        "Marco normativo/doctrinal",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "JSON parseable",
        "Compresion union-dedupe",
        "Trazabilidad de supuestos"
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
          "justification": "Sin delimitacion del problema no hay analisis pertinente."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion requiere fundamento legal verificable."
        },
        {
          "source": "JSON parseable",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "La reutilizacion automatizada exige estructura valida."
        },
        {
          "source": "Compresion union-dedupe",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Conserva reglas utiles sin perdida ni duplicado."
        }
      ],
      "evidence": [
        "README destino define estructura canonica y artefactos base.",
        "Programa analitico destino fija proposito y ejes juridicos.",
        ".bib local confirma base normativa e institucional verificable.",
        "Historial previo registra necesidad de normalizacion ante salidas no parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 42: se refuerza patron comun transversal sin mover contenido tematico especifico de Filosofia.",
      "Ciclo 42: se mantiene gate estricto de JSON parseable para propagacion recursiva.",
      "Ciclo 42: se consolida regla de compresion lossless por union-dedupe sin recorte.",
      "Ciclo 42: se preservan reglas locales del destino y se agregan solo abstracciones estables verificables."
    ]
  }
}