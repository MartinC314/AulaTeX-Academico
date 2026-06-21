{
  "summary": [
    "Se consolida sincronización transversal conservadora entre actividad de Filosofía del Derecho y materia de Seguridad Social.",
    "Se preserva identidad UnADM, estructura por ejes y control de calidad sin mezclar contenido temático no equivalente.",
    "Se refuerza compresión lossless por unión-deduplicación y política de no regresión.",
    "Se mantiene alerta institucional por antecedentes de salidas no parseables y necesidad de normalización previa."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redacción.",
    "Usar carpeta de materia destino como punto de entrada canónico.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 créditos.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "No sobrescribir reglas válidas previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README y programa analítico de la materia como canon estructural local.",
    "Alinear cada entrega a ejes estables: problema, conceptos/marco normativo, evidencia, análisis propio y conclusión.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones con límites claros entre marco, análisis y cierre.",
    "Ajustar formato final al producto solicitado por planeación semanal.",
    "Mantener consistencia editorial entre reporte, presentación y actividad."
  ],
  "activity_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Relacionar el desarrollo con seguridad social cuando corresponda al destino.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizar aguas abajo.",
    "Validar estructura mínima completa antes de propagación recursiva.",
    "Confirmar respaldo verificable o marca [supuesto] en afirmaciones relevantes.",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Comprobar compresión por unión-dedupe sin recorte ni regresión."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificación y acentos correctos en español en .tex y .bib.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos, sin referencias rotas y con rutas limpias.",
    "Normalizar nombres de archivos cuando existan marcadores o caracteres corruptos.",
    "Usar estructura mínima: portada, desarrollo por ejes, conclusión y referencias."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliográfica central del destino.",
    "Priorizar fuentes institucionales y normativas verificables.",
    "No inventar referencias; registrar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Distinguir bibliografía base de materia y bibliografía específica de actividad.",
    "Verificar que toda clave citada exista en el .bib local."
  ],
  "propagation_hints": [
    "Propagar lateral y recursivamente solo abstracciones editoriales estables.",
    "No transferir redacción literal ni contenido temático específico de Filosofía del Derecho.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual común.",
    "Mantener reglas locales de Seguridad Social como capa dominante del destino.",
    "Aplicar normalización manual al reutilizar salidas históricas no parseables.",
    "Conservar trazabilidad de reglas provisionales con etiqueta [supuesto]."
  ],
  "open_questions": [
    "Confirmar norma de citación exigida en la materia destino [supuesto].",
    "Confirmar rúbrica oficial por actividad para ajustar profundidad argumentativa [supuesto].",
    "Verificar vigencia de cualquier fuente provisional heredada de nodos no jurídicos [supuesto].",
    "Confirmar uso obligatorio de plantillas Actividad-1 en reporte y presentación del destino [supuesto]."
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
        "Materia destino: Derecho a la Seguridad Social.",
        "Semestre 2, bloque 1, obligatoria, 8 créditos."
      ]
    },
    "essence": [
      "Problema jurídico delimitado.",
      "Fundamento normativo y conceptual verificable.",
      "Evidencia explícita y trazable.",
      "Análisis propio no descriptivo.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Transformar consignas en productos jurídicos verificables.",
      "Preservar memoria editorial persistente sin pérdida por deduplicación.",
      "Habilitar sincronización transversal segura entre nodos no equivalentes."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explícito de [supuesto].",
      "Separación visible entre marco, análisis y cierre.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo/doctrinal.",
      "Contrastar evidencia pertinente.",
      "Fijar postura propia sustentada.",
      "Concluir con implicación jurídica práctica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "JSON parseable",
        "Normalización estructurada",
        "Compresión unión-dedupe",
        "Problema jurídico",
        "Marco normativo",
        "Evidencia verificable",
        "Análisis propio",
        "Conclusión jurídica transferible"
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
          "source": "JSON parseable",
          "target": "Normalización estructurada",
          "kind": "depends_on",
          "justification": "La reutilización recursiva segura requiere estructura válida."
        },
        {
          "source": "Compresión unión-dedupe",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Conserva reglas útiles sin recorte ni duplicación."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "La argumentación exige una pregunta delimitada."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión válida depende de fundamento legal verificable."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Calidad transversal de entregas",
          "kind": "supports",
          "justification": "Unifica tono, formato y trazabilidad entre nodos."
        }
      ],
      "evidence": [
        "README destino define estructura canónica y artefactos base.",
        "Programa analítico destino fija propósito y ejes jurídicos.",
        "Bibliografía local destino contiene base institucional y normativa verificable.",
        "Memoria origen aporta patrón reusable: problema, conceptos, evidencia, análisis y conclusión."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas equivalentes de identidad, estructura y calidad.",
      "Se transfirieron solo abstracciones estables; se excluyó contenido temático específico de Filosofía.",
      "Se reforzó gate de JSON parseable y normalización previa por antecedentes institucionales.",
      "Se mantuvo prioridad de contexto local del destino y no regresión editorial."
    ]
  }
}