{
  "summary": [
    "Sincronizacion transversal aplicada con enfoque conservador y sin regresion.",
    "Se preserva identidad UnADM y estructura canonica de la materia destino.",
    "Se refuerza patron estable: problema, conceptos/norma, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene regla critica: no propagar salidas no parseables sin normalizacion.",
    "Se integra control de trazabilidad para reglas provisionales con etiqueta [supuesto].",
    "Se consolida compresion lossless por union-dedupe, sin recorte semantico."
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
    "Tomar README de materia como canon estructural local.",
    "Alinear cada entrega a ejes: problema, conceptos/norma, producto, analisis y conclusion.",
    "Usar estructura minima: portada, desarrollo por ejes, conclusion y referencias.",
    "Mantener consistencia entre reporte, presentacion y programa analitico.",
    "Definir objetivo puntual antes del desarrollo."
  ],
  "activity_rules": [
    "Delimitar al inicio el problema juridico o social.",
    "Sustentar afirmaciones con norma, doctrina o evidencia verificable.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Ajustar formato y alcance al producto solicitado por la planeacion semanal.",
    "Marcar como [supuesto] todo dato no visible en la consigna."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar manualmente respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de propagar recursivamente.",
    "Confirmar que toda afirmacion relevante tenga respaldo o etiqueta [supuesto].",
    "Validar correspondencia entre citas en texto y archivo .bib local.",
    "Verificar compresion lossless por union-dedupe y ausencia de regresion."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener metadatos institucionales y de curso consistentes en .tex.",
    "Usar espanol con acentos correctos en .tex y .bib.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Normalizar nombres de archivo y resolver tokens o marcadores corruptos antes de compilar."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central local.",
    "Priorizar fuentes institucionales UnADM y normas juridicas vigentes verificables.",
    "Agregar solo referencias comprobables; no inventar fuentes.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Marcar faltantes como pendientes o [supuesto], sin fabricacion."
  ],
  "propagation_hints": [
    "Propagar a nodos laterales solo abstracciones editoriales estables, no contenido tematico literal.",
    "Propagar reglas curriculares especificas solo dentro de la misma materia.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Mantener bandera de riesgo por antecedentes de salida no parseable en ciclos tempranos.",
    "Aplicar sincronizacion progresiva y conservadora: agregar mejoras verificables sin borrar reglas utiles."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida en la materia (APA, ISO o institucional) [supuesto].",
    "Confirmar si el codigo local LDE-S2B1 es oficial en todos los entregables [supuesto].",
    "Confirmar dato oficial de figura docente para plantilla base [supuesto].",
    "Verificar si toda regla provisional heredada desde otros dominios sigue vigente en Derecho [supuesto]."
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
      "Resolver consignas en productos juridicos verificables.",
      "Sostener cada entrega en problema, fundamento, evidencia, analisis y cierre.",
      "Preservar continuidad editorial sin mezclar contenido ajeno a la materia."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables evaluables y profesionales.",
      "Garantizar trazabilidad, calidad formal y validez academica.",
      "Habilitar propagacion segura entre nodos por reglas estables."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion visible entre marco, analisis y conclusion.",
      "Cierre con utilidad juridica practica."
    ],
    "argumentative_patterns": [
      "Iniciar con encuadre del problema y objetivo.",
      "Exponer marco normativo y conceptos clave.",
      "Contrastar evidencia verificable pertinente.",
      "Presentar postura propia sustentada.",
      "Cerrar con conclusion juridica transferible."
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
          "justification": "Sin delimitacion del problema no hay analisis pertinente."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida requiere fundamento legal."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura propia gana solidez con respaldo comprobable."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "La consolidacion segura exige estructura valida."
        }
      ],
      "evidence": [
        "README local define estructura canonica y artefactos base.",
        "Programa analitico fija proposito y ejes de trabajo de la materia.",
        "Archivo .bib local confirma base normativa e institucional verificable.",
        "Historial institucional exige normalizacion previa de salidas no parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 65: se refuerza sincronizacion transversal sin traslado tematico literal desde Filosofia del Derecho.",
      "Ciclo 65: se preservan reglas utiles del destino y se deduplican variantes repetidas.",
      "Ciclo 65: se mantiene gate duro de JSON parseable y normalizacion manual de excepciones.",
      "Ciclo 65: se afianza patron argumentativo comun reutilizable entre actividades y materias."
    ]
  }
}