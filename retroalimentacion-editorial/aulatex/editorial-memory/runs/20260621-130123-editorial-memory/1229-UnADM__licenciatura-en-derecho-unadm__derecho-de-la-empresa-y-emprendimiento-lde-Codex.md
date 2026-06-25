{
  "summary": [
    "Se consolida sincronizacion transversal con transferencia de abstracciones estables desde actividad no equivalente.",
    "Se preservan reglas utiles previas sin regresion y con deduplicacion lossless.",
    "Se refuerza marco reusable: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene normalizacion estructurada obligatoria antes de propagacion recursiva.",
    "Se conserva alerta local por tokens Slug sin expandir y nombres de archivo con artefactos.",
    "Supuesto: no hay consigna local de actividad especifica en este ciclo."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial de la materia en todos los artefactos.",
    "Usar Licenciatura en Derecho como programa academico.",
    "Respetar contexto curricular local confirmado: semestre 6, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna o archivo local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Organizar en secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el entregable al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Conservar correspondencia entre README, .tex, presentacion y .bib."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No asumir que fuentes de otras semanas aplican automaticamente a la actividad local.",
    "Agregar fuentes nuevas solo en el .bib de la materia con metadatos minimos."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar memoria.",
    "No eliminar reglas utiles previas durante fusion union-dedupe.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y claves del .bib.",
    "Revisar y normalizar respuestas no estructuradas antes de propagacion lateral, ascendente o aguas abajo.",
    "Verificar que el README liste rutas y archivos reales."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Actualizar documenttitle y documentsubtitle por actividad concreta.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo con artefactos de salto antes de compilar.",
    "Supuesto: autor visible en plantilla es provisional hasta confirmacion por actividad."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo obras verificables.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos pertinentes a la materia.",
    "Conservar metadatos minimos: autor, titulo, año, fuente editorial o URL.",
    "Mantener unadmSitioWeb y unadmMallaDerecho2024 como base local mientras no haya conflicto.",
    "Registrar fuentes especificas en derecho-de-la-empresa-y-emprendimiento.bib.",
    "No citar claves ausentes del .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales y estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "No propagar contenido doctrinal especifico de Filosofia del Derecho a esta materia.",
    "Propagar alerta de tokens Slug sin expandir a nodos con plantillas generadas.",
    "Mantener estrategia progresiva y conservadora: agregar solo mejoras verificables."
  ],
  "open_questions": [
    "Confirmar consigna de la proxima actividad para ajustar tipo de entregable.",
    "Confirmar si documentauthor debe parametrizarse por actividad.",
    "Confirmar correccion definitiva de rutas con artefactos en README.",
    "Confirmar politica local para year en unadmSitioWeb versus fecha de consulta.",
    "Confirmar cierre completo del archivo de reporte local truncado."
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
        "Integridad academica con trazabilidad bibliografica.",
        "Entrada canonica por carpeta de materia."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 6, bloque 2, obligatoria, 8 creditos.",
        "Transferencia profesional como criterio de cierre."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo pertinente.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible.",
      "Control explicito de supuestos."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos solidos y verificables.",
      "Asegurar consistencia entre identidad institucional, estructura argumentativa y evidencia.",
      "Permitir propagacion segura de memoria editorial entre nodos."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Supuestos marcados en linea.",
      "Sin afirmaciones sin fuente.",
      "Cierre con aplicacion practica juridica."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis propio -> conclusion.",
      "Marco normativo y doctrinal como soporte del criterio personal.",
      "Verificacion final de coherencia entre pregunta guia y cierre."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Problema juridico",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Integridad bibliografica",
        "Control de supuestos",
        "Tokens Slug sin expandir"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin JSON valido la transferencia es insegura."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion exige respaldo comprobable."
        },
        {
          "source": "Control de supuestos",
          "target": "Integridad argumentativa",
          "kind": "supports",
          "justification": "Diferencia hechos confirmados de inferencias."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura de entregables",
          "kind": "develops",
          "justification": "Define tono, formato y criterios comunes."
        },
        {
          "source": "Tokens Slug sin expandir",
          "target": "Calidad tecnica de artefactos",
          "kind": "contrasts",
          "justification": "Genera riesgo de rutas invalidas y compilacion fallida."
        }
      ],
      "evidence": [
        "README local de materia.",
        "Programa analitico local.",
        "Archivo .bib local con claves base.",
        "Reglas heredadas de normalizacion y control de supuestos."
      ]
    },
    "reinforcement_log": [
      "Ciclo 22: deduplicacion completa de reglas repetidas.",
      "Ciclo 22: conservadas reglas institucionales y gates criticos sin recorte.",
      "Ciclo 22: transferidas solo abstracciones estables por relacion transversal.",
      "Ciclo 22: bloqueada transferencia doctrinal especifica del nodo origen."
    ]
  }
}