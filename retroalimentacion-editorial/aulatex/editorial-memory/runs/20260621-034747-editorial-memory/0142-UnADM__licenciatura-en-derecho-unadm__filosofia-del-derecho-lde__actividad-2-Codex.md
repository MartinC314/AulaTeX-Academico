{
  "summary": [
    "Se refuerza actividad-2 con transferencia lateral desde actividad-1 por patrones reutilizables.",
    "Se conserva identidad UnADM, ejes editoriales troncales y controles de calidad sin regresión.",
    "Se deduplica memoria por unión lossless y se eliminan redundancias no informativas.",
    "Se mantiene regla crítica: no propagar salidas no estructuradas sin normalización previa.",
    "Se evita copiar contenido exclusivo del hermano; solo se transfieren estructura, calidad y relaciones estables."
  ],
  "identity_rules": [
    "Mantener tono formal académico y precisión jurídica alineada con UnADM.",
    "Vincular cada entrega a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto todo dato no confirmado en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual de la actividad antes del desarrollo.",
    "Separar en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear formato final al producto solicitado en la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener trazabilidad entre afirmaciones, citas y bibliografía."
  ],
  "activity_rules": [
    "Ajustar actividad-2 a la instrucción docente disponible.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Diferenciar postura propia, cita textual y paráfrasis.",
    "No asumir tema, semana o formato sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar esquema mínimo completo antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en cada afirmación sustantiva.",
    "Verificar consistencia entre citas en texto y archivo .bib.",
    "No eliminar reglas útiles previas; solo unir y deduplicar."
  ],
  "latex_rules": [
    "Usar acentos y codificación correcta en español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves ya citadas sin necesidad.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y rutas de archivos.",
    "Confirmar nombres canónicos de archivos antes de referenciarlos."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar fuentes específicas de actividad en el .bib canónico de la asignatura.",
    "No inventar referencias ni metadatos bibliográficos.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Tratar filosofia-del-derecho-clean.bib como complemento temático (supuesto) y no como sustitución automática."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validación de JSON y estructura.",
    "Transferir a nodos hermanos solo patrones generales reutilizables.",
    "Aplicar normalización manual cuando reaparezcan entradas no estructuradas.",
    "Preservar historial de fuentes provisionales como antecedente, sin volverlo regla definitiva.",
    "Evitar regresiones: mantener reglas institucionales y gates ya validados."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-2: tema, semana y producto solicitado.",
    "Confirmar si hay rúbrica específica para profundidad argumentativa.",
    "Confirmar estilo de citación obligatorio institucional (supuesto: no confirmado).",
    "Confirmar nombre final del .bib canónico de asignatura tras resolver token Slug.",
    "Confirmar si filosofia-del-derecho-clean.bib aplica a actividad-2 o solo a semana temática distinta."
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
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos.",
      "Asegurar coherencia entre consigna, desarrollo y cierre argumentativo.",
      "Garantizar trazabilidad editorial y bibliográfica en cada actividad."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales y trazables.",
      "Cierre con criterio jurídico propio.",
      "Marcado explícito de supuestos."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/fuentes -> análisis -> conclusión.",
      "Afirmación jurídica -> respaldo verificable -> interpretación propia.",
      "Consigna local -> adecuación de formato -> verificación final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ejes editoriales troncales",
        "Normalización de salidas",
        "Trazabilidad cita-bibliografía",
        "Integridad académica",
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
          "justification": "Define tono, propósito y estándar común de entrega."
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
          "justification": "Permite verificar respaldo de afirmaciones."
        },
        {
          "source": "Ejes editoriales troncales",
          "target": "Actividad 2",
          "kind": "develops",
          "justification": "Son patrones reutilizables entre nodos hermanos."
        }
      ],
      "evidence": [
        "README fija identidad UnADM e integridad académica.",
        "Programa analítico define propósito y ejes de trabajo transferibles.",
        "Regla histórica validada: bloquear propagación sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 42: refuerzo lateral aplicado por analogía controlada.",
      "Se preservaron reglas útiles previas sin eliminación.",
      "Se removió duplicación textual y se mantuvo compresión lossless por unión-dedupe.",
      "Se mantuvo carácter provisional de datos no verificados con marcado de supuesto."
    ]
  }
}