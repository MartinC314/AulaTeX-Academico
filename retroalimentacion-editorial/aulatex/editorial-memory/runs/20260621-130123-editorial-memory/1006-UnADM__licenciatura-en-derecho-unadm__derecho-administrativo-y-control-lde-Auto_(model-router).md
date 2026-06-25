{
  "summary": [
    "Se consolida memoria editorial de materia para Derecho administrativo y control.",
    "Se aplica compresión union-dedupe sin regresión.",
    "Se preserva identidad UnADM y encuadre de Licenciatura en Derecho.",
    "Se mantiene ubicación curricular local: semestre 6, bloque 1, obligatoria, 8 créditos.",
    "Se sincronizan solo abstracciones editoriales transversales desde Filosofía del Derecho.",
    "No se transfiere doctrina específica de Filosofía del Derecho al destino.",
    "Se refuerzan ejes estables: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se conserva alerta por salidas no JSON parseables antes de propagación.",
    "Se mantiene prioridad de normalización estructurada antes de reutilizar memoria.",
    "Se preserva la carpeta de materia como punto de entrada canónico."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en portada, metadatos y redacción académica.",
    "Usar nombre exacto de materia: Derecho administrativo y control.",
    "Conservar enfoque de Licenciatura en Derecho en todos los entregables.",
    "Usar ubicación curricular local: semestre 6, bloque 1, obligatoria, 8 créditos.",
    "Citar malla-curricular-derecho-unadm.pdf como fuente de ubicación curricular.",
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Marcar como [supuesto] todo dato no visible en la consigna local.",
    "Declarar cuando una regla provenga de fuente provisional.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Fuente provisional: Codex desde ingeniería-en-sistemas-computacionales.",
    "Fuente provisional: GPT-Pro desde Actividad 1."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar cada producto con problema, conceptos, normas, doctrina, fuentes, análisis propio y conclusión jurídica.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear entregables a la planeación semanal y al programa analítico local.",
    "Explicitar el tipo de producto solicitado antes del desarrollo.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener consistencia entre README, plantilla .tex y archivo .bib.",
    "Nombrar archivos con slug derecho-administrativo-y-control cuando aplique.",
    "Corregir artefactos de estructura en README antes de publicar índices.",
    "Resolver tokens PowerShell sin expandir en README y programa analítico por el slug literal derecho-administrativo-y-control. [supuesto]",
    "Corregir nombres de archivo con caracteres espurios o saltos de línea en README. [supuesto]"
  ],
  "activity_rules": [
    "Verificar que el producto corresponda a la consigna de la actividad.",
    "Identificar si el producto es reporte, presentación o visual.",
    "Incluir postura académica propia en cada actividad.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Vincular el tema con control administrativo y práctica profesional.",
    "Formular criterio jurídico transferible a la práctica profesional.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No omitir conclusión final orientada a aplicación jurídica.",
    "Separar reglas editoriales generales de contenidos sustantivos heredados de otras materias.",
    "No asumir que fuentes de otra semana o materia correspondan a una actividad local."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar respuesta no estructurada antes de aplicar aguas abajo.",
    "Validar estructura mínima completa antes de reutilizar memoria.",
    "Detener propagación si hay campos críticos vacíos.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de [supuesto].",
    "Verificar integridad académica con citas verificables y sin fuentes inventadas.",
    "Confirmar trazabilidad entre afirmaciones y bibliografía local.",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Validar que README y programa no conserven placeholders ni rutas corruptas.",
    "Revisar que reglas heredadas no contradigan el programa analítico local.",
    "Confirmar que el producto final responda a la consigna específica.",
    "Compilar artefactos LaTeX sin errores críticos ni referencias rotas."
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
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
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
    "No agregar referencias sin evidencia documental.",
    "Usar solo obras realmente consultables.",
    "Conservar metadatos mínimos: autor, título, año, medio o editorial, URL si aplica y nota de consulta.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Confirmar convención final del archivo de referencias antes de renombrar."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo tras validación de estructura JSON.",
    "Propagar recursivamente solo reglas generales verificadas.",
    "Propagar a laterales solo reglas editoriales compartibles.",
    "No propagar contenido específico de actividad a laterales.",
    "No trasladar doctrina de Filosofía del Derecho sin verificación local.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Aplicar normalización manual cuando la fuente sea provisional.",
    "Mantener estrategia de compresión union-dedupe lossless en fusiones futuras.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Marcar conflictos de nomenclatura entre rutas antes de consolidar. [supuesto]",
    "Preservar alerta institucional sobre respuestas no estructuradas en niveles superiores.",
    "Ciclo 10 refuerza sincronización transversal conservadora."
  ],
  "open_questions": [
    "Confirmar nombre oficial de la figura docente en plantilla.",
    "Confirmar si existe formato institucional obligatorio de citas para la Licenciatura en Derecho.",
    "Confirmar convención final del archivo de referencias de la materia.",
    "Verificar si el año de consulta del sitio institucional UnADM debe mantenerse en 2026.",
    "Confirmar si los tokens PowerShell sin expandir en README y programa son artefactos de generación. [supuesto]",
    "Corregir posibles artefactos de ruta o nombre en listado de estructura del README. [supuesto]",
    "Definir fuente definitiva para reemplazar referencias provisionales Codex y GPT-Pro.",
    "Confirmar consignas locales de actividades antes de especializar reglas.",
    "Confirmar fuentes obligatorias por semana cuando existan.",
    "Confirmar si derecho-administrativo-y-control.bib es el archivo canónico definitivo."
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
        "Normalización estructurada antes de propagación.",
        "Carpeta de materia como entrada canónica.",
        "Respeto del programa analítico local.",
        "Consistencia entre README, LaTeX y bibliografía."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho administrativo y control.",
        "Semestre 6, bloque 1.",
        "Tipo obligatoria.",
        "8 créditos.",
        "Coursecode local: LDE-S6B1.",
        "Fuente curricular local: malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Identidad UnADM.",
      "Integridad académica.",
      "Problema jurídico o social delimitado.",
      "Conceptos, normas, doctrina y datos pertinentes.",
      "Fuentes verificables.",
      "Análisis propio y postura académica.",
      "Control administrativo.",
      "Conclusión transferible a la práctica jurídica.",
      "Normalización estructurada.",
      "Coherencia entre consigna, desarrollo y cierre."
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
      "Transformar la planeación semanal en reportes, presentaciones y productos visuales.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Vincular el estudio del control administrativo con la práctica profesional.",
      "Evitar entregas descriptivas sin criterio jurídico propio.",
      "Preservar trazabilidad editorial entre README, programa, LaTeX y bibliografía."
    ],
    "style_markers": [
      "Encuadre jurídico inicial.",
      "Objetivo explícito.",
      "Secciones ordenadas y verificables.",
      "Citas trazables.",
      "Lenguaje institucional UnADM.",
      "Marcado explícito de [supuesto].",
      "Conclusión práctica obligatoria.",
      "Criterio jurídico transferible.",
      "Prudencia ante fuentes heredadas.",
      "No traslado literal entre materias no equivalentes."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo.",
      "Delimitar conceptos clave.",
      "Ubicar marco normativo o doctrinal.",
      "Incorporar fuentes verificables.",
      "Analizar con postura propia sustentada.",
      "Relacionar el argumento con control administrativo.",
      "Contrastar descripción con criterio jurídico aplicable.",
      "Cerrar con conclusión jurídica transferible.",
      "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
      "Ajustar profundidad al producto solicitado."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Licenciatura en Derecho",
        "Derecho administrativo y control",
        "Semestre 6 bloque 1",
        "Malla curricular de Derecho",
        "Problema jurídico",
        "Marco normativo o doctrinal",
        "Conceptos jurídicos pertinentes",
        "Fuentes verificables",
        "Integridad académica",
        "Análisis propio",
        "Postura académica",
        "Control administrativo",
        "Práctica profesional",
        "Conclusión transferible",
        "Planeación semanal",
        "Programa analítico local",
        "README local",
        "Plantilla LaTeX",
        "Archivo BibTeX local",
        "Normalización estructurada",
        "Propagación recursiva",
        "Salida JSON parseable",
        "Fuente provisional",
        "Supuesto marcado"
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
          "source": "Malla curricular de Derecho",
          "target": "Semestre 6 bloque 1",
          "kind": "supports",
          "justification": "La ubicación curricular local se declara con fuente institucional."
        },
        {
          "source": "Programa analítico local",
          "target": "Planeación semanal",
          "kind": "develops",
          "justification": "El programa orienta la transformación de la planeación en productos académicos."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis propio requiere un problema delimitado."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión práctica debe apoyarse en fundamentos jurídicos verificables."
        },
        {
          "source": "Fuentes verificables",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Las citas verificables evitan afirmaciones sin respaldo."
        },
        {
          "source": "Control administrativo",
          "target": "Práctica profesional",
          "kind": "develops",
          "justification": "La materia orienta el criterio jurídico hacia la administración pública y su control."
        },
        {
          "source": "Plantilla LaTeX",
          "target": "README local",
          "kind": "depends_on",
          "justification": "Los nombres y metadatos deben ser consistentes con la estructura declarada."
        },
        {
          "source": "Archivo BibTeX local",
          "target": "Fuentes verificables",
          "kind": "supports",
          "justification": "El .bib local registra la evidencia bibliográfica usada por la materia."
        },
        {
          "source": "Salida JSON parseable",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura válida no debe aplicarse memoria aguas abajo."
        },
        {
          "source": "Fuente provisional",
          "target": "Supuesto marcado",
          "kind": "supports",
          "justification": "Toda fuente no verificada debe declararse provisional o como supuesto."
        },
        {
          "source": "Doctrina específica de Filosofía del Derecho",
          "target": "Derecho administrativo y control",
          "kind": "contrasts",
          "justification": "La sincronización transversal solo permite abstracciones editoriales, no contenido doctrinal no verificado."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 6, bloque 1, obligatoria, 8 créditos.",
        "README local: fuente curricular UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: identidad UnADM, integridad académica, citas verificables y conclusión jurídica con criterio propio.",
        "Programa analítico local: claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: productos como reportes, presentaciones y productos visuales.",
        "Programa analítico local: ejes de problema, conceptos, producto, análisis propio y conclusión transferible.",
        "derecho-administrativo-y-control.bib: entrada unadmSitioWeb.",
        "derecho-administrativo-y-control.bib: entrada unadmMallaDerecho2024.",
        "Plantilla LaTeX local: documenttitle Plantilla base de Derecho administrativo y control.",
        "Plantilla LaTeX local: documentsubtitle Actividad X - Derecho administrativo y control.",
        "Plantilla LaTeX local: coursecode LDE-S6B1.",
        "Plantilla LaTeX local: Figura docente marcada como Nombre por definir.",
        "Memoria institucional heredada: salida sin JSON parseable desde Codex para UnADM.",
        "Memoria de origen: normalización estructurada obligatoria antes de propagar.",
        "Regla de transferencia: compartir solo abstracciones editoriales estables entre nodos no equivalentes."
      ]
    },
    "reinforcement_log": [
      "Ciclo 10 consolida sincronización transversal desde actividad hacia materia.",
      "Se preserva memoria local de Derecho administrativo y control como autoridad principal.",
      "Se deduplican reglas repetidas sin eliminar contenido útil.",
      "Se refuerza normalización JSON como gate de propagación.",
      "Se refuerza no invención de fuentes.",
      "Se marca como provisional todo origen no verificado.",
      "Se conserva el encuadre curricular local con evidencia del README.",
      "Se incorporan ejes editoriales transversales sin trasladar doctrina de Filosofía del Derecho.",
      "Se corrigen relaciones del grafo a tipos permitidos: supports, contrasts, depends_on y develops.",
      "Se mantiene el ADN: problema, fuentes, análisis propio y conclusión jurídica aplicable."
    ]
  }
}