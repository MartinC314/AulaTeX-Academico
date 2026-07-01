{
  "summary": [
    "Se consolida sincronizacion transversal conservadora desde actividad de origen hacia materia destino.",
    "Se preservan reglas utiles vigentes del destino y se deduplican sin recorte semantico.",
    "Se transfieren solo abstracciones estables: identidad UnADM, estructura argumentativa, control de supuestos y gates de calidad.",
    "Se evita trasladar contenido tematico especifico de Filosofia del Derecho al destino de Derecho Internacional Publico.",
    "Se refuerza normalizacion obligatoria de salidas estructuradas antes de propagacion recursiva.",
    "Supuesto: la consigna local por actividad aun no esta anexada en esta memoria de materia."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local de la materia: Bases de derecho internacional publico.",
    "Alinear entregables al contexto curricular verificado del destino: semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Usar codigo local de curso LDE-S4B1 en metadatos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "No mezclar metadatos curriculares de materias origen con el destino.",
    "Tratar Codex y GPT-Pro como procedencia provisional, no como identidad del entregable.",
    "Marcar como supuesto cualquier dato no visible en la consigna local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeacion semanal.",
    "Distinguir reporte, presentacion y producto visual segun consigna.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Conservar separacion documental entre README, programa analitico, .bib y plantillas .tex."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Integrar conceptos, normas, doctrina o datos pertinentes al caso.",
    "Distinguir hechos, argumentos, normas y criterio propio.",
    "Evitar extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna de actividad vigente.",
    "Validar sintaxis LaTeX y cierre de entornos antes de compilar."
  ],
  "latex_rules": [
    "Reutilizar plantilla .tex local de la materia sin romper identidad institucional.",
    "Mantener compatibilidad con clase article, spanish, letterpaper y oneside.",
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir caracteres anomalos en nombres de archivo antes de compilar.",
    "No cambiar estructura base de portada sin instruccion editorial."
  ],
  "bibliography_rules": [
    "Registrar fuentes de actividad en bases-de-derecho-internacional-publico.bib.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Validar que todas las claves citadas existan en el .bib local.",
    "Conservar entradas institucionales base: unadmSitioWeb y unadmMallaDerecho2024."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Aplicar compresion lossless por union y deduplicacion.",
    "Evitar regresiones respecto de reglas utiles previas.",
    "No propagar supuestos como reglas definitivas.",
    "Propagar transversalmente abstracciones estables, no redaccion literal.",
    "Mantener trazabilidad de incidencias historicas de parseo en cada ciclo.",
    "Ciclo 1 requiere normalizacion manual si se reutilizan salidas no estructuradas."
  ],
  "open_questions": [
    "Confirmar criterio editorial definitivo sobre uso de publico sin acento frente a publico con acento.",
    "Confirmar y corregir en README los nombres con caracteres anomalos observados.",
    "Confirmar resolucion de tokens $(@{...}.Slug) en README y programa analitico.",
    "Confirmar formato minimo de conclusion juridica por tipo de evidencia en esta materia.",
    "Supuesto: faltan consignas especificas por actividad para afinar reglas locales de producto."
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
        "Destino verificado: semestre 4, bloque 1, obligatoria, 8 creditos.",
        "Asignatura: Bases de derecho internacional publico.",
        "Codigo local: LDE-S4B1.",
        "No mezclar contexto curricular entre materias."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo o doctrinal.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible.",
      "Consistencia cita-bibliografia.",
      "Normalizacion JSON antes de propagacion."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos con rigor juridico y trazabilidad.",
      "Garantizar coherencia entre consigna, desarrollo, evidencia y cierre.",
      "Sostener un cerebro editorial reusable y estable para la materia destino."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales no redundantes.",
      "Supuestos siempre etiquetados.",
      "Cierre con criterio juridico aplicable.",
      "Sin extrapolaciones no verificadas."
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
        "Supuestos etiquetados"
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
          "source": "Supuestos etiquetados",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Separa hechos verificados de inferencias pendientes."
        }
      ],
      "evidence": [
        "README local de la materia destino.",
        "Programa analitico local de la materia destino.",
        "Archivo .bib local con claves institucionales existentes.",
        "Regla persistente heredada: revisar y normalizar salidas no estructuradas."
      ]
    },
    "reinforcement_log": [
      "Se reforzo gate de JSON parseable como condicion de propagacion.",
      "Se reforzo separacion entre procedencia provisional y identidad editorial.",
      "Se reforzaron ejes transversales reutilizables sin trasladar contenido tematico ajeno.",
      "Se consolidaron reglas de supuestos etiquetados y no invencion de fuentes.",
      "Se incorporo control de tokens sin expandir como higiene editorial-tecnica."
    ]
  }
}