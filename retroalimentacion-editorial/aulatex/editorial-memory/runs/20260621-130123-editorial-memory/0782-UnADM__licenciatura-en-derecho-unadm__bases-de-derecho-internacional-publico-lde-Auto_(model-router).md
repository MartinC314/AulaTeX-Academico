{
  "summary": [
    "Materia destino consolidada con identidad UnADM y contexto curricular local.",
    "Asignatura destino: Bases de derecho internacional público.",
    "Contexto local verificado: Licenciatura en Derecho, semestre 4, bloque 1, obligatoria, 8 créditos.",
    "Se preservan plantilla base, programa analítico y bibliografía local.",
    "Se refuerzan ejes transversales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se transfiere solo abstracción editorial estable desde Filosofía del Derecho.",
    "No se trasladan contenidos temáticos específicos del origen.",
    "Se mantiene normalización estructurada obligatoria antes de propagación.",
    "Se conserva incidencia histórica de salidas no parseables.",
    "Se aplica compresión union-dedupe sin regresión."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local: Bases de derecho internacional público.",
    "Conservar código local LDE-S4B1 en metadatos.",
    "Alinear entregables a Licenciatura en Derecho, semestre 4, bloque 1, obligatoria, 8 créditos.",
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Conservar al alumno registrado en plantilla si no hay instrucción local que lo sustituya.",
    "Citar malla-curricular-derecho-unadm.pdf como fuente de ubicación curricular.",
    "Tratar Codex y GPT-Pro como procedencia provisional, no como identidad del entregable.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "No mezclar metadatos curriculares de Filosofía del Derecho con la materia destino."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar cada entrega con problema, conceptos, fuentes, análisis propio y conclusión jurídica.",
    "Separar conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Transformar la planeación semanal en el producto académico solicitado.",
    "Distinguir reporte, presentación y producto visual según la consigna.",
    "Mantener el programa analítico como guía editorial de actividades.",
    "Conservar separación entre reporte, presentación, programa analítico y bibliografía.",
    "Conservar referencias-bases-de-derecho-internacional-publico como repositorio de apoyo.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Adaptar cada actividad al producto solicitado por la planeación semanal.",
    "Verificar correspondencia entre consigna, producto y formato final.",
    "Incluir postura académica propia sustentada en fuentes verificables.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Distinguir hechos, argumentos, normas, doctrina, datos y criterio propio.",
    "Sustentar afirmaciones con cita explícita.",
    "Integrar normas, doctrina o datos pertinentes cuando correspondan.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Evitar extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna, rúbrica o evidencia como pendientes.",
    "No asumir fuentes de otra asignatura como fuentes locales.",
    "No trasladar contenido temático de Filosofía del Derecho a Derecho Internacional Público."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de propagar memoria.",
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar respuestas no estructuradas antes de reutilizarlas.",
    "Mantener auditoría de parseo JSON antes de nueva propagación.",
    "Revisar consistencia entre instrucciones de actividad y programa analítico.",
    "Verificar que README, programa analítico, .bib y plantillas locales coincidan.",
    "Bloquear afirmaciones sin respaldo documental o marca de supuesto.",
    "Validar citas en texto contra el archivo .bib local.",
    "Validar referencias antes de cerrar entregables.",
    "Validar sintaxis LaTeX y cierre de entornos antes de compilar.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Marcar faltantes como pendientes sin sustituirlos por invenciones.",
    "Preservar reglas útiles previas aunque se reubiquen por categoría."
  ],
  "latex_rules": [
    "Reutilizar la plantilla .tex local como base de nuevas actividades.",
    "Usar reporte-bases-de-derecho-internacional-publico.tex para reportes.",
    "Usar presentacion-bases-de-derecho-internacional-publico.tex solo para presentaciones.",
    "Mantener compatibilidad con clase article, spanish, letterpaper y oneside.",
    "Completar metadatos de portada sin alterar identidad institucional.",
    "Definir título, subtítulo y subject coherentes con la actividad.",
    "No cambiar la estructura base de portada sin instrucción editorial.",
    "Usar acentos y codificación correcta en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Conservar nombres de archivo locales salvo normalización acordada.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Revisar y cerrar correctamente entornos tabular antes de compilar.",
    "Reparar el corte visible en \\end{tabular} del reporte base antes de usarlo como plantilla."
  ],
  "bibliography_rules": [
    "Registrar fuentes de actividad en bases-de-derecho-internacional-publico.bib.",
    "Priorizar fuentes institucionales UnADM y documentos jurídicos verificables.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Agregar entradas BibTeX específicas solo cuando la fuente exista y sea verificable.",
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "Marcar referencias faltantes como pendientes.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Validar que las claves citadas existan en el .bib local.",
    "No asumir bibliografía de Filosofía del Derecho como bibliografía del destino.",
    "No asumir fuentes de semanas posteriores sin confirmación local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas y no duplicadas.",
    "Compartir solo abstracciones editoriales estables entre materias no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferir redacción literal entre nodos no equivalentes.",
    "No propagar supuestos como reglas definitivas.",
    "No trasladar contexto curricular del origen al destino.",
    "No trasladar contenido temático específico de Filosofía del Derecho.",
    "Propagar correcciones locales solo después de verificar archivos afectados.",
    "Mantener compresión union-dedupe con criterio lossless.",
    "Conservar incidencias históricas de salida no estructurada.",
    "Normalizar manualmente memorias heredadas del ciclo 1 si se reutilizan.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local."
  ],
  "open_questions": [
    "Confirmar consignas específicas de actividades de la materia destino.",
    "Confirmar rúbricas de evaluación por actividad.",
    "Confirmar fuentes obligatorias de cada semana.",
    "Definir formato mínimo de conclusión jurídica por tipo de evidencia.",
    "Confirmar si el nombre editorial debe usar público con acento en títulos visibles.",
    "Confirmar si los nombres de archivo deben conservar publico sin acento por compatibilidad.",
    "Revisar nombres en README con caracteres anómalos.",
    "Corregir tokens sin expandir en README y programa analítico.",
    "Confirmar sustitución del token Slug por bases-de-derecho-internacional-publico.bib.",
    "Revisar y reparar el corte del entorno tabular en el reporte .tex.",
    "Confirmar si referencias-bases-de-derecho-internacional-publico contiene fuentes locales adicionales.",
    "Confirmar si existen actividades ya creadas que deban heredar esta memoria."
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
        "Trazabilidad de fuentes provisionales sin convertirlas en autoridad.",
        "Consistencia entre portada, metadatos, programa y bibliografía."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Bases de derecho internacional público.",
        "Semestre 4, bloque 1.",
        "Obligatoria, 8 créditos.",
        "Código local: LDE-S4B1.",
        "Contexto curricular verificado localmente.",
        "No mezclar contexto curricular de materias distintas."
      ]
    },
    "essence": [
      "Identidad institucional UnADM.",
      "Consigna de actividad.",
      "Problema jurídico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable.",
      "Análisis propio y postura académica.",
      "Conclusión jurídica transferible.",
      "Consistencia cita-bibliografía.",
      "Normalización JSON antes de propagación.",
      "Conservadurismo editorial ante faltantes."
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
      "Transformar la planeación semanal en reportes, presentaciones y productos visuales.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Garantizar que cada entrega responda a la consigna local.",
      "Sostener integridad académica mediante fuentes verificables.",
      "Convertir el cierre en criterio jurídico aplicable."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Encuadre breve del problema.",
      "Secciones funcionales y no redundantes.",
      "Diferenciación entre norma, doctrina, datos y criterio propio.",
      "Citas explícitas para afirmaciones sustantivas.",
      "Supuestos siempre etiquetados.",
      "Cierre con criterio jurídico aplicable.",
      "Metadatos locales consistentes.",
      "Sin redacción temática importada de otra materia.",
      "Sin fuentes inventadas."
    ],
    "argumentative_patterns": [
      "Consigna -> objetivo -> desarrollo alineado -> verificación final.",
      "Problema -> conceptos -> norma o doctrina -> análisis -> conclusión.",
      "Afirmación -> evidencia -> interpretación -> postura propia.",
      "Hechos -> marco jurídico -> valoración -> consecuencia jurídica.",
      "Fuente verificable -> cita explícita -> uso argumentativo.",
      "Faltante detectado -> marca de pendiente -> no invención.",
      "Contexto local -> producto solicitado -> formato adecuado.",
      "Conclusión -> transferencia a la práctica jurídica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Bases de derecho internacional público",
        "Licenciatura en Derecho",
        "Semestre 4 bloque 1",
        "Código LDE-S4B1",
        "Consigna de actividad",
        "Planeación semanal",
        "Producto académico solicitado",
        "Problema jurídico o social",
        "Conceptos jurídicos pertinentes",
        "Marco normativo o doctrinal",
        "Evidencia verificable",
        "Análisis propio",
        "Postura académica",
        "Conclusión jurídica transferible",
        "Integridad académica",
        "Consistencia cita-bibliografía",
        "Bibliografía local",
        "Normalización JSON",
        "Propagación recursiva conservadora",
        "Tokens sin expandir",
        "Caracteres anómalos en README",
        "Cierre de entornos LaTeX"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Portada y metadatos",
          "kind": "develops",
          "justification": "La pauta local exige conservar identidad UnADM en cada actividad."
        },
        {
          "source": "Malla curricular de Derecho",
          "target": "Semestre 4 bloque 1",
          "kind": "supports",
          "justification": "El README local la declara como fuente de ubicación curricular."
        },
        {
          "source": "Consigna de actividad",
          "target": "Producto académico solicitado",
          "kind": "depends_on",
          "justification": "El formato final debe derivarse de la planeación semanal."
        },
        {
          "source": "Producto académico solicitado",
          "target": "Reporte o presentación",
          "kind": "develops",
          "justification": "Las plantillas locales separan reportes y presentaciones."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Marco normativo o doctrinal",
          "kind": "develops",
          "justification": "El encuadre inicial orienta la selección de normas, doctrina o datos."
        },
        {
          "source": "Evidencia verificable",
          "target": "Análisis propio",
          "kind": "supports",
          "justification": "La postura académica debe sostenerse en fuentes consultables."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "develops",
          "justification": "El cierre debe derivarse del razonamiento presentado."
        },
        {
          "source": "Consistencia cita-bibliografía",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Evita referencias rotas y afirmaciones sin respaldo."
        },
        {
          "source": "Bibliografía local",
          "target": "Citas en texto",
          "kind": "supports",
          "justification": "Cada clave citada debe existir en bases-de-derecho-internacional-publico.bib."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva conservadora",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia segura."
        },
        {
          "source": "Tokens sin expandir",
          "target": "Compilación confiable",
          "kind": "contrasts",
          "justification": "Los tokens no resueltos rompen referencias editoriales y nombres esperados."
        },
        {
          "source": "Cierre de entornos LaTeX",
          "target": "Compilación confiable",
          "kind": "supports",
          "justification": "El reporte base muestra un entorno tabular cortado que debe repararse."
        },
        {
          "source": "Filosofía del Derecho",
          "target": "Bases de derecho internacional público",
          "kind": "contrasts",
          "justification": "La relación es transversal, no equivalente; solo se comparten abstracciones editoriales."
        }
      ],
      "evidence": [
        "README destino: materia de la Licenciatura en Derecho de la UnADM.",
        "README destino: semestre 4, bloque 1, obligatoria, 8 créditos.",
        "README destino: fuente curricular malla-curricular-derecho-unadm.pdf.",
        "README destino: carpeta como punto de entrada canónico.",
        "README destino: identidad UnADM, integridad académica, citas verificables y conclusión jurídica.",
        "Programa analítico destino: claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico destino: transformar planeación semanal en reportes, presentaciones y productos visuales.",
        "Programa analítico destino: ejes de problema, conceptos, producto, análisis propio y conclusión.",
        "Bibliografía local: claves unadmSitioWeb y unadmMallaDerecho2024.",
        "Reporte local: clase article, spanish, letterpaper y oneside.",
        "Reporte local: metadatos de curso Bases de derecho internacional publico y código LDE-S4B1.",
        "Reporte local: corte visible en entorno tabular pendiente de reparación.",
        "README y programa local: token $(@{...}.Slug) pendiente de resolución.",
        "Memoria heredada: salida sin JSON parseable desde Codex.",
        "Memoria destino previa: salida sin JSON parseable desde GPT-Pro."
      ]
    },
    "reinforcement_log": [
      "Ciclo 20: se consolidó memoria de materia destino con deduplicación semántica.",
      "Ciclo 20: se preservó contexto curricular local verificado.",
      "Ciclo 20: se reforzó transferencia transversal conservadora.",
      "Ciclo 20: se evitaron contenidos temáticos específicos de Filosofía del Derecho.",
      "Ciclo 20: se mantuvo regla de no propagar salidas no parseables.",
      "Ciclo 20: se reforzó validación cita-bibliografía.",
      "Ciclo 20: se registró reparación pendiente de tokens y entorno tabular.",
      "Ciclo 20: se conservaron fuentes institucionales locales existentes.",
      "Ciclo 20: se mantuvo trazabilidad de Codex y GPT-Pro como procedencia provisional.",
      "Ciclo 20: se reforzó ADN editorial: problema, evidencia, análisis propio y conclusión transferible."
    ]
  }
}