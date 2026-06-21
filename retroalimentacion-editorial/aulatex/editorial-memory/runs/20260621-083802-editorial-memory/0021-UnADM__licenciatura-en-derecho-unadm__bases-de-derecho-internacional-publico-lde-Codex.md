{
  "summary": [
    "Se refuerza memoria de materia con transferencia transversal estable desde actividad origen sin mover contenido tematico especifico.",
    "Se conserva normalizacion estructurada obligatoria antes de propagacion recursiva.",
    "Se consolidan ejes editoriales reutilizables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene identidad UnADM y contexto curricular local de semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Se incorpora incidencia tecnica local verificable: tokens Slug sin expandir y caracteres anómalos en README/programa."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local: Bases de derecho internacional publico.",
    "Alinear entregables a Licenciatura en Derecho, semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Usar codigo de curso LDE-S4B1 en metadatos.",
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
    "Integrar conceptos, normas, doctrina o datos pertinentes al caso de actividad.",
    "Evitar extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes.",
    "Verificar que cada producto corresponda exactamente a su consigna."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre README, programa analitico, .bib y plantillas locales.",
    "Mantener auditoria de parseo JSON antes de nueva propagacion."
  ],
  "latex_rules": [
    "Reutilizar plantilla .tex local sin romper identidad institucional.",
    "Mantener compatibilidad con clase article, spanish, letterpaper y oneside.",
    "Completar metadatos de portada segun actividad en curso.",
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Corregir tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir caracteres anómalos en nombres/rutas antes de compilar.",
    "Revisar y cerrar correctamente entornos tabular antes de compilar."
  ],
  "bibliography_rules": [
    "Registrar fuentes de actividad en bases-de-derecho-internacional-publico.bib.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Marcar referencias faltantes como pendientes.",
    "Conservar metadatos minimos: autor, titulo, año y fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas, estables y no duplicadas.",
    "Aplicar compresion lossless por union-dedupe sin recortar reglas utiles previas.",
    "No propagar supuestos como reglas definitivas.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual en saltos transversales.",
    "Evitar traslado de contenido tematico especifico de Filosofia del Derecho a Derecho Internacional Publico.",
    "Conservar incidencias historicas de salidas no estructuradas para prevencion de regresiones."
  ],
  "open_questions": [
    "Confirmar criterio editorial final sobre uso de publico/publico con acento en nombres visibles. [supuesto]",
    "Confirmar si se normalizara de inmediato la nomenclatura con caracteres anómalos en README. [supuesto]",
    "Confirmar correccion definitiva de tokens Slug sin expandir en README y programa analitico.",
    "Confirmar si la plantilla de reporte requiere ajuste adicional de tabular truncado."
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
      "Consigna primero, desarrollo alineado despues.",
      "Problema, conceptos, evidencia, analisis propio y conclusion juridica.",
      "Transferencia transversal conservadora sin contaminar contenidos tematicos."
    ],
    "reason_for_being": [
      "Guiar productos academicos verificables y transferibles a practica juridica.",
      "Asegurar calidad estructural y trazabilidad editorial en propagacion recursiva."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales no redundantes.",
      "Supuestos etiquetados.",
      "Cierre con criterio juridico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> norma/doctrina -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> postura propia.",
      "Consigna -> producto solicitado -> verificacion final."
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
          "justification": "El formato y profundidad del entregable dependen de la consigna."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica valida requiere respaldo documental."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Consistencia cita-bibliografia",
          "kind": "supports",
          "justification": "La estructura valida facilita controles automaticos de calidad."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura argumentativa juridica",
          "kind": "develops",
          "justification": "Define tono, formato y estandar academico comun."
        }
      ],
      "evidence": [
        "README de materia destino con ubicacion curricular y pauta editorial.",
        "Programa analitico destino con proposito y ejes de trabajo.",
        "Archivo .bib local con claves institucionales verificables.",
        "Incidencia visible de tokens $(@{...}.Slug) sin expandir en README/programa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 21: deduplicacion integral y conservacion de reglas utiles previas.",
      "Ciclo 21: transferencia transversal solo de abstracciones estables.",
      "Ciclo 21: refuerzo de gates JSON, evidencia y consistencia cita-bibliografia.",
      "Ciclo 21: se mantiene vacio tematico local abierto donde falta consigna especifica."
    ]
  }
}