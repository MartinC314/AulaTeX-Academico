{
  "summary": [
    "Se refuerza memoria de actividad-2 con transferencia lateral controlada desde actividad-1.",
    "Se preservan reglas válidas previas con unión-deduplicación lossless.",
    "Se mantiene normalización estructurada obligatoria antes de propagación recursiva.",
    "Se consolidan ejes editoriales troncales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se evita copiar contenido exclusivo de un nodo hermano; solo patrones reutilizables."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular actividad-2 a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como entrada canónica editorial.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el producto al formato solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante, no solo resumen descriptivo.",
    "Diferenciar postura propia, cita textual y paráfrasis.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir tema, semana o formato de actividad-2 sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar que cada afirmación sustantiva tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No eliminar reglas útiles previas; solo unir y deduplicar."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves ya citadas.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y malla curricular como base contextual.",
    "Agregar fuentes específicas de actividad en el .bib canónico de la asignatura.",
    "No inventar referencias ni metadatos bibliográficos.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Supuesto: filosofia-del-derecho-clean.bib es complemento temático y no reemplazo automático del .bib canónico."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir solo patrones generales reutilizables entre nodos hermanos.",
    "Evitar trasladar conclusiones específicas o bibliografía exclusiva sin validación local.",
    "Aplicar normalización manual cuando reaparezcan entradas no estructuradas.",
    "Mantener historial de fuentes provisionales como antecedente, no como autoridad final."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-2: tema, semana y producto requerido.",
    "Confirmar plantilla obligatoria de secciones definida por la docente.",
    "Confirmar si existe estilo de citación institucional obligatorio.",
    "Confirmar nombre canónico final del archivo .bib por tokens dañados en README.",
    "Confirmar si las fuentes de interpretación jurídica aplican a actividad-2 o solo a semana temática específica."
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
      "Problema jurídico o social que activa la actividad.",
      "Conceptos y fuentes pertinentes con respaldo verificable.",
      "Producto alineado a planeación semanal.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en entregables académicos trazables.",
      "Asegurar fundamento jurídico y evidencia verificable.",
      "Conservar coherencia entre consigna, desarrollo y cierre."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales y trazables.",
      "Marcado explícito de supuestos.",
      "Cierre con criterio jurídico propio."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/fuentes -> análisis -> conclusión.",
      "Afirmación jurídica -> evidencia verificable -> interpretación propia.",
      "Consigna local -> ajuste de formato -> validación final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalización de salidas",
        "Ejes editoriales troncales",
        "Integridad académica",
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
          "source": "Identidad institucional UnADM",
          "target": "Ejes editoriales troncales",
          "kind": "supports",
          "justification": "Define tono, propósito y estándar de entrega."
        },
        {
          "source": "Ejes editoriales troncales",
          "target": "Actividad-2",
          "kind": "develops",
          "justification": "Patrones reutilizables entre actividades hermanas."
        }
      ],
      "evidence": [
        "README fija identidad UnADM, integridad académica y cierre jurídico.",
        "Programa analítico define propósito y ejes de trabajo.",
        "Regla validada: bloquear propagación sin JSON parseable.",
        "Transferencia hermano-a-hermano limitada a patrones reutilizables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 82: se refuerza ADN editorial sin recorte, con deduplicación lossless.",
      "Se consolidan reglas de identidad, estructura, calidad y trazabilidad.",
      "Se mantiene separación entre patrones transferibles y contenido específico no transferible."
    ]
  }
}