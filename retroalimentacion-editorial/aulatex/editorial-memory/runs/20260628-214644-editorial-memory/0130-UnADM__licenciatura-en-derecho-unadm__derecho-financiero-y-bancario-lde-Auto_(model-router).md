{
  "summary": [
    "Se consolida memoria de materia para Derecho financiero y bancario con identidad UnADM.",
    "Se preserva la ubicación local: semestre 3, bloque 2, obligatoria, 8 créditos.",
    "Se refuerza el flujo editorial reusable: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se conserva compresión union-dedupe sin regresión.",
    "Se mantienen reglas de normalización antes de propagar memoria.",
    "Se detectan artefactos de plantilla en README, programa analítico y portada .tex.",
    "Se tratan salidas heredadas no parseables como provisionales y auditables."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, metadatos y tono.",
    "Usar datos locales de materia: Derecho financiero y bancario, clave LDE-S3B2, semestre 3, bloque 2.",
    "Usar Licenciatura en Derecho como programa académico.",
    "Conservar autor Martin Jonathan de la Cruz y matrícula ES2611202040 según .tex local.",
    "Conservar Roma Norte, Ciudad de México salvo lineamiento contrario.",
    "Marcar como supuesto cualquier dato no confirmado en consigna o documentos locales.",
    "Completar figura docente con dato real o etiqueta explícita de supuesto.",
    "Tratar fuentes heredadas de motor como provisionales hasta verificación local.",
    "Usar la carpeta de materia como punto de entrada canónico."
  ],
  "structure_rules": [
    "Alinear cada entrega al producto solicitado por la planeación semanal.",
    "Definir objetivo puntual antes del desarrollo.",
    "Abrir con encuadre breve del problema jurídico o social.",
    "Separar conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir descripción conceptual de postura argumentada.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener coherencia entre README, programa analítico, .tex y .bib.",
    "Corregir nombres de archivo con caracteres faltantes en README.",
    "Expandir el token de plantilla del .bib al slug derecho-financiero-y-bancario.bib.",
    "No eliminar reglas válidas previas; agregar solo mejoras verificables."
  ],
  "activity_rules": [
    "Delimitar el problema jurídico o social de cada actividad.",
    "Sustentar afirmaciones con norma, doctrina, datos o fuentes verificables.",
    "Incluir cita explícita cuando se use evidencia.",
    "Exigir postura argumentada del estudiante, no solo resumen.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Adaptar reporte, presentación o producto visual a la consigna confirmada.",
    "No asumir fuentes de otra semana como obligatorias de una actividad específica.",
    "Marcar como supuesto cualquier elemento no visible en la consigna."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar salida no estructurada antes de reutilizarla.",
    "Validar estructura mínima completa antes de guardar memoria.",
    "Confirmar trazabilidad de cada regla a contexto local o memoria heredada.",
    "Bloquear campos obligatorios vacíos sin marca de supuesto.",
    "Comprobar que toda mejora agregada sea verificable.",
    "Validar deduplicación semántica antes de guardar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna de actividad."
  ],
  "latex_rules": [
    "Mantener documentclass article en español, letterpaper y oneside salvo instrucción contraria.",
    "Conservar macros de identidad académica en el encabezado del .tex.",
    "Sincronizar título, subtítulo, materia y actividad entre portada y contenido.",
    "Reemplazar Actividad X por número real de actividad antes de entregar.",
    "Completar Figura docente con dato real o supuesto explícito.",
    "Revisar que la tabla de identificación compile sin comandos incompletos.",
    "Evitar romper comandos y rutas en portada, tablas y referencias.",
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Corregir caracteres anómalos en rutas o nombres de archivo.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Usar derecho-financiero-y-bancario.bib como archivo bibliográfico canónico.",
    "Registrar fuentes específicas de actividad en el .bib de la materia.",
    "Priorizar fuentes institucionales UnADM y documentos curriculares locales cuando apliquen.",
    "Conservar unadmSitioWeb y unadmMallaDerecho2024.",
    "No inventar fuentes ni metadatos bibliográficos.",
    "Agregar entradas BibTeX solo con fuente verificable.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Incluir fecha de consulta en referencias web.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Validar citas en texto contra entradas reales del .bib."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar lateralmente solo abstracciones editoriales estables.",
    "No transferir contenido doctrinal específico de Filosofía del Derecho al destino.",
    "Reutilizar reglas institucionales de identidad, estructura, calidad y bibliografía.",
    "Mantener union-dedupe con pérdida cero.",
    "Aplicar normalización manual si reaparece salida no estructurada.",
    "Etiquetar reglas heredadas para auditoría de no regresión.",
    "Conservar especificidad local de Derecho financiero y bancario.",
    "No reducir reglas locales verificadas al consolidar memoria transversal."
  ],
  "open_questions": [
    "Confirmar nombre real de la figura docente.",
    "Confirmar si el grupo debe aparecer en la tabla de identificación.",
    "Definir formato obligatorio de citación para la materia.",
    "Validar si la localización de portada debe mantenerse o actualizarse.",
    "Confirmar planeación semanal vigente antes de generar actividades.",
    "Confirmar número real de actividad para sustituir Actividad X.",
    "Verificar si los nombres de archivos del README deben corregirse manualmente o regenerarse.",
    "Confirmar rúbricas específicas de actividades futuras.",
    "Confirmar fuentes obligatorias por semana."
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
        "Carpeta de materia como entrada canónica.",
        "Normalización estructurada antes de propagar.",
        "Fuentes heredadas tratadas como provisionales."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Derecho financiero y bancario.",
        "Clave local: LDE-S3B2.",
        "Semestre 3, bloque 2.",
        "Obligatoria, 8 créditos."
      ]
    },
    "essence": [
      "Identidad institucional UnADM.",
      "Problema jurídico o social delimitado.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable.",
      "Análisis jurídico propio.",
      "Conclusión transferible a la práctica jurídica.",
      "Coherencia entre consigna, desarrollo y cierre.",
      "Trazabilidad entre texto, .bib y documentos locales."
    ],
    "reason_for_being": [
      "Orientar productos académicos de Derecho financiero y bancario con claridad, fundamento jurídico y evidencia.",
      "Transformar la planeación semanal en reportes, presentaciones o productos visuales.",
      "Evitar entregas descriptivas sin postura jurídica.",
      "Convertir evidencia verificable en análisis propio.",
      "Cerrar cada producto con utilidad profesional."
    ],
    "style_markers": [
      "Frases precisas y accionables.",
      "Secciones explícitas y funcionales.",
      "Uso visible de supuestos cuando falta información.",
      "Separación entre descripción y análisis.",
      "Citas verificables antes de afirmaciones fuertes.",
      "Conclusiones con criterio jurídico propio.",
      "Metadatos institucionales consistentes.",
      "Sin redacción literal transferida desde materias no equivalentes."
    ],
    "argumentative_patterns": [
      "Delimitar problema antes de desarrollar.",
      "Definir objetivo puntual.",
      "Exponer conceptos y normas aplicables.",
      "Integrar evidencia verificable.",
      "Analizar con postura propia.",
      "Contrastar descripción y valoración jurídica.",
      "Cerrar con conclusión aplicable a la práctica.",
      "Alinear todo el producto con la consigna confirmada."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Licenciatura en Derecho",
        "Derecho financiero y bancario",
        "Semestre 3 bloque 2",
        "Malla curricular de Derecho",
        "Problema jurídico o social",
        "Conceptos jurídicos clave",
        "Marco normativo o doctrinal",
        "Evidencia verificable",
        "Análisis jurídico propio",
        "Postura argumentada del estudiante",
        "Conclusión jurídica transferible",
        "Planeación semanal",
        "Producto académico",
        "Normalización estructurada",
        "Bibliografía canónica",
        "Trazabilidad editorial",
        "Supuesto explícito"
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
          "justification": "La pauta local exige identidad UnADM, citas verificables y conclusión jurídica propia."
        },
        {
          "source": "Malla curricular de Derecho",
          "target": "Semestre 3 bloque 2",
          "kind": "supports",
          "justification": "El README local cita la malla curricular como fuente de ubicación."
        },
        {
          "source": "Planeación semanal",
          "target": "Producto académico",
          "kind": "depends_on",
          "justification": "El programa analítico indica transformar la planeación en reportes, presentaciones o productos visuales."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Marco normativo o doctrinal",
          "kind": "develops",
          "justification": "El encuadre del problema orienta qué conceptos, normas y doctrina son pertinentes."
        },
        {
          "source": "Evidencia verificable",
          "target": "Análisis jurídico propio",
          "kind": "supports",
          "justification": "La postura argumentada requiere respaldo comprobable."
        },
        {
          "source": "Análisis jurídico propio",
          "target": "Conclusión jurídica transferible",
          "kind": "develops",
          "justification": "El cierre profesional surge del razonamiento jurídico y no del resumen."
        },
        {
          "source": "Bibliografía canónica",
          "target": "Trazabilidad editorial",
          "kind": "supports",
          "justification": "El .bib local permite validar citas y fuentes."
        },
        {
          "source": "Supuesto explícito",
          "target": "Trazabilidad editorial",
          "kind": "supports",
          "justification": "Marcar datos no confirmados evita afirmaciones falsas."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "La memoria heredada exige validar JSON y estructura antes de propagar."
        },
        {
          "source": "Derecho financiero y bancario",
          "target": "Licenciatura en Derecho",
          "kind": "depends_on",
          "justification": "El README local identifica la materia dentro de la Licenciatura en Derecho de la UnADM."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 3, bloque 2, obligatoria, 8 créditos.",
        "README local: fuente curricular UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: identidad UnADM, integridad académica, citas verificables y conclusión jurídica propia.",
        "Programa analítico local: claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: productos académicos desde planeación semanal.",
        "Programa analítico local: ejes problema, conceptos, producto, análisis y conclusión.",
        "derecho-financiero-y-bancario.bib: entradas unadmSitioWeb y unadmMallaDerecho2024.",
        "reporte .tex local: autor Martin Jonathan de la Cruz y matrícula ES2611202040.",
        "reporte .tex local: título y subtítulo de plantilla pendientes de personalización.",
        "Memoria heredada: antecedente de salida sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas del origen y destino.",
      "Se conservaron reglas locales verificadas del destino.",
      "Se transfirieron solo abstracciones estables desde Filosofía del Derecho.",
      "Se excluyeron conceptos doctrinales específicos no equivalentes al destino.",
      "Se reforzó normalización JSON antes de propagación.",
      "Se reforzó trazabilidad entre consigna, fuentes, .tex y .bib.",
      "Se mantuvo criterio de no inventar fuentes.",
      "Se preservó la estructura problema, conceptos, evidencia, análisis y cierre.",
      "Se marcaron vacíos locales como preguntas abiertas.",
      "Se consolidó cerebro editorial mínimo de materia para propagación recursiva conservadora."
    ]
  }
}