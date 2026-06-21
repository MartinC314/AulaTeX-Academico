{
  "summary": [
    "Se consolida refuerzo lateral desde Actividad 1 hacia Actividad 4 con deduplicación lossless.",
    "Se preserva identidad UnADM y contexto curricular verificable de Filosofía del Derecho.",
    "Se mantienen ejes editoriales comunes: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se refuerza validación JSON estricta por antecedentes de salidas no parseables.",
    "Se evita transferir conclusiones, redacción literal o bibliografía exclusiva del nodo hermano."
  ],
  "identity_rules": [
    "Mantener tono formal académico, claro y jurídicamente preciso.",
    "Alinear contenido con UnADM, Licenciatura en Derecho y asignatura Filosofía del Derecho.",
    "Usar carpeta de asignatura como entrada canónica documental.",
    "Vincular ubicación curricular a semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Citar malla-curricular-derecho-unadm.pdf para soporte curricular cuando aplique.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el producto al formato solicitado por la planeación semanal.",
    "Separar hechos, conceptos, argumentos y postura personal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Adaptar Actividad 4 a los ejes del programa analítico sin copiar contenido de Actividad 1.",
    "Incluir postura argumentada del estudiante, no solo resumen descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Confirmar que el producto final corresponda a la consigna específica de Actividad 4.",
    "No asumir fuentes de otras semanas sin validar pertinencia local."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregable y consigna local."
  ],
  "latex_rules": [
    "Usar acentos y codificación correcta en español en .tex y .bib.",
    "Citar en .tex solo claves existentes en .bib.",
    "Conservar claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Verificar nombres de archivos del README antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: el .bib canónico esperado es filosofia-del-derecho.bib; confirmar localmente."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y jurídicas verificables.",
    "Registrar en .bib solo fuentes realmente consultables.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Usar filosofia-del-derecho-clean.bib solo si coincide con la consigna de Actividad 4.",
    "Marcar como pendiente cualquier dato bibliográfico incompleto."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir solo patrones reutilizables de identidad, estructura, calidad y método argumentativo.",
    "Preservar reglas útiles previas y evitar regresiones.",
    "Aplicar unión-dedupe sin recorte semántico.",
    "Si falta consigna local, propagar plantilla base y abrir preguntas en vez de inventar contenido."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual completa de Actividad 4; confirmar producto, extensión y rúbrica.",
    "Confirmar si Actividad 4 requiere reporte, presentación u otro formato.",
    "Confirmar nombre canónico final del archivo .bib por token Slug no resuelto.",
    "Confirmar si filosofia-del-derecho-clean.bib aplica a Actividad 4 o solo a Semana 7.",
    "Confirmar fuentes obligatorias específicas de la semana de Actividad 4."
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
        "Entrada canónica en carpeta de asignatura."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos.",
        "Asignatura: Filosofía del Derecho."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Conceptos y marco normativo-doctrinal.",
      "Evidencia verificable.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica aplicable."
    ],
    "reason_for_being": [
      "Convertir la planeación semanal en productos académicos sólidos y verificables.",
      "Garantizar continuidad editorial entre actividades sin copiar contenido específico.",
      "Asegurar trazabilidad institucional, técnica y argumentativa."
    ],
    "style_markers": [
      "Definir objetivo antes del desarrollo.",
      "Usar secciones funcionales con lógica jurídica.",
      "Sostener afirmaciones con cita explícita.",
      "Marcar supuestos de forma visible."
    ],
    "argumentative_patterns": [
      "Plantear problema.",
      "Exponer marco conceptual y normativo.",
      "Contrastar evidencia con análisis propio.",
      "Fijar postura justificada.",
      "Cerrar con conclusión jurídica transferible."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ejes editoriales de Filosofía del Derecho",
        "Normalización estructurada",
        "Validación JSON estricta",
        "Integridad académica verificable",
        "Relación problema-evidencia-conclusión"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "README de asignatura",
        "programa-analitico-filosofia-del-derecho.md"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Tono y formato académico",
          "kind": "supports",
          "justification": "La pauta editorial exige alineación institucional explícita."
        },
        {
          "source": "Ejes editoriales de Filosofía del Derecho",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Los ejes determinan el orden de redacción y cierre."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay reutilización segura."
        },
        {
          "source": "Integridad académica verificable",
          "target": "Conclusión jurídica propia",
          "kind": "supports",
          "justification": "La conclusión requiere respaldo y análisis, no resumen."
        }
      ],
      "evidence": [
        "README define identidad UnADM, entrada canónica y criterio de conclusión jurídica.",
        "Programa analítico define cinco ejes de trabajo reutilizables.",
        "Histórico de salidas no parseables justifica gate de JSON estricto."
      ]
    },
    "reinforcement_log": [
      "Ciclo 5: deduplicación de reglas repetidas con preservación total de intención.",
      "Ciclo 5: refuerzo lateral de patrón estructural y de calidad desde Actividad 1.",
      "Ciclo 5: exclusión explícita de transferencia de conclusiones y bibliografía exclusiva de hermano.",
      "Ciclo 5: mantenimiento de banderas de supuesto ante falta de consigna local completa."
    ]
  }
}