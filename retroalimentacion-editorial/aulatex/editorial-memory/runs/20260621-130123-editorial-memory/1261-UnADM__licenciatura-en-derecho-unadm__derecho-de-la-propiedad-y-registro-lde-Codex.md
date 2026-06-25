{
  "summary": [
    "Sincronización transversal aplicada con estrategia progresiva y conservadora.",
    "Se preservan reglas válidas del destino y se refuerzan abstracciones estables del origen.",
    "Se mantiene política de normalización obligatoria antes de propagación recursiva.",
    "Se consolidan ejes comunes: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se evita transferencia de redacción literal y de contenidos temáticos exclusivos de Filosofía del Derecho."
  ],
  "identity_rules": [
    "Mantener identidad explícita UnADM en tono, portada y metadatos.",
    "Usar nombre exacto de materia: Derecho de la propiedad y registro.",
    "Conservar programa: Licenciatura en Derecho.",
    "Registrar ubicación curricular: semestre 7, bloque 1, obligatoria, 8 créditos.",
    "Usar código local LDE-S7B1 cuando aplique.",
    "Usar la carpeta de la materia como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener consistencia entre estructura local de materia y formato de actividad."
  ],
  "activity_rules": [
    "Declarar objetivo de la actividad en la primera sección sustantiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Relacionar el desarrollo con propiedad y registro cuando la consigna lo exija.",
    "No asumir fuentes de semanas posteriores sin validación de consigna."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregable y consigna vigente."
  ],
  "latex_rules": [
    "Conservar plantilla base .tex de la materia como punto de partida.",
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Completar metadatos académicos obligatorios antes de compilar.",
    "Evitar placeholders sin resolver en portada y tabla de autor.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Compilar sin errores críticos y sin referencias rotas."
  ],
  "bibliography_rules": [
    "Usar derecho-de-la-propiedad-y-registro.bib como archivo local canónico de la materia.",
    "Priorizar fuentes institucionales UnADM y fuentes jurídicas verificables.",
    "No inventar referencias; registrar solo fuentes consultables.",
    "Distinguir bibliografía base de materia y bibliografía específica por actividad.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Verificar trazabilidad entre claves citadas y entradas reales del .bib."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas, generales y no ambiguas.",
    "Compartir entre nodos no equivalentes solo abstracciones editoriales estables.",
    "Evitar propagar contenido temático específico de una asignatura distinta.",
    "Mantener compresión lossless por unión y deduplicación sin regresión.",
    "Aplicar normalización manual si se detectan salidas heredadas no estructuradas."
  ],
  "open_questions": [
    "Supuesto: falta rúbrica local detallada por actividad; confirmar criterio de evaluación.",
    "Confirmar si cada actividad exige reporte, presentación u otro formato.",
    "Confirmar estilo de citación jurídica requerido por la figura docente.",
    "Confirmar resolución definitiva de placeholders en authortable.",
    "Confirmar si existe guía institucional adicional para actividades de propiedad y registro."
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
        "Entrada canónica por carpeta de asignatura.",
        "Normalización estructurada antes de propagación."
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
      "Conceptos y marco normativo.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir la planeación semanal en productos académicos sólidos y verificables.",
      "Asegurar coherencia entre consigna, argumentación, evidencia y cierre jurídico.",
      "Proteger la identidad institucional y la trazabilidad editorial en cada entrega."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Supuestos marcados explícitamente.",
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
        "Integridad académica",
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
          "justification": "La identidad institucional exige verificabilidad y forma consistente."
        },
        {
          "source": "Normalización JSON",
          "target": "Trazabilidad bibliográfica",
          "kind": "depends_on",
          "justification": "La validación automática requiere estructura parseable."
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
          "justification": "La conclusión jurídica debe fundarse en norma y doctrina."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La evidencia citada evita afirmaciones no sustentadas."
        }
      ],
      "evidence": [
        "README de la materia: identidad UnADM, entrada canónica y pauta editorial.",
        "Programa analítico: ejes de trabajo y propósito de realización.",
        "Bib local: claves institucionales existentes y verificables.",
        "Regla heredada estable: bloquear propagación sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 8: deduplicación completa de reglas repetidas.",
      "Ciclo 8: refuerzo de gates críticos de parseo, supuestos y trazabilidad .bib.",
      "Ciclo 8: transferencia transversal limitada a abstracciones estables, sin tema específico de Filosofía del Derecho.",
      "Ciclo 8: conservación explícita de reglas útiles previas sin eliminación."
    ]
  }
}