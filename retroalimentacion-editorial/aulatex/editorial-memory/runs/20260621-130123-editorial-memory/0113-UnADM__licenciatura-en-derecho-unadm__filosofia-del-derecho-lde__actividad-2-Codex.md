{
  "summary": [
    "Memoria de actividad-2 consolidada con transferencia lateral controlada desde actividad-1.",
    "Se preservan reglas válidas previas y se deduplican sin recorte semántico.",
    "Se refuerzan ejes troncales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se mantiene normalización obligatoria antes de propagación recursiva.",
    "Se evita traslado de conclusiones o bibliografía exclusiva del hermano."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Mantener integridad académica con citas verificables."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el contenido al producto solicitado por la planeación semanal.",
    "Diferenciar postura propia, cita textual y paráfrasis.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Ajustar actividad-2 a la instrucción docente disponible.",
    "No asumir tema, semana o formato sin evidencia local.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas heredadas antes de reutilizarlas.",
    "Confirmar que cada afirmación sustantiva tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No eliminar reglas útiles previas; solo unir y deduplicar."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener compatibilidad entre claves citadas en .tex y entradas .bib.",
    "No renombrar claves bibliográficas ya usadas sin justificación editorial.",
    "Evitar comandos no estándar sin justificación.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir caracteres anómalos en rutas o nombres de archivo antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y malla curricular como base de contexto.",
    "Registrar fuentes específicas de actividad en el .bib canónico de la asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Usar filosofia-del-derecho-clean.bib solo si la consigna coincide con su tema [supuesto]."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir solo patrones reutilizables; no copiar redacción literal entre hermanos.",
    "Mantener reglas institucionales validadas sin regresión.",
    "Aplicar compresión lossless por unión y deduplicación.",
    "Cuando falte consigna local, propagar estructura base y abrir preguntas."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-2: tema, semana y producto.",
    "Confirmar plantilla obligatoria de secciones definida por docente.",
    "Confirmar estilo de citación obligatorio institucional.",
    "Confirmar nombre canónico final del .bib de asignatura.",
    "Confirmar si filosofia-del-derecho-clean.bib complementa o no el .bib canónico para actividad-2 [supuesto]."
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
        "Integridad académica y citas verificables.",
        "Carpeta de asignatura como entrada canónica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos.",
        "Asignatura: Filosofía del Derecho."
      ]
    },
    "essence": [
      "Problema jurídico o social que activa la asignatura.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeación.",
      "Análisis propio y postura académica.",
      "Conclusión transferible a la práctica jurídica."
    ],
    "reason_for_being": [
      "Transformar la planeación semanal en productos académicos trazables y útiles para práctica profesional.",
      "Estandarizar calidad editorial sin perder adaptación a la consigna local.",
      "Asegurar transferencia lateral robusta entre actividades hermanas."
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
      "Afirmación jurídica -> respaldo verificable -> interpretación propia.",
      "Consigna local -> adecuación de formato -> verificación final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalización de salidas",
        "Trazabilidad cita-bibliografía",
        "Integridad académica",
        "Transferencia lateral controlada",
        "Ejes editoriales troncales"
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
          "justification": "Define tono, formato y propósito común."
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
        "README fija identidad UnADM, integridad académica y conclusión jurídica.",
        "Programa analítico define propósito y ejes de trabajo transferibles.",
        "Regla histórica válida: bloquear propagación sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 7: se refuerza transferencia por analogía controlada entre hermanos.",
      "Ciclo 7: se consolidan reglas de calidad sin eliminar reglas útiles previas.",
      "Ciclo 7: se depuran duplicados y se mantienen supuestos explícitos donde falta dato local."
    ]
  }
}