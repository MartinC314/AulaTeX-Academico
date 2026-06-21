{
  "summary": [
    "Se consolida sincronizacion transversal con reglas estables entre actividad origen y materia destino.",
    "Se preserva identidad UnADM y contexto curricular local del destino.",
    "Se refuerza normalizacion estructurada obligatoria antes de propagacion recursiva.",
    "Se incorporan ejes editoriales reutilizables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene estrategia conservadora: no transferir contenido tematico especifico de Filosofia del Derecho."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local de la materia destino sin mezclar nombres de otras asignaturas.",
    "Alinear entregables al contexto curricular verificado del destino: Licenciatura en Derecho, semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como procedencia provisional, no como identidad del entregable."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear la estructura al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Distinguir reporte, presentacion y producto visual segun consigna."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes.",
    "Distinguir hechos, argumentos, normas y criterio propio."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna de la actividad."
  ],
  "latex_rules": [
    "Reutilizar plantilla .tex local del destino sin romper identidad institucional.",
    "Usar codificacion y acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Corregir tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico antes de referenciar nombres de archivo.",
    "Revisar y cerrar correctamente entornos LaTeX abiertos antes de compilar [supuesto: existe corte de tabular en reporte base]."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de cada actividad en el .bib local de la materia destino.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Validar que toda clave citada exista en el .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales verificadas y no duplicadas.",
    "Aplicar compresion lossless por union y deduplicacion.",
    "Evitar regresiones: conservar reglas utiles previas aunque cambie su categoria.",
    "No propagar supuestos como reglas definitivas.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual en nodos no equivalentes."
  ],
  "open_questions": [
    "Confirmar criterio editorial final sobre uso de publico sin acento frente a publico con acento en nombres visibles.",
    "Confirmar correccion definitiva de nombres con caracteres anómalos en README.",
    "Confirmar reparacion del entorno tabular cortado en reporte base del destino.",
    "Confirmar si todas las actividades del destino usan un solo .bib o .bib por actividad.",
    "Supuesto: el archivo .bib canónico del destino es bases-de-derecho-internacional-publico.bib; validar en automatizaciones."
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
        "Destino: semestre 4, bloque 1, obligatoria, 8 creditos.",
        "No mezclar metadatos curriculares del origen con el destino."
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
      "Convertir planeacion semanal en entregables juridicos claros, fundados y evaluables.",
      "Asegurar trazabilidad editorial entre consigna, desarrollo, evidencia y cierre."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y no redundantes.",
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
          "justification": "La forma del entregable depende del producto solicitado."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica valida requiere respaldo documental."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia segura."
        },
        {
          "source": "Consistencia cita-bibliografia",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita afirmaciones sin fuente y referencias rotas."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura argumentativa juridica",
          "kind": "develops",
          "justification": "El formato y tono institucional guian la construccion del entregable."
        }
      ],
      "evidence": [
        "README del destino: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico del destino: proposito y ejes de trabajo.",
        "Bibliografia local del destino con claves institucionales existentes.",
        "Memoria origen: regla estable de normalizacion estructurada previa a propagacion."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas en summary, identidad, estructura y gates.",
      "Se conservaron reglas institucionales previas sin recorte funcional.",
      "Se transfirieron solo abstracciones estables por relacion transversal.",
      "Se excluyo contenido tematico especifico del origen por no equivalencia de nodo.",
      "Se marcaron supuestos tecnicos pendientes de verificacion local."
    ]
  }
}