{
  "summary": [
    "Se consolida la memoria de materia desde actividad-1 con abstraccion ascendente y deduplicacion lossless.",
    "Se preservan reglas utiles previas sin regresion y se refuerza trazabilidad entre README, programa analitico, .tex y .bib.",
    "Se mantiene control estricto de normalizacion: no propagar insumos no JSON parseable sin estructuracion previa.",
    "Se estabilizan ejes editoriales transferibles: problema, conceptos, evidencia, analisis propio y conclusion juridica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en redaccion, tono y formato.",
    "Alinear la materia a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica de actividades y entregables.",
    "Marcar como [supuesto] todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local. [supuesto]",
    "Usar malla-curricular-derecho-unadm.pdf como respaldo curricular verificado."
  ],
  "structure_rules": [
    "Abrir cada entrega con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener trazabilidad entre actividad, archivo .tex y .bib de materia."
  ],
  "activity_rules": [
    "Verificar correspondencia exacta entre consigna y tipo de producto.",
    "Sustentar afirmaciones sustantivas con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "No asumir que fuentes de semanas posteriores aplican a actividad-1. [supuesto]",
    "Agregar bibliografia especifica de actividad solo cuando sea verificable.",
    "Conservar continuidad editorial entre actividades y nucleo de la materia."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de [supuesto].",
    "Validar consistencia entre citas en .tex y entradas en .bib.",
    "Confirmar no regresion: no eliminar reglas utiles heredadas en cada ciclo."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar sin migracion completa.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Separar entregables por tipo en archivos .tex dedicados.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) antes de fijar nombres canonicos.",
    "No adoptar nombres anomalos del README como canon hasta correccion local. [supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "Registrar y mantener claves recurrentes trazables en toda la materia.",
    "Tratar filosofia-del-derecho-clean.bib como bib depurado tematico y no canon global hasta confirmacion. [supuesto]"
  ],
  "propagation_hints": [
    "Propagar hacia ancestros y laterales solo reglas verificadas y normalizadas.",
    "Elevar patrones editoriales reutilizables, no redaccion literal de actividades.",
    "Reusar puertas de calidad institucionales como filtro previo obligatorio.",
    "Mantener etiqueta de compresion union-dedupe lossless en propagacion recursiva.",
    "Conservar trazabilidad de citas recurrentes al escalar al nivel licenciatura.",
    "Registrar incidencias de ingesta (no JSON parseable) sin perder contenido util."
  ],
  "open_questions": [
    "Confirmar nombre canonico final del .bib de la materia tras resolver token Slug. [supuesto]",
    "Confirmar si actividad-1 exige reporte, presentacion u otro formato principal. [supuesto]",
    "Confirmar rubrica especifica de evaluacion para ajustar profundidad argumentativa. [supuesto]",
    "Confirmar si bibliografia de Semana 7 se reutiliza formalmente en actividad-1. [supuesto]",
    "Completar y verificar la entrada truncada scjnIncapacidadResistencia2019 en .bib local. [supuesto]"
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
      "Conceptos, normas y doctrina pertinentes.",
      "Evidencia verificable con citas.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Guiar productos academicos consistentes, verificables y utiles para practica juridica.",
      "Convertir planeacion semanal en entregables con estructura argumentativa estable."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado explicito y estable.",
      "Marcado de supuestos.",
      "Cierre con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Presentar marco conceptual y normativo.",
      "Analizar con postura propia sustentada.",
      "Concluir con aplicabilidad juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofia del Derecho",
        "Hermeneutica e interpretacion juridica",
        "Argumentacion juridica",
        "Derecho y moral",
        "Justicia",
        "Analisis critico del fenomeno juridico",
        "Ejes editoriales de la materia"
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
          "justification": "La interpretacion fundamenta la construccion argumentativa."
        },
        {
          "source": "Argumentacion juridica",
          "target": "Analisis critico del fenomeno juridico",
          "kind": "develops",
          "justification": "La argumentacion permite evaluar razones y consecuencias."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "La asignatura integra debate axiologico y validez normativa."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "La conclusion profesional exige soporte normativo verificable."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "Actividad-1: patron problema-conceptos-evidencia-analisis-conclusion.",
        "Regla persistente: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 76: fusion ascendente desde actividad-1 aplicada con union-dedupe lossless.",
      "Ciclo 76: deduplicacion semantica completada en tono, estructura y gates de calidad.",
      "Ciclo 76: se preserva trazabilidad de citas recurrentes y fuentes provisionales marcadas.",
      "Ciclo 76: se refuerza no regresion y control de ingesta para propagacion recursiva."
    ]
  }
}