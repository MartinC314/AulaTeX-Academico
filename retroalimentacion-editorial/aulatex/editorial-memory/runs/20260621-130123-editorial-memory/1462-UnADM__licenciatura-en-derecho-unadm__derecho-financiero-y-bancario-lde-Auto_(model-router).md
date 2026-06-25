{
  "summary": [
    "Se consolida memoria de materia para Derecho financiero y bancario.",
    "Se preserva identidad UnADM con compresión unión-dedupe.",
    "Se transfieren solo abstracciones editoriales estables desde Filosofía del Derecho.",
    "Se conserva ubicación curricular local: semestre 3, bloque 2, obligatoria, 8 créditos.",
    "Se refuerzan ejes transversales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se mantienen reglas de normalización estructurada antes de propagar.",
    "Se detectan artefactos de plantilla en README, programa analítico y .tex.",
    "Se mantienen vacíos locales como preguntas abiertas con marca de supuesto."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, tono y metadatos.",
    "Usar la Licenciatura en Derecho como programa académico.",
    "Usar datos locales: Derecho financiero y bancario, clave LDE-S3B2, semestre 3, bloque 2.",
    "Conservar tipo obligatoria y 8 créditos según README local.",
    "Citar malla-curricular-derecho-unadm.pdf como fuente curricular.",
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Conservar autor Martin Jonathan de la Cruz y matrícula ES2611202040 según .tex local.",
    "Conservar Roma Norte, Ciudad de México salvo lineamiento contrario.",
    "Marcar como supuesto cualquier dato no visible o no confirmado.",
    "Marcar figura docente y grupo como supuestos hasta confirmación.",
    "Tratar fuentes heredadas de motor como provisionales y auditables.",
    "No transferir contenido doctrinal específico de Filosofía del Derecho al destino sin consigna local."
  ],
  "structure_rules": [
    "Alinear cada entrega al flujo: problema, conceptos o normas, producto, análisis propio y conclusión.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Separar conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el formato al producto solicitado por la planeación semanal.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener coherencia entre README, programa analítico, .tex y .bib.",
    "Corregir artefactos de plantilla en nombres de archivos.",
    "Expandir el token de plantilla al archivo derecho-financiero-y-bancario.bib.",
    "No eliminar reglas previas válidas; agregar solo mejoras verificables.",
    "Distinguir reglas de materia de reglas de actividad específica."
  ],
  "activity_rules": [
    "Confirmar consigna antes de crear una actividad específica.",
    "Delimitar el problema jurídico o social de cada actividad.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Usar norma, doctrina o datos pertinentes al tema financiero y bancario.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Adaptar profundidad y formato a la rúbrica disponible.",
    "No asumir fuentes de otra semana o materia como aplicables.",
    "Separar descripción conceptual, análisis propio y conclusión jurídica.",
    "Cerrar con postura jurídica propia aplicable a la práctica profesional."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar y normalizar salidas no estructuradas antes de reutilizarlas.",
    "Validar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar trazabilidad de cada regla a contexto local o memoria heredada.",
    "Bloquear campos obligatorios vacíos sin marca de supuesto.",
    "Validar deduplicación semántica antes de guardar memoria.",
    "Comprobar que toda mejora sea verificable.",
    "No inventar fuentes, citas ni metadatos.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Comprobar correspondencia entre producto y consigna confirmada.",
    "Revisar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Evitar regresiones respecto de reglas útiles previas."
  ],
  "latex_rules": [
    "Mantener documentclass article en spanish, letterpaper, oneside salvo instrucción contraria.",
    "Conservar macros de identidad académica en el encabezado.",
    "Sincronizar título, subtítulo, materia y actividad real.",
    "Reemplazar Actividad X antes de entregar.",
    "Reemplazar título de plantilla por título de actividad concreta.",
    "Completar Figura docente con dato real o supuesto explícito.",
    "Revisar que la tabla de identificación compile sin celdas abiertas.",
    "Evitar romper comandos y rutas en portada, tablas y referencias.",
    "Usar codificación y acentos correctos en español.",
    "Corregir caracteres anómalos en rutas o nombres de archivo.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug).",
    "Compilar sin errores críticos ni referencias rotas.",
    "Mantener claves BibTeX estables."
  ],
  "bibliography_rules": [
    "Usar derecho-financiero-y-bancario.bib como archivo bibliográfico canónico.",
    "Registrar fuentes específicas de actividad en el .bib de la materia.",
    "Priorizar fuentes institucionales UnADM y documentos curriculares locales cuando apliquen.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Agregar entradas BibTeX solo con fuente verificable.",
    "No inventar referencias ni metadatos bibliográficos.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL.",
    "Incluir fecha de consulta en referencias web.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Validar consistencia entre claves citadas y entradas del .bib.",
    "No asumir bibliografía de Filosofía del Derecho como aplicable al destino.",
    "Citar la malla curricular local para ubicación curricular."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Aplicar compresión unión-dedupe con pérdida cero.",
    "Propagar lateralmente solo abstracciones independientes de actividad específica.",
    "Propagar a nivel materia identidad, estructura, calidad y bibliografía general.",
    "No propagar redacción literal entre materias no equivalentes.",
    "Etiquetar reglas heredadas para auditoría de no regresión.",
    "Mantener vacíos de contexto como preguntas abiertas.",
    "Aplicar normalización manual si reaparece salida no estructurada.",
    "Reutilizar reglas institucionales sin reducir especificidad local.",
    "Evitar transferir citas doctrinales específicas sin evidencia local.",
    "Reforzar el grafo conceptual con relaciones verificables.",
    "Ciclo 14 mantiene estrategia progresiva y conservadora."
  ],
  "open_questions": [
    "Confirmar nombre real de la figura docente.",
    "Confirmar si el grupo debe aparecer en la tabla de identificación.",
    "Definir formato obligatorio de citación para la materia.",
    "Supuesto: no existe formato de citación confirmado aún.",
    "Confirmar planeación semanal vigente antes de generar actividades.",
    "Confirmar número real de actividad para sustituir Actividad X.",
    "Confirmar rúbrica específica para ajustar profundidad argumentativa.",
    "Validar si la localización de portada debe mantenerse.",
    "Verificar si los nombres de archivos del README deben corregirse manualmente.",
    "Confirmar si habrá carpeta de referencias específica por actividad.",
    "Confirmar fuentes obligatorias de cada semana.",
    "Confirmar si el reporte base será plantilla única o derivará por actividad."
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
        "Trazabilidad entre README, programa, .tex y .bib.",
        "Supuestos marcados de forma explícita.",
        "No regresión de reglas útiles previas."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho financiero y bancario.",
        "Clave local: LDE-S3B2.",
        "Semestre 3, bloque 2.",
        "Materia obligatoria de 8 créditos.",
        "Fuente curricular: malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Identidad institucional UnADM.",
      "Integridad académica.",
      "Evidencia verificable.",
      "Problema jurídico o social delimitado.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Análisis jurídico propio.",
      "Conclusión transferible a la práctica jurídica.",
      "Consistencia entre plantilla, bibliografía y consigna.",
      "Normalización estructurada antes de propagación.",
      "No invención de fuentes."
    ],
    "reason_for_being": [
      "Orientar productos académicos de Derecho financiero y bancario.",
      "Transformar la planeación semanal en entregables verificables.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Conservar identidad UnADM con rigor jurídico.",
      "Producir conclusiones aplicables a la práctica profesional.",
      "Sostener trazabilidad documental entre archivos locales.",
      "Prevenir errores por plantillas incompletas.",
      "Facilitar propagación segura de reglas editoriales."
    ],
    "style_markers": [
      "Frases directas y accionables.",
      "Supuestos explícitos.",
      "Citas verificables.",
      "Sin fuentes inventadas.",
      "Separación clara entre descripción y análisis.",
      "Cierre jurídico con criterio propio.",
      "Coherencia entre título, subtítulo y actividad.",
      "Deduplicación semántica sin recorte útil.",
      "Tono institucional sin exceso retórico.",
      "Transferencia profesional visible."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Objetivo puntual antes del desarrollo.",
      "Marco conceptual y normativo delimitado.",
      "Evidencia verificable como soporte.",
      "Análisis propio diferenciado del resumen.",
      "Contraste entre norma, doctrina y caso cuando aplique.",
      "Conclusión derivada del desarrollo.",
      "Implicación práctica para el ejercicio jurídico.",
      "Correspondencia entre consigna y producto.",
      "Citas en texto sincronizadas con .bib."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM.",
        "Licenciatura en Derecho.",
        "Derecho financiero y bancario.",
        "Clave LDE-S3B2.",
        "Semestre 3, bloque 2.",
        "Materia obligatoria de 8 créditos.",
        "Malla curricular de Derecho.",
        "Carpeta de materia como entrada canónica.",
        "Planeación semanal.",
        "Producto académico.",
        "Problema jurídico o social.",
        "Conceptos jurídicos pertinentes.",
        "Marco normativo o doctrinal.",
        "Evidencia verificable.",
        "Citas explícitas.",
        "Archivo derecho-financiero-y-bancario.bib.",
        "Análisis jurídico propio.",
        "Conclusión jurídica transferible.",
        "Normalización estructurada.",
        "JSON parseable.",
        "Artefactos de plantilla.",
        "Supuestos explícitos.",
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
          "justification": "La pauta local exige identidad UnADM, citas verificables y conclusión jurídica."
        },
        {
          "source": "Malla curricular de Derecho",
          "target": "Semestre 3, bloque 2",
          "kind": "supports",
          "justification": "El README local declara la malla como fuente de ubicación curricular."
        },
        {
          "source": "Malla curricular de Derecho",
          "target": "Materia obligatoria de 8 créditos",
          "kind": "supports",
          "justification": "El README local registra tipo y créditos con fuente curricular."
        },
        {
          "source": "Carpeta de materia como entrada canónica",
          "target": "Trazabilidad entre README, programa, .tex y .bib",
          "kind": "develops",
          "justification": "La pauta editorial local define la carpeta como punto de entrada."
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
          "source": "Marco normativo o doctrinal",
          "target": "Evidencia verificable",
          "kind": "depends_on",
          "justification": "Las afirmaciones jurídicas deben apoyarse en normas, doctrina o datos pertinentes."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión profesional debe derivar de fuentes comprobables."
        },
        {
          "source": "Citas explícitas",
          "target": "Archivo derecho-financiero-y-bancario.bib",
          "kind": "depends_on",
          "justification": "Las citas del texto deben corresponder a entradas bibliográficas locales."
        },
        {
          "source": "Normalización estructurada",
          "target": "JSON parseable",
          "kind": "depends_on",
          "justification": "La propagación segura requiere salida estructurada y parseable."
        },
        {
          "source": "Artefactos de plantilla",
          "target": "Compilación LaTeX",
          "kind": "contrasts",
          "justification": "Tokens sin expandir y caracteres anómalos pueden romper rutas y referencias."
        },
        {
          "source": "Supuestos explícitos",
          "target": "No invención de fuentes",
          "kind": "supports",
          "justification": "Marcar incertidumbre evita presentar datos no verificados como hechos."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 3, bloque 2, obligatoria, 8 créditos.",
        "README local: fuente curricular malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: identidad UnADM, integridad académica, citas verificables y conclusión jurídica.",
        "Programa analítico local: productos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: planeación transformada en reportes, presentaciones y productos visuales.",
        "Programa analítico local: ejes de problema, conceptos, producto, análisis propio y conclusión.",
        "Bibliografía local: entradas unadmSitioWeb y unadmMallaDerecho2024.",
        ".tex local: autor Martin Jonathan de la Cruz y matrícula ES2611202040.",
        ".tex local: título y subtítulo de plantilla pendientes.",
        "Memoria heredada: revisar salidas no estructuradas antes de aplicar aguas abajo.",
        "Memoria origen: bloquear propagación si la salida no es JSON parseable.",
        "Transferencia transversal: solo abstracciones estables entre nodos no equivalentes."
      ]
    },
    "reinforcement_log": [
      "Ciclo 14 consolida destino como materia, no como actividad.",
      "Se deduplican variantes semánticas de reglas institucionales.",
      "Se conserva ubicación curricular local verificada.",
      "Se refuerza trazabilidad README-programa-.tex-.bib.",
      "Se preserva regla de JSON parseable antes de propagación.",
      "Se evita transferir citas doctrinales específicas de Filosofía del Derecho.",
      "Se conserva el flujo editorial problema-evidencia-análisis-conclusión.",
      "Se agregan gates para plantillas sin expandir y campos pendientes.",
      "Se mantienen supuestos abiertos sin inventar datos.",
      "Se preserva estrategia progresiva y conservadora."
    ]
  }
}