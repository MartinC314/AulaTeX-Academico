{
  "summary": [
    "Consolidar cerebro editorial de Derechos de autor con identidad UnADM.",
    "Aplicar sincronización transversal conservadora desde Filosofía del Derecho.",
    "Transferir solo abstracciones estables entre materias no equivalentes.",
    "Preservar reglas útiles locales sin regresión.",
    "Usar compresión por unión y deduplicación.",
    "Mantener normalización estructurada antes de propagar memoria.",
    "Tratar herencias Codex y GPT-Pro como provisionales hasta validación local.",
    "Usar README y programa analítico como fuentes locales de encuadre.",
    "Usar derechos-de-autor.bib como bibliografía local canónica.",
    "Corregir marcadores de plantilla y nombres corruptos antes de publicar."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, tono y metadatos.",
    "Alinear entregables con Licenciatura en Derecho.",
    "Usar datos curriculares locales: semestre 5, bloque 1, obligatoria, 8 créditos.",
    "Citar malla-curricular-derecho-unadm.pdf para ubicación curricular.",
    "Supuesto: la clave local LDE-S5B1 se mantiene hasta confirmación oficial.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Mantener enfoque jurídico con criterio propio en la conclusión.",
    "No transferir datos personales del alumno a otros nodos.",
    "Tratar fuentes heredadas no verificadas como provisionales.",
    "Usar la carpeta de asignatura como entrada canónica."
  ],
  "structure_rules": [
    "Conservar README como punto de entrada canónico de la asignatura.",
    "Usar programa analítico como marco editorial local.",
    "Organizar cada producto por problema, conceptos, marco normativo o doctrinal, análisis y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear la entrega al producto solicitado por la planeación semanal.",
    "Mantener separación entre reporte, presentación y referencias.",
    "Guardar bibliografía específica en derechos-de-autor.bib.",
    "Normalizar nombres de archivo con slug derechos-de-autor.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug).",
    "Corregir nombres corruptos como eporte y eferencias antes de publicar.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Iniciar cada actividad con problema jurídico o social delimitado.",
    "Vincular conceptos con normas, doctrina o datos verificables.",
    "Cumplir el formato solicitado por la planeación semanal.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Agregar fuentes específicas por actividad al BibTeX local.",
    "No asumir fuentes de otra materia como fuentes de Derechos de autor.",
    "No asumir que fuentes de semanas posteriores corresponden a una actividad previa.",
    "Confirmar producto exacto cuando falte consigna textual.",
    "Cerrar con aplicación jurídica práctica."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que toda afirmación tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar consistencia entre portada y datos curriculares locales.",
    "Detectar y corregir campos pendientes como Nombre por definir.",
    "Auditar README por caracteres extraños y marcadores de plantilla.",
    "Verificar que el producto corresponda a la consigna local.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Mantener normalización manual para contenido heredado de ciclos previos.",
    "Evitar regresiones respecto de reglas útiles previas."
  ],
  "latex_rules": [
    "Mantener documentclass article en español y letterpaper salvo instrucción contraria.",
    "Declarar metadatos con macros antes de input de plantilla.",
    "Validar orden correcto entre paquetes LaTeX e input de plantilla.",
    "No dejar usepackage sin argumento.",
    "Evitar paquetes truncados o líneas incompletas en preámbulo.",
    "Usar codificación y acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Validar que los paquetes queden en preámbulo efectivo.",
    "Usar tipografía sans serif de forma consistente si la plantilla la requiere.",
    "Conservar tabla de autor con datos académicos completos solo en nodo local.",
    "No propagar datos personales del alumno a otras materias.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "No copiar LaTeX completo en memoria editorial."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Usar solo materiales institucionales o verificables.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos consultables.",
    "Registrar fuentes base UnADM incluidas en derechos-de-autor.bib.",
    "Conservar entrada local unadmSitioWeb si se cita.",
    "Conservar entrada local unadmMallaDerecho2024 si se cita.",
    "Agregar entradas BibTeX completas por actividad.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Incluir fecha de consulta cuando la fuente sea web.",
    "Asegurar que toda cita en texto tenga entrada en .bib.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "No reutilizar bibliografía de Filosofía del Derecho sin pertinencia local verificada."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar hacia arriba reglas institucionales validadas en esta materia.",
    "Propagar lateralmente solo reglas genéricas de calidad, estructura y bibliografía.",
    "No propagar redacción literal entre materias no equivalentes.",
    "No propagar datos personales del alumno.",
    "No propagar marcadores pendientes ni nombres corruptos de archivo.",
    "Propagar advertencias sobre herencias Codex y GPT-Pro solo como provisionales.",
    "Mantener auditoría manual para contenido heredado de ciclos previos.",
    "Reutilizar patrón problema-conceptos-evidencia-análisis-cierre.",
    "Evitar transferir conceptos específicos de Filosofía del Derecho como contenido de Derechos de autor.",
    "Preservar reglas locales más específicas sobre reglas transversales.",
    "Aplicar sincronización progresiva y conservadora."
  ],
  "open_questions": [
    "Confirmar si LDE-S5B1 es clave oficial en toda la suite.",
    "Definir nombre de figura docente.",
    "Validar si Roma Norte, Ciudad de México debe mantenerse fija.",
    "Confirmar sustitución definitiva del token de plantilla por derechos-de-autor.bib.",
    "Revisar y corregir nombres de archivo corruptos en README.",
    "Validar orden correcto entre paquetes LaTeX e input de template.",
    "Confirmar si la herencia Codex desde ingeniería sigue vigente.",
    "Confirmar si la herencia GPT-Pro debe conservarse tras validación local.",
    "Confirmar fuentes jurídicas obligatorias específicas de Derechos de autor.",
    "Confirmar rúbricas y consignas por actividad.",
    "Confirmar si habrá archivo de referencias separado por actividad.",
    "Confirmar si las actividades requieren reporte, presentación o producto visual."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Institucional sin rigidez excesiva.",
        "Trazable y verificable."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "README como entrada canónica.",
        "Programa analítico como marco editorial.",
        "Malla curricular como fuente de ubicación.",
        "Datos no visibles marcados como supuesto."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Derechos de autor.",
        "Semestre 5.",
        "Bloque 1.",
        "Obligatoria.",
        "8 créditos.",
        "Supuesto: clave local LDE-S5B1."
      ]
    },
    "essence": [
      "Identidad institucional UnADM.",
      "Integridad académica.",
      "Problema jurídico delimitado.",
      "Conceptos jurídicos pertinentes.",
      "Marco normativo o doctrinal.",
      "Fuentes verificables.",
      "Análisis propio.",
      "Postura argumentada.",
      "Conclusión transferible.",
      "Calidad bibliográfica.",
      "Normalización JSON.",
      "Corrección técnica LaTeX."
    ],
    "reason_for_being": [
      "Orientar productos académicos de Derechos de autor con claridad jurídica.",
      "Transformar planeación semanal en entregables verificables.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Asegurar que cada conclusión derive de fundamentos consultables.",
      "Evitar productos meramente descriptivos.",
      "Preservar memoria editorial persistente sin pérdida útil.",
      "Facilitar propagación transversal solo de reglas estables."
    ],
    "style_markers": [
      "Frases directas y trazables.",
      "Supuestos explícitamente marcados.",
      "Sin afirmaciones sin fuente.",
      "Cierre con criterio jurídico propio.",
      "Estructura problema-conceptos-marco-análisis-cierre.",
      "Citas verificables y correspondencia BibTeX.",
      "Nombres de archivo normalizados.",
      "Metadatos locales consistentes.",
      "Advertencias provisionales visibles.",
      "Sin redacción literal transferida entre materias."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> norma o doctrina -> análisis -> conclusión.",
      "Afirmación -> evidencia -> interpretación -> postura.",
      "Consigna -> producto requerido -> desarrollo alineado -> verificación.",
      "Fuente institucional -> dato curricular -> metadato local.",
      "Marco verificable -> razonamiento jurídico -> aplicación práctica.",
      "Supuesto -> necesidad de confirmación -> uso provisional.",
      "Actividad -> bibliografía específica -> cita en texto -> entrada .bib.",
      "Error técnico -> corrección previa -> compilación válida."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Licenciatura en Derecho",
        "Derechos de autor",
        "Semestre 5 bloque 1",
        "Obligatoria 8 créditos",
        "README canónico",
        "Programa analítico editorial",
        "derechos-de-autor.bib",
        "Malla curricular de Derecho",
        "Problema jurídico",
        "Conceptos jurídicos",
        "Marco normativo o doctrinal",
        "Fuentes verificables",
        "Análisis propio",
        "Postura argumentada",
        "Conclusión transferible",
        "Integridad académica",
        "Normalización JSON",
        "Calidad bibliográfica",
        "Corrección LaTeX",
        "Tokens de plantilla sin expandir",
        "Nombres de archivo corruptos",
        "Herencia provisional Codex",
        "Herencia provisional GPT-Pro",
        "Propagación transversal conservadora"
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
          "justification": "La pauta local exige identidad UnADM, citas verificables y conclusión jurídica."
        },
        {
          "source": "README canónico",
          "target": "Datos curriculares locales",
          "kind": "supports",
          "justification": "El README registra semestre 5, bloque 1, tipo obligatoria y 8 créditos."
        },
        {
          "source": "Malla curricular de Derecho",
          "target": "Semestre 5 bloque 1",
          "kind": "supports",
          "justification": "El README señala la malla curricular como fuente de ubicación."
        },
        {
          "source": "Programa analítico editorial",
          "target": "Estructura problema-conceptos-marco-análisis-cierre",
          "kind": "develops",
          "justification": "El programa define ejes de trabajo para los productos académicos."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "El análisis debe responder al problema delimitado."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica debe derivar de fundamentos verificables."
        },
        {
          "source": "Fuentes verificables",
          "target": "Calidad bibliográfica",
          "kind": "supports",
          "justification": "Toda afirmación sustantiva requiere fuente consultable y entrada .bib."
        },
        {
          "source": "derechos-de-autor.bib",
          "target": "Citas en texto",
          "kind": "depends_on",
          "justification": "Las citas deben corresponder con entradas BibTeX locales."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación transversal conservadora",
          "kind": "depends_on",
          "justification": "No se propaga memoria si la estructura no es parseable."
        },
        {
          "source": "Tokens de plantilla sin expandir",
          "target": "Corrección LaTeX",
          "kind": "depends_on",
          "justification": "Los tokens deben resolverse antes de compilar o publicar."
        },
        {
          "source": "Nombres de archivo corruptos",
          "target": "README canónico",
          "kind": "contrasts",
          "justification": "Los nombres corruptos debilitan la función canónica del README."
        },
        {
          "source": "Herencia provisional Codex",
          "target": "Validación local",
          "kind": "depends_on",
          "justification": "La fuente heredada no debe consolidarse sin confirmación."
        },
        {
          "source": "Herencia provisional GPT-Pro",
          "target": "Validación local",
          "kind": "depends_on",
          "justification": "La fuente heredada debe tratarse como provisional."
        },
        {
          "source": "Filosofía del Derecho",
          "target": "Derechos de autor",
          "kind": "contrasts",
          "justification": "Son nodos no equivalentes; solo comparten abstracciones editoriales estables."
        },
        {
          "source": "Propagación transversal conservadora",
          "target": "Reglas institucionales estables",
          "kind": "develops",
          "justification": "El salto conserva identidad, estructura reusable, calidad y grafo conceptual."
        }
      ],
      "evidence": [
        "README de Derechos de autor: materia de Licenciatura en Derecho de la UnADM.",
        "README de Derechos de autor: semestre 5, bloque 1, obligatoria, 8 créditos.",
        "README de Derechos de autor: fuente malla-curricular-derecho-unadm.pdf.",
        "README de Derechos de autor: carpeta como punto de entrada canónico.",
        "README de Derechos de autor: integridad académica y citas verificables.",
        "README de Derechos de autor: conclusión jurídica con criterio propio.",
        "Programa analítico: productos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico: transformar planeación semanal en reportes, presentaciones y productos visuales.",
        "Programa analítico: ejes problema, conceptos, producto, análisis y conclusión.",
        "derechos-de-autor.bib: entrada unadmSitioWeb.",
        "derechos-de-autor.bib: entrada unadmMallaDerecho2024.",
        "Reporte local: documentclass article en español y letterpaper.",
        "Reporte local: metadatos de curso Derechos de autor.",
        "Reporte local: figura docente pendiente como Nombre por definir.",
        "Reporte local: usepackage final sin argumento detectado.",
        "Memoria origen: no propagar salidas no JSON parseable.",
        "Memoria origen: usar problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
        "Memoria heredada: Codex desde ingeniería es fuente provisional."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2 consolida memoria de materia con deduplicación conservadora.",
      "Se preservan reglas locales de Derechos de autor.",
      "Se integran solo abstracciones transversales desde Filosofía del Derecho.",
      "Se evita transferir fuentes o conceptos específicos de Filosofía como contenido local.",
      "Se refuerza la normalización JSON como compuerta de propagación.",
      "Se refuerza el patrón problema-conceptos-marco-análisis-cierre.",
      "Se refuerza la exigencia de citas verificables y correspondencia BibTeX.",
      "Se refuerza la corrección de tokens de plantilla y nombres corruptos.",
      "Se mantiene advertencia de herencias Codex y GPT-Pro como provisionales.",
      "Se mantiene apertura de vacíos contextuales locales para validación posterior."
    ]
  }
}