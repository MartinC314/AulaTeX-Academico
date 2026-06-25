{
  "summary": [
    "Materia consolidada con identidad UnADM y enfoque jurídico aplicado.",
    "Ciclo 3 sincroniza abstracciones transversales desde Filosofía del Derecho.",
    "Se preservan reglas locales de semestre 5, bloque 2, obligatoria, 8 créditos.",
    "Se mantiene compresión lossless por unión y deduplicación.",
    "Se exige JSON parseable antes de toda propagación.",
    "Se conserva normalización manual para memorias heredadas no estructuradas.",
    "Se refuerzan cinco ejes editoriales: problema, conceptos, producto, análisis propio y conclusión.",
    "La transferencia entre nodos no equivalentes usa abstracciones, no redacción literal.",
    "Las fuentes heredadas no verificadas quedan como notas técnicas provisionales."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho.",
    "Usar contexto local: semestre 5, bloque 2, obligatoria, 8 créditos.",
    "Citar malla-curricular-derecho-unadm.pdf para ubicación curricular.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Usar tono académico-jurídico formal, claro y preciso.",
    "Exigir postura propia sustentada.",
    "Conservar trazabilidad editorial al consolidar memoria.",
    "Marcar como [supuesto] todo dato no visible en consigna o documentos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales.",
    "Registrar fuentes provisionales como nota técnica, no como autoridad académica.",
    "Usar macros de portada: documenttitle, coursename, coursecode, universityname.",
    "Usar coursecode LDE-S5B2 mientras no exista corrección institucional. [supuesto]",
    "Mantener autor de plantilla Martin Jonathan de la Cruz salvo instrucción contraria. [supuesto]"
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Desarrollar conceptos, normas, doctrina o datos pertinentes al caso.",
    "Adaptar la salida al producto pedido: reporte, presentación o visual.",
    "Alinear la entrega con la planeación semanal.",
    "Usar el programa analítico como guía de ejes editoriales.",
    "Seguir cinco ejes: problema, conceptos, producto solicitado, análisis propio y conclusión transferible.",
    "Incluir análisis propio antes del cierre.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener README como entrada canónica de la asignatura."
  ],
  "activity_rules": [
    "Verificar la instrucción específica de cada actividad antes de redactar.",
    "Confirmar producto exacto solicitado antes de estructurar.",
    "Rubricar cada entrega contra los ejes del programa analítico.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Integrar evidencia trazable en el cuerpo del trabajo.",
    "Agregar fuentes específicas de actividad al .bib local antes de la versión final.",
    "No citar bibliografía base si no fue usada en el argumento.",
    "Incluir conclusión jurídica con criterio propio.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No reutilizar reglas laterales sin comprobar pertinencia jurídica.",
    "No asumir fuentes de otra actividad como fuentes de la actividad actual."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de fusionar memoria.",
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar manualmente memorias heredadas no estructuradas.",
    "Comprobar unión-dedupe sin eliminar reglas útiles previas.",
    "Confirmar ausencia de contradicciones con reglas institucionales.",
    "Revisar consistencia entre metadatos de materia y contenido entregado.",
    "Comprobar que cada afirmación factual tenga fuente o marca de supuesto.",
    "Validar correspondencia entre consigna, producto y estructura.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar caracteres corruptos en README y plantilla antes de publicar. [supuesto]",
    "Validar que nombres de archivos no contengan variables sin resolver.",
    "Confirmar que no existan referencias rotas antes de compilar."
  ],
  "latex_rules": [
    "Usar la plantilla .tex local como base de nuevas actividades.",
    "Usar reporte-etapas-del-proceso-y-estrategia-del-litigio.tex para reportes.",
    "Usar presentacion-etapas-del-proceso-y-estrategia-del-litigio.tex para presentaciones si existe. [supuesto]",
    "Conservar macros institucionales de curso, universidad y asignatura.",
    "No eliminar campos de portada; completar faltantes según actividad.",
    "Mantener compatibilidad con español y formato letterpaper de la plantilla.",
    "Usar documentclass article con opciones spanish, letterpaper, oneside si la plantilla local lo conserva.",
    "Conservar bloque authortable de la plantilla al adaptar portada.",
    "Usar codificación y acentos correctos en .tex y .bib.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "No confiar en nombres generados con variables sin resolver."
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
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar nombre canónico final del archivo .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar arriba y laterales reglas de validación JSON.",
    "Propagar unión-dedupe sin regresión.",
    "Propagar la restricción de no inventar fuentes.",
    "Propagar a materias vecinas de Derecho los cinco ejes editoriales.",
    "Propagar solo abstracciones editoriales estables entre nodos no equivalentes.",
    "No propagar metadatos específicos de esta materia a nodos laterales.",
    "No propagar redacción literal de actividades.",
    "Aplicar normalización manual si se detecta salida no estructurada.",
    "Ciclo 1 necesita normalización manual si se reutiliza.",
    "Conservar fuentes heredadas no verificadas como provisionales.",
    "Mantener especificidad local al recibir reglas transversales."
  ],
  "open_questions": [
    "Confirmar si el nombre de autor en plantilla es definitivo o variable por estudiante.",
    "Confirmar estilo de citación jurídica requerido: APA, Chicago, ISO 690 u otro.",
    "Confirmar código de curso correcto: la plantilla usa LDE-S5B2. [supuesto]",
    "Confirmar existencia operativa de presentacion-etapas-del-proceso-y-estrategia-del-litigio.tex. [supuesto]",
    "Corregir nombres corruptos en README y validar nombres reales de archivos. [supuesto]",
    "Confirmar nombre canónico final del archivo .bib de la asignatura.",
    "Definir checklist mínimo por tipo de producto: reporte, presentación y material visual.",
    "Confirmar si la fuente provisional Codex debe conservarse solo como nota técnica.",
    "Confirmar fuentes obligatorias por semana o actividad.",
    "Confirmar rúbrica específica de evaluación por actividad.",
    "Confirmar producto exacto cuando la consigna local no esté visible."
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
        "Asignatura: Etapas del proceso y estrategia del litigio.",
        "Semestre 5, bloque 2, obligatoria, 8 créditos.",
        "Fuente curricular local: malla-curricular-derecho-unadm.pdf.",
        "Coursecode visible en plantilla: LDE-S5B2. [supuesto]"
      ]
    },
    "essence": [
      "Identidad UnADM aplicada a productos jurídicos.",
      "Problema jurídico o social como punto de partida.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeación.",
      "Análisis propio y postura académica.",
      "Conclusión jurídica transferible a la práctica.",
      "Integridad académica con evidencia verificable.",
      "Memoria persistente por unión-dedupe sin regresión.",
      "Transferencia transversal por abstracciones estables."
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
      "Transformar la planeación semanal en reportes, presentaciones y productos visuales.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Consolidar una base editorial reutilizable para actividades de litigio.",
      "Evitar productos descriptivos sin criterio jurídico propio."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Objetivo visible.",
      "Bloques argumentativos claros.",
      "Marco normativo o doctrinal explícito.",
      "Citas trazables.",
      "Supuestos marcados.",
      "Análisis propio diferenciado del resumen.",
      "Cierre jurídico aplicable.",
      "Metadatos institucionales completos.",
      "Lenguaje académico sin grandilocuencia."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis propio -> conclusión jurídica.",
      "Afirmación -> evidencia verificable -> interpretación -> implicación práctica.",
      "Consigna -> producto esperado -> estructura -> checklist de cumplimiento.",
      "Hecho relevante -> norma aplicable -> razonamiento jurídico -> efecto procesal. [supuesto disciplinar]",
      "Concepto -> función en el litigio -> uso práctico. [supuesto disciplinar]",
      "Fuente institucional -> dato curricular -> metadato de portada.",
      "Regla heredada -> pertinencia local -> adopción conservadora.",
      "Memoria no estructurada -> normalización -> propagación segura."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Licenciatura en Derecho",
        "Etapas del proceso y estrategia del litigio",
        "Semestre 5 bloque 2",
        "Obligatoria 8 créditos",
        "Carpeta de asignatura como entrada canónica",
        "Problema jurídico o social",
        "Conceptos jurídicos pertinentes",
        "Marco normativo o doctrinal",
        "Evidencia verificable",
        "Análisis propio",
        "Postura académica",
        "Conclusión jurídica transferible",
        "Producto solicitado por la planeación",
        "Reporte",
        "Presentación",
        "Material visual",
        "Integridad académica",
        "Citas trazables",
        "Archivo .bib local",
        "JSON parseable",
        "Normalización estructurada",
        "Unión-dedupe sin regresión",
        "Fuentes provisionales",
        "Variables sin resolver en README",
        "Caracteres corruptos en rutas",
        "Estrategia de litigio. [supuesto por nombre de asignatura]",
        "Etapas procesales. [supuesto por nombre de asignatura]"
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
          "justification": "La pauta local exige conservar identidad UnADM, citas verificables y conclusión jurídica."
        },
        {
          "source": "Malla curricular de Derecho",
          "target": "Semestre 5 bloque 2",
          "kind": "supports",
          "justification": "El README local declara semestre, bloque, tipo y créditos con fuente institucional."
        },
        {
          "source": "Carpeta de asignatura como entrada canónica",
          "target": "Metadatos institucionales",
          "kind": "supports",
          "justification": "El README local define la carpeta como punto de entrada canónico."
        },
        {
          "source": "Programa analítico",
          "target": "Cinco ejes editoriales",
          "kind": "develops",
          "justification": "El programa enumera problema, conceptos, producto, análisis propio y conclusión."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Marco normativo o doctrinal",
          "kind": "depends_on",
          "justification": "El fundamento se selecciona según el problema planteado."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Análisis propio",
          "kind": "supports",
          "justification": "El análisis requiere conceptos, normas, doctrina o datos pertinentes."
        },
        {
          "source": "Evidencia verificable",
          "target": "Postura académica",
          "kind": "supports",
          "justification": "La postura debe estar sustentada y no limitarse a resumen."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "develops",
          "justification": "El cierre debe derivar del razonamiento y aplicar a la práctica profesional."
        },
        {
          "source": "Producto solicitado por la planeación",
          "target": "Estructura de entrega",
          "kind": "develops",
          "justification": "La estructura se adapta a reporte, presentación o visual."
        },
        {
          "source": "Archivo .bib local",
          "target": "Citas trazables",
          "kind": "supports",
          "justification": "Las fuentes citadas deben registrarse en el repositorio bibliográfico de la asignatura."
        },
        {
          "source": "JSON parseable",
          "target": "Propagación recursiva segura",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay fusión confiable de memoria."
        },
        {
          "source": "Unión-dedupe sin regresión",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Permite compresión lossless sin eliminar reglas útiles."
        },
        {
          "source": "Fuentes provisionales",
          "target": "Autoridad académica",
          "kind": "contrasts",
          "justification": "Las fuentes heredadas no verificadas deben quedar fuera del sustento académico."
        },
        {
          "source": "Variables sin resolver en README",
          "target": "Compilación confiable",
          "kind": "contrasts",
          "justification": "Los tokens sin expandir pueden romper rutas, citas o nombres de archivo."
        },
        {
          "source": "Caracteres corruptos en rutas",
          "target": "Compilación confiable",
          "kind": "contrasts",
          "justification": "Los nombres anómalos deben corregirse antes de referenciar archivos."
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
        "Plantilla tex local: macros documenttitle, coursename, coursecode y universityname.",
        "Plantilla tex local: coursecode LDE-S5B2.",
        "README local contiene token sin resolver tipo $(@{...}.Slug).",
        "README local muestra posibles caracteres corruptos en nombres de archivo. [supuesto]"
      ]
    },
    "reinforcement_log": [
      "Ciclo 3 preserva reglas útiles del destino.",
      "Ciclo 3 incorpora solo abstracciones estables del origen.",
      "Se deduplican variantes ortográficas sin recortar contenido útil.",
      "Se evita transferir fuentes específicas de Filosofía del Derecho al destino.",
      "Se conservan solo citas locales verificables: unadmSitioWeb y unadmMallaDerecho2024.",
      "Se refuerza la pauta problema-fundamento-análisis-cierre.",
      "Se refuerza la separación entre bibliografía base y bibliografía específica.",
      "Se refuerza el bloqueo de propagación ante JSON no parseable.",
      "Se refuerza la revisión de tokens sin resolver y rutas corruptas.",
      "Se marca como supuesto lo no confirmado por documentos locales."
    ]
  }
}