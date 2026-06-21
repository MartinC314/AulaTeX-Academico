{
  "summary": [
    "Se consolida sincronizacion transversal conservadora desde actividad origen hacia materia destino.",
    "Se preservan reglas institucionales validas y se deduplican sin perdida.",
    "Se refuerza normalizacion estructurada obligatoria antes de propagacion recursiva.",
    "Se transfieren solo abstracciones estables: identidad, estructura reusable, calidad y trazabilidad.",
    "No se transfiere contenido tematico especifico de Filosofia del Derecho al destino."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local de la materia destino en todos los entregables.",
    "Usar contexto curricular verificado localmente del destino; no mezclar datos del origen.",
    "Usar la carpeta de materia como entrada canonica.",
    "Tratar Codex y GPT-Pro como procedencia provisional, no como identidad del entregable.",
    "Marcar como supuesto cualquier dato no visible en la consigna local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al solicitado por la planeacion semanal.",
    "Distinguir reporte, presentacion y producto visual segun consigna.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, normas, argumentos y criterio propio.",
    "Evitar extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna local."
  ],
  "latex_rules": [
    "Reutilizar plantilla .tex local sin romper identidad institucional.",
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Mantener claves BibTeX estables para evitar quiebres de compilacion.",
    "Corregir tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo con caracteres anómalos antes de referenciar o compilar.",
    "Revisar y cerrar correctamente entornos tabular antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de cada actividad en el .bib local de la materia.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Tratar bibliografia heredada de otra materia como no transferible salvo validacion local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Compartir entre nodos no equivalentes solo abstracciones editoriales estables.",
    "Evitar transferir redaccion literal o contenido tematico del origen.",
    "Preservar reglas utiles previas y evitar regresiones.",
    "No convertir supuestos en reglas definitivas sin evidencia local.",
    "Mantener compresion lossless por union y deduplicacion."
  ],
  "open_questions": [
    "Confirmar nomenclatura final con o sin acento en 'publico' para identidad de archivos. [supuesto]",
    "Confirmar reparacion completa de tokens $(@{...}.Slug) en README y programa analitico.",
    "Confirmar cierre del entorno tabular truncado en reporte base .tex.",
    "Confirmar formato minimo de conclusion juridica por tipo de actividad.",
    "Confirmar si existe rubrica local especifica para profundidad argumentativa."
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
        "Usar solo contexto curricular verificado en el destino.",
        "No mezclar metadatos curriculares entre materias."
      ]
    },
    "essence": [
      "Problema.",
      "Conceptos y marco normativo.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables juridicos claros, fundados y verificables.",
      "Sostener calidad editorial transversal sin contaminar contexto tematico entre materias."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales sin redundancia.",
      "Supuestos siempre etiquetados.",
      "Cierre con criterio juridico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> norma/doctrina -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> posicion propia.",
      "Consigna -> desarrollo alineado -> verificacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Consigna de actividad",
        "Estructura argumentativa juridica",
        "Evidencia verificable",
        "Conclusion transferible",
        "Normalizacion JSON",
        "Consistencia cita-bibliografia",
        "Trazabilidad de fuente provisional"
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
          "justification": "El producto define forma y alcance del desarrollo."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica valida requiere sustento documental."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Trazabilidad de fuente provisional",
          "kind": "supports",
          "justification": "Permite propagar memoria confiable y auditable."
        },
        {
          "source": "Consistencia cita-bibliografia",
          "target": "Evidencia verificable",
          "kind": "depends_on",
          "justification": "Sin correspondencia cita-.bib no hay verificabilidad."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura argumentativa juridica",
          "kind": "develops",
          "justification": "La institucion exige formato academico y cierre juridico propio."
        }
      ],
      "evidence": [
        "README destino: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico destino: proposito y ejes de trabajo.",
        "Archivo .bib destino con fuentes institucionales base.",
        "Memoria origen: gates de parseo JSON y normalizacion estructurada."
      ]
    },
    "reinforcement_log": [
      "Ciclo 44: se integran reglas transversales estables del origen sin mover contenido tematico.",
      "Ciclo 44: se refuerza gate de bloqueo por JSON no parseable.",
      "Ciclo 44: se refuerza etiquetado de supuestos y no-invencion de fuentes.",
      "Ciclo 44: se agrega control tecnico de tokens Slug sin expandir y tabular truncado."
    ]
  }
}