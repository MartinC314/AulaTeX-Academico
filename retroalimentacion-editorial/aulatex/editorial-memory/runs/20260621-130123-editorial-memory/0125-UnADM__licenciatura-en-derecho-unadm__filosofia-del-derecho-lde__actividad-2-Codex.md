{
  "summary": [
    "Se refuerza memoria de actividad-2 con transferencia lateral controlada desde actividad-1.",
    "Se conservan reglas válidas previas con unión y deduplicación lossless.",
    "Se mantiene normalización obligatoria antes de propagación recursiva.",
    "Se consolidan ejes editoriales troncales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se evita traslado de conclusiones o bibliografía exclusiva del nodo hermano."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Conservar integridad académica y citas verificables."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el desarrollo al producto solicitado por la planeación semanal.",
    "Diferenciar postura propia, cita textual y paráfrasis.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Ajustar actividad-2 a la instrucción docente disponible.",
    "No asumir tema, semana o formato sin evidencia local.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Mantener postura argumentada del estudiante."
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
    "No renombrar claves bibliográficas ya citadas sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir caracteres anómalos en rutas y nombres antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y malla curricular como base contextual.",
    "Registrar fuentes específicas de actividad en el .bib canónico de la asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Tratar filosofia-del-derecho-clean.bib como complemento temático bajo consigna [supuesto]."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir solo patrones reutilizables: identidad, estructura, calidad, conceptos y relaciones.",
    "No propagar redacción literal ni conclusiones específicas de nodos hermanos.",
    "Mantener etiqueta de herencia provisional cuando el origen no fue estructurado.",
    "Aplicar compresión por unión-dedupe lossless en cada ciclo.",
    "Evitar regresiones frente a reglas institucionales ya validadas."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-2: tema, semana y producto.",
    "Confirmar plantilla obligatoria de secciones definida por docente.",
    "Confirmar estilo de citación obligatorio institucional [supuesto: no confirmado].",
    "Confirmar nombre canónico final del .bib de asignatura por token Slug.",
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
      "Problema jurídico o social que activa la actividad.",
      "Conceptos y fuentes pertinentes con respaldo.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible.",
      "Normalización estructurada antes de propagación."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en producto académico verificable.",
      "Asegurar trazabilidad entre afirmaciones, citas y bibliografía.",
      "Preservar consistencia editorial entre nodos hermanos sin copiar contenido específico."
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
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/programa-analitico-filosofia-del-derecho.md",
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf"
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
          "justification": "Patrón reusable entre actividades hermanas."
        }
      ],
      "evidence": [
        "README fija identidad UnADM e integridad académica.",
        "Programa analítico define propósito y ejes de trabajo.",
        "Regla persistente: bloquear propagación sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 10: se refuerza transferencia lateral por analogía controlada.",
      "Ciclo 10: se preservan reglas útiles previas sin recorte.",
      "Ciclo 10: se mantiene carácter provisional de fuentes heredadas no verificadas.",
      "Ciclo 10: se evita copiar contenido exclusivo de actividad-1."
    ]
  }
}