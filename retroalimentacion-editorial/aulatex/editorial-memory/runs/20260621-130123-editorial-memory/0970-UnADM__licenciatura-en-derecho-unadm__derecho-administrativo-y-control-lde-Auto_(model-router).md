{
  "summary": [
    "Se consolida memoria transversal para Derecho administrativo y control.",
    "Se aplica compresión union-dedupe sin regresión.",
    "Se preserva identidad UnADM y enfoque de Licenciatura en Derecho.",
    "Se mantiene alineación curricular local: semestre 6, bloque 1, obligatoria, 8 créditos.",
    "Se reutilizan solo abstracciones editoriales estables desde Filosofía del Derecho.",
    "No se trasladan contenidos doctrinales de Filosofía del Derecho sin verificación local.",
    "Se refuerzan ejes comunes: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se conserva alerta institucional sobre salidas no JSON parseables.",
    "Se prioriza normalización estructurada antes de propagación recursiva.",
    "Se detectan artefactos locales en README y programa analítico que requieren corrección."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en portada, metadatos y redacción académica.",
    "Usar nombre exacto de materia: Derecho administrativo y control.",
    "Conservar enfoque de Licenciatura en Derecho en todos los entregables.",
    "Mantener encuadre curricular local: semestre 6, bloque 1, obligatoria, 8 créditos.",
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Marcar como [supuesto] todo dato no visible en la consigna local.",
    "Declarar cuando una regla provenga de fuente provisional.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Fuente provisional: Codex desde ingeniería-en-sistemas-computacionales.",
    "Fuente provisional: GPT-Pro desde Actividad 1.",
    "No transferir ubicación curricular de otra materia al destino.",
    "Citar la malla curricular local para ubicación curricular."
  ],
  "structure_rules": [
    "Organizar cada producto con problema, conceptos, normas, doctrina, análisis propio y conclusión jurídica.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear entregables a la planeación semanal y al programa analítico local.",
    "Explicitar el producto solicitado antes del desarrollo.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener consistencia entre README, plantilla tex y archivo bib.",
    "Corregir artefactos de estructura en README antes de publicar índices.",
    "Nombrar archivos con slug derecho-administrativo-y-control cuando aplique.",
    "Resolver tokens PowerShell sin expandir en README y programa analítico por el slug literal derecho-administrativo-y-control. [supuesto]",
    "Corregir nombres de archivo con caracteres espurios o saltos de línea en README. [supuesto]"
  ],
  "activity_rules": [
    "Cada actividad debe incluir postura académica propia.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Vincular el tema con control administrativo y práctica profesional.",
    "Formular criterio jurídico transferible a la práctica profesional.",
    "No omitir conclusión final orientada a aplicación jurídica.",
    "Identificar si el producto es reporte, presentación o visual.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Separar reglas editoriales generales de contenidos sustantivos heredados de otras materias.",
    "Confirmar que el producto corresponda a la consigna específica de la actividad.",
    "No asumir que fuentes de otra semana o materia aplican a una actividad local."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar respuesta no estructurada antes de aplicar aguas abajo.",
    "Validar estructura mínima completa antes de propagar.",
    "Detener propagación si hay campos críticos vacíos.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de [supuesto].",
    "Verificar integridad académica con citas verificables y sin fuentes inventadas.",
    "Confirmar trazabilidad entre afirmaciones y bibliografía local.",
    "Validar consistencia entre citas en texto y archivo bib local.",
    "Validar que README y programa no conserven placeholders ni rutas corruptas.",
    "Revisar que reglas heredadas no contradigan el programa analítico local.",
    "Revisar correspondencia del producto con la consigna de actividad.",
    "Corregir artefactos locales antes de publicar índices o plantillas."
  ],
  "latex_rules": [
    "Mantener plantilla LaTeX en español.",
    "Mantener formato letterpaper según archivo base.",
    "Usar codificación y acentos correctos en español en archivos tex y bib.",
    "Completar metadatos institucionales y de curso antes de compilar.",
    "Conservar tabla de datos académicos del estudiante y docente en portada.",
    "Asegurar coherencia entre título, subtítulo y actividad real.",
    "Reemplazar Actividad X por número y nombre real de la actividad.",
    "Mantener coursecode LDE-S6B1 salvo evidencia institucional distinta.",
    "Sustituir Nombre por definir por el nombre oficial de la figura docente antes de entregar.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico."
  ],
  "bibliography_rules": [
    "Registrar fuentes de cada actividad en derecho-administrativo-y-control.bib.",
    "Priorizar fuentes institucionales UnADM y documentos curriculares locales.",
    "Usar la malla curricular local como fuente de ubicación curricular.",
    "Conservar entradas base: unadmSitioWeb y unadmMallaDerecho2024.",
    "Agregar fuentes específicas solo si fueron consultadas o proporcionadas.",
    "No inventar fuentes para llenar bibliografía.",
    "Usar solo obras realmente consultables.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Incluir metadatos mínimos: autor, título, año, medio o URL y nota de consulta.",
    "Validar correspondencia entre citas en texto y entradas BibTeX.",
    "Confirmar convención final del archivo de referencias local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validación de JSON y estructura.",
    "Mantener estrategia de compresión union-dedupe lossless en fusiones futuras.",
    "Aplicar normalización manual cuando la fuente sea provisional.",
    "Preservar alerta institucional sobre respuestas no estructuradas en niveles superiores.",
    "Propagar a laterales solo reglas editoriales compartibles.",
    "No propagar contenido específico de actividad a laterales.",
    "No trasladar doctrina de Filosofía del Derecho sin verificación local.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Marcar conflictos de nomenclatura entre rutas antes de consolidar. [supuesto]",
    "Ciclo 1 necesita normalización manual si se reutiliza."
  ],
  "open_questions": [
    "Confirmar nombre oficial de la figura docente en plantilla.",
    "Confirmar si existe formato institucional obligatorio de citas para la Licenciatura en Derecho.",
    "Confirmar convención final del archivo de referencias en la materia.",
    "Verificar si el año de consulta del sitio institucional UnADM debe mantenerse en 2026.",
    "Confirmar si los tokens PowerShell sin expandir en README y programa son artefactos de generación. [supuesto]",
    "Corregir posibles artefactos de ruta o nombre en listado de estructura del README. [supuesto]",
    "Definir fuente definitiva para reemplazar referencias provisionales Codex y GPT-Pro.",
    "Confirmar fuentes obligatorias por unidad o semana antes de cada actividad.",
    "Confirmar producto exacto solicitado en cada actividad local.",
    "Confirmar rúbrica específica antes de ajustar profundidad argumentativa."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Institucional sin rigidez innecesaria.",
        "Aplicado a la práctica profesional."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Carpeta de materia como entrada canónica.",
        "Normalización estructurada antes de propagación.",
        "Supuestos marcados de forma visible."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Derecho administrativo y control.",
        "Semestre 6, bloque 1.",
        "Tipo obligatoria.",
        "8 créditos.",
        "Fuente curricular local: malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Identidad UnADM.",
      "Integridad académica.",
      "Problema jurídico o social.",
      "Conceptos jurídicos pertinentes.",
      "Normas y doctrina verificables.",
      "Control administrativo.",
      "Evidencia trazable.",
      "Análisis propio.",
      "Postura académica.",
      "Conclusión transferible.",
      "Práctica profesional.",
      "Normalización estructurada."
    ],
    "reason_for_being": [
      "Orientar productos académicos de Derecho administrativo y control con claridad y fundamento jurídico.",
      "Transformar la planeación semanal en reportes, presentaciones o productos visuales.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Conectar el control administrativo con aplicación jurídica profesional.",
      "Proteger integridad académica mediante fuentes verificables.",
      "Evitar propagación de reglas no estructuradas o no verificadas."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Objetivo explícito antes del desarrollo.",
      "Secciones claras y reutilizables.",
      "Lenguaje jurídico preciso.",
      "Citas trazables.",
      "Marcado explícito de supuestos.",
      "Conclusión práctica obligatoria.",
      "Coherencia entre consigna, desarrollo y cierre.",
      "Separación entre regla editorial y contenido sustantivo.",
      "No traslado acrítico de doctrinas externas."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo.",
      "Delimitar conceptos clave.",
      "Ubicar marco normativo o doctrinal.",
      "Presentar evidencia verificable.",
      "Analizar con postura propia sustentada.",
      "Relacionar el tema con control administrativo.",
      "Contrastar descripción con criterio jurídico.",
      "Cerrar con conclusión aplicable a la práctica profesional.",
      "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
      "Ajustar profundidad a consigna y rúbrica local."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Licenciatura en Derecho",
        "Derecho administrativo y control",
        "Semestre 6 bloque 1",
        "Malla curricular de Derecho",
        "Integridad académica",
        "Problema jurídico",
        "Conceptos jurídicos",
        "Marco normativo",
        "Doctrina verificable",
        "Evidencia trazable",
        "Análisis propio",
        "Postura académica",
        "Conclusión jurídica",
        "Conclusión transferible",
        "Control administrativo",
        "Práctica profesional",
        "Planeación semanal",
        "Programa analítico local",
        "Carpeta canónica",
        "Archivo bib local",
        "Normalización estructurada",
        "JSON parseable",
        "Fuente provisional",
        "Supuesto editorial",
        "README con artefactos",
        "Tokens sin expandir"
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
          "justification": "La identidad institucional exige rigor, trazabilidad y fuentes verificables."
        },
        {
          "source": "Licenciatura en Derecho",
          "target": "Derecho administrativo y control",
          "kind": "develops",
          "justification": "La materia pertenece al trayecto curricular local de Derecho."
        },
        {
          "source": "Malla curricular de Derecho",
          "target": "Semestre 6 bloque 1",
          "kind": "supports",
          "justification": "La ubicación curricular local se declara en README y bibliografía base."
        },
        {
          "source": "Carpeta canónica",
          "target": "Programa analítico local",
          "kind": "supports",
          "justification": "La carpeta organiza README, programa, plantilla y bibliografía de la materia."
        },
        {
          "source": "Planeación semanal",
          "target": "Producto solicitado",
          "kind": "depends_on",
          "justification": "El tipo de entrega debe definirse por la consigna o planeación local."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis requiere un problema delimitado para evitar resumen descriptivo."
        },
        {
          "source": "Conceptos jurídicos",
          "target": "Marco normativo",
          "kind": "supports",
          "justification": "Los conceptos ordenan la selección de normas y doctrina aplicables."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusión jurídica",
          "kind": "supports",
          "justification": "La conclusión debe derivar de normas, doctrina o evidencia verificable."
        },
        {
          "source": "Control administrativo",
          "target": "Práctica profesional",
          "kind": "develops",
          "justification": "La materia exige aplicación jurídica al ámbito administrativo."
        },
        {
          "source": "Conclusión jurídica",
          "target": "Conclusión transferible",
          "kind": "develops",
          "justification": "El cierre debe traducir el análisis en criterio aplicable."
        },
        {
          "source": "Archivo bib local",
          "target": "Evidencia trazable",
          "kind": "supports",
          "justification": "Las citas deben corresponder a entradas bibliográficas verificables."
        },
        {
          "source": "Normalización estructurada",
          "target": "JSON parseable",
          "kind": "depends_on",
          "justification": "La memoria solo debe propagarse si la salida puede validarse estructuralmente."
        },
        {
          "source": "Fuente provisional",
          "target": "Supuesto editorial",
          "kind": "supports",
          "justification": "Las reglas heredadas no verificadas deben marcarse antes de reutilizarse."
        },
        {
          "source": "README con artefactos",
          "target": "Tokens sin expandir",
          "kind": "develops",
          "justification": "El README muestra nombres corruptos y tokens pendientes de normalización."
        },
        {
          "source": "Tokens sin expandir",
          "target": "Carpeta canónica",
          "kind": "contrasts",
          "justification": "Los placeholders degradan la función canónica de la carpeta."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 6, bloque 1, obligatoria, 8 créditos.",
        "README local: fuente curricular malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: pauta de identidad UnADM, integridad académica y citas verificables.",
        "README local: conclusión jurídica con criterio propio.",
        "README local: nombres de archivo con saltos o caracteres espurios.",
        "README local: token $(@{...}.Slug) sin expandir.",
        "Programa analítico local: claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: reportes, presentaciones y productos visuales.",
        "Programa analítico local: ejes de problema, conceptos, fuentes, análisis propio y cierre.",
        "Programa analítico local: fuentes específicas deben agregarse al bib de la materia.",
        "derecho-administrativo-y-control.bib: entrada unadmSitioWeb.",
        "derecho-administrativo-y-control.bib: entrada unadmMallaDerecho2024.",
        "Plantilla tex local: curso Derecho administrativo y control.",
        "Plantilla tex local: coursecode LDE-S6B1.",
        "Plantilla tex local: Actividad X pendiente de sustituir.",
        "Plantilla tex local: Figura docente pendiente de confirmar.",
        "Memoria heredada: salida sin JSON parseable desde Codex para UnADM.",
        "Memoria transversal: reglas editoriales generales desde Filosofía del Derecho."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin eliminar contenido útil.",
      "Se conservaron reglas locales sobre semestre, bloque, obligatoriedad y créditos.",
      "Se integraron solo patrones editoriales transversales del origen.",
      "Se excluyeron doctrinas y citas específicas de Filosofía del Derecho por no estar verificadas en destino.",
      "Se reforzó la prohibición de fuentes inventadas.",
      "Se reforzó la validación JSON antes de propagación recursiva.",
      "Se mantuvo alerta por fuentes provisionales Codex y GPT-Pro.",
      "Se incorporó corrección de tokens sin expandir como tarea local.",
      "Se preservó el eje problema-conceptos-evidencia-análisis-cierre.",
      "Se fortaleció la conexión entre control administrativo y práctica profesional."
    ]
  }
}