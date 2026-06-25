{
  "summary": [
    "Memoria editorial consolidada para la materia Bases de derecho internacional publico.",
    "Se preserva identidad UnADM y contexto curricular local verificado.",
    "Se refuerzan ejes transversales: problema, conceptos, fuentes, análisis propio y conclusión jurídica.",
    "Se conserva la normalización estructurada antes de toda propagación.",
    "Se aplica compresión por unión y deduplicación sin eliminar reglas útiles.",
    "Se evita transferir contenido temático específico de Filosofía del Derecho.",
    "Se mantiene incidencia histórica de salidas no parseables desde Codex y GPT-Pro.",
    "Supuesto: el destino usa como base los archivos locales ya existentes."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, tono y metadatos.",
    "Usar nombre local de la materia: Bases de derecho internacional publico.",
    "Alinear entregables a Licenciatura en Derecho, semestre 4, bloque 1, obligatoria, 8 créditos.",
    "Usar código local LDE-S4B1 en metadatos cuando aplique.",
    "Usar la carpeta de materia como punto de entrada canónico.",
    "No mezclar metadatos curriculares del origen con el destino.",
    "Conservar al alumno registrado en plantilla salvo instrucción local contraria.",
    "Marcar como supuesto cualquier dato no visible en consigna, README, programa o archivo local.",
    "Tratar Codex y GPT-Pro como procedencia provisional, no como autoridad editorial.",
    "Citar la malla curricular UnADM solo como fuente de ubicación curricular verificada."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Integrar fuentes verificables dentro del desarrollo, no como adorno final.",
    "Alinear cada entrega al producto solicitado por la planeación semanal.",
    "Distinguir reporte, presentación y producto visual según consigna.",
    "Mantener el programa analítico como guía editorial de actividades.",
    "Conservar separación entre reporte, presentación, programa analítico y bibliografía.",
    "Usar la carpeta referencias-bases-de-derecho-internacional-publico como repositorio de apoyo.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Adaptar cada actividad al producto solicitado por la planeación semanal.",
    "Incluir postura académica propia, no solo resumen descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Distinguir hechos, argumentos, normas, doctrina y criterio propio.",
    "Integrar conceptos, normas, doctrina o datos pertinentes al caso.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Evitar extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna, rúbrica o evidencia como pendientes.",
    "No asumir que bibliografía de otra materia corresponde a esta materia.",
    "Convertir la planeación en reporte, presentación o producto visual según consigna."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Validar consistencia entre instrucciones de actividad y programa analítico.",
    "Bloquear afirmaciones sin respaldo documental o sin marca de supuesto.",
    "Validar correspondencia entre citas en texto y entradas del .bib local.",
    "Validar sintaxis LaTeX y cierre de entornos antes de compilar.",
    "Verificar que README, programa analítico, .bib y plantillas locales coincidan.",
    "Marcar faltantes como pendientes sin sustituirlos por invenciones.",
    "Auditar incidencias históricas de parseo antes de nueva propagación."
  ],
  "latex_rules": [
    "Reutilizar la plantilla .tex local de la materia como base de nuevas actividades.",
    "Usar reporte-bases-de-derecho-internacional-publico.tex para reportes.",
    "Usar presentacion-bases-de-derecho-internacional-publico.tex solo para presentaciones.",
    "Mantener compatibilidad con clase article, spanish, letterpaper y oneside.",
    "Completar título, subtítulo y subject coherentes con la actividad.",
    "No cambiar estructura base de portada sin instrucción editorial.",
    "Usar acentos y codificación correcta en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Reparar entornos tabular incompletos antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir caracteres anómalos en rutas o nombres de archivo antes de referenciarlos.",
    "Conservar nombres de archivo locales salvo normalización acordada."
  ],
  "bibliography_rules": [
    "Registrar fuentes de actividad en bases-de-derecho-internacional-publico.bib.",
    "Priorizar fuentes institucionales UnADM y documentos jurídicos verificables.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Agregar entradas BibTeX específicas solo cuando la fuente exista y sea verificable.",
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Validar que toda clave citada exista en el .bib local.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Marcar referencias faltantes como pendientes.",
    "Supuesto: el archivo .bib canónico local es bases-de-derecho-internacional-publico.bib porque existe en la carpeta destino."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas y no duplicadas.",
    "Compartir solo abstracciones editoriales estables entre materias no equivalentes.",
    "No propagar contenido temático específico de Filosofía del Derecho.",
    "Preservar reglas útiles previas aunque se reubiquen por categoría.",
    "Aplicar compresión union-dedupe con criterio lossless.",
    "No propagar supuestos como reglas definitivas.",
    "Propagar correcciones locales solo después de verificar archivos afectados.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Conservar incidencias históricas de salida no estructurada de ciclos previos.",
    "Ciclo 1 requiere normalización manual si se reutiliza."
  ],
  "open_questions": [
    "Confirmar consigna textual de cada actividad antes de producir entregables.",
    "Confirmar rúbrica de evaluación específica por actividad.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar si el nombre editorial debe usar publico sin acento o público con acento.",
    "Revisar nombres en README con caracteres anómalos.",
    "Corregir tokens sin expandir en README y programa analítico.",
    "Reparar corte del entorno tabular en el archivo de reporte .tex.",
    "Confirmar si se normalizarán rutas y nombres de archivo con acentos.",
    "Confirmar alcance de la carpeta de referencias locales.",
    "Supuesto: no hay todavía bibliografía temática internacional pública distinta de las fuentes institucionales locales."
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
        "Normalización estructurada obligatoria.",
        "Trazabilidad de fuentes provisionales.",
        "Consistencia entre portada, metadatos, programa y bibliografía."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Bases de derecho internacional publico.",
        "Semestre 4, bloque 1.",
        "Obligatoria, 8 créditos.",
        "Código local: LDE-S4B1.",
        "Contexto curricular verificado localmente.",
        "No mezclar contexto curricular de materias distintas."
      ]
    },
    "essence": [
      "Identidad institucional UnADM.",
      "Consigna de actividad como eje rector.",
      "Problema jurídico o social contextualizado.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Fuentes verificables y trazables.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible.",
      "Normalización JSON antes de propagación.",
      "Consistencia cita-bibliografía.",
      "Estrategia conservadora ante vacíos."
    ],
    "reason_for_being": [
      "Orientar productos académicos de Bases de derecho internacional publico con claridad, fundamento jurídico y transferencia profesional.",
      "Transformar la planeación semanal en reportes, presentaciones o productos visuales alineados con la consigna.",
      "Convertir fuentes verificables en argumentos jurídicos propios.",
      "Evitar entregables descriptivos sin criterio académico.",
      "Proteger la identidad local de la materia frente a transferencias transversales.",
      "Asegurar que toda propagación sea estructurada, parseable y verificable."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Encuadre breve del problema.",
      "Secciones funcionales y no redundantes.",
      "Distinción entre norma, doctrina, hechos y criterio propio.",
      "Citas explícitas junto a afirmaciones sustantivas.",
      "Supuestos siempre etiquetados.",
      "Cierre con criterio jurídico aplicable.",
      "Metadatos locales consistentes.",
      "Lenguaje académico en español.",
      "Sin traslado literal de redacción de nodos origen."
    ],
    "argumentative_patterns": [
      "Consigna -> objetivo -> desarrollo alineado -> verificación final.",
      "Problema -> conceptos -> norma o doctrina -> análisis -> conclusión.",
      "Afirmación -> evidencia -> interpretación -> posición propia.",
      "Fuente verificable -> regla aplicable -> implicación jurídica.",
      "Hecho relevante -> marco jurídico -> valoración académica.",
      "Vacío de evidencia -> supuesto marcado -> pregunta abierta.",
      "Producto solicitado -> formato adecuado -> revisión de cumplimiento."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Bases de derecho internacional publico",
        "Licenciatura en Derecho",
        "Semestre 4 bloque 1",
        "Código LDE-S4B1",
        "Consigna de actividad",
        "Planeación semanal",
        "Problema jurídico o social",
        "Conceptos jurídicos pertinentes",
        "Marco normativo o doctrinal",
        "Evidencia verificable",
        "Análisis propio",
        "Postura académica",
        "Conclusión jurídica transferible",
        "Consistencia cita-bibliografía",
        "Normalización JSON",
        "Propagación recursiva",
        "Fuentes provisionales",
        "Plantilla LaTeX local",
        "Bibliografía local"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Bases de derecho internacional publico",
          "kind": "supports",
          "justification": "La materia destino pertenece a la Licenciatura en Derecho de la UnADM."
        },
        {
          "source": "Malla curricular UnADM",
          "target": "Semestre 4 bloque 1",
          "kind": "supports",
          "justification": "La ubicación curricular local se declara en README y bibliografía base."
        },
        {
          "source": "Consigna de actividad",
          "target": "Producto académico",
          "kind": "depends_on",
          "justification": "El formato final debe responder al producto solicitado."
        },
        {
          "source": "Planeación semanal",
          "target": "Estructura argumentativa jurídica",
          "kind": "develops",
          "justification": "La planeación orienta secciones, profundidad y producto."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "El problema activa la interpretación y la postura académica."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Análisis propio",
          "kind": "supports",
          "justification": "El análisis requiere fundamento jurídico o doctrinal verificable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión válida depende del respaldo documental."
        },
        {
          "source": "Consistencia cita-bibliografía",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Evita citas huérfanas, referencias inventadas y afirmaciones sin fuente."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia segura."
        },
        {
          "source": "Fuentes provisionales",
          "target": "Autoridad editorial",
          "kind": "contrasts",
          "justification": "Codex y GPT-Pro se conservan como trazabilidad, no como fuente de autoridad."
        },
        {
          "source": "Plantilla LaTeX local",
          "target": "Producto académico",
          "kind": "supports",
          "justification": "La plantilla preserva portada, metadatos y estructura institucional."
        },
        {
          "source": "Bibliografía local",
          "target": "Consistencia cita-bibliografía",
          "kind": "supports",
          "justification": "El .bib local concentra las claves citables de la materia."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 4, bloque 1, obligatoria, 8 créditos.",
        "README local: carpeta como punto de entrada canónico.",
        "Programa analítico local: claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: transformar planeación semanal en productos académicos.",
        "Programa analítico local: ejes de problema, conceptos, fuentes, análisis propio y cierre.",
        "bases-de-derecho-internacional-publico.bib: entrada unadmSitioWeb.",
        "bases-de-derecho-internacional-publico.bib: entrada unadmMallaDerecho2024.",
        "Plantilla local de reporte: curso Bases de derecho internacional publico.",
        "Plantilla local de reporte: código LDE-S4B1.",
        "Incidencia heredada: salida sin JSON parseable desde Codex.",
        "Incidencia heredada: salida sin JSON parseable desde GPT-Pro.",
        "Regla transversal heredada: revisar respuestas no estructuradas antes de aplicar aguas abajo."
      ]
    },
    "reinforcement_log": [
      "Ciclo 21 consolida materia destino con estrategia progresiva y conservadora.",
      "Se deduplican reglas equivalentes sin recortar contenido útil.",
      "Se preserva contexto curricular local y se excluyen metadatos de Filosofía del Derecho.",
      "Se transfieren solo patrones editoriales transversales.",
      "Se refuerza el eje problema-conceptos-evidencia-análisis-conclusión.",
      "Se mantiene bloqueo de propagación ante JSON no parseable.",
      "Se refuerza la validación cita-bibliografía en el .bib local.",
      "Se registra como pendiente la reparación de tokens y caracteres anómalos.",
      "Se conserva trazabilidad de fuentes provisionales sin convertirlas en autoridad.",
      "Se deja abierta la confirmación de consigna, rúbrica y fuentes obligatorias por actividad."
    ]
  }
}