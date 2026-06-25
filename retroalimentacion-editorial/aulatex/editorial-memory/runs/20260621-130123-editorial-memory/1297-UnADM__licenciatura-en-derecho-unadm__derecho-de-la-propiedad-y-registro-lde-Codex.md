{
  "summary": [
    "Se mantiene base institucional UnADM y se refuerza sincronización transversal entre materias de Derecho.",
    "Se transfiere solo abstracción estable del origen: ejes editoriales, normalización estructurada y control de supuestos.",
    "Se conserva estrategia progresiva y conservadora sin regresión y con deduplicación lossless."
  ],
  "identity_rules": [
    "Mantener identidad explícita UnADM en tono, portada y metadatos.",
    "Usar nombre exacto de materia: Derecho de la propiedad y registro.",
    "Conservar programa y nivel: Licenciatura en Derecho.",
    "Registrar ubicación curricular: semestre 7, bloque 1, obligatoria, 8 créditos.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "No propagar literalidad de Filosofía del Derecho al destino."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el producto al entregable pedido en planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica.",
    "Mantener estructura reusable sin arrastrar secciones temáticas del origen."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Relacionar el desarrollo con propiedad y registro cuando aplique.",
    "No asumir fuentes de semanas posteriores sin validación de consigna."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto final y consigna local."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener plantilla base de la materia como punto de partida.",
    "Completar metadatos académicos obligatorios antes de compilar.",
    "Evitar placeholders sin resolver en portada y tabla de autor.",
    "Mantener claves BibTeX estables.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico antes de automatizar rutas."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes jurídicas verificables.",
    "Usar archivo local derecho-de-la-propiedad-y-registro.bib para fuentes específicas.",
    "No inventar referencias.",
    "Registrar solo obras consultables o archivos locales existentes.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Compartir a nodos no equivalentes solo abstracciones editoriales estables.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferir redacción literal o contenido temático específico del origen.",
    "Mantener unión-dedupe sin eliminar reglas útiles previas.",
    "Marcar supuestos en cada salto transversal."
  ],
  "open_questions": [
    "Confirmar rúbrica local por actividad en Derecho de la propiedad y registro.",
    "Confirmar estilo de citación jurídica exigido por figura docente.",
    "Confirmar producto requerido en cada actividad (reporte, presentación u otro).",
    "Confirmar corrección final de placeholders en authortable.",
    "Supuesto: persisten tokens corruptos en README/programa; confirmar nombres canónicos finales de archivos."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador en inferencias."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Normalización estructurada obligatoria antes de propagación.",
        "Sin propagación de salidas no parseables."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho de la propiedad y registro.",
        "Semestre 7, bloque 1, obligatoria, 8 créditos.",
        "Código local: LDE-S7B1."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Transformar planeación semanal en productos académicos claros y verificables.",
      "Asegurar trazabilidad entre consigna, argumentación y evidencia.",
      "Sostener consistencia institucional en todos los entregables."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Supuestos explícitos.",
      "Sin ambigüedad operativa.",
      "Sin placeholders al cierre."
    ],
    "argumentative_patterns": [
      "Del problema al marco conceptual.",
      "Del marco normativo a la evidencia.",
      "De la evidencia al análisis propio.",
      "Del análisis a una conclusión aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad académica",
        "Normalización JSON",
        "Trazabilidad bibliográfica",
        "Problema jurídico",
        "Marco normativo/doctrinal",
        "Análisis propio",
        "Conclusión transferible"
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
          "justification": "La identidad institucional exige rigor de citas y formato."
        },
        {
          "source": "Normalización JSON",
          "target": "Trazabilidad bibliográfica",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay validación automatizable."
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
          "justification": "La conclusión requiere fundamento jurídico verificable."
        },
        {
          "source": "Ejes editoriales transversales",
          "target": "Derecho de la propiedad y registro",
          "kind": "develops",
          "justification": "Se transfieren patrones estables sin contenido temático literal del origen."
        }
      ],
      "evidence": [
        "README de la materia: identidad UnADM y pauta editorial.",
        "Programa analítico: propósito y ejes de trabajo.",
        "derecho-de-la-propiedad-y-registro.bib: claves institucionales locales.",
        "Regla consolidada: bloquear propagación sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 17: se refuerza normalización estructurada como precondición de propagación recursiva.",
      "Ciclo 17: se consolidan ejes editoriales transversales comunes entre nodos de Derecho.",
      "Ciclo 17: se evita transferencia literal desde Filosofía del Derecho y se conserva solo abstracción reusable.",
      "Ciclo 17: se preservan reglas útiles previas del destino sin recorte."
    ]
  }
}