{
  "summary": [
    "Memoria de materia consolidada para Electiva Semestre 8 Bloque 1.",
    "Sincronización transversal aplicada desde Filosofía del Derecho con enfoque conservador.",
    "Se transfieren solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Se preserva identidad institucional UnADM y estructura argumentativa jurídica.",
    "Se refuerzan trazabilidad de fuentes, normalización JSON y control de placeholders.",
    "Se evita trasladar contenido temático de Filosofía del Derecho sin evidencia local.",
    "Destino canónico: UnADM/licenciatura-en-derecho-unadm/electiva-semestre-8-bloque-1-lde.",
    "Supuesto: falta consigna temática específica de actividades locales de la electiva."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, tono y formato.",
    "Usar tono jurídico formal, claro y verificable.",
    "Conservar contexto curricular local: Licenciatura en Derecho, semestre 8, bloque 1, tipo Electiva.",
    "Mantener la carpeta de materia como punto de entrada canónico.",
    "Evitar renombrar la asignatura sin confirmación oficial.",
    "Mantener código provisional LDE-S8B1 hasta confirmación oficial distinta.",
    "Conservar autor y matrícula definidos en plantilla base.",
    "Marcar como supuesto todo dato no visible o no confirmado en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validación local.",
    "No eliminar reglas útiles previas; extender solo con evidencia verificable."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Declarar objetivo puntual antes del desarrollo.",
    "Organizar entregables en secuencia: problema, conceptos o fuentes, producto, análisis propio y conclusión.",
    "Separar conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por la planeación o consigna.",
    "Usar el programa analítico como guía de reportes, presentaciones y productos visuales.",
    "Conservar README, programa analítico, plantillas, bibliografía y referencias como base local.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Vincular el producto con al menos un problema jurídico o social delimitado.",
    "Relacionar conceptos, normas, doctrina o datos con el producto solicitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Diferenciar resumen de fuentes y postura propia.",
    "Evitar entregas solo descriptivas.",
    "Cerrar con postura académica sustentada.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Confirmar que el producto corresponda a la consigna de la actividad.",
    "No extrapolar fuentes, semanas o contenidos de otras materias sin evidencia local.",
    "No trasladar contenido temático de Filosofía del Derecho sin insumo verificable."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar respuestas no estructuradas antes de reutilizarlas.",
    "Validar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar consistencia entre portada, metadatos y nombre de asignatura.",
    "Revisar que la malla curricular respalde semestre, bloque y tipo.",
    "Marcar como pendiente todo dato no confirmado.",
    "Confirmar trazabilidad de afirmaciones con cita o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar que rutas locales citadas existan antes de usarlas como fuente.",
    "Corregir placeholders, literales de generador y caracteres corruptos antes de entrega.",
    "Compilar sin errores críticos ni referencias rotas."
  ],
  "latex_rules": [
    "Mantener plantilla LaTeX base de la materia para reportes.",
    "Mantener clase article con spanish, letterpaper y oneside en reporte.",
    "Usar codificación y acentos correctos en español.",
    "Mantener documenttitle, documentsubtitle, documentsubject, coursename y coursecode consistentes.",
    "Conservar definiciones de universidad y curso sin renombrados inconsistentes.",
    "Conservar universitydepartmentimage como departamentos/UnADM salvo cambio verificado.",
    "Completar campos pendientes de portada antes de entrega.",
    "Actualizar figura docente solo con nombre confirmado.",
    "No dejar créditos vacíos si el dato oficial está disponible.",
    "Usar electiva-semestre-8-bloque-1.bib como archivo bibliográfico local.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en archivos finales.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Verificar nombres de archivos del README antes de referenciarlos."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM como base contextual.",
    "Conservar unadmSitioWeb y unadmMallaDerecho2024 sin renombrar.",
    "Registrar fuentes específicas de cada actividad en el .bib local.",
    "Usar solo fuentes consultadas y verificables.",
    "No inventar referencias.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL.",
    "Mantener notas de consulta y ruta cuando la fuente sea local.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Agregar fuentes doctrinales, normativas o jurisprudenciales solo cuando la actividad las requiera.",
    "Validar que cada cita textual o paráfrasis tenga entrada BibTeX correspondiente."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar arriba y laterales reglas validadas de calidad, estructura y trazabilidad.",
    "Compartir solo abstracciones editoriales estables con nodos no equivalentes.",
    "No propagar metadatos específicos de esta electiva a materias no equivalentes.",
    "No propagar contenidos temáticos de Filosofía del Derecho al destino sin evidencia local.",
    "Aplicar unión y deduplicación lossless en cada ciclo.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Propagar la regla de no inventar fuentes a nodos relacionados.",
    "Propagar verificación de JSON parseable a nodos superiores.",
    "Registrar ciclos con salida no estructurada como normalización manual requerida."
  ],
  "open_questions": [
    "Confirmar créditos oficiales de la electiva para portada y README.",
    "Confirmar nombre de figura docente para plantilla base.",
    "Confirmar nombre oficial de la electiva si difiere del usado actualmente.",
    "Confirmar código oficial de asignatura frente al provisional LDE-S8B1.",
    "Confirmar existencia y consistencia de presentacion-electiva-semestre-8-bloque-1.tex.",
    "Corregir en README nombres de archivo con caracteres faltantes.",
    "Corregir en README tokens $(@{...}.Slug) sin expandir.",
    "Confirmar carpeta local de referencias y nombre canónico.",
    "Confirmar consignas específicas de actividades de la electiva.",
    "Confirmar fuentes obligatorias por semana o unidad.",
    "Supuesto: la malla curricular local respalda semestre 8, bloque 1 y tipo Electiva.",
    "Supuesto: no existe insumo temático local suficiente para reglas sustantivas adicionales."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Jurídicamente preciso.",
        "Claro y verificable.",
        "Argumentativo con criterio propio.",
        "Sobrio en inferencias.",
        "Conservador ante datos no confirmados."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Portada consistente con plantilla local.",
        "Entrada canónica por carpeta de materia.",
        "Supuestos etiquetados sin ambigüedad.",
        "Fuentes heredadas tratadas como provisionales."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 8.",
        "Bloque 1.",
        "Tipo Electiva.",
        "Código provisional LDE-S8B1.",
        "Transferencia profesional como criterio de cierre."
      ]
    },
    "essence": [
      "Identidad institucional UnADM.",
      "Estructura argumentativa jurídica.",
      "Problema jurídico o social delimitado.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeación.",
      "Análisis propio y postura académica.",
      "Conclusión transferible a la práctica jurídica.",
      "Trazabilidad de fuentes.",
      "Control de placeholders editoriales.",
      "Normalización estructurada antes de propagación."
    ],
    "reason_for_being": [
      "Orientar productos académicos de la electiva con claridad y fundamento jurídico.",
      "Transformar la planeación semanal en reportes, presentaciones y productos visuales.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Garantizar entregables verificables, compilables y alineados con UnADM.",
      "Conservar memoria editorial persistente sin pérdida de reglas útiles."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Encuadre breve del problema.",
      "Secciones estables y reutilizables.",
      "Fuentes citadas de forma verificable.",
      "Postura propia diferenciada del resumen.",
      "Supuestos etiquetados.",
      "Cierre jurídico transferible.",
      "Metadatos curriculares consistentes.",
      "No renombrar sin confirmación.",
      "No inventar fuentes."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/fuentes -> análisis -> conclusión.",
      "Afirmación -> evidencia verificable -> inferencia jurídica.",
      "Descripción breve -> posición crítica -> implicación práctica.",
      "Consigna -> producto solicitado -> estructura de entrega.",
      "Dato no confirmado -> marca de supuesto -> pregunta abierta.",
      "Fuente local -> cita BibTeX -> trazabilidad editorial.",
      "Regla heredada -> validación local -> propagación conservadora."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Licenciatura en Derecho",
        "Electiva Semestre 8 Bloque 1",
        "Código provisional LDE-S8B1",
        "Problema jurídico o social",
        "Conceptos jurídicos pertinentes",
        "Marco normativo o doctrinal",
        "Producto solicitado por planeación",
        "Análisis propio",
        "Postura académica sustentada",
        "Conclusión jurídica transferible",
        "Trazabilidad de fuentes",
        "Bibliografía local",
        "Normalización JSON",
        "Control de placeholders",
        "Compilación LaTeX estable",
        "Malla curricular de Derecho",
        "Supuestos editoriales",
        "Propagación transversal conservadora",
        "Unión-dedupe lossless"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Portada consistente",
          "kind": "supports",
          "justification": "Define tono, formato y metadatos institucionales."
        },
        {
          "source": "Malla curricular de Derecho",
          "target": "Contexto curricular local",
          "kind": "supports",
          "justification": "Respalda semestre, bloque y tipo cuando se verifica localmente."
        },
        {
          "source": "Contexto curricular local",
          "target": "Código provisional LDE-S8B1",
          "kind": "depends_on",
          "justification": "El código se mantiene provisional hasta confirmación oficial."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "El análisis parte de un problema delimitado."
        },
        {
          "source": "Conceptos jurídicos pertinentes",
          "target": "Marco normativo o doctrinal",
          "kind": "develops",
          "justification": "Los conceptos ordenan la explicación normativa o doctrinal."
        },
        {
          "source": "Producto solicitado por planeación",
          "target": "Estructura de entrega",
          "kind": "depends_on",
          "justification": "La forma final se ajusta a la consigna."
        },
        {
          "source": "Trazabilidad de fuentes",
          "target": "Calidad académica",
          "kind": "supports",
          "justification": "Evita afirmaciones sin respaldo y referencias inventadas."
        },
        {
          "source": "Bibliografía local",
          "target": "Citas verificables",
          "kind": "supports",
          "justification": "Conecta fuentes consultadas con entradas BibTeX estables."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación transversal conservadora",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay reutilización confiable."
        },
        {
          "source": "Control de placeholders",
          "target": "Compilación LaTeX estable",
          "kind": "supports",
          "justification": "Reduce errores por tokens sin expandir y rutas corruptas."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "develops",
          "justification": "La conclusión sintetiza la postura y su utilidad profesional."
        },
        {
          "source": "Unión-dedupe lossless",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Conserva reglas útiles sin duplicación semántica."
        }
      ],
      "evidence": [
        "README local declara materia de la Licenciatura en Derecho de la UnADM.",
        "README local ubica la materia en semestre 8, bloque 1, tipo Electiva.",
        "README local deja créditos vacíos.",
        "README local contiene nombres corruptos de reporte y referencias.",
        "README local contiene token $(@{...}.Slug) sin expandir.",
        "Programa analítico local fija ejes: problema, conceptos, producto, análisis y conclusión.",
        "Programa analítico local exige claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Archivo electiva-semestre-8-bloque-1.bib contiene unadmSitioWeb.",
        "Archivo electiva-semestre-8-bloque-1.bib contiene unadmMallaDerecho2024.",
        "Plantilla LaTeX local define autor Martin Jonathan de la Cruz y matrícula ES2611202040.",
        "Plantilla LaTeX local mantiene figura docente por definir.",
        "Plantilla LaTeX local mantiene créditos vacíos.",
        "Memoria heredada registra antecedente de salida no JSON parseable.",
        "Regla transversal estable: no inventar fuentes.",
        "Regla transversal estable: validar JSON antes de propagación."
      ]
    },
    "reinforcement_log": [
      "Ciclo 5 consolida destino como cerebro editorial de materia.",
      "Se deduplican reglas repetidas de identidad, estructura y calidad.",
      "Se preservan reglas útiles previas sin regresión.",
      "Se incorporan solo abstracciones transferibles desde Filosofía del Derecho.",
      "Se evita importar jurisprudencia, doctrina o bibliografía temática no verificable para la electiva.",
      "Se refuerza control de placeholders detectados en README y programa analítico.",
      "Se refuerza consistencia entre portada, README, .bib y plantilla LaTeX.",
      "Se mantienen vacíos locales como preguntas abiertas o supuestos."
    ]
  }
}