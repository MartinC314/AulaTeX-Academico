{
  "summary": [
    "Materia destino consolidada con identidad UnADM y enfoque jurídico aplicado.",
    "Sincronización transversal aplicada con abstracciones estables, no redacción literal de actividad.",
    "Se conserva compresión por unión-dedupe sin pérdida y sin regresión.",
    "Se mantiene validación JSON parseable antes de cualquier propagación.",
    "Se refuerzan cinco ejes editoriales: problema, conceptos, producto, análisis propio y conclusión.",
    "Se preserva contexto local verificable: Licenciatura en Derecho, semestre 5, bloque 2, obligatoria, 8 créditos.",
    "Se mantienen fuentes heredadas no verificadas como provisionales y fuera de autoridad académica.",
    "Se excluyen fuentes filosóficas específicas del origen por no ser equivalentes al destino."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, tono y metadatos.",
    "Alinear entregables con Licenciatura en Derecho.",
    "Usar ubicación curricular local: semestre 5, bloque 2, obligatoria, 8 créditos.",
    "Citar malla-curricular-derecho-unadm.pdf como fuente curricular local.",
    "Usar tono académico-jurídico formal con postura propia sustentada.",
    "Conservar trazabilidad de origen editorial en cada consolidación.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Usar macros de portada: documenttitle, coursename, coursecode, universityname.",
    "Usar coursecode LDE-S5B2 mientras no exista corrección institucional. [supuesto]",
    "Mantener autor de plantilla Martin Jonathan de la Cruz salvo instrucción contraria. [supuesto]",
    "Marcar como [supuesto] todo dato no visible en consigna o documentos locales.",
    "Registrar fuentes provisionales como nota técnica, no como autoridad académica."
  ],
  "structure_rules": [
    "Partir de un problema jurídico o social claro.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
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
    "Rubricar cada entrega contra los ejes del programa analítico.",
    "Exigir conclusión jurídica con criterio propio en cada entrega.",
    "Integrar evidencia verificable y citas trazables en el cuerpo del trabajo.",
    "Agregar fuentes específicas de actividad al .bib local antes de la versión final.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No reutilizar reglas laterales sin comprobar pertinencia jurídica.",
    "No asumir que fuentes de otra asignatura corresponden a esta materia.",
    "Distinguir pauta general de consigna local de actividad."
  ],
  "quality_gates": [
    "Validar JSON parseable en toda memoria antes de aplicar propagación.",
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de fusionar memoria.",
    "Comprobar unión-dedupe sin eliminar reglas útiles previas.",
    "Confirmar ausencia de contradicciones con reglas heredadas de institución.",
    "Revisar respuestas no estructuradas antes de aplicarlas aguas abajo.",
    "Normalizar manualmente memorias del ciclo 1 si provienen de salida no parseable.",
    "Revisar consistencia entre metadatos de materia y contenido entregado.",
    "Comprobar que cada afirmación factual tenga fuente o marca de supuesto.",
    "Validar correspondencia entre citas en texto y archivo .bib.",
    "Confirmar que el producto corresponda a la consigna de actividad.",
    "Revisar caracteres corruptos en README y plantilla antes de publicar. [supuesto]",
    "Validar que nombres de archivos no contengan variables sin resolver.",
    "Compilar sin errores críticos y sin referencias rotas."
  ],
  "latex_rules": [
    "Usar la plantilla .tex local como base de nuevas actividades.",
    "Usar reporte-etapas-del-proceso-y-estrategia-del-litigio.tex para reportes.",
    "Usar presentacion-etapas-del-proceso-y-estrategia-del-litigio.tex para presentaciones si existe en carpeta. [supuesto]",
    "Conservar macros institucionales de curso, universidad y asignatura.",
    "No eliminar campos de portada; completar faltantes según actividad.",
    "Usar documentclass article con opciones spanish, letterpaper, oneside.",
    "Mantener compatibilidad con español y acentos correctos.",
    "Conservar bloque authortable de la plantilla al adaptar portada.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "No confiar en nombres generados con variables sin resolver en README o markdown.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) antes de compilar.",
    "Corregir caracteres anómalos en rutas o nombres antes de referenciarlos.",
    "Verificar nombres de archivos del README contra archivos reales."
  ],
  "bibliography_rules": [
    "Usar etapas-del-proceso-y-estrategia-del-litigio.bib como repositorio local.",
    "Conservar fuentes institucionales ya registradas: sitio UnADM y malla curricular Derecho.",
    "Conservar claves BibTeX unadmSitioWeb y unadmMallaDerecho2024.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "No inventar referencias.",
    "Registrar solo fuentes consultadas y verificables.",
    "Agregar entradas BibTeX específicas de actividad antes de citar.",
    "No citar bibliografía base si no fue usada en el argumento.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Incluir fecha de consulta cuando la fuente sea web o institucional dinámica.",
    "Validar consistencia entre cita textual, clave BibTeX y entrada .bib."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar arriba y laterales reglas de validación JSON y no regresión.",
    "Propagar unión-dedupe sin pérdida como regla institucional.",
    "Propagar a materias vecinas de Derecho los cinco ejes editoriales.",
    "Propagar solo abstracciones generales entre nodos no equivalentes.",
    "No propagar metadatos específicos de esta materia a otras materias.",
    "No propagar fuentes específicas de una asignatura como autoridad transversal.",
    "Mantener contexto local del destino sobre reglas laterales.",
    "Propagar la restricción de no inventar fuentes.",
    "Propagar advertencia de normalización manual para ciclo 1.",
    "Aplicar normalización manual si se detecta salida heredada no estructurada.",
    "Evitar regresiones respecto de reglas útiles previas."
  ],
  "open_questions": [
    "Confirmar si el nombre de autor en plantilla es definitivo o variable por estudiante.",
    "Confirmar estilo de citación jurídica requerido: APA, Chicago, ISO 690 u otro.",
    "Corregir nombres corruptos en README y validar nombres reales de archivos. [supuesto]",
    "Confirmar existencia operativa de presentacion-etapas-del-proceso-y-estrategia-del-litigio.tex. [supuesto]",
    "Confirmar si la fuente provisional Codex debe conservarse solo como nota técnica.",
    "Confirmar código de curso correcto: README no lo declara y plantilla usa LDE-S5B2. [supuesto]",
    "Definir checklist mínimo por tipo de producto: reporte, presentación y material visual.",
    "Confirmar rúbricas específicas por actividad antes de ajustar profundidad argumentativa.",
    "Confirmar fuentes obligatorias de cada semana o unidad.",
    "Confirmar si el token Slug del README debe resolverse siempre como etapas-del-proceso-y-estrategia-del-litigio.bib."
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
        "Fuentes provisionales separadas de autoridad académica.",
        "Trazabilidad editorial en consolidaciones."
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
      "Identidad UnADM.",
      "Enfoque jurídico aplicado.",
      "Cinco ejes editoriales.",
      "Problema jurídico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeación.",
      "Análisis propio y postura académica.",
      "Conclusión transferible a la práctica jurídica.",
      "Normalización estructurada.",
      "Unión-dedupe sin regresión.",
      "Citas verificables.",
      "Metadatos locales preservados."
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
      "Transformar la planeación semanal en reportes, presentaciones y productos visuales.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Convertir la materia en cerebro editorial persistente para actividades futuras.",
      "Evitar productos meramente descriptivos.",
      "Garantizar trazabilidad de fuentes y reglas."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Objetivo puntual explícito.",
      "Bloques argumentativos visibles.",
      "Marco normativo o doctrinal separado.",
      "Citas trazables.",
      "Postura propia sustentada.",
      "Cierre jurídico aplicable.",
      "Supuestos marcados.",
      "Metadatos institucionales consistentes.",
      "Redacción sin trasplantes literales entre materias."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis propio -> conclusión jurídica.",
      "Afirmación -> evidencia verificable -> interpretación -> implicación práctica.",
      "Consigna -> producto solicitado -> estructura -> criterios de evaluación.",
      "Fuente institucional -> ubicación curricular -> metadatos de portada.",
      "Norma o doctrina -> aplicación al caso -> postura del estudiante.",
      "Dato no visible -> marca de supuesto -> confirmación pendiente.",
      "Memoria heredada -> validación JSON -> dedupe -> propagación segura."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Licenciatura en Derecho",
        "Etapas del proceso y estrategia del litigio",
        "Semestre 5 bloque 2",
        "Asignatura obligatoria de 8 créditos",
        "Cinco ejes editoriales",
        "Problema jurídico o social",
        "Marco normativo o doctrinal",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "Producto solicitado por la planeación",
        "Integridad académica",
        "Citas verificables",
        "Archivo .bib local",
        "JSON parseable",
        "Normalización estructurada",
        "Unión-dedupe sin regresión",
        "Fuentes provisionales",
        "Tokens sin resolver",
        "Compilación LaTeX estable"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La pauta local exige identidad institucional, citas verificables y conclusión con criterio propio."
        },
        {
          "source": "Malla curricular de Derecho",
          "target": "Semestre 5 bloque 2",
          "kind": "supports",
          "justification": "El README local declara ubicación curricular y fuente institucional."
        },
        {
          "source": "Programa analítico",
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
          "source": "Problema jurídico o social",
          "target": "Marco normativo o doctrinal",
          "kind": "depends_on",
          "justification": "El marco debe responder al problema planteado."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión debe derivar del razonamiento del estudiante."
        },
        {
          "source": "Citas verificables",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Las afirmaciones jurídicas requieren respaldo documental o marca de supuesto."
        },
        {
          "source": "Archivo .bib local",
          "target": "Citas verificables",
          "kind": "supports",
          "justification": "El repositorio BibTeX local conserva fuentes institucionales y específicas."
        },
        {
          "source": "JSON parseable",
          "target": "Propagación recursiva segura",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay fusión confiable aguas abajo."
        },
        {
          "source": "Unión-dedupe sin regresión",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Permite compresión lossless sin borrar reglas útiles previas."
        },
        {
          "source": "Tokens sin resolver",
          "target": "Compilación LaTeX estable",
          "kind": "contrasts",
          "justification": "Los tokens en nombres de archivo rompen referencias y deben resolverse."
        },
        {
          "source": "Fuentes provisionales",
          "target": "Autoridad académica",
          "kind": "contrasts",
          "justification": "Las fuentes heredadas no verificadas no deben sustentar argumentos académicos."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 5, bloque 2, obligatoria, 8 créditos.",
        "README local: fuente curricular UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: exige identidad UnADM, integridad académica, citas verificables y conclusión jurídica.",
        "Programa analítico local: productos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: planeación transformada en reportes, presentaciones y productos visuales.",
        "Programa analítico local: cinco ejes de trabajo.",
        "Bib local: unadmSitioWeb.",
        "Bib local: unadmMallaDerecho2024.",
        "Plantilla .tex local: macros documenttitle, coursename, coursecode y universityname.",
        "Plantilla .tex local: coursecode LDE-S5B2.",
        "Contexto heredado: salida previa no JSON parseable requiere normalización.",
        "Transferencia transversal: compartir abstracciones estables entre nodos no equivalentes."
      ]
    },
    "reinforcement_log": [
      "Ciclo 20 consolida memoria destino por unión-dedupe.",
      "Se preservan reglas locales de identidad, estructura, calidad, LaTeX y bibliografía.",
      "Se incorporan solo abstracciones estables desde Filosofía del Derecho.",
      "Se evita transferir bibliografía filosófica específica al destino.",
      "Se refuerza validación JSON como puerta de propagación recursiva.",
      "Se refuerza revisión de citas contra .bib local.",
      "Se refuerza resolución de tokens Slug en README y programa analítico.",
      "Se conserva advertencia sobre fuentes provisionales heredadas.",
      "Se mantiene prioridad de consigna local sobre reglas laterales.",
      "Se fija patrón argumentativo: problema, fundamento, análisis propio y cierre jurídico."
    ]
  }
}