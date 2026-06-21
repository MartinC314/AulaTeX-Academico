{
  "summary": [
    "Se consolida transferencia lateral desde Actividad 1 a Actividad 4 con deduplicación lossless.",
    "Se preservan reglas institucionales UnADM, ejes editoriales y control de calidad estructural.",
    "Se refuerza validación JSON estricta por antecedentes de salidas no parseables.",
    "Se mantiene separación entre patrones reutilizables y contenido específico no transferible.",
    "Supuesto: la consigna local de Actividad 4 no está completa; se mantiene estructura base verificable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato académico.",
    "Alinear la actividad con Licenciatura en Derecho y asignatura Filosofía del Derecho.",
    "Vincular ubicación curricular a semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el producto al formato solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Separar hechos, conceptos, argumentos y postura personal."
  ],
  "activity_rules": [
    "Incluir explícitamente problema, conceptos, evidencia y análisis propio.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Adaptar Actividad 4 a los ejes del programa analítico sin copiar conclusiones de Actividad 1.",
    "No asumir que bibliografía de otra semana aplica a Actividad 4 sin confirmación."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna específica de Actividad 4."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Citar en .tex solo claves existentes en .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y referencias de .bib.",
    "Corregir nombres de archivo con caracteres dañados antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Registrar fuentes específicas de Actividad 4 en el .bib de la asignatura.",
    "No inventar referencias ni metadatos faltantes.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Usar filosofia-del-derecho-clean.bib solo si coincide con la consigna local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir solo patrones generales: identidad, estructura, calidad, conceptos y relaciones recurrentes.",
    "Evitar copiar redacción literal, conclusiones o bibliografía exclusiva entre actividades hermanas.",
    "Preservar reglas útiles previas y agregar solo mejoras verificables.",
    "Mantener bandera de normalización manual para ciclos con salidas históricamente defectuosas."
  ],
  "open_questions": [
    "Confirmar consigna completa de Actividad 4: producto, extensión y rúbrica.",
    "Confirmar si Actividad 4 requiere reporte, presentación u otro formato.",
    "Confirmar nombre canónico final del .bib por token Slug no resuelto en README.",
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
        "Entrada canónica en carpeta de asignatura.",
        "Normalización obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2.",
        "Asignatura obligatoria de 8 créditos.",
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
      "Convertir planeación semanal en entregables con fundamento jurídico y evidencia.",
      "Asegurar trazabilidad entre problema, fuentes, análisis y cierre profesional."
    ],
    "style_markers": [
      "Definir objetivo al inicio.",
      "Usar secciones funcionales estables.",
      "Sostener afirmaciones con citas explícitas.",
      "Marcar supuestos cuando falte dato local."
    ],
    "argumentative_patterns": [
      "Plantear problema.",
      "Desarrollar marco conceptual y normativo.",
      "Contrastar fuentes con análisis propio.",
      "Emitir postura justificada.",
      "Cerrar con conclusión jurídica aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ejes editoriales de Filosofía del Derecho",
        "Integridad académica y verificabilidad",
        "Normalización estructurada",
        "Validación JSON estricta",
        "Relación problema-evidencia-conclusión"
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
          "justification": "La pauta editorial exige alineación institucional explícita."
        },
        {
          "source": "Ejes editoriales de Filosofía del Derecho",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Los cinco ejes ordenan la construcción del producto."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia segura."
        },
        {
          "source": "Integridad académica y verificabilidad",
          "target": "Conclusión jurídica propia",
          "kind": "supports",
          "justification": "La conclusión requiere evidencia y postura argumentada."
        }
      ],
      "evidence": [
        "README: identidad UnADM, entrada canónica, integridad académica y conclusión jurídica propia.",
        "Programa analítico: ejes problema, conceptos, producto, análisis, conclusión.",
        "Historial de ciclos: salidas no parseables obligan gate de JSON estricto."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas de tono, estructura y calidad.",
      "Se preservaron reglas útiles previas sin recorte semántico.",
      "Se eliminaron transferencias de contenido específico de Actividad 1 no reutilizable.",
      "Se reforzó control de supuestos por falta de consigna local completa.",
      "Se mantuvo compatibilidad editorial para propagación lateral recursiva."
    ]
  }
}