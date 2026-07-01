{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre Filosofia del Derecho (actividad) y Bases de derecho internacional publico (materia).",
    "Se preservan reglas utiles previas del destino y se agregan solo abstracciones estables verificables.",
    "Se refuerzan ejes editoriales comunes: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene bloqueo de propagacion para salidas no JSON parseable y normalizacion obligatoria.",
    "Supuesto: no se transfiere contenido tematico especifico de Filosofia del Derecho por no equivalencia de nodos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local de la materia destino en todos los entregables.",
    "Usar carpeta de materia como entrada canonica.",
    "Usar contexto curricular verificado del destino y no mezclar con el origen.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar Codex y GPT-Pro como trazabilidad provisional, no como identidad del entregable.",
    "Conservar alumno de plantilla salvo instruccion local explicita."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto final con la planeacion semanal.",
    "Distinguir reporte, presentacion y producto visual segun consigna.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Adaptar cada actividad al producto solicitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante y evitar resumen solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, normas, argumentos y criterio propio.",
    "No extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar memoria.",
    "Normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre consigna, programa analitico y producto.",
    "Mantener auditoria de parseo JSON por ciclo."
  ],
  "latex_rules": [
    "Reutilizar plantilla .tex local de la materia sin romper identidad institucional.",
    "Mantener compatibilidad con clase article, spanish, letterpaper y oneside.",
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, sin referencias rotas y con entornos cerrados.",
    "Corregir caracteres anomalos en nombres de archivo y rutas antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas de actividad en el .bib local de la materia.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Validar que toda clave citada exista en el .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas, generales y no duplicadas.",
    "Aplicar compresion lossless por union y deduplicacion.",
    "Preservar reglas utiles previas sin regresion.",
    "No propagar supuestos como reglas definitivas.",
    "Transferir identidad, estructura reusable, gates y grafo conceptual; no redaccion literal.",
    "Si falta contexto local, mantener cerebro editorial minimo y abrir vacios como preguntas."
  ],
  "open_questions": [
    "Confirmar criterio editorial definitivo de publico con o sin acento en nombres visibles.",
    "Confirmar correccion de nombres con caracteres anomalos en README.",
    "Confirmar reparacion completa de tokens $(@{...}.Slug) en README y programa analitico.",
    "Confirmar cierre correcto del entorno tabular en el reporte .tex local.",
    "Supuesto: la materia destino aun no define rubrica detallada por tipo de actividad."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador ante datos no verificados."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada obligatoria antes de propagacion.",
        "Trazabilidad de procedencia sin contaminar identidad del entregable."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Destino: semestre 4, bloque 1, obligatoria, 8 creditos.",
        "Usar solo contexto curricular verificado del nodo destino.",
        "No mezclar metadatos curriculares entre materias."
      ]
    },
    "essence": [
      "Problema juridico o social que activa la actividad.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable y cita explicita.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico y criterio propio.",
      "Asegurar calidad formal, trazabilidad y consistencia documental.",
      "Permitir reutilizacion transversal de reglas estables sin contaminar contexto local."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y no redundantes.",
      "Supuestos siempre etiquetados.",
      "Cierre con criterio juridico aplicable.",
      "Correspondencia estricta entre consigna y producto."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> marco normativo/doctrinal -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> posicion propia.",
      "Consigna -> desarrollo alineado -> verificacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Consigna de actividad",
        "Estructura argumentativa juridica",
        "Evidencia verificable",
        "Analisis propio",
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
          "justification": "La forma y tipo de entregable se determinan por la consigna."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "El criterio propio gana validez cuando se sustenta documentalmente."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion juridica deriva del razonamiento argumentado."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Consistencia cita-bibliografia",
          "kind": "depends_on",
          "justification": "La reutilizacion segura requiere estructura valida y verificable."
        }
      ],
      "evidence": [
        "README de la materia destino: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico destino: proposito y ejes de trabajo.",
        "bases-de-derecho-internacional-publico.bib: fuentes institucionales base.",
        "Memoria origen: regla de normalizacion estructurada obligatoria antes de propagar."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: se mantiene estrategia progresiva y conservadora.",
      "Ciclo 2: se preservan reglas previas del destino sin eliminaciones.",
      "Ciclo 2: se incorporan abstracciones estables del origen no dependientes de tema.",
      "Ciclo 2: se evita traslado de contenido doctrinal especifico de Filosofia del Derecho.",
      "Ciclo 2: se refuerzan gates de parseo JSON, supuestos y consistencia cita-bibliografia."
    ]
  }
}