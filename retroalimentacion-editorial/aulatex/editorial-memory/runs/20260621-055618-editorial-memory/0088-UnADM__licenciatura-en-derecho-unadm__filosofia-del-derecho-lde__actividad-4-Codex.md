{
  "summary": [
    "Se consolida memoria lateral para Actividad 4 con deduplicación lossless y sin recorte útil.",
    "Se preserva identidad UnADM, marco curricular y pauta editorial común de la asignatura.",
    "Se refuerza el flujo reusable: problema, conceptos/fuentes, análisis propio y conclusión jurídica.",
    "Se mantiene validación JSON estricta por antecedentes de salidas no parseables.",
    "Se conserva regla de marcar supuestos cuando falte consigna local verificable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato académico.",
    "Alinear la actividad a Licenciatura en Derecho y asignatura Filosofía del Derecho.",
    "Ubicar la materia en semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el producto al tipo solicitado en la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Adaptar Actividad 4 a los ejes del programa analítico.",
    "Incluir explícitamente problema, conceptos, evidencia y postura propia.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No trasladar conclusiones específicas de Actividad 1 a Actividad 4."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de reutilizar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna de Actividad 4.",
    "Normalizar respuestas no estructuradas heredadas antes de propagación recursiva."
  ],
  "latex_rules": [
    "Usar acentos y codificación correcta en español en .tex y .bib.",
    "Citar solo claves existentes en el .bib activo.",
    "Mantener claves BibTeX estables para evitar rupturas de compilación.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Verificar nombres de archivo del README antes de referenciarlos.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: el .bib canónico esperado es filosofia-del-derecho.bib por slug visible."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y jurídicas verificables.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Agregar fuentes de Actividad 4 en el .bib de asignatura solo si aplican a su consigna.",
    "No inventar referencias ni metadatos faltantes.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Registrar URL verificable cuando la fuente sea digital.",
    "Supuesto: filosofia-del-derecho-clean.bib está orientado a otra actividad temática; validar reutilización."
  ],
  "propagation_hints": [
    "Propagar solo patrones reutilizables de identidad, estructura y calidad.",
    "Evitar copiar redacción literal, conclusiones y bibliografía exclusiva entre actividades hermanas.",
    "Mantener unión-dedupe sin regresión de reglas útiles previas.",
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Si falta consigna local, transferir plantilla base y abrir preguntas."
  ],
  "open_questions": [
    "Confirmar consigna exacta de Actividad 4: producto, extensión y criterios.",
    "Confirmar rúbrica docente específica de evaluación para Actividad 4.",
    "Confirmar si Actividad 4 requiere reporte, presentación u otro formato.",
    "Confirmar nombre canónico final del archivo .bib en uso.",
    "Confirmar si se reutiliza bibliografía existente o se crea bloque incremental propio."
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
      "Conceptos, normas y doctrina pertinentes.",
      "Producto alineado a planeación.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en entregables académicos sólidos.",
      "Asegurar claridad jurídica, evidencia verificable y cierre argumentativo.",
      "Mantener continuidad editorial entre actividades sin contaminar especificidades."
    ],
    "style_markers": [
      "Definir objetivo antes del desarrollo.",
      "Separar hechos, conceptos, argumentos y postura.",
      "Citar de forma explícita cada afirmación sustantiva.",
      "Marcar supuestos de manera visible.",
      "Cerrar con conclusión práctica para el ejercicio jurídico."
    ],
    "argumentative_patterns": [
      "Plantear problema inicial.",
      "Construir marco conceptual y normativo.",
      "Contrastar evidencia con análisis propio.",
      "Fijar postura razonada.",
      "Concluir con aplicabilidad jurídica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ejes editoriales de Filosofía del Derecho",
        "Normalización estructurada",
        "Validación JSON estricta",
        "Integridad académica y verificabilidad",
        "Relación problema-evidencia-conclusión"
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
          "justification": "La pauta institucional define estilo y consistencia."
        },
        {
          "source": "Ejes editoriales de Filosofía del Derecho",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Los ejes ordenan la secuencia argumentativa reusable."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia segura."
        },
        {
          "source": "Integridad académica y verificabilidad",
          "target": "Conclusión jurídica propia",
          "kind": "supports",
          "justification": "La conclusión debe derivar de evidencia trazable."
        }
      ],
      "evidence": [
        "README fija identidad UnADM, entrada canónica y exigencia de citas verificables.",
        "Programa analítico define cinco ejes de trabajo transferibles.",
        "Antecedentes de salidas no parseables justifican gate JSON estricto."
      ]
    },
    "reinforcement_log": [
      "Ciclo 88: refuerzo lateral aplicado por analogía controlada entre nodos hermanos.",
      "Se deduplicaron reglas repetidas con variantes ortográficas sin pérdida funcional.",
      "Se conservaron reglas útiles previas y se eliminaron relaciones no permitidas por esquema.",
      "Se evitaron fuentes inventadas y contenido específico no verificable de Actividad 1."
    ]
  }
}