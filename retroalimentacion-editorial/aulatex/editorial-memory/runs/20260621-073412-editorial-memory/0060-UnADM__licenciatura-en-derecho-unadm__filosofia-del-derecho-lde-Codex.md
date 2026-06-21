{
  "summary": [
    "Se consolida memoria de materia desde actividad-1 con abstraccion ascendente y deduplicacion lossless.",
    "Se preservan reglas utiles previas sin regresion y se refuerza identidad UnADM.",
    "Se fija normalizacion obligatoria para insumos no JSON parseable antes de cualquier propagacion.",
    "Se elevan ejes transferibles: problema, conceptos, evidencia, analisis propio y conclusion juridica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y trazabilidad.",
    "Alinear entregables con Licenciatura en Derecho: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local. [supuesto]",
    "Conservar referencia institucional de malla curricular como respaldo curricular verificado."
  ],
  "structure_rules": [
    "Iniciar cada producto con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener trazabilidad entre actividad, archivo .tex y .bib de la materia."
  ],
  "activity_rules": [
    "Evitar entregas solo descriptivas; exigir postura argumentada del estudiante.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir que fuentes de semanas posteriores aplican automaticamente a actividad-1. [supuesto]",
    "Agregar fuentes especificas de actividad solo tras verificacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de [supuesto].",
    "Validar consistencia entre citas en texto y entradas en .bib.",
    "Verificar correspondencia del producto con la consigna vigente."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol para .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar sin migracion completa.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo anomalos antes de tratarlos como canon. [supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Registrar fuentes de actividad en el .bib de la materia con deduplicacion sin perdida.",
    "No completar entradas truncadas sin verificacion local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas y normalizadas.",
    "Elevar patrones reutilizables del hijo al ancestro sin copiar redaccion literal.",
    "Reusar puertas de calidad institucionales en nodos laterales de Derecho.",
    "Mantener etiqueta de compresion union-dedupe lossless en cada ciclo.",
    "Conservar trazabilidad de incidencias de ingesta no parseable como riesgo operativo."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-1 para fijar producto final.",
    "Confirmar nombre canonico definitivo del archivo .bib de la materia. [supuesto]",
    "Determinar si filosofia-del-derecho-clean.bib es solo semanal o base reutilizable. [supuesto]",
    "Completar y verificar la entrada truncada scjnIncapacidadResistencia2019. [supuesto]",
    "Sustituir referencias provisionales heredadas (Codex/GPT-Pro) por fuentes verificadas locales."
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
        "Materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Filosofia del Derecho."
      ]
    },
    "essence": [
      "Problema juridico o social bien delimitado.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable con citas trazables.",
      "Analisis propio con postura academica.",
      "Conclusion juridica aplicable a la practica."
    ],
    "reason_for_being": [
      "Orientar productos academicos consistentes con identidad UnADM y rigor juridico.",
      "Convertir planeacion semanal en entregables trazables y evaluables.",
      "Sostener continuidad editorial entre actividades, materia y propagacion institucional."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable y funcional.",
      "Marcado explicito de [supuesto].",
      "Cierre con transferencia profesional."
    ],
    "argumentative_patterns": [
      "Delimitacion del problema -> marco conceptual/normativo -> analisis critico -> conclusion transferible.",
      "Afirmacion sustantiva -> evidencia verificable -> inferencia juridica.",
      "Consigna de actividad -> estructura del producto -> validacion de calidad."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofia del Derecho",
        "Hermeneutica e interpretacion juridica",
        "Argumentacion juridica",
        "Derecho y moral",
        "Justicia",
        "Analisis critico del fenomeno juridico",
        "Problema-conceptos-evidencia-analisis-conclusion"
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
          "justification": "La interpretacion provee criterios para construir argumentos juridicos."
        },
        {
          "source": "Argumentacion juridica",
          "target": "Analisis critico del fenomeno juridico",
          "kind": "develops",
          "justification": "La argumentacion permite evaluar razones, normas y efectos."
        },
        {
          "source": "Marco normativo y doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "La conclusion valida requiere soporte normativo verificable."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "La materia integra el debate entre validez juridica y valor moral."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "Bibliografia local .bib: claves juridicas recurrentes y trazables.",
        "Actividad-1: patron editorial estable transferido al nivel materia."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas con preservacion completa de contenido util.",
      "Se reforzo puerta de calidad JSON parseable como condicion de propagacion.",
      "Se elevo patron argumentativo central desde actividad-1 al ancestro materia.",
      "Se mantuvieron fuentes provisionales marcadas como [supuesto] hasta verificacion.",
      "Se preservo compatibilidad LaTeX/BibTeX y trazabilidad de citas recurrentes."
    ]
  }
}