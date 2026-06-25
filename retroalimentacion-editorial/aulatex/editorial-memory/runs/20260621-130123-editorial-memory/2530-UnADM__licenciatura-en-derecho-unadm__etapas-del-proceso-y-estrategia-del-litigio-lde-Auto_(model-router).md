{
  "summary": [
    "Materia destino consolidada con identidad UnADM y enfoque jurídico aplicado.",
    "Sincronización transversal desde actividad no equivalente mediante abstracciones editoriales estables.",
    "Se preservan reglas locales verificables de semestre 5, bloque 2, obligatoria y 8 créditos.",
    "Se mantiene compresión union-dedupe sin pérdida y sin regresión.",
    "Se exige JSON parseable antes de cualquier propagación recursiva.",
    "Se refuerzan cinco ejes editoriales: problema, conceptos, producto, análisis propio y conclusión transferible.",
    "Se separan fuentes provisionales de autoridad académica.",
    "Se conserva la carpeta de asignatura como punto de entrada canónico."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, tono y metadatos.",
    "Alinear entregables con Licenciatura en Derecho.",
    "Usar contexto local: semestre 5, bloque 2, obligatoria, 8 créditos.",
    "Citar malla-curricular-derecho-unadm.pdf para ubicación curricular.",
    "Usar tono académico-jurídico formal, claro y verificable.",
    "Exigir postura propia sustentada en cada producto.",
    "Conservar trazabilidad de origen editorial en cada consolidación.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Marcar como [supuesto] todo dato no visible en consigna o documentos locales.",
    "Registrar fuentes heredadas no verificadas como nota técnica, no como autoridad académica.",
    "Usar macros de portada: documenttitle, coursename, coursecode y universityname.",
    "Usar coursecode LDE-S5B2 mientras no exista corrección institucional. [supuesto]",
    "Mantener autor de plantilla Martin Jonathan de la Cruz salvo instrucción de actividad o docente. [supuesto]"
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Desarrollar normas, doctrina, datos o evidencias pertinentes al caso.",
    "Alinear la estructura al producto solicitado en la planeación semanal.",
    "Adaptar la salida a reporte, presentación o producto visual según consigna.",
    "Usar el programa analítico como guía de ejes editoriales.",
    "Incluir análisis propio antes del cierre.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener README como entrada canónica de la asignatura."
  ],
  "activity_rules": [
    "Verificar la instrucción específica de cada actividad antes de redactar.",
    "Rubricar cada entrega contra los ejes del programa analítico.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Incluir postura argumentada del estudiante.",
    "Agregar fuentes específicas de actividad al .bib local antes de la versión final.",
    "No reutilizar reglas laterales sin comprobar pertinencia jurídica.",
    "No trasladar contenido literal de actividades de otra materia.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Confirmar que el producto corresponda a la consigna local."
  ],
  "quality_gates": [
    "Validar JSON parseable en toda memoria antes de fusionar o propagar.",
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Aplicar union-dedupe sin eliminar reglas útiles previas.",
    "Confirmar ausencia de contradicciones con reglas heredadas de institución.",
    "Comprobar que cada afirmación factual tenga fuente o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar respuestas no estructuradas antes de reutilizarlas.",
    "Normalizar manualmente memorias heredadas no parseables.",
    "Revisar consistencia entre metadatos de materia y contenido entregado.",
    "Validar que nombres de archivos en README no contengan variables sin resolver.",
    "Revisar caracteres corruptos en README y plantilla antes de publicar. [supuesto]",
    "Compilar sin errores críticos y sin referencias rotas."
  ],
  "latex_rules": [
    "Usar la plantilla .tex local de la materia como base de nuevas actividades.",
    "Usar reporte-etapas-del-proceso-y-estrategia-del-litigio.tex para reportes.",
    "Usar presentacion-etapas-del-proceso-y-estrategia-del-litigio.tex para presentaciones si el archivo existe. [supuesto]",
    "Conservar macros institucionales de curso, universidad y asignatura.",
    "No eliminar campos de portada; completar faltantes según actividad.",
    "Conservar bloque authortable de la plantilla al adaptar portada.",
    "Usar documentclass article con opciones spanish, letterpaper y oneside cuando se derive de la plantilla local.",
    "Mantener compatibilidad con español y acentos correctos en .tex y .bib.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Mantener claves BibTeX estables para evitar compilaciones rotas.",
    "No confiar en nombres generados con variables sin resolver en README o markdown.",
    "Resolver tokens sin expandir como $(@{...}.Slug) antes de referenciar archivos.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Verificar nombres reales de archivos antes de citarlos o incluirlos."
  ],
  "bibliography_rules": [
    "Usar etapas-del-proceso-y-estrategia-del-litigio.bib como repositorio local.",
    "Conservar fuentes institucionales registradas: unadmSitioWeb y unadmMallaDerecho2024.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Agregar entradas BibTeX específicas de actividad antes de citar.",
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "No citar bibliografía base si no fue usada en el argumento.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Incluir fecha de consulta cuando la fuente sea web o institucional dinámica.",
    "Distinguir bibliografía base, bibliografía local y bibliografía específica de actividad.",
    "Validar correspondencia entre citas en texto y entradas .bib.",
    "No asumir que bibliografía de materias laterales corresponde a esta asignatura."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar arriba y laterales reglas de JSON parseable y no regresión.",
    "Propagar union-dedupe como método de compresión lossless.",
    "Propagar a materias vecinas de Derecho los cinco ejes editoriales generales.",
    "Propagar el patrón problema, fundamento, análisis propio y conclusión jurídica.",
    "Propagar la restricción de no inventar fuentes.",
    "Propagar solo abstracciones editoriales entre nodos no equivalentes.",
    "No propagar metadatos específicos de esta materia a otros nodos.",
    "Mantener metadatos curriculares locales dentro del nodo destino.",
    "Aplicar normalización manual si se detecta salida no estructurada.",
    "Marcar herencias provisionales como notas técnicas hasta verificación local.",
    "Evitar regresiones respecto de reglas útiles previas."
  ],
  "open_questions": [
    "Confirmar si el nombre de autor en plantilla es definitivo o variable por estudiante.",
    "Confirmar estilo de citación jurídica requerido: APA, Chicago, ISO 690 u otro.",
    "Confirmar código de curso correcto; plantilla usa LDE-S5B2. [supuesto]",
    "Confirmar existencia operativa de presentacion-etapas-del-proceso-y-estrategia-del-litigio.tex. [supuesto]",
    "Corregir nombres corruptos en README y validar nombres reales de archivos. [supuesto]",
    "Confirmar si la fuente provisional Codex debe conservarse solo como nota técnica.",
    "Definir checklist mínimo por tipo de producto: reporte, presentación y material visual.",
    "Confirmar rúbricas específicas de cada actividad antes de redactar.",
    "Confirmar fuentes obligatorias de cada semana o unidad.",
    "Confirmar si el .bib local es el único repositorio bibliográfico de la materia."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Jurídicamente preciso.",
        "Claro y verificable.",
        "Argumentativo con criterio propio.",
        "Aplicado a la práctica profesional.",
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
        "Semestre 5, bloque 2, obligatoria, 8 créditos.",
        "Fuente curricular local: malla-curricular-derecho-unadm.pdf.",
        "Coursecode visible en plantilla: LDE-S5B2. [supuesto]"
      ]
    },
    "essence": [
      "Identidad UnADM.",
      "Fundamento jurídico verificable.",
      "Cinco ejes editoriales.",
      "Problema jurídico o social inicial.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeación.",
      "Análisis propio y postura académica.",
      "Conclusión transferible a la práctica jurídica.",
      "Normalización estructurada.",
      "Union-dedupe sin regresión.",
      "Transferencia transversal por abstracciones."
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
      "Transformar la planeación semanal en reportes, presentaciones y productos visuales.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Evitar productos meramente descriptivos.",
      "Sostener una memoria editorial persistente y verificable.",
      "Permitir propagación recursiva segura sin pérdida de reglas útiles."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Objetivo explícito.",
      "Bloques argumentativos visibles.",
      "Marco normativo o doctrinal diferenciado.",
      "Citas trazables.",
      "Postura propia sustentada.",
      "Cierre jurídico aplicable.",
      "Supuestos marcados.",
      "Metadatos UnADM consistentes.",
      "Lenguaje jurídico claro."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> fundamento -> análisis propio -> conclusión jurídica.",
      "Afirmación -> evidencia verificable -> interpretación -> implicación práctica.",
      "Consigna -> producto esperado -> criterios -> desarrollo -> autocheck.",
      "Norma o doctrina -> aplicación al caso -> postura razonada.",
      "Fuente institucional -> dato curricular -> uso editorial limitado.",
      "Supuesto -> justificación -> pendiente de verificación.",
      "Memoria heredada -> normalización -> deduplicación -> propagación segura."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Licenciatura en Derecho",
        "Etapas del proceso y estrategia del litigio",
        "Semestre 5 bloque 2",
        "Materia obligatoria de 8 créditos",
        "Carpeta de asignatura como entrada canónica",
        "Programa analítico editorial",
        "Cinco ejes editoriales",
        "Problema jurídico o social",
        "Conceptos jurídicos pertinentes",
        "Marco normativo o doctrinal",
        "Evidencia verificable",
        "Análisis propio",
        "Postura académica",
        "Conclusión jurídica transferible",
        "Producto solicitado por planeación",
        "Reporte académico",
        "Presentación académica",
        "Producto visual",
        "JSON parseable",
        "Normalización estructurada",
        "Union-dedupe sin regresión",
        "Fuentes provisionales",
        "Bibliografía local",
        "Claves BibTeX estables",
        "Tokens sin resolver",
        "Compilación LaTeX sin errores críticos"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Portada y metadatos institucionales",
          "kind": "supports",
          "justification": "La pauta local exige conservar identidad UnADM en cada actividad."
        },
        {
          "source": "Malla curricular de Derecho",
          "target": "Semestre 5 bloque 2",
          "kind": "supports",
          "justification": "El README local declara la ubicación curricular con fuente institucional."
        },
        {
          "source": "Programa analítico editorial",
          "target": "Cinco ejes editoriales",
          "kind": "develops",
          "justification": "El programa enumera problema, conceptos, producto, análisis propio y conclusión."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Estructura de entrega",
          "kind": "develops",
          "justification": "Los ejes ordenan el desarrollo de reportes, presentaciones y productos visuales."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La pauta editorial exige citas verificables y fuentes trazables."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "develops",
          "justification": "La conclusión debe derivar de una postura argumentada, no de un resumen."
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
          "source": "Fuentes provisionales",
          "target": "Autoridad académica",
          "kind": "contrasts",
          "justification": "Las fuentes heredadas no verificadas se conservan como nota técnica."
        },
        {
          "source": "Tokens sin resolver",
          "target": "Compilación LaTeX sin errores críticos",
          "kind": "contrasts",
          "justification": "Los nombres con variables sin expandir pueden romper rutas y referencias."
        },
        {
          "source": "Bibliografía local",
          "target": "Claves BibTeX estables",
          "kind": "depends_on",
          "justification": "Las citas trazables requieren entradas estables en el .bib de la materia."
        },
        {
          "source": "Transferencia transversal por abstracciones",
          "target": "Pertinencia local",
          "kind": "supports",
          "justification": "Entre materias no equivalentes se heredan patrones, no redacción ni fuentes específicas."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 5, bloque 2, obligatoria, 8 créditos.",
        "README local: fuente curricular UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: actividades con identidad UnADM, integridad académica, citas verificables y conclusión jurídica con criterio propio.",
        "Programa analítico local: productos académicos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: propósito de transformar planeación semanal en reportes, presentaciones y productos visuales.",
        "Programa analítico local: ejes de trabajo problema, conceptos, producto, análisis propio y conclusión.",
        "Bib local: entrada unadmSitioWeb.",
        "Bib local: entrada unadmMallaDerecho2024.",
        "Plantilla .tex local: macros documenttitle, coursename, coursecode y universityname.",
        "Plantilla .tex local: coursecode visible LDE-S5B2.",
        "Memoria heredada: salida no JSON parseable requiere normalización manual.",
        "Memoria consolidada: bloquear propagación si la salida no es JSON parseable.",
        "Memoria consolidada: aplicar union-dedupe sin eliminar reglas útiles previas."
      ]
    },
    "reinforcement_log": [
      "Ciclo 17: se consolida destino sin transferir contenido literal de Filosofía del Derecho.",
      "Ciclo 17: se refuerza transferencia transversal por abstracciones editoriales estables.",
      "Ciclo 17: se preserva contexto local verificable de la materia destino.",
      "Ciclo 17: se normalizan duplicados semánticos y variantes con acentos.",
      "Ciclo 17: se mantienen reglas previas útiles de identidad, estructura, calidad, LaTeX y bibliografía.",
      "Ciclo 17: se restringen citas del grafo a claves locales verificadas.",
      "Ciclo 17: se conserva advertencia sobre fuentes provisionales heredadas.",
      "Ciclo 17: se refuerza validación JSON parseable antes de propagación recursiva.",
      "Ciclo 17: se refuerza no inventar fuentes ni asumir bibliografía de materias laterales.",
      "Ciclo 17: se agregan relaciones conceptuales con tipos permitidos y justificación breve."
    ]
  }
}