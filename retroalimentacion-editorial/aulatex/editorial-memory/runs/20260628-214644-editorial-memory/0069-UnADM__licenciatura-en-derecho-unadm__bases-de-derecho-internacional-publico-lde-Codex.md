{
  "summary": [
    "Se sincroniza memoria transversal desde actividad de origen con estrategia conservadora.",
    "Se preserva identidad UnADM y contexto curricular local del destino.",
    "Se refuerza normalización estructurada obligatoria antes de propagación recursiva.",
    "Se consolidan ejes estables reutilizables: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se evita traslado de contenido temático específico de Filosofía del Derecho.",
    "Se detectan tokens sin expandir y cortes de texto en README y .tex del destino."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local de la materia en todos los entregables.",
    "Usar contexto curricular verificado del destino: semestre 4, bloque 1, obligatoria, 8 créditos.",
    "No mezclar metadatos curriculares entre origen y destino.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como procedencia provisional."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como entrada canónica.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Distinguir hechos, normas, argumentos y criterio propio.",
    "Evitar extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna vigente de actividad."
  ],
  "latex_rules": [
    "Reutilizar plantilla .tex local sin romper identidad institucional.",
    "Usar codificación y acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir nombres/rutas con caracteres anómalos antes de compilar.",
    "Revisar y cerrar correctamente entornos tabular del reporte base."
  ],
  "bibliography_rules": [
    "Registrar fuentes de actividad en el .bib local de la materia.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Validar que toda clave citada exista en el .bib local."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables en nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "No propagar redacción literal ni contenido temático específico del origen.",
    "Preservar reglas útiles previas sin regresión.",
    "Aplicar compresión lossless por unión y deduplicación.",
    "Mantener trazabilidad de incidencias de parseo en ciclos previos."
  ],
  "open_questions": [
    "Confirmar criterio editorial final de público/publico en nombre visible de la materia.",
    "Confirmar corrección definitiva de tokens $(@{...}.Slug) en README y programa analítico.",
    "Confirmar reparación completa del corte de entorno tabular en reporte .tex.",
    "Supuesto: la consigna local de cada actividad seguirá definiendo el tipo de entregable.",
    "Supuesto: bases-de-derecho-internacional-publico.bib es el archivo canónico definitivo."
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
        "Normalización estructurada obligatoria antes de propagación."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Bases de derecho internacional público.",
        "Semestre 4, bloque 1, obligatoria, 8 créditos."
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
      "Convertir planeación semanal en productos académicos con fundamento jurídico y trazabilidad editorial.",
      "Asegurar consistencia entre consigna, argumentación y evidencia."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Secciones funcionales sin redundancia.",
      "Supuestos etiquetados.",
      "Cierre con criterio jurídico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> norma/doctrina -> análisis -> conclusión.",
      "Afirmación -> evidencia -> interpretación -> postura propia.",
      "Consigna -> desarrollo alineado -> verificación final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Consigna de actividad",
        "Estructura argumentativa jurídica",
        "Evidencia verificable",
        "Conclusión transferible",
        "Normalización JSON",
        "Consistencia cita-bibliografía"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Consigna de actividad",
          "target": "Estructura argumentativa jurídica",
          "kind": "depends_on",
          "justification": "La forma del entregable depende del producto solicitado."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica exige respaldo documental."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia segura."
        },
        {
          "source": "Consistencia cita-bibliografía",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Evita afirmaciones sin fuente y referencias inválidas."
        }
      ],
      "evidence": [
        "README y programa analítico del destino.",
        "Archivo .bib local con claves institucionales.",
        "Historial de incidencias de salida no estructurada en ciclos previos."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin pérdida de contenido útil.",
      "Se reforzaron gates de parseo JSON y normalización previa.",
      "Se mantuvo separación entre identidad local y procedencia provisional.",
      "Se añadieron acciones concretas para tokens sin expandir y errores LaTeX locales."
    ]
  }
}