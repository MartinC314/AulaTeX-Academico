{
  "summary": [
    "Se consolida memoria lateral para Actividad 5 con deduplicacion lossless.",
    "Se preserva identidad UnADM y contexto curricular de Derecho, semestre 1, bloque 2.",
    "Se refuerza normalizacion JSON obligatoria antes de propagacion recursiva.",
    "Se mantienen ejes editoriales: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se transfiere solo patron reusable desde Actividad 1; no contenido literal ni conclusiones especificas."
  ],
  "identity_rules": [
    "Mantener tono formal academico y precision juridica.",
    "Alinear toda entrega a UnADM y Licenciatura en Derecho.",
    "Conservar encuadre de asignatura: Filosofia del Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar memorias de modelo previo como fuente provisional, no academica."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Distinguir en cada bloque: afirmacion, evidencia e inferencia.",
    "Alinear el formato final al producto pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Adaptar el contenido al enunciado real de Actividad 5.",
    "Evitar entrega solo descriptiva; incluir postura argumentada.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No arrastrar bibliografia de otra semana sin validar pertinencia.",
    "Si falta dato operativo, declarar supuesto y continuar con consistencia."
  ],
  "quality_gates": [
    "Bloquear propagacion si no hay JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar.",
    "Confirmar respaldo o marca de supuesto en cada afirmacion relevante.",
    "Validar consistencia entre citas en texto y claves del .bib.",
    "Verificar que el producto responda a la consigna y no solo resuma.",
    "Aplicar revision manual extra por historial de incidentes de parseo."
  ],
  "latex_rules": [
    "Usar acentos y codificacion en espanol de forma consistente.",
    "Mantener claves BibTeX estables ya citadas en .tex.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y rutas.",
    "Supuesto: .bib canonico esperado es filosofia-del-derecho.bib hasta verificacion local."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Registrar en .bib solo fuentes realmente citadas.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a Semana 7; validar uso en Actividad 5."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Reutilizar reglas institucionales sin perder especificidad local.",
    "Aplicar union y deduplicacion; no recortar reglas utiles previas.",
    "No propagar como academicas fuentes provisionales de modelos.",
    "Cuando falte consigna local, propagar plantilla estructural y preguntas abiertas."
  ],
  "open_questions": [
    "Confirmar enunciado exacto de Actividad 5.",
    "Confirmar rubrica de evaluacion de Actividad 5.",
    "Confirmar tipo de producto requerido: reporte, presentacion o recurso visual.",
    "Confirmar nombre canonico final del archivo .bib.",
    "Confirmar pertinencia de bibliografia de Interpretacion juridica para Actividad 5."
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
        "Carpeta de asignatura como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Filosofia del Derecho."
      ]
    },
    "essence": [
      "Problema juridico o social como punto de partida.",
      "Conceptos y marco normativo pertinentes.",
      "Analisis propio sustentado en evidencia.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables.",
      "Garantizar trazabilidad entre consigna, argumentos, fuentes y cierre."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales sin ornamento.",
      "Postura personal sustentada.",
      "Uso explicito de supuestos."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> inferencia juridica.",
      "Contraste doctrinal breve -> toma de postura."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Problema juridico",
        "Marco normativo o doctrinal",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion JSON",
        "Consistencia cita-.bib"
      ],
      "citations": [
        "README.md",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Estructura de actividad",
          "kind": "supports",
          "justification": "Define tono, integridad y forma del entregable."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere una pregunta delimitada."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica valida exige respaldo trazable."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia confiable."
        },
        {
          "source": "Bibliografia base",
          "target": "Bibliografia especifica de actividad",
          "kind": "contrasts",
          "justification": "La base orienta; la especifica responde a la consigna."
        }
      ],
      "evidence": [
        "README fija identidad UnADM, citas verificables y conclusion juridica propia.",
        "Programa analitico fija ejes problema-conceptos-fuentes-analisis-cierre.",
        "Historial confirma necesidad de gate por salidas no parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 8: deduplicadas reglas repetidas de identidad, estructura y calidad.",
      "Ciclo 8: reforzada separacion entre bibliografia base y especifica.",
      "Ciclo 8: mantenida regla de supuestos explicitos por falta de consigna local.",
      "Ciclo 8: preservada restriccion de no transferir conclusiones ni bibliografia exclusiva entre hermanos."
    ]
  }
}