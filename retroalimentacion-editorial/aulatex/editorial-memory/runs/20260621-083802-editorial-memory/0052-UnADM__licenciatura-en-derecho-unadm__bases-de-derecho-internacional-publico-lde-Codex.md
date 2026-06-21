{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre actividad de origen y materia destino.",
    "Se preservan reglas utiles previas y se deduplican sin perdida.",
    "Se refuerzan ejes estables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene bloqueo de propagacion ante salidas no JSON parseable.",
    "Se evita transferir contenido tematico especifico de Filosofia del Derecho al destino de Derecho Internacional Publico."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local: Bases de derecho internacional publico.",
    "Alinear entregables al contexto local verificado: Licenciatura en Derecho, semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "No mezclar metadatos curriculares del origen con el destino.",
    "Marcar como supuesto cualquier dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como procedencia provisional, no como identidad del entregable."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear estructura al producto solicitado por la planeacion semanal.",
    "Distinguir reporte, presentacion y producto visual segun consigna.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, normas, argumentos y criterio propio.",
    "Evitar extrapolar fuentes de semanas o materias no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre consigna, programa analitico y producto final.",
    "Validar sintaxis LaTeX y cierre de entornos antes de compilar."
  ],
  "latex_rules": [
    "Reutilizar plantilla .tex local de la materia sin romper identidad institucional.",
    "Mantener compatibilidad con clase article, spanish, letterpaper y oneside.",
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo con caracteres anommalos antes de compilar.",
    "Reparar cortes de entornos tabular detectados en plantillas locales."
  ],
  "bibliography_rules": [
    "Registrar fuentes de actividad en bases-de-derecho-internacional-publico.bib.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Marcar referencias faltantes como pendientes.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Validar que toda clave citada exista en el .bib local."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables en nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "No propagar redaccion literal ni contenido tematico especifico del origen.",
    "Preservar reglas utiles previas y evitar regresiones.",
    "Aplicar compresion lossless por union y deduplicacion.",
    "Si falta contexto local, mantener cerebro minimo y abrir preguntas."
  ],
  "open_questions": [
    "Confirmar criterio editorial sobre uso de publico sin acento frente a publico con acento en nombres visibles.",
    "Confirmar normalizacion final de nombres con caracteres anommalos en README.",
    "Confirmar resolucion definitiva de tokens $(@{...}.Slug) en README y programa analitico.",
    "Confirmar si el archivo .bib canonico ya quedo fijado sin alias adicionales.",
    "Supuesto: el recorte de entorno tabular en el .tex de reporte sigue pendiente de reparacion local."
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
      "Consigna de actividad como ancla.",
      "Problema juridico o social como disparador.",
      "Evidencia verificable para sostener afirmaciones.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros, fundados y verificables.",
      "Asegurar trazabilidad editorial entre consigna, desarrollo, evidencia y cierre."
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
          "justification": "La forma del entregable depende del producto pedido."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica valida requiere respaldo documental."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Sincronizacion transversal",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay propagacion segura."
        },
        {
          "source": "Consistencia cita-bibliografia",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita afirmaciones sin fuente y claves rotas."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura argumentativa juridica",
          "kind": "develops",
          "justification": "La identidad define tono, forma y trazabilidad del entregable."
        }
      ],
      "evidence": [
        "README destino: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico destino: proposito y ejes de trabajo.",
        "Archivo .bib local: claves institucionales base existentes.",
        "Historial: incidencias de salida no estructurada en ciclos previos."
      ]
    },
    "reinforcement_log": [
      "Ciclo 52: se integran abstracciones estables del origen sin trasladar contenido tematico especifico.",
      "Ciclo 52: se refuerza gate de JSON parseable como condicion de propagacion recursiva.",
      "Ciclo 52: se preservan reglas previas del destino y se eliminan duplicados semanticos.",
      "Ciclo 52: se mantiene estrategia progresiva y conservadora con compresion lossless."
    ]
  }
}