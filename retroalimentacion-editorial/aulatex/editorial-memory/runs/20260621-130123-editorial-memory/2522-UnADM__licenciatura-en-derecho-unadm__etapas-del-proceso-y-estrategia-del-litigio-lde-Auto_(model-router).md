{
  "summary": [
    "Materia destino consolidada con identidad UnADM y enfoque jurídico aplicado.",
    "Ciclo 15 refuerza sincronización transversal conservadora.",
    "Se preserva compresión por unión-dedupe sin pérdida ni regresión.",
    "Se validan como estables los cinco ejes editoriales: problema, conceptos, producto, análisis propio y conclusión.",
    "Se transfieren solo abstracciones editoriales desde Filosofía del Derecho.",
    "No se transfieren fuentes ni redacción literal de actividad no equivalente.",
    "La salida heredada no parseable permanece como antecedente técnico provisional.",
    "El contexto local verificable ubica la materia en semestre 5, bloque 2, obligatoria, 8 créditos.",
    "La carpeta de asignatura es entrada canónica.",
    "La bibliografía local inicia con unadmSitioWeb y unadmMallaDerecho2024."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, tono y metadatos.",
    "Alinear entregables con Licenciatura en Derecho.",
    "Usar contexto curricular local: semestre 5, bloque 2, obligatoria, 8 créditos.",
    "Citar malla-curricular-derecho-unadm.pdf para ubicación curricular.",
    "Usar tono académico-jurídico formal, claro y verificable.",
    "Exigir postura propia sustentada en cada producto.",
    "Conservar trazabilidad editorial en cada consolidación.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Usar macros de portada: documenttitle, coursename, coursecode y universityname.",
    "Usar coursecode LDE-S5B2 mientras no exista corrección institucional. [supuesto]",
    "Mantener documentauthor de plantilla salvo instrucción docente o de actividad. [supuesto]",
    "Marcar como [supuesto] todo dato no visible en consigna o documentos locales.",
    "Registrar fuentes heredadas no verificadas como nota técnica, no como autoridad académica.",
    "Tratar Codex y GPT-Pro heredados como fuentes provisionales hasta verificación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Desarrollar normas, doctrina, datos o conceptos pertinentes al caso.",
    "Alinear estructura al producto pedido en la planeación semanal.",
    "Adaptar salida a reporte, presentación o producto visual según consigna.",
    "Incluir análisis propio antes del cierre.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener README como entrada canónica de estructura.",
    "Usar programa analítico como guía de ejes editoriales.",
    "Aplicar cinco ejes: problema, conceptos, producto solicitado, análisis propio y conclusión."
  ],
  "activity_rules": [
    "Verificar instrucción específica de cada actividad antes de redactar.",
    "Confirmar producto exacto solicitado antes de elegir plantilla.",
    "Rubricar cada entrega contra los ejes del programa analítico.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Integrar evidencia trazable en el cuerpo del trabajo.",
    "Agregar fuentes específicas de actividad al .bib local antes de versión final.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Enfocar el análisis en proceso, estrategia y práctica litigiosa cuando la consigna lo exija.",
    "No reutilizar reglas laterales sin comprobar pertinencia jurídica local.",
    "No asumir que fuentes de otra materia o semana aplican a la actividad local."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de fusionar memoria.",
    "Revisar respuestas no estructuradas antes de aplicarlas aguas abajo.",
    "Aplicar unión-dedupe sin eliminar reglas útiles previas.",
    "Confirmar ausencia de contradicciones con reglas institucionales heredadas.",
    "Comprobar que cada afirmación factual tenga fuente o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que el producto corresponda a la consigna de actividad.",
    "Revisar consistencia entre metadatos de materia y contenido entregado.",
    "Validar que nombres de archivos en README no contengan variables sin resolver.",
    "Corregir caracteres corruptos en README y rutas antes de publicar.",
    "No propagar fuentes provisionales como autoridad académica.",
    "Compilar entregables sin errores críticos ni referencias rotas."
  ],
  "latex_rules": [
    "Usar plantilla .tex local de la materia como base.",
    "Usar reporte-etapas-del-proceso-y-estrategia-del-litigio.tex para reportes.",
    "Usar presentacion-etapas-del-proceso-y-estrategia-del-litigio.tex para presentaciones si existe. [supuesto]",
    "Conservar documentclass article con opciones spanish, letterpaper y oneside.",
    "Conservar macros institucionales de curso, universidad y asignatura.",
    "No eliminar campos de portada; completar faltantes según actividad.",
    "Conservar bloque authortable de la plantilla al adaptar portada.",
    "Mantener compatibilidad con español y acentos correctos.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "No confiar en nombres generados con variables sin resolver.",
    "Resolver tokens tipo $(@{...}.Slug) antes de compilar.",
    "Corregir caracteres anómalos en rutas o nombres de archivo.",
    "Verificar nombres reales de archivos del README antes de referenciarlos.",
    "Compilar sin errores críticos y sin referencias rotas."
  ],
  "bibliography_rules": [
    "Usar etapas-del-proceso-y-estrategia-del-litigio.bib como repositorio local.",
    "Conservar claves BibTeX unadmSitioWeb y unadmMallaDerecho2024.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Agregar entradas BibTeX específicas de actividad antes de citar.",
    "Registrar solo fuentes realmente consultadas.",
    "No inventar referencias.",
    "No citar bibliografía base si no fue usada en el argumento.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Incluir fecha de consulta en fuentes web o institucionales dinámicas.",
    "Validar correspondencia entre citas en texto y entradas .bib.",
    "No transferir citas de Filosofía del Derecho sin consulta local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar arriba y laterales reglas de JSON parseable y no regresión.",
    "Propagar unión-dedupe como estrategia de compresión sin pérdida.",
    "Propagar a materias de Derecho los ejes: problema, fundamento, análisis propio y conclusión jurídica.",
    "Propagar solo abstracciones editoriales entre nodos no equivalentes.",
    "No propagar metadatos específicos de esta materia a otros nodos.",
    "No propagar redacción literal de actividades.",
    "No propagar fuentes locales como obligatorias para materias distintas.",
    "Mantener fuentes provisionales como notas técnicas.",
    "Normalizar manualmente memorias heredadas no parseables antes de reutilizarlas.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Crear cerebro editorial mínimo cuando el destino no tenga contexto local."
  ],
  "open_questions": [
    "Confirmar consigna textual de cada actividad local.",
    "Confirmar producto exacto solicitado por actividad.",
    "Confirmar rúbrica de evaluación específica.",
    "Confirmar estilo de citación jurídica requerido: APA, Chicago, ISO 690 u otro.",
    "Confirmar si documentauthor es fijo de plantilla o variable por estudiante.",
    "Confirmar código de curso LDE-S5B2 con fuente institucional. [supuesto]",
    "Confirmar existencia operativa de presentacion-etapas-del-proceso-y-estrategia-del-litigio.tex. [supuesto]",
    "Corregir nombres corruptos en README y validar nombres reales de archivos. [supuesto]",
    "Confirmar si la fuente provisional Codex debe conservarse solo como nota técnica.",
    "Definir checklist mínimo por tipo de producto: reporte, presentación y material visual.",
    "Confirmar fuentes obligatorias de cada semana.",
    "Confirmar si cada actividad requiere .bib propio o solo .bib de asignatura."
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
        "Carpeta de asignatura como entrada canónica.",
        "Portada y metadatos institucionales conservados.",
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
      "Enfoque jurídico aplicado.",
      "Problema jurídico o social claro.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por planeación.",
      "Análisis propio y postura académica.",
      "Conclusión jurídica transferible.",
      "Evidencia verificable.",
      "Normalización estructurada.",
      "Unión-dedupe sin regresión."
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
      "Transformar planeación semanal en reportes, presentaciones o productos visuales.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Formar criterio jurídico aplicable a la práctica profesional.",
      "Asegurar memoria editorial persistente sin pérdida de reglas útiles."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Objetivo explícito.",
      "Bloques argumentativos visibles.",
      "Marco normativo o doctrinal verificable.",
      "Citas trazables.",
      "Postura propia sustentada.",
      "Cierre jurídico aplicable.",
      "Supuestos marcados.",
      "Metadatos UnADM completos.",
      "Redacción sin relleno descriptivo."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis propio -> conclusión jurídica.",
      "Afirmación -> evidencia verificable -> interpretación -> implicación práctica.",
      "Consigna -> producto -> estructura -> rúbrica -> entrega.",
      "Hecho o caso -> norma aplicable -> razonamiento jurídico -> consecuencia.",
      "Fuente institucional -> ubicación curricular -> identidad editorial.",
      "Dato no visible -> marca de supuesto -> verificación pendiente.",
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
        "Cinco ejes editoriales",
        "Problema jurídico o social",
        "Conceptos jurídicos pertinentes",
        "Marco normativo o doctrinal",
        "Producto solicitado por planeación",
        "Análisis propio",
        "Postura académica",
        "Conclusión jurídica transferible",
        "Práctica profesional",
        "Evidencia verificable",
        "Citas trazables",
        "Bibliografía local",
        "JSON parseable",
        "Normalización estructurada",
        "Unión-dedupe sin regresión",
        "Fuentes provisionales",
        "Tokens sin resolver",
        "Caracteres corruptos en README"
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
          "justification": "La pauta local exige conservar identidad UnADM en cada actividad."
        },
        {
          "source": "Malla curricular de Derecho",
          "target": "Semestre 5 bloque 2",
          "kind": "supports",
          "justification": "El README local declara la ubicación curricular con fuente institucional."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Estructura de entrega",
          "kind": "develops",
          "justification": "El programa analítico organiza los productos por problema, conceptos, producto, análisis y conclusión."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "El encuadre del problema activa la argumentación del estudiante."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión requiere fundamento jurídico para ser aplicable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Las afirmaciones deben tener fuente o marca de supuesto."
        },
        {
          "source": "Bibliografía local",
          "target": "Citas trazables",
          "kind": "supports",
          "justification": "El .bib de la asignatura concentra las fuentes consultadas."
        },
        {
          "source": "JSON parseable",
          "target": "Propagación recursiva segura",
          "kind": "depends_on",
          "justification": "La fusión confiable de memoria requiere estructura validable."
        },
        {
          "source": "Normalización estructurada",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Las salidas heredadas no estructuradas deben revisarse antes de reutilizarse."
        },
        {
          "source": "Unión-dedupe sin regresión",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "La compresión conserva reglas útiles y elimina duplicados."
        },
        {
          "source": "Fuentes provisionales",
          "target": "Autoridad académica",
          "kind": "contrasts",
          "justification": "Las fuentes heredadas no verificadas no deben tratarse como bibliografía académica."
        },
        {
          "source": "Tokens sin resolver",
          "target": "Compilación LaTeX",
          "kind": "contrasts",
          "justification": "Los nombres con variables sin resolver pueden romper referencias y rutas."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 5, bloque 2, obligatoria, 8 créditos.",
        "README local: fuente curricular UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: integridad académica, citas verificables y conclusión jurídica con criterio propio.",
        "Programa analítico local: claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: reportes, presentaciones y productos visuales.",
        "Programa analítico local: cinco ejes de trabajo.",
        "Bib local: unadmSitioWeb.",
        "Bib local: unadmMallaDerecho2024.",
        "Plantilla local: documentclass article con spanish, letterpaper y oneside.",
        "Plantilla local: macros documenttitle, coursename, coursecode y universityname.",
        "Plantilla local: coursecode LDE-S5B2.",
        "README local: token $(@{...}.Slug) pendiente de resolver.",
        "README local: posibles caracteres corruptos en nombres de archivos."
      ]
    },
    "reinforcement_log": [
      "Ciclo 15 conserva reglas útiles previas sin regresión.",
      "Se deduplican reglas repetidas de identidad, estructura y calidad.",
      "Se refuerza transferencia transversal por abstracciones estables.",
      "Se evita importar citas y conceptos específicos de Filosofía del Derecho.",
      "Se mantiene contexto local de semestre 5, bloque 2, obligatoria, 8 créditos.",
      "Se conserva advertencia de JSON parseable antes de propagación.",
      "Se conserva advertencia de normalización manual para salidas no estructuradas.",
      "Se refuerza separación entre fuentes provisionales y autoridad académica.",
      "Se refuerza control de tokens sin resolver en README y bibliografía.",
      "Se refuerza conclusión jurídica con criterio propio como sello de la materia."
    ]
  }
}