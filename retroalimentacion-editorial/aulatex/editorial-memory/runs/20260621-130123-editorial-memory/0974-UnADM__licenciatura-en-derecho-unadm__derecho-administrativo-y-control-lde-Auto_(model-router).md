{
  "summary": [
    "Se consolida memoria de materia para Derecho administrativo y control.",
    "Se aplica compresión union-dedupe lossless y sin regresión.",
    "Se preserva identidad institucional UnADM.",
    "Se mantiene alineación curricular local: semestre 6, bloque 1, obligatoria, 8 créditos.",
    "Se reutilizan solo abstracciones editoriales estables desde Filosofía del Derecho.",
    "No se transfiere doctrina específica de la materia origen.",
    "Se conserva alerta por salidas no JSON parseables heredadas.",
    "Se refuerzan ejes editoriales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se prioriza normalización estructurada antes de propagación recursiva.",
    "Se preservan fuentes locales verificables: README, programa analítico y archivo .bib local."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en portada, metadatos y redacción académica.",
    "Usar nombre exacto de materia: Derecho administrativo y control.",
    "Conservar enfoque de Licenciatura en Derecho en todos los entregables.",
    "Conservar encuadre curricular local: semestre 6, bloque 1, obligatoria, 8 créditos.",
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Marcar como [supuesto] todo dato no visible en la consigna local.",
    "Declarar cuando una regla provenga de fuente provisional.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Fuente provisional: Codex desde ingeniería-en-sistemas-computacionales. [supuesto]",
    "Fuente provisional: GPT-Pro desde Actividad 1. [supuesto]",
    "Usar malla-curricular-derecho-unadm.pdf como fuente curricular local."
  ],
  "structure_rules": [
    "Organizar cada producto con problema, conceptos, fuentes, análisis propio y conclusión jurídica.",
    "Incluir normas y doctrina cuando la consigna lo requiera.",
    "Definir objetivo puntual antes del desarrollo.",
    "Abrir con encuadre breve del problema jurídico o social.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear entregables a la planeación semanal y al programa analítico local.",
    "Explicitar el tipo de producto antes de desarrollar.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener consistencia entre README, plantilla .tex y archivo .bib.",
    "Nombrar archivos con slug derecho-administrativo-y-control cuando aplique.",
    "Corregir artefactos de estructura en README antes de publicar índices.",
    "Resolver tokens PowerShell sin expandir por el slug literal derecho-administrativo-y-control. [supuesto]",
    "Corregir nombres de archivo con saltos de línea o caracteres espurios en README. [supuesto]"
  ],
  "activity_rules": [
    "Verificar que el producto corresponda a la consigna específica.",
    "Identificar si el producto es reporte, presentación o visual.",
    "Vincular el tema con control administrativo y práctica profesional.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura académica propia.",
    "Evitar entregas solo descriptivas.",
    "Formular criterio jurídico transferible a la práctica profesional.",
    "No omitir conclusión final orientada a aplicación jurídica.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Separar reglas editoriales generales de contenidos sustantivos heredados de otras materias.",
    "No asumir que fuentes de otras semanas o materias corresponden a una actividad local."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Detener propagación si hay respuesta no estructurada.",
    "Detener propagación si hay campos críticos vacíos.",
    "Revisar respuesta no estructurada antes de reutilizarla.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de [supuesto].",
    "Verificar integridad académica con citas verificables y sin fuentes inventadas.",
    "Confirmar trazabilidad entre afirmaciones y bibliografía local.",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Validar que README y programa no conserven placeholders ni rutas corruptas.",
    "Revisar que reglas heredadas no contradigan el programa analítico local.",
    "Validar que no se transfiera doctrina específica de Filosofía del Derecho sin evidencia local."
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
    "Conservar metadatos mínimos: autor, título, año, medio o fuente y nota de consulta.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Validar que las citas en texto existan en el .bib local.",
    "No asumir bibliografía de Filosofía del Derecho como bibliografía local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validación de estructura JSON.",
    "Propagar a laterales solo reglas editoriales compartibles.",
    "No propagar contenido específico de actividad a laterales.",
    "No transferir doctrina sustantiva entre materias no equivalentes sin evidencia local.",
    "Aplicar normalización manual cuando la fuente sea provisional.",
    "Mantener estrategia de compresión union-dedupe lossless en fusiones futuras.",
    "Preservar alerta institucional sobre respuestas no estructuradas en niveles superiores.",
    "Marcar conflictos de nomenclatura entre rutas antes de consolidar. [supuesto]",
    "Reutilizar gates de calidad institucional sin reducir especificidad local.",
    "Ciclo 1 necesita normalización manual si se reutiliza.",
    "Ciclo 2 necesita normalización manual si se reutiliza."
  ],
  "open_questions": [
    "Definir fuente definitiva para reemplazar referencias provisionales Codex y GPT-Pro.",
    "Confirmar nombre oficial de la figura docente en plantilla.",
    "Validar si existe formato institucional obligatorio de citas para la Licenciatura en Derecho.",
    "Confirmar convención final del archivo de referencias en la materia.",
    "Confirmar si el archivo de referencias debe llamarse referencias-derecho-administrativo-y-control.",
    "Verificar si el año de consulta del sitio institucional UnADM debe mantenerse en 2026.",
    "Confirmar si los tokens PowerShell sin expandir en README y programa son artefacto de generación. [supuesto]",
    "Corregir posibles artefactos de ruta o nombre en listado de estructura del README. [supuesto]",
    "Confirmar fuentes obligatorias por actividad local.",
    "Confirmar rúbricas específicas antes de ajustar profundidad argumentativa."
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
        "Respeto del programa analítico local."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho administrativo y control.",
        "Semestre 6, bloque 1.",
        "Tipo obligatoria.",
        "8 créditos.",
        "Fuente curricular local: malla-curricular-derecho-unadm.pdf.",
        "Coursecode local: LDE-S6B1."
      ]
    },
    "essence": [
      "Identidad UnADM.",
      "Integridad académica.",
      "Problema jurídico delimitado.",
      "Control administrativo.",
      "Marco normativo o doctrinal verificable.",
      "Evidencia trazable.",
      "Análisis propio.",
      "Postura académica.",
      "Conclusión transferible.",
      "Aplicación profesional.",
      "Normalización estructurada.",
      "Propagación conservadora."
    ],
    "reason_for_being": [
      "Orientar productos académicos de Derecho administrativo y control.",
      "Convertir la planeación semanal en entregables claros y verificables.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Vincular el control administrativo con práctica jurídica profesional.",
      "Garantizar trazabilidad entre afirmaciones, citas y bibliografía local.",
      "Evitar regresiones editoriales al fusionar memorias.",
      "Preservar reglas institucionales útiles sin trasladar contenido ajeno no verificado."
    ],
    "style_markers": [
      "Usar nombre exacto de la materia.",
      "Presentar encuadre institucional breve.",
      "Declarar objetivo antes del desarrollo.",
      "Separar problema, conceptos, fuentes, análisis y cierre.",
      "Usar citas verificables.",
      "Marcar [supuesto] cuando falte evidencia local.",
      "Cerrar con criterio jurídico aplicable.",
      "Evitar resumen sin postura.",
      "Evitar doctrina heredada no validada.",
      "Mantener consistencia entre README, .tex y .bib.",
      "Corregir placeholders antes de publicar."
    ],
    "argumentative_patterns": [
      "Problema jurídico → objetivo → marco normativo → análisis propio → conclusión transferible.",
      "Consigna → producto esperado → estructura del entregable → verificación final.",
      "Afirmación → fuente verificable → interpretación jurídica → criterio propio.",
      "Contexto institucional → ubicación curricular → propósito de aprendizaje → práctica profesional.",
      "Regla heredada → validación local → adopción conservadora.",
      "Dato no visible → marca [supuesto] → pregunta abierta.",
      "Control administrativo → evidencia normativa → impacto en administración pública.",
      "Bibliografía base → fuente específica → cita en texto → entrada .bib."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Licenciatura en Derecho",
        "Derecho administrativo y control",
        "Semestre 6 bloque 1",
        "Malla curricular local",
        "Problema jurídico",
        "Control administrativo",
        "Marco normativo",
        "Marco doctrinal",
        "Evidencia verificable",
        "Citas trazables",
        "Bibliografía local",
        "Análisis propio",
        "Postura académica",
        "Conclusión jurídica",
        "Transferencia profesional",
        "Planeación semanal",
        "Producto solicitado",
        "Reporte",
        "Presentación",
        "Producto visual",
        "Normalización estructurada",
        "JSON parseable",
        "Propagación recursiva",
        "Union-dedupe lossless",
        "Fuentes provisionales",
        "Supuestos visibles",
        "README local",
        "Programa analítico local",
        "Plantilla LaTeX",
        "Archivo BibTeX local",
        "Tokens PowerShell sin expandir",
        "Rutas corruptas"
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
          "justification": "La pauta local exige identidad institucional, citas verificables y criterio propio."
        },
        {
          "source": "Malla curricular local",
          "target": "Semestre 6 bloque 1",
          "kind": "supports",
          "justification": "El README local declara semestre 6, bloque 1, tipo obligatoria y 8 créditos."
        },
        {
          "source": "Derecho administrativo y control",
          "target": "Control administrativo",
          "kind": "develops",
          "justification": "La materia debe vincular actividades con control administrativo y práctica profesional."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis académico se estructura desde un problema delimitado."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusión jurídica",
          "kind": "supports",
          "justification": "La conclusión transferible requiere sustento jurídico verificable."
        },
        {
          "source": "Marco doctrinal",
          "target": "Postura académica",
          "kind": "supports",
          "justification": "La postura propia debe dialogar con conceptos y doctrina pertinente."
        },
        {
          "source": "Evidencia verificable",
          "target": "Citas trazables",
          "kind": "supports",
          "justification": "Cada afirmación sustantiva debe poder rastrearse a una fuente consultable."
        },
        {
          "source": "Citas trazables",
          "target": "Bibliografía local",
          "kind": "depends_on",
          "justification": "Las citas en texto deben existir en derecho-administrativo-y-control.bib."
        },
        {
          "source": "Planeación semanal",
          "target": "Producto solicitado",
          "kind": "develops",
          "justification": "El programa analítico indica transformar la planeación en productos académicos."
        },
        {
          "source": "Producto solicitado",
          "target": "Reporte",
          "kind": "develops",
          "justification": "El destino admite reporte como tipo de artefacto."
        },
        {
          "source": "Producto solicitado",
          "target": "Presentación",
          "kind": "develops",
          "justification": "El destino admite presentación como tipo de artefacto."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "La memoria solo debe propagarse si la salida es JSON parseable."
        },
        {
          "source": "JSON parseable",
          "target": "Propagación recursiva",
          "kind": "supports",
          "justification": "El gate institucional bloquea salidas no estructuradas."
        },
        {
          "source": "Union-dedupe lossless",
          "target": "Normalización estructurada",
          "kind": "supports",
          "justification": "La consolidación preserva reglas útiles y elimina duplicados sin recorte."
        },
        {
          "source": "Fuentes provisionales",
          "target": "Supuestos visibles",
          "kind": "depends_on",
          "justification": "Las fuentes heredadas no verificadas deben declararse como provisionales o supuestas."
        },
        {
          "source": "README local",
          "target": "Programa analítico local",
          "kind": "supports",
          "justification": "Ambos documentos fijan identidad, ubicación curricular y pauta editorial."
        },
        {
          "source": "Plantilla LaTeX",
          "target": "Archivo BibTeX local",
          "kind": "depends_on",
          "justification": "La compilación académica requiere correspondencia entre citas y .bib."
        },
        {
          "source": "Tokens PowerShell sin expandir",
          "target": "Rutas corruptas",
          "kind": "supports",
          "justification": "El README y programa muestran placeholders que pueden romper referencias."
        },
        {
          "source": "Filosofía del Derecho",
          "target": "Derecho administrativo y control",
          "kind": "contrasts",
          "justification": "La relación es transversal; solo se comparten abstracciones editoriales estables."
        },
        {
          "source": "Conclusión jurídica",
          "target": "Transferencia profesional",
          "kind": "develops",
          "justification": "El cierre debe convertir el análisis en criterio aplicable a la práctica."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 6, bloque 1, obligatoria, 8 créditos.",
        "README local: fuente curricular UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: cada actividad conserva identidad UnADM, integridad académica, citas verificables y conclusión jurídica.",
        "Programa analítico local: productos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: transformar planeación semanal en reportes, presentaciones y productos visuales.",
        "Programa analítico local: ejes de problema, conceptos, producto, análisis propio y conclusión transferible.",
        "derecho-administrativo-y-control.bib: entrada unadmSitioWeb.",
        "derecho-administrativo-y-control.bib: entrada unadmMallaDerecho2024.",
        "Plantilla LaTeX local: documenttitle Plantilla base de Derecho administrativo y control.",
        "Plantilla LaTeX local: documentsubtitle Actividad X - Derecho administrativo y control.",
        "Plantilla LaTeX local: coursecode LDE-S6B1.",
        "Plantilla LaTeX local: figura docente pendiente como Nombre por definir.",
        "Memoria institucional heredada: alerta por salida sin JSON parseable desde Codex.",
        "Memoria origen transversal: ejes editoriales estables de problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
        "Regla de transferencia: compartir solo abstracciones editoriales estables entre nodos no equivalentes."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2 consolida destino con estrategia progresiva y conservadora.",
      "Se preservan reglas locales sobre semestre 6, bloque 1, obligatoriedad y créditos.",
      "Se deduplican frases repetidas sin eliminar reglas útiles.",
      "Se normalizan alertas sobre Codex y GPT-Pro como fuentes provisionales.",
      "Se integran reglas transversales de estructura sin trasladar doctrina de Filosofía del Derecho.",
      "Se refuerza gate de JSON parseable antes de propagación.",
      "Se refuerza trazabilidad entre citas en texto y derecho-administrativo-y-control.bib.",
      "Se mantiene obligación de marcar supuestos visibles.",
      "Se preserva corrección pendiente de tokens PowerShell en README y programa.",
      "Se conserva necesidad de completar figura docente antes de entrega.",
      "Se fortalece grafo conceptual con control administrativo y transferencia profesional.",
      "Se limita bibliografía a fuentes locales verificables y futuras fuentes consultadas."
    ]
  }
}