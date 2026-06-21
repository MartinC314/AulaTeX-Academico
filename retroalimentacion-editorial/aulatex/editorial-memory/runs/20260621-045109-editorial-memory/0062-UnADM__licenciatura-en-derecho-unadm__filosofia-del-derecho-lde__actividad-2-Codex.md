{
  "summary": [
    "Se refuerza memoria de actividad-2 con transferencia lateral desde actividad-1 por patrones reutilizables.",
    "Se conserva identidad UnADM, ejes troncales y control de calidad sin recorte.",
    "Se mantiene compresión lossless por unión y deduplicación.",
    "Se evita transferir conclusiones o bibliografía exclusiva del hermano sin validación local.",
    "Se mantiene estatus provisional de fuentes heredadas no verificadas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y propósito.",
    "Vincular actividad-2 a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el producto al formato pedido por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a práctica profesional."
  ],
  "activity_rules": [
    "Ajustar actividad-2 a la instrucción docente disponible.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Diferenciar postura propia, cita textual y paráfrasis.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir tema, semana ni formato sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas heredadas antes de reutilizar.",
    "Confirmar respaldo o marca de supuesto en cada afirmación sustantiva.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No eliminar reglas útiles previas; solo unir y deduplicar."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en .tex y .bib.",
    "Mantener compatibilidad entre claves de cita del .tex y entradas .bib.",
    "No renombrar claves bibliográficas ya citadas sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir caracteres anómalos en rutas y nombres antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y malla curricular de Derecho como base.",
    "Agregar fuentes específicas de actividad en el .bib canónico de la asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib es temático y no reemplaza automáticamente al .bib canónico."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir solo patrones generales: identidad, estructura, calidad, conceptos y relaciones recurrentes.",
    "Evitar copiar redacción literal, conclusiones específicas o bibliografía exclusiva entre hermanos.",
    "Mantener normalización manual cuando reaparezcan entradas no estructuradas.",
    "Preservar reglas validadas sin regresión."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-2: tema, semana y producto.",
    "Confirmar plantilla obligatoria de secciones definida por docente.",
    "Confirmar estilo de citación obligatorio institucional. [supuesto: no confirmado]",
    "Confirmar nombre canónico final del .bib de asignatura.",
    "Confirmar si actividad-2 reutiliza bibliografía existente o requiere .bib propio."
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
      "Conceptos y marco normativo o doctrinal.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos trazables.",
      "Sostener argumentación jurídica con evidencia y criterio propio."
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
          "justification": "Define tono y finalidad académica común."
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
        "README fija identidad UnADM, integridad académica y cierre jurídico.",
        "Programa analítico fija propósito y ejes transferibles.",
        "Regla histórica vigente: bloquear propagación sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 62: refuerzo lateral aplicado por analogía controlada entre hermanos.",
      "Se consolidan reglas repetidas por deduplicación lossless.",
      "Se preserva todo patrón válido previo sin eliminar reglas útiles.",
      "Se agregan mejoras verificables: control de supuestos, token Slug, no-copia de contenido exclusivo."
    ]
  }
}