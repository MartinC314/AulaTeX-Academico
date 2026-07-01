{
  "summary": [
    "Se sincroniza ADN editorial transversal desde actividad de origen hacia materia destino con estrategia conservadora.",
    "Se preservan reglas institucionales UnADM, normalización estructurada y compresión por unión-dedupe sin recorte.",
    "Se consolidan ejes estables reutilizables: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se mantiene alerta crítica: no propagar salidas no estructuradas ni datos no verificados.",
    "Se crea cerebro editorial mínimo del destino con vacíos locales explícitos como supuestos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, metadatos y formato.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Vincular toda entrega a Licenciatura en Derecho.",
    "Respetar contexto curricular local confirmado: semestre 6, bloque 2, obligatoria, 8 créditos.",
    "Marcar como supuesto todo dato no visible en consigna o archivo local verificable.",
    "Tratar toda fuente heredada no verificada como provisional hasta confirmación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Transformar planeación en reporte, presentación o producto visual según consigna."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Incluir evidencia normativa, doctrinal o empírica pertinente.",
    "No asumir fuentes de otras semanas o materias como obligatorias de la actividad actual.",
    "Registrar en .bib local solo fuentes realmente usadas en la actividad."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de reutilizar memoria.",
    "Normalizar manualmente respuestas no estructuradas antes de propagar.",
    "No eliminar reglas útiles previas durante fusión por deduplicación.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Usar codificación correcta para español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar rupturas de compilación.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Corregir tokens sin expandir en README y programa analítico.",
    "Verificar que nombres de archivo listados existan y no contengan artefactos de salto."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y fuentes jurídicas confiables.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL.",
    "Distinguir bibliografía base de materia y bibliografía específica de actividad.",
    "No citar en texto claves ausentes en el .bib local."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo abstracciones estables, no redacción literal.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferir contenidos temáticos exclusivos de Filosofía del Derecho al destino.",
    "Mantener estrategia progresiva: reforzar primero reglas comunes de calidad editorial.",
    "Mantener estrategia conservadora: abrir preguntas cuando falte contexto local."
  ],
  "open_questions": [
    "Supuesto: falta consigna específica de actividades de la materia destino.",
    "Confirmar rúbrica local de evaluación argumentativa y de citación.",
    "Confirmar si el autor de plantilla debe parametrizarse por actividad.",
    "Confirmar cierre íntegro del archivo de reporte local y entornos LaTeX truncados.",
    "Confirmar resolución final del token Slug en README y programa analítico."
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
        "Normalización estructurada obligatoria antes de propagación."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia destino: Derecho de la empresa y emprendimiento.",
        "Semestre 6, bloque 2, obligatoria, 8 créditos."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Conceptos y marco normativo.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica aplicable."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos y verificables.",
      "Asegurar coherencia entre consigna, argumentación y cierre jurídico.",
      "Sostener continuidad editorial institucional entre nodos de la suite."
    ],
    "style_markers": [
      "Frases directas y trazables a evidencia.",
      "Uso explícito de supuestos cuando falta dato.",
      "Cierre con transferencia a práctica profesional."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis propio -> conclusión.",
      "Afirmación -> evidencia -> interpretación -> postura.",
      "Consigna local -> desarrollo focalizado -> verificación de cumplimiento."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalización estructurada",
        "Problema jurídico",
        "Evidencia verificable",
        "Análisis propio",
        "Conclusión jurídica transferible"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalización estructurada",
          "target": "Propagación segura",
          "kind": "supports",
          "justification": "Evita heredar ruido de salidas no parseables."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión gana validez práctica cuando está respaldada."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Consistencia transversal entre materias",
          "kind": "develops",
          "justification": "Unifica tono, formato y criterios de calidad."
        }
      ],
      "evidence": [
        "README de materia destino con pauta editorial y ubicación curricular.",
        "Programa analítico destino con ejes de trabajo reutilizables.",
        "Memoria origen con reglas estables de estructura y calidad."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas y se conservaron todas las útiles.",
      "Se excluyó transferencia de contenido temático específico no transversal.",
      "Se reforzaron gates de JSON parseable, supuestos y trazabilidad bibliográfica.",
      "Se inicializó ADN editorial del destino sin inventar fuentes nuevas."
    ]
  }
}