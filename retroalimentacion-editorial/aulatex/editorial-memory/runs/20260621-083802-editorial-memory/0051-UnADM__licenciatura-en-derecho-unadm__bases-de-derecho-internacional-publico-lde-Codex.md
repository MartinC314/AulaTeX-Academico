{
  "summary": [
    "Se refuerza sincronizacion transversal con reglas estables y deduplicadas.",
    "Se preserva identidad UnADM y contexto curricular local del destino.",
    "Se incorporan del origen solo abstracciones reutilizables: normalizacion, estructura argumentativa y control de supuestos.",
    "Se evita transferir contenido tematico especifico de Filosofia del Derecho."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local: Bases de derecho internacional publico.",
    "Usar codigo de curso LDE-S4B1 en metadatos.",
    "Alinear entregables a Licenciatura en Derecho, semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como procedencia provisional, no como identidad."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear estructura y profundidad al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Distinguir reporte, presentacion y producto visual segun consigna."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, normas, doctrina, argumentos y criterio propio.",
    "Evitar extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre consigna de actividad y producto entregable."
  ],
  "latex_rules": [
    "Reutilizar plantilla .tex local sin romper identidad institucional.",
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Corregir tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico antes de nuevas referencias.",
    "Corregir nombres de archivo con caracteres anomalos en README antes de propagar."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas de actividad en bases-de-derecho-internacional-publico.bib.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Validar que toda clave citada exista en el .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir entre nodos no equivalentes solo abstracciones editoriales estables.",
    "Evitar traslado literal de redaccion y contenido tematico de la materia origen.",
    "Preservar reglas utiles previas sin regresion.",
    "Aplicar compresion lossless por union y deduplicacion.",
    "No convertir supuestos en reglas definitivas sin verificacion local."
  ],
  "open_questions": [
    "Confirmar correccion definitiva de tokens $(@{...}.Slug) en README y programa analitico del destino.",
    "Confirmar reparacion del corte de entorno tabular en reporte-bases-de-derecho-internacional-publico.tex.",
    "Confirmar criterio editorial final sobre uso de publico/publico con acento en nombres visibles.",
    "Confirmar rubricas locales por actividad para ajustar gates de profundidad argumentativa."
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
        "Semestre 4, bloque 1, obligatoria, 8 creditos.",
        "No mezclar metadatos curriculares del origen con el destino."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible.",
      "Normalizacion JSON previa a propagacion."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos juridicos consistentes y verificables.",
      "Asegurar trazabilidad editorial sin invenciones ni perdida de reglas utiles.",
      "Mantener un cerebro editorial transversal, progresivo y conservador."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales no redundantes.",
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
        "Control de supuestos"
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
          "justification": "El formato y alcance del producto dependen de la consigna."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "Una conclusion juridica valida requiere respaldo verificable."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Consistencia cita-bibliografia",
          "kind": "develops",
          "justification": "La estructura parseable facilita control de calidad documental."
        },
        {
          "source": "Control de supuestos",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Etiquetar incertidumbre evita afirmar datos no verificados."
        }
      ],
      "evidence": [
        "README destino: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico destino: proposito y ejes de trabajo.",
        "Bibliografia local destino: claves institucionales verificadas.",
        "Memoria origen: gates de parseo JSON, estructura minima y control de supuestos."
      ]
    },
    "reinforcement_log": [
      "Ciclo 51: se consolidan reglas transversales estables sin mezclar contenido tematico de Filosofia del Derecho.",
      "Ciclo 51: se refuerza gate de JSON parseable como condicion de propagacion recursiva.",
      "Ciclo 51: se agrega control explicito de tokens sin expandir y anomalias de nombres de archivo.",
      "Ciclo 51: se mantiene estrategia conservadora con compresion lossless por deduplicacion."
    ]
  }
}