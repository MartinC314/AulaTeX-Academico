{
  "summary": [
    "Materia destino consolidada con identidad UnADM y enfoque jurídico aplicado.",
    "Sincronización transversal desde actividad no equivalente realizada solo con abstracciones estables.",
    "Se preservan reglas útiles previas mediante unión-dedupe sin regresión.",
    "Validar JSON parseable antes de cualquier propagación recursiva.",
    "Normalizar salidas heredadas no estructuradas antes de reutilizarlas.",
    "Mantener fuentes heredadas no verificadas como provisionales y fuera de autoridad académica.",
    "Ciclo 4 refuerza identidad, estructura reusable, controles de calidad y grafo conceptual."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho.",
    "Usar contexto local: semestre 5, bloque 2, obligatoria, 8 créditos.",
    "Usar tono académico-jurídico formal, claro y verificable.",
    "Exigir postura propia sustentada en cada producto.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Conservar trazabilidad de origen editorial al consolidar memoria.",
    "Marcar como [supuesto] todo dato no visible en consigna o documentos locales.",
    "Registrar fuentes provisionales como nota técnica, no como autoridad académica.",
    "Usar macros de portada: documenttitle, coursename, coursecode y universityname.",
    "Usar coursecode LDE-S5B2 mientras no exista corrección institucional. [supuesto]",
    "Mantener autor de plantilla Martin Jonathan de la Cruz salvo instrucción de actividad o docente. [supuesto]"
  ],
  "structure_rules": [
    "Partir de un problema jurídico o social claro.",
    "Definir objetivo puntual antes del desarrollo.",
    "Desarrollar conceptos, normas, doctrina o datos pertinentes al caso.",
    "Separar bloques: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear la estructura al producto solicitado en planeación semanal.",
    "Adaptar la salida al producto pedido: reporte, presentación o visual.",
    "Incluir análisis propio antes del cierre.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener README como entrada canónica de la asignatura.",
    "Usar el programa analítico como guía de ejes editoriales.",
    "Seguir cinco ejes: problema, conceptos, producto solicitado, análisis propio y conclusión transferible."
  ],
  "activity_rules": [
    "Verificar la instrucción específica de cada actividad antes de redactar.",
    "Confirmar el producto exacto solicitado antes de elegir plantilla.",
    "Rubricar cada entrega contra los ejes del programa analítico.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Integrar evidencia trazable en el cuerpo del trabajo.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Exigir conclusión jurídica con criterio propio en cada entrega.",
    "Agregar fuentes específicas de actividad al .bib local antes de la versión final.",
    "No reutilizar reglas laterales sin comprobar pertinencia jurídica.",
    "No transferir redacción literal de actividades de materias no equivalentes."
  ],
  "quality_gates": [
    "Validar JSON parseable en toda memoria antes de aplicar propagación.",
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de fusionar memoria.",
    "Revisar respuestas no estructuradas antes de aplicarlas aguas abajo.",
    "Normalizar manualmente memorias heredadas de salidas no parseables.",
    "Comprobar unión-dedupe sin eliminar reglas útiles previas.",
    "Confirmar ausencia de contradicciones con reglas heredadas de institución.",
    "Revisar consistencia entre metadatos de materia y contenido entregado.",
    "Comprobar que cada afirmación factual tenga fuente o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Validar correspondencia del producto con la consigna de actividad.",
    "Revisar caracteres corruptos en README y plantilla antes de publicar. [supuesto]",
    "Validar que nombres de archivos no contengan variables sin resolver."
  ],
  "latex_rules": [
    "Usar la plantilla .tex local de la materia como base de nuevas actividades.",
    "Usar reporte-etapas-del-proceso-y-estrategia-del-litigio.tex para reportes.",
    "Usar presentacion-etapas-del-proceso-y-estrategia-del-litigio.tex para presentaciones si el archivo existe. [supuesto]",
    "Conservar macros institucionales de curso, universidad y asignatura.",
    "No eliminar campos de portada; completar faltantes según actividad.",
    "Usar documentclass article con opciones spanish, letterpaper y oneside.",
    "Mantener compatibilidad con español y formato letterpaper definido en plantilla.",
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
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Incluir fecha de consulta cuando la fuente sea web o institucional dinámica."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar arriba y laterales reglas de validación JSON y no regresión.",
    "Propagar a materias vecinas de Derecho los cinco ejes editoriales.",
    "Propagar la restricción de no inventar fuentes.",
    "Propagar la advertencia de normalización manual para salidas no estructuradas.",
    "Propagar solo reglas generales entre nodos no equivalentes.",
    "No propagar metadatos específicos de esta materia a otros nodos.",
    "Mantener metadatos locales dentro de la materia destino.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Aplicar normalización manual si se detecta salida no estructurada en nodos vecinos.",
    "Evitar regresiones respecto de reglas útiles previas."
  ],
  "open_questions": [
    "Confirmar si el nombre de autor en plantilla es definitivo o variable por estudiante.",
    "Confirmar estilo de citación jurídica requerido: APA, Chicago, ISO 690 u otro.",
    "Revisar y corregir posibles caracteres corruptos en README y plantilla .tex. [supuesto]",
    "Definir checklist mínimo por tipo de producto: reporte, presentación y material visual.",
    "Confirmar existencia operativa de presentacion-etapas-del-proceso-y-estrategia-del-litigio.tex. [supuesto]",
    "Confirmar si la fuente provisional Codex debe conservarse solo como nota técnica.",
    "Confirmar código de curso correcto: README no lo declara pero plantilla usa LDE-S5B2. [supuesto]",
    "Confirmar rúbrica específica de cada actividad antes de ajustar profundidad argumentativa.",
    "Confirmar fuentes obligatorias de cada semana.",
    "Confirmar nombre canónico final del archivo .bib si el README conserva token sin resolver."
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
      "Identidad UnADM.",
      "Enfoque jurídico aplicado.",
      "Cinco ejes editoriales.",
      "Problema jurídico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por planeación.",
      "Análisis propio y postura académica.",
      "Conclusión transferible a la práctica jurídica.",
      "Normalización estructurada.",
      "Unión-dedupe sin regresión.",
      "Citas verificables.",
      "Fuentes no verificadas como provisionales."
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
      "Transformar planeación semanal en reportes, presentaciones o productos visuales.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Convertir cada actividad en una pieza jurídica verificable y aplicable.",
      "Preservar memoria editorial persistente sin pérdida de reglas útiles."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Objetivo puntual visible.",
      "Bloques argumentativos separados.",
      "Marco normativo o doctrinal explícito.",
      "Postura propia sustentada.",
      "Citas trazables.",
      "Supuestos marcados.",
      "Cierre jurídico aplicable.",
      "Metadatos UnADM conservados.",
      "Redacción sin trasplantes literales de otros nodos."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual y normativo -> análisis propio -> conclusión jurídica.",
      "Afirmación -> evidencia verificable -> interpretación -> implicación práctica.",
      "Consigna -> producto solicitado -> estructura adecuada -> checklist de calidad.",
      "Dato local -> fuente institucional -> uso editorial prudente.",
      "Regla heredada -> pertinencia local -> adopción sin regresión.",
      "Fuente provisional -> verificación pendiente -> no autoridad académica.",
      "Actividad jurídica -> criterio propio -> transferencia profesional."
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
        "Conceptos, normas, doctrina o datos pertinentes",
        "Producto solicitado por planeación",
        "Análisis propio y postura académica",
        "Conclusión jurídica transferible",
        "Integridad académica",
        "Citas verificables",
        "Bibliografía local",
        "Fuentes institucionales UnADM",
        "Malla curricular Derecho",
        "JSON parseable",
        "Normalización estructurada",
        "Unión-dedupe sin regresión",
        "Propagación recursiva segura",
        "Variables sin resolver en README",
        "Caracteres corruptos en rutas",
        "Fuentes provisionales"
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
          "justification": "La pauta local exige identidad institucional, citas verificables y conclusión jurídica."
        },
        {
          "source": "Malla curricular Derecho",
          "target": "Semestre 5 bloque 2",
          "kind": "supports",
          "justification": "El README declara semestre, bloque, tipo, créditos y fuente curricular."
        },
        {
          "source": "Programa analítico editorial",
          "target": "Cinco ejes editoriales",
          "kind": "develops",
          "justification": "El programa lista problema, conceptos, producto, análisis propio y conclusión."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Estructura de entrega",
          "kind": "develops",
          "justification": "Los ejes ordenan la construcción de reportes, presentaciones y productos visuales."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Análisis propio y postura académica",
          "kind": "supports",
          "justification": "El problema activa la argumentación y evita entregas meramente descriptivas."
        },
        {
          "source": "Conceptos, normas, doctrina o datos pertinentes",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "El fundamento permite cerrar con aplicación profesional."
        },
        {
          "source": "Citas verificables",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Las afirmaciones deben tener fuente explícita o marca de supuesto."
        },
        {
          "source": "Bibliografía local",
          "target": "Citas verificables",
          "kind": "supports",
          "justification": "El .bib local conserva fuentes institucionales y entradas específicas de actividad."
        },
        {
          "source": "JSON parseable",
          "target": "Propagación recursiva segura",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay fusión confiable aguas abajo."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva segura",
          "kind": "supports",
          "justification": "La normalización evita aplicar salidas no estructuradas."
        },
        {
          "source": "Unión-dedupe sin regresión",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Permite compresión lossless sin borrar reglas útiles previas."
        },
        {
          "source": "Variables sin resolver en README",
          "target": "Compilación LaTeX confiable",
          "kind": "contrasts",
          "justification": "Los tokens sin resolver pueden romper nombres de archivo y referencias."
        },
        {
          "source": "Caracteres corruptos en rutas",
          "target": "Compilación LaTeX confiable",
          "kind": "contrasts",
          "justification": "Las rutas corruptas deben corregirse antes de compilar o referenciar."
        },
        {
          "source": "Fuentes provisionales",
          "target": "Autoridad académica",
          "kind": "contrasts",
          "justification": "Las fuentes heredadas no verificadas solo son notas técnicas."
        }
      ],
      "evidence": [
        "README de materia: Licenciatura en Derecho de la UnADM.",
        "README de materia: semestre 5, bloque 2, obligatoria, 8 créditos.",
        "README de materia: fuente curricular UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
        "README de materia: carpeta como punto de entrada canónico.",
        "README de materia: integridad académica, citas verificables y conclusión jurídica con criterio propio.",
        "Programa analítico: claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico: reportes, presentaciones y productos visuales.",
        "Programa analítico: cinco ejes de trabajo.",
        "Bib local: unadmSitioWeb.",
        "Bib local: unadmMallaDerecho2024.",
        "Plantilla tex local: macros documenttitle, coursename, coursecode y universityname.",
        "Plantilla tex local: coursecode LDE-S5B2.",
        "Plantilla tex local: documentclass article con spanish, letterpaper y oneside.",
        "README local: token $(@{...}.Slug) pendiente de resolver.",
        "README local: posibles caracteres corruptos en nombres de archivo. [supuesto]",
        "Memoria heredada: salida no JSON parseable desde Codex.",
        "Memoria destino previa: salida no JSON parseable desde GPT-Pro.",
        "Regla transversal consolidada: validar JSON parseable antes de propagar.",
        "Regla transversal consolidada: aplicar unión-dedupe sin regresión."
      ]
    },
    "reinforcement_log": [
      "Ciclo 4 preservó reglas locales válidas y eliminó duplicados semánticos.",
      "Se evitó transferir fuentes y conceptos específicos de Filosofía del Derecho.",
      "Se transfirieron solo patrones estables: problema, fundamento, análisis propio y conclusión.",
      "Se reforzó validación JSON como compuerta de propagación recursiva.",
      "Se reforzó no inventar fuentes y marcar supuestos.",
      "Se consolidó el archivo .bib local como repositorio bibliográfico de la materia.",
      "Se mantuvo coursecode LDE-S5B2 como dato visible en plantilla con verificación pendiente.",
      "Se conservaron advertencias sobre tokens sin resolver y caracteres corruptos.",
      "Se corrigió el grafo para usar solo relaciones permitidas.",
      "Se mantuvo la memoria heredada no estructurada como nota técnica provisional."
    ]
  }
}