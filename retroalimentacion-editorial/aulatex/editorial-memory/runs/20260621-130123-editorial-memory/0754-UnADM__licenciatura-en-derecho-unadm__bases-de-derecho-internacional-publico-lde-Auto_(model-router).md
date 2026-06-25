{
  "summary": [
    "Materia destino consolidada como cerebro editorial UnADM.",
    "Asignatura local: Bases de derecho internacional publico.",
    "Ubicación local verificada: Licenciatura en Derecho, semestre 4, bloque 1, obligatoria, 8 créditos.",
    "Se conserva plantilla base, programa analítico y bibliografía local.",
    "Se refuerzan ejes transversales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se conserva incidencia histórica de salidas no JSON parseable.",
    "Se aplica transferencia conservadora desde Filosofía del Derecho.",
    "No se trasladan contenidos temáticos específicos del origen.",
    "Se prioriza estructura reusable, identidad institucional y gates de calidad.",
    "Se detectan nombres anómalos y tokens sin expandir en README y programa analítico."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, tono y metadatos.",
    "Usar nombre local de la materia: Bases de derecho internacional publico.",
    "Usar código de curso LDE-S4B1 en metadatos.",
    "Alinear entregables a Licenciatura en Derecho, semestre 4, bloque 1, obligatoria, 8 créditos.",
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Conservar al alumno registrado en plantilla si no hay instrucción local que lo sustituya.",
    "No mezclar metadatos curriculares de Filosofía del Derecho con el destino.",
    "Tratar Codex y GPT-Pro como procedencia provisional, no como identidad del entregable.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Citar malla-curricular-derecho-unadm.pdf para ubicación curricular cuando corresponda."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar cada entrega con problema, conceptos, fuentes, análisis propio y conclusión jurídica.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Transformar la planeación semanal en el producto académico solicitado.",
    "Mantener el programa analítico como guía editorial de actividades.",
    "Conservar separación entre reporte, presentación, programa analítico y bibliografía.",
    "Distinguir reporte, presentación y producto visual según consigna.",
    "Conservar la carpeta referencias-bases-de-derecho-internacional-publico como repositorio de apoyo.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Adaptar cada actividad al producto solicitado por la planeación semanal.",
    "Verificar que el producto corresponda a la consigna de la actividad.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Evitar entregas solo descriptivas.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Integrar normas, doctrina o datos pertinentes al caso de actividad.",
    "Distinguir hechos, argumentos, normas y criterio propio.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Evitar extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de propagar memoria.",
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar respuestas no estructuradas antes de reutilizarlas.",
    "Normalizar manualmente memorias heredadas no estructuradas.",
    "Revisar consistencia entre instrucciones de actividad y programa analítico.",
    "Bloquear afirmaciones sin respaldo documental o normativo.",
    "Confirmar que todo supuesto esté marcado como supuesto.",
    "Validar citas y referencias antes de cerrar entregables.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que README, programa analítico, .bib y plantillas locales coincidan.",
    "Validar sintaxis LaTeX y cierre de entornos antes de compilar.",
    "Marcar faltantes como pendientes sin sustituirlos por invenciones.",
    "Mantener auditoría de parseo JSON antes de nueva propagación."
  ],
  "latex_rules": [
    "Reutilizar la plantilla .tex local de la materia como base de nuevas actividades.",
    "Usar reporte-bases-de-derecho-internacional-publico.tex para reportes base.",
    "Usar presentacion-bases-de-derecho-internacional-publico.tex solo para productos de presentación.",
    "Completar metadatos de portada sin alterar identidad institucional.",
    "Definir título, subtítulo y subject coherentes con la actividad en curso.",
    "Mantener compatibilidad con clase article, spanish, letterpaper y oneside.",
    "Usar codificación y acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "No cambiar la estructura base de portada sin instrucción editorial.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Revisar y cerrar correctamente entornos tabular antes de compilar.",
    "Compilar sin errores críticos y sin referencias rotas."
  ],
  "bibliography_rules": [
    "Registrar fuentes de actividad en bases-de-derecho-internacional-publico.bib.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Agregar entradas BibTeX específicas solo cuando la fuente exista y sea verificable.",
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "Marcar referencias faltantes como pendientes.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Validar que las claves citadas existan en el .bib local.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Conservar la malla curricular de Derecho como fuente institucional local."
  ],
  "propagation_hints": [
    "Propagar hacia arriba y laterales solo reglas verificadas y no duplicadas.",
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Compartir solo abstracciones editoriales estables entre materias no equivalentes.",
    "Evitar transferir redacción literal de actividades origen.",
    "No propagar contenidos temáticos específicos de Filosofía del Derecho.",
    "No propagar supuestos como reglas definitivas.",
    "Preservar reglas útiles previas aunque se reubiquen por categoría.",
    "Mantener compresión union-dedupe con criterio lossless.",
    "Conservar incidencias históricas de salidas no estructuradas.",
    "Ciclo 1 requiere normalización manual si se reutiliza.",
    "Propagar correcciones locales solo después de verificar archivos afectados.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local."
  ],
  "open_questions": [
    "Confirmar consignas específicas de actividades de la materia destino.",
    "Confirmar rúbricas de evaluación por actividad.",
    "Confirmar fuentes obligatorias de cada semana.",
    "Confirmar si el nombre editorial debe conservar publico sin acento o usar público con acento.",
    "Revisar nombres anómalos en README: reporte y referencias.",
    "Corregir tokens sin expandir en README y programa analítico.",
    "Reparar corte de entorno tabular en el archivo de reporte .tex.",
    "Validar si se normaliza nomenclatura de archivos con caracteres acentuados.",
    "Definir formato mínimo de conclusión jurídica por tipo de evidencia.",
    "Confirmar si existe bibliografía internacional pública obligatoria no registrada aún."
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
        "Usar solo contexto curricular verificado del nodo destino.",
        "No mezclar contexto curricular de materias distintas."
      ]
    },
    "essence": [
      "Identidad institucional UnADM.",
      "Materia jurídica con estructura académica verificable.",
      "Problema jurídico o social como punto de partida.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable y cita explícita.",
      "Análisis propio y postura académica.",
      "Conclusión transferible a la práctica jurídica.",
      "Consistencia entre consigna, desarrollo y cierre.",
      "Consistencia cita-bibliografía.",
      "Normalización JSON antes de propagación."
    ],
    "reason_for_being": [
      "Orientar productos académicos de Bases de derecho internacional publico.",
      "Transformar la planeación semanal en reportes, presentaciones y productos visuales.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Asegurar claridad, fundamento jurídico, evidencia y transferencia profesional.",
      "Evitar productos descriptivos sin criterio jurídico propio.",
      "Preservar continuidad editorial entre actividades de la materia."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Encuadre breve del problema jurídico o social.",
      "Secciones funcionales y no redundantes.",
      "Marco normativo o doctrinal separado del análisis propio.",
      "Afirmaciones respaldadas con fuentes verificables.",
      "Supuestos siempre etiquetados.",
      "Cierre con criterio jurídico aplicable.",
      "Metadatos locales consistentes.",
      "Lenguaje jurídico preciso.",
      "Sin contenido temático importado de materias no equivalentes."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> norma o doctrina -> análisis -> conclusión.",
      "Afirmación -> evidencia -> interpretación -> posición propia.",
      "Consigna -> producto solicitado -> desarrollo alineado -> verificación final.",
      "Hechos -> normas aplicables -> argumentos -> criterio del estudiante.",
      "Fuente verificable -> cita explícita -> conclusión transferible.",
      "Pendiente identificado -> supuesto marcado -> confirmación requerida."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Licenciatura en Derecho",
        "Bases de derecho internacional publico",
        "Semestre 4, bloque 1",
        "Consigna de actividad",
        "Planeación semanal",
        "Problema jurídico o social",
        "Conceptos clave",
        "Marco normativo o doctrinal",
        "Fuentes verificables",
        "Análisis propio",
        "Postura académica",
        "Conclusión jurídica transferible",
        "Integridad académica",
        "Consistencia cita-bibliografía",
        "Normalización JSON",
        "Plantilla LaTeX local",
        "Bibliografía local",
        "Malla curricular de Derecho",
        "Tokens sin expandir",
        "Nombres anómalos en README",
        "Entorno tabular incompleto"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Metadatos locales",
          "kind": "supports",
          "justification": "La portada y los metadatos deben conservar identidad institucional."
        },
        {
          "source": "Malla curricular de Derecho",
          "target": "Semestre 4, bloque 1",
          "kind": "supports",
          "justification": "El README local señala esta fuente para ubicación curricular."
        },
        {
          "source": "Consigna de actividad",
          "target": "Planeación semanal",
          "kind": "depends_on",
          "justification": "El producto debe ajustarse a lo solicitado para cada actividad."
        },
        {
          "source": "Planeación semanal",
          "target": "Producto académico",
          "kind": "develops",
          "justification": "La planeación se transforma en reporte, presentación o producto visual."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Estructura argumentativa jurídica",
          "kind": "develops",
          "justification": "El encuadre del problema ordena el desarrollo del trabajo."
        },
        {
          "source": "Conceptos clave",
          "target": "Análisis propio",
          "kind": "supports",
          "justification": "Los conceptos delimitan el razonamiento jurídico del estudiante."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Análisis propio",
          "kind": "supports",
          "justification": "El análisis requiere normas, doctrina o datos pertinentes."
        },
        {
          "source": "Fuentes verificables",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Las citas explícitas evitan afirmaciones sin respaldo."
        },
        {
          "source": "Consistencia cita-bibliografía",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Las claves citadas deben existir en el .bib local."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "develops",
          "justification": "La conclusión debe derivar del razonamiento y ser aplicable profesionalmente."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia segura."
        },
        {
          "source": "Plantilla LaTeX local",
          "target": "Producto académico",
          "kind": "supports",
          "justification": "La plantilla mantiene formato e identidad de la materia."
        },
        {
          "source": "Tokens sin expandir",
          "target": "Compilación segura",
          "kind": "contrasts",
          "justification": "Los tokens en nombres de archivo pueden romper referencias editoriales."
        },
        {
          "source": "Entorno tabular incompleto",
          "target": "Compilación segura",
          "kind": "contrasts",
          "justification": "El cierre incompleto de tabular impide compilar sin errores."
        },
        {
          "source": "Filosofía del Derecho",
          "target": "Bases de derecho internacional publico",
          "kind": "contrasts",
          "justification": "Son nodos no equivalentes; solo se transfieren abstracciones editoriales estables."
        }
      ],
      "evidence": [
        "README local: materia de Licenciatura en Derecho de la UnADM.",
        "README local: semestre 4, bloque 1, obligatoria, 8 créditos.",
        "README local: fuente curricular malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: cada actividad conserva identidad UnADM, integridad académica y citas verificables.",
        "README local: conclusión jurídica con criterio propio.",
        "Programa analítico local: claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: transformar planeación semanal en reportes, presentaciones y productos visuales.",
        "Programa analítico local: ejes de problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
        "Bibliografía local: unadmSitioWeb.",
        "Bibliografía local: unadmMallaDerecho2024.",
        "README local: nombres anómalos en reporte y referencias.",
        "README y programa analítico local: token $(@{...}.Slug) sin expandir.",
        "Reporte .tex local: corte visible en cierre de entorno tabular.",
        "Memoria heredada: salida sin JSON parseable desde Codex.",
        "Memoria destino previa: salida sin JSON parseable desde GPT-Pro.",
        "Transferencia ciclo 13: solo abstracciones editoriales estables desde Filosofía del Derecho."
      ]
    },
    "reinforcement_log": [
      "Ciclo 13 consolida memoria destino sin regresión.",
      "Ciclo 13 deduplica reglas equivalentes por unión conservadora.",
      "Ciclo 13 preserva identidad UnADM y contexto curricular local.",
      "Ciclo 13 refuerza normalización JSON antes de propagación recursiva.",
      "Ciclo 13 incorpora reglas transversales verificables del origen.",
      "Ciclo 13 evita trasladar bibliografía temática de Filosofía del Derecho.",
      "Ciclo 13 mantiene la bibliografía local como fuente canónica del destino.",
      "Ciclo 13 registra pendientes técnicos de README, tokens y tabular.",
      "Ciclo 13 conserva incidencias históricas de salidas no estructuradas.",
      "Ciclo 13 fortalece el patrón problema-evidencia-análisis-conclusión."
    ]
  }
}