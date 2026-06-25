{
  "summary": [
    "Materia destino consolidada con identidad UnADM y enfoque jurídico aplicado.",
    "Ciclo 11 sincroniza abstracciones editoriales estables desde actividad transversal.",
    "Se preserva compresión por unión-dedupe sin pérdida y sin regresión.",
    "Se mantiene validación JSON parseable antes de toda propagación.",
    "La herencia no estructurada previa queda marcada como provisional y normalizada.",
    "El destino conserva contexto local: Licenciatura en Derecho, semestre 5, bloque 2, obligatoria, 8 créditos.",
    "La transferencia no copia redacción ni fuentes específicas de Filosofía del Derecho."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 2, obligatoria, 8 créditos.",
    "Usar tono académico-jurídico formal, claro y verificable.",
    "Exigir postura propia sustentada en cada producto.",
    "Conservar trazabilidad de origen editorial al consolidar memoria.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Usar macros de portada: documenttitle, coursename, coursecode y universityname.",
    "Usar coursecode visible en plantilla: LDE-S5B2; confirmar valor institucional. [supuesto]",
    "Mantener autor de plantilla Martin Jonathan de la Cruz salvo instrucción de actividad o docente. [supuesto]",
    "Marcar como [supuesto] todo dato no visible en consigna o documentos locales.",
    "Registrar fuentes provisionales como nota técnica y no como autoridad académica.",
    "No trasladar metadatos curriculares de materias laterales no equivalentes."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar bloques: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Desarrollar conceptos, normas, doctrina o datos pertinentes al caso.",
    "Alinear la estructura al producto solicitado en la planeación semanal.",
    "Adaptar salida al producto pedido: reporte, presentación o material visual.",
    "Mantener README como entrada canónica de la asignatura.",
    "Usar el programa analítico como guía de ejes editoriales.",
    "Seguir cinco ejes: problema, conceptos, producto solicitado, análisis propio y conclusión transferible.",
    "Cerrar con conclusión jurídica aplicable a la práctica profesional."
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
    "Agregar fuentes específicas de actividad al .bib local antes de redactar versión final.",
    "No reutilizar reglas laterales sin comprobar pertinencia jurídica.",
    "No asumir que fuentes de otra materia corresponden a esta asignatura."
  ],
  "quality_gates": [
    "Validar JSON parseable en toda memoria antes de propagar.",
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de fusionar memoria.",
    "Aplicar unión-dedupe sin eliminar reglas útiles previas.",
    "Confirmar ausencia de contradicciones con reglas institucionales heredadas.",
    "Revisar consistencia entre metadatos de materia y contenido entregado.",
    "Comprobar que cada afirmación factual tenga fuente o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar respuestas no estructuradas antes de aplicarlas aguas abajo.",
    "Normalizar manualmente memorias provenientes de salida no parseable.",
    "Revisar caracteres corruptos en README y plantilla antes de publicar. [supuesto]",
    "Validar que nombres de archivos no contengan variables sin resolver."
  ],
  "latex_rules": [
    "Usar la plantilla .tex local de la materia como base de nuevas actividades.",
    "Usar reporte-etapas-del-proceso-y-estrategia-del-litigio.tex para reportes.",
    "Usar presentacion-etapas-del-proceso-y-estrategia-del-litigio.tex para presentaciones si existe y compila. [supuesto]",
    "Conservar macros institucionales de curso, universidad y asignatura.",
    "No eliminar campos de portada; completar faltantes según actividad.",
    "Conservar bloque authortable de la plantilla al adaptar portada.",
    "Mantener documentclass article con opciones spanish, letterpaper y oneside salvo consigna distinta.",
    "Mantener compatibilidad con español y acentos correctos en .tex y .bib.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "No confiar en nombres generados con variables sin resolver en README o markdown.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) antes de compilar o documentar.",
    "Corregir caracteres anómalos en rutas o nombres antes de referenciarlos.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas."
  ],
  "bibliography_rules": [
    "Usar etapas-del-proceso-y-estrategia-del-litigio.bib como repositorio local.",
    "Conservar fuentes institucionales registradas: sitio UnADM y malla curricular Derecho.",
    "Conservar claves BibTeX locales unadmSitioWeb y unadmMallaDerecho2024.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Agregar entradas BibTeX específicas de actividad antes de citar.",
    "No inventar referencias.",
    "Usar solo obras realmente consultadas o consultables.",
    "No citar bibliografía base si no fue usada en el argumento.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Incluir fecha de consulta cuando la fuente sea web o institucional dinámica.",
    "No trasladar bibliografía específica de Filosofía del Derecho sin uso real en esta materia."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar arriba y laterales la regla de unión-dedupe sin regresión.",
    "Propagar la restricción de no inventar fuentes.",
    "Propagar reglas generales; mantener metadatos específicos en la materia destino.",
    "Propagar a materias de Derecho los ejes: problema, fundamento, análisis propio y conclusión jurídica.",
    "Compartir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Evitar transferir redacción literal de actividades laterales.",
    "No propagar fuentes específicas de otra materia como autoridad local.",
    "Conservar advertencia de normalización manual para ciclos con salida no parseable.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local."
  ],
  "open_questions": [
    "Confirmar si documentauthor debe ser fijo de plantilla o variable por estudiante.",
    "Confirmar código de curso institucional: plantilla usa LDE-S5B2. [supuesto]",
    "Confirmar estilo de citación jurídica requerido: APA, Chicago, ISO 690 u otro.",
    "Confirmar existencia operativa de presentacion-etapas-del-proceso-y-estrategia-del-litigio.tex. [supuesto]",
    "Corregir nombres corruptos en README y validar nombres reales de archivos. [supuesto]",
    "Confirmar si la fuente provisional Codex debe conservarse solo como nota técnica.",
    "Definir checklist mínimo por tipo de producto: reporte, presentación y material visual.",
    "Confirmar rúbricas específicas de actividades futuras.",
    "Confirmar fuentes obligatorias por semana o unidad.",
    "Confirmar si cada actividad requiere .bib propio o solo repositorio local acumulativo."
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
        "Fuentes provisionales separadas de autoridad académica.",
        "Trazabilidad editorial en cada consolidación."
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
      "Problema jurídico o social claro.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeación.",
      "Análisis propio y postura académica.",
      "Conclusión jurídica transferible.",
      "Fundamento verificable.",
      "Estrategia de litigio orientada a práctica profesional.",
      "Normalización estructurada antes de propagar.",
      "Unión-dedupe sin regresión."
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
      "Transformar la planeación semanal en reportes, presentaciones y productos visuales.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Formar criterio jurídico aplicado a etapas procesales y estrategia de litigio.",
      "Evitar productos descriptivos sin postura ni sustento.",
      "Preservar memoria editorial persistente segura y reutilizable."
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
      "Metadatos institucionales completos.",
      "Lenguaje académico sin relleno."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis propio -> conclusión jurídica.",
      "Afirmación -> evidencia verificable -> interpretación -> implicación práctica.",
      "Hecho o consigna -> cuestión jurídica -> criterio del estudiante -> consecuencia procesal.",
      "Concepto jurídico -> fuente -> aplicación al caso -> límite o advertencia.",
      "Planeación semanal -> producto solicitado -> estructura mínima -> revisión por rúbrica.",
      "Supuesto -> verificación pendiente -> uso provisional limitado.",
      "Memoria heredada -> normalización -> deduplicación -> propagación segura."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Licenciatura en Derecho",
        "Etapas del proceso",
        "Estrategia del litigio",
        "Problema jurídico o social",
        "Marco normativo",
        "Doctrina jurídica",
        "Evidencia verificable",
        "Análisis propio",
        "Postura académica",
        "Conclusión jurídica transferible",
        "Producto solicitado",
        "Programa analítico",
        "Carpeta canónica de asignatura",
        "Bibliografía local",
        "JSON parseable",
        "Normalización estructurada",
        "Unión-dedupe sin regresión",
        "Fuente provisional",
        "Supuesto marcado"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad académica con citas verificables",
          "kind": "supports",
          "justification": "La pauta local exige identidad institucional, integridad académica y citas verificables."
        },
        {
          "source": "Programa analítico",
          "target": "Cinco ejes editoriales",
          "kind": "develops",
          "justification": "El programa define problema, conceptos, producto, análisis propio y conclusión transferible."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Estructura de entrega",
          "kind": "develops",
          "justification": "Los ejes organizan la construcción de reportes, presentaciones y productos visuales."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Marco normativo",
          "kind": "depends_on",
          "justification": "El fundamento normativo se selecciona según el problema planteado."
        },
        {
          "source": "Marco normativo",
          "target": "Análisis propio",
          "kind": "supports",
          "justification": "La interpretación del estudiante debe apoyarse en normas, doctrina o datos pertinentes."
        },
        {
          "source": "Evidencia verificable",
          "target": "Postura académica",
          "kind": "supports",
          "justification": "La postura propia requiere respaldo explícito y trazable."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "develops",
          "justification": "El cierre debe derivar del razonamiento y proyectarse a la práctica profesional."
        },
        {
          "source": "Bibliografía local",
          "target": "Citas trazables",
          "kind": "supports",
          "justification": "El archivo .bib local conserva las fuentes usadas en cada actividad."
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
          "justification": "La normalización permite consolidar reglas útiles sin ambigüedad."
        },
        {
          "source": "Unión-dedupe sin regresión",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "La compresión conserva reglas válidas y elimina redundancias."
        },
        {
          "source": "Fuente provisional",
          "target": "Supuesto marcado",
          "kind": "depends_on",
          "justification": "Toda fuente heredada no verificada debe limitarse y marcarse."
        },
        {
          "source": "Transferencia transversal",
          "target": "Abstracciones editoriales estables",
          "kind": "depends_on",
          "justification": "Entre materias no equivalentes se comparten patrones, no redacción literal ni fuentes específicas."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 5, bloque 2, obligatoria, 8 créditos.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: integridad académica, citas verificables y conclusión jurídica con criterio propio.",
        "Programa analítico local: claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: reportes, presentaciones y productos visuales.",
        "Programa analítico local: cinco ejes de trabajo.",
        "Bib local: unadmSitioWeb.",
        "Bib local: unadmMallaDerecho2024.",
        "Plantilla .tex local: macros de portada institucional.",
        "Plantilla .tex local: coursecode LDE-S5B2.",
        "Memoria heredada: salida no JSON parseable requiere normalización.",
        "Regla consolidada: bloquear propagación si la salida no es JSON parseable.",
        "Regla consolidada: aplicar unión-dedupe sin eliminar reglas útiles previas."
      ]
    },
    "reinforcement_log": [
      "Ciclo 11 conserva reglas locales válidas y elimina duplicados semánticos.",
      "Ciclo 11 refuerza identidad UnADM sin importar redacción específica del origen.",
      "Ciclo 11 transfiere solo patrones estables desde Filosofía del Derecho.",
      "Ciclo 11 excluye fuentes específicas del origen por no estar verificadas para esta materia.",
      "Ciclo 11 mantiene metadatos curriculares locales del destino.",
      "Ciclo 11 fortalece gates de JSON parseable, normalización y no regresión.",
      "Ciclo 11 corrige el grafo para usar relaciones permitidas.",
      "Ciclo 11 deja abiertas verificaciones de plantilla, citación y archivos corruptos."
    ]
  }
}