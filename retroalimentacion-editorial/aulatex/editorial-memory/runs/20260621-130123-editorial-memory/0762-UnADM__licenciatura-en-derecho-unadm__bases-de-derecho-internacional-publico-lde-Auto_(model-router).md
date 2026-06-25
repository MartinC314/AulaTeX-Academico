{
  "summary": [
    "Materia destino consolidada con identidad UnADM y contexto curricular local.",
    "Asignatura destino: Bases de derecho internacional publico.",
    "Ubicación local verificada: semestre 4, bloque 1, obligatoria, 8 créditos.",
    "Código local verificado en plantilla: LDE-S4B1.",
    "Plantilla base, programa analítico y bibliografía local definidos.",
    "Se preservan ejes transversales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se aplica transferencia transversal conservadora desde Filosofía del Derecho.",
    "No se trasladan contenidos temáticos específicos de Filosofía del Derecho.",
    "Se conserva incidencia histórica de salidas no JSON parseable.",
    "Se refuerza normalización estructurada antes de propagación recursiva.",
    "Se mantiene compresión union-dedupe sin regresión."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial/local de la materia: Bases de derecho internacional publico.",
    "Alinear entregables a Licenciatura en Derecho, semestre 4, bloque 1, obligatoria, 8 créditos.",
    "Usar código local LDE-S4B1 en metadatos.",
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Conservar al alumno registrado en plantilla si no hay instrucción local que lo sustituya.",
    "Tratar Codex y GPT-Pro como procedencia provisional, no como identidad del entregable.",
    "Marcar como supuesto cualquier dato no visible en consigna local.",
    "No mezclar metadatos curriculares del origen con el destino.",
    "Usar solo contexto curricular verificado en README, programa analítico o malla curricular local."
  ],
  "structure_rules": [
    "Transformar la planeación semanal en el producto académico solicitado.",
    "Mantener programa analítico como guía editorial de actividades.",
    "Conservar separación entre reporte, presentación, programa analítico y bibliografía.",
    "Distinguir reporte, presentación y producto visual según consigna.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Integrar fuentes dentro del desarrollo, no solo al final.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Conservar carpeta referencias-bases-de-derecho-internacional-publico como repositorio de apoyo."
  ],
  "activity_rules": [
    "Adaptar cada actividad al producto solicitado por la planeación semanal.",
    "Verificar que el producto corresponda a la consigna local.",
    "Incluir postura académica propia sustentada en fuentes verificables.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Distinguir hechos, argumentos, normas, doctrina y criterio propio.",
    "Integrar conceptos, normas, doctrina o datos pertinentes al caso.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Cerrar con conclusión transferible a la práctica jurídica.",
    "Evitar extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de propagar memoria.",
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Revisar consistencia entre instrucciones de actividad y programa analítico.",
    "Verificar que README, programa analítico, .bib y plantillas locales coincidan.",
    "Bloquear afirmaciones sin respaldo documental, normativo o marca de supuesto.",
    "Validar citas y referencias antes de cerrar entregables.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Validar sintaxis LaTeX y cierre de entornos antes de compilar.",
    "Revisar nombres de archivos con caracteres anómalos antes de referenciarlos.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) antes de compilar o documentar.",
    "Marcar faltantes como pendientes sin sustituirlos por invenciones.",
    "Mantener auditoría de parseo JSON antes de nueva propagación."
  ],
  "latex_rules": [
    "Reutilizar la plantilla .tex local de la materia como base de nuevas actividades.",
    "Usar reporte-bases-de-derecho-internacional-publico.tex para reportes base.",
    "Usar presentacion-bases-de-derecho-internacional-publico.tex solo para presentaciones.",
    "Completar metadatos de portada sin alterar identidad institucional.",
    "Definir título, subtítulo y subject coherentes con la actividad en curso.",
    "Mantener compatibilidad con clase article, spanish, letterpaper y oneside.",
    "No cambiar estructura base de portada sin instrucción editorial.",
    "Usar acentos y codificación correcta en .tex y .bib.",
    "Conservar nombres de archivo locales salvo normalización acordada.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir en README y programa analítico.",
    "Revisar y cerrar correctamente entornos tabular antes de compilar.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas."
  ],
  "bibliography_rules": [
    "Registrar fuentes de actividad en bases-de-derecho-internacional-publico.bib.",
    "Priorizar fuentes institucionales UnADM y documentos jurídicos verificables.",
    "Conservar la malla curricular de Derecho como fuente institucional local.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Agregar entradas BibTeX específicas solo cuando la fuente exista y sea verificable.",
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "Marcar referencias faltantes como pendientes.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Validar que las claves citadas existan en el .bib local.",
    "Validar correspondencia entre citas en texto y bibliografía local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas y no duplicadas.",
    "Compartir solo abstracciones editoriales estables entre materias no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferir redacción literal de actividades origen.",
    "No propagar supuestos como reglas definitivas.",
    "No trasladar contenido temático específico de Filosofía del Derecho.",
    "Preservar reglas útiles previas aunque se reubiquen por categoría.",
    "Mantener compresión union-dedupe con criterio lossless.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Propagar correcciones locales solo después de verificar archivos afectados.",
    "Conservar incidencias históricas de salida no estructurada detectadas en ciclos previos.",
    "Normalizar manualmente memorias heredadas de ciclo 1 si se reutilizan."
  ],
  "open_questions": [
    "Confirmar consigna textual de cada actividad local antes de producir entregables.",
    "Confirmar formato exacto por actividad: reporte, presentación o producto visual.",
    "Confirmar rúbrica de evaluación específica por actividad.",
    "Confirmar fuentes obligatorias de cada semana.",
    "Confirmar criterio editorial sobre publico sin acento frente a público con acento.",
    "Revisar nombres en README con caracteres anómalos.",
    "Corregir tokens sin expandir en README y programa analítico.",
    "Revisar y reparar corte de entorno tabular en reporte .tex.",
    "Confirmar si la carpeta referencias-bases-de-derecho-internacional-publico tiene fuentes verificables adicionales.",
    "Definir formato mínimo de conclusión jurídica por tipo de evidencia."
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
      "Contexto curricular local verificado.",
      "Consigna de actividad como eje rector.",
      "Problema jurídico o social inicial.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable.",
      "Análisis propio y postura académica.",
      "Conclusión jurídica transferible.",
      "Consistencia cita-bibliografía.",
      "Normalización estructurada antes de propagación."
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
      "Transformar planeación semanal en reporte, presentación o producto visual según consigna.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Sostener entregables jurídicos verificables y no meramente descriptivos.",
      "Preservar un cerebro editorial estable para actividades futuras de la materia."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Encuadre jurídico breve.",
      "Secciones funcionales y no redundantes.",
      "Norma y doctrina separadas del criterio propio.",
      "Afirmaciones con cita explícita.",
      "Supuestos siempre etiquetados.",
      "Cierre con criterio jurídico aplicable.",
      "Metadatos institucionales consistentes.",
      "Sin traslado temático indebido entre materias."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> norma/doctrina -> análisis -> conclusión.",
      "Consigna -> producto esperado -> desarrollo alineado -> verificación final.",
      "Afirmación -> evidencia -> interpretación -> postura propia.",
      "Hecho -> norma aplicable -> razonamiento jurídico -> consecuencia práctica.",
      "Fuente institucional -> ubicación curricular -> identidad del entregable.",
      "Pendiente identificado -> supuesto marcado -> no invención."
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
        "Propagación recursiva",
        "Plantilla LaTeX local",
        "Programa analítico local",
        "Malla curricular de Derecho",
        "Fuentes provisionales de trazabilidad"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Plantilla LaTeX local",
          "kind": "develops",
          "justification": "La portada y metadatos deben conservar identidad institucional."
        },
        {
          "source": "Malla curricular de Derecho",
          "target": "Semestre 4 bloque 1",
          "kind": "supports",
          "justification": "La ubicación curricular local se respalda en la fuente institucional indicada."
        },
        {
          "source": "Programa analítico local",
          "target": "Planeación semanal",
          "kind": "supports",
          "justification": "El programa analítico orienta actividades y productos."
        },
        {
          "source": "Consigna de actividad",
          "target": "Producto académico solicitado",
          "kind": "depends_on",
          "justification": "El formato del entregable depende de la consigna."
        },
        {
          "source": "Producto académico solicitado",
          "target": "Plantilla LaTeX local",
          "kind": "depends_on",
          "justification": "Reporte y presentación usan plantillas locales distintas."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Marco normativo o doctrinal",
          "kind": "develops",
          "justification": "El problema inicial determina las normas y doctrina pertinentes."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Análisis propio",
          "kind": "supports",
          "justification": "El análisis jurídico requiere fundamentos verificables."
        },
        {
          "source": "Evidencia verificable",
          "target": "Postura académica",
          "kind": "supports",
          "justification": "La postura propia debe estar sustentada."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión válida requiere respaldo documental o normativo."
        },
        {
          "source": "Consistencia cita-bibliografía",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Evita referencias rotas y afirmaciones sin fuente."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia segura."
        },
        {
          "source": "Fuentes provisionales de trazabilidad",
          "target": "Identidad institucional UnADM",
          "kind": "contrasts",
          "justification": "La procedencia técnica no sustituye la identidad del entregable."
        },
        {
          "source": "Bases de derecho internacional publico",
          "target": "Filosofía del Derecho",
          "kind": "contrasts",
          "justification": "Son materias distintas; solo se comparten reglas editoriales transversales."
        }
      ],
      "evidence": [
        "README destino: materia de Licenciatura en Derecho de la UnADM.",
        "README destino: semestre 4, bloque 1, obligatoria, 8 créditos.",
        "README destino: fuente curricular UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
        "README destino: carpeta como punto de entrada canónico.",
        "README destino: integridad académica, citas verificables y conclusión jurídica con criterio propio.",
        "Programa analítico destino: claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico destino: reportes, presentaciones y productos visuales.",
        "Programa analítico destino: ejes de problema, conceptos, producto, análisis y conclusión.",
        "Bibliografía local: unadmSitioWeb.",
        "Bibliografía local: unadmMallaDerecho2024.",
        "Plantilla reporte destino: documentclass article, spanish, letterpaper, oneside.",
        "Plantilla reporte destino: coursename Bases de derecho internacional publico.",
        "Plantilla reporte destino: coursecode LDE-S4B1.",
        "Incidencia histórica: salida sin JSON parseable desde Codex.",
        "Incidencia histórica: salida sin JSON parseable desde GPT-Pro.",
        "Origen transversal: reglas estables de problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
        "Origen transversal: normalización estructurada obligatoria antes de propagación."
      ]
    },
    "reinforcement_log": [
      "Ciclo 15 consolida destino como materia, no como actividad.",
      "Se deduplican reglas repetidas sin eliminar contenido útil.",
      "Se preserva identidad UnADM y currículo local del destino.",
      "Se descartan contenidos temáticos específicos del origen por relación transversal.",
      "Se refuerzan ejes editoriales reutilizables entre materias jurídicas.",
      "Se normalizan gates de JSON parseable y estructura mínima.",
      "Se integran alertas locales sobre tokens sin expandir y caracteres anómalos.",
      "Se conserva advertencia de no inventar referencias.",
      "Se mantiene consistencia entre citas en texto y .bib local.",
      "Se refuerza cierre jurídico transferible como rasgo de estilo.",
      "Se registran Codex y GPT-Pro como trazabilidad provisional.",
      "Se evita usar fuentes heredadas no verificadas como identidad editorial."
    ]
  }
}