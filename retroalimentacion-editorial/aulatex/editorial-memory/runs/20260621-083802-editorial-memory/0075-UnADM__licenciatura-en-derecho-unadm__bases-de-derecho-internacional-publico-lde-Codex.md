{
  "summary": [
    "Se consolida sincronizacion transversal con enfoque conservador y sin regresion.",
    "Se preservan reglas estables de identidad UnADM, estructura argumentativa y control de calidad.",
    "Se agregan mejoras verificables del contexto local: reparacion de tokens Slug y rutas con caracteres anómalos.",
    "Se evita transferir contenido tematico propio de Filosofia del Derecho por no equivalencia de nodos.",
    "Se mantiene compresion lossless por union y deduplicacion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local de materia: Bases de derecho internacional publico.",
    "Usar contexto curricular del destino verificado: semestre 4, bloque 1, obligatoria, 8 creditos.",
    "No mezclar metadatos curriculares entre materias distintas.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como procedencia provisional, no como identidad."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeacion semanal.",
    "Distinguir reporte, presentacion y producto visual segun consigna.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Conservar separacion entre README, programa analitico, .bib y plantillas .tex."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar resumen solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Integrar conceptos, normas, doctrina o datos pertinentes al caso.",
    "No extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna de la actividad vigente."
  ],
  "latex_rules": [
    "Reutilizar plantilla .tex local de la materia.",
    "Mantener compatibilidad con article, spanish, letterpaper y oneside.",
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Mantener claves BibTeX estables.",
    "Corregir rutas y nombres con caracteres anómalos en README.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Revisar y cerrar entornos tabular incompletos antes de compilar."
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
    "Propagar recursivamente solo reglas generales verificadas y no duplicadas.",
    "Aplicar estrategia conservadora en saltos transversales entre nodos no equivalentes.",
    "No propagar contenido tematico especifico del origen cuando no sea transferible.",
    "Preservar reglas utiles previas aunque se reubiquen por categoria.",
    "Mantener auditoria de parseo JSON en cada ciclo.",
    "Si falta contexto local, crear cerebro editorial minimo y abrir vacios como preguntas."
  ],
  "open_questions": [
    "Confirmar consigna concreta de la primera actividad del destino para ajustar artefacto.",
    "Confirmar criterio editorial final sobre publico con o sin acento en nombres visibles.",
    "Confirmar reparacion definitiva de lineas corruptas en README (eporte/eferencias).",
    "Confirmar si el reporte base ya corrige el corte de entorno tabular detectado.",
    "Supuesto: no hay rubrica local detallada por actividad; validar cuando se publique."
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
      "Problema juridico o social.",
      "Conceptos y marco normativo.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables claros, verificables y utiles para practica juridica.",
      "Sostener coherencia institucional y tecnica en toda la suite LaTeX."
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
        "Integridad de compilacion LaTeX"
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
          "justification": "El producto define forma y profundidad del desarrollo."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion valida exige respaldo documental y normativo."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Integridad de compilacion LaTeX",
          "kind": "depends_on",
          "justification": "La memoria estructurada reduce errores de automatizacion y build."
        },
        {
          "source": "Consistencia cita-bibliografia",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "Sin claves validas no hay trazabilidad de fuentes."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura argumentativa juridica",
          "kind": "develops",
          "justification": "La identidad institucional exige forma academica consistente."
        }
      ],
      "evidence": [
        "README y programa analitico del destino confirman contexto curricular y pauta editorial.",
        "Archivo .bib local contiene claves institucionales base verificables.",
        "Se detectan tokens Slug sin expandir y lineas con caracteres anómalos en README.",
        "Historial previo confirma incidencia de salidas no parseables y necesidad de normalizacion."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas equivalentes de identidad, estructura y gates.",
      "Se reforzo regla de no mezclar contexto curricular entre origen y destino.",
      "Se transfirieron solo abstracciones estables; se excluyo contenido tematico de Filosofia del Derecho.",
      "Se agrego control explicito sobre tokens Slug sin expandir por evidencia local.",
      "Se mantuvo estrategia progresiva y conservadora en ciclo 75."
    ]
  }
}