{
  "summary": [
    "Se mantiene identidad UnADM y canon local de Derecho a la Seguridad Social.",
    "Se sincroniza patron transversal estable: problema, fundamento, evidencia, analisis propio y conclusion juridica.",
    "Se conserva compresion lossless por union-dedupe sin regresion.",
    "Se mantiene alerta por salidas no parseables y normalizacion manual obligatoria."
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
    "Tomar README y programa analitico como canon estructural local.",
    "Alinear entregas a ejes: problema, conceptos/norma, producto, analisis y conclusion.",
    "Usar estructura minima: portada, desarrollo, conclusion y referencias.",
    "Mantener consistencia entre reporte, presentacion y actividad.",
    "Registrar solo reglas accionables y verificables."
  ],
  "activity_rules": [
    "Definir objetivo y problema juridico al inicio.",
    "Sustentar afirmaciones con fuentes verificables.",
    "Incluir postura propia argumentada; evitar resumen descriptivo puro.",
    "Distinguir hechos, normas, doctrina y opinion.",
    "Cerrar con conclusion juridica aplicable a practica profesional.",
    "Ajustar formato al producto solicitado en planeacion semanal."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar manualmente respuestas no estructuradas antes de reutilizar.",
    "Verificar estructura minima completa antes de propagar recursivamente.",
    "Confirmar soporte verificable o marca [supuesto] en afirmaciones relevantes.",
    "Validar consistencia entre citas en texto y .bib local.",
    "Confirmar que la compresion sea union-dedupe y no recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificacion y acentos correctos en espanol en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Normalizar nombres/rutas con marcadores corruptos antes de compilar.",
    "No copiar bloques LaTeX completos entre nodos no equivalentes."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente central local.",
    "Priorizar fuentes institucionales y normativas verificables.",
    "No inventar referencias; marcar faltantes como [supuesto] o pendiente.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables en relacion transversal.",
    "No transferir contenido tematico literal de Filosofia del Derecho al destino.",
    "Propagar reglas generales de identidad, calidad y trazabilidad a nodos compatibles.",
    "Mantener reglas curriculares especificas dentro de la materia destino.",
    "Aplicar estrategia progresiva y conservadora: reforzar sin reemplazar."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida por la materia (APA, ISO o institucional) [supuesto].",
    "Confirmar si codigo local LDE-S2B1 es oficial en todos los entregables [supuesto].",
    "Confirmar rubricas especificas por actividad para ajustar profundidad argumentativa.",
    "Confirmar vigencia de cualquier fuente provisional heredada de otros dominios [supuesto]."
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
      "Fundamento normativo y doctrinal verificable.",
      "Evidencia suficiente y trazable.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir consignas en productos juridicos verificables y utiles profesionalmente.",
      "Preservar coherencia institucional y tecnica en todo el ciclo editorial."
    ],
    "style_markers": [
      "Frases directas y accionables.",
      "Etiqueta explicita de [supuesto].",
      "Separacion clara entre marco, analisis y cierre.",
      "Trazabilidad de reglas heredadas."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo/doctrinal.",
      "Contrastar evidencia relevante.",
      "Fijar postura propia sustentada.",
      "Concluir con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
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
          "justification": "Sin pregunta juridica delimitada no hay analisis consistente."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion requiere base legal verificable."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "La consolidacion segura exige estructura valida."
        },
        {
          "source": "Identidad UnADM",
          "target": "Problema juridico",
          "kind": "develops",
          "justification": "La institucion define enfoque formativo y rigor de planteamiento."
        }
      ],
      "evidence": [
        "README local define estructura canonica y control editorial.",
        "Programa analitico local fija proposito y ejes de trabajo.",
        ".bib local confirma base normativa e institucional verificable.",
        "Memoria origen aporta patron editorial reusable no tematico."
      ]
    },
    "reinforcement_log": [
      "Se deduplican reglas repetidas y se conservan todas las utiles.",
      "Se refuerzan gates de parseo JSON y normalizacion manual.",
      "Se incorpora patron transversal de argumentacion sin mezclar contenido disciplinar.",
      "Se mantiene trazabilidad de supuestos y fuentes provisionales."
    ]
  }
}