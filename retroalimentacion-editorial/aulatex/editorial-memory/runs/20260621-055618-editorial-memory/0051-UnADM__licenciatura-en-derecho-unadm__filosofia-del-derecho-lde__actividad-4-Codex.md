{
  "summary": [
    "Se consolida refuerzo lateral entre actividades hermanas con deduplicación lossless.",
    "Se preserva identidad UnADM, marco curricular y ejes editoriales comunes.",
    "Se mantiene regla crítica: no propagar si no hay JSON parseable y estructura mínima completa.",
    "Se transfiere solo patrón reusable; no se copian conclusiones ni bibliografía exclusiva de Actividad 1.",
    "Supuesto: la consigna específica de Actividad 4 no está visible y debe confirmarse."
  ],
  "identity_rules": [
    "Mantener tono formal académico UnADM.",
    "Alinear contenido con Licenciatura en Derecho y Filosofía del Derecho.",
    "Conservar ubicación curricular: semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear formato final al producto pedido por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a práctica profesional.",
    "Separar hechos, conceptos, argumentos y postura personal."
  ],
  "activity_rules": [
    "Integrar los cinco ejes del programa analítico en cada entrega.",
    "Incluir postura argumentada del estudiante; evitar solo resumen descriptivo.",
    "Sustentar afirmaciones con evidencia verificable y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir automáticamente que fuentes de otras semanas aplican a Actividad 4.",
    "Confirmar el tipo de producto requerido antes de redactar."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de reutilizar memoria.",
    "Normalizar respuestas no estructuradas heredadas antes de propagar.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar correspondencia entre consigna local y producto generado.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Usar acentos y codificación correctos en .tex y .bib.",
    "Citar solo claves existentes en .bib.",
    "Mantener claves BibTeX estables; no renombrar sin necesidad.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver tokens sin expandir en README y programa analítico antes de fijar rutas."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y jurídicas verificables.",
    "No inventar referencias ni metadatos.",
    "Registrar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Agregar al .bib de asignatura solo fuentes realmente usadas en Actividad 4.",
    "Supuesto: filosofia-del-derecho-clean.bib parece de Semana 7; verificar pertinencia para Actividad 4."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validación JSON y estructura.",
    "Conservar reglas útiles previas y evitar regresiones.",
    "Transferir a hermanos solo patrones generales reutilizables.",
    "No transferir redacción literal ni conclusiones específicas entre actividades.",
    "Mantener bandera de normalización manual para ciclos con salidas no estructuradas.",
    "Aplicar mejora progresiva por analogía controlada con trazabilidad."
  ],
  "open_questions": [
    "Confirmar consigna exacta de Actividad 4: producto, extensión y criterios.",
    "Confirmar rúbrica docente específica para profundidad argumentativa.",
    "Confirmar nombre canónico final del .bib ante token Slug sin resolver en README.",
    "Definir si Actividad 4 usa .bib incremental o el general de asignatura.",
    "Verificar si las fuentes periodísticas actuales cumplen criterio académico de la actividad.",
    "Supuesto: el título documental heredado de Actividad 1 no aplica a Actividad 4; confirmar metadatos."
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
      "Conceptos y marco normativo.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos.",
      "Sostener trazabilidad entre consigna, evidencia y argumento.",
      "Garantizar transferibilidad profesional del cierre jurídico."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Secciones funcionales con lógica jurídica.",
      "Cita explícita por afirmación relevante.",
      "Marcado de supuestos cuando falte dato local."
    ],
    "argumentative_patterns": [
      "Plantear problema.",
      "Delimitar conceptos y norma aplicable.",
      "Contrastar fuentes con análisis propio.",
      "Fijar postura razonada.",
      "Concluir con implicación jurídica práctica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ejes editoriales de Filosofía del Derecho",
        "Normalización estructurada",
        "Validación JSON",
        "Integridad académica",
        "Coherencia pregunta-desarrollo-conclusión"
      ],
      "citations": [
        "README de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Tono y formato académico",
          "kind": "supports",
          "justification": "Define estándar transversal de todas las actividades."
        },
        {
          "source": "Ejes editoriales de Filosofía del Derecho",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Ordenan problema, conceptos, evidencia, análisis y cierre."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin formato estructurado no hay transferencia segura."
        },
        {
          "source": "Integridad académica",
          "target": "Conclusión jurídica propia",
          "kind": "supports",
          "justification": "La postura final requiere respaldo verificable."
        }
      ],
      "evidence": [
        "README exige identidad UnADM, citas verificables y conclusión jurídica propia.",
        "Programa analítico fija cinco ejes de trabajo reutilizables.",
        "Histórico de salidas no parseables justifica gate estricto de JSON."
      ]
    },
    "reinforcement_log": [
      "Ciclo 51: deduplicación de reglas repetidas en destino.",
      "Ciclo 51: se preservan reglas institucionales y de calidad previas.",
      "Ciclo 51: se agrega control explícito de no transferir contenido específico entre hermanos.",
      "Ciclo 51: se mantiene incertidumbre local como preguntas abiertas en lugar de inventar."
    ]
  }
}