{
  "summary": [
    "Sincronización transversal aplicada con estrategia conservadora y sin regresión.",
    "Se preservan reglas institucionales UnADM y ejes metodológicos reutilizables.",
    "Se deduplica memoria por unión sin recorte de reglas útiles previas.",
    "Se refuerza normalización JSON antes de propagación recursiva.",
    "Se mantiene separación entre identidad local fiscal y abstracciones transferidas.",
    "Supuesto: no hay consigna de actividad específica en destino al cierre de ciclo 12."
  ],
  "identity_rules": [
    "Conservar identidad UnADM en tono, portada y metadatos.",
    "Usar contexto curricular verificado del destino: semestre 6, bloque 1, obligatoria, 8 créditos.",
    "Usar clave de curso LDE-S6B1 cuando aplique.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Verificar datos personales y figura docente antes de entrega final."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener separación entre reporte .tex, presentación .tex y .bib local.",
    "Corregir rutas o tokens dinámicos sin expandir en README y programa analítico."
  ],
  "activity_rules": [
    "Incluir problema jurídico explícito al inicio.",
    "Incluir conceptos, normas, doctrina o datos pertinentes.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Vincular análisis fiscal-tributario con aplicación profesional concreta.",
    "Validar que el producto final corresponda a la consigna de la actividad."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar consistencia entre metadatos de portada y programa analítico.",
    "Revisar placeholders o entornos LaTeX truncados antes de compilar."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Completar campos pendientes de plantilla antes de compilar.",
    "Cerrar correctamente entornos tabular y el documento.",
    "Sustituir tokens sin expandir tipo $(@{...}.Slug) por nombres reales de archivo."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y normas jurídicas verificables.",
    "Registrar fuentes específicas por actividad en derecho-fiscal-y-tributario.bib.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL.",
    "Usar la malla curricular solo para respaldo de datos curriculares.",
    "Supuesto: bibliografía temática fiscal adicional se define por consigna semanal."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Compartir solo abstracciones estables en saltos transversales.",
    "No transferir redacción literal ni bibliografía temática de otra materia.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Mantener compresión lossless por unión y deduplicación.",
    "Aplicar normalización manual cuando la entrada heredada sea ambigua."
  ],
  "open_questions": [
    "Confirmar rúbrica de evaluación específica de la próxima actividad fiscal.",
    "Confirmar formato de citación requerido por la asignatura.",
    "Confirmar si autor y matrícula deben permanecer en plantillas compartidas.",
    "Confirmar figura docente a nivel de plantilla.",
    "Confirmar resolución final de rutas truncadas en README.",
    "Confirmar que el .bib canónico único del destino sea derecho-fiscal-y-tributario.bib."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Sobrio y profesional."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Trazabilidad de supuestos y fuentes.",
        "Carpeta de asignatura como entrada canónica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho fiscal y tributario.",
        "Semestre 6, bloque 1, obligatoria, 8 créditos.",
        "Clave local LDE-S6B1."
      ]
    },
    "essence": [
      "Problema jurídico inicial.",
      "Marco conceptual y normativo pertinente.",
      "Análisis propio sustentado.",
      "Conclusión jurídica transferible.",
      "Consistencia técnica .tex/.bib/JSON."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos evaluables y verificables.",
      "Sostener una línea editorial institucional reusable entre actividades.",
      "Garantizar calidad argumentativa y trazabilidad documental."
    ],
    "style_markers": [
      "Supuestos explícitos.",
      "Sin afirmaciones sin fuente.",
      "Estructura funcional por secciones.",
      "Cierre con implicación práctica jurídica."
    ],
    "argumentative_patterns": [
      "Problema breve y concreto.",
      "Delimitación conceptual y normativa.",
      "Contraste de fuentes con postura propia.",
      "Conclusión aplicada al ejercicio profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema jurídico",
        "Marco normativo",
        "Análisis propio",
        "Conclusión transferible",
        "Normalización JSON",
        "Consistencia LaTeX-BibTeX"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad académica con citas verificables",
          "kind": "supports",
          "justification": "La identidad institucional exige trazabilidad y evidencia verificable."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "Sin problema delimitado no hay argumentación jurídica sólida."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión profesional requiere fundamento normativo explícito."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "La transferencia segura entre nodos requiere estructura parseable."
        },
        {
          "source": "Consistencia LaTeX-BibTeX",
          "target": "Calidad editorial",
          "kind": "supports",
          "justification": "Compilación limpia y citas consistentes evitan degradación documental."
        }
      ],
      "evidence": [
        "README de la materia con ubicación curricular y pauta editorial.",
        "Programa analítico con ejes de trabajo y regla bibliográfica local.",
        "derecho-fiscal-y-tributario.bib con fuentes institucionales base.",
        "Historial de salidas no parseables que justifica gate de normalización JSON."
      ]
    },
    "reinforcement_log": [
      "Ciclo 12: se refuerzan reglas transversales estables sin trasladar contenido temático de Filosofía del Derecho.",
      "Ciclo 12: deduplicación aplicada en identidad, estructura, quality gates y patrón argumentativo.",
      "Ciclo 12: se conserva ADN editorial mínimo del destino con trazabilidad de supuestos.",
      "Ciclo 12: se mantiene política de no regresión y propagación condicionada a JSON válido."
    ]
  }
}