{
  "summary": [
    "Se mantiene identidad UnADM y enfoque juridico del destino.",
    "Se refuerza patron transversal: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se conserva regla critica: normalizar antes de propagar.",
    "Se aplica compresion lossless por union-dedupe sin recorte.",
    "Se evita transferir contenido tematico de Filosofia del Derecho al destino."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "No sobrescribir reglas validas previas; unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README y programa analitico como canon estructural local.",
    "Alinear cada entrega a ejes: problema, fundamento, evidencia, analisis, conclusion.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar marco normativo/doctrinal de analisis propio.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Ajustar formato al producto solicitado en planeacion semanal."
  ],
  "activity_rules": [
    "Delimitar problema juridico o social al inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Relacionar contenido con seguridad social cuando corresponda."
  ],
  "quality_gates": [
    "Bloquear propagacion si salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de propagar recursivamente.",
    "Confirmar respaldo verificable o marca [supuesto] en afirmaciones relevantes.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar no regresion de reglas utiles previas."
  ],
  "latex_rules": [
    "Conservar plantilla base de materia y personalizar solo campos variables.",
    "Mantener codificacion y acentos correctos en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Normalizar nombres de archivo y resolver marcadores/tokens sin expandir.",
    "Mantener consistencia de metadatos institucionales en archivos .tex."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente central local.",
    "Priorizar fuentes institucionales UnADM y marco juridico verificable.",
    "No inventar referencias; usar solo obras consultables.",
    "Registrar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Verificar que cada cita LaTeX tenga clave BibTeX existente."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables en saltos transversales.",
    "No propagar redaccion literal ni contenido tematico no equivalente.",
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Mantener alerta por antecedente de salida no parseable en ciclos tempranos.",
    "Reforzar identidad, gates de calidad y grafo conceptual comun."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida por materia (APA, ISO, institucional o juridica mexicana) [supuesto].",
    "Confirmar si codigo local LDE-S2B1 es oficial en todos los entregables [supuesto].",
    "Confirmar campos obligatorios de portada por actividad en planeaciones locales.",
    "Verificar vigencia de fuentes provisionales heredadas externas a Derecho [supuesto]."
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
      "Resolver consignas con base juridica verificable.",
      "Estructurar productos con problema, fundamento, evidencia, analisis y cierre.",
      "Preservar memoria editorial sin perdida por deduplicacion."
    ],
    "reason_for_being": [
      "Convertir cada consigna en producto juridico util y verificable.",
      "Garantizar continuidad editorial entre actividades y formatos.",
      "Asegurar trazabilidad y calidad en propagacion recursiva."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiqueta explicita de [supuesto] cuando falte evidencia local.",
      "Separacion clara entre marco, analisis y conclusion.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo y doctrinal pertinente.",
      "Contrastar evidencia relevante.",
      "Sostener postura propia fundada.",
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
          "justification": "No hay analisis solido sin pregunta juridica delimitada."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida requiere fundamento legal verificable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura personal se legitima con fuentes comprobables."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "La consolidacion segura exige estructura valida."
        }
      ],
      "evidence": [
        "README de destino define estructura canonica y archivos base.",
        "Programa analitico define proposito y ejes de trabajo.",
        "Archivo .bib local confirma base normativa e institucional.",
        "Regla heredada valida: normalizar salidas no estructuradas antes de reutilizar."
      ]
    },
    "reinforcement_log": [
      "Ciclo 27: se transfiere patron editorial comun sin mezclar contenido disciplinar de Filosofia.",
      "Ciclo 27: se refuerzan gates de calidad y control JSON parseable.",
      "Ciclo 27: se conserva ADN local de seguridad social y se deduplica sin perdida."
    ]
  }
}