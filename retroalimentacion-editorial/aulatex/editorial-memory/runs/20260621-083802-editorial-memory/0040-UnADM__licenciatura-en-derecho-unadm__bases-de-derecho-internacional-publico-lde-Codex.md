{
  "summary": [
    "Se refuerza sincronizacion transversal con abstracciones editoriales estables entre actividad y materia no equivalente.",
    "Se conserva identidad UnADM y contexto curricular local del destino: semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Se mantiene normalizacion estructurada obligatoria y bloqueo de propagacion sin JSON parseable.",
    "Se consolidan ejes reutilizables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se evita traslado de contenido tematico especifico de Filosofia del Derecho al destino de Derecho Internacional Publico.",
    "Se incorpora control de supuestos y trazabilidad de fuentes heredadas como procedencia provisional."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local de la materia en todos los entregables.",
    "Alinear entregables al contexto curricular verificado del destino.",
    "No mezclar metadatos curriculares del nodo origen con el destino.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como procedencia provisional, no como verdad editorial."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear la estructura al producto solicitado por la planeacion semanal.",
    "Distinguir reporte, presentacion y producto visual segun consigna.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener separacion entre README, programa analitico, .bib y plantillas .tex."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante y evitar solo resumen descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, normas, doctrina y criterio propio.",
    "No extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes.",
    "Verificar correspondencia entre producto entregado y consigna de actividad."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Validar sintaxis LaTeX y cierre de entornos antes de compilar.",
    "Conservar auditoria de incidencias historicas de parseo."
  ],
  "latex_rules": [
    "Reutilizar plantilla .tex local del destino sin romper identidad institucional.",
    "Usar codificacion y acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo con caracteres anomalos antes de referenciarlos."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de cada actividad en el .bib local de la materia.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Validar que toda clave citada exista en el .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo reglas generales estables en nodos no equivalentes.",
    "Preservar reglas utiles previas y evitar regresiones.",
    "No propagar supuestos como reglas definitivas.",
    "Aplicar compresion lossless por union y deduplicacion.",
    "Si falta contexto local, mantener cerebro editorial minimo y abrir vacios como preguntas."
  ],
  "open_questions": [
    "Confirmar criterio editorial final sobre uso de publico/publico con acento en nombres visibles. [supuesto]",
    "Confirmar normalizacion definitiva de nombres corruptos en README (lineas con eporte/eferencias).",
    "Confirmar si se corrige de forma automatica el token Slug no expandido en rutas bibliograficas.",
    "Confirmar rubrica local de evaluacion por actividad para ajustar profundidad argumentativa.",
    "Confirmar formato minimo obligatorio de conclusion juridica por tipo de evidencia."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada obligatoria antes de propagacion."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Destino: semestre 4, bloque 1, obligatoria, 8 creditos.",
        "No mezclar contexto curricular del origen con el destino."
      ]
    },
    "essence": [
      "Consigna primero, forma despues.",
      "Problema, conceptos, evidencia, analisis propio y conclusion juridica.",
      "Transferencia transversal de metodo, no de contenido tematico."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables juridicos claros, verificables y transferibles.",
      "Sostener coherencia institucional, academica y tecnica en toda la suite LaTeX."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales sin redundancia.",
      "Supuestos etiquetados.",
      "Cierre con criterio juridico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> norma/doctrina -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> postura propia.",
      "Consigna -> desarrollo alineado -> verificacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Consigna de actividad",
        "Estructura argumentativa juridica",
        "Evidencia verificable",
        "Conclusion juridica transferible",
        "Normalizacion JSON",
        "Consistencia cita-bibliografia",
        "Trazabilidad de fuentes provisionales"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Consigna de actividad",
          "target": "Estructura argumentativa juridica",
          "kind": "depends_on",
          "justification": "El producto define la forma valida del desarrollo."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "Sin respaldo no hay cierre juridico defendible."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo valido no hay transferencia segura."
        },
        {
          "source": "Consistencia cita-bibliografia",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita citas huerfanas y referencias inventadas."
        },
        {
          "source": "Trazabilidad de fuentes provisionales",
          "target": "Calidad editorial",
          "kind": "develops",
          "justification": "Separa procedencia tecnica de autoridad academica."
        }
      ],
      "evidence": [
        "README de destino confirma contexto curricular y pauta editorial.",
        "Programa analitico de destino define proposito y ejes de trabajo.",
        ".bib local contiene claves institucionales verificables.",
        "Memoria origen aporta gates de JSON, supuestos y estructura argumentativa reutilizable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 40: deduplicacion completa de reglas repetidas y variantes ortograficas.",
      "Ciclo 40: se refuerza transferencia conservadora de metodo transversal.",
      "Ciclo 40: se preservan incidencias historicas de salida no estructurada como control de riesgo.",
      "Ciclo 40: se mantienen vacios locales abiertos sin inventar fuentes ni consignas."
    ]
  }
}