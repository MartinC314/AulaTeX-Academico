{
  "summary": [
    "Materia destino consolidada con identidad UnADM y enfoque jurídico aplicado.",
    "Ciclo 16 sincroniza abstracciones editoriales transversales desde Filosofía del Derecho.",
    "Se preservan reglas locales verificables de semestre 5, bloque 2, obligatoria, 8 créditos.",
    "Se mantienen cinco ejes editoriales: problema, conceptos, producto, análisis propio y conclusión transferible.",
    "Se refuerza validación JSON antes de cualquier propagación recursiva.",
    "Se conserva compresión por unión y deduplicación sin regresión.",
    "Fuentes heredadas no verificadas quedan como notas técnicas provisionales.",
    "La transferencia entre nodos no equivalentes evita redacción literal de actividades."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho.",
    "Usar contexto local: semestre 5, bloque 2, obligatoria, 8 créditos.",
    "Citar malla-curricular-derecho-unadm.pdf para ubicación curricular.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Usar tono académico-jurídico formal con postura propia sustentada.",
    "Conservar trazabilidad del origen editorial al consolidar memoria.",
    "Registrar fuentes provisionales como nota técnica, no como autoridad académica.",
    "Marcar como [supuesto] todo dato no visible en consigna o documentos locales.",
    "Usar macros de portada: documenttitle, coursename, coursecode, universityname.",
    "Usar coursecode LDE-S5B2 mientras no exista corrección institucional. [supuesto]",
    "Mantener autor de plantilla Martin Jonathan de la Cruz salvo instrucción docente o de actividad. [supuesto]"
  ],
  "structure_rules": [
    "Partir de un problema jurídico o social claro.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Desarrollar conceptos, normas, doctrina o datos pertinentes al caso.",
    "Integrar evidencia verificable antes de interpretar.",
    "Incluir análisis propio antes de la conclusión.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Adaptar salida al producto pedido: reporte, presentación o visual.",
    "Mantener README como entrada canónica de la asignatura.",
    "Usar programa analítico como guía de ejes editoriales.",
    "Seguir cinco ejes: problema, conceptos, producto solicitado, análisis propio y conclusión transferible."
  ],
  "activity_rules": [
    "Verificar la instrucción específica de cada actividad antes de redactar.",
    "Confirmar el producto exacto solicitado por la planeación semanal.",
    "Rubricar cada entrega contra los ejes del programa analítico.",
    "Exigir conclusión jurídica con criterio propio en cada entrega.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Agregar fuentes específicas de actividad al .bib local antes de la versión final.",
    "No citar bibliografía base si no fue usada en el argumento.",
    "No reutilizar reglas laterales sin comprobar pertinencia jurídica.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna."
  ],
  "quality_gates": [
    "Validar JSON parseable en toda memoria antes de aplicar propagación.",
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar respuestas no estructuradas antes de aplicarlas aguas abajo.",
    "Normalizar manualmente memorias heredadas no parseables.",
    "Comprobar unión-dedupe sin eliminar reglas útiles previas.",
    "Revisar estructura mínima completa antes de fusionar memoria.",
    "Revisar consistencia entre metadatos de materia y contenido entregado.",
    "Comprobar que cada afirmación factual tenga fuente o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar ausencia de contradicciones con reglas institucionales heredadas.",
    "Validar que nombres de archivos en README no contengan variables sin resolver.",
    "Revisar caracteres corruptos en README y plantilla antes de publicar. [supuesto]"
  ],
  "latex_rules": [
    "Usar la plantilla .tex local de la materia como base de nuevas actividades.",
    "Usar reporte-etapas-del-proceso-y-estrategia-del-litigio.tex para reportes.",
    "Usar presentacion-etapas-del-proceso-y-estrategia-del-litigio.tex para presentaciones si existe en carpeta. [supuesto]",
    "Conservar documentclass article con opciones spanish, letterpaper, oneside.",
    "Mantener compatibilidad con español y formato letterpaper definido en plantilla.",
    "Conservar macros institucionales de curso, universidad y asignatura.",
    "No eliminar campos de portada; completar faltantes según actividad.",
    "Conservar bloque authortable de la plantilla al adaptar portada.",
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "No confiar en nombres generados con variables sin resolver en README o markdown.",
    "Resolver tokens sin expandir tipo Slug antes de referenciar archivos."
  ],
  "bibliography_rules": [
    "Usar etapas-del-proceso-y-estrategia-del-litigio.bib como repositorio local.",
    "Conservar fuentes institucionales registradas: sitio UnADM y malla curricular Derecho.",
    "Conservar claves BibTeX unadmSitioWeb y unadmMallaDerecho2024.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Agregar entradas BibTeX específicas de actividad antes de citar.",
    "Registrar fuentes específicas de actividad en el .bib de la asignatura.",
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Incluir fecha de consulta cuando la fuente sea web o institucional dinámica.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "No citar bibliografía base si no fue usada en el argumento.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar arriba y laterales reglas de validación JSON y no regresión.",
    "Propagar unión-dedupe sin eliminar reglas útiles previas.",
    "Propagar a materias vecinas de Derecho los cinco ejes editoriales.",
    "Compartir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "No propagar metadatos específicos de esta materia a nodos laterales.",
    "No propagar redacción literal de actividades.",
    "Mantener fuentes provisionales separadas de autoridad académica.",
    "Aplicar normalización manual si se detecta salida no estructurada en nodos vecinos.",
    "Propagar restricción de no inventar fuentes.",
    "Ciclo 1 necesita normalización manual si se reutiliza.",
    "Reforzar conexiones entre problema, fundamento, análisis propio y práctica profesional."
  ],
  "open_questions": [
    "Confirmar si documentauthor debe ser fijo de plantilla o variable por estudiante.",
    "Confirmar estilo de citación jurídica requerido: APA, Chicago, ISO 690 u otro.",
    "Confirmar existencia operativa de presentacion-etapas-del-proceso-y-estrategia-del-litigio.tex. [supuesto]",
    "Confirmar código de curso correcto; plantilla usa LDE-S5B2. [supuesto]",
    "Corregir nombres corruptos en README y validar nombres reales de archivos. [supuesto]",
    "Definir checklist mínimo por tipo de producto: reporte, presentación y material visual.",
    "Confirmar si la fuente provisional Codex debe conservarse solo como nota técnica.",
    "Confirmar si la fuente provisional GPT-Pro debe conservarse solo como nota técnica.",
    "Confirmar rúbrica local de cada actividad antes de fijar profundidad argumentativa.",
    "Confirmar fuentes obligatorias por semana o unidad.",
    "Confirmar producto exacto cuando la consigna local no esté visible.",
    "Confirmar si hay lineamientos docentes adicionales sobre litigio y estrategia procesal."
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
        "Trazabilidad editorial en cada consolidación.",
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
      "Problema jurídico o social como punto de partida.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeación.",
      "Análisis propio y postura académica.",
      "Conclusión jurídica transferible a la práctica.",
      "Normalización estructurada antes de propagar.",
      "JSON parseable como condición de memoria confiable.",
      "Unión-dedupe sin regresión.",
      "Fuentes verificables y no inventadas.",
      "Transferencia transversal por abstracciones, no por copia literal."
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
      "Transformar la planeación semanal en reportes, presentaciones y productos visuales.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Formar criterio jurídico propio sustentado en fuentes verificables.",
      "Conectar el aprendizaje con la práctica profesional del litigio.",
      "Preservar memoria editorial persistente para producción LaTeX confiable."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Objetivo puntual visible.",
      "Bloques argumentativos identificables.",
      "Marco normativo o doctrinal delimitado.",
      "Citas trazables.",
      "Supuestos marcados.",
      "Análisis propio explícito.",
      "Cierre jurídico aplicable.",
      "Metadatos UnADM consistentes.",
      "Lenguaje académico sin relleno."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual o normativo -> análisis propio -> conclusión jurídica.",
      "Afirmación -> evidencia verificable -> interpretación -> implicación práctica.",
      "Consigna -> producto solicitado -> estructura adecuada -> verificación final.",
      "Fuente institucional -> ubicación curricular -> identidad del entregable.",
      "Norma o doctrina -> caso o problema -> criterio del estudiante.",
      "Resumen mínimo -> valoración jurídica -> consecuencia profesional.",
      "Supuesto detectado -> marca explícita -> verificación pendiente.",
      "Memoria heredada -> normalización -> unión-dedupe -> propagación segura."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Licenciatura en Derecho",
        "Etapas del proceso y estrategia del litigio",
        "Semestre 5 bloque 2",
        "Asignatura obligatoria de 8 créditos",
        "Malla curricular Derecho UnADM",
        "Cinco ejes editoriales",
        "Problema jurídico o social",
        "Conceptos, normas, doctrina o datos",
        "Producto solicitado por planeación",
        "Análisis propio",
        "Postura académica",
        "Conclusión jurídica transferible",
        "Fundamento jurídico",
        "Evidencia verificable",
        "Integridad académica",
        "Normalización estructurada",
        "JSON parseable",
        "Unión-dedupe sin regresión",
        "Propagación transversal conservadora",
        "Fuentes provisionales",
        "Archivo .bib local",
        "Plantilla LaTeX local",
        "Macros institucionales",
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
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La pauta local exige identidad institucional, citas verificables y conclusión con criterio propio."
        },
        {
          "source": "Malla curricular Derecho UnADM",
          "target": "Semestre 5 bloque 2",
          "kind": "supports",
          "justification": "El README local declara semestre 5, bloque 2, tipo obligatoria y 8 créditos."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Estructura de entrega",
          "kind": "develops",
          "justification": "El programa analítico organiza productos por problema, conceptos, producto, análisis y conclusión."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "El problema activa la interpretación jurídica y evita entregas solo descriptivas."
        },
        {
          "source": "Fundamento jurídico",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión debe derivar de normas, doctrina, datos o fuentes verificables."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Cada afirmación factual requiere fuente o marca de supuesto."
        },
        {
          "source": "Archivo .bib local",
          "target": "Citas trazables",
          "kind": "depends_on",
          "justification": "Las citas del texto deben corresponder con entradas BibTeX locales."
        },
        {
          "source": "Plantilla LaTeX local",
          "target": "Macros institucionales",
          "kind": "develops",
          "justification": "La plantilla contiene documenttitle, coursename, coursecode y universityname."
        },
        {
          "source": "Tokens sin resolver",
          "target": "Compilación confiable",
          "kind": "contrasts",
          "justification": "Variables sin resolver en README o markdown pueden romper rutas y referencias."
        },
        {
          "source": "Caracteres corruptos en README",
          "target": "Publicación limpia",
          "kind": "contrasts",
          "justification": "Nombres alterados de archivos deben corregirse antes de publicar o compilar."
        },
        {
          "source": "JSON parseable",
          "target": "Propagación transversal conservadora",
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
          "source": "Fuentes provisionales",
          "target": "Autoridad académica",
          "kind": "contrasts",
          "justification": "Las fuentes heredadas no verificadas se conservan como notas técnicas."
        },
        {
          "source": "Transferencia transversal por abstracciones",
          "target": "Sin copia literal de actividades",
          "kind": "supports",
          "justification": "El salto entre materias no equivalentes solo comparte reglas editoriales estables."
        }
      ],
      "evidence": [
        "README local: materia de Licenciatura en Derecho de la UnADM.",
        "README local: semestre 5, bloque 2, obligatoria, 8 créditos.",
        "README local: fuente curricular UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: identidad UnADM, integridad académica, citas verificables y conclusión jurídica.",
        "Programa analítico local: claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: reportes, presentaciones y productos visuales.",
        "Programa analítico local: cinco ejes de trabajo.",
        "Bib local: unadmSitioWeb.",
        "Bib local: unadmMallaDerecho2024.",
        "Plantilla .tex local: documentclass article con spanish, letterpaper y oneside.",
        "Plantilla .tex local: macros documenttitle, documentsubtitle, documentsubject y documentauthor.",
        "Plantilla .tex local: coursename Etapas del proceso y estrategia del litigio.",
        "Plantilla .tex local: coursecode LDE-S5B2.",
        "README local: existen tokens Slug sin resolver en referencia al .bib.",
        "README local: nombres de archivos muestran caracteres corruptos al inicio.",
        "Memoria heredada institucional: salida no JSON parseable requiere revisión.",
        "Memoria origen: bloquear propagación si la salida no es JSON parseable.",
        "Memoria origen: no inventar referencias y usar fuentes consultables.",
        "Memoria origen: iniciar con problema, conceptos, evidencia, análisis propio y conclusión jurídica."
      ]
    },
    "reinforcement_log": [
      "Ciclo 16 preserva identidad local de materia y contexto curricular.",
      "Ciclo 16 agrega solo abstracciones transversales desde actividad origen.",
      "Ciclo 16 elimina duplicados semánticos sin recortar reglas útiles.",
      "Ciclo 16 conserva advertencia sobre memorias no JSON parseables.",
      "Ciclo 16 refuerza unión-dedupe como compresión lossless.",
      "Ciclo 16 mantiene fuentes Codex y GPT-Pro como provisionales.",
      "Ciclo 16 evita trasladar citas de Filosofía del Derecho no verificadas para esta materia.",
      "Ciclo 16 conserva citas locales unadmSitioWeb y unadmMallaDerecho2024.",
      "Ciclo 16 refuerza cinco ejes editoriales para productos jurídicos.",
      "Ciclo 16 marca supuestos sobre coursecode, autor y plantilla de presentación.",
      "Ciclo 16 prioriza estructura reusable, gates de calidad y grafo conceptual.",
      "Ciclo 16 mantiene propagación recursiva conservadora entre nodos no equivalentes."
    ]
  }
}