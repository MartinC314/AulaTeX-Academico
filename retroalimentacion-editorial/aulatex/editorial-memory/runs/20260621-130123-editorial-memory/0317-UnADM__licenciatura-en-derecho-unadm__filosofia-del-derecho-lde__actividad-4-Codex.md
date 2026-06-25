{
  "summary": [
    "Se consolida memoria lateral para Actividad 4 con deduplicacion lossless.",
    "Se preserva identidad UnADM y marco curricular verificable.",
    "Se refuerza validacion JSON estricta por antecedentes no parseables.",
    "Se transfieren solo patrones reutilizables desde Actividad 1.",
    "Supuesto: falta consigna local completa de Actividad 4."
  ],
  "identity_rules": [
    "Mantener tono formal academico y precision juridica.",
    "Alinear contenido con UnADM y Licenciatura en Derecho.",
    "Mantener referencia curricular: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto pedido en la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante.",
    "Evitar entrega solo descriptiva o de resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Adaptar reglas al tipo de producto real de Actividad 4 cuando se confirme consigna."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar.",
    "Normalizar respuestas no estructuradas heredadas antes de propagar.",
    "Validar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y .bib."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Citar solo claves existentes en el .bib activo.",
    "Mantener claves BibTeX estables para evitar roturas.",
    "Evitar comandos no estandar sin justificacion.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Verificar nombres reales de archivos del README con tokens sin resolver."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y juridicas verificables.",
    "No inventar referencias ni metadatos.",
    "Registrar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a otra actividad; validar uso en Actividad 4."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Reutilizar reglas institucionales sin perder especificidad local.",
    "Evitar copiar conclusiones o bibliografia exclusiva entre hermanos.",
    "Propagar patrones, no redaccion literal.",
    "Mantener bandera de normalizacion manual para ciclos con salidas defectuosas."
  ],
  "open_questions": [
    "Confirmar consigna textual completa de Actividad 4.",
    "Confirmar producto requerido: reporte, presentacion u otro.",
    "Confirmar rubrica de evaluacion especifica.",
    "Confirmar archivo .bib canonico final con slug resuelto.",
    "Confirmar si Actividad 4 reutiliza bibliografia existente o requiere .bib incremental."
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
        "Entrada canonica en carpeta de asignatura.",
        "Normalizacion estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura Filosofia del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema, conceptos, evidencia, analisis propio y conclusion juridica.",
      "Transferencia profesional del cierre argumentativo.",
      "Trazabilidad de fuentes y consistencia estructural."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables.",
      "Asegurar fundamento juridico con criterio propio.",
      "Preservar memoria editorial reutilizable sin perdida."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales separadas.",
      "Cita explicita por afirmacion relevante.",
      "Supuestos marcados cuando falten datos locales."
    ],
    "argumentative_patterns": [
      "Plantear problema.",
      "Definir conceptos y marco normativo.",
      "Contrastar fuentes con analisis propio.",
      "Fijar postura justificada.",
      "Concluir con aplicabilidad juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ejes editoriales de Filosofia del Derecho",
        "Validacion JSON estricta",
        "Normalizacion estructurada",
        "Integridad academica y verificabilidad",
        "Relacion problema-evidencia-conclusion juridica"
      ],
      "citations": [
        "README.md",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Tono formal academico",
          "kind": "supports",
          "justification": "La pauta editorial exige alineacion institucional constante."
        },
        {
          "source": "Ejes editoriales de Filosofia del Derecho",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Los ejes ordenan problema, fuentes, analisis y cierre."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin salida estructurada no hay transferencia segura."
        },
        {
          "source": "Integridad academica y verificabilidad",
          "target": "Conclusion juridica propia",
          "kind": "supports",
          "justification": "La conclusion valida depende de evidencia y citas."
        }
      ],
      "evidence": [
        "README fija identidad UnADM, entrada canonica y conclusion juridica propia.",
        "Programa analitico fija cinco ejes de trabajo transferibles.",
        "Antecedentes de salidas no parseables justifican gate JSON estricto.",
        "Supuesto: consigna de Actividad 4 no visible en el contexto recibido."
      ]
    },
    "reinforcement_log": [
      "Ciclo 14: deduplicacion de reglas repetidas y variantes ortograficas.",
      "Ciclo 14: eliminada transferencia de contenido especifico de Actividad 1 no reutilizable.",
      "Ciclo 14: mantenidas reglas de calidad, estructura e identidad con mayor trazabilidad.",
      "Ciclo 14: reforzada distincion entre patrones transferibles y datos locales pendientes."
    ]
  }
}