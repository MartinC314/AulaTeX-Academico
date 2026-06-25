{
  "summary": [
    "Se consolida en la materia la memoria valida de actividad-1 con abstraccion ascendente y deduplicacion lossless.",
    "Se preserva identidad UnADM, ubicacion curricular verificada y punto de entrada canonico en carpeta de materia.",
    "Se refuerza el patron transversal: problema, conceptos y fuentes, analisis propio, conclusion juridica transferible.",
    "Se mantiene como regla dura la normalizacion previa de insumos no JSON parseable antes de cualquier propagacion.",
    "Se conserva trazabilidad entre consigna, producto .tex y soporte bibliografico .bib sin regresion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y criterios academicos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica editorial y operativa.",
    "Marcar como [supuesto] todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Usar malla-curricular-derecho-unadm.pdf como respaldo curricular verificado."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear el tipo de producto a la planeacion semanal.",
    "Cerrar con conclusion juridica aplicable a practica profesional.",
    "Mantener trazabilidad entre actividad, .tex y .bib."
  ],
  "activity_rules": [
    "Delimitar problema y pregunta guia al inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar solo descripcion.",
    "Verificar coherencia entre pregunta, desarrollo y conclusion.",
    "No asumir fuentes de semanas posteriores para actividad-1 sin verificacion.",
    "Validar que el producto final coincide con la consigna activa."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar memoria.",
    "Normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en texto y entradas .bib.",
    "Evitar regresion: no eliminar reglas utiles heredadas."
  ],
  "latex_rules": [
    "Usar espanol con acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar sin migracion completa.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Tratar nombres de archivo anomalos como pendientes, no como canon. [supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "Registrar fuentes de actividad en el .bib de la asignatura.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "No completar entradas truncadas sin verificacion local. [supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Elevar a niveles superiores reglas transferibles, no redaccion literal de actividades.",
    "Propagar puertas de calidad y trazabilidad como nucleo comun institucional.",
    "Mantener etiqueta union-dedupe lossless en cada ciclo.",
    "Aplicar normalizacion manual en nodos con historial no parseable.",
    "Propagar citas recurrentes solo con respaldo en .bib local verificable."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-1 para fijar plantilla final.",
    "Confirmar nombre canonico definitivo del .bib de la materia.",
    "Resolver placeholder Slug en README y programa analitico. [supuesto]",
    "Confirmar si filosofia-del-derecho-clean.bib es solo Semana 7 o reutilizable en otras actividades. [supuesto]",
    "Verificar integridad completa de scjnIncapacidadResistencia2019 en .bib local. [supuesto]"
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
      "Problema juridico o social que activa la asignatura.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable con cita.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos trazables y argumentativos.",
      "Sostener coherencia entre identidad institucional, metodologia y evidencia.",
      "Garantizar calidad tecnica LaTeX y calidad academica juridica en conjunto."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable por funcion argumentativa.",
      "Marcado explicito de [supuesto].",
      "Cierre con implicacion profesional."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Construir marco conceptual-normativo.",
      "Contrastar fuentes y elaborar postura propia.",
      "Concluir con criterio juridico aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofia del Derecho",
        "Hermeneutica e interpretacion juridica",
        "Argumentacion juridica",
        "Derecho y moral",
        "Justicia",
        "Analisis critico del fenomeno juridico",
        "Trazabilidad editorial actividad-materia"
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
          "justification": "La interpretacion sustenta la construccion de razones juridicas."
        },
        {
          "source": "Argumentacion juridica",
          "target": "Analisis critico del fenomeno juridico",
          "kind": "develops",
          "justification": "Permite evaluar normas, hechos y consecuencias."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "Articula validez normativa y dimension axiologica."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "La conclusion requiere soporte verificable."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        ".bib local: claves recurrentes de doctrina, normativa y jurisprudencia.",
        "Memoria de actividad-1: patron problema-conceptos-evidencia-analisis-conclusion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 22: se elevo patron argumentativo de actividad a materia sin copiar redaccion literal.",
      "Ciclo 22: se consolidaron puertas de calidad parseo JSON + estructura minima + no regresion.",
      "Ciclo 22: se mantuvieron fuentes provisionales como provisionales con marca [supuesto].",
      "Ciclo 22: se reforzo trazabilidad entre consigna, .tex y .bib como regla de sistema."
    ]
  }
}