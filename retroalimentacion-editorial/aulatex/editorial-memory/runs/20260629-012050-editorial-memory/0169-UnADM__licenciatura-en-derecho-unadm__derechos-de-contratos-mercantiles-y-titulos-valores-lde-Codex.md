{
  "summary": [
    "Se consolida sincronización transversal conservadora entre actividad de origen y materia destino.",
    "Se preservan reglas estables: identidad UnADM, estructura argumentativa y control de calidad JSON.",
    "Se evita transferencia literal de contenido temático de Filosofía del Derecho por no equivalencia de nodo.",
    "Se refuerza saneamiento editorial local del destino: placeholders slug y nombres truncados en README/programa.",
    "Se mantiene política de compresión lossless por unión y deduplicación sin regresión."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables a Licenciatura en Derecho y a la materia destino.",
    "Conservar tono jurídico-formal con postura académica propia.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Usar carpeta de materia como entrada canónica."
  ],
  "structure_rules": [
    "Abrir cada entrega con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en bloques: conceptos o normas, evidencia, análisis propio y cierre.",
    "Alinear formato final al producto pedido en planeación semanal.",
    "Cerrar con conclusión jurídica transferible a práctica profesional.",
    "Mantener consistencia entre README, programa analítico, .tex y .bib."
  ],
  "activity_rules": [
    "Contextualizar actividad con problema concreto.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Distinguir evidencia citada de interpretación propia.",
    "Evitar entregas meramente descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir fuentes de otras semanas sin validación local."
  ],
  "quality_gates": [
    "Bloquear propagación si salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizar.",
    "Validar estructura mínima completa antes de propagar.",
    "Confirmar trazabilidad entre afirmaciones, citas y .bib.",
    "Verificar que no existan fuentes inventadas.",
    "Revisar ausencia de regresión de reglas útiles previas."
  ],
  "latex_rules": [
    "Mantener codificación correcta de español en .tex y .bib.",
    "Conservar claves BibTeX estables.",
    "Corregir macros truncadas antes de compilar.",
    "Resolver placeholders tipo $(@{...}.Slug) con nombres reales.",
    "Corregir nombres truncados en README de estructura de archivos.",
    "Compilar sin errores críticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Usar el .bib local confirmado de la materia destino.",
    "Registrar fuentes específicas por actividad en el .bib local.",
    "Priorizar fuentes institucionales UnADM y normativas verificables.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL.",
    "Agregar fecha de consulta en recursos web cuando aplique."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo abstracciones editoriales estables.",
    "Evitar transferir contenido doctrinal específico entre materias no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Mantener alerta institucional de normalización manual en ciclo 1 [supuesto].",
    "Aplicar unión-dedupe lossless en cada fusión.",
    "No eliminar reglas previas útiles aunque sean heredadas provisionales."
  ],
  "open_questions": [
    "Confirmar si la alerta histórica de salida no JSON parseable sigue vigente.",
    "Confirmar corrección final de nombres truncados en README.",
    "Confirmar resolución completa de placeholders slug en README y programa.",
    "Confirmar plantilla oficial de presentación de la materia.",
    "Confirmar rúbricas y consignas reales por actividad en destino.",
    "Confirmar política local de año fijo vs fecha de consulta en fuentes web."
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
        "Carpeta de materia como entrada canónica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 6, bloque 2, obligatoria, 8 créditos.",
        "Asignatura: Derechos de contratos mercantiles y títulos valores."
      ]
    },
    "essence": [
      "Problema jurídico claro.",
      "Conceptos o normas pertinentes.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos.",
      "Sostener trazabilidad entre argumento y fuente.",
      "Garantizar consistencia editorial transversal sin perder contexto local."
    ],
    "style_markers": [
      "Supuestos marcados explícitamente.",
      "Secciones breves y funcionales.",
      "Cierre con postura jurídica propia.",
      "Sin afirmaciones sin respaldo."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Definir marco conceptual o normativo.",
      "Contrastar evidencia.",
      "Desarrollar análisis propio.",
      "Concluir con aplicabilidad profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "identidad institucional UnADM",
        "integridad académica",
        "trazabilidad de fuentes",
        "problema jurídico",
        "análisis propio",
        "conclusión jurídica transferible",
        "normalización JSON",
        "consistencia README-programa-.tex-.bib"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "identidad institucional UnADM",
          "target": "integridad académica",
          "kind": "supports",
          "justification": "El marco institucional exige forma y fondo verificables."
        },
        {
          "source": "trazabilidad de fuentes",
          "target": "conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión es defendible cuando deriva de evidencia citada."
        },
        {
          "source": "problema jurídico",
          "target": "análisis propio",
          "kind": "develops",
          "justification": "El análisis nace de un problema delimitado."
        },
        {
          "source": "normalización JSON",
          "target": "consistencia README-programa-.tex-.bib",
          "kind": "depends_on",
          "justification": "La propagación confiable requiere estructura técnica validada."
        }
      ],
      "evidence": [
        "README de materia con pauta editorial y ubicación curricular.",
        "Programa analítico con ejes de trabajo reutilizables.",
        ".bib local existente con entradas institucionales confirmadas.",
        "Incidencias previas de salida no estructurada registradas [supuesto vigente hasta verificación]."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas de identidad, estructura y calidad.",
      "Se preservaron reglas útiles heredadas sin recorte semántico.",
      "Se filtró contenido específico de Filosofía del Derecho por transferencia transversal conservadora.",
      "Se añadieron refuerzos verificables de saneamiento local en README/programa.",
      "Se mantuvo política de no invención de fuentes y trazabilidad cita-.bib."
    ]
  }
}