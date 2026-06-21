{
  "summary": [
    "Se refuerza sincronizacion transversal con reglas estables y sin mezclar contenido tematico de Filosofia del Derecho.",
    "Se conserva identidad UnADM y contexto curricular local del destino: semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Se consolida compresion lossless por deduplicacion y union de reglas utiles previas.",
    "Se prioriza estructura reusable: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene bloqueo de propagacion ante salidas no parseables y necesidad de normalizacion estructurada."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local de la materia en todos los entregables.",
    "Usar contexto curricular verificado solo desde README y programa analitico del destino.",
    "No mezclar metadatos curriculares del nodo origen con el destino.",
    "Tratar Codex y GPT-Pro como procedencia provisional, no como identidad del entregable.",
    "Marcar como supuesto todo dato no visible en la consigna local."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear la forma final al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Distinguir reporte, presentacion y producto visual segun consigna."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Integrar normas, doctrina o datos pertinentes al caso.",
    "Evitar extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre consigna, producto solicitado y entregable final."
  ],
  "latex_rules": [
    "Reutilizar plantillas .tex locales sin romper identidad institucional.",
    "Mantener compatibilidad con article, spanish, letterpaper y oneside.",
    "Completar metadatos de portada segun actividad en curso.",
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Corregir tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Revisar y cerrar entornos tabular antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de actividad en el .bib local de la materia.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Validar que toda clave citada exista en el .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas, generales y no duplicadas.",
    "Aplicar estrategia conservadora: transferir abstracciones editoriales, no redaccion literal.",
    "Preservar reglas utiles previas y evitar regresiones.",
    "No propagar supuestos como reglas definitivas.",
    "Registrar incidencias historicas de parseo como memoria de riesgo operativo."
  ],
  "open_questions": [
    "Confirmar criterio editorial final sobre publico sin acento vs publico con acento en nombres visibles.",
    "Confirmar correccion completa de tokens $(@{...}.Slug) en README y programa analitico.",
    "Confirmar reparacion del corte de entorno tabular en reporte-bases-de-derecho-internacional-publico.tex.",
    "Confirmar si existe rubrica local por actividad para ajustar profundidad argumentativa.",
    "Supuesto: no se transfiere bibliografia tematica de Filosofia del Derecho por no equivalencia disciplinar directa."
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
      "Identidad institucional valida.",
      "Consigna como ancla del producto.",
      "Estructura juridico-argumentativa reusable.",
      "Evidencia verificable y trazable.",
      "Conclusion transferible a practica profesional."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables claros, verificables y juridicamente fundados.",
      "Sostener coherencia entre consigna, desarrollo y cierre.",
      "Asegurar propagacion segura entre nodos con control de calidad."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales sin redundancia.",
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
          "justification": "La consigna define formato, alcance y producto."
        },
        {
          "source": "Estructura argumentativa juridica",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "Un desarrollo ordenado habilita cierre profesional util."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion requiere respaldo documental para ser valida."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo valido no hay transferencia segura."
        },
        {
          "source": "Consistencia cita-bibliografia",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "Evita citas huerfanas y fortalece trazabilidad."
        }
      ],
      "evidence": [
        "README del destino: contexto curricular y pauta editorial.",
        "Programa analitico del destino: ejes de trabajo y proposito.",
        "Archivo .bib local: claves institucionales base.",
        "Historial de ciclos: incidencias de salida no parseable y regla de normalizacion."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas conservando semantica.",
      "Se preservaron gates de parseo y normalizacion como bloque critico.",
      "Se transfirieron solo abstracciones estables entre nodos no equivalentes.",
      "Se evito migrar contenido doctrinal especifico de Filosofia del Derecho.",
      "Se reforzo grafo conceptual orientado a consistencia editorial transversal."
    ]
  }
}