{
  "summary": [
    "Consolidar cerebro editorial de Derechos de autor con identidad UnADM.",
    "Sincronizar solo abstracciones estables desde Filosofía del Derecho.",
    "Mantener compresión lossless por unión y deduplicación.",
    "Preservar reglas útiles previas sin regresión.",
    "Validar localmente herencias Codex y GPT-Pro antes de usarlas.",
    "Usar README como entrada canónica de la asignatura.",
    "Aplicar estructura problema, conceptos, evidencia, análisis propio y cierre.",
    "Bloquear propagación de salidas no JSON parseable."
  ],
  "identity_rules": [
    "Usar identidad institucional UnADM en portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho.",
    "Usar datos curriculares locales: semestre 5, bloque 1, obligatoria, 8 créditos.",
    "Mantener enfoque jurídico con criterio propio en la conclusión.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Supuesto: la materia conserva nomenclatura local LDE-S5B1.",
    "Tratar fuentes heredadas Codex y GPT-Pro como provisionales hasta validación local.",
    "Citar malla-curricular-derecho-unadm.pdf para soporte curricular cuando se use."
  ],
  "structure_rules": [
    "Conservar README como punto de entrada canónico.",
    "Usar programa analítico como marco editorial.",
    "Organizar productos por problema, conceptos, marco normativo o doctrinal, análisis y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear formato final al producto solicitado por la planeación semanal.",
    "Mantener separación entre reporte, presentación y referencias.",
    "Guardar bibliografía específica en derechos-de-autor.bib.",
    "Normalizar nombres de archivo con slug derechos-de-autor.",
    "Corregir marcadores literales de plantilla en README y programa analítico.",
    "Corregir nombres corruptos como eporte y eferencias antes de publicar."
  ],
  "activity_rules": [
    "Iniciar cada actividad con problema jurídico o social delimitado.",
    "Vincular conceptos con normas, doctrina o datos verificables.",
    "Cumplir el formato solicitado por la consigna.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Cerrar con conclusión aplicable a la práctica jurídica.",
    "Agregar fuentes específicas por actividad al BibTeX local.",
    "No asumir fuentes de otras actividades sin confirmación local."
  ],
  "quality_gates": [
    "Rechazar salidas no JSON parseable antes de propagar memoria.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Verificar consistencia entre portada y datos curriculares locales.",
    "Confirmar que toda afirmación tenga respaldo o marca de supuesto.",
    "Exigir correspondencia entre citas en texto y .bib local.",
    "Detectar campos pendientes como Nombre por definir.",
    "Auditar README por caracteres extraños y marcadores de plantilla.",
    "Validar que el producto corresponda a la consigna de actividad.",
    "Mantener auditoría manual para herencias Codex y GPT-Pro."
  ],
  "latex_rules": [
    "Mantener documentclass article en español y letterpaper salvo instrucción contraria.",
    "Declarar metadatos con macros antes de \\input{template}.",
    "Conservar tabla de autor con datos académicos completos en documentos locales.",
    "No propagar datos personales del alumno a otras materias.",
    "Usar codificación y acentos correctos en español.",
    "Evitar paquetes truncados o líneas incompletas en preámbulo.",
    "Nunca dejar \\usepackage sin argumento.",
    "Validar que paquetes LaTeX queden en preámbulo efectivo.",
    "Mover paquetes cargados después de \\input{template} si la plantilla lo exige.",
    "Usar tipografía sans serif de forma consistente si la plantilla la requiere.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Verificar nombres de archivos antes de referenciarlos.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Mantener claves BibTeX estables."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Usar solo materiales institucionales o verificables.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos consultables.",
    "Registrar fuentes base UnADM incluidas en derechos-de-autor.bib.",
    "Conservar entrada local unadmSitioWeb si se cita.",
    "Conservar entrada local unadmMallaDerecho2024 si se cita.",
    "Agregar entradas BibTeX completas por actividad.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Incluir fecha de consulta en fuentes web.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Asegurar que toda cita en texto tenga entrada en .bib.",
    "Asegurar que entradas .bib citadas correspondan al producto actual."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar hacia arriba reglas institucionales validadas localmente.",
    "Propagar lateralmente a materias LDE solo reglas genéricas de calidad y estructura.",
    "Compartir identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferir redacción literal entre materias no equivalentes.",
    "No propagar datos personales del alumno.",
    "No propagar marcadores pendientes ni nombres corruptos de archivo.",
    "Marcar como provisional toda herencia no verificada localmente.",
    "Mantener normalización manual para contenido heredado de ciclos previos.",
    "Evitar regresiones respecto de reglas útiles previas."
  ],
  "open_questions": [
    "Confirmar si LDE-S5B1 es clave oficial en toda la suite.",
    "Definir nombre de figura docente.",
    "Validar si Roma Norte, Ciudad de México debe mantenerse fija.",
    "Confirmar sustitución definitiva de marcadores literales por derechos-de-autor.bib.",
    "Revisar y corregir errores de nombres de archivo en README.",
    "Validar orden correcto entre paquetes LaTeX y \\input{template}.",
    "Confirmar si la fuente Codex desde ingeniería sigue vigente.",
    "Confirmar fuentes obligatorias específicas de cada actividad.",
    "Confirmar rúbrica local para ajustar profundidad argumentativa.",
    "Confirmar si existen lineamientos propios de Derechos de autor no capturados aún."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Institucional sin rigidez excesiva."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Carpeta de asignatura como entrada canónica.",
        "Fuentes heredadas tratadas como provisionales hasta validación."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Derechos de autor.",
        "Semestre 5, bloque 1.",
        "Tipo obligatoria.",
        "8 créditos.",
        "Supuesto: clave local LDE-S5B1."
      ]
    },
    "essence": [
      "Problema jurídico o social delimitado.",
      "Conceptos pertinentes.",
      "Marco normativo o doctrinal verificable.",
      "Producto solicitado por la planeación.",
      "Evidencia trazable.",
      "Análisis propio.",
      "Conclusión jurídica transferible.",
      "Integridad bibliográfica.",
      "Normalización estructurada."
    ],
    "reason_for_being": [
      "Orientar productos académicos de Derechos de autor con identidad UnADM.",
      "Transformar planeación semanal en reporte, presentación o producto visual.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Formar criterio jurídico aplicable a la práctica profesional.",
      "Sostener trazabilidad entre consigna, evidencia, citas y conclusión."
    ],
    "style_markers": [
      "Declarar supuestos de forma explícita.",
      "Usar secciones funcionales y trazables.",
      "Evitar resumen sin postura.",
      "Cerrar con implicación práctica.",
      "Mantener consistencia entre portada, contenido y referencias.",
      "Separar bibliografía base y fuentes de actividad.",
      "Corregir tokens y nombres corruptos antes de publicar.",
      "No transferir literalidad de materias no equivalentes."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Objetivo puntual.",
      "Conceptos clave definidos.",
      "Marco normativo o doctrinal.",
      "Evidencia verificable.",
      "Análisis con postura propia.",
      "Contraste entre fuentes cuando proceda.",
      "Conclusión aplicable a la práctica jurídica.",
      "Revisión de coherencia entre pregunta guía y cierre."
    ],
    "knowledge_graph": {
      "concepts": [
        "Derechos de autor.",
        "Identidad institucional UnADM.",
        "Licenciatura en Derecho.",
        "Semestre 5 bloque 1.",
        "Problema jurídico o social.",
        "Conceptos jurídicos pertinentes.",
        "Marco normativo o doctrinal.",
        "Evidencia verificable.",
        "Análisis propio.",
        "Postura académica.",
        "Conclusión jurídica transferible.",
        "Integridad bibliográfica.",
        "Normalización estructurada.",
        "Propagación segura.",
        "README canónico.",
        "Programa analítico editorial.",
        "BibTeX local.",
        "Malla curricular de Derecho.",
        "Herencia provisional Codex.",
        "Herencia provisional GPT-Pro."
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "README canónico",
          "target": "Identidad institucional UnADM",
          "kind": "supports",
          "justification": "Define la asignatura como punto de entrada local."
        },
        {
          "source": "Malla curricular de Derecho",
          "target": "Semestre 5 bloque 1",
          "kind": "supports",
          "justification": "La ubicación curricular local remite al PDF institucional."
        },
        {
          "source": "Programa analítico editorial",
          "target": "Problema jurídico o social",
          "kind": "develops",
          "justification": "Fija el encuadre inicial de los productos."
        },
        {
          "source": "Programa analítico editorial",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "Exige postura académica dentro del desarrollo."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad bibliográfica",
          "kind": "supports",
          "justification": "Toda afirmación debe conectarse con citas y BibTeX."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "develops",
          "justification": "La postura argumentada permite un cierre útil para la práctica."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación segura",
          "kind": "supports",
          "justification": "Evita heredar salidas no parseables."
        },
        {
          "source": "Herencia provisional Codex",
          "target": "Propagación segura",
          "kind": "depends_on",
          "justification": "Requiere validación local antes de reutilizarse."
        },
        {
          "source": "Herencia provisional GPT-Pro",
          "target": "Propagación segura",
          "kind": "depends_on",
          "justification": "Requiere normalización antes de aplicarse aguas abajo."
        },
        {
          "source": "Derechos de autor",
          "target": "Marco normativo o doctrinal",
          "kind": "depends_on",
          "justification": "El contenido específico exige fuentes jurídicas locales verificadas."
        }
      ],
      "evidence": [
        "README de Derechos de autor define materia, ubicación curricular y pauta editorial.",
        "README local remite a UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
        "Programa analítico local fija propósito y ejes de trabajo.",
        "derechos-de-autor.bib contiene unadmSitioWeb y unadmMallaDerecho2024.",
        "Reporte local declara curso Derechos de autor y clave LDE-S5B1.",
        "Reporte local contiene marcador pendiente Figura docente: Nombre por definir.",
        "README local contiene nombres corruptos eporte y eferencias.",
        "README y programa analítico contienen token $(@{...}.Slug) sin expandir.",
        "Memoria heredada indica salida sin JSON parseable desde Codex.",
        "Memoria previa del destino marca herencias Codex y GPT-Pro como provisionales."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2 deduplica reglas repetidas del destino.",
      "Se preservan reglas locales de identidad UnADM y currículo S5B1.",
      "Se incorporan abstracciones estables desde Filosofía del Derecho.",
      "No se transfieren citas ni temas específicos de Filosofía del Derecho.",
      "Se refuerza patrón problema, conceptos, evidencia, análisis y conclusión.",
      "Se refuerza bloqueo de salidas no JSON parseable.",
      "Se mantiene advertencia sobre herencias Codex y GPT-Pro.",
      "Se conserva auditoría de tokens, nombres corruptos y preámbulo LaTeX.",
      "Se limita el grafo a conceptos verificables del nodo destino y reglas transversales."
    ]
  }
}