{
  "summary": [
    "Ciclo 19 consolida memoria transversal para materia destino.",
    "Se preserva identidad UnADM y enfoque jurídico aplicado.",
    "Se transfieren solo abstracciones editoriales estables del origen.",
    "Se evita copiar redacción literal de actividades no equivalentes.",
    "Se mantiene compresión por unión-dedupe sin regresión.",
    "Se exige JSON parseable antes de cualquier propagación.",
    "Se separan fuentes provisionales de autoridad académica.",
    "Se confirma contexto local: semestre 5, bloque 2, obligatoria, 8 créditos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho.",
    "Usar contexto local: semestre 5, bloque 2, obligatoria, 8 créditos.",
    "Usar tono académico-jurídico formal y claro.",
    "Exigir postura propia sustentada.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Conservar trazabilidad de origen editorial al consolidar memoria.",
    "Marcar como [supuesto] todo dato no visible en documentos locales.",
    "Registrar fuentes provisionales como nota técnica, no como autoridad académica.",
    "Usar macros de portada: documenttitle, coursename, coursecode, universityname.",
    "Usar coursecode LDE-S5B2 mientras no exista corrección institucional. [supuesto]",
    "Mantener autor de plantilla salvo instrucción de actividad o docente. [supuesto]"
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Desarrollar conceptos, normas, doctrina o datos pertinentes al caso.",
    "Alinear la entrega al producto solicitado por la planeación.",
    "Adaptar formato a reporte, presentación o producto visual.",
    "Incluir análisis propio antes del cierre.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener README como entrada canónica de la asignatura.",
    "Usar programa analítico como guía de ejes editoriales.",
    "Aplicar cinco ejes: problema, conceptos, producto, análisis propio, conclusión."
  ],
  "activity_rules": [
    "Verificar instrucción específica de cada actividad antes de redactar.",
    "Rubricar cada entrega contra los ejes del programa analítico.",
    "Confirmar producto exacto solicitado antes de elegir plantilla.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Agregar fuentes específicas de actividad al .bib local antes de versión final.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Incluir conclusión jurídica con criterio propio.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No reutilizar reglas laterales sin comprobar pertinencia jurídica.",
    "No asumir fuentes de otra actividad como fuentes de esta materia."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de fusionar memoria.",
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Comprobar unión-dedupe sin eliminar reglas útiles previas.",
    "Revisar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar ausencia de contradicciones con reglas institucionales.",
    "Comprobar que cada afirmación factual tenga fuente o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar consistencia entre metadatos de materia y contenido entregado.",
    "Verificar correspondencia del producto con la consigna local.",
    "Revisar caracteres corruptos en README y plantilla antes de publicar. [supuesto]",
    "Validar que nombres de archivos no contengan variables sin resolver."
  ],
  "latex_rules": [
    "Usar plantilla .tex local como base de nuevas actividades.",
    "Usar reporte-etapas-del-proceso-y-estrategia-del-litigio.tex para reportes.",
    "Usar presentación local solo si existe en carpeta. [supuesto]",
    "Conservar macros institucionales de curso, universidad y asignatura.",
    "No eliminar campos de portada; completar faltantes según actividad.",
    "Mantener compatibilidad con español y formato letterpaper.",
    "Usar documentclass article con opciones spanish, letterpaper, oneside.",
    "Conservar bloque authortable al adaptar portada.",
    "Usar codificación y acentos correctos en .tex y .bib.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Mantener claves BibTeX estables.",
    "Compilar sin errores críticos ni referencias rotas.",
    "No confiar en nombres generados con variables sin resolver.",
    "Resolver tokens tipo $(@{...}.Slug) antes de compilar o citar archivos.",
    "Verificar nombres reales del README antes de referenciarlos."
  ],
  "bibliography_rules": [
    "Usar etapas-del-proceso-y-estrategia-del-litigio.bib como repositorio local.",
    "Conservar claves BibTeX unadmSitioWeb y unadmMallaDerecho2024.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Agregar entradas BibTeX específicas de actividad antes de citar.",
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "No citar bibliografía base si no fue usada en el argumento.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Incluir fecha de consulta en fuentes web o institucionales dinámicas.",
    "Validar que toda cita textual o paráfrasis tenga entrada .bib.",
    "No trasladar bibliografía del origen si no corresponde a la actividad destino."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo tras validar JSON y estructura.",
    "Propagar reglas generales; mantener metadatos específicos en la materia local.",
    "Propagar validación JSON y control de no regresión.",
    "Propagar unión-dedupe sin eliminar reglas útiles previas.",
    "Propagar restricción de no inventar fuentes.",
    "Propagar cinco ejes editoriales a materias vecinas de Derecho.",
    "Evitar propagar citas o casos específicos de Filosofía del Derecho.",
    "Usar abstracciones, no redacción literal, entre nodos no equivalentes.",
    "Normalizar manualmente memorias heredadas no parseables.",
    "Conservar advertencia: ciclo 1 requiere normalización manual si se reutiliza."
  ],
  "open_questions": [
    "Confirmar estilo de citación jurídica requerido: APA, Chicago, ISO 690 u otro.",
    "Confirmar si documentauthor es fijo de plantilla o variable por estudiante.",
    "Confirmar código de curso oficial; plantilla usa LDE-S5B2. [supuesto]",
    "Confirmar existencia operativa de presentación local. [supuesto]",
    "Corregir nombres corruptos en README y validar archivos reales. [supuesto]",
    "Confirmar si fuente provisional Codex debe conservarse solo como nota técnica.",
    "Definir checklist mínimo por tipo de producto: reporte, presentación y visual.",
    "Confirmar rúbricas específicas de actividades futuras.",
    "Confirmar fuentes obligatorias de cada semana antes de redactar.",
    "Confirmar si habrá bibliografía procesal base adicional en .bib local."
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
        "Trazabilidad editorial en cada consolidación."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Etapas del proceso y estrategia del litigio.",
        "Semestre 5, bloque 2.",
        "Asignatura obligatoria de 8 créditos.",
        "Fuente curricular local: malla-curricular-derecho-unadm.pdf.",
        "Coursecode visible en plantilla: LDE-S5B2. [supuesto]"
      ]
    },
    "essence": [
      "Identidad UnADM.",
      "Fundamento jurídico verificable.",
      "Problema jurídico o social claro.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeación.",
      "Análisis propio y postura académica.",
      "Conclusión jurídica transferible.",
      "Estrategia de litigio aplicada.",
      "Normalización estructurada.",
      "Unión-dedupe sin regresión."
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, fundamento jurídico y evidencia.",
      "Transformar planeación semanal en reportes, presentaciones o productos visuales.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Conectar teoría procesal y práctica profesional.",
      "Garantizar memoria editorial persistente y verificable.",
      "Evitar propagación de errores estructurales o fuentes no verificadas."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Objetivo explícito.",
      "Bloques argumentativos visibles.",
      "Citas trazables.",
      "Postura propia sustentada.",
      "Lenguaje jurídico sobrio.",
      "Cierre jurídico aplicable.",
      "Supuestos marcados.",
      "Metadatos institucionales completos.",
      "Sin redacción literal transferida entre nodos no equivalentes."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual y normativo -> análisis propio -> conclusión jurídica.",
      "Afirmación -> evidencia verificable -> interpretación -> implicación práctica.",
      "Consigna -> producto esperado -> estructura -> checklist de cumplimiento.",
      "Norma -> doctrina -> aplicación al caso -> estrategia procesal.",
      "Dato local -> marca de fuente -> uso limitado -> no extrapolación.",
      "Memoria heredada -> normalización -> validación JSON -> propagación segura.",
      "Concepto general -> pertinencia local -> adaptación sin copia literal."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Licenciatura en Derecho",
        "Etapas del proceso",
        "Estrategia del litigio",
        "Problema jurídico",
        "Marco normativo",
        "Doctrina jurídica",
        "Evidencia verificable",
        "Análisis propio",
        "Postura académica",
        "Conclusión jurídica transferible",
        "Práctica profesional",
        "Producto solicitado",
        "Programa analítico",
        "Carpeta canónica",
        "Bibliografía local",
        "Citas trazables",
        "JSON parseable",
        "Normalización estructurada",
        "Unión-dedupe sin regresión",
        "Fuente provisional",
        "Supuesto editorial"
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
          "source": "Programa analítico",
          "target": "Cinco ejes editoriales",
          "kind": "develops",
          "justification": "El programa define problema, conceptos, producto, análisis propio y conclusión."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Estructura de entrega",
          "kind": "supports",
          "justification": "Los ejes ordenan el desarrollo de reportes, presentaciones y productos visuales."
        },
        {
          "source": "Problema jurídico",
          "target": "Marco normativo",
          "kind": "depends_on",
          "justification": "El marco se selecciona según el problema planteado."
        },
        {
          "source": "Marco normativo",
          "target": "Análisis propio",
          "kind": "supports",
          "justification": "El análisis debe partir de normas, doctrina o datos pertinentes."
        },
        {
          "source": "Evidencia verificable",
          "target": "Postura académica",
          "kind": "supports",
          "justification": "La postura propia requiere respaldo trazable."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "develops",
          "justification": "El cierre debe derivar del razonamiento y servir a la práctica profesional."
        },
        {
          "source": "Bibliografía local",
          "target": "Citas trazables",
          "kind": "supports",
          "justification": "El archivo .bib local permite consistencia entre citas y fuentes."
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
          "justification": "La normalización evita reutilizar salidas no estructuradas."
        },
        {
          "source": "Unión-dedupe sin regresión",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Permite compresión lossless sin borrar reglas útiles previas."
        },
        {
          "source": "Fuente provisional",
          "target": "Autoridad académica",
          "kind": "contrasts",
          "justification": "Las fuentes heredadas no verificadas no deben usarse como autoridad académica."
        },
        {
          "source": "Transferencia transversal",
          "target": "Redacción literal de actividad",
          "kind": "contrasts",
          "justification": "Entre nodos no equivalentes se transfieren abstracciones, no textos específicos."
        },
        {
          "source": "Carpeta canónica",
          "target": "Plantillas locales",
          "kind": "supports",
          "justification": "El README local identifica archivos base y pauta editorial."
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
        "Plantilla local: macros documenttitle, coursename, coursecode y universityname.",
        "Plantilla local: coursecode LDE-S5B2.",
        "Herencia institucional: salida no JSON parseable requiere normalización.",
        "Regla persistente: no inventar fuentes.",
        "Regla persistente: validar citas contra .bib."
      ]
    },
    "reinforcement_log": [
      "Ciclo 19 preserva reglas útiles previas sin recorte.",
      "Se deduplican formulaciones equivalentes.",
      "Se corrigen relaciones del grafo a tipos permitidos.",
      "Se refuerza transferencia por abstracciones entre nodos no equivalentes.",
      "Se excluyen citas específicas del origen no pertinentes al destino.",
      "Se conserva advertencia de fuentes provisionales heredadas.",
      "Se mantiene validación JSON como gate de propagación.",
      "Se refuerza correspondencia entre consigna, producto y cierre jurídico.",
      "Se preserva bibliografía local verificable.",
      "Se dejan abiertos vacíos de estilo de citación, autor y plantillas."
    ]
  }
}