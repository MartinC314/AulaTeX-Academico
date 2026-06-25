{
  "summary": [
    "Sincronización transversal desde Filosofía del Derecho hacia Derecho fiscal y tributario.",
    "Se transfieren solo abstracciones editoriales estables.",
    "Se conserva identidad UnADM y contexto local de la materia destino.",
    "Se refuerza estructura reusable: problema, conceptos, normas, análisis propio y conclusión.",
    "Se mantiene compresión por unión y deduplicación sin regresión.",
    "Se normalizan herencias no JSON antes de cualquier propagación.",
    "No se transfiere bibliografía temática de Filosofía como obligatoria para Fiscal.",
    "Supuesto: la herencia institucional es válida si no contradice el contexto local."
  ],
  "identity_rules": [
    "Conservar identidad UnADM en portada, tono, metadatos y contexto.",
    "Usar datos locales: Derecho fiscal y tributario, semestre 6, bloque 1, obligatoria, 8 créditos.",
    "Usar clave de curso LDE-S6B1 cuando aplique.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Marcar como provisional toda fuente heredada no específica de la materia.",
    "Citar malla-curricular-derecho-unadm.pdf solo para ubicación curricular.",
    "Verificar datos personales antes de entrega final.",
    "Verificar figura docente antes de entrega final.",
    "Autor base en plantilla: Martin Jonathan de la Cruz; matrícula ES2611202040; verificar antes de compartir.",
    "Fuente provisional heredada: Codex desde ingeniería en sistemas computacionales.",
    "Fuente provisional heredada: GPT-Pro desde Actividad 1.",
    "Fuente provisional heredada: Auto model-router desde Actividad 1."
  ],
  "structure_rules": [
    "Usar README de la materia como punto de entrada canónico.",
    "Usar programa analítico como guía editorial local.",
    "Alinear cada entrega con problema, conceptos o normas, producto, análisis propio y conclusión.",
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna.",
    "Alinear el producto final con la planeación semanal y la consigna.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener separación entre reporte .tex, presentación .tex y .bib local.",
    "Mantener estructura local: reporte, presentación, bibliografía, programa analítico y carpeta de referencias.",
    "Corregir rutas truncadas o rotas en README antes de publicar.",
    "Resolver slug .bib dinámico sin expandir en README y programa analítico."
  ],
  "activity_rules": [
    "Incluir problema jurídico o social explícito al inicio.",
    "Incluir conceptos, normas, doctrina o datos pertinentes.",
    "Desarrollar el producto solicitado por la planeación.",
    "Incluir análisis propio con postura académica.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Evitar entregas solo descriptivas.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Vincular argumentos fiscales y tributarios con aplicación profesional concreta.",
    "Cerrar con conclusión jurídica transferible a la práctica.",
    "No asumir fuentes de actividades o semanas distintas sin confirmación local."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de guardar memoria.",
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar respuestas no estructuradas antes de reutilizarlas.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Verificar consistencia entre metadatos de portada y programa analítico.",
    "Confirmar semestre, bloque, tipo y créditos contra la malla curricular local.",
    "Revisar que no existan placeholders sin resolver en README, .tex o .bib.",
    "Comprobar que toda cita usada tenga entrada bibliográfica verificable.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar integridad de .tex para compilación.",
    "Verificar cierre correcto de entornos LaTeX.",
    "Corregir rutas con caracteres anómalos antes de publicar.",
    "Verificar que el producto corresponda a la consigna de la actividad."
  ],
  "latex_rules": [
    "Completar campos pendientes de plantilla antes de compilar.",
    "Mantener variables institucionales y de curso consistentes en el preámbulo.",
    "Usar español y formato carta según plantilla base.",
    "Actualizar título, subtítulo y actividad antes de cada entrega.",
    "Conservar portada institucional con UnADM y Licenciatura en Derecho.",
    "Sustituir placeholders generados por expresiones de plantilla.",
    "Reemplazar título y subtítulo base por los de la actividad real.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir captura incompleta del bloque authortable antes de compilar.",
    "Cerrar correctamente todos los entornos tabular.",
    "Cerrar correctamente el documento LaTeX.",
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Verificar nombres de archivos del README antes de referenciarlos."
  ],
  "bibliography_rules": [
    "Registrar fuentes específicas de actividad en derecho-fiscal-y-tributario.bib.",
    "Priorizar fuentes institucionales UnADM.",
    "Priorizar normas jurídicas verificables.",
    "Priorizar documentos normativos verificables para argumentos fiscales.",
    "Usar unadmSitioWeb y unadmMallaDerecho2024 cuando sean pertinentes.",
    "Citar la malla curricular local solo para datos curriculares.",
    "Agregar doctrina, legislación o jurisprudencia solo si la actividad lo exige.",
    "No inventar referencias.",
    "Usar solo obras consultables.",
    "Marcar fuente pendiente cuando falte dato verificable.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "No asumir bibliografía temática de Filosofía como base obligatoria de Fiscal."
  ],
  "propagation_hints": [
    "Propagar hacia arriba y laterales solo tras normalización JSON.",
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Conservar regla de sin regresión en ciclos siguientes.",
    "Mantener unión-deduplicación como método de compresión.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Propagar reglas generales de identidad UnADM a materias laterales.",
    "No propagar datos específicos de Derecho fiscal y tributario a materias no equivalentes.",
    "No propagar bibliografía local como obligatoria fuera del nodo destino.",
    "Aplicar normalización manual si la entrada heredada es ambigua.",
    "Ciclo 1 necesita normalización manual si se reutiliza.",
    "Ciclos posteriores deben priorizar mejoras verificables del contexto local antes de lateralizar."
  ],
  "open_questions": [
    "Confirmar figura docente en plantilla.",
    "Confirmar si el autor y matrícula deben permanecer en plantillas compartidas.",
    "Confirmar formato de citación requerido por la asignatura.",
    "Confirmar si se requiere bibliografía fiscal base adicional.",
    "Confirmar fuentes obligatorias por actividad.",
    "Confirmar producto exacto de cada actividad: reporte, presentación u otro formato.",
    "Confirmar rúbrica de evaluación específica.",
    "Resolver expresiones PowerShell sin expandir en README y programa analítico para el slug .bib.",
    "Corregir rutas truncadas en README para reporte y referencias.",
    "Cerrar correctamente el bloque authortable y el documento LaTeX del reporte.",
    "Supuesto: la entrada .bib local será derecho-fiscal-y-tributario.bib en todas las actividades.",
    "Confirmar si fuentes provisionales heredadas siguen vigentes para Derecho fiscal y tributario."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Sobrio y profesional.",
        "Orientado a evidencia verificable."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Portada institucional consistente.",
        "Entrada canónica en carpeta de asignatura.",
        "Supuestos etiquetados."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Derecho fiscal y tributario.",
        "Semestre 6, bloque 1, obligatoria, 8 créditos.",
        "Clave local LDE-S6B1.",
        "Ubicación curricular respaldada por malla institucional."
      ]
    },
    "essence": [
      "Problema jurídico o social que activa la asignatura.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Marco normativo fiscal y tributario verificable.",
      "Producto solicitado por la planeación.",
      "Análisis propio y postura académica.",
      "Conclusión transferible a la práctica jurídica.",
      "Identidad institucional UnADM.",
      "Integridad académica.",
      "Consistencia entre .tex y .bib.",
      "Trazabilidad de fuentes."
    ],
    "reason_for_being": [
      "Transformar la planeación semanal en productos académicos claros.",
      "Integrar problema, fuentes, análisis propio y cierre argumentativo.",
      "Aterrizar argumentos fiscales y tributarios en aplicación profesional.",
      "Evitar entregas descriptivas sin criterio jurídico.",
      "Sostener conclusiones con normas, doctrina o datos verificables.",
      "Mantener una memoria editorial reutilizable para actividades futuras."
    ],
    "style_markers": [
      "Supuestos siempre etiquetados.",
      "Sin afirmaciones sin fuente.",
      "Secciones funcionales.",
      "Cierre profesional transferible.",
      "Sin contenido de relleno descriptivo.",
      "Metadatos curriculares consistentes.",
      "Lenguaje jurídico preciso.",
      "Citas verificables.",
      "Rutas y archivos normalizados.",
      "No trasladar redacción literal entre materias no equivalentes."
    ],
    "argumentative_patterns": [
      "Problema inicial breve y concreto.",
      "Objetivo puntual antes del desarrollo.",
      "Marco conceptual delimitado.",
      "Marco normativo o doctrinal explícito.",
      "Contraste de fuentes cuando existan posturas relevantes.",
      "Postura propia sustentada.",
      "Aplicación fiscal o tributaria concreta.",
      "Conclusión jurídica derivada del análisis.",
      "Coherencia entre pregunta guía, desarrollo y cierre.",
      "Transferencia a práctica profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Licenciatura en Derecho",
        "Derecho fiscal y tributario",
        "Ubicación curricular",
        "Malla curricular de Derecho",
        "Problema jurídico",
        "Problema social",
        "Conceptos jurídicos",
        "Normas jurídicas",
        "Doctrina",
        "Datos pertinentes",
        "Marco normativo",
        "Análisis propio",
        "Postura académica",
        "Conclusión transferible",
        "Aplicación profesional",
        "Integridad académica",
        "Citas verificables",
        "Bibliografía local",
        "Consistencia .tex/.bib",
        "Normalización JSON",
        "Propagación recursiva",
        "Compresión unión-dedupe",
        "Supuestos explícitos",
        "Rutas canónicas",
        "Placeholders sin resolver"
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
          "justification": "La pauta institucional exige formato consistente y fuentes verificables."
        },
        {
          "source": "Ubicación curricular",
          "target": "Malla curricular de Derecho",
          "kind": "depends_on",
          "justification": "Los datos de semestre, bloque, tipo y créditos deben verificarse con fuente local."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "supports",
          "justification": "La postura académica requiere partir de un conflicto definido."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica necesita fundamento normativo explícito."
        },
        {
          "source": "Citas verificables",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Toda afirmación sustantiva debe tener respaldo o marca de supuesto."
        },
        {
          "source": "Bibliografía local",
          "target": "Consistencia .tex/.bib",
          "kind": "supports",
          "justification": "Las citas del documento deben corresponder con entradas BibTeX verificables."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia segura entre nodos."
        },
        {
          "source": "Compresión unión-dedupe",
          "target": "Sin regresión editorial",
          "kind": "supports",
          "justification": "La deduplicación conserva reglas útiles sin recortar memoria válida."
        },
        {
          "source": "Supuestos explícitos",
          "target": "Trazabilidad de fuentes",
          "kind": "supports",
          "justification": "Los datos no visibles deben distinguirse de los verificados."
        },
        {
          "source": "Placeholders sin resolver",
          "target": "Compilación LaTeX",
          "kind": "contrasts",
          "justification": "Los tokens y bloques truncados impiden una entrega limpia."
        },
        {
          "source": "Filosofía del Derecho",
          "target": "Derecho fiscal y tributario",
          "kind": "develops",
          "justification": "Solo aporta patrón metodológico transversal: problema, conceptos, fuentes, análisis y cierre."
        },
        {
          "source": "Derecho fiscal y tributario",
          "target": "Aplicación profesional",
          "kind": "develops",
          "justification": "Las actividades deben conectar argumentos fiscales y tributarios con práctica jurídica concreta."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 6, bloque 1, obligatoria, 8 créditos.",
        "README local: fuente curricular malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: identidad UnADM, integridad académica, citas verificables y conclusión jurídica.",
        "Programa analítico local: claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
        "Programa analítico local: fuentes específicas por actividad en derecho-fiscal-y-tributario.bib.",
        "Bib local: unadmSitioWeb.",
        "Bib local: unadmMallaDerecho2024.",
        "Reporte local: plantilla base con curso Derecho fiscal y tributario.",
        "Reporte local: coursecode LDE-S6B1.",
        "Reporte local: authortable contiene figura docente por definir.",
        "Reporte local: captura truncada del bloque authortable.",
        "Origen transversal: patrón editorial problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
        "Origen transversal: bloquear propagación si la salida no es JSON parseable.",
        "Origen transversal: validar consistencia entre citas en texto y archivo .bib.",
        "Supuesto: no se transfiere bibliografía temática de Filosofía como obligatoria en Fiscal."
      ]
    },
    "reinforcement_log": [
      "Se deduplican reglas repetidas sin eliminar reglas útiles.",
      "Se conserva contexto curricular local del destino.",
      "Se refuerza normalización JSON como gate transversal.",
      "Se incorpora patrón argumentativo de Filosofía solo como abstracción estable.",
      "Se evita transferencia literal de redacción y bibliografía temática no equivalente.",
      "Se refuerza vínculo fiscal-tributario con aplicación profesional.",
      "Se preservan alertas locales sobre rutas truncadas, slug dinámico y authortable incompleto.",
      "Se normalizan relaciones del grafo a tipos permitidos.",
      "Se marca como supuesto todo dato no confirmado localmente.",
      "Se mantiene cerebro editorial mínimo para actividades fiscales futuras."
    ]
  }
}