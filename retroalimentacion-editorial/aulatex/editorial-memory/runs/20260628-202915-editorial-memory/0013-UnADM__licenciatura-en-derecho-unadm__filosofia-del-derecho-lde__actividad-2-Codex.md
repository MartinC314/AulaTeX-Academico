{
  "summary": [
    "Se consolida actividad-2 con transferencia lateral controlada desde actividad-1.",
    "Se preservan reglas válidas por unión y deduplicación sin recorte.",
    "Se refuerzan ejes troncales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se mantiene normalización obligatoria antes de propagación recursiva.",
    "Se evita copiar contenidos exclusivos del hermano; solo patrones reutilizables."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular actividad-2 a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como [supuesto] todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Conservar cierre con criterio jurídico propio."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en: conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Alinear el formato al producto pedido en la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Diferenciar postura propia, cita textual y paráfrasis."
  ],
  "activity_rules": [
    "Ajustar actividad-2 solo a instrucción docente disponible.",
    "No asumir tema, semana o formato sin evidencia local.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Mantener integridad académica en todo el producto."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas heredadas antes de reutilizarlas.",
    "Confirmar que cada afirmación sustantiva tenga respaldo o marca de [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No eliminar reglas útiles previas; aplicar unión-dedupe lossless."
  ],
  "latex_rules": [
    "Usar codificación correcta para español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves ya citadas.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Verificar nombres canónicos de archivos por caracteres anómalos en rutas."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y malla curricular como base contextual.",
    "Registrar fuentes específicas de actividad en el .bib canónico de la asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "[supuesto] filosofia-del-derecho-clean.bib es temático y no sustituye automáticamente al .bib canónico."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir solo patrones reutilizables entre hermanos.",
    "Evitar traspasar conclusiones o bibliografía exclusiva de una actividad a otra.",
    "Registrar herencias provisionales como antecedente histórico, no como verdad final.",
    "Si falta consigna local, propagar plantilla base y preguntas abiertas."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-2 (tema, semana y producto).",
    "Confirmar rúbrica específica para ajustar profundidad argumentativa.",
    "Confirmar estilo de citación obligatorio institucional. [supuesto: no confirmado]",
    "Confirmar nombre canónico final del .bib de asignatura.",
    "Confirmar si actividad-2 requiere reporte, presentación u otro formato principal."
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
      "Problema jurídico/social relevante.",
      "Conceptos y normas con respaldo.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir la planeación semanal en productos académicos sólidos y trazables.",
      "Garantizar consistencia institucional, metodológica y técnica en LaTeX."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales y trazables.",
      "Marcado explícito de [supuesto].",
      "Cierre con criterio jurídico propio."
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
        "Normalización estructurada",
        "Trazabilidad cita-bibliografía",
        "Integridad académica"
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
          "justification": "Define tono, propósito y criterio de cierre."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin JSON válido no hay transferencia segura."
        },
        {
          "source": "Trazabilidad cita-bibliografía",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Permite verificar respaldo de cada afirmación."
        },
        {
          "source": "Ejes editoriales troncales",
          "target": "Actividad-2",
          "kind": "develops",
          "justification": "Patrón reutilizable entre nodos hermanos."
        }
      ],
      "evidence": [
        "README fija identidad UnADM y pauta editorial.",
        "Programa analítico define propósito y ejes de trabajo.",
        "Regla vigente: bloquear salidas no parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: se refuerza transferencia lateral por analogía controlada.",
      "Se deduplican reglas repetidas y se preserva cobertura útil.",
      "Se mantiene alerta sobre fuentes heredadas provisionales.",
      "Se consolida política de no copiar contenido exclusivo entre hermanos."
    ]
  }
}