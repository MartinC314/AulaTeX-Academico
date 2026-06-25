{
  "summary": [
    "Se consolida memoria de materia para Derecho administrativo y control.",
    "Se sincronizan abstracciones transversales desde Filosofía del Derecho.",
    "Se preserva identidad UnADM y enfoque de Licenciatura en Derecho.",
    "Se mantiene alineación local: semestre 6, bloque 1, obligatoria, 8 créditos.",
    "Se refuerzan ejes: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se conserva alerta por salidas no JSON parseables.",
    "Se aplica compresión union-dedupe sin regresión.",
    "No se trasladan doctrinas ni citas específicas de Filosofía del Derecho."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en portada, metadatos y redacción académica.",
    "Usar nombre exacto de materia: Derecho administrativo y control.",
    "Conservar enfoque de Licenciatura en Derecho.",
    "Ubicar la materia en semestre 6, bloque 1, obligatoria, 8 créditos.",
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Usar la malla curricular local como fuente de ubicación curricular.",
    "Marcar como [supuesto] todo dato no visible en consigna local.",
    "Declarar como provisional toda regla heredada no verificada.",
    "Fuente provisional: Codex desde ingeniería-en-sistemas-computacionales. [supuesto]",
    "Fuente provisional: GPT-Pro desde Actividad 1. [supuesto]",
    "Respetar el programa analítico local sobre cualquier herencia transversal."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar cada producto con problema, conceptos, fuentes, análisis propio y conclusión jurídica.",
    "Incluir marco normativo o doctrinal cuando la consigna lo requiera.",
    "Alinear entregables a la planeación semanal y al programa analítico local.",
    "Explicitar el producto solicitado: reporte, presentación o visual.",
    "Cerrar con conclusión transferible a la práctica jurídica.",
    "Mantener consistencia entre README, plantilla .tex y archivo .bib.",
    "Nombrar archivos con slug derecho-administrativo-y-control cuando aplique.",
    "Corregir artefactos de estructura en README antes de publicar índices.",
    "Resolver tokens PowerShell sin expandir por el slug literal. [supuesto]",
    "Corregir nombres con saltos de línea o caracteres espurios en README."
  ],
  "activity_rules": [
    "Incluir postura académica propia en cada actividad.",
    "Evitar entregas solo descriptivas.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Vincular el tema con control administrativo y práctica profesional.",
    "Formular criterio jurídico transferible.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Confirmar que el producto corresponda a la consigna real.",
    "Separar reglas editoriales generales de contenidos sustantivos heredados.",
    "No asumir fuentes de otra materia como fuentes locales.",
    "No omitir conclusión final orientada a aplicación jurídica."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de aplicar aguas abajo.",
    "Detener propagación si hay campos críticos vacíos.",
    "Revisar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de [supuesto].",
    "Verificar integridad académica con citas verificables.",
    "Bloquear fuentes inventadas.",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Confirmar trazabilidad entre afirmaciones y bibliografía local.",
    "Validar que README y programa no conserven placeholders ni rutas corruptas.",
    "Revisar que reglas heredadas no contradigan el programa analítico local.",
    "Evitar regresiones respecto de reglas útiles previas."
  ],
  "latex_rules": [
    "Mantener plantilla LaTeX en español.",
    "Mantener formato letterpaper según archivo base.",
    "Completar metadatos institucionales y de curso antes de compilar.",
    "Conservar tabla de datos académicos del estudiante y docente en portada.",
    "Asegurar coherencia entre documenttitle, documentsubtitle y actividad real.",
    "Reemplazar Actividad X por número y nombre real.",
    "Mantener coursecode LDE-S6B1 salvo evidencia institucional distinta.",
    "Sustituir Nombre por definir por figura docente oficial antes de entregar.",
    "Usar codificación y acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico."
  ],
  "bibliography_rules": [
    "Registrar fuentes de cada actividad en derecho-administrativo-y-control.bib.",
    "Priorizar fuentes institucionales UnADM y documentos curriculares locales.",
    "Conservar entradas base: unadmSitioWeb y unadmMallaDerecho2024.",
    "Usar malla curricular local como fuente de ubicación curricular.",
    "Agregar fuentes específicas solo si fueron consultadas o proporcionadas.",
    "No inventar fuentes para llenar bibliografía.",
    "Conservar metadatos mínimos: autor, título, año, medio y URL o archivo.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Confirmar formato institucional de citas antes de normalizar estilo.",
    "No trasladar referencias doctrinales de Filosofía del Derecho sin verificación local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Propagar a laterales solo reglas editoriales compartibles.",
    "No propagar contenido específico de actividad a laterales.",
    "No trasladar doctrina local entre materias no equivalentes.",
    "Aplicar normalización manual cuando la fuente sea provisional.",
    "Mantener estrategia union-dedupe lossless en fusiones futuras.",
    "Preservar alerta institucional sobre respuestas no estructuradas.",
    "Marcar conflictos de nomenclatura entre rutas antes de consolidar. [supuesto]",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Priorizar contexto local de Derecho administrativo y control."
  ],
  "open_questions": [
    "Definir fuente definitiva para reemplazar referencias provisionales Codex y GPT-Pro.",
    "Confirmar nombre oficial de la figura docente.",
    "Confirmar formato institucional obligatorio de citas.",
    "Confirmar convención final del archivo de referencias.",
    "Verificar si el año de consulta del sitio UnADM debe mantenerse en 2026.",
    "Confirmar si tokens PowerShell en README y programa son artefactos de generación. [supuesto]",
    "Corregir artefactos de ruta o nombre en estructura del README. [supuesto]",
    "Confirmar fuentes obligatorias por actividad.",
    "Confirmar rúbricas específicas antes de ajustar profundidad argumentativa.",
    "Confirmar tipos de producto habilitados por actividad."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Institucional sin rigidez innecesaria.",
        "Aplicado a la práctica profesional.",
        "Conservador ante fuentes no verificadas."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Normalización estructurada antes de propagación.",
        "No invención de fuentes.",
        "Supuestos marcados de forma visible.",
        "Carpeta de materia como entrada canónica.",
        "Respeto del programa analítico local.",
        "Consistencia entre README, LaTeX y bibliografía."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho administrativo y control.",
        "Semestre 6, bloque 1, obligatoria, 8 créditos.",
        "Coursecode local: LDE-S6B1.",
        "Fuente curricular local: malla-curricular-derecho-unadm.pdf.",
        "Marco local regido por README y programa analítico."
      ]
    },
    "essence": [
      "Identidad UnADM.",
      "Integridad académica.",
      "Problema jurídico o social.",
      "Conceptos, normas y doctrina pertinentes.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Control administrativo.",
      "Conclusión transferible a la práctica jurídica.",
      "Normalización estructurada."
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, fundamento jurídico y transferencia profesional.",
      "Transformar la planeación semanal en entregables verificables.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Vincular la materia con control administrativo y práctica profesional.",
      "Sostener una memoria editorial reutilizable sin perder contexto local."
    ],
    "style_markers": [
      "Abrir con problema delimitado.",
      "Declarar objetivo puntual.",
      "Diferenciar descripción, análisis y postura.",
      "Citar fuentes verificables.",
      "Marcar supuestos explícitamente.",
      "Cerrar con criterio jurídico aplicable.",
      "Evitar doctrina heredada no verificada.",
      "Usar nombres canónicos de archivos y materia.",
      "Corregir placeholders antes de publicar."
    ],
    "argumentative_patterns": [
      "Problema jurídico -> conceptos -> marco normativo -> análisis propio -> conclusión.",
      "Consigna -> producto solicitado -> estructura de entrega -> verificación final.",
      "Afirmación -> fuente verificable -> interpretación -> criterio jurídico.",
      "Contexto administrativo -> mecanismo de control -> efecto jurídico -> aplicación profesional.",
      "Dato no visible -> marca [supuesto] -> pregunta abierta.",
      "Herencia transversal -> abstracción editorial -> validación local."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Licenciatura en Derecho",
        "Derecho administrativo y control",
        "Semestre 6 bloque 1",
        "Integridad académica",
        "Problema jurídico",
        "Marco normativo/doctrinal",
        "Fuentes verificables",
        "Análisis propio",
        "Conclusión transferible",
        "Control administrativo",
        "Práctica profesional",
        "Normalización estructurada",
        "JSON parseable",
        "README local",
        "Programa analítico local",
        "Archivo BibTeX local",
        "Malla curricular Derecho UnADM",
        "Plantilla LaTeX",
        "Supuesto editorial"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La identidad institucional exige rigor, trazabilidad y no invención de fuentes."
        },
        {
          "source": "Malla curricular Derecho UnADM",
          "target": "Semestre 6 bloque 1",
          "kind": "supports",
          "justification": "La ubicación curricular local se declara con fuente institucional."
        },
        {
          "source": "README local",
          "target": "Carpeta de materia como entrada canónica",
          "kind": "supports",
          "justification": "La pauta editorial local define la carpeta como punto de entrada."
        },
        {
          "source": "Programa analítico local",
          "target": "Ejes editoriales",
          "kind": "develops",
          "justification": "El programa fija problema, conceptos, fuentes, análisis propio y cierre."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis requiere un problema delimitado."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión práctica necesita fundamento jurídico verificable."
        },
        {
          "source": "Fuentes verificables",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Las citas trazables reducen afirmaciones sin respaldo."
        },
        {
          "source": "Control administrativo",
          "target": "Práctica profesional",
          "kind": "develops",
          "justification": "La materia debe conectar teoría jurídica con aplicación administrativa."
        },
        {
          "source": "Normalización estructurada",
          "target": "JSON parseable",
          "kind": "depends_on",
          "justification": "La propagación recursiva requiere salida estructurada válida."
        },
        {
          "source": "Archivo BibTeX local",
          "target": "Fuentes verificables",
          "kind": "supports",
          "justification": "El .bib local concentra las referencias consultadas de la materia."
        },
        {
          "source": "Plantilla LaTeX",
          "target": "Identidad UnADM",
          "kind": "supports",
          "justification": "Los metadatos y portada sostienen la identidad institucional."
        },
        {
          "source": "Supuesto editorial",
          "target": "Preguntas abiertas",
          "kind": "develops",
          "justification": "Todo dato no visible debe quedar pendiente de confirmación."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 6, bloque 1, obligatoria, 8 créditos.",
        "README local: fuente curricular malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: integridad académica, citas verificables y conclusión jurídica.",
        "README local: estructura contiene tokens sin expandir y nombres corruptos.",
        "Programa analítico local: claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: reportes, presentaciones y productos visuales.",
        "Programa analítico local: problema, conceptos, fuentes, análisis propio y cierre.",
        "derecho-administrativo-y-control.bib: entrada unadmSitioWeb.",
        "derecho-administrativo-y-control.bib: entrada unadmMallaDerecho2024.",
        "Plantilla LaTeX local: documenttitle base de la materia.",
        "Plantilla LaTeX local: documentsubtitle contiene Actividad X.",
        "Plantilla LaTeX local: coursecode LDE-S6B1.",
        "Plantilla LaTeX local: figura docente pendiente."
      ]
    },
    "reinforcement_log": [
      "Ciclo 19: se consolidó sincronización transversal conservadora.",
      "Ciclo 19: se deduplicaron variantes de reglas equivalentes.",
      "Ciclo 19: se preservó identidad local de Derecho administrativo y control.",
      "Ciclo 19: se evitaron citas doctrinales no verificadas del origen.",
      "Ciclo 19: se reforzó el gate de JSON parseable.",
      "Ciclo 19: se normalizó el grafo con relaciones permitidas.",
      "Ciclo 19: se mantuvo alerta por fuentes provisionales.",
      "Ciclo 19: se priorizó programa analítico local sobre herencia transversal.",
      "Ciclo 19: se conservaron preguntas abiertas operativas.",
      "Ciclo 19: se reforzó consistencia entre README, LaTeX y .bib."
    ]
  }
}