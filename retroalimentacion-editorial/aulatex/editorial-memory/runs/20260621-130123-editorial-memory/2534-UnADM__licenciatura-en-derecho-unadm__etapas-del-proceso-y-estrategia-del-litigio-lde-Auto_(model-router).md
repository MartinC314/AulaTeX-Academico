{
  "summary": [
    "Materia consolidada con identidad UnADM y enfoque jurídico aplicado.",
    "Sincronización transversal desde actividad no equivalente.",
    "Transferir solo abstracciones editoriales estables.",
    "Conservar cinco ejes: problema, conceptos, producto, análisis propio y conclusión.",
    "Aplicar compresión union-dedupe sin pérdida ni regresión.",
    "Validar JSON parseable antes de propagar.",
    "Mantener fuentes heredadas no verificadas como provisionales.",
    "Ciclo 18 refuerza estructura reusable, calidad y grafo conceptual."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho.",
    "Usar contexto local: semestre 5, bloque 2, obligatoria, 8 créditos.",
    "Usar tono académico-jurídico formal.",
    "Exigir postura propia sustentada.",
    "Conservar trazabilidad de origen editorial.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Marcar como [supuesto] todo dato no visible en documentos locales.",
    "Registrar fuentes provisionales como nota técnica.",
    "No tratar fuentes provisionales como autoridad académica.",
    "Usar macros de portada: documenttitle, coursename, coursecode, universityname.",
    "Usar coursecode LDE-S5B2 mientras no exista corrección institucional. [supuesto]",
    "Mantener autor de plantilla salvo instrucción docente o de actividad. [supuesto]"
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Desarrollar conceptos, normas, doctrina o datos pertinentes al caso.",
    "Alinear la entrega al producto solicitado en la planeación.",
    "Adaptar salida a reporte, presentación o producto visual según consigna.",
    "Incluir análisis propio antes del cierre.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Usar el programa analítico como guía de ejes editoriales.",
    "Mantener README como entrada canónica de la asignatura."
  ],
  "activity_rules": [
    "Verificar instrucción específica de cada actividad antes de redactar.",
    "Rubricar cada entrega contra los ejes del programa analítico.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Incluir postura argumentada del estudiante.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Agregar fuentes específicas de actividad al .bib local antes de la versión final.",
    "No reutilizar reglas laterales sin comprobar pertinencia jurídica.",
    "No asumir fuentes de otras semanas o materias como aplicables.",
    "Confirmar que el producto corresponda a la consigna local."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de fusionar memoria.",
    "Aplicar union-dedupe sin eliminar reglas útiles previas.",
    "Comprobar que cada afirmación factual tenga fuente o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar metadatos de materia contra contenido entregado.",
    "Confirmar ausencia de contradicciones con reglas institucionales.",
    "Normalizar manualmente memorias heredadas no estructuradas.",
    "Revisar caracteres corruptos en README y plantilla antes de publicar.",
    "Validar que nombres de archivos no contengan variables sin resolver.",
    "Verificar que fuentes provisionales no aparezcan como bibliografía académica."
  ],
  "latex_rules": [
    "Usar plantilla .tex local como base de nuevas actividades.",
    "Conservar documentclass article con opciones spanish, letterpaper, oneside.",
    "Mantener compatibilidad con español y acentos correctos.",
    "Conservar macros institucionales de curso, universidad y asignatura.",
    "No eliminar campos de portada.",
    "Completar campos faltantes según actividad.",
    "Conservar bloque authortable de la plantilla al adaptar portada.",
    "Usar reporte-etapas-del-proceso-y-estrategia-del-litigio.tex para reportes.",
    "Usar presentacion-etapas-del-proceso-y-estrategia-del-litigio.tex si existe y aplica. [supuesto]",
    "No confiar en nombres generados con variables sin resolver.",
    "Resolver tokens tipo $(@{...}.Slug) antes de compilar.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Usar etapas-del-proceso-y-estrategia-del-litigio.bib como repositorio local.",
    "Conservar fuentes institucionales registradas.",
    "Conservar claves BibTeX unadmSitioWeb y unadmMallaDerecho2024.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Agregar entradas BibTeX específicas de actividad antes de citar.",
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "No citar bibliografía base si no fue usada en el argumento.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Incluir fecha de consulta en fuentes web o institucionales dinámicas.",
    "Validar correspondencia entre citas en texto y entradas .bib."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar reglas generales; mantener metadatos específicos en la materia local.",
    "Propagar a materias vecinas los ejes: problema, fundamento, análisis propio y conclusión.",
    "Propagar la restricción de no inventar fuentes.",
    "Propagar la regla de marcar supuestos.",
    "Propagar la regla de union-dedupe sin regresión.",
    "Propagar advertencia de normalización manual para memorias no parseables.",
    "Evitar transferir redacción literal entre nodos no equivalentes.",
    "Reutilizar patrones argumentativos, no contenidos temáticos ajenos.",
    "Conservar trazabilidad del ciclo y origen editorial."
  ],
  "open_questions": [
    "Confirmar si el autor de plantilla es definitivo o variable.",
    "Confirmar estilo de citación jurídica requerido.",
    "Confirmar código de curso oficial si difiere de LDE-S5B2. [supuesto]",
    "Confirmar existencia operativa de la plantilla de presentación. [supuesto]",
    "Corregir caracteres corruptos en README y validar nombres reales de archivos.",
    "Definir checklist mínimo por tipo de producto.",
    "Confirmar fuentes obligatorias por actividad.",
    "Confirmar rúbrica específica de cada actividad.",
    "Confirmar si las fuentes provisionales deben conservarse solo como nota técnica."
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
        "Semestre 5, bloque 2.",
        "Asignatura obligatoria de 8 créditos.",
        "Asignatura: Etapas del proceso y estrategia del litigio.",
        "Fuente curricular local: malla-curricular-derecho-unadm.pdf.",
        "Coursecode visible en plantilla: LDE-S5B2. [supuesto]"
      ]
    },
    "essence": [
      "Identidad UnADM.",
      "Enfoque jurídico aplicado.",
      "Problema jurídico o social claro.",
      "Fundamento normativo o doctrinal verificable.",
      "Análisis propio del estudiante.",
      "Conclusión jurídica transferible.",
      "Producto ajustado a consigna.",
      "Memoria persistente sin regresión."
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad y fundamento jurídico.",
      "Transformar planeación semanal en entregables verificables.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre.",
      "Vincular el aprendizaje con la práctica profesional.",
      "Sostener calidad editorial entre actividades y materias.",
      "Evitar propagación de errores estructurales."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Objetivo explícito.",
      "Bloques argumentativos visibles.",
      "Citas trazables.",
      "Supuestos marcados.",
      "Conclusión jurídica aplicable.",
      "Portada institucional completa.",
      "Lenguaje jurídico sobrio.",
      "Evitar relleno descriptivo.",
      "No trasladar redacción literal de otros nodos."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual -> marco normativo -> análisis propio -> conclusión.",
      "Afirmación -> evidencia verificable -> interpretación -> implicación práctica.",
      "Consigna -> producto esperado -> criterios de evaluación -> entrega final.",
      "Hecho relevante -> norma aplicable -> razonamiento jurídico -> postura.",
      "Fuente institucional -> dato curricular -> metadato de portada.",
      "Supuesto -> verificación pendiente -> uso limitado."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Licenciatura en Derecho",
        "Etapas del proceso",
        "Estrategia del litigio",
        "Problema jurídico",
        "Conceptos jurídicos pertinentes",
        "Marco normativo",
        "Doctrina jurídica",
        "Evidencia verificable",
        "Análisis propio",
        "Postura académica",
        "Conclusión jurídica transferible",
        "Producto solicitado",
        "Planeación semanal",
        "Normalización estructurada",
        "JSON parseable",
        "Union-dedupe sin regresión",
        "Fuentes provisionales",
        "Archivo .bib local",
        "Plantilla LaTeX local"
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
          "justification": "La pauta local exige identidad institucional, citas verificables y criterio propio."
        },
        {
          "source": "Malla curricular",
          "target": "Contexto curricular",
          "kind": "supports",
          "justification": "README local la declara como fuente de semestre, bloque, tipo y créditos."
        },
        {
          "source": "Programa analítico",
          "target": "Cinco ejes editoriales",
          "kind": "develops",
          "justification": "El programa enumera problema, conceptos, producto, análisis y conclusión."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Estructura de entrega",
          "kind": "develops",
          "justification": "Los ejes organizan el desarrollo de reportes, presentaciones y productos visuales."
        },
        {
          "source": "Problema jurídico",
          "target": "Marco normativo",
          "kind": "depends_on",
          "justification": "La selección normativa depende del problema que activa la actividad."
        },
        {
          "source": "Marco normativo",
          "target": "Análisis propio",
          "kind": "supports",
          "justification": "El razonamiento jurídico debe apoyarse en normas, doctrina o datos pertinentes."
        },
        {
          "source": "Evidencia verificable",
          "target": "Postura académica",
          "kind": "supports",
          "justification": "La postura propia no debe quedar como opinión sin respaldo."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "develops",
          "justification": "El cierre debe derivarse del razonamiento previo y proyectarse a la práctica."
        },
        {
          "source": "Archivo .bib local",
          "target": "Citas trazables",
          "kind": "supports",
          "justification": "Las entradas BibTeX locales permiten verificar las fuentes usadas."
        },
        {
          "source": "JSON parseable",
          "target": "Propagación recursiva segura",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay fusión confiable de memoria."
        },
        {
          "source": "Union-dedupe sin regresión",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Permite comprimir sin borrar reglas útiles previas."
        },
        {
          "source": "Fuentes provisionales",
          "target": "Autoridad académica",
          "kind": "contrasts",
          "justification": "Las fuentes no verificadas solo sirven como nota técnica."
        },
        {
          "source": "Plantilla LaTeX local",
          "target": "Portada institucional",
          "kind": "develops",
          "justification": "La plantilla contiene macros institucionales que deben conservarse."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 5, bloque 2, obligatoria, 8 créditos.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: integridad académica, citas verificables y conclusión jurídica.",
        "Programa analítico local: claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: reportes, presentaciones y productos visuales.",
        "Programa analítico local: cinco ejes de trabajo.",
        "Bib local: unadmSitioWeb.",
        "Bib local: unadmMallaDerecho2024.",
        "Plantilla .tex local: documenttitle, coursename, coursecode y universityname.",
        "Plantilla .tex local: coursecode LDE-S5B2.",
        "Memoria institucional heredada: revisar respuestas no estructuradas antes de aplicar aguas abajo."
      ]
    },
    "reinforcement_log": [
      "Ciclo 18 conserva reglas válidas del destino.",
      "Ciclo 18 agrega solo abstracciones transversales del origen.",
      "Ciclo 18 excluye bibliografía temática de Filosofía del Derecho por no ser equivalente.",
      "Ciclo 18 refuerza no inventar fuentes.",
      "Ciclo 18 corrige propagación hacia relaciones con tipos permitidos.",
      "Ciclo 18 mantiene normalización JSON como gate central.",
      "Ciclo 18 preserva union-dedupe sin regresión.",
      "Ciclo 18 marca supuestos de plantilla y coursecode.",
      "Ciclo 18 mantiene foco local en Etapas del proceso y estrategia del litigio.",
      "Ciclo 18 refuerza conclusión jurídica aplicable a práctica profesional."
    ]
  }
}