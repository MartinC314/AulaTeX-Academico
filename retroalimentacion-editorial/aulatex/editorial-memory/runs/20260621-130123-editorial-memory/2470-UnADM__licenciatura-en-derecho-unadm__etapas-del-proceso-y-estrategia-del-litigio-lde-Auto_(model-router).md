{
  "summary": [
    "Materia destino consolidada con identidad UnADM y enfoque jurídico aplicado.",
    "Sincronización transversal ciclo 2 completada con unión-dedupe sin regresión.",
    "Se transfieren abstracciones editoriales estables, no redacción literal del origen.",
    "Se preservan cinco ejes editoriales: problema, conceptos, producto, análisis propio y conclusión.",
    "Se mantiene validación JSON parseable antes de cualquier propagación.",
    "Las fuentes heredadas no verificadas quedan como provisionales y no como autoridad académica.",
    "El contexto local verificable ubica la asignatura en semestre 5, bloque 2, obligatoria, 8 créditos.",
    "La carpeta de asignatura funciona como entrada canónica local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 2, obligatoria, 8 créditos.",
    "Usar tono académico-jurídico formal, claro y preciso.",
    "Exigir postura propia sustentada en cada producto.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Conservar trazabilidad del origen editorial al consolidar memoria.",
    "Marcar como [supuesto] todo dato no visible en consigna o documentos locales.",
    "Registrar fuentes provisionales como nota técnica, no como autoridad académica.",
    "Usar macros de portada: documenttitle, documentsubtitle, documentsubject, coursename, coursecode y universityname.",
    "Usar coursecode LDE-S5B2 mientras no exista corrección institucional. [supuesto]",
    "Mantener documentauthor de plantilla salvo instrucción de actividad o docente. [supuesto]"
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar bloques: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Desarrollar conceptos, normas, doctrina o datos pertinentes al caso.",
    "Alinear la estructura al producto solicitado por la planeación semanal.",
    "Adaptar la salida al producto pedido: reporte, presentación o visual.",
    "Incluir análisis propio antes del cierre.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener README como entrada canónica de la asignatura.",
    "Usar el programa analítico como guía de ejes editoriales."
  ],
  "activity_rules": [
    "Verificar la instrucción específica de cada actividad antes de redactar.",
    "Rubricar cada entrega contra los cinco ejes del programa analítico.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Integrar evidencia trazable en el cuerpo del trabajo.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Incluir criterio jurídico propio en cada conclusión.",
    "Agregar fuentes específicas de actividad al .bib local antes de la versión final.",
    "No reutilizar reglas laterales sin comprobar pertinencia jurídica.",
    "No asumir que fuentes de otra actividad correspondan a la actividad actual."
  ],
  "quality_gates": [
    "Validar JSON parseable en toda memoria antes de fusionar o propagar.",
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Aplicar unión-dedupe sin eliminar reglas útiles previas.",
    "Confirmar ausencia de contradicciones con reglas institucionales heredadas.",
    "Comprobar que cada afirmación factual tenga fuente o marca de supuesto.",
    "Revisar consistencia entre metadatos de materia y contenido entregado.",
    "Validar correspondencia entre citas en texto y archivo .bib.",
    "Revisar respuestas no estructuradas antes de reutilizarlas.",
    "Normalizar manualmente memorias provenientes de ciclos no parseables.",
    "Validar que nombres de archivos en README no contengan variables sin resolver.",
    "Revisar caracteres corruptos en README y plantilla antes de publicar. [supuesto]"
  ],
  "latex_rules": [
    "Usar la plantilla .tex local de la materia como base de nuevas actividades.",
    "Usar reporte-etapas-del-proceso-y-estrategia-del-litigio.tex para reportes.",
    "Usar presentacion-etapas-del-proceso-y-estrategia-del-litigio.tex para presentaciones si existe operativamente. [supuesto]",
    "Conservar macros institucionales de curso, universidad y asignatura.",
    "No eliminar campos de portada; completar faltantes según actividad.",
    "Mantener compatibilidad con español y formato letterpaper de la plantilla.",
    "Usar documentclass article con opciones spanish, letterpaper y oneside cuando se derive del reporte local.",
    "Conservar bloque authortable de la plantilla al adaptar portada.",
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "No confiar en nombres generados con variables sin resolver en README o markdown.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) antes de referenciar archivos."
  ],
  "bibliography_rules": [
    "Usar etapas-del-proceso-y-estrategia-del-litigio.bib como repositorio local.",
    "Conservar fuentes institucionales registradas: sitio UnADM y malla curricular Derecho.",
    "Conservar claves BibTeX unadmSitioWeb y unadmMallaDerecho2024.",
    "Agregar entradas BibTeX específicas de actividad antes de citar.",
    "No inventar referencias.",
    "Registrar solo fuentes consultadas y verificables.",
    "No citar bibliografía base si no fue usada en el argumento.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Incluir fecha de consulta cuando la fuente sea web o institucional dinámica.",
    "Validar correspondencia entre citas en texto y entradas .bib."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar arriba y laterales la regla de JSON parseable.",
    "Propagar arriba y laterales la regla de unión-dedupe sin regresión.",
    "Propagar a materias vecinas de Derecho los cinco ejes editoriales.",
    "Propagar solo abstracciones generales entre nodos no equivalentes.",
    "No propagar metadatos específicos de esta materia a otros nodos.",
    "No propagar redacción literal de actividades.",
    "Propagar la restricción de no inventar fuentes.",
    "Propagar la advertencia de normalización manual para memorias no estructuradas.",
    "Mantener fuentes provisionales fuera de autoridad académica."
  ],
  "open_questions": [
    "Confirmar si documentauthor debe ser fijo de plantilla o variable por estudiante.",
    "Confirmar código de curso correcto; la plantilla usa LDE-S5B2. [supuesto]",
    "Confirmar estilo de citación jurídica requerido: APA, Chicago, ISO 690 u otro.",
    "Confirmar existencia operativa de presentacion-etapas-del-proceso-y-estrategia-del-litigio.tex. [supuesto]",
    "Corregir nombres corruptos en README y validar nombres reales de archivos. [supuesto]",
    "Definir checklist mínimo por tipo de producto: reporte, presentación y material visual.",
    "Confirmar si la fuente provisional Codex debe conservarse solo como nota técnica.",
    "Confirmar rúbricas específicas por actividad antes de fijar profundidad argumentativa.",
    "Confirmar fuentes obligatorias de cada semana antes de redactar."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Jurídicamente preciso.",
        "Claro y verificable.",
        "Argumentativo con criterio propio.",
        "Aplicado a la práctica profesional."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Carpeta de asignatura como entrada canónica.",
        "Portada y metadatos institucionales conservados.",
        "Fuentes provisionales separadas de autoridad académica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 5, bloque 2, obligatoria, 8 créditos.",
        "Asignatura: Etapas del proceso y estrategia del litigio.",
        "Fuente curricular local: malla-curricular-derecho-unadm.pdf.",
        "Coursecode visible en plantilla: LDE-S5B2. [supuesto]"
      ]
    },
    "essence": [
      "Identidad UnADM.",
      "Claridad académica.",
      "Fundamento jurídico verificable.",
      "Problema jurídico o social claro.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeación.",
      "Análisis propio y postura académica.",
      "Conclusión jurídica transferible.",
      "Normalización estructurada.",
      "Unión-dedupe sin regresión."
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
      "Transformar la planeación semanal en reportes, presentaciones y productos visuales.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Formar criterio jurídico aplicado a la estrategia del litigio.",
      "Garantizar memoria editorial persistente y verificable."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Objetivo visible.",
      "Bloques argumentativos ordenados.",
      "Marco normativo o doctrinal explícito.",
      "Citas trazables.",
      "Postura propia sustentada.",
      "Cierre jurídico aplicable.",
      "Supuestos marcados.",
      "Lenguaje académico-jurídico sin relleno.",
      "Metadatos UnADM consistentes."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis propio -> conclusión jurídica.",
      "Afirmación -> evidencia verificable -> interpretación -> implicación práctica.",
      "Consigna -> producto solicitado -> estructura -> rúbrica.",
      "Fuente -> cita -> uso argumentativo -> conclusión.",
      "Dato no visible -> marca [supuesto] -> verificación pendiente.",
      "Regla heredada -> pertinencia local -> adopción conservadora."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Licenciatura en Derecho",
        "Etapas del proceso y estrategia del litigio",
        "Semestre 5 bloque 2",
        "Carpeta canónica de asignatura",
        "Cinco ejes editoriales",
        "Problema jurídico o social",
        "Conceptos jurídicos pertinentes",
        "Normas aplicables",
        "Doctrina verificable",
        "Datos pertinentes al caso",
        "Producto solicitado por la planeación",
        "Análisis propio",
        "Postura académica",
        "Conclusión jurídica transferible",
        "Integridad académica",
        "Citas verificables",
        "Bibliografía local",
        "JSON parseable",
        "Normalización estructurada",
        "Unión-dedupe sin regresión",
        "Fuentes provisionales",
        "Tokens sin resolver",
        "Plantilla LaTeX local",
        "Metadatos institucionales"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Metadatos institucionales",
          "kind": "supports",
          "justification": "La pauta local exige conservar identidad UnADM en portada y metadatos."
        },
        {
          "source": "Licenciatura en Derecho",
          "target": "Etapas del proceso y estrategia del litigio",
          "kind": "develops",
          "justification": "El README ubica la materia dentro de la Licenciatura en Derecho."
        },
        {
          "source": "Semestre 5 bloque 2",
          "target": "Etapas del proceso y estrategia del litigio",
          "kind": "supports",
          "justification": "La ubicación curricular local declara semestre 5 y bloque 2."
        },
        {
          "source": "Carpeta canónica de asignatura",
          "target": "Bibliografía local",
          "kind": "supports",
          "justification": "El README define la carpeta como entrada canónica y lista el .bib local."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Producto solicitado por la planeación",
          "kind": "develops",
          "justification": "El programa analítico incluye el producto solicitado como eje de trabajo."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis necesita partir de un problema delimitado."
        },
        {
          "source": "Normas aplicables",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión debe apoyarse en fundamento jurídico verificable."
        },
        {
          "source": "Doctrina verificable",
          "target": "Postura académica",
          "kind": "supports",
          "justification": "La postura propia debe estar sustentada y no ser solo opinión."
        },
        {
          "source": "Citas verificables",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La pauta editorial exige citas verificables e integridad académica."
        },
        {
          "source": "Bibliografía local",
          "target": "Citas verificables",
          "kind": "supports",
          "justification": "El .bib local registra fuentes institucionales y debe recibir fuentes específicas."
        },
        {
          "source": "JSON parseable",
          "target": "Propagación recursiva segura",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay fusión confiable aguas abajo."
        },
        {
          "source": "Normalización estructurada",
          "target": "JSON parseable",
          "kind": "supports",
          "justification": "La normalización corrige salidas heredadas no estructuradas."
        },
        {
          "source": "Unión-dedupe sin regresión",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Permite compresión lossless sin borrar reglas útiles previas."
        },
        {
          "source": "Fuentes provisionales",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Separar fuentes no verificadas evita tratarlas como autoridad académica."
        },
        {
          "source": "Tokens sin resolver",
          "target": "Compilación LaTeX",
          "kind": "contrasts",
          "justification": "Los tokens en nombres de archivo pueden romper referencias y trazabilidad."
        },
        {
          "source": "Plantilla LaTeX local",
          "target": "Metadatos institucionales",
          "kind": "supports",
          "justification": "La plantilla visible contiene macros de curso, universidad y asignatura."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 5, bloque 2, obligatoria, 8 créditos.",
        "README local: fuente curricular malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: integridad académica, citas verificables y conclusión jurídica con criterio propio.",
        "Programa analítico local: claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: reportes, presentaciones y productos visuales.",
        "Programa analítico local: cinco ejes de trabajo.",
        "Bib local: unadmSitioWeb.",
        "Bib local: unadmMallaDerecho2024.",
        "Plantilla .tex local: documenttitle, documentsubtitle, documentsubject, coursename, coursecode y universityname.",
        "Plantilla .tex local: coursecode LDE-S5B2.",
        "Memoria institucional heredada: salida no JSON parseable requiere normalización.",
        "Memoria origen transversal: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
        "Regla consolidada: no inventar fuentes.",
        "Regla consolidada: validar JSON parseable antes de propagar.",
        "Regla consolidada: aplicar unión-dedupe sin regresión."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin eliminar contenido útil.",
      "Se mantuvieron metadatos locales del destino sobre los del origen.",
      "Se transfirieron solo patrones editoriales estables del origen.",
      "Se excluyeron conceptos y citas específicos de Filosofía del Derecho como autoridad local.",
      "Se reforzó el patrón problema-fundamento-análisis-conclusión.",
      "Se preservó la advertencia sobre salidas no JSON parseables.",
      "Se mantuvo la fuente Codex como provisional y técnica.",
      "Se consolidó el .bib local como repositorio bibliográfico de la materia.",
      "Se reforzó la revisión de tokens sin resolver y caracteres corruptos.",
      "Se actualizó el grafo conceptual con relaciones permitidas y justificadas."
    ]
  }
}