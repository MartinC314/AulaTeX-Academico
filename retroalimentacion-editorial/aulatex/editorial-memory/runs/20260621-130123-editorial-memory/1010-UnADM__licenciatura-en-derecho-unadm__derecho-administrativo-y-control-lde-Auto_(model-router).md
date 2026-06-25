{
  "summary": [
    "Se sincroniza memoria transversal hacia Derecho administrativo y control en ciclo 11.",
    "Se aplica compresión por unión y deduplicación sin regresión.",
    "Se preserva identidad UnADM y encuadre local de Licenciatura en Derecho.",
    "Se mantiene ubicación curricular local: semestre 6, bloque 1, obligatoria, 8 créditos.",
    "Se reutilizan solo abstracciones editoriales estables desde Filosofía del Derecho.",
    "Se excluye doctrina específica no verificada para esta materia.",
    "Se refuerzan ejes editoriales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se conserva alerta institucional sobre salidas no JSON parseables.",
    "Se prioriza consistencia entre README, programa analítico, LaTeX y bibliografía local."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en portada, metadatos y redacción académica.",
    "Usar nombre exacto de materia: Derecho administrativo y control.",
    "Conservar enfoque de Licenciatura en Derecho en todos los entregables.",
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Ubicar la materia en semestre 6, bloque 1, obligatoria, 8 créditos.",
    "Citar malla-curricular-derecho-unadm.pdf para ubicación curricular.",
    "Marcar como [supuesto] todo dato no visible en la consigna local.",
    "Declarar como provisional toda regla heredada no verificada localmente.",
    "Tratar fuentes Codex y GPT-Pro heredadas como provisionales hasta confirmación local.",
    "No trasladar identidad curricular de Filosofía del Derecho al destino."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Integrar problema, conceptos, normas, doctrina, evidencia, análisis propio y conclusión transferible.",
    "Alinear cada entrega a la planeación semanal y al programa analítico local.",
    "Explicitar el producto solicitado antes del desarrollo.",
    "Adaptar estructura a reporte, presentación o producto visual según consigna.",
    "Vincular el desarrollo con control administrativo y práctica profesional.",
    "Cerrar con conclusión jurídica aplicable a la práctica profesional.",
    "Mantener consistencia entre README, plantilla .tex y archivo .bib.",
    "Nombrar archivos con slug derecho-administrativo-y-control cuando aplique.",
    "Corregir artefactos de estructura en README antes de publicar índices.",
    "Resolver tokens PowerShell sin expandir por el slug literal derecho-administrativo-y-control. [supuesto]",
    "Corregir nombres de archivo con saltos de línea o caracteres espurios. [supuesto]"
  ],
  "activity_rules": [
    "Verificar el producto exacto solicitado por cada actividad.",
    "Incluir postura académica propia, no solo resumen descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Distinguir hechos, normas, doctrina, interpretación y criterio propio.",
    "Relacionar el tema con control administrativo cuando la consigna lo permita.",
    "Formular criterio jurídico transferible a la práctica profesional.",
    "No omitir conclusión final orientada a aplicación jurídica.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Separar reglas editoriales generales de contenidos sustantivos heredados.",
    "No asumir que fuentes de otra materia correspondan a esta asignatura.",
    "No asumir que fuentes de semanas posteriores correspondan a una actividad local."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar memoria aguas abajo.",
    "Detener propagación si hay respuesta no estructurada o campos críticos vacíos.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de [supuesto].",
    "Verificar integridad académica con citas verificables y sin fuentes inventadas.",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Confirmar trazabilidad entre afirmaciones y bibliografía local.",
    "Revisar que reglas heredadas no contradigan el programa analítico local.",
    "Validar que README y programa no conserven placeholders ni rutas corruptas.",
    "Validar que el producto corresponda a la consigna de actividad.",
    "Revisar respuestas no estructuradas antes de reutilizarlas.",
    "Compilar LaTeX sin errores críticos ni referencias rotas."
  ],
  "latex_rules": [
    "Mantener plantilla LaTeX en español.",
    "Mantener formato letterpaper según archivo base.",
    "Completar metadatos institucionales y de curso antes de compilar.",
    "Conservar tabla de datos académicos del estudiante y figura docente en portada.",
    "Sustituir Nombre por definir por el nombre oficial de la figura docente antes de entregar.",
    "Asegurar coherencia entre \\documenttitle, \\documentsubtitle y actividad real.",
    "Reemplazar Actividad X por número y nombre real de la actividad.",
    "Mantener coursecode LDE-S6B1 salvo evidencia institucional distinta.",
    "Usar codificación y acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar compilaciones rotas.",
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
    "Conservar metadatos mínimos: autor, título, año, medio o URL y nota de consulta.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Validar correspondencia entre citas en texto y entradas BibTeX.",
    "Confirmar convención final del archivo de referencias local. [supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validación de JSON y estructura.",
    "Propagar a laterales solo reglas editoriales compartibles.",
    "No propagar contenido específico de actividad a laterales.",
    "No trasladar doctrina específica de Filosofía del Derecho sin verificación local.",
    "Preservar alerta institucional sobre respuestas no estructuradas en niveles superiores.",
    "Aplicar normalización manual cuando la fuente sea provisional.",
    "Mantener estrategia de compresión unión-dedupe lossless en fusiones futuras.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Marcar conflictos de nomenclatura entre rutas antes de consolidar. [supuesto]",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Ciclo 1 necesita normalización manual si se reutiliza.",
    "Ciclo 11 refuerza transferencia transversal conservadora."
  ],
  "open_questions": [
    "Confirmar nombre oficial de la figura docente en plantilla.",
    "Confirmar si existe formato institucional obligatorio de citas para Derecho.",
    "Confirmar convención final del archivo de referencias en la materia.",
    "Verificar si el año de consulta del sitio institucional UnADM debe mantenerse en 2026.",
    "Confirmar si los tokens PowerShell sin expandir son artefacto de generación. [supuesto]",
    "Corregir posibles artefactos de ruta o nombre en README. [supuesto]",
    "Definir fuente definitiva para reemplazar referencias provisionales Codex y GPT-Pro.",
    "Confirmar rúbricas específicas de actividades futuras.",
    "Confirmar fuentes obligatorias por semana cuando exista consigna local.",
    "Confirmar si cada actividad requiere reporte, presentación o producto visual."
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
        "Carpeta de materia como entrada canónica.",
        "Normalización estructurada antes de propagación.",
        "Supuestos marcados de forma visible.",
        "No invención de fuentes.",
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
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable.",
      "Análisis propio con postura académica.",
      "Control administrativo como eje local.",
      "Conclusión transferible a la práctica jurídica.",
      "Normalización estructurada.",
      "Consistencia documental."
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
      "Transformar la planeación semanal en reportes, presentaciones o productos visuales.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Formar criterio jurídico aplicable al control administrativo.",
      "Garantizar trazabilidad entre consigna, desarrollo, citas y bibliografía.",
      "Proteger la memoria editorial contra salidas no estructuradas y fuentes no verificadas."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Objetivo explícito.",
      "Secciones visibles.",
      "Marco normativo o doctrinal delimitado.",
      "Citas trazables.",
      "Postura propia identificable.",
      "Conclusión práctica obligatoria.",
      "Supuestos marcados con [supuesto].",
      "Lenguaje jurídico claro.",
      "Metadatos UnADM consistentes.",
      "Advertencia ante fuentes provisionales."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo.",
      "Delimitar conceptos y marco normativo.",
      "Distinguir norma, doctrina, evidencia y opinión propia.",
      "Analizar con postura sustentada.",
      "Vincular el tema con control administrativo cuando corresponda.",
      "Contrastar consigna, fuentes y criterio jurídico.",
      "Cerrar con conclusión aplicable a práctica profesional.",
      "Verificar coherencia entre pregunta guía, desarrollo y cierre.",
      "Evitar exposición meramente descriptiva.",
      "Alinear forma del producto con la planeación semanal."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Licenciatura en Derecho",
        "Derecho administrativo y control",
        "Semestre 6 bloque 1",
        "Integridad académica",
        "Normalización estructurada",
        "Problema jurídico",
        "Marco normativo",
        "Doctrina verificable",
        "Evidencia trazable",
        "Análisis propio",
        "Postura académica",
        "Control administrativo",
        "Práctica profesional",
        "Conclusión transferible",
        "Planeación semanal",
        "Programa analítico local",
        "README local",
        "Plantilla LaTeX",
        "Bibliografía local",
        "Malla curricular de Derecho",
        "Fuentes provisionales",
        "JSON parseable",
        "Compresión unión-dedupe"
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
          "justification": "La malla local respalda la ubicación curricular de la materia."
        },
        {
          "source": "Derecho administrativo y control",
          "target": "Control administrativo",
          "kind": "develops",
          "justification": "El eje local de la materia orienta el análisis hacia administración pública y control."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis requiere un problema delimitado para evitar desarrollo descriptivo."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión práctica debe apoyarse en normas y fuentes verificables."
        },
        {
          "source": "Doctrina verificable",
          "target": "Postura académica",
          "kind": "supports",
          "justification": "La postura propia debe dialogar con fuentes consultables."
        },
        {
          "source": "Evidencia trazable",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La trazabilidad evita fuentes inventadas y afirmaciones sin respaldo."
        },
        {
          "source": "Planeación semanal",
          "target": "Producto solicitado",
          "kind": "develops",
          "justification": "La planeación define si el entregable será reporte, presentación o producto visual."
        },
        {
          "source": "Programa analítico local",
          "target": "Estructura editorial",
          "kind": "supports",
          "justification": "El programa local fija propósito, ejes de trabajo y pauta de realización."
        },
        {
          "source": "README local",
          "target": "Carpeta de materia",
          "kind": "supports",
          "justification": "El README declara la carpeta como punto de entrada canónico."
        },
        {
          "source": "Plantilla LaTeX",
          "target": "Metadatos UnADM",
          "kind": "depends_on",
          "justification": "La portada y los campos del documento requieren metadatos completos."
        },
        {
          "source": "Bibliografía local",
          "target": "Citas verificables",
          "kind": "supports",
          "justification": "El archivo .bib local debe contener las fuentes citadas en cada actividad."
        },
        {
          "source": "JSON parseable",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "La memoria no debe propagarse si no puede validarse estructuralmente."
        },
        {
          "source": "Fuentes provisionales",
          "target": "Supuestos marcados",
          "kind": "depends_on",
          "justification": "Toda fuente heredada no verificada debe declararse provisional o como supuesto."
        },
        {
          "source": "Compresión unión-dedupe",
          "target": "Sin regresión",
          "kind": "supports",
          "justification": "La deduplicación conserva reglas útiles sin recortar contenido válido."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 6, bloque 1, obligatoria, 8 créditos.",
        "README local: fuente curricular malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: identidad UnADM, integridad académica, citas verificables y conclusión jurídica.",
        "Programa analítico local: productos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: reportes, presentaciones y productos visuales.",
        "Programa analítico local: ejes de problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
        "derecho-administrativo-y-control.bib: entrada unadmSitioWeb.",
        "derecho-administrativo-y-control.bib: entrada unadmMallaDerecho2024.",
        "Plantilla LaTeX local: coursecode LDE-S6B1.",
        "Plantilla LaTeX local: documentsubtitle contiene Actividad X.",
        "Plantilla LaTeX local: figura docente pendiente.",
        "Memoria institucional heredada: revisar respuestas no estructuradas antes de aplicar aguas abajo.",
        "Memoria de origen: normalización estructurada obligatoria antes de propagar.",
        "Memoria de origen: ejes estables de problema, conceptos, evidencia, análisis propio y conclusión jurídica."
      ]
    },
    "reinforcement_log": [
      "Ciclo 11 conserva memoria local y agrega solo abstracciones transversales verificables.",
      "Se deduplican reglas repetidas de identidad, estructura, calidad y bibliografía.",
      "Se refuerza prohibición de fuentes inventadas.",
      "Se refuerza bloqueo ante salidas no JSON parseables.",
      "Se mantiene alerta sobre fuentes provisionales Codex y GPT-Pro.",
      "Se evita transferir doctrina específica de Filosofía del Derecho.",
      "Se preserva ubicación curricular local del destino.",
      "Se actualiza el grafo con relaciones válidas: supports, contrasts, depends_on y develops.",
      "Se mantiene malla curricular como evidencia de ubicación.",
      "Se refuerza consistencia entre README, programa, LaTeX y .bib.",
      "Se conserva conclusión jurídica transferible como marca estilística.",
      "Se consolida el destino como cerebro editorial mínimo y operativo de materia."
    ]
  }
}