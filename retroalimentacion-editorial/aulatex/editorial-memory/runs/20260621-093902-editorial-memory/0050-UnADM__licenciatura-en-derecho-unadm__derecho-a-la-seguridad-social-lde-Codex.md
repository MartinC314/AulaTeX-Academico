{
  "summary": [
    "Se sincroniza memoria transversal sin mezclar contenido tematico de Filosofia del Derecho.",
    "Se preserva identidad UnADM y estructura canonica de la materia destino.",
    "Se refuerza patron estable: problema, fundamento, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene compresion lossless por union-dedupe y sin regresion.",
    "Se conserva alerta institucional por salidas no parseables en ciclos previos y normalizacion obligatoria."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar carpeta de materia como entrada canonica del destino.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Conservar trazabilidad de toda regla heredada provisional con etiqueta [supuesto].",
    "No sobrescribir reglas validas previas; solo unir y deduplicar.",
    "No transferir datos personales entre nodos laterales salvo requerimiento explicito [supuesto]."
  ],
  "structure_rules": [
    "Tomar README y programa analitico locales como canon estructural.",
    "Alinear cada entrega a ejes: problema, conceptos/norma, evidencia, analisis, conclusion.",
    "Usar estructura minima: portada, desarrollo por ejes, conclusion y referencias.",
    "Alinear formato final al producto solicitado en planeacion semanal.",
    "Normalizar nombres de archivo y rutas antes de tratarlos como canon."
  ],
  "activity_rules": [
    "Definir objetivo puntual y problema juridico al inicio.",
    "Distinguir hechos, conceptos, normas y postura propia.",
    "Sustentar afirmaciones con evidencia verificable o marcar [supuesto].",
    "Evitar entregas solo descriptivas; exigir argumentacion propia.",
    "Cerrar con conclusion juridica aplicable a practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si salida no es JSON parseable.",
    "Normalizar manualmente salidas no estructuradas antes de reutilizar.",
    "Verificar estructura minima completa antes de propagacion recursiva.",
    "Validar coherencia entre consigna, desarrollo y conclusion.",
    "Verificar correspondencia entre citas en texto y entradas del .bib.",
    "Confirmar compresion por union-dedupe sin recorte ni regresion."
  ],
  "latex_rules": [
    "Conservar plantillas base de la materia y personalizar solo campos variables.",
    "Mantener metadatos institucionales y curriculares consistentes en .tex.",
    "Mantener compatibilidad tecnica; evitar cambios de clase sin justificacion.",
    "Compilar sin errores criticos, referencias rotas ni rutas corruptas.",
    "Usar espanol consistente y acentos correctos en .tex y .bib."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como repositorio bibliografico central.",
    "No inventar fuentes; agregar solo referencias verificables.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener claves BibTeX estables para evitar roturas de citacion."
  ],
  "propagation_hints": [
    "Propagar lateral y arriba solo reglas estables y abstractas ya validadas.",
    "No propagar contenido doctrinal especifico de Filosofia a Seguridad Social.",
    "Priorizar identidad, gates de calidad y patrones argumentativos reutilizables.",
    "Mantener bandera de riesgo historica por ciclos con salida no parseable.",
    "Si falta contexto local, crear cerebro minimo y abrir preguntas sin inventar datos."
  ],
  "open_questions": [
    "Confirmar si la materia exige norma de citacion especifica (APA, ISO o institucional) [supuesto].",
    "Confirmar vigencia de reglas heredadas desde nodos no juridicos [supuesto].",
    "Confirmar campos institucionales pendientes en portada segun consigna local [supuesto].",
    "Confirmar si cada actividad requiere .tex y presentacion dedicados o solo reporte [supuesto]."
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
      "Identidad institucional fuerte.",
      "Estructura reusable por ejes juridicos.",
      "Evidencia verificable y trazabilidad.",
      "Analisis propio obligatorio.",
      "Cierre juridico transferible."
    ],
    "reason_for_being": [
      "Convertir consignas en productos juridicos verificables y consistentes.",
      "Asegurar continuidad editorial entre actividades sin perder contexto local.",
      "Permitir propagacion segura entre nodos por reglas estables y comprobables."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Marcado explicito de [supuesto].",
      "Separacion visible entre marco, analisis y cierre.",
      "Sin redaccion literal heredada entre nodos no equivalentes."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo/doctrinal aplicable.",
      "Contrastar evidencia pertinente.",
      "Fijar postura propia sustentada.",
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
          "justification": "Sin delimitacion del problema no hay analisis juridico valido."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion exige fundamento legal verificable."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "La consolidacion lossless requiere estructura valida."
        },
        {
          "source": "Identidad UnADM",
          "target": "Estructura reusable por ejes",
          "kind": "develops",
          "justification": "La identidad institucional define forma y consistencia editorial."
        }
      ],
      "evidence": [
        "README local define estructura canonica de archivos y control editorial.",
        "Programa analitico local define proposito y ejes de trabajo.",
        ".bib local confirma base normativa e institucional verificable.",
        "Historial de ciclos previos confirma necesidad de gate JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 50: se refuerza sincronizacion transversal conservadora.",
      "Ciclo 50: se preservan reglas utiles previas sin eliminacion.",
      "Ciclo 50: se deduplican reglas repetidas y se mantiene lossless.",
      "Ciclo 50: se evita transferencia de contenido tematico no equivalente."
    ]
  }
}