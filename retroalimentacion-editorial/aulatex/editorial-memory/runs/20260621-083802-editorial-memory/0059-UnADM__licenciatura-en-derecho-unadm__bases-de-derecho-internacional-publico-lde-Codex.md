{
  "summary": [
    "Se sincroniza memoria transversal desde actividad de Filosofía del Derecho hacia materia de Bases de Derecho Internacional Público sin mezclar contenidos temáticos.",
    "Se preservan reglas útiles previas del destino y se refuerzan abstracciones editoriales estables: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se mantiene estrategia conservadora: transferencia por patrones, no por redacción literal.",
    "Se refuerza normalización estructurada obligatoria antes de propagación recursiva.",
    "Se detectan y mantienen pendientes locales de tokens sin expandir y cortes en nombres/entornos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local: Bases de derecho internacional publico.",
    "Alinear entregables al contexto curricular verificado del destino: semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Usar codigo de curso LDE-S4B1 en metadatos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar Codex y GPT-Pro como procedencia provisional, no como identidad del entregable.",
    "No mezclar metadatos curriculares ni tematicos entre materias distintas."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear la estructura al producto solicitado por la planeacion semanal.",
    "Distinguir reporte, presentacion y producto visual segun consigna.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener separacion entre README, programa analitico, .tex y .bib."
  ],
  "activity_rules": [
    "Adaptar cada actividad al producto solicitado en la semana correspondiente.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, normas, argumentos y criterio propio.",
    "Evitar extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre consigna, producto y programa analitico local.",
    "Mantener auditoria de parseo y cambios por ciclo."
  ],
  "latex_rules": [
    "Reutilizar plantillas locales de la materia sin romper identidad institucional.",
    "Mantener compatibilidad con clase article, spanish, letterpaper y oneside.",
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Compilar sin errores criticos, referencias rotas ni entornos abiertos.",
    "Corregir cortes de nombres de archivo en README (supuesto: error de salto de linea en 'reporte' y 'referencias').",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "No cambiar estructura base de portada sin instruccion editorial."
  ],
  "bibliography_rules": [
    "Registrar fuentes de actividad en bases-de-derecho-internacional-publico.bib.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Validar que toda clave citada exista en el .bib local.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas, generales y no duplicadas.",
    "Aplicar compresion lossless por union-dedupe y sin regresion.",
    "Transferir solo abstracciones estables entre nodos no equivalentes.",
    "No propagar supuestos como reglas definitivas.",
    "Conservar incidencias historicas de salidas no estructuradas para control de calidad.",
    "Priorizar identidad, gates de calidad, estructura reusable y grafo conceptual."
  ],
  "open_questions": [
    "Confirmar si el nombre editorial final usara 'publico' o 'público' de forma normalizada.",
    "Confirmar reparacion local de tokens Slug sin expandir en README y programa analitico.",
    "Confirmar reparacion del corte de entorno tabular en reporte .tex.",
    "Confirmar formato minimo de conclusion juridica por tipo de actividad en la materia destino."
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
        "Asignatura: Bases de derecho internacional publico."
      ]
    },
    "essence": [
      "Consigna primero, desarrollo despues.",
      "Problema, conceptos, evidencia, analisis propio y conclusion juridica.",
      "Transferencia transversal por patrones editoriales, no por contenido tematico."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables academicos validos, verificables y utiles para practica juridica.",
      "Preservar coherencia institucional y calidad tecnica en LaTeX y bibliografia.",
      "Habilitar propagacion segura entre nodos mediante memoria estructurada."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y no redundantes.",
      "Supuestos etiquetados.",
      "Cierre con criterio juridico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> norma/doctrina -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> posicion propia.",
      "Consigna -> producto alineado -> verificacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Consigna de actividad",
        "Estructura argumentativa juridica",
        "Evidencia verificable",
        "Conclusion transferible",
        "Normalizacion JSON",
        "Consistencia cita-bibliografia"
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
          "justification": "La forma del entregable depende del producto solicitado."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica necesita respaldo documental."
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
          "justification": "Evita afirmaciones sin fuente y claves rotas."
        }
      ],
      "evidence": [
        "README del destino: identidad y ubicacion curricular.",
        "Programa analitico del destino: proposito y ejes de trabajo.",
        "Archivo .bib local con claves institucionales existentes.",
        "Historial de incidencias de salida no estructurada en ciclos previos."
      ]
    },
    "reinforcement_log": [
      "Ciclo 59: se consolidan reglas transversales estables del origen sin trasladar contenido doctrinal especifico.",
      "Ciclo 59: se refuerza gate de JSON parseable como condicion de propagacion.",
      "Ciclo 59: se mantienen pendientes locales tecnicos (Slug sin expandir y tabular incompleto) como preguntas abiertas.",
      "Ciclo 59: sin regresion; deduplicacion aplicada en tono, estructura y calidad."
    ]
  }
}