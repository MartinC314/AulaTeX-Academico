{
  "summary": [
    "Se sincroniza memoria transversal con enfoque conservador y sin regresión.",
    "Se preserva identidad UnADM y canon local de la materia destino.",
    "Se refuerza patrón estable: problema, fundamento, evidencia, análisis propio y conclusión jurídica.",
    "Se mantiene regla crítica: no propagar salidas no parseables sin normalización.",
    "Se aplica compresión lossless por unión y deduplicación."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 créditos.",
    "Usar la carpeta de materia como punto de entrada canónico.",
    "No sobrescribir reglas válidas previas; unir y deduplicar.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Mantener trazabilidad de reglas heredadas y su estado de verificación."
  ],
  "structure_rules": [
    "Tomar README y programa analítico como canon estructural local.",
    "Alinear cada entrega a ejes: problema, conceptos/norma, producto, análisis y conclusión.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar desarrollo en marco conceptual, marco normativo/doctrinal, análisis propio y cierre.",
    "Alinear formato final al producto solicitado por la planeación semanal.",
    "Mantener consistencia editorial entre reporte y presentación."
  ],
  "activity_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Sustentar afirmaciones con evidencia verificable y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar entregas solo descriptivas.",
    "Distinguir hechos, normas, doctrina y opinión propia.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "No asumir fuentes de semanas distintas sin validación de consigna."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Normalizar manualmente respuestas no estructuradas antes de reutilizar.",
    "Validar estructura mínima completa antes de propagación recursiva.",
    "Confirmar respaldo verificable o marca [supuesto] en afirmaciones relevantes.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que la compresión sea unión-dedupe y no recorte.",
    "Verificar no regresión de reglas útiles previas."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificación y acentos correctos en español en .tex y .bib.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Mantener claves BibTeX estables para evitar roturas.",
    "Usar estructura mínima: portada, desarrollo por ejes, conclusión y referencias.",
    "Normalizar nombres/rutas de archivo y resolver marcadores corruptos antes de compilar."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliográfica local central.",
    "Priorizar fuentes institucionales UnADM y normas jurídicas vigentes verificables.",
    "Agregar solo referencias realmente consultables y pertinentes a la actividad.",
    "No inventar referencias.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Verificar que toda cita LaTeX tenga entrada BibTeX correspondiente."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo abstracciones editoriales estables.",
    "No transferir redacción literal ni contenido temático específico de Filosofía del Derecho.",
    "Propagar primero identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Mantener reglas locales del destino cuando haya conflicto de especificidad.",
    "Conservar alerta institucional histórica de salidas no parseables (ciclo 1).",
    "Aplicar propagación recursiva solo tras validar JSON y estructura."
  ],
  "open_questions": [
    "Confirmar norma de citación exigida en la materia (APA, ISO, institucional o jurídica mexicana) [supuesto].",
    "Confirmar si el código local LDE-S2B1 es oficial en todos los entregables [supuesto].",
    "Confirmar campos obligatorios de portada para figura docente en actividades [supuesto].",
    "Confirmar si toda actividad inicial requiere archivo específico -Actividad-1 en reporte y presentación.",
    "Verificar vigencia de cualquier fuente provisional heredada de nodos no jurídicos [supuesto]."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Normalización estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho a la Seguridad Social.",
        "Semestre 2, bloque 1, obligatoria, 8 créditos."
      ]
    },
    "essence": [
      "Producto jurídico verificable y trazable.",
      "Centralidad del problema jurídico y su fundamento normativo.",
      "Evidencia verificable más análisis propio.",
      "Cierre con utilidad profesional transferible."
    ],
    "reason_for_being": [
      "Convertir consignas en entregables jurídicos sólidos sin perder identidad institucional.",
      "Asegurar calidad técnica, argumentativa y bibliográfica en todo ciclo editorial."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explícito de [supuesto].",
      "Separación visible entre marco, análisis y cierre.",
      "Cierre con implicación jurídica práctica."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Presentar marco conceptual y normativo.",
      "Contrastar evidencia pertinente.",
      "Fijar postura propia sustentada.",
      "Concluir con criterio jurídico aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema jurídico",
        "Marco normativo",
        "Evidencia verificable",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "JSON parseable",
        "Compresión unión-dedupe"
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
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "No hay análisis sólido sin delimitación previa del problema."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión válida requiere fundamento legal verificable."
        },
        {
          "source": "JSON parseable",
          "target": "Compresión unión-dedupe",
          "kind": "depends_on",
          "justification": "La deduplicación lossless exige estructura válida."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Calidad editorial transversal",
          "kind": "supports",
          "justification": "Asegura coherencia entre nodos no equivalentes."
        }
      ],
      "evidence": [
        "README de la materia destino como canon estructural.",
        "Programa analítico del destino con ejes y propósito verificables.",
        "Archivo derecho-a-la-seguridad-social.bib con base normativa local.",
        "Historial institucional de salida no parseable en ciclo 1."
      ]
    },
    "reinforcement_log": [
      "Se conserva regla histórica de normalización previa a propagación.",
      "Se refuerzan gates de parseo JSON y trazabilidad de supuestos.",
      "Se preserva el patrón argumentativo común sin mezclar contenido temático ajeno.",
      "Se mantiene compresión lossless por unión-dedupe sin recorte."
    ]
  }
}