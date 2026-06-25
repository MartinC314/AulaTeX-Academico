{
  "summary": [
    "Se consolida memoria de materia desde actividad-1 con abstraccion ascendente y deduplicacion lossless.",
    "Se preservan reglas institucionales UnADM, ejes editoriales y control de calidad sin regresion.",
    "Se mantiene normalizacion obligatoria para insumos no JSON parseable antes de cualquier propagacion.",
    "Se eleva trazabilidad entre consigna, producto .tex, citas y .bib de la asignatura."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y finalidad academica.",
    "Alinear la materia con Licenciatura en Derecho: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica editorial.",
    "Marcar como [supuesto] todo dato no visible en consigna o documento fuente.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local. [supuesto]",
    "Usar malla-curricular-derecho-unadm.pdf como respaldo curricular verificado."
  ],
  "structure_rules": [
    "Estructurar productos con: problema, conceptos/marco, evidencia, analisis propio y conclusion juridica.",
    "Separar entregables por tipo: reporte, presentacion y recursos bibliograficos.",
    "Alinear cada entrega al producto solicitado por la planeacion semanal.",
    "Mantener trazabilidad entre actividad, archivo .tex y .bib de materia."
  ],
  "activity_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con problema juridico o social delimitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir que bibliografia de semanas posteriores aplica a actividad-1. [supuesto]"
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en texto y entradas del .bib.",
    "Confirmar no regresion: no eliminar reglas utiles previamente consolidadas."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar sin migracion completa.",
    "Compilar sin errores criticos, sin referencias rotas y con rutas validas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo anómalos antes de tratarlos como canon."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM, UNAM-IIJ, SCJN y normatividad vigente verificable.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "Registrar en .bib de asignatura solo entradas verificadas y trazables.",
    "Mantener entradas truncadas como pendientes de verificacion sin completarlas inferencialmente. [supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas en README, programa analitico y .bib local.",
    "Elevar al ancestro patrones reutilizables, no redaccion literal de actividades.",
    "Transferir citas recurrentes como trazas de conocimiento, no como obligatoriedad universal.",
    "Aplicar union-dedupe lossless en cada ciclo para evitar duplicados y regresion.",
    "Mantener registro de riesgos de ingesta por salidas no parseables."
  ],
  "open_questions": [
    "Confirmar nombre canonico final del .bib de materia frente a placeholders Slug. [supuesto]",
    "Confirmar si actividad-1 requiere reporte, presentacion u otro formato principal. [supuesto]",
    "Confirmar rubrica especifica para calibrar profundidad argumentativa. [supuesto]",
    "Confirmar alcance de reutilizacion entre filosofia-del-derecho-clean.bib y actividades iniciales. [supuesto]",
    "Completar y verificar campos faltantes de scjnIncapacidadResistencia2019. [supuesto]"
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
      "Conceptos, normas, doctrina y datos pertinentes.",
      "Evidencia verificable y analisis propio.",
      "Conclusion juridica transferible a la practica profesional.",
      "Trazabilidad editorial entre consigna, escritura y bibliografia."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos juridicamente fundamentados.",
      "Estandarizar calidad editorial LaTeX sin perder flexibilidad por actividad.",
      "Sostener memoria persistente con compresion lossless y sin regresion."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable y funcional.",
      "Postura propia explicita.",
      "Cierre juridico aplicable.",
      "Marcado explicito de [supuesto]."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer marco conceptual y normativo.",
      "Presentar evidencia verificable.",
      "Analizar criticamente con postura propia.",
      "Concluir con implicacion juridica practica."
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
        "noauthor_constitucion_nodate",
        "de_victimas_ley_2013",
        "ruiz_rodriguez_filosofia_derecho_2009",
        "rojas_gonzalez_filosofia_derecho_2018"
      ],
      "relations": [
        {
          "source": "Hermeneutica e interpretacion juridica",
          "target": "Argumentacion juridica",
          "kind": "supports",
          "justification": "La interpretacion provee criterios para construir argumentos juridicos solidos."
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
          "justification": "La asignatura integra el debate entre validez normativa y dimension axiologica."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "La conclusion practica requiere soporte normativo verificable."
        }
      ],
      "evidence": [
        "README de materia: identidad, pauta editorial y ubicacion curricular.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "filosofia-del-derecho-clean.bib: trazas de hermeneutica y argumentacion juridica.",
        "Memoria actividad-1: patron estable problema-conceptos-evidencia-analisis-conclusion.",
        "Regla persistente: bloquear propagacion ante salida no JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: se refuerza abstraccion ascendente desde actividad-1 a materia.",
      "Ciclo 2: se deduplican reglas repetidas manteniendo contenido util total.",
      "Ciclo 2: se preservan riesgos de ingesta historicos (Codex/GPT-Pro) como trazabilidad.",
      "Ciclo 2: se consolidan puertas de calidad y trazabilidad bibliografica transferibles."
    ]
  }
}