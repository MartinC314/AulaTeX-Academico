{
  "summary": [
    "Materia destino consolidada: Garantías constitucionales, Licenciatura en Derecho, UnADM.",
    "Ubicación curricular local verificada: semestre 2, bloque 1, obligatoria, 8 créditos.",
    "Sincronización transversal aplicada desde actividad no equivalente.",
    "Se transfieren solo abstracciones editoriales estables.",
    "No se transfiere contenido disciplinar de Filosofía del Derecho sin validación local.",
    "Se conserva control institucional contra salidas no estructuradas.",
    "Se aplica compresión lossless por unión y deduplicación.",
    "El cerebro editorial mínimo queda activo para reportes y presentaciones.",
    "Supuesto: reglas heredadas se aplican como control editorial, no como contenido temático."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en portada, encabezados y referencias institucionales.",
    "Usar datos locales: Garantías constitucionales, LDE-S2B1, semestre 2, bloque 1.",
    "Registrar tipo obligatoria y 8 créditos cuando aparezcan datos curriculares.",
    "Conservar coherencia con la Licenciatura en Derecho en todo producto.",
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas desde Codex y GPT-Pro como provisionales.",
    "No trasladar contenido disciplinar de otra materia sin validación expresa.",
    "Citar la malla curricular local para ubicación curricular cuando corresponda."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir conceptos, normas, doctrina, datos y postura personal.",
    "Alinear cada entrega al producto solicitado por la planeación semanal.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna.",
    "Mantener separación entre reporte, presentación, programa analítico y bibliografía.",
    "Usar nombres locales verificados: reporte-garantias-constitucionales.tex, presentacion-garantias-constitucionales.tex y garantias-constitucionales.bib.",
    "Mantener referencias-garantias-constitucionales como depósito de fuentes locales.",
    "Evitar cambios de nombres de archivo base salvo requerimiento explícito.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Incluir problema jurídico o social claro desde la introducción.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Desarrollar postura académica argumentada del estudiante.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Vincular afirmaciones relevantes con fuente verificable o norma identificable.",
    "Evitar afirmaciones constitucionales sin fundamento normativo o bibliográfico.",
    "Distinguir hechos, normas, doctrina y opinión propia.",
    "Confirmar que el producto corresponda a la consigna local de actividad.",
    "No asumir que fuentes de otra semana o materia correspondan a la actividad local.",
    "Cerrar con aplicación jurídica concreta."
  ],
  "quality_gates": [
    "Bloquear propagación automática si la entrada no es JSON parseable.",
    "Validar estructura mínima completa antes de aplicar memoria aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Aplicar unión y deduplicación sin eliminar reglas útiles previas.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Verificar congruencia entre portada y datos curriculares locales.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar que toda cita usada tenga entrada bibliográfica local.",
    "Compilar LaTeX antes de entregar productos finales.",
    "Revisar truncamientos visibles en README y plantilla LaTeX.",
    "Verificar que no queden placeholders literales en rutas, nombres de archivo o bibliografía.",
    "Confirmar que fuentes institucionales correspondan a archivos o enlaces disponibles.",
    "Bloquear transferencia temática entre materias si no hay validación disciplinar local."
  ],
  "latex_rules": [
    "Conservar clase article en español, letterpaper y oneside según plantilla.",
    "Completar campos de plantilla antes de entregar: actividad, figura docente y fecha.",
    "Mantener coursecode como LDE-S2B1 salvo indicación institucional distinta.",
    "Mantener tabla de autor con matrícula, semestre, bloque, tipo y créditos correctos.",
    "Evitar comandos rotos o texto truncado en portada y metadatos.",
    "Verificar cierre completo de authortable y macros de portada.",
    "Reparar truncamiento detectado cerca de la macro de portada antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir nombres truncados en README antes de usarlo como índice operativo.",
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "No introducir paquetes nuevos sin necesidad editorial o técnica verificable.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Verificar nombres de archivos del README antes de referenciarlos."
  ],
  "bibliography_rules": [
    "Registrar fuentes específicas de actividad en garantias-constitucionales.bib.",
    "Mantener como base las entradas institucionales UnADM ya presentes.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Priorizar fuentes institucionales UnADM y normas jurídicas verificables.",
    "No inventar referencias.",
    "Usar solo fuentes consultadas y verificables.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL.",
    "Incluir nota de consulta o procedencia cuando la fuente sea institucional o local.",
    "Agregar normas jurídicas con identificador, emisor y fecha cuando sean usadas.",
    "Usar claves BibTeX estables y descriptivas.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Corregir menciones al archivo bibliográfico que usen placeholders generados.",
    "No asumir bibliografía de Filosofía del Derecho como fuente local de Garantías constitucionales."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar arriba y laterales solo reglas editoriales generales ya validadas.",
    "Propagar controles de identidad, estructura, calidad, LaTeX y bibliografía.",
    "Evitar propagar datos curriculares específicos fuera de Garantías constitucionales.",
    "Evitar trasladar contenidos temáticos entre materias sin validación local.",
    "Mantener alerta de JSON no parseable como regla institucional de control.",
    "Etiquetar herencias incompletas con necesidad de normalización manual.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Aplicar estrategia progresiva y conservadora en ciclos siguientes.",
    "Conservar sin regresión todas las reglas útiles ya validadas."
  ],
  "open_questions": [
    "Confirmar consigna local de la primera actividad en Garantías constitucionales.",
    "Confirmar producto exacto solicitado: reporte, presentación u otro formato.",
    "Confirmar rúbrica de evaluación específica.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar si se requiere formato APA, jurídico mexicano u otro estilo de citación.",
    "Confirmar nombre de figura docente en plantilla destino.",
    "Confirmar si la fecha debe ser automática con today o fija por entrega.",
    "Verificar y corregir truncamiento en reporte-garantias-constitucionales.tex.",
    "Corregir nombres truncados de archivos en README.md.",
    "Reemplazar placeholder bibliográfico en README.md y programa analítico.",
    "Confirmar fuentes constitucionales locales antes de crear entradas normativas.",
    "Supuesto: la herencia institucional sin JSON parseable se conserva solo como control de riesgo."
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
        "Normalización estructurada antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Garantías constitucionales.",
        "Semestre 2, bloque 1.",
        "Tipo obligatoria.",
        "8 créditos.",
        "Coursecode local: LDE-S2B1."
      ]
    },
    "essence": [
      "Identidad institucional UnADM.",
      "Problema jurídico o social verificable.",
      "Conceptos y fuentes pertinentes.",
      "Marco normativo o doctrinal delimitado.",
      "Análisis propio con postura académica.",
      "Conclusión transferible a la práctica jurídica.",
      "Consistencia entre texto, citas y bibliografía.",
      "Separación entre control editorial y contenido disciplinar.",
      "Compresión lossless por deduplicación.",
      "Propagación conservadora entre nodos no equivalentes."
    ],
    "reason_for_being": [
      "Orientar productos académicos de Garantías constitucionales con claridad, fundamento jurídico y evidencia.",
      "Transformar la planeación semanal en entregables verificables.",
      "Evitar productos descriptivos sin postura argumentada.",
      "Asegurar que cada conclusión tenga utilidad profesional.",
      "Proteger la integridad editorial frente a fuentes provisionales.",
      "Mantener continuidad institucional entre materias sin mezclar contenidos no validados."
    ],
    "style_markers": [
      "Frases precisas y verificables.",
      "Supuestos marcados de forma explícita.",
      "Problema jurídico visible desde el inicio.",
      "Marco normativo separado de la opinión propia.",
      "Citas explícitas para afirmaciones relevantes.",
      "Conclusión jurídica aplicable.",
      "Metadatos locales consistentes.",
      "Sin placeholders visibles.",
      "Sin referencias inventadas.",
      "Sin transferencia temática no validada."
    ],
    "argumentative_patterns": [
      "Problema inicial breve seguido de objetivo puntual.",
      "Definición de conceptos antes del análisis.",
      "Marco normativo o doctrinal como soporte de la postura.",
      "Distinción entre hechos, normas, doctrina y opinión.",
      "Análisis propio sustentado con fuentes verificables.",
      "Contraste entre afirmación y fundamento.",
      "Cierre que responde a la pregunta guía.",
      "Conclusión transferible a práctica jurídica.",
      "Validación cita-texto-bib antes de entrega.",
      "Adecuación del formato al producto solicitado."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Garantías constitucionales",
        "Licenciatura en Derecho",
        "Ubicación curricular local",
        "Problema jurídico o social",
        "Objetivo de actividad",
        "Conceptos clave",
        "Marco normativo o doctrinal",
        "Fuentes verificables",
        "Análisis propio",
        "Postura académica",
        "Conclusión transferible",
        "Integridad académica",
        "Consistencia cita-texto-bib",
        "Bibliografía local",
        "Normas jurídicas verificables",
        "Normalización estructurada",
        "JSON parseable",
        "Plantilla LaTeX local",
        "Propagación transversal conservadora"
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
          "justification": "La identidad institucional exige trazabilidad, citas verificables y presentación formal."
        },
        {
          "source": "Ubicación curricular local",
          "target": "Garantías constitucionales",
          "kind": "develops",
          "justification": "Los datos de semestre, bloque, tipo y créditos contextualizan la materia destino."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Objetivo de actividad",
          "kind": "supports",
          "justification": "El objetivo se define a partir del problema que activa la entrega."
        },
        {
          "source": "Objetivo de actividad",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis necesita una finalidad explícita para evitar desarrollo descriptivo."
        },
        {
          "source": "Conceptos clave",
          "target": "Marco normativo o doctrinal",
          "kind": "supports",
          "justification": "Los conceptos delimitan la interpretación de normas y doctrina."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Postura académica",
          "kind": "supports",
          "justification": "La postura debe apoyarse en normas, doctrina o fuentes verificables."
        },
        {
          "source": "Fuentes verificables",
          "target": "Consistencia cita-texto-bib",
          "kind": "depends_on",
          "justification": "Cada fuente citada debe existir en la bibliografía local."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión transferible",
          "kind": "develops",
          "justification": "La conclusión sintetiza la postura y la proyecta a la práctica jurídica."
        },
        {
          "source": "Bibliografía local",
          "target": "Fuentes verificables",
          "kind": "supports",
          "justification": "El archivo garantias-constitucionales.bib concentra las fuentes consultadas."
        },
        {
          "source": "Normas jurídicas verificables",
          "target": "Marco normativo o doctrinal",
          "kind": "supports",
          "justification": "Las afirmaciones constitucionales requieren fundamento normativo identificable."
        },
        {
          "source": "Normalización estructurada",
          "target": "JSON parseable",
          "kind": "depends_on",
          "justification": "La propagación confiable requiere salida estructurada y validable."
        },
        {
          "source": "JSON parseable",
          "target": "Propagación transversal conservadora",
          "kind": "supports",
          "justification": "Solo una memoria parseable permite sincronizar nodos sin pérdida ni mezcla temática."
        },
        {
          "source": "Plantilla LaTeX local",
          "target": "Identidad institucional UnADM",
          "kind": "supports",
          "justification": "La portada y metadatos materializan la identidad institucional."
        },
        {
          "source": "Propagación transversal conservadora",
          "target": "Garantías constitucionales",
          "kind": "supports",
          "justification": "La materia recibe patrones editoriales estables sin importar contenido ajeno."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 2, bloque 1, obligatoria, 8 créditos.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: pauta de identidad UnADM, integridad académica y citas verificables.",
        "Programa analítico local: productos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: ejes de problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
        "garantias-constitucionales.bib: entrada unadmSitioWeb.",
        "garantias-constitucionales.bib: entrada unadmMallaDerecho2024.",
        "Plantilla local: reporte-garantias-constitucionales.tex.",
        "Plantilla local: coursecode LDE-S2B1.",
        "Contexto local: README contiene nombres truncados.",
        "Contexto local: README y programa analítico contienen placeholder $(@{...}.Slug).",
        "Contexto local: plantilla LaTeX aparece truncada cerca de macros de portada.",
        "Memoria origen: normalizar salidas no estructuradas antes de propagar.",
        "Memoria origen: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
        "Memoria destino previa: no transferir contenido disciplinar de Filosofía del Derecho sin validación expresa."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin eliminar controles útiles.",
      "Se preservó la identidad curricular local de Garantías constitucionales.",
      "Se reforzó la separación entre reglas editoriales y contenido disciplinar.",
      "Se incorporó el origen parseable solo como abstracción transversal estable.",
      "Se mantuvo la alerta histórica sobre Codex y GPT-Pro como fuente provisional.",
      "Se reforzó el gate de JSON parseable antes de propagación recursiva.",
      "Se consolidó la estructura problema-conceptos-marco-análisis-cierre.",
      "Se reforzó la consistencia cita-texto-bib como requisito de integridad académica.",
      "Se preservaron reglas LaTeX locales sobre plantilla, metadatos y compilación.",
      "Se marcaron pendientes locales sobre truncamientos y placeholders.",
      "Se evitó transferir bibliografía o conceptos específicos de Filosofía del Derecho.",
      "Se actualizó el grafo conceptual con relaciones permitidas y justificadas."
    ]
  }
}