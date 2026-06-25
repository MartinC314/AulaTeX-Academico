{
  "summary": [
    "Materia destino consolidada con cerebro editorial UnADM.",
    "Se preserva contexto local verificado: Licenciatura en Derecho, semestre 4, bloque 1, obligatoria, 8 créditos.",
    "Se refuerzan ejes transversales: problema, conceptos, fuentes, análisis propio y conclusión jurídica.",
    "Se mantiene estrategia conservadora sin trasladar contenido temático específico de Filosofía del Derecho.",
    "Se conserva incidencia histórica de salidas no JSON parseables.",
    "Se prioriza compresión por unión y deduplicación."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre local de la materia: Bases de derecho internacional publico.",
    "Usar código local de curso LDE-S4B1.",
    "Alinear entregables a Licenciatura en Derecho, semestre 4, bloque 1, obligatoria, 8 créditos.",
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Conservar al alumno registrado en plantilla si no hay instrucción local que lo sustituya.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar Codex y GPT-Pro como procedencia provisional, no como identidad del entregable.",
    "No mezclar metadatos curriculares del origen con el destino."
  ],
  "structure_rules": [
    "Transformar la planeación semanal en el producto académico solicitado.",
    "Mantener el programa analítico como guía editorial de actividades.",
    "Organizar cada entrega con problema jurídico o social, conceptos, fuentes, análisis propio y conclusión jurídica.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir reporte, presentación y producto visual según la consigna.",
    "Conservar separación entre reporte, presentación, programa analítico y bibliografía.",
    "Conservar la carpeta referencias-bases-de-derecho-internacional-publico como repositorio de apoyo.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Adaptar cada actividad al producto solicitado por la planeación semanal.",
    "Verificar que el producto corresponda a la consigna vigente.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Distinguir hechos, argumentos, normas y criterio propio.",
    "Integrar normas, doctrina o datos pertinentes al caso de actividad.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Evitar extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes.",
    "No sustituir vacíos documentales por invenciones."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de propagar memoria.",
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Revisar consistencia entre instrucciones de actividad y programa analítico.",
    "Verificar que README, programa analítico, .bib y plantillas locales coincidan.",
    "Validar citas y referencias antes de cerrar entregables.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Validar sintaxis LaTeX y cierre de entornos antes de compilar.",
    "Marcar faltantes como pendientes sin inventar contenido.",
    "Mantener auditoría de parseo JSON antes de nueva propagación."
  ],
  "latex_rules": [
    "Reutilizar la plantilla .tex local de la materia como base de nuevas actividades.",
    "Usar reporte-bases-de-derecho-internacional-publico.tex para reportes base.",
    "Usar presentacion-bases-de-derecho-internacional-publico.tex solo para presentaciones.",
    "Mantener compatibilidad con clase article, spanish, letterpaper y oneside.",
    "Completar metadatos de portada sin alterar identidad institucional.",
    "Definir título, subtítulo y subject coherentes con la actividad en curso.",
    "No cambiar la estructura base de portada sin instrucción editorial.",
    "Usar acentos y codificación correcta en .tex y .bib.",
    "Conservar nombres de archivo locales salvo normalización acordada.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Revisar y cerrar correctamente entornos tabular antes de compilar.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial."
  ],
  "bibliography_rules": [
    "Registrar fuentes de actividad en bases-de-derecho-internacional-publico.bib.",
    "Priorizar fuentes institucionales UnADM y documentos jurídicos verificables.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Conservar la malla curricular de Derecho como fuente institucional local.",
    "Agregar entradas BibTeX específicas solo cuando la fuente exista y sea verificable.",
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "Marcar referencias faltantes como pendientes.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Validar que las claves citadas existan en el .bib local.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "No asumir que bibliografía de Filosofía del Derecho aplica al destino."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas y no duplicadas.",
    "Compartir solo abstracciones editoriales estables entre materias no equivalentes.",
    "Preservar reglas útiles previas aunque se reubiquen por categoría.",
    "Mantener compresión union-dedupe con criterio lossless.",
    "No propagar supuestos como reglas definitivas.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Conservar incidencias históricas de salida no estructurada detectadas en ciclos previos.",
    "Normalizar manualmente memorias heredadas del ciclo 1 si se reutilizan.",
    "Propagar correcciones locales solo después de verificar archivos afectados.",
    "Evitar traslado de fuentes, casos o conceptos temáticos del nodo origen."
  ],
  "open_questions": [
    "Confirmar consigna textual de cada actividad antes de producir entregables.",
    "Confirmar rúbrica de evaluación específica por actividad.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar si el nombre editorial debe conservar publico sin acento o usar público con acento.",
    "Revisar nombres en README con caracteres anómalos.",
    "Corregir tokens sin expandir en README y programa analítico.",
    "Revisar y reparar posible corte de entorno tabular en el archivo de reporte .tex.",
    "Definir formato mínimo de conclusión jurídica por tipo de evidencia.",
    "Confirmar si se normaliza nomenclatura de archivos con caracteres acentuados.",
    "Supuesto: la bibliografía local canónica es bases-de-derecho-internacional-publico.bib."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Institucional sin rigidez excesiva.",
        "Conservador ante evidencia incompleta."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Carpeta de materia como entrada canónica.",
        "Normalización estructurada obligatoria antes de propagación.",
        "Fuentes provisionales tratadas como trazabilidad."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Bases de derecho internacional publico.",
        "Destino verificado: semestre 4, bloque 1, obligatoria, 8 créditos.",
        "Código local: LDE-S4B1.",
        "Usar solo contexto curricular verificado del destino.",
        "No mezclar contexto curricular de materias distintas."
      ]
    },
    "essence": [
      "Identidad institucional UnADM.",
      "Consigna de actividad como eje rector.",
      "Problema jurídico o social que activa la asignatura.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable.",
      "Análisis propio y postura académica.",
      "Conclusión transferible a la práctica jurídica.",
      "Consistencia entre cita y bibliografía.",
      "Normalización JSON antes de propagar.",
      "Separación entre plantilla, programa, bibliografía y producto final."
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
      "Transformar la planeación semanal en reportes, presentaciones y productos visuales.",
      "Evitar entregas descriptivas sin criterio jurídico propio.",
      "Garantizar integridad académica mediante fuentes verificables.",
      "Proteger la identidad local de la materia frente a transferencias transversales."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Encuadre breve del problema.",
      "Secciones funcionales y no redundantes.",
      "Marco normativo o doctrinal separado del análisis.",
      "Postura personal argumentada.",
      "Supuestos siempre etiquetados.",
      "Cierre con criterio jurídico aplicable.",
      "Lenguaje académico en español.",
      "Metadatos locales consistentes.",
      "Sin redacción literal heredada de materias no equivalentes."
    ],
    "argumentative_patterns": [
      "Consigna -> objetivo -> desarrollo alineado -> verificación final.",
      "Problema -> conceptos -> norma o doctrina -> análisis -> conclusión.",
      "Afirmación -> evidencia -> interpretación -> posición propia.",
      "Hechos -> regla aplicable -> razonamiento -> consecuencia jurídica.",
      "Fuente institucional -> ubicación curricular -> identidad del entregable.",
      "Vacío documental -> marca de supuesto -> pregunta abierta."
    ],
    "knowledge_graph": {
      "concepts": [
        "UnADM",
        "Licenciatura en Derecho",
        "Bases de derecho internacional publico",
        "LDE-S4B1",
        "Consigna de actividad",
        "Planeación semanal",
        "Problema jurídico o social",
        "Conceptos jurídicos",
        "Marco normativo o doctrinal",
        "Evidencia verificable",
        "Análisis propio",
        "Postura académica",
        "Conclusión transferible",
        "Integridad académica",
        "Consistencia cita-bibliografía",
        "Normalización JSON",
        "Plantilla LaTeX local",
        "Bibliografía local",
        "Malla curricular de Derecho",
        "Procedencia provisional"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Consigna de actividad",
          "target": "Planeación semanal",
          "kind": "depends_on",
          "justification": "La actividad debe ajustarse al producto solicitado por la planeación."
        },
        {
          "source": "Planeación semanal",
          "target": "Plantilla LaTeX local",
          "kind": "develops",
          "justification": "La plantilla se adapta según reporte, presentación o producto visual."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Marco normativo o doctrinal",
          "kind": "depends_on",
          "justification": "El marco se selecciona según el problema abordado."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Análisis propio",
          "kind": "supports",
          "justification": "El análisis requiere reglas, doctrina o datos pertinentes."
        },
        {
          "source": "Evidencia verificable",
          "target": "Postura académica",
          "kind": "supports",
          "justification": "La postura del estudiante debe estar sustentada."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión transferible",
          "kind": "develops",
          "justification": "La conclusión deriva del razonamiento jurídico aplicado."
        },
        {
          "source": "Consistencia cita-bibliografía",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Evita referencias rotas y afirmaciones sin fuente."
        },
        {
          "source": "Bibliografía local",
          "target": "Consistencia cita-bibliografía",
          "kind": "supports",
          "justification": "Las claves citadas deben existir en el .bib local."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia segura."
        },
        {
          "source": "Malla curricular de Derecho",
          "target": "Licenciatura en Derecho",
          "kind": "supports",
          "justification": "La malla curricular respalda la ubicación institucional local."
        },
        {
          "source": "Procedencia provisional",
          "target": "Identidad institucional UnADM",
          "kind": "contrasts",
          "justification": "Codex y GPT-Pro registran trazabilidad, no identidad del entregable."
        },
        {
          "source": "Bases de derecho internacional publico",
          "target": "Contenido temático de Filosofía del Derecho",
          "kind": "contrasts",
          "justification": "La transferencia transversal no debe mezclar materias no equivalentes."
        }
      ],
      "evidence": [
        "README local: materia de Licenciatura en Derecho de la UnADM.",
        "README local: semestre 4, bloque 1, obligatoria, 8 créditos.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: integridad académica, citas verificables y conclusión jurídica.",
        "Programa analítico local: claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
        "Bibliografía local: unadmSitioWeb.",
        "Bibliografía local: unadmMallaDerecho2024.",
        "Plantilla local: clase article con spanish, letterpaper y oneside.",
        "Memoria institucional heredada: revisar salidas no estructuradas antes de reutilizarlas.",
        "Memoria origen: bloquear propagación si la salida no es JSON parseable.",
        "Memoria origen: no inventar referencias y marcar supuestos."
      ]
    },
    "reinforcement_log": [
      "Ciclo 17 consolida reglas transversales sin importar contenido temático del origen.",
      "Se deduplican reglas repetidas de identidad, estructura, calidad, LaTeX y bibliografía.",
      "Se refuerza el uso exclusivo del contexto curricular local del destino.",
      "Se conserva la incidencia histórica de salidas no parseables.",
      "Se añade control explícito contra mezcla de fuentes de Filosofía del Derecho.",
      "Se mantiene la bibliografía local como fuente canónica de claves citables.",
      "Se elevan anomalías de README y LaTeX a preguntas abiertas verificables.",
      "Se preserva el patrón editorial problema-conceptos-evidencia-análisis-conclusión."
    ]
  }
}