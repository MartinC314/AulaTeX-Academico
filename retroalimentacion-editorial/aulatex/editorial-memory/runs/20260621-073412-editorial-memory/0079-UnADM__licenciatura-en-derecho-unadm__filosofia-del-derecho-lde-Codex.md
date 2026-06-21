{
  "summary": [
    "Se consolida en materia la memoria valida de actividad-1 con abstraccion ascendente.",
    "Se mantiene compresion lossless por union y deduplicacion sin regresion.",
    "Se preserva identidad UnADM, trazabilidad curricular y calidad de ingesta estructurada.",
    "Se refuerzan ejes editoriales transferibles: problema, conceptos, evidencia, analisis propio y conclusion juridica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en redaccion y formato.",
    "Alinear entregables con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local. [supuesto]",
    "Conservar referencia provisional Codex como riesgo historico de ingesta. [supuesto]",
    "Conservar referencia provisional GPT-Pro desde actividad-1 hasta sustitucion verificada. [supuesto]"
  ],
  "structure_rules": [
    "Iniciar cada producto con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear el tipo de producto a la planeacion semanal.",
    "Mantener trazabilidad entre actividad, archivo .tex y .bib de materia."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar entregas solo descriptivas.",
    "No asumir que fuentes de semanas posteriores aplican automaticamente a actividad-1.",
    "Agregar fuentes especificas de actividad solo cuando sean verificables."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna de la actividad."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "No renombrar claves citadas sin migracion completa.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo anomalos antes de declararlos canonicos. [supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "Registrar fuentes de actividad en el .bib de la asignatura.",
    "Tratar filosofia-del-derecho-clean.bib como archivo tematico de Semana 7, no canon general automatico. [supuesto]",
    "No completar entradas truncadas sin verificacion local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas por README, programa analitico y .bib local.",
    "Elevar patrones reutilizables desde actividades sin copiar redaccion literal.",
    "Mantener puertas de calidad institucional en nodos ancestro y laterales.",
    "Registrar incidencias de no parseable como riesgo de ingesta sin perder contenido util.",
    "Evitar propagar placeholders o nombres anomalos hasta correccion local."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-1 y su producto final.",
    "Confirmar nombre canonico definitivo del .bib de la materia.",
    "Resolver en origen los placeholders $(@{...}.Slug) en README y programa analitico.",
    "Confirmar si actividad-1 requiere .bib propio o reutiliza bibliografia de materia.",
    "Verificar integridad completa de la entrada scjnIncapacidadResistencia2019. [supuesto]"
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
        "Carpeta de materia como entrada canonica editorial."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Filosofia del Derecho."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas y doctrina pertinentes.",
      "Evidencia verificable.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos con fundamento juridico, evidencia y criterio propio.",
      "Sostener una memoria editorial persistente, trazable y reutilizable sin perdida."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable por funcion argumentativa.",
      "Marcado explicito de supuestos.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer marco conceptual y normativo.",
      "Analizar con postura propia y evidencia.",
      "Concluir con aplicacion juridica.",
      "Verificar coherencia interna del hilo argumental."
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
          "justification": "La interpretacion sustenta la formulacion de razones juridicas."
        },
        {
          "source": "Argumentacion juridica",
          "target": "Analisis critico del fenomeno juridico",
          "kind": "develops",
          "justification": "La argumentacion permite evaluar validez, alcance y consecuencias."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "El curso integra debate axiologico y normativo."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "La conclusion exige respaldo normativo verificable."
        }
      ],
      "evidence": [
        "README de materia: identidad y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "Actividad-1: patron estable de construccion argumentativa.",
        "Reglas de calidad: bloqueo por no parseable y normalizacion obligatoria.",
        "Bibliografia local: claves juridicas recurrentes verificables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 79: se elevan patrones del hijo al ancestro con deduplicacion semantica.",
      "Ciclo 79: se preservan reglas historicas utiles de calidad y normalizacion.",
      "Ciclo 79: se mantiene trazabilidad de citas recurrentes sin inventar fuentes.",
      "Ciclo 79: se consolidan conexiones entre identidad institucional y patron argumentativo."
    ]
  }
}