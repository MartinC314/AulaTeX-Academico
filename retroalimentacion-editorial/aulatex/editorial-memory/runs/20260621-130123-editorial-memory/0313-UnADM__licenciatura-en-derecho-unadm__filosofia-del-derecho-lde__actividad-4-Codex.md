{
  "summary": [
    "Se consolida refuerzo lateral para Actividad 4 con deduplicación lossless.",
    "Se preserva identidad UnADM y contexto curricular verificable de la asignatura.",
    "Se mantiene normalización estructurada obligatoria antes de propagación recursiva.",
    "Se transfieren patrones reutilizables de estructura, calidad y argumentación sin copiar conclusiones del nodo hermano.",
    "Supuesto: la consigna específica de Actividad 4 no está visible y debe confirmarse."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato académico.",
    "Alinear la actividad con Licenciatura en Derecho y Filosofía del Derecho.",
    "Vincular ubicación curricular a semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el producto final a la planeación semanal de la actividad.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Incluir problema, conceptos, evidencia y análisis propio en secuencia lógica.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Adaptar formato de entrega según consigna: reporte, presentación o producto visual.",
    "No asumir bibliografía de otras semanas sin confirmar pertinencia para Actividad 4."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregable y consigna local de Actividad 4."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Citar en .tex solo claves existentes en .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y rutas antes de compilar.",
    "Supuesto: el .bib canónico esperado es filosofia-del-derecho.bib por slug visible."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Registrar fuentes específicas de Actividad 4 en el .bib de la asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "No usar entradas truncadas o incompletas."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Reutilizar reglas institucionales sin perder especificidad local del nodo destino.",
    "Evitar regresiones: conservar reglas útiles previas ya verificadas.",
    "Propagar solo patrones reutilizables entre hermanos.",
    "Cuando falten datos locales, propagar plantilla estructural y preguntas abiertas."
  ],
  "open_questions": [
    "Confirmar consigna textual de Actividad 4: producto, extensión y criterios.",
    "Confirmar si Actividad 4 requiere reporte o formato alterno.",
    "Confirmar rúbrica docente específica para calibrar profundidad argumentativa.",
    "Confirmar nombre canónico final del archivo .bib en README con token no resuelto.",
    "Confirmar si filosofia-del-derecho-clean.bib aplica a Actividad 4 o solo a Semana 7."
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
        "Entrada canónica en carpeta de asignatura.",
        "Normalización estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Filosofía del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por planeación.",
      "Análisis propio y postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Transformar planeación semanal en entregables académicos sólidos.",
      "Asegurar trazabilidad entre problema, evidencia, análisis y conclusión.",
      "Preservar continuidad editorial institucional entre actividades."
    ],
    "style_markers": [
      "Definir objetivo antes del desarrollo.",
      "Separar hechos, conceptos, argumentos y postura personal.",
      "Marcar supuestos de forma explícita.",
      "Sostener cada afirmación relevante con cita."
    ],
    "argumentative_patterns": [
      "Plantear problema inicial.",
      "Delimitar marco conceptual y normativo.",
      "Contrastar fuentes con análisis propio.",
      "Emitir postura justificada.",
      "Cerrar con conclusión jurídica aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalización estructurada",
        "Validación JSON estricta",
        "Ejes editoriales de Filosofía del Derecho",
        "Integridad académica y verificabilidad",
        "Relación problema-evidencia-conclusión"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "README.md de la asignatura",
        "programa-analitico-filosofia-del-derecho.md"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Tono y formato académico",
          "kind": "supports",
          "justification": "La pauta editorial institucional exige alineación explícita."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia confiable."
        },
        {
          "source": "Ejes editoriales de Filosofía del Derecho",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Los ejes ordenan el flujo del desarrollo y cierre."
        },
        {
          "source": "Integridad académica y verificabilidad",
          "target": "Conclusión jurídica propia",
          "kind": "supports",
          "justification": "La conclusión válida depende de evidencia trazable."
        }
      ],
      "evidence": [
        "README: identidad UnADM, entrada canónica y exigencia de conclusión jurídica propia.",
        "Programa analítico: cinco ejes de trabajo reutilizables.",
        "Antecedentes de salidas no parseables: se mantiene gate de JSON estricto."
      ]
    },
    "reinforcement_log": [
      "Ciclo 13: unión y deduplicación de reglas repetidas sin recorte semántico.",
      "Ciclo 13: refuerzo lateral entre hermanos limitado a patrones reutilizables.",
      "Ciclo 13: se evita copiar redacción o bibliografía exclusiva de Actividad 1.",
      "Ciclo 13: se conservan supuestos abiertos por ausencia de consigna local completa."
    ]
  }
}