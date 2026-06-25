{
  "summary": [
    "Materia consolidada con identidad UnADM y enfoque jurídico aplicado.",
    "Ciclo 7 sincroniza abstracciones transversales sin copiar redacción literal del origen.",
    "Se preserva compresión por unión-dedupe sin pérdida y sin regresión.",
    "Se mantiene validación JSON parseable antes de cualquier propagación.",
    "Se refuerzan cinco ejes editoriales: problema, conceptos, producto, análisis propio y conclusión transferible.",
    "Se conserva trazabilidad de fuentes provisionales sin tratarlas como autoridad académica.",
    "El destino usa contexto local verificable: semestre 5, bloque 2, obligatoria, 8 créditos.",
    "La carpeta de asignatura permanece como entrada canónica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 2, obligatoria, 8 créditos.",
    "Usar tono académico-jurídico formal con postura propia sustentada.",
    "Conservar trazabilidad de origen editorial al consolidar memoria.",
    "Usar macros de portada: documenttitle, coursename, coursecode y universityname.",
    "Usar coursecode LDE-S5B2 mientras no exista corrección institucional. [supuesto]",
    "Mantener autor de plantilla Martin Jonathan de la Cruz salvo instrucción de actividad o docente. [supuesto]",
    "Registrar fuentes provisionales como nota técnica y no como autoridad académica.",
    "Marcar como [supuesto] todo dato no visible en consigna o documentos locales.",
    "Usar la carpeta de asignatura como punto de entrada canónico."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Desarrollar conceptos, normas, doctrina o datos pertinentes al caso.",
    "Alinear la estructura al producto solicitado por la planeación semanal.",
    "Adaptar salida al producto pedido: reporte, presentación o visual.",
    "Usar el programa analítico como guía de ejes editoriales.",
    "Seguir cinco ejes: problema, conceptos, producto solicitado, análisis propio y conclusión transferible.",
    "Incluir análisis propio antes del cierre.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener README como entrada canónica de la asignatura."
  ],
  "activity_rules": [
    "Verificar instrucción específica de cada actividad antes de redactar.",
    "Rubricar cada entrega contra los ejes del programa analítico.",
    "Exigir conclusión jurídica con criterio propio en cada entrega.",
    "Integrar evidencia verificable y citas trazables en el cuerpo del trabajo.",
    "Agregar fuentes específicas de actividad al .bib local antes de la versión final.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No reutilizar reglas laterales sin comprobar pertinencia jurídica.",
    "No asumir que fuentes de otra asignatura corresponden a una actividad local."
  ],
  "quality_gates": [
    "Validar JSON parseable en toda memoria antes de aplicar propagación.",
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de fusionar memoria.",
    "Comprobar unión-dedupe sin eliminar reglas útiles previas.",
    "Confirmar ausencia de contradicciones con reglas heredadas de institución.",
    "Revisar consistencia entre metadatos de materia y contenido entregado.",
    "Comprobar que cada afirmación factual tenga fuente o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar respuestas no estructuradas antes de aplicarlas aguas abajo.",
    "Normalizar manualmente memorias heredadas cuando provengan de salida no parseable.",
    "Revisar caracteres corruptos en README y plantilla antes de publicar. [supuesto]",
    "Validar que nombres de archivos en README no contengan variables sin resolver."
  ],
  "latex_rules": [
    "Usar la plantilla .tex local de la materia como base de nuevas actividades.",
    "Usar reporte-etapas-del-proceso-y-estrategia-del-litigio.tex para reportes.",
    "Usar presentacion-etapas-del-proceso-y-estrategia-del-litigio.tex para presentaciones si existe en carpeta. [supuesto]",
    "Conservar macros institucionales de curso, universidad y asignatura.",
    "Usar documentclass article con opciones spanish, letterpaper y oneside.",
    "Mantener compatibilidad con español y formato letterpaper definido en plantilla.",
    "No eliminar campos de portada; completar faltantes según actividad.",
    "Conservar bloque authortable de la plantilla al adaptar portada.",
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar compilaciones rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "No confiar en nombres generados con variables sin resolver en README o markdown."
  ],
  "bibliography_rules": [
    "Usar etapas-del-proceso-y-estrategia-del-litigio.bib como repositorio local.",
    "Conservar fuentes institucionales ya registradas: sitio UnADM y malla curricular Derecho.",
    "Conservar claves BibTeX unadmSitioWeb y unadmMallaDerecho2024.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Agregar entradas BibTeX específicas de actividad antes de citar.",
    "Registrar fuentes específicas de actividad en el .bib de la asignatura.",
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "No citar bibliografía base si no fue usada en el argumento.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Incluir fecha de consulta cuando la fuente sea web o institucional dinámica.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo después de validar JSON y estructura.",
    "Propagar reglas de validación JSON y control de no regresión.",
    "Propagar la regla de unión-dedupe sin regresión.",
    "Propagar a materias vecinas de Derecho los cinco ejes editoriales.",
    "Propagar la restricción de no inventar fuentes.",
    "Propagar solo abstracciones editoriales entre nodos no equivalentes.",
    "No propagar metadatos específicos de esta materia a nodos vecinos.",
    "Mantener especificidad local al recibir reglas institucionales.",
    "Aplicar normalización manual si se detecta salida no estructurada.",
    "Ciclo 1 necesita normalización manual si se reutiliza.",
    "Ciclo 7 refuerza transferencia transversal conservadora."
  ],
  "open_questions": [
    "Confirmar si el nombre de autor en plantilla es definitivo o variable por estudiante.",
    "Confirmar estilo de citación jurídica requerido: APA, Chicago, ISO 690 u otro.",
    "Corregir nombres corruptos en README y validar nombres reales de archivos. [supuesto]",
    "Confirmar existencia operativa de presentacion-etapas-del-proceso-y-estrategia-del-litigio.tex. [supuesto]",
    "Confirmar si la fuente provisional Codex debe conservarse solo como nota técnica.",
    "Confirmar código de curso correcto: README no lo declara pero plantilla usa LDE-S5B2. [supuesto]",
    "Definir checklist mínimo por tipo de producto: reporte, presentación y material visual.",
    "Confirmar consigna textual de cada actividad antes de especializar memoria.",
    "Confirmar rúbrica de evaluación específica por actividad.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Verificar integridad completa de la plantilla .tex local antes de compilar. [supuesto]"
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
        "Portada y metadatos institucionales conservados.",
        "Integridad académica con citas verificables.",
        "Carpeta de asignatura como entrada canónica.",
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
      "Cinco ejes editoriales.",
      "Problema jurídico o social claro.",
      "Fundamento conceptual, normativo o doctrinal.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible.",
      "Normalización estructurada.",
      "Unión-dedupe sin regresión."
    ],
    "reason_for_being": [
      "Transformar la planeación semanal en productos académicos jurídicos.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Orientar reportes, presentaciones y productos visuales con claridad institucional.",
      "Conectar teoría jurídica, estrategia procesal y práctica profesional.",
      "Garantizar memoria editorial persistente sin pérdida de reglas útiles."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Objetivo puntual visible.",
      "Bloques argumentativos claros.",
      "Citas trazables.",
      "Marco normativo o doctrinal explícito.",
      "Postura propia sustentada.",
      "Lenguaje jurídico sobrio.",
      "Cierre jurídico aplicable.",
      "Supuestos marcados.",
      "Sin redacción literal transferida entre nodos no equivalentes."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual y normativo -> análisis propio -> conclusión jurídica.",
      "Afirmación -> evidencia verificable -> interpretación -> implicación práctica.",
      "Hecho relevante -> regla aplicable -> razonamiento jurídico -> consecuencia procesal.",
      "Concepto jurídico -> fuente doctrinal o normativa -> aplicación al caso.",
      "Consigna -> producto solicitado -> criterios de evaluación -> entrega final.",
      "Duda factual -> marca de supuesto -> verificación pendiente.",
      "Fuente heredada -> estado provisional -> confirmación local antes de uso académico."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Licenciatura en Derecho",
        "Etapas del proceso",
        "Estrategia del litigio",
        "Problema jurídico o social",
        "Marco normativo",
        "Marco doctrinal",
        "Argumentación jurídica",
        "Interpretación jurídica",
        "Evidencia verificable",
        "Análisis propio",
        "Postura académica",
        "Conclusión jurídica transferible",
        "Producto solicitado",
        "Planeación semanal",
        "Integridad académica",
        "Bibliografía local",
        "JSON parseable",
        "Normalización estructurada",
        "Unión-dedupe sin regresión"
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
          "justification": "La pauta local exige conservar identidad institucional, citas verificables y criterio propio."
        },
        {
          "source": "Malla curricular Derecho",
          "target": "Ubicación curricular",
          "kind": "supports",
          "justification": "El README local registra semestre 5, bloque 2, tipo obligatoria y 8 créditos."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Estructura de entrega",
          "kind": "develops",
          "justification": "El programa analítico organiza productos por problema, conceptos, producto, análisis y conclusión."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Marco normativo",
          "kind": "depends_on",
          "justification": "El marco debe responder al problema planteado y no operar como resumen aislado."
        },
        {
          "source": "Marco normativo",
          "target": "Análisis propio",
          "kind": "supports",
          "justification": "La interpretación del caso requiere reglas, doctrina o datos pertinentes."
        },
        {
          "source": "Argumentación jurídica",
          "target": "Conclusión jurídica transferible",
          "kind": "develops",
          "justification": "El cierre debe derivar de razones verificables y aplicables a la práctica profesional."
        },
        {
          "source": "Interpretación jurídica",
          "target": "Estrategia del litigio",
          "kind": "supports",
          "justification": "La estrategia procesal requiere comprender normas, hechos y consecuencias jurídicas."
        },
        {
          "source": "Evidencia verificable",
          "target": "Postura académica",
          "kind": "supports",
          "justification": "La postura propia debe estar sustentada y no ser opinión sin respaldo."
        },
        {
          "source": "Bibliografía local",
          "target": "Citas trazables",
          "kind": "supports",
          "justification": "El .bib local conserva fuentes institucionales y entradas específicas de actividad."
        },
        {
          "source": "JSON parseable",
          "target": "Propagación recursiva segura",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay fusión confiable de memoria editorial."
        },
        {
          "source": "Normalización estructurada",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Permite reutilizar reglas sin arrastrar salidas no estructuradas."
        },
        {
          "source": "Unión-dedupe sin regresión",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Comprime reglas repetidas sin eliminar reglas útiles previas."
        },
        {
          "source": "Fuente provisional",
          "target": "Autoridad académica",
          "kind": "contrasts",
          "justification": "Las fuentes heredadas no verificadas se registran como nota técnica y no como respaldo académico."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 5, bloque 2, obligatoria, 8 créditos.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: identidad UnADM, integridad académica, citas verificables y conclusión jurídica con criterio propio.",
        "Programa analítico local: propósito de transformar planeación semanal en reportes, presentaciones y productos visuales.",
        "Programa analítico local: cinco ejes de trabajo editorial.",
        "Bib local: unadmSitioWeb.",
        "Bib local: unadmMallaDerecho2024.",
        "Plantilla .tex local: macros documenttitle, coursename, coursecode y universityname.",
        "Plantilla .tex local: coursecode LDE-S5B2.",
        "Memoria heredada institucional: salida no parseable requiere normalización.",
        "Memoria de origen: validación JSON y estructura antes de propagar.",
        "Memoria de origen: no inventar fuentes y marcar supuestos.",
        "Memoria de origen: problema, conceptos, evidencia, análisis propio y conclusión jurídica."
      ]
    },
    "reinforcement_log": [
      "Ciclo 7 conserva reglas útiles del destino y elimina duplicados semánticos.",
      "Ciclo 7 incorpora solo abstracciones transversales del origen.",
      "Ciclo 7 evita trasladar citas específicas de Filosofía del Derecho como bibliografía local.",
      "Ciclo 7 refuerza interpretación y argumentación jurídica como conceptos transversales.",
      "Ciclo 7 mantiene fuentes locales verificadas: unadmSitioWeb y unadmMallaDerecho2024.",
      "Ciclo 7 conserva advertencia sobre salidas no JSON parseable.",
      "Ciclo 7 refuerza revisión de tokens sin expandir en README y programa analítico.",
      "Ciclo 7 preserva metadatos curriculares locales de la materia destino.",
      "Ciclo 7 mantiene fuentes provisionales fuera de autoridad académica.",
      "Ciclo 7 consolida el ADN editorial como cerebro persistente de materia."
    ]
  }
}