{
  "summary": [
    "Memoria de materia consolidada para Derecho financiero y bancario con identidad UnADM.",
    "Ciclo 3 aplica sincronización transversal progresiva y conservadora.",
    "Se preservan reglas válidas previas sin regresión.",
    "Se deduplican reglas por unión semántica con compresión lossless.",
    "La materia se ubica en semestre 3, bloque 2, obligatoria, 8 créditos.",
    "La carpeta local es el punto de entrada canónico de la asignatura.",
    "Se mantienen como ejes editoriales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se detectan artefactos de plantilla en README, programa analítico y portada .tex.",
    "Se conserva alerta por salidas heredadas no parseables desde motores previos.",
    "Se transfieren solo abstracciones editoriales estables desde Filosofía del Derecho."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar la Licenciatura en Derecho como programa académico.",
    "Usar datos locales: Derecho financiero y bancario, clave LDE-S3B2, semestre 3, bloque 2.",
    "Registrar tipo obligatoria y 8 créditos según README local.",
    "Conservar autor Martin Jonathan de la Cruz según .tex local.",
    "Conservar matrícula ES2611202040 según .tex local.",
    "Marcar como supuesto cualquier dato no confirmado del docente, grupo o consigna.",
    "Conservar ubicación Roma Norte, Ciudad de México salvo lineamiento contrario.",
    "Tratar fuentes heredadas de motor como provisionales y auditables.",
    "Citar malla-curricular-derecho-unadm.pdf para ubicación curricular.",
    "Usar la carpeta de materia como entrada canónica."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por la planeación semanal.",
    "Usar reportes, presentaciones o productos visuales según consigna.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener coherencia entre README, programa analítico, .tex y .bib.",
    "Corregir artefactos de plantilla en README y programa analítico.",
    "Expandir el token de plantilla del .bib al slug derecho-financiero-y-bancario.bib.",
    "Corregir nombres truncados de reporte y referencias en README.",
    "No eliminar reglas útiles previas.",
    "Agregar solo mejoras verificables."
  ],
  "activity_rules": [
    "Delimitar el problema jurídico o social de cada actividad.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Usar norma, doctrina o datos pertinentes al tema financiero y bancario.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Separar descripción conceptual, análisis propio y conclusión jurídica.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Adaptar profundidad y formato a la rúbrica confirmada.",
    "No asumir fuentes obligatorias sin consigna local.",
    "No trasladar contenidos sustantivos de Filosofía del Derecho al destino."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar trazabilidad de cada regla a contexto local o memoria heredada.",
    "Bloquear campos obligatorios vacíos sin marca de supuesto.",
    "Validar deduplicación semántica antes de guardar memoria.",
    "Comprobar que cada mejora agregada sea verificable.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna de actividad.",
    "Auditar fuentes heredadas de motor antes de tratarlas como locales."
  ],
  "latex_rules": [
    "Mantener documentclass article en español, letterpaper y oneside salvo instrucción contraria.",
    "Conservar macros de identidad académica en el encabezado del .tex.",
    "Reemplazar título y subtítulo de plantilla por los de la actividad real.",
    "Mantener sincronizados título, subtítulo, materia y clave.",
    "Completar Figura docente con dato real o etiqueta explícita de supuesto.",
    "Revisar que la tabla de identificación compile sin celdas abiertas.",
    "Evitar romper comandos y rutas en portada, tablas y referencias.",
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Compilar sin errores críticos y sin referencias rotas."
  ],
  "bibliography_rules": [
    "Usar derecho-financiero-y-bancario.bib como archivo bibliográfico canónico.",
    "Registrar fuentes específicas de actividad en el .bib canónico.",
    "Priorizar fuentes institucionales UnADM y documentos curriculares locales.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Agregar entradas BibTeX solo con fuente verificable.",
    "No inventar fuentes ni metadatos bibliográficos.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Incluir fecha de consulta en referencias web.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Validar correspondencia entre citas en texto y entradas .bib."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar lateralmente solo abstracciones independientes de actividad específica.",
    "Conservar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferir redacción literal entre nodos no equivalentes.",
    "Mantener método union-dedupe con pérdida cero.",
    "Etiquetar reglas heredadas para auditoría de no regresión.",
    "Aplicar normalización manual si reaparece salida no estructurada.",
    "Mantener vacíos de contexto local como preguntas abiertas.",
    "No reducir especificidad local al incorporar memoria transversal.",
    "Revisar salidas de ciclos previos antes de reutilizarlas."
  ],
  "open_questions": [
    "Confirmar nombre real de la figura docente.",
    "Confirmar si el grupo debe aparecer en la tabla de identificación.",
    "Confirmar planeación semanal vigente antes de crear actividades.",
    "Confirmar número real de actividad para sustituir Actividad X.",
    "Definir formato obligatorio de citación para la materia.",
    "Supuesto: el formato de citación aún no está definido.",
    "Validar si la ubicación de portada debe mantenerse o actualizarse.",
    "Verificar si los nombres truncados del README deben corregirse manualmente o regenerarse.",
    "Confirmar rúbrica de evaluación específica.",
    "Confirmar fuentes obligatorias de cada semana."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Sobrio y verificable.",
        "Orientado a práctica profesional."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Entrada canónica por carpeta de materia.",
        "Trazabilidad entre README, programa, .tex y .bib.",
        "Supuestos marcados de forma explícita."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Derecho financiero y bancario.",
        "Clave local: LDE-S3B2.",
        "Semestre 3, bloque 2.",
        "Materia obligatoria de 8 créditos."
      ]
    },
    "essence": [
      "Identidad institucional UnADM.",
      "Integridad académica.",
      "Problema jurídico o social delimitado.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable.",
      "Análisis jurídico propio.",
      "Conclusión transferible a la práctica jurídica.",
      "Consistencia entre estructura, citas y bibliografía.",
      "Normalización estructurada antes de propagar.",
      "Adaptación del producto a la planeación semanal."
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
      "Transformar la planeación semanal en entregables jurídicos verificables.",
      "Evitar productos meramente descriptivos.",
      "Sostener postura propia con fuentes comprobables.",
      "Conectar aprendizaje jurídico con práctica profesional.",
      "Mantener memoria editorial reusable sin perder especificidad local."
    ],
    "style_markers": [
      "Frases directas y verificables.",
      "Supuestos marcados como supuesto.",
      "No inventar fuentes.",
      "No trasladar contenido sustantivo ajeno al destino.",
      "Diferenciar regla institucional de dato local.",
      "Usar lenguaje jurídico claro.",
      "Evitar redundancias semánticas.",
      "Cerrar con implicación profesional.",
      "Mantener consistencia .tex-.bib.",
      "Registrar vacíos como preguntas abiertas."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Objetivo puntual antes del desarrollo.",
      "Marco conceptual y normativo delimitado.",
      "Evidencia verificable como soporte.",
      "Análisis propio separado de la descripción.",
      "Contraste entre regla, hecho y consecuencia jurídica cuando aplique.",
      "Conclusión derivada del desarrollo.",
      "Transferencia a la práctica profesional.",
      "Coherencia entre pregunta guía, desarrollo y cierre.",
      "Producto final ajustado a consigna y rúbrica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Licenciatura en Derecho",
        "Derecho financiero y bancario",
        "Semestre 3 bloque 2",
        "Materia obligatoria de 8 créditos",
        "Carpeta de materia como entrada canónica",
        "Problema jurídico o social",
        "Conceptos jurídicos pertinentes",
        "Marco normativo o doctrinal",
        "Evidencia verificable",
        "Análisis jurídico propio",
        "Postura argumentada del estudiante",
        "Conclusión transferible",
        "Planeación semanal",
        "Producto académico",
        "Integridad académica",
        "Normalización estructurada",
        "JSON parseable",
        "Consistencia .tex-.bib",
        "Archivo bibliográfico canónico",
        "Artefactos de plantilla",
        "Supuestos explícitos"
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
          "justification": "La pauta local exige identidad UnADM, citas verificables y criterio propio."
        },
        {
          "source": "Malla curricular de la Licenciatura en Derecho",
          "target": "Semestre 3 bloque 2",
          "kind": "supports",
          "justification": "El README local cita la malla curricular como fuente de ubicación."
        },
        {
          "source": "Derecho financiero y bancario",
          "target": "Materia obligatoria de 8 créditos",
          "kind": "depends_on",
          "justification": "El dato curricular proviene del README local."
        },
        {
          "source": "Carpeta de materia como entrada canónica",
          "target": "Consistencia .tex-.bib",
          "kind": "supports",
          "justification": "La carpeta integra README, programa, .tex y .bib."
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
          "target": "Postura argumentada del estudiante",
          "kind": "supports",
          "justification": "La postura debe sostenerse con normas, doctrina o datos pertinentes."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión profesional debe derivar de fuentes comprobables."
        },
        {
          "source": "Normalización estructurada",
          "target": "JSON parseable",
          "kind": "depends_on",
          "justification": "La propagación segura requiere salida estructurada válida."
        },
        {
          "source": "Archivo bibliográfico canónico",
          "target": "Consistencia .tex-.bib",
          "kind": "supports",
          "justification": "Las citas del texto deben existir en derecho-financiero-y-bancario.bib."
        },
        {
          "source": "Artefactos de plantilla",
          "target": "Consistencia .tex-.bib",
          "kind": "contrasts",
          "justification": "Los tokens sin expandir y nombres truncados rompen coherencia editorial."
        },
        {
          "source": "Supuestos explícitos",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Marcar datos no confirmados evita presentar inferencias como hechos."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 3, bloque 2, obligatoria, 8 créditos.",
        "README local: fuente curricular malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: conservar identidad UnADM, integridad académica, citas verificables y conclusión jurídica.",
        "Programa analítico local: claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: transformar planeación en reportes, presentaciones y productos visuales.",
        "Programa analítico local: ejes de problema, conceptos, producto, análisis y conclusión.",
        "derecho-financiero-y-bancario.bib: entradas unadmSitioWeb y unadmMallaDerecho2024.",
        "reporte local .tex: autor Martin Jonathan de la Cruz y matrícula ES2611202040.",
        "reporte local .tex: título y subtítulo de plantilla pendientes de actividad real.",
        "Memoria heredada: revisar salidas no estructuradas antes de aplicar aguas abajo."
      ]
    },
    "reinforcement_log": [
      "Ciclo 3 preserva reglas institucionales UnADM sin regresión.",
      "Se deduplicaron repeticiones de identidad, estructura, calidad, LaTeX y bibliografía.",
      "Se reforzó la separación entre abstracción transversal y contenido sustantivo de origen.",
      "Se mantuvo Derecho financiero y bancario como contexto curricular local.",
      "Se conservaron vacíos locales como preguntas abiertas.",
      "Se normalizó el grafo con relaciones permitidas.",
      "Se excluyeron citas sustantivas de Filosofía del Derecho por no ser equivalentes al destino.",
      "Se conservaron solo citas locales verificables del .bib destino.",
      "Se reforzó el gate de JSON parseable por antecedentes de salidas no estructuradas.",
      "Se mantuvo la regla de no inventar fuentes ni metadatos."
    ]
  }
}