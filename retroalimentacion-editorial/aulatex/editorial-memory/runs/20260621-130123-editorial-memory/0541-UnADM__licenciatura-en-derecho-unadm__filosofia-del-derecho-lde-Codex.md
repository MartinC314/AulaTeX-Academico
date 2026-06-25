{
  "summary": [
    "Se consolida memoria de materia desde actividad-1 con abstraccion ascendente y deduplicacion lossless.",
    "Se preservan reglas validas previas sin regresion y se refuerza trazabilidad curricular UnADM.",
    "Se mantiene normalizacion obligatoria de insumos no estructurados antes de propagar.",
    "Se fijan ejes transferibles: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se registra riesgo tecnico por placeholders de nombre .bib y salidas no JSON parseable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y criterio juridico.",
    "Alinear la materia a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica editorial y tecnica.",
    "Marcar como [supuesto] todo dato no visible en consigna o documento local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local. [supuesto]",
    "Conservar trazabilidad a malla-curricular-derecho-unadm.pdf como respaldo curricular."
  ],
  "structure_rules": [
    "Estructurar productos con: problema, conceptos o marco, evidencia, analisis propio y cierre.",
    "Separar entregables por tipo: reporte, presentacion y soporte bibliografico.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear el formato final al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Iniciar cada actividad con delimitacion de problema juridico o social.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir bibliografia de semanas posteriores para actividad-1 sin evidencia. [supuesto]"
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en .tex y entradas en .bib."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correctos en español para .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar sin migracion completa.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "No adoptar nombres anomalos como canon hasta correccion local. [supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año, fuente editorial o URL.",
    "Registrar en .bib de materia solo entradas verificadas y trazables."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales verificadas en README, programa y .bib local.",
    "Elevar al ancestro patrones argumentativos, identidad y puertas de calidad reutilizables.",
    "Evitar propagar texto literal de actividades; propagar patrones sinteticos.",
    "Mantener etiqueta union-dedupe lossless en cada ciclo de consolidacion.",
    "Conservar registro de incidencias tecnicas como riesgo de ingesta sin perder reglas utiles."
  ],
  "open_questions": [
    "Confirmar nombre canonico final del archivo .bib de la materia. [supuesto]",
    "Confirmar si actividad-1 requiere reporte, presentacion u otro formato principal. [supuesto]",
    "Confirmar rubrica especifica de evaluacion para profundidad argumentativa. [supuesto]",
    "Verificar integridad completa de scjnIncapacidadResistencia2019 en .bib local. [supuesto]",
    "Sustituir fuentes provisionales heredadas por fuentes verificadas locales. [supuesto]"
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
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos juridicos con fundamento y trazabilidad.",
      "Sostener continuidad editorial entre actividades y materia sin perdida de calidad."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable.",
      "Postura personal argumentada.",
      "Marcado explicito de [supuesto].",
      "Cierre juridico aplicable."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer marco conceptual y normativo.",
      "Presentar evidencia citada.",
      "Analizar con postura propia.",
      "Concluir con implicacion practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofia del Derecho",
        "Hermeneutica juridica",
        "Argumentacion juridica",
        "Derecho y moral",
        "Justicia",
        "Transferencia profesional"
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
          "source": "Hermeneutica juridica",
          "target": "Argumentacion juridica",
          "kind": "supports",
          "justification": "La interpretacion sustenta la construccion de razones juridicas."
        },
        {
          "source": "Argumentacion juridica",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "Estructura el paso de premisas a cierre aplicable."
        },
        {
          "source": "Marco normativo",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "La postura requiere base normativa verificable."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "Integra debate de validez, justicia y deber ser."
        }
      ],
      "evidence": [
        "README de materia.",
        "Programa analitico de la asignatura.",
        "filosofia-del-derecho-clean.bib.",
        "reporte-filosofia-del-derecho-Actividad-1.tex."
      ]
    },
    "reinforcement_log": [
      "Ciclo 4: se eleva patron nuclear de actividad al nivel materia sin copia literal.",
      "Ciclo 4: se conserva normalizacion JSON como puerta obligatoria de propagacion.",
      "Ciclo 4: se refuerza trazabilidad entre .tex, .bib y consigna.",
      "Ciclo 4: se mantienen fuentes provisionales marcadas como [supuesto] hasta verificacion."
    ]
  }
}