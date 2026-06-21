{
  "summary": [
    "Se consolida memoria de actividad-2 con transferencia lateral desde actividad-1 por unión y deduplicación lossless.",
    "Se preservan reglas válidas institucionales UnADM, estructura argumentativa y control de calidad sin regresión.",
    "Se refuerza regla de normalización obligatoria antes de propagación recursiva.",
    "Se mantiene separación entre patrones reutilizables y contenido específico de cada actividad.",
    "Se marca como supuesto todo dato no confirmado por consigna local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y cierre.",
    "Vincular actividad-2 a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
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
    "Ajustar actividad-2 a la instrucción docente disponible.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Diferenciar postura propia, cita textual y paráfrasis.",
    "No asumir tema, semana o formato sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas heredadas antes de reutilizarlas.",
    "Confirmar que cada afirmación sustantiva tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener compatibilidad entre claves de cita en .tex y entradas .bib.",
    "No renombrar claves bibliográficas ya citadas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Compilar sin errores críticos y sin referencias rotas."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y malla curricular de Derecho como base de contexto.",
    "Registrar fuentes específicas de actividad en el .bib canónico de la asignatura.",
    "No inventar referencias ni metadatos.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib es complemento temático y no reemplazo automático del .bib canónico."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir solo patrones reutilizables entre nodos hermanos.",
    "Evitar copiar conclusiones, redacción literal o bibliografía exclusiva de otra actividad.",
    "Mantener unión-dedupe lossless y evitar recorte semántico.",
    "Registrar normalización manual cuando reaparezcan salidas no estructuradas."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-2: tema, semana y producto.",
    "Confirmar plantilla obligatoria de secciones para actividad-2 según docente.",
    "Confirmar estilo de citación institucional obligatorio (supuesto: no confirmado).",
    "Confirmar nombre canónico final del archivo .bib de la asignatura.",
    "Confirmar si actividad-2 requiere bibliografía propia adicional."
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
      "Conceptos y fuentes pertinentes.",
      "Análisis propio con postura académica.",
      "Evidencia verificable.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos trazables.",
      "Asegurar fundamento jurídico y claridad argumentativa.",
      "Sostener transferencia profesional desde cada actividad."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales y trazables.",
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
          "justification": "Define marco común de tono, formato y finalidad."
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
          "target": "Actividad-2",
          "kind": "develops",
          "justification": "Son patrones reutilizables entre actividades hermanas."
        }
      ],
      "evidence": [
        "README fija identidad UnADM, integridad académica y conclusión jurídica.",
        "Programa analítico fija propósito y ejes transferibles.",
        "Regla vigente: bloquear propagación sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 64: se refuerza transferencia lateral por analogía controlada.",
      "Se eliminan duplicados semánticos y se preserva contenido útil previo.",
      "Se mantiene carácter provisional de fuentes heredadas no verificadas.",
      "Se evita trasladar contenido exclusivo de actividad-1 hacia actividad-2."
    ]
  }
}