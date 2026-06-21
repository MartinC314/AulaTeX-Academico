{
  "summary": [
    "Se consolida refuerzo lateral entre actividades hermanas con deduplicación lossless.",
    "Se preserva ADN UnADM: identidad institucional, estructura por ejes y cierre jurídico propio.",
    "Se mantiene validación JSON estricta por antecedentes de salidas no parseables.",
    "Se transfieren solo patrones reutilizables; no se copian conclusiones ni bibliografía exclusiva de Actividad 1.",
    "Supuesto: falta consigna visible de Actividad 4; se mantienen reglas base y preguntas abiertas."
  ],
  "identity_rules": [
    "Mantener tono formal académico y precisión jurídica.",
    "Alinear toda entrega con UnADM y Licenciatura en Derecho.",
    "Vincular contexto curricular: semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Separar hechos, conceptos, argumentos y postura personal.",
    "Alinear formato final al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Adaptar Actividad 4 a los cinco ejes del programa analítico.",
    "Incluir problema, conceptos o normas, evidencia y postura propia.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir que bibliografía de otra semana aplica sin validación."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de reutilizar aguas abajo.",
    "Normalizar respuestas no estructuradas heredadas antes de propagar.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna específica de Actividad 4."
  ],
  "latex_rules": [
    "Usar acentos y codificación correcta en español en .tex y .bib.",
    "Citar en .tex solo claves existentes en .bib.",
    "Mantener claves BibTeX estables; no renombrar claves activas sin migración completa.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Verificar nombres de archivos en README antes de referenciarlos.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib por slug."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y jurídicas verificables.",
    "Registrar fuentes específicas de la actividad en el .bib de la asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Usar filosofia-del-derecho-clean.bib solo si la consigna de Actividad 4 coincide temáticamente."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Reutilizar reglas institucionales de calidad sin perder especificidad local.",
    "Aplicar unión y deduplicación semántica; evitar regresiones.",
    "Propagar solo patrones generales cuando falte consigna textual.",
    "Mantener bandera de normalización manual para ciclos con salidas históricas no estructuradas."
  ],
  "open_questions": [
    "Confirmar consigna textual de Actividad 4: producto, extensión y rúbrica.",
    "Confirmar si Actividad 4 requiere reporte, presentación u otro formato.",
    "Confirmar fuentes obligatorias de la semana de Actividad 4.",
    "Confirmar nombre canónico final del archivo .bib con token Slug resuelto.",
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
      "Conceptos y marco normativo o doctrinal.",
      "Evidencia verificable.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos y verificables.",
      "Asegurar trazabilidad editorial entre identidad institucional, argumentación y evidencia."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Secciones funcionales con lógica jurídica.",
      "Citas explícitas por afirmación relevante.",
      "Uso explícito de supuestos cuando faltan datos locales."
    ],
    "argumentative_patterns": [
      "Plantear problema.",
      "Delimitar conceptos y normas aplicables.",
      "Contrastar fuentes con análisis propio.",
      "Emitir postura justificada.",
      "Cerrar con conclusión aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ejes editoriales de Filosofía del Derecho",
        "Normalización estructurada",
        "Validación JSON",
        "Integridad académica",
        "Conclusión jurídica transferible"
      ],
      "citations": [
        "README de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Tono formal académico",
          "kind": "supports",
          "justification": "La pauta editorial exige alineación institucional explícita."
        },
        {
          "source": "Ejes editoriales de Filosofía del Derecho",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Los ejes definen orden de desarrollo y cierre."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay reutilización segura."
        },
        {
          "source": "Integridad académica",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión debe derivar de evidencia y análisis propio."
        }
      ],
      "evidence": [
        "README define identidad, integridad académica y conclusión jurídica propia.",
        "Programa analítico define cinco ejes reutilizables.",
        "Antecedentes de salidas no parseables justifican gate de JSON estricto.",
        "Supuesto: consigna local de Actividad 4 no visible."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas con variantes ortográficas.",
      "Se preservaron reglas útiles previas sin recorte semántico.",
      "Se reforzó transferencia lateral por patrones, no por contenido específico.",
      "Se mantuvieron supuestos abiertos donde falta evidencia local."
    ]
  }
}