{
  "summary": [
    "Se consolida memoria de materia desde actividad-1 con abstraccion ascendente.",
    "Se preserva compresion lossless por union y deduplicacion sin regresion.",
    "Se mantiene normalizacion obligatoria para insumos no JSON parseable.",
    "Se refuerzan ejes editoriales transferibles: problema, conceptos, evidencia, analisis propio y conclusion juridica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y trazabilidad.",
    "Alinear entregables con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica de actividades y entregables.",
    "Marcar como [supuesto] todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local. [supuesto]",
    "Conservar referencia a malla-curricular-derecho-unadm.pdf como base curricular verificada."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener trazabilidad entre actividad, .tex y .bib de materia."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante y evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir fuentes de semanas posteriores para actividad-1 sin verificacion. [supuesto]",
    "Confirmar que el tipo de producto coincida con la consigna de la actividad."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar correspondencia entre citas en texto y entradas del .bib.",
    "Evitar eliminar reglas utiles previas en cada ciclo."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables y no renombrarlas sin migracion completa.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres o rutas anomalas antes de fijarlas como canon. [supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente/editorial o URL.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "Registrar fuentes de actividad en el .bib de la materia con deduplicacion lossless.",
    "No completar entradas truncadas sin verificacion local. [supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas por README, programa analitico y .bib local.",
    "Elevar patrones editoriales reutilizables, no redaccion literal de actividades.",
    "Conservar trazabilidad de citas recurrentes y puertas de calidad al subir de nivel.",
    "Aplicar normalizacion manual en ciclos con insumos no estructurados.",
    "Mantener etiqueta de compresion union-dedupe lossless en propagaciones."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-1 para fijar plantilla final.",
    "Confirmar nombre canonico definitivo del archivo .bib de la materia. [supuesto]",
    "Determinar si filosofia-del-derecho-clean.bib es solo de Semana 7 o reutilizable por otras actividades. [supuesto]",
    "Verificar y completar localmente la entrada truncada scjnIncapacidadResistencia2019. [supuesto]"
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
      "Uso de conceptos, normas y doctrina pertinentes.",
      "Evidencia verificable con citas trazables.",
      "Analisis propio con postura academica.",
      "Conclusion juridica aplicable."
    ],
    "reason_for_being": [
      "Orientar productos academicos con claridad, fundamento juridico y transferencia profesional.",
      "Convertir planeacion semanal en entregables con estructura estable y verificable."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado explicito y consistente.",
      "Marcado expreso de [supuesto].",
      "Cierre con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer marco conceptual y normativo.",
      "Analizar con postura propia y evidencia.",
      "Concluir con transferibilidad profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofia del Derecho",
        "Hermeneutica e interpretacion juridica",
        "Argumentacion juridica",
        "Derecho y moral",
        "Justicia",
        "Analisis critico del fenomeno juridico",
        "Ejes editoriales de cinco pasos"
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
          "justification": "La interpretacion aporta criterios para construir argumentos."
        },
        {
          "source": "Argumentacion juridica",
          "target": "Analisis critico del fenomeno juridico",
          "kind": "develops",
          "justification": "La argumentacion permite evaluar validez y consecuencias."
        },
        {
          "source": "Marco normativo y doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "La conclusion requiere soporte normativo verificable."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "La materia integra debate axiologico y juridico."
        }
      ],
      "evidence": [
        "README de materia para identidad y ubicacion curricular.",
        "Programa analitico para proposito y ejes de trabajo.",
        "Reglas heredadas de actividad-1 para patron argumentativo transferible.",
        "Reglas de calidad sobre JSON parseable y normalizacion previa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 29: se eleva patron de actividad a nivel materia sin perdida semantica.",
      "Ciclo 29: se deduplican reglas repetidas y se conservan todas las utiles.",
      "Ciclo 29: se mantiene control estricto de ingesta no estructurada.",
      "Ciclo 29: se refuerza trazabilidad curricular, bibliografica y de compilacion LaTeX."
    ]
  }
}