{
  "summary": [
    "Se refuerza memoria de actividad-2 con transferencia lateral controlada desde actividad-1.",
    "Se conserva todo patrón válido institucional, estructural y de calidad sin recorte.",
    "Se deduplica en modo lossless y se eliminan solo redundancias literales.",
    "Se mantiene carácter provisional de fuentes heredadas no verificadas localmente.",
    "Se preserva regla crítica: no propagar salidas no parseables y normalizar antes de reutilizar."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y propósito.",
    "Vincular actividad-2 a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Mantener enfoque académico-jurídico con transferencia a práctica profesional."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear formato final al producto solicitado por la planeación semanal.",
    "Diferenciar con claridad postura propia, cita textual y paráfrasis.",
    "Cerrar con conclusión jurídica transferible a práctica profesional."
  ],
  "activity_rules": [
    "Ajustar actividad-2 a la instrucción docente disponible.",
    "No asumir tema, semana o formato sin evidencia local.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Evitar entregas solo descriptivas; incluir postura argumentada del estudiante.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Usar fuentes de hermenéutica o argumentación solo si la consigna lo exige."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas heredadas antes de reutilizarlas.",
    "Confirmar que cada afirmación sustantiva tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No eliminar reglas útiles previas; aplicar unión-deduplicación lossless."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre claves citadas en .tex y entradas .bib.",
    "No renombrar claves bibliográficas ya usadas sin migración completa.",
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y rutas.",
    "Corregir caracteres anómalos en nombres de archivo antes de compilar.",
    "Compilar sin errores críticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y malla curricular para contexto.",
    "Agregar fuentes específicas de actividad en el .bib canónico de asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Tratar filosofia-del-derecho-clean.bib como complemento temático [supuesto], no sustitución automática."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir solo patrones reutilizables; no copiar conclusiones ni redacción literal.",
    "Evitar regresiones frente a reglas institucionales ya validadas.",
    "Cuando falte consigna local, propagar estructura base y preguntas abiertas.",
    "Mantener registro de herencia provisional de entradas no estructuradas.",
    "Aplicar analogía controlada: conservar esqueleto editorial y adaptar contenido local."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-2: tema, semana y producto.",
    "Confirmar plantilla obligatoria de secciones definida por docente.",
    "Confirmar estilo de citación obligatorio institucional [supuesto: no confirmado].",
    "Confirmar nombre canónico final del .bib de asignatura por token Slug.",
    "Confirmar si actividad-2 reutiliza bibliografía existente o requiere corpus propio."
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
        "Asignatura: Filosofía del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Conceptos y fuentes pertinentes.",
      "Producto conforme a planeación.",
      "Análisis propio y postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos trazables.",
      "Asegurar fundamento jurídico, evidencia y criterio propio.",
      "Garantizar calidad formal y verificabilidad bibliográfica."
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
        "Trazabilidad cita-bibliografía",
        "Integridad académica",
        "Ejes editoriales troncales",
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
          "justification": "Define tono, formato y finalidad académica común."
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
          "justification": "Son patrones reutilizables entre nodos hermanos."
        }
      ],
      "evidence": [
        "README fija identidad UnADM, integridad académica y conclusión jurídica.",
        "Programa analítico fija propósito y ejes de trabajo transferibles.",
        "Regla heredada vigente: bloquear propagación sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 12: consolidación por analogía controlada entre hermanos.",
      "Se preservaron reglas útiles previas sin eliminación.",
      "Se removieron duplicados literales y se mantuvo compresión lossless.",
      "Se reforzó separación entre patrones transferibles y contenido específico.",
      "Se mantuvo etiqueta de supuestos para vacíos de consigna local."
    ]
  }
}