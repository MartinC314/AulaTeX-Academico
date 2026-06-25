{
  "summary": [
    "Memoria de materia consolidada para Derecho financiero y bancario con identidad UnADM.",
    "Se aplica compresión lossless por unión y deduplicación semántica.",
    "Se preservan reglas institucionales válidas sin regresión.",
    "La materia se ubica en Licenciatura en Derecho, semestre 3, bloque 2, obligatoria, 8 créditos.",
    "El destino exige integridad académica, citas verificables, análisis propio y conclusión jurídica transferible.",
    "Se sincronizan solo abstracciones editoriales estables desde Filosofía del Derecho.",
    "Se mantienen vacíos locales como preguntas abiertas con marca de supuesto.",
    "Existen antecedentes de salidas no parseables en JSON desde Codex y GPT-Pro.",
    "README y programa analítico contienen tokens de plantilla y caracteres faltantes por corregir.",
    "El reporte .tex mantiene título y subtítulo de plantilla pendientes de personalizar por actividad."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar Licenciatura en Derecho como programa académico del destino.",
    "Usar datos locales: Derecho financiero y bancario, clave LDE-S3B2, semestre 3, bloque 2.",
    "Conservar tipo obligatoria y 8 créditos según README local.",
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Conservar autor Martin Jonathan de la Cruz y matrícula ES2611202040 según .tex local.",
    "Conservar localización Roma Norte, Ciudad de México salvo lineamiento contrario.",
    "Marcar como supuesto cualquier dato no confirmado, especialmente figura docente o grupo.",
    "Tratar fuentes heredadas de motor como provisionales y auditables.",
    "Citar malla-curricular-derecho-unadm.pdf como fuente de ubicación curricular."
  ],
  "structure_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Separar conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por la planeación semanal.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener coherencia entre README, programa analítico, .tex y .bib.",
    "Corregir artefactos de plantilla en README y programa analítico.",
    "Expandir el token del archivo .bib a derecho-financiero-y-bancario.bib.",
    "Corregir nombres de archivos con caracteres faltantes antes de referenciarlos.",
    "No eliminar reglas útiles previas; solo agregar mejoras verificables."
  ],
  "activity_rules": [
    "Delimitar el problema financiero, bancario, jurídico o social de cada actividad.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Usar norma, doctrina o datos pertinentes al tema financiero y bancario.",
    "Incluir postura argumentada del estudiante, no solo descripción.",
    "Separar descripción conceptual, análisis propio y conclusión jurídica.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Adaptar el producto a la planeación semanal confirmada.",
    "No asumir fuentes de otras semanas sin confirmación local.",
    "Marcar como supuesto cualquier elemento no visible en la consigna."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Validar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar trazabilidad de cada regla a contexto local o memoria heredada.",
    "Comprobar que cada mejora agregada sea verificable.",
    "Bloquear campos obligatorios vacíos sin marca de supuesto.",
    "Validar deduplicación semántica antes de guardar memoria.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que el producto corresponda a la consigna vigente.",
    "Revisar compilación LaTeX sin errores críticos ni referencias rotas."
  ],
  "latex_rules": [
    "Mantener documentclass article en español, letterpaper y oneside salvo instrucción contraria.",
    "Conservar macros de identidad académica en el encabezado del .tex.",
    "Sincronizar título, subtítulo, materia y actividad entre portada y contenido.",
    "Reemplazar título y subtítulo de plantilla por los de la actividad real antes de entregar.",
    "Completar Figura docente con dato real o etiqueta explícita de supuesto.",
    "Revisar que la tabla de identificación compile sin celdas abiertas.",
    "Evitar romper comandos y rutas en portada, tablas y referencias.",
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens sin expandir en README, programa analítico y nombres de archivo.",
    "Verificar nombres de archivos del README antes de referenciarlos."
  ],
  "bibliography_rules": [
    "Usar derecho-financiero-y-bancario.bib como archivo bibliográfico canónico.",
    "Registrar fuentes específicas de actividad en el .bib de la materia.",
    "Priorizar fuentes institucionales UnADM y documentos curriculares locales cuando apliquen.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "No inventar fuentes ni metadatos bibliográficos.",
    "Agregar entradas BibTeX solo con fuente verificable.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Incluir fecha de consulta en referencias web.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Validar correspondencia entre citas en texto y claves BibTeX."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar a nivel materia reglas generales de identidad, estructura y bibliografía.",
    "Propagar lateralmente solo reglas independientes de una asignatura o actividad específica.",
    "Compartir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferir redacción literal de actividades ajenas.",
    "Mantener método unión-dedupe con compresión lossless.",
    "Etiquetar origen de reglas heredadas para auditoría de no regresión.",
    "Aplicar normalización manual si reaparece salida no estructurada.",
    "Mantener vacíos de contexto local como preguntas abiertas."
  ],
  "open_questions": [
    "Confirmar nombre real de la figura docente.",
    "Confirmar si el grupo debe aparecer en la tabla de identificación.",
    "Definir formato obligatorio de citación para la materia; supuesto: no definido aún.",
    "Validar si la localización de portada debe mantenerse o actualizarse por lineamiento oficial.",
    "Confirmar planeación semanal vigente antes de generar actividades.",
    "Confirmar número real de actividad para sustituir Actividad X en el subtítulo.",
    "Confirmar producto exacto solicitado por cada consigna.",
    "Confirmar rúbrica de evaluación específica.",
    "Verificar si los nombres de archivos del README deben corregirse manualmente o regenerarse.",
    "Confirmar fuentes obligatorias de cada semana."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Sobrio y verificable.",
        "Argumentativo con criterio propio.",
        "Orientado a práctica profesional."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Entrada canónica por carpeta de materia.",
        "Trazabilidad documental entre README, programa, .tex y .bib.",
        "Supuestos marcados de forma explícita.",
        "No regresión de reglas útiles previas."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho financiero y bancario.",
        "Clave local: LDE-S3B2.",
        "Semestre 3, bloque 2.",
        "Materia obligatoria de 8 créditos.",
        "Fuente curricular institucional: malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Identidad institucional UnADM.",
      "Problema jurídico o social delimitado.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable.",
      "Análisis jurídico propio.",
      "Postura académica argumentada.",
      "Conclusión transferible a la práctica jurídica.",
      "Consistencia entre .tex y .bib.",
      "Normalización estructurada antes de propagar."
    ],
    "reason_for_being": [
      "Orientar productos académicos de Derecho financiero y bancario con claridad, fundamento jurídico y evidencia.",
      "Transformar la planeación semanal en reportes, presentaciones o productos visuales verificables.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Asegurar que cada entrega tenga utilidad profesional y no sea solo descriptiva.",
      "Preservar memoria editorial institucional sin perder especificidad local."
    ],
    "style_markers": [
      "Frases directas y verificables.",
      "Supuestos explícitos cuando falte confirmación.",
      "Fuentes no inventadas.",
      "Citas trazables al .bib canónico.",
      "Portada y metadatos institucionales consistentes.",
      "Conceptos jurídicos conectados con práctica profesional.",
      "Conclusión con criterio propio.",
      "Corrección preventiva de plantillas y tokens."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Objetivo puntual antes del desarrollo.",
      "Marco conceptual y normativo delimitado.",
      "Evidencia verificable como soporte.",
      "Análisis propio diferenciado de la descripción.",
      "Contraste entre norma, doctrina y caso cuando aplique.",
      "Cierre con implicación jurídica práctica.",
      "Coherencia entre pregunta guía, desarrollo y conclusión."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM.",
        "Licenciatura en Derecho.",
        "Derecho financiero y bancario.",
        "Ubicación curricular.",
        "Malla curricular de Derecho.",
        "Problema jurídico o social.",
        "Conceptos jurídicos clave.",
        "Marco normativo.",
        "Doctrina jurídica.",
        "Evidencia verificable.",
        "Análisis jurídico propio.",
        "Postura académica.",
        "Conclusión transferible.",
        "Planeación semanal.",
        "Producto académico.",
        "Reporte.",
        "Presentación.",
        "Bibliografía canónica.",
        "Consistencia .tex-.bib.",
        "Normalización estructurada.",
        "Propagación recursiva.",
        "No regresión editorial."
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
          "justification": "La identidad institucional exige trazabilidad, tono formal y fuentes verificables."
        },
        {
          "source": "Malla curricular de Derecho",
          "target": "Ubicación curricular",
          "kind": "supports",
          "justification": "El README local usa la malla curricular como fuente de semestre, bloque, tipo y créditos."
        },
        {
          "source": "Carpeta de materia",
          "target": "Producto académico",
          "kind": "supports",
          "justification": "La pauta local define la carpeta como punto de entrada canónico."
        },
        {
          "source": "Planeación semanal",
          "target": "Producto académico",
          "kind": "develops",
          "justification": "El programa analítico indica transformar la planeación en reportes, presentaciones o productos visuales."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Análisis jurídico propio",
          "kind": "develops",
          "justification": "El problema delimita el eje argumentativo de la entrega."
        },
        {
          "source": "Conceptos jurídicos clave",
          "target": "Marco normativo",
          "kind": "depends_on",
          "justification": "La explicación normativa requiere delimitar conceptos antes del análisis."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión profesional debe derivar de fuentes comprobables."
        },
        {
          "source": "Bibliografía canónica",
          "target": "Consistencia .tex-.bib",
          "kind": "supports",
          "justification": "Las citas del texto deben corresponder a entradas del archivo .bib local."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin JSON parseable no hay transferencia segura de memoria."
        },
        {
          "source": "No regresión editorial",
          "target": "Propagación recursiva",
          "kind": "supports",
          "justification": "La propagación debe conservar reglas útiles previas y solo agregar mejoras verificables."
        },
        {
          "source": "Filosofía del Derecho",
          "target": "Derecho financiero y bancario",
          "kind": "contrasts",
          "justification": "Son nodos no equivalentes; solo comparten abstracciones editoriales transversales."
        },
        {
          "source": "Estructura problema-conceptos-evidencia-análisis-cierre",
          "target": "Derecho financiero y bancario",
          "kind": "develops",
          "justification": "El patrón editorial transversal se adapta al contexto financiero y bancario sin copiar redacción literal."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 3, bloque 2, obligatoria, 8 créditos.",
        "README local: fuente curricular UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: cada actividad conserva identidad UnADM, integridad académica, citas verificables y conclusión jurídica.",
        "Programa analítico local: productos académicos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: planeación transformada en reportes, presentaciones y productos visuales.",
        "Programa analítico local: ejes de problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
        "derecho-financiero-y-bancario.bib: entrada unadmSitioWeb.",
        "derecho-financiero-y-bancario.bib: entrada unadmMallaDerecho2024.",
        "reporte local .tex: autor Martin Jonathan de la Cruz.",
        "reporte local .tex: matrícula ES2611202040.",
        "reporte local .tex: clave LDE-S3B2.",
        "Memoria heredada: revisar respuesta no estructurada antes de aplicar aguas abajo.",
        "Memoria transversal: bloquear propagación si la salida no es JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 19: se consolidó memoria de materia con unión-dedupe.",
      "Ciclo 19: se preservó identidad UnADM y ubicación curricular local.",
      "Ciclo 19: se transfirieron solo abstracciones editoriales estables desde Filosofía del Derecho.",
      "Ciclo 19: se evitó importar fuentes y conceptos específicos no equivalentes.",
      "Ciclo 19: se reforzó gate de JSON parseable antes de propagación recursiva.",
      "Ciclo 19: se reforzó consistencia entre README, programa analítico, .tex y .bib.",
      "Ciclo 19: se mantuvieron preguntas abiertas para datos locales no confirmados.",
      "Ciclo 19: se normalizaron duplicados semánticos sin eliminar reglas útiles."
    ]
  }
}