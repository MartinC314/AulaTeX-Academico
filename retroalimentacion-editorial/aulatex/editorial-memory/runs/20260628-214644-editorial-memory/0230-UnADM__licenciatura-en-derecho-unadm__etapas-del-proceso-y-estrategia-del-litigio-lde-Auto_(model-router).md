{
  "summary": [
    "Materia destino consolidada con identidad UnADM y enfoque jurídico aplicado.",
    "Ciclo 2 completado con compresión por unión-dedupe sin pérdida.",
    "Se preservan reglas estables: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se mantiene validación JSON parseable antes de cualquier propagación.",
    "La herencia no estructurada previa queda como nota técnica provisional.",
    "El destino conserva cerebro editorial mínimo reconstruible y vacíos locales abiertos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho.",
    "Usar ubicación curricular local: semestre 5, bloque 2, obligatoria, 8 créditos.",
    "Citar malla-curricular-derecho-unadm.pdf como fuente de ubicación curricular.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Usar tono académico-jurídico formal con postura propia sustentada.",
    "Conservar trazabilidad de origen editorial al consolidar memoria.",
    "Marcar como [supuesto] todo dato no visible en consigna o documento local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Registrar fuentes provisionales como nota técnica, no como autoridad académica.",
    "Usar macros de portada: documenttitle, coursename, coursecode y universityname.",
    "Usar coursecode LDE-S5B2 mientras no exista corrección institucional. [supuesto]",
    "Mantener autor de plantilla Martin Jonathan de la Cruz salvo instrucción contraria. [supuesto]"
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Desarrollar conceptos, normas, doctrina o datos pertinentes al caso.",
    "Adaptar la salida al producto pedido: reporte, presentación o producto visual.",
    "Alinear la entrega con la planeación semanal y la consigna local.",
    "Usar el programa analítico como guía de ejes editoriales.",
    "Seguir cinco ejes: problema, conceptos, producto solicitado, análisis propio y conclusión transferible.",
    "Incluir análisis propio antes del cierre.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener README como entrada canónica de la asignatura."
  ],
  "activity_rules": [
    "Verificar la instrucción específica de cada actividad antes de redactar.",
    "Confirmar producto exacto solicitado por la consigna.",
    "Rubricar cada entrega contra los ejes del programa analítico.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Integrar evidencia trazable en el cuerpo del trabajo.",
    "Incluir postura argumentada del estudiante, no solo resumen descriptivo.",
    "Evitar entregas solo descriptivas.",
    "Exigir conclusión jurídica con criterio propio en cada entrega.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Agregar fuentes específicas de actividad al .bib local antes de la versión final.",
    "No reutilizar reglas laterales sin comprobar pertinencia jurídica.",
    "No asumir que fuentes de otra actividad corresponden a la actividad actual."
  ],
  "quality_gates": [
    "Bloquear propagación si la memoria no es JSON parseable.",
    "Validar JSON parseable en toda memoria antes de fusionar.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar respuestas no estructuradas antes de reutilizarlas.",
    "Normalizar manualmente herencias no parseables antes de consolidar.",
    "Comprobar unión-dedupe sin eliminar reglas útiles previas.",
    "Confirmar ausencia de contradicciones con reglas heredadas de institución.",
    "Revisar consistencia entre metadatos de materia y contenido entregado.",
    "Confirmar que toda afirmación factual tenga fuente o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que el producto corresponda a la consigna local.",
    "Revisar caracteres corruptos en README y plantilla antes de publicar. [supuesto]",
    "Validar que nombres de archivos no contengan variables sin resolver."
  ],
  "latex_rules": [
    "Usar la plantilla .tex local de la materia como base de nuevas actividades.",
    "Usar reporte-etapas-del-proceso-y-estrategia-del-litigio.tex para reportes.",
    "Usar presentacion-etapas-del-proceso-y-estrategia-del-litigio.tex para presentaciones si existe. [supuesto]",
    "Conservar macros institucionales de curso, universidad y asignatura.",
    "No eliminar campos de portada; completar faltantes según actividad.",
    "Usar documentclass article con opciones spanish, letterpaper y oneside.",
    "Mantener compatibilidad con español y acentos correctos en .tex y .bib.",
    "Conservar bloque authortable de la plantilla al adaptar portada.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "No confiar en nombres generados con variables sin resolver en README o markdown."
  ],
  "bibliography_rules": [
    "Usar etapas-del-proceso-y-estrategia-del-litigio.bib como repositorio local.",
    "Conservar fuentes institucionales registradas: unadmSitioWeb y unadmMallaDerecho2024.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Agregar entradas BibTeX específicas de actividad antes de citar.",
    "Registrar fuentes específicas de actividad en el .bib de la asignatura.",
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "No citar bibliografía base si no fue usada en el argumento.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Incluir fecha de consulta cuando la fuente sea web o institucional dinámica.",
    "Validar correspondencia entre citas en texto y entradas .bib."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo después de validar JSON y estructura.",
    "Propagar reglas de validación JSON y control de no regresión.",
    "Propagar unión-dedupe sin pérdida como criterio de consolidación.",
    "Propagar a materias vecinas de Derecho los cinco ejes editoriales.",
    "Propagar la restricción de no inventar fuentes.",
    "Propagar solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Mantener metadatos específicos dentro de la materia destino.",
    "Evitar transferir redacción literal de actividades laterales.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Aplicar normalización manual si se detecta salida no estructurada.",
    "Marcar ciclos heredados no parseables como provisionales hasta revisión."
  ],
  "open_questions": [
    "Confirmar consigna textual de cada actividad local.",
    "Confirmar producto exacto solicitado: reporte, presentación u otro formato.",
    "Confirmar rúbrica de evaluación específica.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar estilo de citación jurídica requerido: APA, Chicago, ISO 690 u otro.",
    "Confirmar si documentauthor debe ser fijo de plantilla o variable por estudiante.",
    "Confirmar código de curso correcto: plantilla usa LDE-S5B2. [supuesto]",
    "Confirmar existencia operativa de presentacion-etapas-del-proceso-y-estrategia-del-litigio.tex. [supuesto]",
    "Corregir nombres corruptos en README y validar nombres reales de archivos. [supuesto]",
    "Confirmar si la fuente provisional Codex debe conservarse solo como nota técnica.",
    "Definir checklist mínimo por tipo de producto: reporte, presentación y material visual."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Sobrio y verificable.",
        "Orientado a práctica jurídica."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Carpeta de asignatura como entrada canónica.",
        "Trazabilidad editorial en cada consolidación.",
        "Fuentes provisionales separadas de autoridades académicas."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 5, bloque 2, obligatoria, 8 créditos.",
        "Asignatura: Etapas del proceso y estrategia del litigio.",
        "Fuente curricular: malla-curricular-derecho-unadm.pdf.",
        "Coursecode operativo: LDE-S5B2. [supuesto]"
      ]
    },
    "essence": [
      "Problema jurídico o social como punto de partida.",
      "Conceptos, normas, doctrina y datos pertinentes.",
      "Producto solicitado por la planeación.",
      "Evidencia verificable y citas explícitas.",
      "Análisis propio y postura académica.",
      "Conclusión jurídica transferible a la práctica.",
      "Sincronización transversal conservadora.",
      "Normalización estructurada antes de propagar.",
      "Compresión por unión-dedupe sin regresión."
    ],
    "reason_for_being": [
      "Transformar la planeación semanal en productos académicos jurídicos.",
      "Integrar problema, fundamento, evidencia, análisis y cierre argumentativo.",
      "Orientar reportes, presentaciones y productos visuales con identidad UnADM.",
      "Fortalecer criterio propio sustentado.",
      "Conectar teoría procesal y estrategia de litigio con práctica profesional.",
      "Evitar propagaciones no estructuradas o sin verificación."
    ],
    "style_markers": [
      "Encuadre inicial breve del problema.",
      "Objetivo puntual visible.",
      "Secciones claras y reutilizables.",
      "Marco conceptual, normativo o doctrinal explícito.",
      "Afirmaciones con fuente o marca [supuesto].",
      "Citas trazables y verificables.",
      "Análisis propio antes de la conclusión.",
      "Cierre jurídico con implicación práctica.",
      "Portada y metadatos institucionales consistentes.",
      "Sin redacción literal transferida desde nodos laterales."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión jurídica.",
      "Consigna -> objetivo -> desarrollo alineado -> verificación por rúbrica.",
      "Afirmación -> evidencia -> interpretación -> implicación práctica.",
      "Norma -> hecho relevante -> criterio jurídico -> consecuencia procesal.",
      "Concepto -> aplicación al caso -> límite o riesgo -> postura propia.",
      "Fuente institucional -> ubicación curricular -> pauta editorial.",
      "Memoria parseable -> deduplicación -> propagación segura."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Licenciatura en Derecho",
        "Etapas del proceso y estrategia del litigio",
        "Ubicación curricular",
        "Cinco ejes editoriales",
        "Problema jurídico o social",
        "Conceptos jurídicos pertinentes",
        "Marco normativo o doctrinal",
        "Evidencia verificable",
        "Citas trazables",
        "Análisis propio",
        "Postura académica",
        "Conclusión jurídica transferible",
        "Producto solicitado por planeación",
        "Integridad académica",
        "Normalización JSON",
        "Compresión unión-dedupe sin pérdida",
        "No regresión editorial",
        "Fuente provisional",
        "Variables sin resolver en README",
        "Plantilla LaTeX local",
        "Repositorio BibTeX local"
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
          "source": "Malla curricular de Derecho",
          "target": "Ubicación curricular",
          "kind": "supports",
          "justification": "El README local declara semestre 5, bloque 2, tipo obligatoria y 8 créditos con esa fuente."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Conclusión jurídica transferible",
          "kind": "develops",
          "justification": "El programa analítico culmina con conclusión aplicable a la práctica jurídica."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Marco normativo o doctrinal",
          "kind": "depends_on",
          "justification": "El fundamento debe responder al problema que activa la actividad."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Toda afirmación factual requiere fuente o marca [supuesto]."
        },
        {
          "source": "Análisis propio",
          "target": "Postura académica",
          "kind": "develops",
          "justification": "La entrega debe superar el resumen descriptivo y sostener criterio propio."
        },
        {
          "source": "Producto solicitado por planeación",
          "target": "Plantilla LaTeX local",
          "kind": "depends_on",
          "justification": "El formato final debe adaptarse a reporte, presentación o visual según consigna."
        },
        {
          "source": "Repositorio BibTeX local",
          "target": "Citas trazables",
          "kind": "supports",
          "justification": "Las fuentes específicas deben registrarse antes de citarse en versión final."
        },
        {
          "source": "Normalización JSON",
          "target": "Compresión unión-dedupe sin pérdida",
          "kind": "depends_on",
          "justification": "La fusión segura requiere estructura parseable para deduplicar sin recortar reglas útiles."
        },
        {
          "source": "Compresión unión-dedupe sin pérdida",
          "target": "No regresión editorial",
          "kind": "supports",
          "justification": "La consolidación conserva reglas útiles previas y agrega mejoras verificables."
        },
        {
          "source": "Fuente provisional",
          "target": "Integridad académica",
          "kind": "contrasts",
          "justification": "Una fuente heredada no verificada no debe usarse como autoridad académica."
        },
        {
          "source": "Variables sin resolver en README",
          "target": "Plantilla LaTeX local",
          "kind": "contrasts",
          "justification": "Los tokens sin expandir y caracteres corruptos deben corregirse antes de compilar."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 5, bloque 2, obligatoria, 8 créditos.",
        "README local: fuente curricular UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: integridad académica, citas verificables y conclusión jurídica con criterio propio.",
        "Programa analítico local: productos académicos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: reportes, presentaciones y productos visuales.",
        "Programa analítico local: cinco ejes de trabajo.",
        "Archivo .bib local: unadmSitioWeb.",
        "Archivo .bib local: unadmMallaDerecho2024.",
        "Plantilla .tex local: macros documenttitle, coursename, coursecode y universityname.",
        "Plantilla .tex local: coursecode LDE-S5B2. [supuesto operativo]",
        "Contexto heredado: salida previa no JSON parseable requiere normalización.",
        "Origen transversal: reglas estables de problema, conceptos, evidencia, análisis propio y conclusión jurídica."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas de identidad, estructura, actividad y calidad.",
      "Se conservaron reglas útiles previas del destino.",
      "Se transfirieron solo abstracciones estables del origen no equivalente.",
      "Se excluyeron citas y conceptos específicos de Filosofía del Derecho no pertinentes al destino.",
      "Se reforzó el eje transversal de integridad académica.",
      "Se reforzó la conclusión jurídica transferible como cierre obligatorio.",
      "Se mantuvo la advertencia sobre fuentes provisionales heredadas.",
      "Se normalizó la relación del grafo a tipos permitidos.",
      "Se preservó el archivo .bib local como repositorio canónico.",
      "Se dejó abierto todo vacío de consigna, rúbrica, estilo de citación y plantilla."
    ]
  }
}