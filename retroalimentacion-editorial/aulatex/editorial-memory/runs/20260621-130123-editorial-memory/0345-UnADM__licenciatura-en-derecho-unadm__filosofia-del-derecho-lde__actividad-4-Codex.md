{
  "summary": [
    "Se consolida refuerzo lateral entre actividades hermanas con deduplicación lossless.",
    "Se preserva identidad UnADM y marco curricular verificable sin copiar contenido específico de Actividad 1.",
    "Se mantiene gate crítico: normalización estructurada y JSON parseable antes de propagar.",
    "Se refuerzan ejes editoriales comunes: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Supuesto: la consigna textual de Actividad 4 no está completa en el contexto visible."
  ],
  "identity_rules": [
    "Mantener tono formal académico y precisión jurídica.",
    "Alinear toda entrega a UnADM, Licenciatura en Derecho, Filosofía del Derecho.",
    "Conservar referencia curricular: semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Separar hechos, conceptos, argumentos y postura personal.",
    "Alinear el formato final al producto solicitado en planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Adaptar Actividad 4 a los cinco ejes del programa analítico.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Evitar trasladar conclusiones específicas desde actividad hermana.",
    "Supuesto: confirmar producto exacto requerido para Actividad 4."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Exigir estructura mínima completa antes de reutilización recursiva.",
    "Revisar y normalizar cualquier respuesta no estructurada heredada.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar correspondencia entre citas en texto y archivo .bib.",
    "Verificar que el producto coincida con la consigna local de Actividad 4."
  ],
  "latex_rules": [
    "Mantener acentos y codificación correcta en español en .tex y .bib.",
    "Citar solo claves existentes en el .bib activo.",
    "No renombrar claves BibTeX ya usadas en documentos vigentes.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Verificar nombres reales de archivos cuando README tenga tokens sin resolver.",
    "Resolver tokens tipo $(@{...}.Slug) antes de automatizar rutas."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y jurídicas verificables.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "No inventar referencias ni metadatos faltantes.",
    "Registrar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Usar filosofia-del-derecho-clean.bib solo cuando la consigna coincida.",
    "Supuesto: filosofia-del-derecho-clean.bib parece orientado a interpretación jurídica; confirmar aplicabilidad a Actividad 4."
  ],
  "propagation_hints": [
    "Propagar solo patrones reutilizables de identidad, estructura y calidad.",
    "No propagar redacción literal ni bibliografía exclusiva de una actividad hermana.",
    "Aplicar unión-dedupe sin regresión de reglas útiles previas.",
    "Mantener bandera de normalización manual para ciclos con salidas históricas no parseables.",
    "Escalar mejoras verificables a nodos laterales de la misma asignatura."
  ],
  "open_questions": [
    "¿Cuál es la consigna textual completa de Actividad 4?",
    "¿El producto requerido es reporte, presentación u otro formato?",
    "¿Existe rúbrica docente específica para Actividad 4?",
    "¿Qué fuentes son obligatorias en la semana correspondiente?",
    "¿Cuál es el nombre canónico final del .bib cuando se resuelva el token Slug?"
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
        "Normalización estructurada obligatoria antes de propagar.",
        "Carpeta de asignatura como entrada canónica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Filosofía del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Conceptos y marco normativo o doctrinal.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos y trazables.",
      "Sostener coherencia entre identidad institucional, argumento jurídico y evidencia."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Secciones funcionales y jerarquía clara.",
      "Citas explícitas para cada afirmación sustantiva.",
      "Supuestos etiquetados cuando falte información local."
    ],
    "argumentative_patterns": [
      "Plantear problema.",
      "Delimitar conceptos y normas.",
      "Contrastar fuentes.",
      "Fijar postura propia justificada.",
      "Concluir con aplicabilidad jurídica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ejes editoriales de Filosofía del Derecho",
        "Integridad académica y verificabilidad",
        "Normalización estructurada",
        "Validación JSON previa a propagación",
        "Conclusión jurídica con criterio propio"
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
          "justification": "La pauta editorial exige alineación institucional explícita."
        },
        {
          "source": "Ejes editoriales de Filosofía del Derecho",
          "target": "Estructura de la actividad",
          "kind": "develops",
          "justification": "Los ejes ordenan problema, conceptos, evidencia, análisis y cierre."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin JSON válido no hay transferencia segura."
        },
        {
          "source": "Integridad académica y verificabilidad",
          "target": "Conclusión jurídica con criterio propio",
          "kind": "supports",
          "justification": "La conclusión debe estar respaldada por fuentes y análisis."
        }
      ],
      "evidence": [
        "README: identidad UnADM, entrada canónica, integridad académica.",
        "Programa analítico: cinco ejes de trabajo reutilizables.",
        "Historial de ciclos: incidencias de salida no parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 21: se deduplican reglas repetidas y variantes ortográficas sin pérdida semántica.",
      "Ciclo 21: se refuerza transferencia lateral por patrones, sin copiar conclusiones ni bibliografía exclusiva.",
      "Ciclo 21: se conserva trazabilidad de supuestos por falta de consigna local completa."
    ]
  }
}