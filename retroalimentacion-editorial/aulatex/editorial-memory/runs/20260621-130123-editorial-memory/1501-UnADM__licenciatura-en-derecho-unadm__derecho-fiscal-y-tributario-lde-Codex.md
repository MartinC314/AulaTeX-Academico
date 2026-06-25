{
  "summary": [
    "Se mantiene sincronización transversal con estrategia conservadora y sin regresión.",
    "Se transfieren solo abstracciones editoriales estables desde actividad de Filosofía hacia materia Fiscal.",
    "Se preserva compresión lossless por unión y deduplicación.",
    "Se refuerza normalización obligatoria de salidas no JSON antes de propagación.",
    "Se consolida núcleo reusable: problema, conceptos/normas, evidencia, análisis propio y conclusión jurídica.",
    "Se evita traslado de contenido temático específico de Filosofía al dominio Fiscal [supuesto]."
  ],
  "identity_rules": [
    "Conservar identidad UnADM en tono, portada y metadatos.",
    "Usar contexto curricular local verificado: Derecho fiscal y tributario, semestre 6, bloque 1, obligatoria, 8 créditos.",
    "Usar carpeta de asignatura como entrada canónica editorial.",
    "Marcar como [supuesto] todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "No mezclar identidad curricular de Filosofía con identidad curricular de Fiscal."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Alinear el producto final con planeación semanal y consigna vigente.",
    "Cerrar con conclusión jurídica transferible a práctica profesional.",
    "Mantener separación funcional entre reporte .tex, presentación .tex y .bib local.",
    "Corregir rutas o slugs truncados en README y programa analítico antes de publicar."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Evitar entregas meramente descriptivas.",
    "Vincular análisis fiscal-tributario con aplicación profesional concreta.",
    "No asumir fuentes de otras semanas o materias sin validación local."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar consistencia entre metadatos de portada y programa analítico.",
    "Confirmar integridad de .tex: entornos cerrados y compilación sin errores críticos.",
    "Corregir placeholders y tokens sin expandir antes de liberar."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Sustituir expresiones de plantilla sin expandir en README, programa y .tex.",
    "Completar campos pendientes de portada y authortable antes de compilar.",
    "No copiar bloques LaTeX completos entre nodos; transferir solo patrones."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y normas jurídicas verificables.",
    "Registrar fuentes específicas por actividad en derecho-fiscal-y-tributario.bib.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "No transferir bibliografía temática de Filosofía como obligatoria en Fiscal [supuesto]."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Compartir hacia nodos no equivalentes solo reglas abstractas y estables.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar propagar redacción literal, ejemplos locales o citas no verificadas.",
    "Mantener política de no regresión: nunca eliminar reglas útiles previas.",
    "Aplicar normalización manual en ciclos con herencia ambigua."
  ],
  "open_questions": [
    "Confirmar formato de citación exigido por la materia fiscal.",
    "Confirmar si autor y matrícula deben permanecer en plantillas compartidas.",
    "Confirmar figura docente para portada final.",
    "Resolver tokens Slug sin expandir en README y programa analítico.",
    "Verificar cierre completo del bloque authortable del reporte .tex."
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
        "Materia destino: Derecho fiscal y tributario.",
        "Semestre 6, bloque 1, obligatoria, 8 créditos."
      ]
    },
    "essence": [
      "Problema jurídico inicial.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos y verificables.",
      "Asegurar consistencia editorial entre actividades y materia.",
      "Garantizar trazabilidad metodológica sin contaminar dominios temáticos."
    ],
    "style_markers": [
      "Supuestos etiquetados.",
      "Sin afirmaciones sin fuente.",
      "Secciones funcionales con cierre profesional.",
      "Sin relleno descriptivo."
    ],
    "argumentative_patterns": [
      "Plantear problema concreto.",
      "Delimitar marco conceptual-normativo.",
      "Contrastar fuentes y fijar postura.",
      "Concluir con implicación práctica jurídica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalización JSON",
        "Problema jurídico",
        "Marco normativo",
        "Evidencia verificable",
        "Análisis propio",
        "Conclusión transferible",
        "Consistencia .tex/.bib"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia segura."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "La argumentación requiere conflicto definido."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica exige fundamento explícito."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La trazabilidad de fuentes sostiene validez editorial."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Consistencia .tex/.bib",
          "kind": "develops",
          "justification": "La identidad se materializa en formato y referencias coherentes."
        }
      ],
      "evidence": [
        "README de la materia: ubicación curricular y pauta editorial.",
        "Programa analítico: propósito, ejes y regla bibliográfica local.",
        "derecho-fiscal-y-tributario.bib: base institucional verificable.",
        "Herencia transversal validada por abstracciones metodológicas, no por contenido temático."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: deduplicación completada sin pérdida de reglas útiles.",
      "Se reforzó gate de JSON parseable como condición de propagación.",
      "Se consolidó patrón argumentativo común reusable entre actividades.",
      "Se mantuvo separación entre identidad local fiscal y origen filosófico.",
      "Se preservó política de no invención de fuentes y marcado de supuestos."
    ]
  }
}