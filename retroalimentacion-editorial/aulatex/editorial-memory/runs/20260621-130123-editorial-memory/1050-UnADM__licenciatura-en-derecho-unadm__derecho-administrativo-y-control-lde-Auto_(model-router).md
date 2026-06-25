{
  "summary": [
    "Se consolida memoria editorial de materia para Derecho administrativo y control.",
    "Se aplica compresión lossless por unión y deduplicación.",
    "Se preserva identidad UnADM y enfoque de Licenciatura en Derecho.",
    "Se mantiene alineación local: semestre 6, bloque 1, obligatoria, 8 créditos.",
    "Se refuerzan ejes transversales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se reutilizan solo abstracciones editoriales estables desde Filosofía del Derecho.",
    "No se trasladan contenidos doctrinales de Filosofía del Derecho sin verificación local.",
    "Se conserva alerta por salidas no JSON parseables desde fuentes provisionales.",
    "Se prioriza normalización estructurada antes de propagación recursiva.",
    "Se preserva control de consistencia entre README, programa analítico, LaTeX y .bib."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en portada, metadatos y redacción académica.",
    "Usar nombre exacto de materia: Derecho administrativo y control.",
    "Conservar enfoque de Licenciatura en Derecho en todos los entregables.",
    "Alinear la materia con semestre 6, bloque 1, obligatoria, 8 créditos.",
    "Usar la malla curricular local como fuente de ubicación curricular.",
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Marcar como [supuesto] todo dato no visible en la consigna local.",
    "Declarar cuando una regla provenga de fuente provisional.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Fuente provisional: Codex desde ingeniería en sistemas computacionales.",
    "Fuente provisional: GPT-Pro desde Actividad 1."
  ],
  "structure_rules": [
    "Organizar cada producto con problema, conceptos, fuentes, análisis propio y conclusión jurídica.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear entregables con la planeación semanal y el programa analítico local.",
    "Explicitar el producto solicitado antes del desarrollo.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener consistencia entre README, plantilla .tex y archivo .bib.",
    "Nombrar archivos con slug derecho-administrativo-y-control cuando aplique.",
    "Corregir artefactos de estructura en README antes de publicar índices.",
    "Resolver tokens PowerShell sin expandir en README y programa analítico por el slug literal. [supuesto]",
    "Corregir nombres de archivo con caracteres espurios o saltos de línea en README. [supuesto]"
  ],
  "activity_rules": [
    "Identificar si el producto es reporte, presentación o visual.",
    "Vincular cada actividad con control administrativo y práctica profesional.",
    "Incluir postura académica propia en cada actividad.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Formular criterio jurídico transferible a la práctica profesional.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No omitir conclusión final orientada a aplicación jurídica.",
    "Separar reglas editoriales generales de contenidos sustantivos heredados de otras materias.",
    "No asumir que fuentes de otra materia correspondan a esta asignatura."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar memoria aguas abajo.",
    "Detener propagación si hay respuesta no estructurada o campos críticos vacíos.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de [supuesto].",
    "Verificar integridad académica con citas verificables y sin fuentes inventadas.",
    "Confirmar trazabilidad entre afirmaciones y bibliografía local.",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Validar que README y programa no conserven placeholders ni rutas corruptas.",
    "Revisar que reglas heredadas no contradigan el programa analítico local.",
    "Verificar que el producto corresponda a la consigna de actividad.",
    "Revisar respuestas no estructuradas antes de reutilizarlas."
  ],
  "latex_rules": [
    "Mantener plantilla LaTeX en español.",
    "Mantener formato letterpaper según archivo base.",
    "Usar codificación y acentos correctos en .tex y .bib.",
    "Completar metadatos institucionales y de curso antes de compilar.",
    "Conservar tabla de datos académicos del estudiante y docente en portada.",
    "Asegurar coherencia entre \\documenttitle, \\documentsubtitle y actividad real.",
    "Reemplazar Actividad X por número y nombre real de la actividad.",
    "Mantener coursecode LDE-S6B1 salvo evidencia institucional distinta.",
    "Sustituir Nombre por definir por el nombre oficial de la figura docente antes de entregar.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) antes de publicar o compilar."
  ],
  "bibliography_rules": [
    "Registrar fuentes de cada actividad en derecho-administrativo-y-control.bib.",
    "Priorizar fuentes institucionales UnADM y documentos curriculares locales.",
    "Conservar entradas base: unadmSitioWeb y unadmMallaDerecho2024.",
    "Usar la malla curricular local como fuente de ubicación curricular.",
    "Agregar fuentes específicas solo si fueron consultadas o proporcionadas.",
    "No inventar fuentes para llenar bibliografía.",
    "No agregar referencias sin evidencia documental.",
    "Usar solo obras realmente consultables.",
    "Conservar metadatos mínimos: autor, título, año, medio o URL.",
    "Incluir nota de consulta cuando aplique.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Validar correspondencia entre citas en texto y entradas .bib."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Propagar a laterales solo reglas editoriales compartibles.",
    "No propagar contenido específico de actividad a laterales.",
    "No trasladar doctrina de Filosofía del Derecho sin verificación local.",
    "Aplicar normalización manual cuando la fuente sea provisional.",
    "Mantener estrategia union-dedupe lossless en fusiones futuras.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Preservar alerta institucional sobre respuestas no estructuradas en niveles superiores.",
    "Marcar conflictos de nomenclatura entre rutas antes de consolidar. [supuesto]",
    "Ciclo 1 necesita normalización manual si se reutiliza."
  ],
  "open_questions": [
    "Definir fuente definitiva para reemplazar referencias provisionales Codex y GPT-Pro.",
    "Confirmar nombre oficial de la figura docente en plantilla.",
    "Validar si existe formato institucional obligatorio de citas para la Licenciatura en Derecho.",
    "Confirmar convención final del archivo de referencias en la materia.",
    "Confirmar si el archivo de referencias debe llamarse referencias-derecho-administrativo-y-control.",
    "Verificar si el año de consulta del sitio institucional UnADM debe mantenerse en 2026.",
    "Confirmar si los tokens PowerShell sin expandir son artefactos de generación. [supuesto]",
    "Corregir posibles artefactos de ruta o nombre en README. [supuesto]",
    "Confirmar fuentes obligatorias por actividad.",
    "Confirmar rúbricas locales de evaluación por actividad."
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
        "No invención de fuentes.",
        "Supuestos marcados de forma visible.",
        "Normalización estructurada previa a propagación.",
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
      "Problema jurídico delimitado.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Control administrativo.",
      "Conclusión transferible a la práctica jurídica.",
      "Normalización estructurada.",
      "Coherencia documental entre README, LaTeX y .bib."
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
      "Transformar la planeación semanal en reportes, presentaciones y productos visuales.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Vincular el aprendizaje con control administrativo y práctica profesional.",
      "Garantizar trazabilidad de fuentes y consistencia editorial local.",
      "Proteger la memoria académica contra propagaciones no estructuradas."
    ],
    "style_markers": [
      "Encuadre breve antes del desarrollo.",
      "Objetivo explícito por actividad.",
      "Secciones limpias y funcionales.",
      "Citas trazables y verificables.",
      "Conclusión práctica obligatoria.",
      "Marcado explícito de supuestos.",
      "Nombre de materia exacto.",
      "Tono institucional UnADM.",
      "No traslado acrítico de contenidos externos.",
      "Corrección preventiva de placeholders y rutas corruptas."
    ],
    "argumentative_patterns": [
      "Plantear problema jurídico o social.",
      "Delimitar objetivo de la actividad.",
      "Definir conceptos clave.",
      "Establecer marco normativo o doctrinal verificable.",
      "Relacionar evidencia con el problema.",
      "Desarrollar postura propia sustentada.",
      "Contrastar descripción con criterio jurídico.",
      "Vincular análisis con control administrativo.",
      "Cerrar con conclusión aplicable a la práctica profesional.",
      "Verificar coherencia entre pregunta guía, desarrollo y conclusión."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Licenciatura en Derecho",
        "Derecho administrativo y control",
        "Semestre 6 bloque 1",
        "Malla curricular de Derecho",
        "Programa analítico local",
        "Problema jurídico",
        "Control administrativo",
        "Marco normativo",
        "Marco doctrinal",
        "Evidencia verificable",
        "Integridad académica",
        "Análisis propio",
        "Postura académica",
        "Conclusión jurídica transferible",
        "Práctica profesional",
        "Producto solicitado",
        "Planeación semanal",
        "Normalización estructurada",
        "JSON parseable",
        "README local",
        "Plantilla LaTeX",
        "Archivo BibTeX local",
        "Fuentes provisionales",
        "Supuestos marcados"
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
          "justification": "La identidad institucional exige rigor, trazabilidad y citas verificables."
        },
        {
          "source": "Malla curricular de Derecho",
          "target": "Semestre 6 bloque 1",
          "kind": "supports",
          "justification": "El README local usa la malla como fuente de ubicación curricular."
        },
        {
          "source": "Programa analítico local",
          "target": "Producto solicitado",
          "kind": "develops",
          "justification": "El programa orienta reportes, presentaciones y productos visuales."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis requiere un problema delimitado para evitar resumen descriptivo."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión práctica debe sostenerse en fuentes jurídicas verificables."
        },
        {
          "source": "Marco doctrinal",
          "target": "Postura académica",
          "kind": "supports",
          "justification": "La doctrina permite argumentar con criterio y no solo describir."
        },
        {
          "source": "Control administrativo",
          "target": "Práctica profesional",
          "kind": "develops",
          "justification": "La materia exige aplicación al ámbito administrativo y sus mecanismos de control."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Las afirmaciones deben tener respaldo documental o marca de supuesto."
        },
        {
          "source": "Archivo BibTeX local",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "El .bib local concentra las fuentes base y específicas de actividad."
        },
        {
          "source": "README local",
          "target": "Plantilla LaTeX",
          "kind": "supports",
          "justification": "Los nombres y rutas del README deben coincidir con los artefactos compilables."
        },
        {
          "source": "Normalización estructurada",
          "target": "JSON parseable",
          "kind": "depends_on",
          "justification": "La propagación recursiva requiere estructura válida y completa."
        },
        {
          "source": "Fuentes provisionales",
          "target": "Supuestos marcados",
          "kind": "depends_on",
          "justification": "Toda procedencia no verificada debe declararse antes de reutilizarse."
        },
        {
          "source": "Filosofía del Derecho",
          "target": "Derecho administrativo y control",
          "kind": "contrasts",
          "justification": "La relación transversal permite reglas editoriales comunes, no doctrina específica no verificada."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 6, bloque 1, obligatoria, 8 créditos.",
        "README local: fuente curricular UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: integridad académica, citas verificables y conclusión jurídica con criterio propio.",
        "Programa analítico local: claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: reportes, presentaciones y productos visuales.",
        "Programa analítico local: problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
        "Bibliografía local: unadmSitioWeb.",
        "Bibliografía local: unadmMallaDerecho2024.",
        "Plantilla LaTeX local: documenttitle de plantilla base.",
        "Plantilla LaTeX local: documentsubtitle con Actividad X pendiente.",
        "Plantilla LaTeX local: coursecode LDE-S6B1.",
        "Plantilla LaTeX local: figura docente pendiente.",
        "Memoria institucional heredada: salida no JSON parseable requiere revisión.",
        "Memoria transversal: no inventar fuentes y validar citas contra .bib."
      ]
    },
    "reinforcement_log": [
      "Ciclo 21 consolida reglas locales con transferencia transversal conservadora.",
      "Se deduplican reglas repetidas sin eliminar contenido útil.",
      "Se conserva encuadre curricular local frente al origen de Filosofía del Derecho.",
      "Se refuerza la regla de no trasladar doctrina no verificada entre materias.",
      "Se normaliza el patrón problema-conceptos-evidencia-análisis-conclusión.",
      "Se fortalece control de calidad para JSON, citas, placeholders y rutas.",
      "Se preservan fuentes locales verificables: unadmSitioWeb y unadmMallaDerecho2024.",
      "Se mantienen abiertas dudas de docente, formato de citas y referencias locales."
    ]
  }
}