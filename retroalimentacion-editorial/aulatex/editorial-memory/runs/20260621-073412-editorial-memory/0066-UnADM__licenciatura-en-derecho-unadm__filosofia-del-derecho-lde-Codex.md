{
  "summary": [
    "Consolidar memoria de materia con abstraccion ascendente desde actividad-1.",
    "Preservar reglas utiles previas sin regresion y con deduplicacion lossless.",
    "Mantener normalizacion estructurada obligatoria antes de propagar.",
    "Fijar ejes editoriales transferibles: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Registrar riesgos de ingesta por salidas no JSON parseable sin perder contenido valido."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear la materia a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica de entregables.",
    "Marcar como [supuesto] todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local. [supuesto]",
    "Usar malla-curricular-derecho-unadm.pdf como respaldo curricular verificado."
  ],
  "structure_rules": [
    "Iniciar cada producto con encuadre breve del problema juridico o social.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear el entregable al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener trazabilidad entre actividad, archivo .tex y .bib de materia."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante y evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir que fuentes de semanas posteriores aplican a actividad-1. [supuesto]",
    "Confirmar que el producto corresponde a la consigna especifica de cada actividad.",
    "Agregar fuentes especificas de actividad solo cuando sean verificables."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar no regresion: no eliminar reglas utiles heredadas."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables y no renombrarlas sin migracion completa.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo anomalos antes de fijarlos como canon. [supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente editorial o URL.",
    "Registrar fuentes de actividad en el .bib de la asignatura con trazabilidad.",
    "No completar entradas truncadas sin verificacion local. [supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Elevar al ancestro solo patrones reutilizables, no redaccion literal del hijo.",
    "Reusar puertas de calidad institucionales en nodos laterales de Derecho.",
    "Aplicar union-dedupe lossless en cada ciclo para evitar duplicados.",
    "Mantener trazabilidad de citas recurrentes y conceptos nucleares.",
    "Si falta consigna textual, propagar solo reglas generales verificadas."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-1. [supuesto]",
    "Confirmar formato requerido por actividad-1: reporte, presentacion u otro.",
    "Confirmar rubrica de evaluacion para calibrar profundidad argumentativa.",
    "Confirmar nombre canonico final del .bib de la materia.",
    "Resolver de forma definitiva el placeholder $(@{...}.Slug) en README/programa.",
    "Verificar integridad completa de scjnIncapacidadResistencia2019 en .bib. [supuesto]"
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
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y utiles profesionalmente.",
      "Estandarizar calidad editorial LaTeX con base institucional UnADM.",
      "Asegurar continuidad entre actividades y memoria de materia."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable.",
      "Cierre con criterio juridico propio.",
      "Marcado explicito de [supuesto].",
      "Trazabilidad cita-texto-bibliografia."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Definir objetivo.",
      "Exponer conceptos y normas.",
      "Analizar con postura propia.",
      "Concluir con aplicacion juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofia del Derecho",
        "Hermeneutica e interpretacion juridica",
        "Argumentacion juridica",
        "Derecho y moral",
        "Justicia",
        "Analisis critico del fenomeno juridico"
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
          "justification": "La argumentacion permite evaluar validez, coherencia y consecuencias."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "La asignatura integra debate axiologico y normativo."
        },
        {
          "source": "Marco normativo-doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "La conclusion exige fundamento verificable."
        }
      ],
      "evidence": [
        "README de materia: identidad y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "filosofia-del-derecho-clean.bib: claves juridicas recurrentes.",
        "Actividad-1: patron problema-conceptos-evidencia-analisis-conclusion."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas por variaciones ortograficas.",
      "Se conservaron controles de JSON parseable y normalizacion previa.",
      "Se elevo patron argumentativo de actividad a materia sin copiar redaccion literal.",
      "Se reforzo trazabilidad curricular y bibliografica con marcas [supuesto] donde aplica.",
      "Se preservo compresion lossless por union-dedupe sin recorte de reglas utiles."
    ]
  }
}