{
  "summary": [
    "Se sincronizan reglas transversales estables desde actividad de Filosofia sin trasladar contenido tematico ajeno.",
    "Se preserva identidad UnADM, estructura por ejes y control de calidad JSON parseable.",
    "Se refuerza compresion lossless por union-dedupe y politica sin regresion.",
    "Se mantiene canon local del destino: README, programa analitico y .bib propio.",
    "Se confirma enfoque de producto juridico verificable: problema, fundamento, evidencia, analisis propio y conclusion."
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
    "Tomar README de materia como canon de estructura editorial local.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Separar desarrollo en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato y alcance al producto solicitado por la planeacion semanal.",
    "Mantener consistencia entre reporte, presentacion y programa analitico."
  ],
  "activity_rules": [
    "Delimitar problema juridico y pregunta guia al inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar solo descripcion.",
    "Distinguir hechos, conceptos, normas y opinion propia.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de propagar recursivamente.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Comprobar consistencia entre citas en texto y archivo .bib local.",
    "Verificar que la compresion aplicada sea union-dedupe sin recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificacion correcta de español en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, citas rotas ni referencias indefinidas.",
    "Normalizar rutas y nombres de archivo antes de compilar.",
    "Resolver tokens o marcadores sin expandir en README y programa analitico."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central.",
    "Priorizar fuentes institucionales UnADM y normativas juridicas verificables.",
    "Agregar solo referencias consultables y pertinentes a la actividad.",
    "No inventar fuentes; registrar faltantes como pendientes o [supuesto].",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Distinguir bibliografia base de materia y bibliografia especifica de actividad."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables en saltos transversales.",
    "No transferir redaccion literal ni conceptos tematicos exclusivos de Filosofia.",
    "Propagar recursivamente solo despues de validar JSON y gates de calidad.",
    "Mantener bandera de riesgo historico por salidas no parseables en ciclos previos.",
    "Priorizar identidad, estructura reusable, calidad y grafo conceptual comun."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida en la materia (APA, ISO o institucional) [supuesto].",
    "Confirmar si LDE-S2B1 es codigo oficial o alias operativo [supuesto].",
    "Confirmar si Actividad 1 de esta materia exige reporte, presentacion o ambos.",
    "Verificar vigencia de cualquier fuente provisional heredada de otros dominios [supuesto]."
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
      "Evidencia pertinente y trazable.",
      "Analisis propio con postura.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir cada consigna en producto juridico verificable y util profesionalmente.",
      "Asegurar continuidad editorial entre nodos sin perder contexto local.",
      "Preservar memoria institucional con compresion lossless y sin regresion."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion clara entre marco, analisis y cierre.",
      "Cierre con implicacion practica."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo y doctrinal.",
      "Contrastar evidencia relevante.",
      "Fijar postura propia sustentada.",
      "Concluir con efecto juridico practico."
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
          "justification": "Sin problema delimitado no hay argumento evaluable."
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
          "justification": "La postura academica exige respaldo trazable."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "La deduplicacion segura requiere estructura valida."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La coherencia institucional mejora pertinencia profesional."
        }
      ],
      "evidence": [
        "README local define estructura canonica y artefactos.",
        "Programa analitico fija proposito y ejes de trabajo.",
        ".bib local confirma base normativa e institucional.",
        "Regla heredada valida: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 21: se consolida sincronizacion transversal conservadora.",
      "Se transfieren patrones editoriales estables y no contenido tematico de Filosofia.",
      "Se mantiene alerta por antecedentes de salidas no parseables.",
      "Se refuerza union-dedupe lossless sin eliminar reglas utiles previas."
    ]
  }
}