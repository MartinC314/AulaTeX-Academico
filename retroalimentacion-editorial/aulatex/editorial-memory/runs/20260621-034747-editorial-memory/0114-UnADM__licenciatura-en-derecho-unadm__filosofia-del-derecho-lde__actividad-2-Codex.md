{
  "summary": [
    "Se consolida actividad-2 con transferencia lateral desde actividad-1 por patrones reutilizables.",
    "Se preserva identidad UnADM, estructura troncal y controles de calidad sin regresión.",
    "Se aplica deduplicación lossless y se eliminan ambigüedades de redacción, no reglas útiles.",
    "Se mantiene carácter provisional de fuentes heredadas no verificadas.",
    "Se refuerza que no se copian conclusiones ni bibliografía exclusiva entre nodos hermanos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular actividad-2 a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como entrada canónica editorial.",
    "Marcar como supuesto todo dato no confirmado en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validación local.",
    "Mantener enfoque académico-jurídico con transferencia a práctica profesional."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear formato final al producto solicitado en la planeación semanal.",
    "Diferenciar explícitamente postura propia, cita y paráfrasis.",
    "Cerrar con conclusión jurídica transferible."
  ],
  "activity_rules": [
    "Ajustar actividad-2 a la instrucción docente disponible.",
    "No asumir tema, semana o formato sin evidencia local.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Usar fuentes de hermenéutica o argumentación solo si la consigna lo requiere."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Verificar que cada afirmación sustantiva tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No eliminar reglas útiles previas; solo unir y deduplicar."
  ],
  "latex_rules": [
    "Usar codificación correcta en español en .tex y .bib.",
    "Mantener claves BibTeX estables y compatibles entre .tex y .bib.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Verificar rutas y nombres de archivo antes de referenciar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: .bib canónico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y malla curricular como contexto base.",
    "Registrar fuentes específicas de actividad en el .bib canónico de la asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib es complemento temático y no reemplazo automático."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir entre hermanos solo patrones generales reutilizables.",
    "No propagar conclusiones específicas ni bibliografía exclusiva de otro hermano.",
    "Mantener normalización manual si reaparecen salidas no estructuradas.",
    "Evitar reglas especulativas como definitivas.",
    "Reforzar controles institucionales sin reducir especificidad local."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-2: tema, semana y producto.",
    "Confirmar rúbrica de evaluación específica para profundidad argumentativa.",
    "Confirmar si existe estilo de citación institucional obligatorio.",
    "Confirmar nombre canónico final del .bib de la asignatura.",
    "Confirmar si actividad-2 requiere reporte, presentación u otro formato principal.",
    "Supuesto: la metadata documental heredada de Actividad 1 no aplica automáticamente a Actividad 2."
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
      "Convertir la planeación semanal en productos académicos con fundamento jurídico y trazabilidad.",
      "Asegurar consistencia editorial entre actividades sin copiar contenido específico.",
      "Sostener memoria persistente por unión y deduplicación lossless."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales trazables.",
      "Marcado explícito de supuestos.",
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
          "source": "Identidad institucional UnADM",
          "target": "Ejes editoriales troncales",
          "kind": "supports",
          "justification": "Define tono, finalidad y marco común de entrega."
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
          "justification": "Permite verificar respaldo y evitar invenciones."
        },
        {
          "source": "Ejes editoriales troncales",
          "target": "Actividad-2",
          "kind": "develops",
          "justification": "Se reutilizan como base sin copiar contenido exclusivo de actividad-1."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad académica y conclusión jurídica.",
        "Programa analítico: propósito y ejes de trabajo transferibles.",
        "Regla histórica: bloquear propagación sin JSON parseable.",
        "Transferencia entre hermanos limitada a patrones reutilizables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 14: se refuerza transferencia lateral por analogía controlada.",
      "Ciclo 14: se elimina duplicidad semántica manteniendo cobertura completa.",
      "Ciclo 14: se preservan reglas útiles previas sin recorte destructivo.",
      "Ciclo 14: se mantienen supuestos abiertos donde faltan datos locales."
    ]
  }
}