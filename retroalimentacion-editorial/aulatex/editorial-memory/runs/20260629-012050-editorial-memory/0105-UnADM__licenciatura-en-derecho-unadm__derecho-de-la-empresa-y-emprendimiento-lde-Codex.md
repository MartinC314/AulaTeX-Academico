{
  "summary": [
    "Se consolida sincronización transversal conservadora desde actividad de Filosofía del Derecho hacia materia destino.",
    "Se preservan reglas estables: identidad UnADM, estructura por ejes y control de calidad por normalización.",
    "Se mantiene deduplicación lossless sin recorte de reglas útiles previas.",
    "Se refuerza que la carpeta de materia es entrada canónica y que toda inferencia no visible se marca como supuesto.",
    "Se prioriza transferencia de abstracciones editoriales, no redacción literal ni contenidos temáticos específicos de otra asignatura."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, metadatos y formato.",
    "Usar nombre oficial de la materia: Derecho de la empresa y emprendimiento.",
    "Vincular entregables a Licenciatura en Derecho.",
    "Respetar contexto curricular local confirmado: semestre 6, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de materia como entrada canónica.",
    "Marcar como supuesto todo dato no visible en consigna o archivos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Desarrollar en secuencia: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el formato final al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Conservar coherencia entre README, programa analítico, .tex y .bib."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Incluir el producto solicitado en la consigna de la actividad.",
    "Conectar conclusión con aplicación práctica jurídica.",
    "No asumir fuentes de semanas distintas sin validación local."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de reutilizar memoria.",
    "Normalizar respuestas no estructuradas antes de propagación lateral, ascendente o descendente.",
    "No eliminar reglas útiles previas durante fusión por unión-dedupe.",
    "Confirmar que cada afirmación tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna local."
  ],
  "latex_rules": [
    "Usar español con acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Corregir tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir nombres de archivo con artefactos visibles de salto o truncamiento.",
    "Actualizar documenttitle y documentsubtitle por actividad concreta.",
    "Verificar cierre completo de entornos antes de compilar."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo fuentes realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y normatividad aplicable.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Registrar fuentes específicas en derecho-de-la-empresa-y-emprendimiento.bib.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL.",
    "No citar claves ausentes del .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas editoriales estables y transversales.",
    "Evitar transferir contenidos temáticos exclusivos de Filosofía del Derecho al destino.",
    "Mantener estrategia progresiva y conservadora: primero calidad e identidad, luego ajustes finos.",
    "Reforzar en nodos vecinos la regla de normalización previa por historial de salidas no estructuradas.",
    "No propagar datos curriculares específicos sin confirmación local.",
    "Si falta consigna local, usar cerebro editorial mínimo y dejar vacíos explícitos."
  ],
  "open_questions": [
    "Supuesto: falta consigna puntual de la próxima actividad en materia destino.",
    "Confirmar si documentauthor debe parametrizarse por actividad o mantenerse fijo.",
    "Confirmar corrección final de tokens Slug sin expandir en README y programa analítico.",
    "Confirmar si el archivo de reporte local está truncado o solo incompleto en captura.",
    "Confirmar criterio institucional para year en unadmSitioWeb frente a fecha de consulta."
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
        "Integridad académica con trazabilidad de fuentes.",
        "Normalización estructurada obligatoria antes de propagación."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho de la empresa y emprendimiento.",
        "Semestre 6, bloque 2, obligatoria, 8 créditos."
      ]
    },
    "essence": [
      "Problema jurídico como punto de partida.",
      "Conceptos y marco normativo con evidencia verificable.",
      "Análisis propio del estudiante.",
      "Conclusión jurídica aplicable.",
      "Calidad formal y trazabilidad técnica en LaTeX y bibliografía."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en entregables académicos sólidos y verificables.",
      "Mantener consistencia institucional entre actividades, materia y licenciatura.",
      "Asegurar transferencia editorial transversal sin contaminación temática."
    ],
    "style_markers": [
      "Frases directas y accionables.",
      "Supuestos declarados cuando falte evidencia local.",
      "Cierre con utilidad profesional jurídica.",
      "Trazabilidad entre afirmación, cita y fuente."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/marco -> análisis -> conclusión.",
      "Afirmación -> evidencia -> interpretación -> postura.",
      "Consigna -> cumplimiento verificable -> control de calidad."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalización estructurada",
        "Problema jurídico",
        "Evidencia verificable",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "Consistencia README-programa-.tex-.bib"
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
          "justification": "Reduce ruido y evita heredar salidas no parseables."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La validez práctica depende del respaldo documental."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Consistencia README-programa-.tex-.bib",
          "kind": "develops",
          "justification": "Unifica criterios de forma y contenido en todo el nodo."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis se orienta por una pregunta jurídica clara."
        }
      ],
      "evidence": [
        "README local con ubicación curricular y pauta editorial.",
        "Programa analítico local con ejes de trabajo.",
        "Bibliografía base local en derecho-de-la-empresa-y-emprendimiento.bib.",
        "Memoria origen con reglas estables de estructura, calidad y normalización."
      ]
    },
    "reinforcement_log": [
      "Se preservaron todas las reglas útiles previas sin regresión.",
      "Se deduplicaron variantes repetidas en formulaciones únicas.",
      "Se transfirieron solo abstracciones estables entre nodos no equivalentes.",
      "Se reforzaron gates de calidad y grafo conceptual para sincronización transversal."
    ]
  }
}