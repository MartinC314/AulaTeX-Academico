{
  "summary": [
    "Se consolida memoria editorial de materia para Derecho financiero y bancario con identidad UnADM.",
    "Se sincroniza ADN transversal desde Filosofía del Derecho solo como abstracción estable.",
    "Se preservan reglas institucionales útiles sin regresión.",
    "La materia destino se ubica en Licenciatura en Derecho, semestre 3, bloque 2, obligatoria, 8 créditos.",
    "La carpeta de materia funciona como punto de entrada canónico.",
    "El flujo editorial base es problema, conceptos o normas, evidencia, análisis propio y conclusión jurídica transferible.",
    "Se mantienen antecedentes de salidas no parseables desde Codex y GPT-Pro como riesgos de normalización.",
    "README y programa analítico contienen tokens o artefactos de plantilla que requieren corrección local.",
    "El .tex local conserva metadatos de plantilla pendientes de personalizar por actividad."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar la Licenciatura en Derecho como programa académico.",
    "Usar datos locales de materia: Derecho financiero y bancario, clave LDE-S3B2, semestre 3, bloque 2.",
    "Conservar tipo obligatoria y 8 créditos según README local.",
    "Citar la malla curricular local como fuente de ubicación curricular.",
    "Usar la carpeta de materia como entrada canónica.",
    "Conservar autor Martin Jonathan de la Cruz y matrícula ES2611202040 según .tex local.",
    "Conservar ubicación Roma Norte, Ciudad de México salvo lineamiento contrario.",
    "Marcar como supuesto cualquier dato no confirmado por consigna o archivo local.",
    "Marcar figura docente y grupo como supuesto mientras no exista dato verificado.",
    "Tratar fuentes heredadas de motores como provisionales y auditables.",
    "No transferir datos curriculares de Filosofía del Derecho al destino."
  ],
  "structure_rules": [
    "Alinear cada entrega al flujo: problema, conceptos o normas, evidencia, análisis propio y conclusión transferible.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Adaptar reporte, presentación o producto visual a la planeación semanal confirmada.",
    "Mantener coherencia entre README, programa analítico, .tex y .bib.",
    "Corregir artefactos de plantilla en README y programa analítico.",
    "Expandir el token de plantilla del .bib al slug derecho-financiero-y-bancario.bib.",
    "Corregir nombres truncados de archivos en README antes de referenciarlos.",
    "No eliminar reglas válidas previas; solo agregar mejoras verificables.",
    "Evitar redacción literal heredada de nodos no equivalentes."
  ],
  "activity_rules": [
    "Delimitar el problema jurídico o social de cada actividad.",
    "Vincular el problema con conceptos, normas, doctrina o datos pertinentes al ámbito financiero y bancario.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante, no solo descripción.",
    "Separar descripción conceptual, análisis propio y conclusión jurídica.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Cerrar con conclusión aplicable a la práctica profesional.",
    "Confirmar que el producto corresponda a la consigna y planeación semanal.",
    "No asumir fuentes ni productos de semanas no verificadas.",
    "Marcar como supuesto cualquier inferencia necesaria para avanzar."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Validar estructura mínima completa antes de aplicar memoria aguas abajo.",
    "Confirmar trazabilidad de cada regla a contexto local o memoria heredada.",
    "Comprobar que toda mejora agregada sea verificable.",
    "Bloquear campos obligatorios vacíos si no tienen marca de supuesto.",
    "Validar deduplicación semántica antes de guardar memoria.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto final y consigna local.",
    "Evitar fuentes inventadas o metadatos bibliográficos no comprobados.",
    "Compilar sin errores críticos antes de entregar artefactos LaTeX."
  ],
  "latex_rules": [
    "Mantener documentclass article en español, letterpaper y oneside salvo instrucción contraria.",
    "Conservar macros de identidad académica en el encabezado del .tex.",
    "Mantener título, subtítulo y materia sincronizados con la actividad real.",
    "Reemplazar título y subtítulo de plantilla antes de entregar.",
    "Completar Figura docente con dato real o etiqueta explícita de supuesto.",
    "Revisar que la tabla de identificación compile sin celdas abiertas.",
    "Evitar romper comandos y rutas en portada, tablas y referencias.",
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar."
  ],
  "bibliography_rules": [
    "Usar derecho-financiero-y-bancario.bib como archivo bibliográfico canónico de la materia.",
    "Registrar fuentes específicas de actividad en el .bib de la materia.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Agregar entradas BibTeX solo con fuente verificable.",
    "No inventar referencias ni metadatos bibliográficos.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Incluir fecha de consulta en referencias web.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Validar consistencia entre citas en texto y claves del .bib.",
    "No importar bibliografía específica de Filosofía del Derecho al destino sin pertinencia local verificada."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Mantener compresión union-dedupe con pérdida cero por deduplicación.",
    "Propagar lateralmente solo reglas independientes de asignatura o actividad específica.",
    "Propagar a nivel materia reglas generales de identidad, estructura, calidad y bibliografía.",
    "Etiquetar origen de reglas heredadas para auditoría de no regresión.",
    "Aplicar normalización manual si reaparece salida no estructurada.",
    "Conservar vacíos de contexto local como preguntas abiertas.",
    "No transferir citas, casos ni conceptos particulares de Filosofía del Derecho sin verificación en Derecho financiero y bancario.",
    "Reforzar conexiones conceptuales estables: identidad, evidencia, análisis propio y transferencia profesional."
  ],
  "open_questions": [
    "Confirmar nombre real de la figura docente.",
    "Confirmar si el grupo debe aparecer en la tabla de identificación.",
    "Confirmar planeación semanal vigente antes de crear actividades.",
    "Confirmar número real de actividad para sustituir Actividad X.",
    "Definir formato obligatorio de citación para la materia.",
    "Supuesto: el formato de citación no está definido aún.",
    "Validar si la ubicación de portada debe mantenerse o actualizarse.",
    "Verificar si los nombres de archivos del README deben corregirse manualmente o regenerarse.",
    "Confirmar consigna específica antes de elegir reporte, presentación o producto visual.",
    "Confirmar fuentes obligatorias por semana o unidad."
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
      "Conclusión transferible a la práctica jurídica.",
      "Consistencia entre .tex, .bib, README y programa analítico.",
      "Normalización estructurada antes de propagación."
    ],
    "reason_for_being": [
      "Transformar la planeación semanal en productos académicos claros y verificables.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Formar criterio jurídico aplicable a la práctica profesional.",
      "Sostener entregas académicas con identidad UnADM e integridad bibliográfica.",
      "Servir como cerebro editorial persistente para actividades futuras de la materia."
    ],
    "style_markers": [
      "Frases directas y verificables.",
      "Supuestos marcados sin ambigüedad.",
      "No inventar fuentes.",
      "Citas explícitas cuando haya afirmaciones sustantivas.",
      "Coherencia entre narrativa, citas y estructura.",
      "Conclusiones con implicación práctica.",
      "Metadatos institucionales consistentes.",
      "Corrección previa de tokens y artefactos de plantilla."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Objetivo puntual antes del desarrollo.",
      "Marco conceptual y normativo delimitado.",
      "Evidencia verificable como soporte.",
      "Análisis propio diferenciado del resumen.",
      "Contraste entre norma, doctrina o datos cuando la consigna lo exija.",
      "Cierre con conclusión jurídica transferible.",
      "Revisión de coherencia entre pregunta guía, desarrollo y conclusión."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM.",
        "Licenciatura en Derecho.",
        "Derecho financiero y bancario.",
        "Ubicación curricular.",
        "Malla curricular de Derecho.",
        "Problema jurídico o social.",
        "Conceptos jurídicos pertinentes.",
        "Marco normativo o doctrinal.",
        "Evidencia verificable.",
        "Citas explícitas.",
        "Análisis jurídico propio.",
        "Postura académica del estudiante.",
        "Conclusión jurídica transferible.",
        "Planeación semanal.",
        "Producto académico.",
        "Reporte.",
        "Presentación.",
        "Producto visual.",
        "Consistencia .tex-.bib.",
        "Normalización estructurada.",
        "JSON parseable.",
        "Supuesto explícito.",
        "Fuente provisional heredada.",
        "Compresión union-dedupe.",
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
          "justification": "La identidad institucional exige trazabilidad, formalidad y citas verificables."
        },
        {
          "source": "Malla curricular de Derecho",
          "target": "Ubicación curricular",
          "kind": "supports",
          "justification": "El README local usa la malla curricular como fuente de semestre, bloque, tipo y créditos."
        },
        {
          "source": "Ubicación curricular",
          "target": "Derecho financiero y bancario",
          "kind": "develops",
          "justification": "La materia se documenta como asignatura de semestre 3, bloque 2, obligatoria y de 8 créditos."
        },
        {
          "source": "Planeación semanal",
          "target": "Producto académico",
          "kind": "develops",
          "justification": "El programa analítico indica que la planeación se transforma en reportes, presentaciones o productos visuales."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Análisis jurídico propio",
          "kind": "develops",
          "justification": "El problema delimita el eje de interpretación y argumentación de la entrega."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Análisis jurídico propio",
          "kind": "supports",
          "justification": "El análisis debe apoyarse en normas, doctrina o datos pertinentes."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión profesional debe derivar de fuentes comprobables y del análisis desarrollado."
        },
        {
          "source": "Citas explícitas",
          "target": "Consistencia .tex-.bib",
          "kind": "depends_on",
          "justification": "Cada cita en texto debe tener clave válida en el archivo bibliográfico canónico."
        },
        {
          "source": "Normalización estructurada",
          "target": "JSON parseable",
          "kind": "depends_on",
          "justification": "La memoria solo puede propagarse de forma segura si cumple estructura parseable."
        },
        {
          "source": "Fuente provisional heredada",
          "target": "Supuesto explícito",
          "kind": "depends_on",
          "justification": "Las fuentes heredadas de motor requieren marca de provisionalidad hasta verificación local."
        },
        {
          "source": "Compresión union-dedupe",
          "target": "No regresión editorial",
          "kind": "supports",
          "justification": "La deduplicación conserva reglas útiles y evita pérdida de memoria válida."
        },
        {
          "source": "Filosofía del Derecho",
          "target": "Derecho financiero y bancario",
          "kind": "contrasts",
          "justification": "Son nodos no equivalentes; solo se transfieren abstracciones editoriales estables."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 3, bloque 2, obligatoria, 8 créditos.",
        "README local: fuente curricular UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: identidad UnADM, integridad académica, citas verificables y conclusión jurídica propia.",
        "Programa analítico local: productos académicos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: ejes de problema, conceptos, producto, análisis propio y conclusión transferible.",
        "Programa analítico local: bibliografía específica en derecho-financiero-y-bancario.bib.",
        "Bib local: entradas unadmSitioWeb y unadmMallaDerecho2024.",
        "Tex local: autor Martin Jonathan de la Cruz y matrícula ES2611202040.",
        "Tex local: título y subtítulo de plantilla pendientes de actividad concreta.",
        "Memoria heredada: revisar respuesta no estructurada antes de aplicar aguas abajo.",
        "Memoria origen: bloquear propagación si la salida no es JSON parseable.",
        "Memoria origen: no inventar fuentes y usar citas verificables.",
        "Memoria origen: iniciar con problema, integrar conceptos, evidencia, análisis propio y conclusión jurídica."
      ]
    },
    "reinforcement_log": [
      "Ciclo 16: se aplicó sincronización transversal progresiva y conservadora.",
      "Ciclo 16: se preservó identidad UnADM y ubicación curricular local del destino.",
      "Ciclo 16: se deduplicaron reglas repetidas sin eliminar reglas útiles.",
      "Ciclo 16: se transfirieron solo abstracciones estables desde Filosofía del Derecho.",
      "Ciclo 16: se excluyeron citas y conceptos específicos de Filosofía del Derecho por no estar verificados en el destino.",
      "Ciclo 16: se reforzó el gate de JSON parseable antes de propagación recursiva.",
      "Ciclo 16: se reforzó la consistencia entre README, programa analítico, .tex y .bib.",
      "Ciclo 16: se mantuvieron vacíos locales como preguntas abiertas con marca de supuesto."
    ]
  }
}