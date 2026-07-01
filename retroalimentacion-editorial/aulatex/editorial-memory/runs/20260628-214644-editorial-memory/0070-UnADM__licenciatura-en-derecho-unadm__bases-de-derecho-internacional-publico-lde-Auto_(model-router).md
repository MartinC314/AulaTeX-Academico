{
  "summary": [
    "Materia destino consolidada con memoria editorial local.",
    "Sincronización transversal desde Filosofía del Derecho aplicada solo como abstracción estable.",
    "Identidad UnADM preservada para Licenciatura en Derecho.",
    "Contexto curricular local verificado: semestre 4, bloque 1, obligatoria, 8 créditos.",
    "Ejes editoriales reforzados: problema, conceptos, fuentes, análisis propio y conclusión jurídica.",
    "No se trasladan contenidos temáticos ni fuentes específicas de Filosofía del Derecho.",
    "Se mantiene normalización estructurada obligatoria antes de propagación recursiva.",
    "Se conserva incidencia histórica de salidas no parseables desde Codex y GPT-Pro.",
    "Plantilla base, programa analítico y bibliografía local ya definidos.",
    "Se detectan tokens sin expandir y nombres anómalos en README y programa analítico."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre local de la materia: Bases de derecho internacional publico.",
    "Alinear entregables a Licenciatura en Derecho, semestre 4, bloque 1, obligatoria, 8 créditos.",
    "Usar código de curso LDE-S4B1 en metadatos.",
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Conservar al alumno registrado en plantilla si no hay instrucción local que lo sustituya.",
    "No mezclar metadatos curriculares de materias origen.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar Codex y GPT-Pro como procedencia provisional, no como identidad del entregable.",
    "Citar malla-curricular-derecho-unadm.pdf como fuente de ubicación curricular."
  ],
  "structure_rules": [
    "Transformar la planeación semanal en el producto académico solicitado.",
    "Mantener el programa analítico como guía editorial de actividades.",
    "Conservar separación entre reporte, presentación, programa analítico y bibliografía.",
    "Distinguir reporte, presentación y producto visual según consigna.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar cada entrega con problema, conceptos, fuentes, análisis propio y conclusión jurídica.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Conservar la carpeta referencias-bases-de-derecho-internacional-publico como repositorio de apoyo."
  ],
  "activity_rules": [
    "Adaptar cada actividad al producto solicitado por la planeación semanal.",
    "Verificar correspondencia entre consigna, producto y programa analítico.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Distinguir hechos, argumentos, normas, doctrina, datos y criterio propio.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Integrar normas, doctrina o datos pertinentes al caso de actividad.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Evitar extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes.",
    "No asumir fuentes específicas sin confirmación local."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de propagar memoria.",
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Revisar consistencia entre instrucciones de actividad y programa analítico.",
    "Verificar que README, programa analítico, .bib y plantillas locales coincidan.",
    "Bloquear afirmaciones sin respaldo documental o normativo.",
    "Confirmar que todo supuesto esté marcado.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Validar citas y referencias antes de cerrar entregables.",
    "Validar sintaxis LaTeX y cierre de entornos antes de compilar.",
    "Marcar faltantes como pendientes sin sustituirlos por invenciones."
  ],
  "latex_rules": [
    "Reutilizar la plantilla .tex local de la materia como base de nuevas actividades.",
    "Usar reporte-bases-de-derecho-internacional-publico.tex para reportes base.",
    "Usar presentacion-bases-de-derecho-internacional-publico.tex solo para presentaciones.",
    "Completar metadatos de portada sin alterar identidad institucional.",
    "Definir título, subtítulo y subject coherentes con la actividad en curso.",
    "Mantener compatibilidad con clase article, spanish, letterpaper y oneside.",
    "Usar acentos y codificación correcta en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Conservar nombres de archivo locales salvo normalización acordada.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Reparar el entorno tabular truncado en la plantilla de reporte antes de compilar.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "No cambiar la estructura base de portada sin instrucción editorial."
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
    "No importar bibliografía temática de Filosofía del Derecho sin uso local confirmado."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar hacia arriba y laterales solo reglas verificadas y no duplicadas.",
    "Compartir solo abstracciones editoriales entre materias no equivalentes.",
    "Preservar reglas útiles previas aunque se reubiquen por categoría.",
    "Mantener compresión union-dedupe con criterio lossless.",
    "No propagar supuestos como reglas definitivas.",
    "No trasladar contenido temático específico del origen al destino.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Normalizar manualmente memorias heredadas de ciclos previos si se reutilizan.",
    "Conservar incidencias históricas de salida no estructurada detectadas en ciclos previos.",
    "Propagar correcciones locales solo después de verificar archivos afectados."
  ],
  "open_questions": [
    "Confirmar consignas específicas de actividades de la materia destino.",
    "Confirmar rúbricas de evaluación por actividad.",
    "Confirmar fuentes obligatorias de cada semana.",
    "Confirmar si el nombre editorial debe conservar publico sin acento o usar público con acento.",
    "Corregir nombres anómalos en README: reporte y referencias.",
    "Corregir tokens sin expandir en README y programa analítico.",
    "Confirmar nombre canónico final del archivo .bib local.",
    "Revisar y reparar corte de entorno tabular en reporte-bases-de-derecho-internacional-publico.tex.",
    "Definir formato mínimo de conclusión jurídica por tipo de evidencia.",
    "Validar si se normaliza nomenclatura de archivos con caracteres acentuados."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Institucional sin rigidez excesiva.",
        "Conservador ante datos no verificados."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Carpeta de materia como entrada canónica.",
        "Normalización estructurada obligatoria antes de propagación.",
        "Trazabilidad de procedencia sin contaminar identidad del entregable."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Bases de derecho internacional publico.",
        "Destino verificado: semestre 4, bloque 1, obligatoria, 8 créditos.",
        "Código local: LDE-S4B1.",
        "Usar solo contexto curricular verificado del nodo destino.",
        "No mezclar contexto curricular de materias distintas."
      ]
    },
    "essence": [
      "Identidad institucional UnADM.",
      "Bases de derecho internacional publico como materia destino.",
      "Problema jurídico o social que activa la actividad.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeación.",
      "Evidencia verificable.",
      "Análisis propio y postura académica.",
      "Conclusión transferible a la práctica jurídica.",
      "Consistencia cita-bibliografía.",
      "Normalización JSON para propagación segura."
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
      "Transformar la planeación semanal en reportes, presentaciones o productos visuales.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Evitar entregas solo descriptivas.",
      "Convertir la consigna local en estructura jurídica verificable.",
      "Preservar memoria editorial transversal sin importar contenido temático ajeno."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Encuadre breve del problema jurídico o social.",
      "Secciones funcionales y no redundantes.",
      "Marco normativo o doctrinal separado del análisis propio.",
      "Afirmaciones respaldadas con cita explícita.",
      "Supuestos siempre etiquetados.",
      "Cierre con criterio jurídico aplicable.",
      "Metadatos locales consistentes.",
      "Lenguaje académico en español correcto.",
      "Sin redacción literal heredada de materias no equivalentes."
    ],
    "argumentative_patterns": [
      "Consigna -> objetivo -> desarrollo alineado -> verificación final.",
      "Problema -> conceptos -> norma o doctrina -> análisis -> conclusión.",
      "Afirmación -> evidencia -> interpretación -> posición propia.",
      "Hechos -> norma aplicable -> valoración jurídica -> consecuencia.",
      "Fuente verificable -> cita en texto -> entrada .bib -> conclusión sustentada.",
      "Dato no visible -> supuesto marcado -> pendiente de confirmación.",
      "Producto solicitado -> formato adecuado -> plantilla local."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Licenciatura en Derecho",
        "Bases de derecho internacional publico",
        "Contexto curricular local",
        "Consigna de actividad",
        "Planeación semanal",
        "Producto académico solicitado",
        "Problema jurídico o social",
        "Conceptos clave",
        "Marco normativo o doctrinal",
        "Evidencia verificable",
        "Análisis propio",
        "Postura académica",
        "Conclusión jurídica transferible",
        "Integridad académica",
        "Consistencia cita-bibliografía",
        "Bibliografía local",
        "Normalización JSON",
        "Propagación recursiva",
        "Tokens sin expandir",
        "Plantilla LaTeX local"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Contexto curricular local",
          "target": "Identidad institucional UnADM",
          "kind": "supports",
          "justification": "El README ubica la materia dentro de la Licenciatura en Derecho de la UnADM."
        },
        {
          "source": "unadmMallaDerecho2024",
          "target": "Contexto curricular local",
          "kind": "supports",
          "justification": "La malla curricular respalda semestre, bloque, tipo y créditos."
        },
        {
          "source": "Consigna de actividad",
          "target": "Producto académico solicitado",
          "kind": "depends_on",
          "justification": "El formato final depende de lo pedido en la planeación."
        },
        {
          "source": "Planeación semanal",
          "target": "Estructura argumentativa jurídica",
          "kind": "develops",
          "justification": "El programa analítico indica transformar la planeación en productos académicos."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Conceptos clave",
          "kind": "develops",
          "justification": "El problema delimita los conceptos pertinentes."
        },
        {
          "source": "Conceptos clave",
          "target": "Marco normativo o doctrinal",
          "kind": "develops",
          "justification": "Los conceptos orientan la selección de normas, doctrina o datos."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Análisis propio",
          "kind": "supports",
          "justification": "El análisis debe fundarse en fuentes jurídicas verificables."
        },
        {
          "source": "Evidencia verificable",
          "target": "Postura académica",
          "kind": "supports",
          "justification": "La postura estudiantil requiere respaldo documental."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "develops",
          "justification": "La conclusión sintetiza el criterio jurídico aplicable."
        },
        {
          "source": "Consistencia cita-bibliografía",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La coincidencia entre citas y .bib evita referencias rotas o inventadas."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia segura de memoria."
        },
        {
          "source": "Tokens sin expandir",
          "target": "Plantilla LaTeX local",
          "kind": "contrasts",
          "justification": "Los tokens pendientes contradicen la compilación y nomenclatura estables."
        },
        {
          "source": "Bibliografía local",
          "target": "Producto académico solicitado",
          "kind": "supports",
          "justification": "Cada actividad debe registrar sus fuentes verificables en el .bib local."
        }
      ],
      "evidence": [
        "README destino: materia de la Licenciatura en Derecho de la UnADM.",
        "README destino: semestre 4, bloque 1, obligatoria, 8 créditos.",
        "README destino: fuente curricular malla-curricular-derecho-unadm.pdf.",
        "README destino: carpeta como punto de entrada canónico.",
        "README destino: pauta de identidad UnADM, integridad académica, citas verificables y conclusión jurídica.",
        "Programa analítico destino: productos académicos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico destino: ejes de problema, conceptos, producto, análisis propio y conclusión.",
        "Programa analítico destino: bibliografía específica debe agregarse al .bib local.",
        "bases-de-derecho-internacional-publico.bib: entradas unadmSitioWeb y unadmMallaDerecho2024.",
        "Reporte LaTeX destino: clase article con spanish, letterpaper y oneside.",
        "Reporte LaTeX destino: metadatos de curso LDE-S4B1.",
        "Reporte LaTeX destino: entorno tabular truncado detectado.",
        "Memoria heredada: salida sin JSON parseable desde Codex.",
        "Memoria destino previa: salida sin JSON parseable desde GPT-Pro."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2 consolida memoria local sin regresión.",
      "Se deduplican reglas repetidas por equivalencia semántica.",
      "Se preservan reglas útiles previas de identidad, estructura, calidad, LaTeX y bibliografía.",
      "Se refuerza el eje transversal problema-conceptos-evidencia-análisis-conclusión.",
      "Se evita trasladar fuentes y contenidos temáticos de Filosofía del Derecho.",
      "Se mantiene el contexto curricular verificado del destino.",
      "Se elevan tokens sin expandir y entorno tabular truncado a pendientes operativos.",
      "Se corrigen relaciones del grafo a tipos permitidos.",
      "Se conserva trazabilidad de Codex y GPT-Pro como procedencia provisional.",
      "Se fija normalización JSON como puerta de propagación recursiva."
    ]
  }
}