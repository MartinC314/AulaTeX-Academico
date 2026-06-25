{
  "summary": [
    "Materia destino consolidada con identidad UnADM y compresión union-dedupe.",
    "Derecho financiero y bancario se ubica en semestre 3, bloque 2, obligatoria, 8 créditos.",
    "La carpeta local es el punto de entrada canónico de la materia.",
    "La pauta editorial exige integridad académica, citas verificables y conclusión jurídica propia.",
    "Se preservan reglas transversales útiles desde Filosofía del Derecho sin transferir contenido específico.",
    "Se detectan artefactos de plantilla en README, programa analítico y reporte base.",
    "El archivo bibliográfico canónico local es derecho-financiero-y-bancario.bib.",
    "Existen antecedentes de salidas no parseables en JSON desde motores heredados.",
    "La sincronización transversal prioriza identidad, estructura reusable, calidad y grafo conceptual."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, metadatos y tono.",
    "Usar Licenciatura en Derecho como programa académico del destino.",
    "Usar datos locales: Derecho financiero y bancario, clave LDE-S3B2, semestre 3, bloque 2.",
    "Conservar tipo obligatoria y 8 créditos según README local.",
    "Citar malla-curricular-derecho-unadm.pdf como fuente de ubicación curricular.",
    "Conservar autor Martin Jonathan de la Cruz y matrícula ES2611202040 según .tex local.",
    "Conservar Roma Norte, Ciudad de México salvo lineamiento contrario.",
    "Marcar como supuesto cualquier dato no confirmado del docente, grupo o consigna.",
    "Tratar fuentes heredadas de motor como provisionales y auditables.",
    "No importar identidad curricular de Filosofía del Derecho al destino."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como entrada canónica antes de crear actividades.",
    "Alinear cada entrega al flujo: problema, conceptos o normas, producto, análisis propio y conclusión transferible.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el producto al formato solicitado por la planeación semanal.",
    "Mantener coherencia entre README, programa analítico, .tex y .bib.",
    "Corregir artefactos de plantilla en README y programa analítico.",
    "Expandir tokens de plantilla al slug literal derecho-financiero-y-bancario.",
    "No eliminar reglas válidas previas; agregar solo mejoras verificables."
  ],
  "activity_rules": [
    "Confirmar consigna antes de generar una actividad específica.",
    "Adaptar reporte, presentación o producto visual a la planeación semanal confirmada.",
    "Sustentar afirmaciones con norma, doctrina, datos o fuentes verificables.",
    "Separar descripción conceptual, análisis propio y conclusión jurídica.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Evitar afirmaciones sin respaldo o sin marca de supuesto.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Cerrar con conclusión jurídica aplicable a la práctica profesional.",
    "No asumir que fuentes de otra materia corresponden a esta asignatura.",
    "Registrar fuentes específicas de cada actividad en el .bib local."
  ],
  "quality_gates": [
    "Verificar que toda salida de memoria sea JSON parseable antes de propagar.",
    "Bloquear propagación si faltan campos obligatorios sin marca de supuesto.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar trazabilidad de cada regla a contexto local o memoria heredada.",
    "Validar deduplicación semántica antes de guardar memoria.",
    "Comprobar que cada mejora agregada sea verificable.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar correspondencia entre producto y consigna de actividad.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Compilar artefactos sin errores críticos ni referencias rotas."
  ],
  "latex_rules": [
    "Mantener documentclass article en español, letterpaper y oneside salvo instrucción contraria.",
    "Conservar macros de identidad académica en el encabezado del .tex.",
    "Reemplazar título y subtítulo de plantilla por los de la actividad real.",
    "Mantener sincronizados título, subtítulo, materia y clave entre portada y contenido.",
    "Completar Figura docente con dato real o etiqueta explícita de supuesto.",
    "Revisar que la tabla de identificación compile sin celdas abiertas.",
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Verificar nombres de archivos del README antes de referenciarlos."
  ],
  "bibliography_rules": [
    "Usar derecho-financiero-y-bancario.bib como archivo bibliográfico canónico.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar fuentes específicas de actividad en el .bib local.",
    "Agregar entradas BibTeX solo con fuente verificable.",
    "No inventar fuentes ni metadatos bibliográficos.",
    "Conservar metadatos mínimos: autor, título, año, fuente o URL.",
    "Incluir fecha de consulta en referencias web.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "No importar bibliografía de Filosofía del Derecho salvo verificación local y pertinencia expresa."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Mantener método union-dedupe con compresión lossless.",
    "Propagar lateralmente solo abstracciones estables entre materias no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferir redacción literal o fuentes específicas de otra asignatura.",
    "Etiquetar reglas heredadas para auditoría de no regresión.",
    "Aplicar normalización manual si reaparece salida no estructurada.",
    "Mantener vacíos de contexto local como preguntas abiertas con marca de supuesto.",
    "Reforzar coherencia entre README, programa, .tex y .bib en nodos descendientes.",
    "No reducir especificidad local al recibir reglas transversales."
  ],
  "open_questions": [
    "Confirmar nombre real de la figura docente.",
    "Confirmar si el grupo debe aparecer en la tabla de identificación.",
    "Definir formato obligatorio de citación para la materia.",
    "Confirmar planeación semanal vigente antes de crear actividades.",
    "Confirmar número real de actividad para sustituir Actividad X.",
    "Validar si la localización de portada debe mantenerse o actualizarse.",
    "Verificar si los nombres de archivos del README deben corregirse manualmente o regenerarse.",
    "Confirmar fuentes obligatorias específicas de Derecho financiero y bancario.",
    "Confirmar si cada actividad requiere reporte, presentación u otro producto principal.",
    "Confirmar rúbrica de evaluación para ajustar profundidad argumentativa."
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
      "Integridad académica.",
      "Evidencia verificable.",
      "Problema jurídico o social delimitado.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Análisis jurídico propio.",
      "Conclusión transferible a la práctica jurídica.",
      "Consistencia entre .tex, .bib, README y programa analítico.",
      "Normalización estructurada antes de propagar."
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, fundamento jurídico y evidencia.",
      "Transformar la planeación semanal en reportes, presentaciones o productos visuales.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Producir conclusiones jurídicas útiles para la práctica profesional.",
      "Conservar memoria editorial persistente sin pérdida por deduplicación."
    ],
    "style_markers": [
      "Frases directas y verificables.",
      "Supuestos explícitos.",
      "Fuentes no inventadas.",
      "Tono institucional UnADM.",
      "Citas trazables al .bib local.",
      "Separación clara entre descripción y análisis.",
      "Conclusiones con criterio jurídico propio.",
      "Coherencia de metadatos en todos los artefactos."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Objetivo puntual antes del desarrollo.",
      "Marco conceptual y normativo delimitado.",
      "Evidencia verificable como soporte.",
      "Análisis propio con criterio jurídico.",
      "Contraste entre descripción y valoración.",
      "Cierre con implicación práctica.",
      "Revisión final de coherencia entre pregunta, desarrollo y conclusión."
    ],
    "knowledge_graph": {
      "concepts": [
        "Derecho financiero y bancario.",
        "Licenciatura en Derecho.",
        "Identidad institucional UnADM.",
        "Ubicación curricular.",
        "Malla curricular de Derecho.",
        "Integridad académica.",
        "Evidencia verificable.",
        "Normalización estructurada.",
        "Carpeta de materia como entrada canónica.",
        "Planeación semanal.",
        "Producto académico.",
        "Problema jurídico o social.",
        "Conceptos y normas pertinentes.",
        "Análisis jurídico propio.",
        "Conclusión transferible.",
        "Archivo bibliográfico canónico.",
        "Consistencia .tex-.bib.",
        "Artefactos de plantilla.",
        "Supuestos editoriales.",
        "Propagación transversal conservadora."
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
          "source": "Malla curricular de Derecho",
          "target": "Ubicación curricular",
          "kind": "supports",
          "justification": "El README local cita la malla curricular como fuente de semestre, bloque, tipo y créditos."
        },
        {
          "source": "Carpeta de materia como entrada canónica",
          "target": "Consistencia .tex-.bib",
          "kind": "supports",
          "justification": "La carpeta agrupa README, programa, reporte, presentación y bibliografía local."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación transversal conservadora",
          "kind": "depends_on",
          "justification": "Las memorias no parseables deben normalizarse antes de aplicarse aguas abajo."
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
          "justification": "El problema delimita el eje del análisis y evita entregas solo descriptivas."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión profesional debe derivar de fuentes comprobables."
        },
        {
          "source": "Archivo bibliográfico canónico",
          "target": "Consistencia .tex-.bib",
          "kind": "supports",
          "justification": "Las citas del documento deben corresponder con entradas BibTeX locales."
        },
        {
          "source": "Artefactos de plantilla",
          "target": "Compilación limpia",
          "kind": "contrasts",
          "justification": "Tokens sin expandir y caracteres anómalos pueden romper rutas, referencias o presentación."
        },
        {
          "source": "Supuestos editoriales",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Marcar incertidumbres evita convertir datos no confirmados en afirmaciones."
        }
      ],
      "evidence": [
        "README local: materia de Licenciatura en Derecho de la UnADM.",
        "README local: semestre 3, bloque 2, obligatoria, 8 créditos.",
        "README local: fuente curricular UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: integridad académica, citas verificables y conclusión jurídica propia.",
        "Programa analítico local: claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
        "derecho-financiero-y-bancario.bib: entradas unadmSitioWeb y unadmMallaDerecho2024.",
        "Reporte local: autor Martin Jonathan de la Cruz y matrícula ES2611202040.",
        "Reporte local: título y subtítulo de plantilla pendientes de actividad real.",
        "Contexto local: token $(@{...}.Slug) pendiente de expansión.",
        "Memoria heredada: antecedente de salida sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 20: se sincronizó ADN transversal desde actividad de Filosofía del Derecho hacia materia de Derecho financiero y bancario.",
      "Se preservaron solo abstracciones estables entre nodos no equivalentes.",
      "Se evitó transferir bibliografía y conceptos específicos de Filosofía del Derecho.",
      "Se reforzó la identidad UnADM con datos curriculares locales del destino.",
      "Se consolidó el flujo problema, conceptos, evidencia, análisis propio y conclusión.",
      "Se reforzó el gate de JSON parseable antes de propagación recursiva.",
      "Se mantuvo compresión lossless por unión y deduplicación semántica.",
      "Se conservaron preguntas abiertas para vacíos de contexto local.",
      "Se reforzó la corrección de tokens y artefactos de plantilla.",
      "Se preservó la regla de no inventar fuentes ni metadatos."
    ]
  }
}