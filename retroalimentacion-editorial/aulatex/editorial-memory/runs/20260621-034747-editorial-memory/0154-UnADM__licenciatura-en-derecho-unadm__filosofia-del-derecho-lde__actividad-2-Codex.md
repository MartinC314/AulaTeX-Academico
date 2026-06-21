{
  "summary": [
    "Se consolida actividad-2 con transferencia lateral desde actividad-1 sin copiar contenidos exclusivos.",
    "Se preservan reglas válidas previas y se aplica unión-deduplicación lossless.",
    "Se refuerzan ejes troncales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se mantiene normalización obligatoria de salidas no estructuradas antes de propagación recursiva.",
    "Se conserva carácter provisional de fuentes heredadas no verificadas y se exige verificación local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y cierre.",
    "Vincular actividad-2 a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el producto al formato solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Ajustar actividad-2 a la instrucción docente disponible.",
    "No asumir tema, semana o formato sin evidencia local.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Diferenciar postura propia, cita textual y paráfrasis.",
    "Evitar entregas solo descriptivas."
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
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener compatibilidad entre claves citadas en .tex y entradas .bib.",
    "No renombrar claves bibliográficas ya citadas sin justificación.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Confirmar nombres canónicos de archivos por caracteres anómalos en README."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y malla curricular como base de contexto.",
    "Registrar fuentes específicas de actividad en filosofia-del-derecho.bib (supuesto por Slug).",
    "Tratar filosofia-del-derecho-clean.bib como complemento temático, no reemplazo automático (supuesto).",
    "No inventar referencias ni metadatos bibliográficos.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Mantener trazabilidad completa entre cita en texto y referencia final."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir solo patrones reutilizables entre hermanos.",
    "Evitar copiar redacción literal, conclusiones específicas y bibliografía exclusiva del nodo hermano.",
    "Conservar sin regresión reglas institucionales ya validadas.",
    "Aplicar normalización manual cuando reaparezcan entradas no estructuradas."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-2: tema, semana y producto.",
    "Confirmar plantilla obligatoria de secciones definida por docente.",
    "Confirmar estilo de citación institucional obligatorio (supuesto: no confirmado).",
    "Confirmar si actividad-2 requiere .bib propio o reutiliza el canónico de asignatura.",
    "Confirmar nombres finales de archivos LaTeX canónicos tras corregir tokens."
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
      "Problema jurídico o social como detonante.",
      "Conceptos y fuentes pertinentes con respaldo.",
      "Producto alineado a planeación.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica aplicable."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en entregables académicos sólidos.",
      "Garantizar fundamento jurídico, evidencia y transferencia profesional.",
      "Sostener coherencia editorial entre actividades hermanas sin pérdida de identidad."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales y trazables.",
      "Cierre con criterio jurídico propio.",
      "Marcado explícito de supuestos.",
      "Consistencia cita-bibliografía."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/fuentes -> análisis -> conclusión.",
      "Afirmación jurídica -> evidencia verificable -> interpretación propia.",
      "Consigna local -> adecuación de formato -> verificación final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ejes editoriales troncales",
        "Normalización de salidas",
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
          "justification": "Define tono, formato y finalidad común."
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
          "target": "Actividad-2",
          "kind": "develops",
          "justification": "Son patrones reutilizables entre nodos hermanos."
        }
      ],
      "evidence": [
        "README fija identidad UnADM e integridad académica.",
        "Programa analítico define propósito y ejes de trabajo.",
        "Regla histórica: bloquear propagación sin JSON parseable.",
        "Regla histórica: normalizar entradas no estructuradas antes de reutilizar."
      ]
    },
    "reinforcement_log": [
      "Ciclo 54: refuerzo lateral aplicado por analogía controlada.",
      "Se preservaron reglas válidas de actividad-1 y actividad-2 sin recorte.",
      "Se eliminaron duplicados semánticos sin pérdida de información normativa.",
      "Se mantuvo separación entre patrones reutilizables y contenido específico de hermano.",
      "Se añadieron supuestos explícitos donde faltan datos locales."
    ]
  }
}