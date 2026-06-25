{
  "summary": [
    "Se mantiene base institucional UnADM y se refuerza sincronización transversal entre materias no equivalentes.",
    "Se transfiere solo abstracción estable: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se conserva regla dura de normalización: no propagar salidas no JSON parseables.",
    "Se deduplican reglas sin pérdida y sin regresión editorial.",
    "Se preserva contexto local del destino: semestre 7, bloque 1, obligatoria, 8 créditos."
  ],
  "identity_rules": [
    "Mantener identidad explícita UnADM en tono, portada y metadatos.",
    "Usar nombre exacto de materia: Derecho de la propiedad y registro.",
    "Conservar programa: Licenciatura en Derecho.",
    "Registrar ubicación curricular: semestre 7, bloque 1, obligatoria, 8 créditos.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "No transferir identidad curricular específica de Filosofía del Derecho al destino."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en secciones: conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Transformar planeación en reporte o presentación según consigna.",
    "Mantener estructura local de la materia sin copiar redacción literal del origen."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Verificar que el producto final corresponda a la actividad solicitada.",
    "No asumir fuentes de semanas posteriores sin validación de consigna.",
    "Relacionar el desarrollo con propiedad y registro cuando aplique."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar que las reglas propagadas sean verificables y no ambiguas.",
    "Evitar regresiones respecto de reglas útiles previas."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir placeholders pendientes en portada y authortable antes de entrega."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes jurídicas verificables.",
    "No inventar referencias.",
    "Usar solo obras realmente consultables o archivos locales existentes.",
    "Registrar fuentes específicas de actividad en derecho-de-la-propiedad-y-registro.bib.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Compartir entre nodos no equivalentes solo abstracciones editoriales estables.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "No propagar datos locales de archivos si no existen en el nodo receptor.",
    "Aplicar estrategia progresiva y conservadora: agregar mejoras verificables sin borrar reglas útiles.",
    "Mantener compresión lossless por unión y deduplicación."
  ],
  "open_questions": [
    "Supuesto: falta rúbrica local detallada por actividad; confirmar criterio de evaluación.",
    "Confirmar formato exigido por actividad: reporte, presentación u otro.",
    "Confirmar estilo de citación jurídica requerido por figura docente.",
    "Confirmar corrección final de tokens corruptos en README/programa.",
    "Confirmar si la Figura docente ya tiene nombre definitivo."
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
        "Carpeta de asignatura como entrada canónica.",
        "Normalización estructurada obligatoria antes de propagación."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia destino: Derecho de la propiedad y registro.",
        "Semestre 7, bloque 1, obligatoria, 8 créditos."
      ]
    },
    "essence": [
      "Problema jurídico bien delimitado.",
      "Marco conceptual y normativo pertinente.",
      "Evidencia trazable.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos claros y verificables.",
      "Garantizar coherencia entre consigna, argumentación y cierre profesional."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Supuestos explícitos.",
      "Sin afirmaciones sin fuente.",
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
          "justification": "La pauta institucional exige verificabilidad y formato consistente."
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
          "justification": "La conclusión jurídica requiere fundamento."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia segura."
        },
        {
          "source": "Evidencia verificable",
          "target": "Trazabilidad bibliográfica",
          "kind": "develops",
          "justification": "La evidencia exige correspondencia entre texto y .bib."
        }
      ],
      "evidence": [
        "README de la materia: identidad, ubicación curricular y pauta editorial.",
        "Programa analítico: ejes de trabajo y propósito.",
        "Regla heredada validada: bloquear propagación sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 15: se consolidan reglas transversales estables desde Filosofía del Derecho.",
      "Ciclo 15: se evita transferencia de contenido temático específico no transversal.",
      "Ciclo 15: se preservan reglas previas útiles del destino sin eliminación."
    ]
  }
}