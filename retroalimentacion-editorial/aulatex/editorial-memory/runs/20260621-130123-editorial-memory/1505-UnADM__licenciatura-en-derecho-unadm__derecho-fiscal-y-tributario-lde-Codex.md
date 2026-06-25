{
  "summary": [
    "Se mantiene sincronización transversal sin regresión y con deduplicación lossless.",
    "Se transfieren solo abstracciones estables desde actividad origen hacia materia destino.",
    "Se refuerzan identidad UnADM, estructura reusable, gates de calidad y grafo conceptual.",
    "Se conserva regla de normalización obligatoria antes de propagación recursiva.",
    "Se confirma contexto local del destino con README, programa analítico y .bib existente.",
    "Se detectan tokens sin expandir y rutas truncadas como deuda técnica prioritaria."
  ],
  "identity_rules": [
    "Conservar identidad institucional UnADM en tono, portada y metadatos.",
    "Usar contexto curricular verificado del destino: semestre 6, bloque 1, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como entrada canónica editorial.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "No transferir datos personales de plantilla como norma editorial global."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener separación entre reporte .tex, presentación .tex y .bib local."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Evitar entregas solo descriptivas.",
    "Vincular análisis fiscal-tributario con aplicación profesional concreta.",
    "No asumir fuentes de otras semanas o materias sin validación local."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Corregir tokens sin expandir en README y programa analítico antes de publicar.",
    "Corregir rutas truncadas o rotas antes de cierre editorial."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Cerrar correctamente todos los entornos LaTeX truncados.",
    "No copiar bloques completos de plantilla entre nodos; transferir solo reglas."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y normativa verificable.",
    "Registrar fuentes específicas por actividad en derecho-fiscal-y-tributario.bib.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Usar malla curricular solo para respaldo de ubicación curricular."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validación JSON y estructura.",
    "Compartir a nodos transversales solo patrones editoriales estables, no contenido temático literal.",
    "Priorizar gates de calidad e identidad sobre detalles de una actividad concreta.",
    "Aplicar estrategia progresiva y conservadora: sumar mejoras verificables sin borrar reglas útiles.",
    "Si un nodo está incompleto, crear cerebro mínimo con vacíos explícitos."
  ],
  "open_questions": [
    "Confirmar formato de citación exigido por la asignatura destino.",
    "Confirmar si la figura docente debe persistir en plantilla compartida. [supuesto]",
    "Confirmar si el .bib local será único para toda la materia o por actividad. [supuesto]",
    "Confirmar corrección final de rutas truncadas en README.",
    "Confirmar resolución definitiva de expresiones $(@{...}.Slug) en archivos de control."
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
      "Marco conceptual y normativo.",
      "Análisis propio sustentado.",
      "Conclusión jurídica transferible.",
      "Trazabilidad técnica y bibliográfica."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos verificables y útiles para práctica jurídica.",
      "Mantener consistencia institucional, metodológica y técnica en toda la materia."
    ],
    "style_markers": [
      "Supuestos explícitos.",
      "Sin afirmaciones sin fuente.",
      "Secciones funcionales y cierre profesional.",
      "Sin relleno descriptivo."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/normas -> contraste -> postura propia -> conclusión aplicada.",
      "Cada afirmación sustantiva requiere fuente o etiqueta de supuesto."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema jurídico",
        "Marco normativo",
        "Análisis propio",
        "Conclusión transferible",
        "Normalización JSON",
        "Consistencia .tex/.bib"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La identidad institucional exige evidencia verificable y formato consistente."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "Sin problema delimitado no hay argumentación sólida."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica válida requiere fundamento normativo explícito."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia segura entre nodos."
        },
        {
          "source": "Consistencia .tex/.bib",
          "target": "Calidad editorial",
          "kind": "supports",
          "justification": "Evita errores de compilación y citas rotas."
        }
      ],
      "evidence": [
        "README local de Derecho fiscal y tributario.",
        "Programa analítico local de la materia.",
        "Archivo derecho-fiscal-y-tributario.bib con fuentes institucionales.",
        "Historial de salidas no parseables en ciclos previos."
      ]
    },
    "reinforcement_log": [
      "Ciclo 3: deduplicación semántica aplicada sin pérdida de reglas útiles.",
      "Ciclo 3: se reforzó transferencia transversal de método, no de contenido temático de Filosofía.",
      "Ciclo 3: se mantuvieron gates críticos de JSON, supuestos y trazabilidad bibliográfica.",
      "Ciclo 3: se preservó ADN argumentativo común de la Licenciatura en Derecho UnADM."
    ]
  }
}