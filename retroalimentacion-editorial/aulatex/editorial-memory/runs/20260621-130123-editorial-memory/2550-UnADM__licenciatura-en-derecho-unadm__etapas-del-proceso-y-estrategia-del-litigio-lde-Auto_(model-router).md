{
  "summary": [
    "Materia destino consolidada con identidad UnADM y enfoque jurídico aplicado.",
    "Sincronización transversal desde actividad no equivalente mediante abstracciones editoriales estables.",
    "Se preservan cinco ejes editoriales: problema, conceptos, producto, análisis propio y conclusión transferible.",
    "Se mantiene compresión union-dedupe sin pérdida y sin regresión.",
    "Toda propagación requiere JSON parseable y normalización previa.",
    "Fuentes heredadas no verificadas quedan como provisionales y fuera de autoridad académica.",
    "Contexto local verificado: Licenciatura en Derecho, semestre 5, bloque 2, obligatoria, 8 créditos.",
    "La carpeta local funciona como entrada canónica de la asignatura."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, tono y metadatos.",
    "Alinear entregables con Licenciatura en Derecho.",
    "Usar contexto curricular local: semestre 5, bloque 2, obligatoria, 8 créditos.",
    "Usar tono académico-jurídico formal, claro y verificable.",
    "Exigir postura propia sustentada en cada producto.",
    "Conservar trazabilidad de origen editorial en cada consolidación.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como [supuesto] todo dato no visible en consigna o documentos locales.",
    "Registrar fuentes provisionales como nota técnica, no como autoridad académica.",
    "Usar macros de portada documenttitle, documentsubtitle, documentsubject, coursename, coursecode y universityname.",
    "Usar coursecode LDE-S5B2 mientras no exista corrección institucional. [supuesto]",
    "Mantener documentauthor de plantilla salvo instrucción docente o de actividad. [supuesto]"
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Desarrollar conceptos, normas, doctrina o datos pertinentes al caso.",
    "Adaptar la salida al producto pedido: reporte, presentación o visual.",
    "Alinear la entrega con la planeación semanal.",
    "Usar el programa analítico como guía de ejes editoriales.",
    "Aplicar cinco ejes: problema, conceptos, producto solicitado, análisis propio y conclusión transferible.",
    "Cerrar con conclusión jurídica aplicable a la práctica profesional.",
    "Evitar estructuras solo descriptivas o de resumen."
  ],
  "activity_rules": [
    "Verificar la instrucción específica de cada actividad antes de redactar.",
    "Confirmar producto exacto solicitado antes de elegir plantilla.",
    "Rubricar cada entrega contra los ejes del programa analítico.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Integrar evidencia trazable en el cuerpo del trabajo.",
    "Incluir postura argumentada del estudiante.",
    "Exigir conclusión jurídica con criterio propio.",
    "Agregar fuentes específicas de actividad al .bib local antes de versión final.",
    "No reutilizar reglas laterales sin comprobar pertinencia jurídica.",
    "No asumir fuentes de otra materia o semana como obligatorias para esta asignatura."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de fusionar o propagar memoria.",
    "Bloquear propagación si la salida no es estructurada.",
    "Revisar memoria no estructurada antes de aplicarla aguas abajo.",
    "Comprobar union-dedupe sin eliminar reglas útiles previas.",
    "Revisar estructura mínima completa antes de consolidar.",
    "Validar consistencia entre metadatos de materia y contenido entregado.",
    "Comprobar que cada afirmación factual tenga fuente o marca de supuesto.",
    "Confirmar ausencia de contradicciones con reglas institucionales heredadas.",
    "Validar correspondencia entre producto final y consigna de actividad.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar caracteres corruptos en README y plantillas antes de publicar.",
    "Validar que nombres de archivo no contengan variables sin resolver."
  ],
  "latex_rules": [
    "Usar la plantilla .tex local de la materia como base.",
    "Usar reporte-etapas-del-proceso-y-estrategia-del-litigio.tex para reportes.",
    "Usar presentacion-etapas-del-proceso-y-estrategia-del-litigio.tex si existe para presentaciones. [supuesto]",
    "Conservar documentclass article con opciones spanish, letterpaper y oneside.",
    "Conservar macros institucionales de curso, universidad y asignatura.",
    "No eliminar campos de portada; completar faltantes según actividad.",
    "Conservar bloque authortable de la plantilla al adaptar portada.",
    "Mantener compatibilidad con español y acentos correctos en .tex y .bib.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "No confiar en nombres generados con variables sin resolver en README o markdown.",
    "Resolver token de Slug antes de referenciar el archivo .bib.",
    "Corregir nombres corruptos visibles en README antes de citarlos.",
    "Supuesto: el .bib canónico local es etapas-del-proceso-y-estrategia-del-litigio.bib."
  ],
  "bibliography_rules": [
    "Usar etapas-del-proceso-y-estrategia-del-litigio.bib como repositorio local.",
    "Conservar claves institucionales unadmSitioWeb y unadmMallaDerecho2024.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Agregar entradas BibTeX específicas de actividad antes de citar.",
    "No inventar referencias.",
    "Usar solo obras realmente consultadas y verificables.",
    "No citar bibliografía base si no fue usada en el argumento.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Incluir fecha de consulta en fuentes web o institucionales dinámicas.",
    "Validar que toda cita textual o parafraseada tenga entrada .bib correspondiente."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar arriba y laterales la regla de JSON parseable.",
    "Propagar arriba y laterales la regla de union-dedupe sin regresión.",
    "Propagar a materias de Derecho los cinco ejes editoriales generales.",
    "Propagar solo abstracciones estables entre nodos no equivalentes.",
    "No propagar metadatos específicos de esta materia a nodos vecinos.",
    "No transferir redacción literal de actividades de Filosofía del Derecho.",
    "Mantener fuentes provisionales separadas de autoridad académica.",
    "Aplicar normalización manual si se detectan salidas no estructuradas heredadas.",
    "Conservar advertencia: ciclo 1 requiere normalización manual si se reutiliza."
  ],
  "open_questions": [
    "Confirmar estilo de citación jurídica requerido: APA, Chicago, ISO 690 u otro.",
    "Confirmar si documentauthor es fijo de plantilla o variable por estudiante. [supuesto]",
    "Confirmar código de curso correcto; la plantilla usa LDE-S5B2. [supuesto]",
    "Confirmar existencia operativa de presentacion-etapas-del-proceso-y-estrategia-del-litigio.tex. [supuesto]",
    "Corregir nombres corruptos en README y validar nombres reales de archivos.",
    "Confirmar si el token Slug del README debe resolverse siempre al .bib local.",
    "Definir checklist mínimo por tipo de producto: reporte, presentación y material visual.",
    "Confirmar rúbrica específica de cada actividad antes de ajustar profundidad argumentativa.",
    "Confirmar fuentes obligatorias de cada semana.",
    "Confirmar si las fuentes provisionales Codex o GPT-Pro deben conservarse solo como notas técnicas."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Verificable y orientado a práctica profesional.",
        "Conservador en propagación editorial."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Portada y metadatos institucionales conservados.",
        "Carpeta de asignatura como entrada canónica.",
        "Trazabilidad editorial en consolidaciones.",
        "Fuentes provisionales separadas de autoridad académica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Etapas del proceso y estrategia del litigio.",
        "Semestre 5, bloque 2.",
        "Obligatoria, 8 créditos.",
        "Fuente curricular local: malla-curricular-derecho-unadm.pdf.",
        "Coursecode visible en plantilla: LDE-S5B2. [supuesto]"
      ]
    },
    "essence": [
      "Identidad UnADM aplicada a productos jurídicos.",
      "Problema jurídico o social como punto de partida.",
      "Conceptos, normas, doctrina y datos pertinentes.",
      "Producto ajustado a planeación semanal.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible a la práctica.",
      "Evidencia verificable y citas trazables.",
      "Normalización estructurada antes de propagar.",
      "Memoria persistente por union-dedupe sin regresión."
    ],
    "reason_for_being": [
      "Transformar planeación semanal en productos académicos jurídicos.",
      "Integrar problema, fuentes, análisis propio y cierre argumentativo.",
      "Orientar reportes, presentaciones y productos visuales con fundamento jurídico.",
      "Conectar formación jurídica con práctica profesional.",
      "Sostener integridad académica mediante evidencia verificable.",
      "Evitar entregas descriptivas sin criterio propio."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Objetivo puntual visible.",
      "Bloques argumentativos claros.",
      "Marco normativo o doctrinal separado.",
      "Citas trazables en el cuerpo.",
      "Postura personal sustentada.",
      "Cierre jurídico aplicable.",
      "Supuestos marcados explícitamente.",
      "Metadatos institucionales completos.",
      "Lenguaje jurídico sobrio y preciso."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual -> marco normativo -> análisis propio -> conclusión jurídica.",
      "Afirmación -> evidencia verificable -> interpretación -> implicación práctica.",
      "Consigna -> producto solicitado -> estructura adecuada -> rúbrica de revisión.",
      "Dato local -> fuente institucional -> marca de supuesto si falta verificación.",
      "Regla heredada -> pertinencia local -> adopción conservadora.",
      "Concepto jurídico -> aplicación al caso -> consecuencia procesal o estratégica.",
      "Postura del estudiante -> fundamento -> límite del argumento -> cierre profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Licenciatura en Derecho",
        "Etapas del proceso y estrategia del litigio",
        "Semestre 5 bloque 2",
        "Asignatura obligatoria de 8 créditos",
        "Entrada canónica de asignatura",
        "Cinco ejes editoriales",
        "Problema jurídico o social",
        "Conceptos jurídicos pertinentes",
        "Marco normativo o doctrinal",
        "Evidencia verificable",
        "Análisis propio",
        "Postura académica",
        "Conclusión jurídica transferible",
        "Práctica profesional",
        "Producto solicitado por planeación",
        "Reporte académico",
        "Presentación académica",
        "Material visual",
        "Bibliografía local",
        "Fuentes institucionales UnADM",
        "JSON parseable",
        "Normalización estructurada",
        "Union-dedupe sin regresión",
        "Fuentes provisionales",
        "Variables sin resolver",
        "Caracteres corruptos en README"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad académica con citas verificables",
          "kind": "supports",
          "justification": "La pauta editorial local exige identidad institucional, citas verificables y conclusión jurídica."
        },
        {
          "source": "Programa analítico local",
          "target": "Cinco ejes editoriales",
          "kind": "develops",
          "justification": "El programa enumera problema, conceptos, producto, análisis propio y conclusión transferible."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Estructura de entrega",
          "kind": "develops",
          "justification": "Los ejes ordenan la construcción de reportes, presentaciones y productos visuales."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "La postura argumentada requiere un problema claro que active el razonamiento jurídico."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "El cierre profesional debe apoyarse en fundamentos jurídicos y evidencia."
        },
        {
          "source": "Evidencia verificable",
          "target": "Postura académica",
          "kind": "supports",
          "justification": "La postura propia no debe ser solo opinión; requiere citas y fuentes consultables."
        },
        {
          "source": "Bibliografía local",
          "target": "Citas trazables",
          "kind": "supports",
          "justification": "El .bib local centraliza fuentes institucionales y específicas de actividad."
        },
        {
          "source": "JSON parseable",
          "target": "Propagación recursiva segura",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay fusión confiable aguas abajo."
        },
        {
          "source": "Union-dedupe sin regresión",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Permite compresión lossless sin borrar reglas útiles previas."
        },
        {
          "source": "Variables sin resolver",
          "target": "Compilación LaTeX confiable",
          "kind": "contrasts",
          "justification": "Los tokens no expandidos rompen referencias canónicas y deben corregirse."
        },
        {
          "source": "Caracteres corruptos en README",
          "target": "Trazabilidad de archivos",
          "kind": "contrasts",
          "justification": "Los nombres corruptos impiden identificar plantillas y carpetas reales."
        },
        {
          "source": "Fuentes provisionales",
          "target": "Autoridad académica",
          "kind": "contrasts",
          "justification": "Las fuentes heredadas no verificadas se conservan como nota técnica, no como sustento académico."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 5, bloque 2, obligatoria, 8 créditos.",
        "README local: fuente curricular malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: integridad académica, citas verificables y conclusión jurídica con criterio propio.",
        "Programa analítico local: productos académicos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: propósito de transformar planeación semanal en reportes, presentaciones y productos visuales.",
        "Programa analítico local: cinco ejes de trabajo.",
        "Bib local: claves unadmSitioWeb y unadmMallaDerecho2024.",
        "Plantilla .tex local: documentclass article con spanish, letterpaper y oneside.",
        "Plantilla .tex local: macros documenttitle, documentsubtitle, documentsubject, coursename, coursecode y universityname.",
        "Plantilla .tex local: coursecode LDE-S5B2 visible.",
        "README local: token Slug sin resolver para archivo .bib.",
        "README local: nombres de archivo con caracteres corruptos visibles.",
        "Memoria heredada: salida no JSON parseable requiere normalización manual.",
        "Memoria consolidada: compresión union-dedupe sin regresión."
      ]
    },
    "reinforcement_log": [
      "Ciclo 22: se consolida sincronización transversal conservadora.",
      "Se transfieren abstracciones estables desde actividad no equivalente.",
      "Se evita importar contenido específico de Filosofía del Derecho.",
      "Se refuerzan identidad UnADM, estructura reusable y gates de calidad.",
      "Se preserva contexto curricular local verificado.",
      "Se mantienen fuentes provisionales fuera de autoridad académica.",
      "Se refuerza corrección de tokens sin resolver y nombres corruptos.",
      "Se conserva regla de no inventar fuentes.",
      "Se fortalece grafo conceptual local para litigio y productos jurídicos."
    ]
  }
}