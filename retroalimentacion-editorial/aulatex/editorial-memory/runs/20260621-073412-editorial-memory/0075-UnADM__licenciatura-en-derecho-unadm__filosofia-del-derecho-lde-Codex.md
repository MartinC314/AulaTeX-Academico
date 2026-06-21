{
  "summary": [
    "Se consolida en materia la memoria valida de actividad-1 con abstraccion ascendente.",
    "Se preservan reglas sin regresion y se aplica compresion lossless por union-dedupe.",
    "Se mantiene normalizacion obligatoria de insumos no JSON parseable antes de propagar.",
    "Se refuerzan ejes editoriales reutilizables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se conserva trazabilidad entre README, programa analitico, .tex y .bib de la materia."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, redaccion y formato.",
    "Alinear entregables a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica editorial.",
    "Marcar como [supuesto] todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local. [supuesto]",
    "Usar malla-curricular-derecho-unadm.pdf como respaldo curricular verificado.",
    "Conservar referencias provisionales historicas (Codex/GPT-Pro) solo como trazabilidad de ingesta. [supuesto]"
  ],
  "structure_rules": [
    "Abrir cada producto con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear cada entrega al tipo de producto solicitado por la planeacion semanal.",
    "Mantener trazabilidad entre actividad, archivo .tex y bibliografia .bib."
  ],
  "activity_rules": [
    "Iniciar cada actividad con problema delimitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir que fuentes de semanas posteriores aplican a actividad-1 sin verificacion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna de la actividad."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables y no renombrarlas sin migracion completa.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Corregir nombres o rutas con caracteres anomalos antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Tratar filosofia-del-derecho.bib como canonico probable hasta confirmacion final. [supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "Registrar fuentes de actividad en el .bib de la asignatura con metadatos minimos.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar autor, titulo, ano y fuente editorial o URL.",
    "Conservar claves recurrentes verificables ya presentes en la materia.",
    "No completar entradas truncadas sin verificacion local (ej. scjnIncapacidadResistencia2019). [supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas por README, programa analitico y .bib local.",
    "Elevar al ancestro patrones editoriales y de calidad, no redaccion literal de actividades.",
    "Reutilizar puertas de calidad institucionales en nodos laterales de Derecho.",
    "Mantener etiqueta de compresion union-dedupe lossless en cada salto.",
    "Registrar incidencias de ingesta no parseable como riesgo sin perder contenido util.",
    "Evitar propagar nombres de archivo anomalos hasta su correccion local."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-1 para validar tipo de producto.",
    "Confirmar nombre canonico final del .bib de materia.",
    "Confirmar si actividad-1 reutiliza bibliografia de Semana 7 o requiere bloque propio. [supuesto]",
    "Confirmar integridad completa de la entrada scjnIncapacidadResistencia2019.",
    "Sustituir fuentes provisionales heredadas por fuentes locales verificadas."
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
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos claros y trazables.",
      "Asegurar fundamento juridico y rigor argumentativo en cada actividad.",
      "Garantizar transferencia profesional del aprendizaje."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable.",
      "Citas verificables.",
      "Marcado explicito de [supuesto].",
      "Cierre juridico aplicable."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Construir marco conceptual y normativo.",
      "Contrastar doctrina, norma y caso cuando aplique.",
      "Sostener tesis propia con evidencia.",
      "Concluir con implicacion practica juridica."
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
          "justification": "La interpretacion fundamenta la construccion de razones juridicas."
        },
        {
          "source": "Argumentacion juridica",
          "target": "Analisis critico del fenomeno juridico",
          "kind": "develops",
          "justification": "Permite evaluar validez, coherencia y consecuencias."
        },
        {
          "source": "Marco normativo y doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "La conclusion exige soporte normativo verificable."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "Integra debate axiologico y validez juridica."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "filosofia-del-derecho-clean.bib: claves juridicas recurrentes.",
        "Actividad-1: patron editorial estable reutilizable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 75: se elevaron patrones y relaciones del hijo al ancestro sin copia literal.",
      "Ciclo 75: se deduplicaron reglas y se conservaron controles utiles previos.",
      "Ciclo 75: se reforzo normalizacion de ingesta no parseable como puerta obligatoria.",
      "Ciclo 75: se mantuvo trazabilidad de citas recurrentes y supuestos pendientes."
    ]
  }
}