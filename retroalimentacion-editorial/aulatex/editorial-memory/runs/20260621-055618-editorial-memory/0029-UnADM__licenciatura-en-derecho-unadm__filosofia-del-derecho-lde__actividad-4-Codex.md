{
  "summary": [
    "Se consolida refuerzo lateral para Actividad 4 con deduplicación lossless.",
    "Se preservan reglas institucionales UnADM, estructura editorial y control de calidad.",
    "Se transfiere solo patrón reutilizable desde Actividad 1, sin copiar conclusiones ni bibliografía exclusiva.",
    "Se mantiene validación JSON estricta por antecedentes de salidas no parseables.",
    "Supuesto: la consigna específica de Actividad 4 no está visible; se conserva plantilla base verificable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato académico.",
    "Alinear la actividad a Licenciatura en Derecho y Filosofía del Derecho.",
    "Usar la carpeta de asignatura como entrada canónica documental.",
    "Vincular ubicación curricular a semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Separar hechos, conceptos, argumentos y postura personal.",
    "Alinear el producto al formato solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Adaptar Actividad 4 a los cinco ejes del programa analítico.",
    "Incluir explícitamente problema, conceptos o normas, evidencia y análisis propio.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir que bibliografía de otra semana aplica automáticamente a Actividad 4."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar correspondencia entre producto entregable y consigna local de Actividad 4.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Citar en .tex solo claves existentes en .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y referencias de archivo.",
    "Corregir nombres de archivo con caracteres dañados antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y jurídicas verificables (UnADM, SCJN, UNAM-IIJ).",
    "Registrar fuentes específicas de Actividad 4 en el .bib de la asignatura.",
    "No inventar referencias ni metadatos faltantes.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib parece orientado a otra semana; verificar pertinencia antes de reutilizar."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Mantener unión-dedupe sin regresión de reglas útiles previas.",
    "Transferir solo patrones generales cuando falte consigna textual local.",
    "No trasladar redacción literal, conclusiones ni bibliografía exclusiva entre hermanos.",
    "Aplicar normalización manual en nodos con historial de salida no estructurada."
  ],
  "open_questions": [
    "Confirmar consigna exacta de Actividad 4: producto, extensión y criterios de evaluación.",
    "Confirmar si el entregable es reporte, presentación u otro formato.",
    "Confirmar rúbrica docente específica para ajustar profundidad argumentativa.",
    "Confirmar nombre canónico final del .bib de la asignatura.",
    "Confirmar si Actividad 4 requiere bibliografía propia incremental."
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
        "Carpeta de asignatura como entrada canónica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos.",
        "Asignatura: Filosofía del Derecho."
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
      "Convertir la planeación semanal en productos académicos sólidos y verificables.",
      "Asegurar trazabilidad entre problema, evidencia, análisis y cierre jurídico."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Secciones funcionales con lógica jurídica.",
      "Cita verificable en cada afirmación sustantiva.",
      "Marcado explícito de supuestos cuando falte dato local."
    ],
    "argumentative_patterns": [
      "Plantear problema.",
      "Delimitar marco conceptual y normativo.",
      "Contrastar fuentes con análisis propio.",
      "Emitir postura justificada.",
      "Cerrar con conclusión aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalización estructurada",
        "Validación JSON estricta",
        "Ejes editoriales de la asignatura",
        "Integridad académica y verificabilidad",
        "Conclusión jurídica con criterio propio"
      ],
      "citations": [
        "README.md de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Tono y formato académico",
          "kind": "supports",
          "justification": "La pauta editorial exige alineación institucional explícita."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay reutilización segura."
        },
        {
          "source": "Ejes editoriales de la asignatura",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Definen el orden problema-conceptos-evidencia-análisis-cierre."
        },
        {
          "source": "Integridad académica y verificabilidad",
          "target": "Conclusión jurídica con criterio propio",
          "kind": "supports",
          "justification": "La conclusión debe derivar de evidencia y razonamiento."
        }
      ],
      "evidence": [
        "README establece identidad UnADM, integridad académica y conclusión jurídica propia.",
        "Programa analítico fija cinco ejes de trabajo reutilizables.",
        "Historial del nodo reporta salidas no parseables; justifica gate JSON."
      ]
    },
    "reinforcement_log": [
      "Ciclo 29: se refuerza transferencia lateral por analogía controlada.",
      "Ciclo 29: se deduplican reglas repetidas y se conserva cobertura total sin recorte útil.",
      "Ciclo 29: se elimina arrastre de contenido específico de Actividad 1 y se mantienen solo patrones reutilizables."
    ]
  }
}