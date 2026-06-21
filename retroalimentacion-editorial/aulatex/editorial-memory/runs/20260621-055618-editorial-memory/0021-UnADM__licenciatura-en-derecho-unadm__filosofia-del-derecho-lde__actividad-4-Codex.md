{
  "summary": [
    "Se consolida refuerzo lateral para Actividad 4 con deduplicación lossless.",
    "Se preservan reglas institucionales UnADM, estructura editorial y gates de calidad.",
    "Se transfiere solo patrón reusable desde Actividad 1, sin copiar redacción ni cierre específico.",
    "Se mantiene validación JSON estricta por antecedentes de salidas no parseables.",
    "Supuesto: la consigna textual de Actividad 4 no está visible; se conserva estructura base verificable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato académico.",
    "Alinear contenido con Licenciatura en Derecho y asignatura Filosofía del Derecho.",
    "Vincular ubicación curricular a semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Sostener enfoque jurídico con postura propia sustentada.",
    "Marcar como supuesto todo dato no visible en la consigna.",
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
    "Adaptar Actividad 4 a los cinco ejes del programa analítico.",
    "Incluir explícitamente problema, conceptos, evidencia y análisis propio.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Supuesto: confirmar producto exacto de Actividad 4 antes de fijar plantilla final."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar correspondencia entre producto entregable y consigna local.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Usar español con acentos correctos en .tex y .bib.",
    "Citar en .tex solo claves existentes en .bib.",
    "Mantener claves BibTeX estables para evitar rupturas de compilación.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver tokens no expandidos tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir nombres de archivo con caracteres dañados antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y jurídicas verificables.",
    "No inventar referencias ni metadatos faltantes.",
    "Registrar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Agregar al .bib de la asignatura solo fuentes realmente usadas.",
    "Supuesto: filosofia-del-derecho-clean.bib podría no corresponder a Actividad 4; validar antes de reutilizar."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Reutilizar reglas institucionales y de calidad sin perder especificidad local.",
    "Evitar regresiones: conservar reglas útiles previas confirmadas.",
    "Transferir patrones, no conclusiones ni bibliografía exclusiva entre hermanos.",
    "Si falta consigna local, propagar estructura base y abrir preguntas."
  ],
  "open_questions": [
    "Confirmar consigna textual de Actividad 4.",
    "Confirmar tipo de producto: reporte, presentación u otro.",
    "Confirmar rúbrica y criterios de evaluación locales.",
    "Confirmar fuentes obligatorias de la semana de Actividad 4.",
    "Confirmar nombre canónico final del archivo .bib de la asignatura."
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
      "Transformar planeación semanal en productos académicos con fundamento jurídico y evidencia.",
      "Garantizar continuidad editorial entre actividades sin contaminar contenido específico."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Secciones funcionales con lógica jurídica.",
      "Cita explícita en afirmaciones sustantivas.",
      "Marcado de supuestos cuando falte evidencia local."
    ],
    "argumentative_patterns": [
      "Plantear problema.",
      "Construir marco conceptual y normativo.",
      "Contrastar fuentes con análisis propio.",
      "Emitir postura justificada.",
      "Concluir con aplicabilidad jurídica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ejes editoriales de Filosofía del Derecho",
        "Normalización estructurada",
        "Validación JSON estricta",
        "Integridad académica verificable"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/programa-analitico-filosofia-del-derecho.md"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad académica verificable",
          "kind": "supports",
          "justification": "La pauta editorial exige citas verificables y formato institucional."
        },
        {
          "source": "Ejes editoriales de Filosofía del Derecho",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Los cinco ejes ordenan el desarrollo argumentativo."
        },
        {
          "source": "Normalización estructurada",
          "target": "Validación JSON estricta",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay propagación segura."
        }
      ],
      "evidence": [
        "README: identidad UnADM, entrada canónica y conclusión jurídica propia.",
        "Programa analítico: cinco ejes reutilizables.",
        "Historial: antecedentes de salida no parseable en ciclos previos."
      ]
    },
    "reinforcement_log": [
      "Ciclo 21: deduplicación semántica aplicada sin recorte de reglas útiles.",
      "Ciclo 21: se reforzó transferencia por patrones reutilizables entre nodos hermanos.",
      "Ciclo 21: se mantuvieron supuestos explícitos donde falta consigna local."
    ]
  }
}