{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre actividad origen y materia destino.",
    "Se preservan reglas utiles vigentes y se deduplican sin perdida.",
    "Se transfieren solo abstracciones estables: identidad, estructura, calidad y trazabilidad.",
    "Se evita traslado de contenido tematico especifico de Filosofia del Derecho al destino.",
    "Se refuerza normalizacion JSON obligatoria antes de propagacion recursiva.",
    "Se incorpora incidencia local verificable: tokens sin expandir y cortes en nombres de archivos del README.",
    "Supuesto: la consigna local por actividad aun no esta disponible en esta memoria."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial/local de la materia: Bases de derecho internacional publico.",
    "Alinear entregables a Licenciatura en Derecho, semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Usar codigo de curso LDE-S4B1 en metadatos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como procedencia provisional, no como identidad del entregable."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeacion semanal.",
    "Distinguir reporte, presentacion y producto visual segun consigna.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Conservar separacion entre README, programa analitico, .bib y plantillas .tex."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, argumentos, normas y criterio propio.",
    "Evitar extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes.",
    "No propagar supuestos como reglas definitivas."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna de la actividad local.",
    "Verificar que README, programa analitico, .bib y plantillas locales coincidan."
  ],
  "latex_rules": [
    "Reutilizar plantilla .tex local sin romper identidad institucional.",
    "Mantener compatibilidad con clase article, spanish, letterpaper y oneside.",
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Revisar y cerrar correctamente entornos tabular antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir caracteres anomalos en nombres de archivo antes de referenciar."
  ],
  "bibliography_rules": [
    "Registrar fuentes de actividad en bases-de-derecho-internacional-publico.bib.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Marcar referencias faltantes como pendientes.",
    "Conservar metadatos minimos: autor, titulo, año, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Validar que las claves citadas existan en el .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Aplicar compresion lossless por union y deduplicacion.",
    "Evitar regresiones respecto de reglas utiles previas.",
    "Propagar solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar gates de calidad e identidad sobre redaccion literal.",
    "Conservar incidencias historicas de salida no estructurada para auditoria.",
    "Si falta consigna local, propagar reglas generales y abrir vacios como preguntas."
  ],
  "open_questions": [
    "Confirmar consigna real de la primera actividad local para ajustar producto objetivo.",
    "Confirmar criterio editorial final sobre publico con o sin acento en nombres visibles.",
    "Confirmar si se normalizaran los nombres cortados del README (eporte/eferencias).",
    "Confirmar reparacion del entorno tabular truncado en reporte-bases-de-derecho-internacional-publico.tex.",
    "Confirmar si existe rubrica local para calibrar profundidad argumentativa.",
    "Supuesto: no hay nuevas fuentes tematicas obligatorias del destino en esta memoria."
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
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 4, bloque 1, obligatoria, 8 creditos.",
        "Asignatura: Bases de derecho internacional publico."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo pertinente.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible.",
      "Normalizacion estructurada previa a propagacion."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en entregables juridicos claros, verificables y utiles.",
      "Sostener un cerebro editorial estable, trazable y reutilizable entre nodos.",
      "Asegurar calidad formal y academica antes de cualquier propagacion."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales sin redundancia.",
      "Supuestos etiquetados.",
      "Cierre con criterio juridico aplicable.",
      "Consistencia cita-bibliografia."
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
          "justification": "El tipo de producto define la forma del desarrollo."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica solo es valida con respaldo documental."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Trazabilidad de fuentes provisionales",
          "kind": "supports",
          "justification": "La estructura parseable permite auditar procedencia y cambios."
        },
        {
          "source": "Consistencia cita-bibliografia",
          "target": "Evidencia verificable",
          "kind": "depends_on",
          "justification": "Sin claves validas no hay soporte comprobable."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura argumentativa juridica",
          "kind": "develops",
          "justification": "La identidad fija tono, formato y estandar de entrega."
        }
      ],
      "evidence": [
        "README destino: ubicacion curricular, pauta editorial y estructura de archivos.",
        "Programa analitico destino: proposito y ejes de trabajo.",
        "Bibliografia destino: claves institucionales existentes.",
        "Memoria origen: regla estable de normalizacion y bloqueo por JSON no parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 16: deduplicacion lossless aplicada sin eliminar reglas utiles previas.",
      "Ciclo 16: se reforzaron gates de parseo JSON, respaldo y supuesto etiquetado.",
      "Ciclo 16: se transfirieron patrones argumentativos generales, no contenido tematico de origen.",
      "Ciclo 16: se añadieron incidencias locales verificables de README/LaTeX para control de calidad."
    ]
  }
}