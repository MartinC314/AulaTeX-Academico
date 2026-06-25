{
  "summary": [
    "Se consolida sincronización transversal entre nodos no equivalentes con transferencia de abstracciones estables.",
    "Se preserva identidad UnADM, integridad académica y estructura argumentativa reusable.",
    "Se refuerza política de normalización: bloquear propagación sin JSON parseable.",
    "Se mantiene estrategia progresiva y conservadora sin regresión.",
    "Se corrigen supuestos locales de rutas con tokens y nombres corruptos en README."
  ],
  "identity_rules": [
    "Mantener identidad explícita UnADM en tono, portada y metadatos.",
    "Usar nombre exacto de materia: Derecho de la propiedad y registro.",
    "Mantener programa: Licenciatura en Derecho.",
    "Mantener ubicación curricular: semestre 7, bloque 1, obligatoria, 8 créditos.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el producto al entregable solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Transformar la planeación en reporte, presentación u otro formato según consigna."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Relacionar el desarrollo con propiedad y registro cuando aplique.",
    "No asumir fuentes de semanas posteriores sin validación de consigna.",
    "Verificar que el producto final corresponda a la actividad solicitada."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar que no existan placeholders sin resolver en metadatos y portada."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener clase y opciones base locales salvo instrucción docente distinta.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir nombres de archivo corruptos en README antes de automatizar rutas."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes jurídicas verificables.",
    "Registrar fuentes específicas por actividad en derecho-de-la-propiedad-y-registro.bib.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Validar que toda cita en texto exista en .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Compartir solo abstracciones editoriales estables entre nodos transversales.",
    "No propagar redacción literal ni datos hiperlocales de otra asignatura.",
    "Reforzar identidad, gates de calidad y patrones argumentativos comunes.",
    "Mantener compresión lossless por unión y deduplicación.",
    "Aplicar normalización manual cuando reaparezcan salidas no estructuradas."
  ],
  "open_questions": [
    "Supuesto: falta rúbrica local detallada por actividad; confirmar criterios de evaluación.",
    "Confirmar estilo de citación jurídica requerido por figura docente.",
    "Confirmar producto exacto por actividad (reporte, presentación u otro).",
    "Confirmar si la figura docente ya tiene nombre definitivo para reemplazar placeholder.",
    "Confirmar si existe protocolo local para corregir automáticamente tokens Slug en README."
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
        "Carpeta de asignatura como entrada canónica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 7, bloque 1, obligatoria, 8 créditos.",
        "Materia: Derecho de la propiedad y registro."
      ]
    },
    "essence": [
      "Problema jurídico.",
      "Conceptos y marco normativo.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos jurídicos sólidos.",
      "Asegurar trazabilidad entre consigna, argumentación, evidencia y cierre."
    ],
    "style_markers": [
      "Frases breves y accionables.",
      "Supuestos marcados explícitamente.",
      "Cero afirmaciones sin fuente o razonamiento.",
      "Sin placeholders al cierre editorial."
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
        "Integridad académica",
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
          "justification": "La identidad institucional exige verificabilidad y formato consistente."
        },
        {
          "source": "Normalización JSON",
          "target": "Trazabilidad bibliográfica",
          "kind": "supports",
          "justification": "La estructura parseable permite validaciones automáticas de citas."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis debe responder al problema delimitado."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica requiere fundamento normativo."
        },
        {
          "source": "Integridad académica",
          "target": "Conclusión transferible",
          "kind": "develops",
          "justification": "Una conclusión útil depende de evidencia y citas verificables."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicación curricular y pauta editorial.",
        "Programa analítico: propósito y ejes de trabajo.",
        "Bib local: claves institucionales base ya registradas.",
        "Histórico: incidencias de salidas no JSON parseables en ciclos previos."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: deduplicación completa de reglas repetidas.",
      "Ciclo 2: transferencia transversal limitada a abstracciones estables.",
      "Ciclo 2: refuerzo de gates de parseo JSON y normalización previa.",
      "Ciclo 2: conservación de ejes argumentativos comunes sin trasladar contenido temático de Filosofía del Derecho."
    ]
  }
}