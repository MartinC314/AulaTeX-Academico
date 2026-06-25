{
  "summary": [
    "Se consolida sincronización transversal con reglas estables de identidad, estructura y control de calidad UnADM.",
    "Se preserva estrategia conservadora: no transferir contenido temático específico de Filosofía del Derecho al nodo electiva sin validación local.",
    "Se refuerzan ejes editoriales reutilizables: problema, conceptos/fuentes, análisis propio y conclusión jurídica transferible.",
    "Se mantiene compresión lossless por unión y deduplicación, sin regresión de reglas útiles previas.",
    "Se mantiene bloqueo de propagación para salidas no JSON parseables y herencias no normalizadas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 8, bloque 2, tipo Electiva.",
    "Usar la carpeta de materia como entrada canónica.",
    "Conservar tono académico-jurídico claro y argumentativo.",
    "Marcar como [supuesto] todo dato no confirmado en consigna o documentos locales.",
    "Mantener autor y matrícula confirmados en front matter: Martin Jonathan de la Cruz, ES2611202040.",
    "Usar código de curso LDE-S8B2 en metadatos.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Alinear el producto final con la consigna semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener consistencia entre README, programa analítico, .tex y .bib.",
    "Corregir placeholders y nombres truncados en rutas y archivos antes de entrega."
  ],
  "activity_rules": [
    "Traducir cada consigna semanal al producto concreto solicitado.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Vincular conceptos, normas, doctrina o datos con el problema jurídico tratado.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Evitar traslado literal de redacción entre materias.",
    "No asumir fuentes de otras semanas o materias sin verificación local."
  ],
  "quality_gates": [
    "Bloquear consolidación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de propagar aguas abajo.",
    "Revisar y normalizar herencias de ciclos con salida no estructurada.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar trazabilidad entre citas en texto y archivo .bib.",
    "Confirmar ausencia de tokens sin expandir y placeholders visibles en README, programa, .tex y .bib.",
    "Verificar correspondencia del producto con la consigna de la actividad vigente."
  ],
  "latex_rules": [
    "Conservar plantilla LaTeX base de la materia.",
    "Actualizar título, subtítulo y número real de actividad antes de compilar.",
    "Mantener codificación y acentos correctos en español.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Mantener nombres de archivo consistentes entre README y artefactos reales.",
    "Resolver tokens tipo $(@{...}.Slug) a nombres literales.",
    "Completar campos no confirmados solo cuando exista evidencia; en otro caso marcar [supuesto]."
  ],
  "bibliography_rules": [
    "Registrar fuentes específicas por actividad en electiva-semestre-8-bloque-2.bib.",
    "Priorizar fuentes institucionales UnADM cuando corresponda.",
    "No inventar referencias.",
    "Agregar entradas BibTeX solo con metadatos verificables.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Mantener claves BibTeX estables y trazables con el texto."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales y estables en nodos no equivalentes.",
    "Priorizar transferencia de identidad, estructura reusable, quality gates y grafo conceptual.",
    "No propagar contenido temático específico de una asignatura a otra sin evidencia local.",
    "Mantener etiqueta de herencia provisional para fuentes no verificadas.",
    "Aplicar unión-dedupe en cada ciclo para evitar duplicados y preservar cobertura."
  ],
  "open_questions": [
    "[supuesto] Confirmar créditos oficiales de la materia destino para metadatos finales.",
    "[supuesto] Confirmar nombre oficial de figura docente en front matter.",
    "[supuesto] Confirmar si existe nombre oficial alterno de la electiva.",
    "[supuesto] Confirmar política institucional para year y fecha de consulta en @misc.",
    "[supuesto] Confirmar si la bibliografía base requiere más claves institucionales obligatorias."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador ante datos no confirmados."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Entrada canónica por carpeta de materia.",
        "Normalización estructurada antes de propagar.",
        "Control explícito de supuestos."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 8, bloque 2, tipo Electiva.",
        "Código de curso LDE-S8B2.",
        "[supuesto] Créditos por confirmar."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Conceptos y fuentes pertinentes.",
      "Análisis propio con postura.",
      "Conclusión jurídica transferible.",
      "Trazabilidad cita-texto-bib."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en entregables jurídicos sólidos.",
      "Asegurar rigor editorial y verificabilidad académica.",
      "Sostener continuidad institucional transversal sin contaminar contextos locales."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Objetivo explícito.",
      "Secciones ordenadas y funcionales.",
      "Marcado visible de [supuesto].",
      "Cierre con aplicación profesional."
    ],
    "argumentative_patterns": [
      "Problema -> objetivo -> marco conceptual/normativo -> análisis propio -> conclusión aplicable.",
      "Afirmación relevante -> evidencia verificable -> interpretación jurídica.",
      "Evitar descripción pura; priorizar juicio jurídico razonado."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalización estructurada",
        "Integridad académica",
        "Control de supuestos",
        "Problema jurídico",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "Trazabilidad cita-texto-bib",
        "Compresión unión-dedupe"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva segura",
          "kind": "supports",
          "justification": "Evita heredar memoria no parseable o ambigua."
        },
        {
          "source": "Integridad académica",
          "target": "Trazabilidad cita-texto-bib",
          "kind": "depends_on",
          "justification": "La verificabilidad exige correspondencia entre afirmaciones y fuentes."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "develops",
          "justification": "La transferencia profesional depende del razonamiento del estudiante."
        },
        {
          "source": "Control de supuestos",
          "target": "Rigor editorial",
          "kind": "supports",
          "justification": "Distingue datos confirmados de pendientes y reduce errores."
        }
      ],
      "evidence": [
        "README local: pauta editorial y ubicación curricular.",
        "Programa analítico local: propósito y ejes de trabajo.",
        ".bib local: claves institucionales verificables.",
        "Regla histórica: revisar salidas no estructuradas antes de propagar."
      ]
    },
    "reinforcement_log": [
      "Ciclo 19: deduplicación integral aplicada sin pérdida de reglas útiles.",
      "Ciclo 19: reforzado gate JSON parseable como condición de propagación.",
      "Ciclo 19: reforzada separación entre abstracciones transversales y contenido temático local.",
      "Ciclo 19: mantenida política conservadora de fuentes provisionales hasta validación."
    ]
  }
}