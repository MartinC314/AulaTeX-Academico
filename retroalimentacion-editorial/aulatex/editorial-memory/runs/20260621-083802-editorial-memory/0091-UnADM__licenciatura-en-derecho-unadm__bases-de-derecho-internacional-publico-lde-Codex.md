{
  "summary": [
    "Se refuerza sincronizacion transversal conservadora entre actividad origen y materia destino.",
    "Se preservan reglas utiles previas y se elimina duplicidad por union-dedupe lossless.",
    "Se transfieren solo abstracciones estables: identidad, estructura, calidad, trazabilidad y normalizacion.",
    "Se mantiene contexto curricular exclusivo del destino: semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Se conserva incidencia historica: salidas no parseables requieren normalizacion previa."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local: Bases de derecho internacional publico.",
    "Usar codigo de curso LDE-S4B1 en metadatos.",
    "Usar carpeta de materia como entrada canonica.",
    "No mezclar metadatos curriculares con materias origen.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como procedencia provisional, no como identidad."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato solicitado por planeacion semanal.",
    "Distinguir reporte, presentacion y producto visual segun consigna.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, argumentos, normas y criterio propio.",
    "Evitar extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes."
  ],
  "quality_gates": [
    "Bloquear propagacion si salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar memoria.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre consigna, programa analitico y entregable."
  ],
  "latex_rules": [
    "Reutilizar plantilla .tex local sin romper identidad institucional.",
    "Mantener compatibilidad con article, spanish, letterpaper y oneside.",
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo con caracteres anómalos antes de referenciar.",
    "Revisar y cerrar entornos LaTeX incompletos antes de compilar."
  ],
  "bibliography_rules": [
    "Registrar fuentes de actividad en bases-de-derecho-internacional-publico.bib.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Validar que toda clave citada exista en el .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Compartir solo reglas generales estables entre nodos no equivalentes.",
    "Evitar trasladar contenido tematico especifico de Filosofia del Derecho.",
    "Preservar reglas utiles previas sin regresion semantica.",
    "Aplicar compresion lossless por union-dedupe, nunca por recorte.",
    "No convertir supuestos en reglas definitivas sin verificacion local."
  ],
  "open_questions": [
    "Confirmar criterio editorial final sobre publico sin acento frente a publico con acento.",
    "Confirmar y corregir todos los tokens $(@{...}.Slug) pendientes en archivos de control.",
    "Confirmar cierre completo del entorno tabular en reporte-bases-de-derecho-internacional-publico.tex.",
    "Confirmar si existe rubrica local por actividad para ajustar profundidad argumentativa.",
    "Supuesto: la materia destino conserva soporte principal para reporte y presentacion."
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
        "Destino verificado: semestre 4, bloque 1, obligatoria, 8 creditos.",
        "No mezclar contexto curricular entre materias."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables juridicos claros, verificables y aplicables.",
      "Asegurar consistencia entre consigna, argumentacion, evidencia y cierre profesional."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales sin redundancia.",
      "Supuestos siempre etiquetados.",
      "Cierre con criterio juridico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> norma/doctrina -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> postura propia.",
      "Consigna -> desarrollo alineado -> verificacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Consigna de actividad",
        "Estructura argumentativa juridica",
        "Evidencia verificable",
        "Conclusion transferible",
        "Normalizacion JSON",
        "Consistencia cita-bibliografia",
        "Identidad institucional UnADM"
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
          "justification": "La forma y alcance del entregable dependen del producto solicitado."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica valida exige respaldo comprobable."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Consistencia cita-bibliografia",
          "kind": "supports",
          "justification": "La estructura valida facilita auditoria editorial y trazabilidad."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura argumentativa juridica",
          "kind": "develops",
          "justification": "La identidad define tono, formato y estandar academico transversal."
        }
      ],
      "evidence": [
        "README destino: identidad y ubicacion curricular verificadas.",
        "Programa analitico destino: proposito y ejes de trabajo.",
        "Bib local destino: claves institucionales base existentes.",
        "Historial: incidencias de salida no parseable en ciclos previos."
      ]
    },
    "reinforcement_log": [
      "Se consolidaron reglas duplicadas en un set unico accionable.",
      "Se reforzo gate de parseo JSON como condicion de propagacion recursiva.",
      "Se conservaron reglas institucionales y de integridad academica sin perdida.",
      "Se evito transferir contenido tematico especifico del origen por ser nodo no equivalente.",
      "Se añadieron vacios locales como preguntas abiertas sin inventar fuentes."
    ]
  }
}