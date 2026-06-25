{
  "summary": [
    "Materia destino con plantilla LaTeX, programa analítico y bibliografía local activos.",
    "Contexto local verificado: Garantías constitucionales, Licenciatura en Derecho, UnADM.",
    "Ubicación curricular verificada: semestre 2, bloque 1, obligatoria, 8 créditos.",
    "Se sincroniza transversalmente desde una actividad no equivalente.",
    "Se transfieren solo abstracciones editoriales estables.",
    "No se transfiere contenido disciplinar de Filosofía del Derecho sin validación local.",
    "Se conserva alerta institucional sobre herencias no estructuradas previas.",
    "Se aplica compresión lossless por unión y deduplicación.",
    "Supuesto: reglas heredadas se usan como control editorial, no como contenido temático."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en portada, encabezados y referencias institucionales.",
    "Usar datos locales: Garantías constitucionales, LDE-S2B1, semestre 2, bloque 1.",
    "Registrar tipo obligatoria y 8 créditos cuando aparezcan datos curriculares.",
    "Conservar coherencia con la Licenciatura en Derecho en todo producto.",
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas desde Codex y GPT-Pro como provisionales.",
    "No trasladar contenido disciplinar entre materias sin validación expresa.",
    "Citar malla-curricular-derecho-unadm.pdf para ubicación curricular."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por la planeación semanal.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna.",
    "Mantener separación entre reporte, presentación, programa analítico y referencias.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Usar nombres locales verificados: reporte-garantias-constitucionales.tex, presentacion-garantias-constitucionales.tex y garantias-constitucionales.bib.",
    "Preservar el programa analítico como guía editorial de la asignatura.",
    "Mantener referencias-garantias-constitucionales como depósito de fuentes locales.",
    "Corregir nombres truncados en README antes de usarlo como índice operativo."
  ],
  "activity_rules": [
    "Incluir problema jurídico o social claro desde la introducción.",
    "Distinguir hechos, normas, doctrina, datos y postura personal.",
    "Vincular afirmaciones relevantes con fuente verificable o norma identificable.",
    "Sustentar afirmaciones con cita explícita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Evitar afirmaciones constitucionales sin fundamento normativo o bibliográfico.",
    "Confirmar que el producto corresponda a la consigna local.",
    "Cerrar con conclusión aplicable a la práctica profesional."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de propagar memoria.",
    "Bloquear propagación automática si la entrada no es estructurada.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Verificar congruencia entre portada y datos curriculares locales.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar que toda cita usada tenga entrada bibliográfica local.",
    "Compilar LaTeX antes de entregar productos finales.",
    "Verificar que no queden placeholders en rutas, nombres de archivo o bibliografía.",
    "Revisar truncamientos visibles en README y plantilla LaTeX.",
    "Aplicar unión-dedupe sin eliminar reglas útiles previas."
  ],
  "latex_rules": [
    "Conservar clase article en español, letterpaper y oneside según plantilla.",
    "Completar campos de plantilla antes de entregar: actividad, figura docente y fecha.",
    "Mantener tabla de autor con matrícula, semestre, bloque, tipo y créditos correctos.",
    "Preservar coursecode como LDE-S2B1 salvo indicación institucional distinta.",
    "Usar codificación y acentos correctos en .tex y .bib.",
    "Evitar comandos no estándar sin justificación editorial o técnica verificable.",
    "No introducir paquetes nuevos sin necesidad verificable.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Reparar truncamiento cerca de la macro de portada antes de compilar.",
    "Verificar cierre completo de authortable y universityname."
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
    "Corregir menciones bibliográficas que usen placeholders generados.",
    "Distinguir bibliografía base de bibliografía específica de actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar a nodos laterales solo reglas editoriales generales validadas.",
    "No propagar datos curriculares específicos fuera de Garantías constitucionales.",
    "No trasladar contenidos temáticos de actividad ajena sin validación local.",
    "Mantener alerta de JSON no parseable como control institucional.",
    "Reutilizar reglas de identidad, estructura, calidad, LaTeX y bibliografía.",
    "Aplicar normalización manual si se detecta salida no estructurada.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Conservar estrategia progresiva y conservadora.",
    "Ciclos 1, 2 y 3 requieren normalización manual si se reutilizan.",
    "Ciclo 6 refuerza grafo conceptual sin añadir fuentes no verificadas."
  ],
  "open_questions": [
    "Falta confirmar consigna local de la primera actividad en Garantías constitucionales.",
    "Falta confirmar producto exacto solicitado: reporte, presentación u otro formato.",
    "Falta confirmar rúbrica de evaluación específica.",
    "Falta confirmar fuentes obligatorias de la semana correspondiente.",
    "Falta definir nombre de figura docente en plantilla destino.",
    "Falta verificar y corregir truncamiento en reporte-garantias-constitucionales.tex.",
    "Falta corregir nombres truncados de archivos en README.md.",
    "Falta reemplazar placeholder bibliográfico en README.md y programa analítico.",
    "Falta confirmar si la fecha debe ser automática con today o fija por entrega.",
    "Falta validar si se requiere APA, estilo jurídico mexicano u otro estilo de citación.",
    "Supuesto: la herencia institucional no estructurada se conserva solo como control de riesgo."
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
        "Marcado explícito de supuestos.",
        "Separación entre memoria local y herencia transversal."
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
      "Orientar productos académicos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
      "Transformar la planeación semanal en productos verificables.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Preservar identidad UnADM y coherencia curricular.",
      "Evitar propagación de contenido no validado entre materias."
    ],
    "style_markers": [
      "Frases precisas y verificables.",
      "Supuestos marcados explícitamente.",
      "Separación clara entre marco normativo y postura personal.",
      "Citas visibles para afirmaciones relevantes.",
      "Cierre con aplicación jurídica concreta.",
      "Metadatos curriculares locales consistentes.",
      "Nombres de archivo estables.",
      "Sin placeholders visibles.",
      "Sin contenido disciplinar heredado sin validación."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Objetivo puntual.",
      "Conceptos clave delimitados.",
      "Marco normativo o doctrinal verificable.",
      "Análisis propio sustentado.",
      "Contraste entre norma, doctrina y postura personal.",
      "Coherencia entre pregunta guía, desarrollo y conclusión.",
      "Conclusión aplicable a práctica jurídica.",
      "Formato final alineado con planeación semanal."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Licenciatura en Derecho",
        "Garantías constitucionales",
        "Ubicación curricular",
        "Malla curricular de Derecho",
        "Problema jurídico o social",
        "Conceptos jurídicos",
        "Normas jurídicas",
        "Doctrina",
        "Datos pertinentes",
        "Marco normativo o doctrinal",
        "Análisis propio",
        "Postura académica",
        "Producto solicitado",
        "Conclusión transferible",
        "Integridad académica",
        "Citas verificables",
        "Bibliografía local",
        "Consistencia cita-texto-bib",
        "Normalización estructurada",
        "Propagación recursiva",
        "Herencia transversal",
        "Supuesto editorial",
        "Plantilla LaTeX local",
        "Placeholder generado",
        "Truncamiento de plantilla"
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
          "justification": "La pauta local exige identidad UnADM, citas verificables e integridad académica."
        },
        {
          "source": "Licenciatura en Derecho",
          "target": "Garantías constitucionales",
          "kind": "develops",
          "justification": "El README ubica la materia dentro de la Licenciatura en Derecho."
        },
        {
          "source": "Malla curricular de Derecho",
          "target": "Ubicación curricular",
          "kind": "supports",
          "justification": "El README cita la malla curricular como fuente de semestre, bloque, tipo y créditos."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis requiere una pregunta o conflicto definido desde la introducción."
        },
        {
          "source": "Conceptos jurídicos",
          "target": "Marco normativo o doctrinal",
          "kind": "develops",
          "justification": "Los conceptos delimitan el marco que sustenta el desarrollo."
        },
        {
          "source": "Normas jurídicas",
          "target": "Marco normativo o doctrinal",
          "kind": "supports",
          "justification": "Las afirmaciones constitucionales deben tener fundamento normativo identificable."
        },
        {
          "source": "Doctrina",
          "target": "Análisis propio",
          "kind": "supports",
          "justification": "La doctrina ayuda a sostener una postura académica no descriptiva."
        },
        {
          "source": "Citas verificables",
          "target": "Consistencia cita-texto-bib",
          "kind": "depends_on",
          "justification": "Toda cita usada debe corresponder a una entrada bibliográfica local."
        },
        {
          "source": "Bibliografía local",
          "target": "Consistencia cita-texto-bib",
          "kind": "supports",
          "justification": "garantias-constitucionales.bib funciona como registro local de fuentes."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica requiere sustento legal o doctrinal verificable."
        },
        {
          "source": "Producto solicitado",
          "target": "Plantilla LaTeX local",
          "kind": "depends_on",
          "justification": "El formato final debe ajustarse a la consigna y a la plantilla disponible."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin JSON parseable no hay transferencia confiable."
        },
        {
          "source": "Herencia transversal",
          "target": "Supuesto editorial",
          "kind": "supports",
          "justification": "Las reglas no verificadas localmente deben marcarse como provisionales."
        },
        {
          "source": "Placeholder generado",
          "target": "Plantilla LaTeX local",
          "kind": "contrasts",
          "justification": "Los placeholders visibles contradicen una entrega compilable y final."
        },
        {
          "source": "Truncamiento de plantilla",
          "target": "Plantilla LaTeX local",
          "kind": "contrasts",
          "justification": "El truncamiento detectado impide compilar y debe corregirse."
        }
      ],
      "evidence": [
        "README.md: Materia de la Licenciatura en Derecho de la UnADM.",
        "README.md: Semestre 2, bloque 1, obligatoria, 8 créditos.",
        "README.md: Fuente curricular malla-curricular-derecho-unadm.pdf.",
        "README.md: La carpeta funciona como punto de entrada canónico.",
        "README.md: Cada actividad debe conservar identidad UnADM e integridad académica.",
        "README.md: Se requieren citas verificables y conclusión jurídica con criterio propio.",
        "programa-analitico-garantias-constitucionales.md: productos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "programa-analitico-garantias-constitucionales.md: integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
        "garantias-constitucionales.bib: entrada unadmSitioWeb.",
        "garantias-constitucionales.bib: entrada unadmMallaDerecho2024.",
        "reporte-garantias-constitucionales.tex: plantilla article en español, letterpaper y oneside.",
        "reporte-garantias-constitucionales.tex: coursecode LDE-S2B1.",
        "reporte-garantias-constitucionales.tex: figura docente pendiente.",
        "reporte-garantias-constitucionales.tex: truncamiento visible cerca de universityname.",
        "Memoria origen: bloquear propagación si la salida no es JSON parseable.",
        "Memoria origen: sustentar afirmaciones con fuentes verificables y cita explícita.",
        "Memoria origen: no inventar referencias.",
        "Memoria origen: cierre jurídico transferible a práctica profesional."
      ]
    },
    "reinforcement_log": [
      "Ciclo 6 consolida memoria destino por unión-dedupe.",
      "Se preservan reglas locales verificadas de Garantías constitucionales.",
      "Se incorporan solo patrones editoriales transversales del origen.",
      "Se excluye contenido disciplinar específico de Filosofía del Derecho.",
      "Se refuerza control de JSON parseable antes de propagación.",
      "Se refuerza consistencia entre cita, texto y .bib.",
      "Se refuerza reparación de placeholders y truncamientos locales.",
      "Se mantiene estrategia progresiva y conservadora."
    ]
  }
}