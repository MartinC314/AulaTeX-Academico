{
  "summary": [
    "Se consolida sincronización transversal con transferencia solo de abstracciones estables.",
    "Se preservan reglas institucionales UnADM, normalización estructurada y deduplicación lossless.",
    "Se refuerza el marco reusable: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se evita transferir contenido doctrinal específico de Filosofía del Derecho por no equivalencia disciplinar.",
    "Se mantiene alerta local por tokens Slug sin expandir y artefactos de nombres en README/programa.",
    "Se mantiene alerta local por posible truncamiento del .tex de reporte."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial de la materia destino en todos los entregables.",
    "Usar Licenciatura en Derecho como programa académico.",
    "Respetar contexto curricular local confirmado: semestre 6, bloque 2, obligatoria, 8 créditos.",
    "Usar carpeta de materia como entrada canónica.",
    "Marcar como supuesto todo dato no visible en consigna o no confirmado en archivos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local."
  ],
  "structure_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Abrir con encuadre breve del problema jurídico o social.",
    "Organizar desarrollo en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el producto final a lo pedido por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Conservar correspondencia entre README, .tex, presentación y .bib."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar entregas solo descriptivas.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Incluir el producto solicitado por la actividad.",
    "Agregar fuentes específicas de actividad al .bib local."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de reutilizar memoria.",
    "No eliminar reglas útiles previas durante fusión por unión-dedupe.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar y normalizar respuestas no estructuradas antes de propagación recursiva.",
    "No propagar datos locales no confirmados como reglas institucionales."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Actualizar documenttitle y documentsubtitle por actividad real.",
    "Verificar rutas e imagen institucional antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir artefactos de nombre de archivo detectados en README.",
    "Verificar y corregir posible truncamiento del archivo de reporte (supuesto)."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes consultables.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Registrar fuentes de actividad en derecho-de-la-empresa-y-emprendimiento.bib.",
    "No citar fuentes ausentes en el .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales validadas por JSON y estructura.",
    "Priorizar transferencia de identidad, estructura reusable y gates de calidad.",
    "Evitar propagar contenido temático de Filosofía del Derecho a materia no equivalente.",
    "Propagar alerta de tokens Slug solo a nodos con plantillas equivalentes.",
    "Mantener estrategia progresiva y conservadora sin regresión de reglas útiles."
  ],
  "open_questions": [
    "Confirmar consigna y rúbrica de la próxima actividad local para ajustar profundidad.",
    "Confirmar si documentauthor debe parametrizarse por actividad o conservar plantilla.",
    "Confirmar valor final del Slug expandido en README y programa analítico.",
    "Confirmar si el .tex de reporte está realmente truncado en repositorio (supuesto).",
    "Confirmar criterio bibliográfico para year=2026 en unadmSitioWeb."
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
        "Integridad académica y trazabilidad bibliográfica.",
        "Entrada canónica por carpeta de materia."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 6, bloque 2, obligatoria, 8 créditos.",
        "Enfoque aplicado con transferencia profesional."
      ]
    },
    "essence": [
      "Problema jurídico claro.",
      "Conceptos y marco jurídico pertinentes.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible.",
      "Control explícito de supuestos."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en entregables académicos sólidos.",
      "Asegurar calidad formal, argumentativa y bibliográfica.",
      "Permitir propagación segura de memoria editorial reusable."
    ],
    "style_markers": [
      "Frases directas y verificables.",
      "Supuestos marcados explícitamente.",
      "Sin afirmaciones sin fuente.",
      "Cierre con aplicación práctica profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> análisis propio -> conclusión.",
      "Marco normativo/doctrinal como soporte del criterio personal.",
      "Coherencia estricta entre consigna, desarrollo y cierre."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalización estructurada",
        "Problema jurídico",
        "Evidencia verificable",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "Integridad bibliográfica",
        "Control de supuestos",
        "Consistencia LaTeX y BibTeX"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin JSON válido no hay transferencia segura."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión requiere respaldo documental."
        },
        {
          "source": "Control de supuestos",
          "target": "Integridad bibliográfica",
          "kind": "supports",
          "justification": "Evita mezclar hechos confirmados con inferencias."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura de entregables",
          "kind": "supports",
          "justification": "Define estándar común de forma y rigor."
        },
        {
          "source": "Consistencia LaTeX y BibTeX",
          "target": "Integridad bibliográfica",
          "kind": "depends_on",
          "justification": "Citas y referencias deben ser trazables y compilables."
        }
      ],
      "evidence": [
        "README local de materia.",
        "Programa analítico local.",
        "Archivo .bib local con claves base institucionales.",
        "Memoria previa consolidada con gates de JSON y normalización."
      ]
    },
    "reinforcement_log": [
      "Ciclo 14: se refuerza transferencia transversal por abstracciones estables.",
      "Ciclo 14: se conserva deduplicación lossless sin recorte de reglas útiles.",
      "Ciclo 14: se mantiene bloqueo de propagación ante salida no estructurada.",
      "Ciclo 14: se mantienen alertas locales de Slug sin expandir y posible truncamiento .tex [supuesto]."
    ]
  }
}