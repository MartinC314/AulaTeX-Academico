{
  "summary": [
    "Se sincronizan reglas transversales estables desde actividad origen a materia destino sin mezclar contenido tematico.",
    "Se conserva identidad UnADM y contexto curricular local del destino.",
    "Se refuerza normalizacion estructurada obligatoria antes de propagacion recursiva.",
    "Se mantiene compresion lossless por union y deduplicacion.",
    "Supuesto: no se transfiere bibliografia tematica de Filosofia del Derecho por no equivalencia de asignatura."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local de la materia en todos los entregables.",
    "Usar solo contexto curricular verificado del destino.",
    "No mezclar metadatos curriculares entre materias distintas.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como procedencia provisional."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear la estructura al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Distinguir reporte, presentacion y producto visual segun consigna.",
    "Conservar separacion entre README, programa analitico, .tex y .bib."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, normas, doctrina y criterio propio.",
    "Evitar extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna activa.",
    "Mantener auditoria de parseo JSON por ciclo."
  ],
  "latex_rules": [
    "Reutilizar plantilla .tex local de la materia como base.",
    "Mantener compatibilidad con clase article, spanish, letterpaper y oneside.",
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo con caracteres anomalos antes de referenciar.",
    "No alterar estructura base de portada sin instruccion editorial."
  ],
  "bibliography_rules": [
    "Registrar fuentes de actividad en el .bib local de la materia.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Validar que toda clave citada exista en el .bib local."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables en saltos transversales.",
    "Evitar transferir redaccion literal y contenido tematico de materia no equivalente.",
    "Preservar reglas utiles previas sin regresion.",
    "Aplicar union-dedupe lossless en cada ciclo.",
    "No promover supuestos a reglas definitivas.",
    "Si falta contexto local, mantener cerebro minimo y abrir preguntas."
  ],
  "open_questions": [
    "Confirmar criterio editorial final sobre publico sin acento o publico con acento en nombres visibles.",
    "Confirmar y corregir corte de entorno tabular en el reporte base del destino.",
    "Confirmar normalizacion definitiva de tokens Slug en README y programa analitico.",
    "Supuesto: la consigna de actividades futuras mantendra eje problema-conceptos-evidencia-analisis-conclusion.",
    "Confirmar si existe rubrica institucional especifica para Bases de derecho internacional publico."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador ante evidencia incompleta."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada obligatoria antes de propagacion.",
        "Trazabilidad de fuentes provisionales sin convertirlas en autoridad."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Destino: semestre 4, bloque 1, obligatoria, 8 creditos.",
        "Asignatura destino: Bases de derecho internacional publico.",
        "Codigo local: LDE-S4B1."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo o doctrinal.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros y verificables.",
      "Sostener calidad editorial transversal sin contaminar contexto curricular local.",
      "Garantizar salidas reutilizables mediante estructura y validacion."
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
          "justification": "La conclusion juridica requiere sustento documental."
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
          "justification": "Evita afirmaciones sin fuente y referencias rotas."
        }
      ],
      "evidence": [
        "README destino con pauta editorial y ubicacion curricular.",
        "Programa analitico destino con ejes de trabajo.",
        "bases-de-derecho-internacional-publico.bib con claves institucionales base.",
        "Regla heredada valida: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 20: se consolidan reglas transversales de estructura y calidad sin traslado tematico.",
      "Ciclo 20: se preserva trazabilidad de fuentes provisionales como metadato.",
      "Ciclo 20: se refuerza gate de normalizacion JSON como condicion de propagacion."
    ]
  }
}