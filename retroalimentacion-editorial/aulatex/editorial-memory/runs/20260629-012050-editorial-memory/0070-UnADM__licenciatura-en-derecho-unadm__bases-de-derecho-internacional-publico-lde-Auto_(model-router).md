{
  "summary": [
    "Materia destino consolidada con identidad UnADM y contexto curricular local.",
    "Destino verificado: Licenciatura en Derecho, semestre 4, bloque 1, obligatoria, 8 créditos.",
    "Se preservan plantilla base, programa analítico y bibliografía local.",
    "Se refuerzan ejes transversales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se conserva normalización estructurada obligatoria antes de propagación.",
    "Se mantiene estrategia conservadora entre materias no equivalentes.",
    "No se trasladan contenidos temáticos específicos de Filosofía del Derecho.",
    "Se conserva incidencia histórica de salidas no JSON parseables."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada y metadatos.",
    "Usar nombre local de la materia: Bases de derecho internacional publico.",
    "Alinear entregables a Licenciatura en Derecho, semestre 4, bloque 1.",
    "Usar código de curso LDE-S4B1 en metadatos.",
    "Conservar al alumno registrado en plantilla salvo instrucción local contraria.",
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar Codex y GPT-Pro como procedencia provisional, no como identidad del entregable.",
    "No mezclar metadatos curriculares del origen con el destino.",
    "Citar la malla curricular de Derecho solo como fuente de ubicación curricular local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Integrar fuentes verificables dentro del desarrollo.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Transformar la planeación semanal en el producto académico solicitado.",
    "Distinguir reporte, presentación y producto visual según consigna.",
    "Conservar separación entre reporte, presentación, programa analítico y bibliografía.",
    "Mantener el programa analítico como guía editorial de actividades.",
    "Conservar la carpeta de referencias local como repositorio de apoyo."
  ],
  "activity_rules": [
    "Adaptar cada actividad al producto solicitado por la planeación semanal.",
    "Verificar correspondencia entre consigna, producto y rúbrica disponible.",
    "Incluir postura académica propia sustentada en fuentes verificables.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Distinguir hechos, argumentos, normas, doctrina y criterio propio.",
    "Integrar conceptos, normas, doctrina o datos pertinentes al caso.",
    "Sustentar afirmaciones con cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Marcar faltantes de consigna o evidencia como pendientes.",
    "Evitar extrapolar fuentes de semanas no confirmadas.",
    "No trasladar citas temáticas de otra materia sin pertinencia local verificada."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de propagar memoria.",
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar respuestas no estructuradas antes de reutilizarlas.",
    "Revisar consistencia entre instrucciones de actividad y programa analítico.",
    "Verificar que README, programa analítico, .bib y plantillas locales coincidan.",
    "Bloquear afirmaciones sin respaldo documental o marca de supuesto.",
    "Validar citas en texto contra el archivo .bib local.",
    "Validar referencias antes de cerrar entregables.",
    "Validar sintaxis LaTeX y cierre de entornos antes de compilar.",
    "Marcar faltantes como pendientes sin sustituirlos por invenciones.",
    "Mantener auditoría de normalización antes de propagación recursiva."
  ],
  "latex_rules": [
    "Reutilizar la plantilla .tex local como base de nuevas actividades.",
    "Usar reporte-bases-de-derecho-internacional-publico.tex para reportes.",
    "Usar presentacion-bases-de-derecho-internacional-publico.tex solo para presentaciones.",
    "Mantener compatibilidad con clase article, spanish, letterpaper y oneside.",
    "Completar metadatos de portada sin alterar identidad institucional.",
    "Definir título, subtítulo y subject coherentes con la actividad.",
    "No cambiar la estructura base de portada sin instrucción editorial.",
    "Usar codificación y acentos correctos en .tex y .bib.",
    "Conservar nombres de archivo locales salvo normalización acordada.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo Slug en README y programa analítico.",
    "Revisar y cerrar correctamente entornos tabular antes de compilar.",
    "Compilar sin errores críticos y sin referencias rotas."
  ],
  "bibliography_rules": [
    "Registrar fuentes de actividad en bases-de-derecho-internacional-publico.bib.",
    "Priorizar fuentes institucionales UnADM y documentos jurídicos verificables.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "Marcar referencias faltantes como pendientes.",
    "Agregar entradas BibTeX específicas solo si la fuente existe.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Validar que las claves citadas existan en el .bib local.",
    "No asumir bibliografía temática de otra materia como fuente local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar hacia arriba y laterales solo reglas verificadas y no duplicadas.",
    "Compartir solo abstracciones editoriales estables entre materias no equivalentes.",
    "Preservar reglas útiles previas aunque se reubiquen por categoría.",
    "Mantener compresión por unión y deduplicación lossless.",
    "No propagar supuestos como reglas definitivas.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Normalizar manualmente memorias heredadas de ciclos previos si se reutilizan.",
    "Conservar incidencias históricas de salida no estructurada.",
    "Propagar correcciones locales solo después de verificar archivos afectados.",
    "Evitar regresiones respecto de reglas útiles previas."
  ],
  "open_questions": [
    "Confirmar consigna textual de cada actividad local.",
    "Confirmar producto exacto solicitado por actividad.",
    "Confirmar rúbrica de evaluación específica.",
    "Confirmar fuentes obligatorias de cada semana.",
    "Confirmar formato mínimo de conclusión jurídica por tipo de evidencia.",
    "Confirmar si el nombre editorial debe usar publico sin acento o público con acento.",
    "Revisar nombres en README con caracteres anómalos.",
    "Corregir tokens sin expandir en README y programa analítico.",
    "Revisar y reparar corte de entorno tabular en el reporte .tex.",
    "Validar si se normaliza nomenclatura de archivos con caracteres acentuados.",
    "Confirmar si existen fuentes locales de derecho internacional público pendientes de integrar."
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
        "Integridad académica verificable.",
        "Carpeta de materia como entrada canónica.",
        "Normalización estructurada obligatoria.",
        "Trazabilidad de procedencia sin contaminar identidad."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Bases de derecho internacional publico.",
        "Destino verificado: semestre 4, bloque 1, obligatoria, 8 créditos.",
        "Código local: LDE-S4B1.",
        "Usar solo contexto curricular verificado en el destino.",
        "No mezclar contexto curricular de materias distintas."
      ]
    },
    "essence": [
      "Identidad institucional UnADM.",
      "Consigna de actividad como eje rector.",
      "Problema jurídico o social inicial.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable.",
      "Análisis propio y postura académica.",
      "Conclusión transferible a la práctica jurídica.",
      "Consistencia entre cita y bibliografía.",
      "Normalización JSON antes de propagación.",
      "Conservadurismo editorial entre materias transversales."
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, fundamento jurídico y evidencia.",
      "Transformar la planeación semanal en reportes, presentaciones o productos visuales.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Formar criterio jurídico aplicable a la práctica profesional.",
      "Proteger integridad académica mediante fuentes verificables.",
      "Conservar memoria editorial reutilizable sin mezclar materias."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Secciones funcionales y no redundantes.",
      "Lenguaje jurídico preciso.",
      "Supuestos siempre etiquetados.",
      "Citas explícitas para afirmaciones sustantivas.",
      "Cierre con criterio jurídico aplicable.",
      "Metadatos locales consistentes.",
      "Sin transferencia literal desde nodos no equivalentes."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> norma o doctrina -> análisis -> conclusión.",
      "Afirmación -> evidencia -> interpretación -> posición propia.",
      "Consigna -> desarrollo alineado -> verificación final.",
      "Hechos -> norma aplicable -> razonamiento -> criterio jurídico.",
      "Fuente verificable -> dato relevante -> uso argumentativo.",
      "Supuesto marcado -> pendiente de confirmación -> no conclusión definitiva."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Licenciatura en Derecho",
        "Bases de derecho internacional publico",
        "Semestre 4 bloque 1",
        "LDE-S4B1",
        "Consigna de actividad",
        "Planeación semanal",
        "Problema jurídico o social",
        "Conceptos jurídicos",
        "Marco normativo",
        "Doctrina",
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
        "Propagación recursiva conservadora"
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
          "justification": "El producto académico debe derivarse de la planeación confirmada."
        },
        {
          "source": "Planeación semanal",
          "target": "Plantilla LaTeX local",
          "kind": "develops",
          "justification": "La plantilla se adapta al formato solicitado."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "El análisis responde al problema planteado."
        },
        {
          "source": "Conceptos jurídicos",
          "target": "Marco normativo",
          "kind": "depends_on",
          "justification": "Los conceptos ordenan la lectura de normas y doctrina."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica requiere fundamento normativo o doctrinal."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Las fuentes verificables evitan afirmaciones sin respaldo."
        },
        {
          "source": "Consistencia cita-bibliografía",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Las claves citadas deben existir en la bibliografía local."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva conservadora",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia segura."
        },
        {
          "source": "Malla curricular de Derecho",
          "target": "Semestre 4 bloque 1",
          "kind": "supports",
          "justification": "La ubicación curricular local se documenta con fuente institucional."
        },
        {
          "source": "Bases de derecho internacional publico",
          "target": "Licenciatura en Derecho",
          "kind": "depends_on",
          "justification": "La materia pertenece al trayecto local de Derecho UnADM."
        },
        {
          "source": "Propagación recursiva conservadora",
          "target": "Contenidos temáticos de Filosofía del Derecho",
          "kind": "contrasts",
          "justification": "La transferencia transversal no debe importar contenido temático no verificado."
        },
        {
          "source": "Bibliografía local",
          "target": "unadmSitioWeb",
          "kind": "develops",
          "justification": "La clave institucional ya existe en el .bib local."
        },
        {
          "source": "Bibliografía local",
          "target": "unadmMallaDerecho2024",
          "kind": "develops",
          "justification": "La clave de malla curricular ya existe en el .bib local."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 4, bloque 1, obligatoria, 8 créditos.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: pauta de identidad UnADM, integridad académica y citas verificables.",
        "Programa analítico local: productos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: ejes de problema, conceptos, fuentes, análisis propio y cierre.",
        "Bibliografía local: clave unadmSitioWeb existente.",
        "Bibliografía local: clave unadmMallaDerecho2024 existente.",
        "Plantilla local: reporte base de la materia.",
        "Plantilla local: curso LDE-S4B1.",
        "Contexto local: README contiene nombres con caracteres anómalos.",
        "Contexto local: README y programa analítico contienen token Slug sin expandir.",
        "Contexto local: reporte .tex muestra entorno tabular cortado.",
        "Memoria heredada: salida no JSON parseable requiere normalización manual."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2 consolida destino como materia, no como actividad.",
      "Se deduplicaron reglas equivalentes sin recortar contenido útil.",
      "Se mantuvo el contexto curricular local verificado.",
      "Se bloquearon metadatos curriculares del origen.",
      "Se conservaron reglas institucionales UnADM transversales.",
      "Se reforzó la estructura problema-conceptos-evidencia-análisis-conclusión.",
      "Se preservó la exigencia de postura propia.",
      "Se reforzó la consistencia entre citas y .bib local.",
      "Se mantuvo la regla de no inventar fuentes.",
      "Se conservaron incidencias de salida no estructurada.",
      "Se añadió contraste explícito contra transferencia temática no verificada.",
      "Se conservaron pendientes técnicos de README, tokens y tabular."
    ]
  }
}