{
  "summary": [
    "Materia destino activa: Garantías constitucionales.",
    "Contexto local verificado: UnADM, Licenciatura en Derecho.",
    "Ubicación curricular local verificada: semestre 2, bloque 1, obligatoria, 8 créditos.",
    "Archivos locales activos: README, programa analítico, plantilla LaTeX y bib local.",
    "Origen ciclo 3 parseable; se integran solo abstracciones editoriales estables.",
    "Relación transversal; no transferir contenido disciplinar de Filosofía del Derecho.",
    "Se preservan alertas históricas de salidas no estructuradas desde Codex y GPT-Pro.",
    "Se aplica compresión por unión y deduplicación sin regresión.",
    "ADN editorial reforzado: problema, conceptos, fuentes, análisis propio y conclusión jurídica.",
    "Supuesto: reglas heredadas aplican como control editorial, no como contenido local."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en portada, encabezados y referencias institucionales.",
    "Usar datos locales: Garantías constitucionales, LDE-S2B1, semestre 2, bloque 1.",
    "Registrar tipo obligatoria y 8 créditos cuando aparezcan datos curriculares.",
    "Conservar coherencia con Licenciatura en Derecho en todo producto.",
    "Usar la carpeta de materia como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas desde Codex y GPT-Pro como provisionales.",
    "No trasladar contenido disciplinar de Filosofía del Derecho sin validación expresa.",
    "Citar la malla curricular local solo para ubicación curricular.",
    "Preservar tono institucional, jurídico y académico."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir problema, fuentes, producto solicitado, postura y conclusión.",
    "Alinear cada entrega al producto pedido por la planeación semanal.",
    "Mantener separación entre reporte, presentación, programa analítico y bibliografía.",
    "Usar nombres locales verificados: reporte-garantias-constitucionales.tex, presentacion-garantias-constitucionales.tex y garantias-constitucionales.bib.",
    "Preservar el programa analítico como guía editorial de la asignatura.",
    "Mantener referencias-garantias-constitucionales como depósito de fuentes locales.",
    "Corregir nombres truncados en README antes de usarlo como índice operativo.",
    "Corregir placeholders generados antes de citar archivos internos.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Incluir problema jurídico o social claro desde la introducción.",
    "Vincular cada afirmación relevante con fuente verificable o norma identificable.",
    "Distinguir hechos, conceptos, normas, doctrina y opinión propia.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Confirmar que el producto corresponda a la consigna local.",
    "No asumir fuentes de otra materia como obligatorias para esta asignatura.",
    "Sustentar afirmaciones constitucionales con fundamento normativo o bibliográfico.",
    "Ajustar profundidad argumentativa a la rúbrica local cuando exista.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna.",
    "Marcar como supuesto cualquier inferencia no visible en la actividad."
  ],
  "quality_gates": [
    "Bloquear propagación automática si la entrada no es JSON parseable.",
    "Validar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o marca de supuesto.",
    "Verificar congruencia entre metadatos de portada y datos curriculares locales.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar que toda cita usada tenga entrada bibliográfica local.",
    "Compilar LaTeX antes de entregar productos finales.",
    "Revisar truncamientos visibles en README y plantilla LaTeX.",
    "Verificar que no queden placeholders literales en rutas, nombres de archivo o bibliografía.",
    "Confirmar disponibilidad de fuentes institucionales antes de usarlas.",
    "Aplicar unión-dedupe sin eliminar reglas útiles previas."
  ],
  "latex_rules": [
    "Conservar clase article en español, letterpaper y oneside según plantilla.",
    "Completar campos de plantilla antes de entregar: actividad, figura docente y fecha.",
    "Mantener tabla de autor con matrícula, semestre, bloque, tipo y créditos correctos.",
    "Preservar coursecode local como LDE-S2B1 salvo indicación institucional distinta.",
    "Evitar comandos rotos o texto truncado en portada y metadatos.",
    "Verificar cierre completo de authortable y macros de portada.",
    "Reparar truncamiento detectado cerca de \\universityname antes de compilar.",
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos o paquetes no estándar sin necesidad editorial o técnica verificable.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico."
  ],
  "bibliography_rules": [
    "Registrar fuentes específicas de actividad en garantias-constitucionales.bib.",
    "Mantener como base las entradas institucionales UnADM ya presentes.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Priorizar fuentes institucionales UnADM y normas jurídicas verificables.",
    "No inventar referencias.",
    "Usar solo fuentes consultadas y verificables.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL.",
    "Agregar normas jurídicas con identificador, emisor y fecha cuando sean usadas.",
    "Incluir nota de consulta o procedencia cuando la fuente sea institucional o local.",
    "Usar claves BibTeX estables y descriptivas.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Corregir menciones al archivo bibliográfico que usen placeholders generados."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar a laterales solo reglas editoriales generales ya validadas.",
    "No propagar datos curriculares específicos fuera de Garantías constitucionales.",
    "No trasladar contenidos temáticos entre materias sin validación local.",
    "Reutilizar controles de identidad, estructura, calidad, LaTeX y bibliografía.",
    "Mantener alerta de salidas no parseables como control institucional.",
    "Aplicar normalización manual si se detecta herencia no estructurada.",
    "Ciclo 1 requiere normalización manual si se reutiliza.",
    "Ciclo 2 requiere normalización manual si se reutiliza.",
    "Ciclo 3 queda normalizado con fuente parseable.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Conservar estrategia progresiva y conservadora."
  ],
  "open_questions": [
    "Falta confirmar consigna local de la primera actividad en Garantías constitucionales.",
    "Falta confirmar producto exacto solicitado por actividad local.",
    "Falta confirmar rúbrica de evaluación local.",
    "Falta definir nombre de figura docente en plantilla destino.",
    "Falta verificar y corregir truncamiento en reporte-garantias-constitucionales.tex.",
    "Falta corregir nombres truncados de archivos en README.md.",
    "Falta reemplazar placeholder bibliográfico en README.md y programa analítico.",
    "Falta confirmar si la fecha debe ser automática con today o fija por entrega.",
    "Falta validar estilo de citación requerido: APA, jurídico mexicano u otro.",
    "Supuesto: la herencia institucional no estructurada se conserva solo como control de riesgo.",
    "Supuesto: fuentes disciplinares de Filosofía del Derecho no aplican al destino.",
    "Confirmar fuentes normativas obligatorias para actividades de Garantías constitucionales."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador ante datos no verificados.",
        "Orientado a práctica profesional."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Entrada canónica por carpeta de materia.",
        "Trazabilidad entre consigna, fuentes y producto.",
        "Normalización estructurada antes de propagar.",
        "Marcado explícito de supuestos."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura destino: Garantías constitucionales.",
        "Semestre 2, bloque 1.",
        "Tipo obligatoria.",
        "8 créditos.",
        "Coursecode local: LDE-S2B1."
      ]
    },
    "essence": [
      "Identidad institucional UnADM.",
      "Integridad académica.",
      "Problema jurídico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Marco normativo o doctrinal.",
      "Análisis propio y postura académica.",
      "Producto solicitado por la planeación.",
      "Conclusión transferible a la práctica jurídica.",
      "Consistencia cita-texto-bib.",
      "Normalización estructurada."
    ],
    "reason_for_being": [
      "Orientar productos académicos de Garantías constitucionales con claridad jurídica.",
      "Transformar la planeación semanal en productos evaluables.",
      "Integrar problema, fuentes, análisis propio y cierre argumentativo.",
      "Evitar contenido sin respaldo o sin marca de supuesto.",
      "Asegurar transferencia profesional de la conclusión jurídica.",
      "Mantener trazabilidad editorial entre consigna, evidencia y archivo final."
    ],
    "style_markers": [
      "Frases precisas y verificables.",
      "Supuestos marcados de forma explícita.",
      "Separación clara entre marco normativo y postura personal.",
      "Cierre con aplicación jurídica concreta.",
      "Metadatos curriculares locales consistentes.",
      "Fuentes citadas con entrada bibliográfica local.",
      "Lenguaje académico sin relleno descriptivo.",
      "No transferencia disciplinar entre materias no equivalentes."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Objetivo puntual.",
      "Marco conceptual delimitado.",
      "Marco normativo o doctrinal verificable.",
      "Contraste entre fuente y postura propia.",
      "Análisis propio sustentado.",
      "Conclusión aplicable a práctica jurídica.",
      "Revisión de coherencia entre pregunta, desarrollo y cierre."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Licenciatura en Derecho",
        "Garantías constitucionales",
        "Ubicación curricular local",
        "Problema jurídico o social",
        "Conceptos jurídicos clave",
        "Marco normativo o doctrinal",
        "Fuentes verificables",
        "Normas jurídicas identificables",
        "Análisis propio",
        "Postura académica",
        "Conclusión transferible",
        "Producto solicitado",
        "Planeación semanal",
        "Integridad académica",
        "Consistencia cita-texto-bib",
        "Normalización estructurada",
        "Propagación recursiva",
        "Control de placeholders",
        "Compilación LaTeX"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La identidad institucional exige trazabilidad y citas verificables."
        },
        {
          "source": "Licenciatura en Derecho",
          "target": "Garantías constitucionales",
          "kind": "develops",
          "justification": "La materia pertenece al contexto curricular local verificado."
        },
        {
          "source": "Ubicación curricular local",
          "target": "Metadatos curriculares locales consistentes",
          "kind": "supports",
          "justification": "Semestre, bloque, tipo y créditos deben coincidir en portada y entrega."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis requiere una pregunta o conflicto delimitado."
        },
        {
          "source": "Conceptos jurídicos clave",
          "target": "Marco normativo o doctrinal",
          "kind": "develops",
          "justification": "Los conceptos organizan la lectura de normas y doctrina."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica requiere sustento legal o doctrinal verificable."
        },
        {
          "source": "Fuentes verificables",
          "target": "Consistencia cita-texto-bib",
          "kind": "supports",
          "justification": "Cada cita debe tener entrada bibliográfica local."
        },
        {
          "source": "Normas jurídicas identificables",
          "target": "Afirmaciones constitucionales sustentadas",
          "kind": "supports",
          "justification": "Las afirmaciones constitucionales no deben quedar sin fundamento."
        },
        {
          "source": "Producto solicitado",
          "target": "Planeación semanal",
          "kind": "depends_on",
          "justification": "El formato final debe responder a la consigna de la semana."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin JSON parseable no hay transferencia confiable."
        },
        {
          "source": "Control de placeholders",
          "target": "Compilación LaTeX",
          "kind": "supports",
          "justification": "Los tokens sin expandir rompen rutas, bibliografía o portada."
        },
        {
          "source": "Compilación LaTeX",
          "target": "Producto final entregable",
          "kind": "supports",
          "justification": "La entrega debe compilar sin errores críticos ni referencias rotas."
        },
        {
          "source": "Filosofía del Derecho",
          "target": "Garantías constitucionales",
          "kind": "contrasts",
          "justification": "La relación es transversal; solo se transfieren abstracciones editoriales."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 2, bloque 1, obligatoria, 8 créditos.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: integridad académica y citas verificables.",
        "Programa analítico local: claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
        "Bib local: unadmSitioWeb.",
        "Bib local: unadmMallaDerecho2024.",
        "Plantilla local: coursecode LDE-S2B1.",
        "Plantilla local: figura docente por definir.",
        "Plantilla local: matrícula, semestre, bloque, tipo y créditos.",
        "README local: placeholders tipo $(@{...}.Slug) pendientes.",
        "README local: nombres truncados de reporte y referencias.",
        "Plantilla local: truncamiento visible cerca de \\universityname.",
        "Memoria origen ciclo 3: normalización JSON y estructura antes de propagar.",
        "Memoria origen ciclo 3: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
        "Memoria origen ciclo 3: no inventar fuentes y validar cita-texto-bib.",
        "Memoria heredada institucional: revisar respuestas no estructuradas antes de aplicarlas."
      ]
    },
    "reinforcement_log": [
      "Ciclo 3 integra origen parseable sin transferir contenido disciplinar.",
      "Se refuerza identidad UnADM con metadatos locales verificados.",
      "Se consolida estructura reusable para actividades futuras.",
      "Se preserva alerta histórica de salidas no JSON parseables.",
      "Se refuerza gate de normalización antes de propagación.",
      "Se mantiene unión-dedupe sin eliminar reglas útiles.",
      "Se prioriza trazabilidad entre consigna, fuente, análisis y cierre.",
      "Se refuerza control LaTeX por truncamientos y placeholders locales.",
      "Se conserva bibliografía local como fuente canónica de citas.",
      "Se dejan abiertos vacíos de consigna, rúbrica y estilo de citación."
    ]
  }
}