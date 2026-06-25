{
  "summary": [
    "Materia destino consolidada con identidad UnADM y enfoque jurídico aplicado.",
    "Sincronización transversal aplicada con abstracciones estables, no redacción literal.",
    "Se preservan reglas útiles previas mediante unión y deduplicación sin regresión.",
    "Se mantiene validación de JSON parseable antes de cualquier propagación.",
    "La herencia institucional no estructurada queda normalizada como nota técnica provisional.",
    "Se refuerzan cinco ejes editoriales: problema, conceptos, producto, análisis propio y conclusión transferible.",
    "Se conserva contexto local verificable: Licenciatura en Derecho, semestre 5, bloque 2, obligatoria, 8 créditos.",
    "Se bloquea la invención de fuentes y se exige trazabilidad bibliográfica local.",
    "Se refuerza la carpeta de asignatura como entrada canónica.",
    "Ciclo 14 consolidado con estrategia progresiva y conservadora."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho.",
    "Usar contexto curricular local: semestre 5, bloque 2, obligatoria, 8 créditos.",
    "Citar la malla curricular Derecho UnADM como fuente de ubicación curricular.",
    "Usar tono académico-jurídico formal, claro y verificable.",
    "Exigir postura propia sustentada en cada producto.",
    "Conservar trazabilidad de origen editorial al consolidar memoria.",
    "Registrar fuentes provisionales como nota técnica, no como autoridad académica.",
    "Marcar como [supuesto] todo dato no visible en consigna o documentos locales.",
    "Usar macros de portada: documenttitle, documentsubtitle, documentsubject, documentauthor, coursename, coursecode y universityname.",
    "Usar coursecode LDE-S5B2 mientras no exista corrección institucional. [supuesto]",
    "Mantener autor de plantilla Martin Jonathan de la Cruz salvo instrucción de actividad o docente. [supuesto]",
    "No transferir metadatos curriculares de Filosofía del Derecho a esta materia."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar bloques: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Desarrollar conceptos, normas, doctrina o datos pertinentes al caso.",
    "Alinear la entrega al producto solicitado por la planeación semanal.",
    "Adaptar salida al producto pedido: reporte, presentación o material visual.",
    "Usar el programa analítico como guía de ejes editoriales.",
    "Seguir cinco ejes: problema, conceptos, producto solicitado, análisis propio y conclusión transferible.",
    "Incluir análisis propio antes del cierre.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener README como entrada canónica de la asignatura.",
    "Transformar la planeación en producto académico verificable según consigna."
  ],
  "activity_rules": [
    "Verificar la instrucción específica de cada actividad antes de redactar.",
    "Confirmar el producto exacto solicitado por la consigna.",
    "Rubricar cada entrega contra los ejes del programa analítico.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Integrar evidencia trazable en el cuerpo del trabajo.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Exigir conclusión jurídica con criterio propio en cada entrega.",
    "Agregar fuentes específicas de actividad al .bib local antes de la versión final.",
    "No reutilizar reglas laterales sin comprobar pertinencia jurídica.",
    "No asumir que fuentes de otra semana o materia corresponden a una actividad local.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión."
  ],
  "quality_gates": [
    "Validar JSON parseable en toda memoria antes de aplicar propagación.",
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de fusionar memoria.",
    "Normalizar manualmente respuestas no estructuradas antes de reutilizarlas.",
    "Comprobar unión-dedupe sin eliminar reglas útiles previas.",
    "Revisar consistencia entre metadatos de materia y contenido entregado.",
    "Confirmar que cada afirmación factual tenga fuente o marca de [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar ausencia de contradicciones con reglas institucionales heredadas.",
    "Validar correspondencia del producto con la consigna de actividad.",
    "Revisar caracteres corruptos en README y plantilla antes de publicar. [supuesto]",
    "Validar que nombres de archivos no contengan variables sin resolver.",
    "Confirmar que no se propaguen metadatos locales hacia nodos no equivalentes."
  ],
  "latex_rules": [
    "Usar la plantilla .tex local de la materia como base de nuevas actividades.",
    "Usar reporte-etapas-del-proceso-y-estrategia-del-litigio.tex para reportes.",
    "Usar presentacion-etapas-del-proceso-y-estrategia-del-litigio.tex para presentaciones si existe en carpeta. [supuesto]",
    "Conservar macros institucionales de curso, universidad y asignatura.",
    "No eliminar campos de portada; completar faltantes según actividad.",
    "Usar documentclass article con opciones spanish, letterpaper y oneside.",
    "Mantener compatibilidad con español y acentos correctos en .tex y .bib.",
    "Conservar bloque authortable de la plantilla al adaptar portada.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Verificar nombres reales de archivos del README antes de referenciarlos.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README, programa analítico y nombres de archivo.",
    "No copiar LaTeX completo en memoria editorial."
  ],
  "bibliography_rules": [
    "Usar etapas-del-proceso-y-estrategia-del-litigio.bib como repositorio local.",
    "Conservar fuentes institucionales ya registradas: sitio UnADM y malla curricular Derecho.",
    "Conservar claves BibTeX unadmSitioWeb y unadmMallaDerecho2024.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Agregar entradas BibTeX específicas de actividad antes de citar.",
    "Registrar solo fuentes realmente consultadas y verificables.",
    "No inventar referencias.",
    "No citar bibliografía base si no fue usada en el argumento.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Incluir fecha de consulta cuando la fuente sea web o institucional dinámica.",
    "Validar correspondencia entre citas en texto y entradas .bib.",
    "No transferir referencias específicas de Filosofía del Derecho salvo uso local verificable."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar arriba y laterales reglas de validación JSON y no regresión.",
    "Propagar unión-dedupe sin pérdida como política editorial.",
    "Propagar a materias vecinas de Derecho los cinco ejes editoriales generales.",
    "Propagar la restricción de no inventar fuentes.",
    "Propagar la obligación de marcar supuestos.",
    "Propagar solo abstracciones estables entre nodos no equivalentes.",
    "No propagar metadatos específicos de esta materia.",
    "No propagar redacción literal de actividades laterales.",
    "Mantener fuentes heredadas no verificadas como provisionales.",
    "Aplicar normalización manual si se detecta salida no estructurada en nodos vecinos.",
    "Ciclo 1 heredado requiere normalización manual si se reutiliza.",
    "Conservar trazabilidad del salto transversal desde Filosofía del Derecho."
  ],
  "open_questions": [
    "Confirmar si el nombre de autor en plantilla es definitivo o variable por estudiante.",
    "Confirmar código de curso correcto: plantilla usa LDE-S5B2. [supuesto]",
    "Confirmar estilo de citación jurídica requerido: APA, Chicago, ISO 690 u otro.",
    "Confirmar existencia operativa de presentacion-etapas-del-proceso-y-estrategia-del-litigio.tex. [supuesto]",
    "Corregir nombres corruptos en README y validar nombres reales de archivos. [supuesto]",
    "Confirmar si la fuente provisional Codex debe conservarse solo como nota técnica.",
    "Definir checklist mínimo por tipo de producto: reporte, presentación y material visual.",
    "Confirmar rúbrica de evaluación específica por actividad.",
    "Confirmar fuentes obligatorias de cada semana.",
    "Confirmar si cada actividad requiere .bib propio o solo .bib de asignatura.",
    "Confirmar producto exacto de cada actividad antes de redactar.",
    "Confirmar si hay criterios procesales o litigiosos específicos no visibles en el contexto local."
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
      "Identidad UnADM aplicada a productos jurídicos.",
      "Problema jurídico o social como punto de partida.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeación.",
      "Análisis propio y postura académica.",
      "Conclusión jurídica transferible a la práctica.",
      "Integridad académica con evidencia verificable.",
      "Normalización estructurada antes de propagar.",
      "Unión-dedupe sin regresión.",
      "Transferencia transversal por abstracciones estables."
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
      "Transformar la planeación semanal en reportes, presentaciones o productos visuales.",
      "Asegurar que cada entrega conecte problema, fundamento, análisis y cierre jurídico.",
      "Fortalecer criterio propio sustentado en fuentes verificables.",
      "Conservar memoria editorial persistente sin pérdida de reglas útiles.",
      "Evitar que contenido no estructurado o no verificado contamine nodos aguas abajo."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Objetivo puntual visible.",
      "Bloques argumentativos claros.",
      "Marco normativo o doctrinal separado.",
      "Citas trazables.",
      "Supuestos marcados.",
      "Postura propia explícita.",
      "Cierre jurídico aplicable.",
      "Metadatos UnADM completos.",
      "Lenguaje jurídico sobrio.",
      "Transferencia profesional explícita.",
      "Sin redacción lateral copiada."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis propio -> conclusión jurídica.",
      "Afirmación -> evidencia verificable -> interpretación -> implicación práctica.",
      "Consigna -> objetivo -> producto -> criterios de evaluación -> entrega.",
      "Hecho o caso -> norma aplicable -> doctrina pertinente -> postura razonada.",
      "Fuente institucional -> dato curricular -> uso editorial delimitado.",
      "Supuesto -> marca explícita -> verificación pendiente.",
      "Bibliografía base -> uso real en argumento -> cita en texto -> entrada .bib.",
      "Memoria heredada -> normalización -> deduplicación -> propagación segura."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Licenciatura en Derecho",
        "Etapas del proceso y estrategia del litigio",
        "Semestre 5 bloque 2",
        "Asignatura obligatoria de 8 créditos",
        "Carpeta de asignatura canónica",
        "Programa analítico editorial",
        "Cinco ejes editoriales",
        "Problema jurídico o social",
        "Conceptos jurídicos pertinentes",
        "Marco normativo",
        "Marco doctrinal",
        "Evidencia verificable",
        "Análisis propio",
        "Postura académica",
        "Conclusión jurídica transferible",
        "Práctica profesional",
        "Producto solicitado por planeación",
        "Reporte académico",
        "Presentación académica",
        "Material visual",
        "Normalización estructurada",
        "JSON parseable",
        "Unión-dedupe sin regresión",
        "Fuentes provisionales",
        "Supuestos marcados",
        "BibTeX local",
        "Metadatos institucionales",
        "Tokens sin expandir",
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
          "justification": "La plantilla local conserva portada, curso, universidad y asignatura."
        },
        {
          "source": "Identidad UnADM",
          "target": "Integridad académica con citas verificables",
          "kind": "supports",
          "justification": "La pauta editorial exige identidad institucional y citas verificables."
        },
        {
          "source": "Programa analítico editorial",
          "target": "Cinco ejes editoriales",
          "kind": "develops",
          "justification": "El programa local enumera problema, conceptos, producto, análisis y conclusión."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Estructura de entrega",
          "kind": "develops",
          "justification": "Los ejes organizan reportes, presentaciones y productos visuales."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "El problema activa la argumentación y orienta la postura del estudiante."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión requiere fundamento jurídico aplicable a la práctica."
        },
        {
          "source": "Evidencia verificable",
          "target": "Postura académica",
          "kind": "supports",
          "justification": "La postura debe sostenerse con fuentes trazables."
        },
        {
          "source": "BibTeX local",
          "target": "Citas trazables",
          "kind": "supports",
          "justification": "El archivo .bib local concentra las fuentes usadas en la asignatura."
        },
        {
          "source": "JSON parseable",
          "target": "Propagación recursiva segura",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay fusión confiable aguas abajo."
        },
        {
          "source": "Normalización estructurada",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "La normalización evita contaminar la memoria con salidas no estructuradas."
        },
        {
          "source": "Unión-dedupe sin regresión",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Permite comprimir sin borrar reglas útiles previas."
        },
        {
          "source": "Fuentes provisionales",
          "target": "Autoridad académica",
          "kind": "contrasts",
          "justification": "Las fuentes heredadas no verificadas no deben usarse como respaldo académico."
        },
        {
          "source": "Supuestos marcados",
          "target": "Afirmaciones no verificadas",
          "kind": "contrasts",
          "justification": "Todo dato no visible debe señalarse como supuesto hasta confirmación local."
        },
        {
          "source": "Tokens sin expandir",
          "target": "Compilación LaTeX confiable",
          "kind": "contrasts",
          "justification": "Los tokens tipo $(@{...}.Slug) pueden romper nombres y referencias."
        },
        {
          "source": "Caracteres corruptos en README",
          "target": "Referencias de archivo confiables",
          "kind": "contrasts",
          "justification": "Los nombres corruptos deben corregirse antes de usarse en compilación."
        },
        {
          "source": "Transferencia transversal por abstracciones estables",
          "target": "Nodos no equivalentes",
          "kind": "supports",
          "justification": "El salto desde una actividad lateral solo comparte patrones editoriales generales."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 5, bloque 2, obligatoria, 8 créditos.",
        "README local: fuente curricular malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: exige identidad UnADM, integridad académica, citas verificables y conclusión jurídica.",
        "Programa analítico local: orienta productos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: transforma planeación semanal en reportes, presentaciones y productos visuales.",
        "Programa analítico local: lista cinco ejes de trabajo.",
        "Bib local: contiene unadmSitioWeb.",
        "Bib local: contiene unadmMallaDerecho2024.",
        "Plantilla .tex local: documentclass article con spanish, letterpaper y oneside.",
        "Plantilla .tex local: macros documenttitle, documentsubtitle, documentsubject, documentauthor, coursename y coursecode.",
        "Plantilla .tex local: coursecode visible LDE-S5B2.",
        "README local: contiene caracteres corruptos en nombres de archivo. [supuesto operativo]",
        "README y programa local: contienen token sin expandir $(@{...}.Slug).",
        "Memoria heredada institucional: salida no JSON parseable requiere normalización.",
        "Regla transversal consolidada: no inventar fuentes.",
        "Regla transversal consolidada: validar JSON parseable antes de propagar.",
        "Regla transversal consolidada: aplicar unión-dedupe sin regresión.",
        "Regla transversal consolidada: compartir abstracciones estables entre nodos no equivalentes."
      ]
    },
    "reinforcement_log": [
      "Ciclo 14 preserva identidad local de la materia destino.",
      "Ciclo 14 deduplica variantes repetidas sin eliminar reglas útiles.",
      "Ciclo 14 refuerza validación JSON como compuerta obligatoria.",
      "Ciclo 14 mantiene fuentes heredadas no verificadas como provisionales.",
      "Ciclo 14 evita transferir metadatos de Filosofía del Derecho.",
      "Ciclo 14 transfiere solo patrones editoriales generales.",
      "Ciclo 14 consolida cinco ejes editoriales como núcleo reusable.",
      "Ciclo 14 refuerza conclusión jurídica con criterio propio.",
      "Ciclo 14 añade control explícito de tokens sin expandir.",
      "Ciclo 14 conserva bibliografía local UnADM como base verificable.",
      "Ciclo 14 deja abiertas verificaciones de autor, coursecode, estilo de cita y plantillas.",
      "Ciclo 14 mantiene estrategia progresiva y conservadora."
    ]
  }
}