{
  "summary": [
    "Se consolida refuerzo lateral para actividad-2 con transferencia de patrones reutilizables desde actividad-1.",
    "Se preservan reglas válidas previas con unión y deduplicación lossless.",
    "Se mantiene normalización obligatoria antes de propagación recursiva.",
    "Se refuerzan ejes troncales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se evita copiar conclusiones, redacción literal o bibliografía exclusiva de un nodo hermano."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y criterios académicos.",
    "Vincular actividad-2 a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el formato final al producto solicitado en la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Diferenciar postura propia, cita textual y paráfrasis.",
    "Evitar entregas solo descriptivas; exigir argumentación.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir tema, semana o formato de actividad-2 sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de reutilizar.",
    "Confirmar respaldo o marca de supuesto en cada afirmación sustantiva.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No eliminar reglas útiles previas; solo unir y deduplicar."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables y compatibles entre .tex y .bib.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y rutas de archivos."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar fuentes específicas de actividad en el .bib canónico de la asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Tratar filosofia-del-derecho-clean.bib como complemento temático, no reemplazo automático [supuesto]."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir solo patrones reutilizables entre hermanos.",
    "Evitar propagar contenido específico de actividad-1 como si fuera de actividad-2.",
    "Aplicar normalización manual cuando aparezcan salidas heredadas no estructuradas.",
    "Mantener trazabilidad de cambios por ciclo para evitar regresiones."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-2: tema, semana y producto.",
    "Confirmar rúbrica docente específica para calibrar profundidad argumentativa.",
    "Confirmar si existe estilo de citación institucional obligatorio [supuesto: no confirmado].",
    "Confirmar nombre canónico final del .bib de asignatura por tokens Slug pendientes.",
    "Confirmar si actividad-2 reutiliza bibliografía existente o requiere bloque bibliográfico propio."
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
      "Problema jurídico o social como punto de partida.",
      "Conceptos y normas con respaldo verificable.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica aplicable a la práctica.",
      "Normalización estructurada antes de toda propagación."
    ],
    "reason_for_being": [
      "Transformar planeación semanal en productos académicos sólidos y trazables.",
      "Asegurar continuidad editorial entre actividades sin pérdida de reglas válidas.",
      "Reforzar pensamiento jurídico argumentativo en cada entrega."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales y trazables.",
      "Marcado explícito de supuestos.",
      "Cierre con criterio jurídico propio.",
      "Consistencia cita-bibliografía."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/fuentes -> análisis -> conclusión.",
      "Afirmación jurídica -> evidencia verificable -> interpretación propia.",
      "Consigna local -> ajuste de formato -> verificación de calidad."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ejes editoriales troncales",
        "Integridad académica",
        "Normalización de salidas",
        "Trazabilidad cita-bibliografía",
        "Transferencia lateral controlada"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/programa-analitico-filosofia-del-derecho.md"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Ejes editoriales troncales",
          "kind": "supports",
          "justification": "Define tono, propósito y estándar de entrega."
        },
        {
          "source": "Normalización de salidas",
          "target": "Transferencia lateral controlada",
          "kind": "depends_on",
          "justification": "Sin estructura válida no hay propagación segura."
        },
        {
          "source": "Trazabilidad cita-bibliografía",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Permite auditar respaldo de afirmaciones."
        },
        {
          "source": "Ejes editoriales troncales",
          "target": "Actividad 2",
          "kind": "develops",
          "justification": "Guían el desarrollo sin copiar contenido específico de actividad-1."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad académica, conclusión jurídica.",
        "Programa analítico: propósito y ejes de trabajo transferibles.",
        "Regla histórica: bloquear propagación sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 61: refuerzo lateral aplicado con analogía controlada entre nodos hermanos.",
      "Se conservaron reglas institucionales, de estructura, calidad y bibliografía sin recorte.",
      "Se eliminaron duplicados semánticos y se mantuvo compresión lossless.",
      "Se añadieron solo mejoras verificables desde README y programa analítico local."
    ]
  }
}