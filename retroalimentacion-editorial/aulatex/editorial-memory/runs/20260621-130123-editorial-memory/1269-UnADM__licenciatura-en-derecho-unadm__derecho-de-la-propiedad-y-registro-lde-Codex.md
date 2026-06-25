{
  "summary": [
    "Sincronización transversal aplicada con estrategia progresiva y conservadora.",
    "Se preservan reglas útiles previas del destino sin recorte.",
    "Se incorporan abstracciones estables del origen: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se refuerza la política de normalización obligatoria antes de propagación recursiva.",
    "Se mantiene compresión lossless por unión y deduplicación."
  ],
  "identity_rules": [
    "Mantener identidad explícita UnADM en tono, portada y metadatos.",
    "Usar nombre exacto de materia: Derecho de la propiedad y registro.",
    "Conservar programa: Licenciatura en Derecho.",
    "Registrar ubicación curricular: semestre 7, bloque 1, obligatoria, 8 créditos.",
    "Usar código local LDE-S7B1 cuando aplique.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "No transferir identidad curricular específica de Filosofía del Derecho al nodo de Propiedad y Registro."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener estructura reusable y no redacción literal entre nodos transversales."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Vincular actividad con propiedad y registro cuando la consigna lo requiera.",
    "No asumir fuentes de semanas posteriores sin validación de consigna.",
    "Verificar que el producto final corresponda a la actividad solicitada."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar que la conclusión responda al problema planteado.",
    "Confirmar que reglas propagadas sean verificables y no ambiguas."
  ],
  "latex_rules": [
    "Conservar plantilla base .tex de la materia como punto de partida.",
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Completar metadatos académicos obligatorios antes de compilar.",
    "Evitar placeholders sin resolver en portada y tabla de autor.",
    "Mantener claves BibTeX estables.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: el .bib canónico local es derecho-de-la-propiedad-y-registro.bib."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes jurídicas verificables.",
    "Registrar fuentes específicas de cada actividad en el .bib local de la materia.",
    "No inventar referencias; usar solo obras consultables o archivos locales existentes.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Mantener trazabilidad entre citas en texto y entradas BibTeX."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Compartir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar propagar redacción literal o datos curriculares de otra asignatura.",
    "Mantener unión-deduplicación sin regresión de reglas útiles.",
    "Aplicar normalización manual cuando se detecten salidas heredadas no parseables."
  ],
  "open_questions": [
    "Confirmar rúbrica formal de evaluación por actividad en esta materia.",
    "Confirmar estilo de citación jurídica exigido por figura docente.",
    "Confirmar sustitución de placeholder en campo 'Figura docente'.",
    "Confirmar si cada actividad pide reporte, presentación u otro producto.",
    "Supuesto: persisten tokens corruptos en README; validar lista final de archivos canónicos."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Accionable y verificable."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Normalización estructurada obligatoria antes de propagación.",
        "Entrada canónica por carpeta de asignatura."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 7, bloque 1, obligatoria, 8 créditos.",
        "Materia: Derecho de la propiedad y registro.",
        "Código local: LDE-S7B1."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Transformar planeación semanal en productos académicos claros.",
      "Garantizar fundamento jurídico, trazabilidad y criterio propio.",
      "Habilitar reutilización editorial segura entre nodos relacionados."
    ],
    "style_markers": [
      "Frases breves y accionables.",
      "Supuestos marcados explícitamente.",
      "Sin afirmaciones sin fuente.",
      "Sin placeholders al cierre."
    ],
    "argumentative_patterns": [
      "Del problema al marco conceptual.",
      "Del marco normativo a la evidencia.",
      "De la evidencia al análisis propio.",
      "Del análisis a la conclusión aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalización JSON",
        "Problema jurídico",
        "Marco normativo/doctrinal",
        "Evidencia verificable",
        "Análisis propio",
        "Conclusión transferible",
        "Trazabilidad bibliográfica"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La identidad institucional exige formato consistente y citas verificables."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis debe responder al problema planteado."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica necesita fundamento normativo."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia segura."
        },
        {
          "source": "Evidencia verificable",
          "target": "Análisis propio",
          "kind": "supports",
          "justification": "La postura argumentada requiere respaldo comprobable."
        },
        {
          "source": "Trazabilidad bibliográfica",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La consistencia texto-.bib evita afirmaciones no verificables."
        }
      ],
      "evidence": [
        "README local: pauta editorial y entrada canónica.",
        "Programa analítico local: propósito y ejes de trabajo.",
        "Bib local: claves institucionales existentes.",
        "Regla estable heredada: bloquear propagación si no hay JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 10: deduplicación aplicada sin pérdida de reglas útiles.",
      "Ciclo 10: se refuerzan ejes editoriales comunes de origen y destino.",
      "Ciclo 10: se mantiene separación entre abstracciones transferibles y contexto local.",
      "Ciclo 10: se conservan controles anti-regresión y normalización obligatoria."
    ]
  }
}