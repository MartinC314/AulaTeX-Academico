{
  "summary": [
    "Se consolida memoria de materia desde actividad-1 con abstraccion ascendente y sin regresion.",
    "Se mantiene compresion lossless por union-deduplicacion en reglas y trazas.",
    "Se preserva normalizacion obligatoria de insumos no JSON parseable antes de propagar.",
    "Se fijan ejes editoriales transferibles: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se refuerza trazabilidad entre consigna, .tex, .bib y criterio institucional UnADM."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, redaccion y formato.",
    "Alinear la materia a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica de la asignatura.",
    "Marcar como [supuesto] todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local. [supuesto]",
    "Usar malla-curricular-derecho-unadm.pdf como respaldo curricular verificado."
  ],
  "structure_rules": [
    "Abrir cada entregable con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear el formato final al producto solicitado por la planeacion semanal.",
    "Mantener trazabilidad entre actividad, archivo .tex y archivo .bib."
  ],
  "activity_rules": [
    "Iniciar cada actividad con problema delimitado y pregunta guia.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir fuentes de semanas posteriores como obligatorias para actividad-1. [supuesto]",
    "Agregar bibliografia especifica de actividad solo si es comprobable."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en .tex y entradas en .bib.",
    "Verificar correspondencia del producto con la consigna vigente."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar sin migracion completa.",
    "Compilar sin errores criticos, referencias rotas ni claves huerfanas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "No adoptar nombres de archivo anomalos como canon hasta corregirlos localmente. [supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Distinguir bibliografia base de materia y bibliografia especifica de actividad.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Registrar fuentes de actividad en el .bib de la asignatura con deduplicacion lossless.",
    "Mantener como provisional el uso de filosofia-del-derecho-clean.bib fuera de su semana declarada. [supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas por README, programa analitico y .bib local.",
    "Elevar patrones reutilizables del hijo al ancestro sin copiar redaccion literal extensa.",
    "Conservar trazabilidad de citas recurrentes y puertas de calidad institucionales.",
    "Aplicar union-deduplicacion sin eliminar reglas utiles previas.",
    "Registrar incidencias de parseo como riesgo de ingesta, no como perdida de memoria.",
    "Mantener etiqueta de normalizacion manual para ciclos con insumos no estructurados."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-1 para fijar producto definitivo. [supuesto]",
    "Confirmar nombre canonico final del .bib de la materia tras resolver token Slug. [supuesto]",
    "Confirmar si actividad-1 debe usar .bib propio o reutilizar bibliografia general. [supuesto]",
    "Verificar integridad completa de la entrada scjnIncapacidadResistencia2019 en .bib. [supuesto]",
    "Confirmar rubrica de evaluacion para calibrar profundidad argumentativa. [supuesto]"
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
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Filosofia del Derecho."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo-doctrinal.",
      "Evidencia verificable.",
      "Analisis propio con postura.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables juridicos rigurosos.",
      "Asegurar trazabilidad academica entre consigna, argumentacion y fuentes.",
      "Sostener una memoria editorial reutilizable y verificable en ciclos sucesivos."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable.",
      "Marcado explicito de supuestos.",
      "Cierre con criterio juridico propio.",
      "Consistencia terminologica y curricular."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer conceptos y marco normativo.",
      "Contrastar fuentes y construir analisis propio.",
      "Concluir con aplicacion practica juridica.",
      "Verificar coherencia interna y soporte de citas."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofia del Derecho",
        "Hermeneutica e interpretacion juridica",
        "Argumentacion juridica",
        "Derecho y moral",
        "Justicia",
        "Analisis critico del fenomeno juridico",
        "Ejes editoriales de cinco pasos",
        "Trazabilidad .tex-.bib-consigna"
      ],
      "citations": [
        "hernandezManriquezHermeneutica2019",
        "scjnMemoriaArgumentacion2008",
        "scjnViolenciaFisica2022",
        "scjnIncapacidadResistencia2019",
        "ruiz_rodriguez_filosofia_derecho_2009",
        "rojas_gonzalez_filosofia_derecho_2018",
        "noauthor_constitucion_nodate",
        "de_victimas_ley_2013"
      ],
      "relations": [
        {
          "source": "Hermeneutica e interpretacion juridica",
          "target": "Argumentacion juridica",
          "kind": "supports",
          "justification": "La interpretacion sostiene la construccion de razones juridicas."
        },
        {
          "source": "Argumentacion juridica",
          "target": "Analisis critico del fenomeno juridico",
          "kind": "develops",
          "justification": "El analisis critico requiere razonamiento argumentativo."
        },
        {
          "source": "Marco normativo y doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "La conclusion valida depende de soporte normativo verificable."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "La materia articula validez juridica y dimension axiologica."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "filosofia-del-derecho-clean.bib: claves juridicas recurrentes.",
        "Memoria de actividad-1: patron problema-conceptos-evidencia-analisis-conclusion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 21: se elevo patron argumentativo de actividad-1 a materia.",
      "Ciclo 21: se mantuvo regla dura de bloqueo por JSON no parseable.",
      "Ciclo 21: se deduplicaron reglas repetidas sin perdida semantica.",
      "Ciclo 21: se preservaron fuentes provisionales con marcado [supuesto].",
      "Ciclo 21: se reforzo trazabilidad curricular y bibliografica verificable."
    ]
  }
}