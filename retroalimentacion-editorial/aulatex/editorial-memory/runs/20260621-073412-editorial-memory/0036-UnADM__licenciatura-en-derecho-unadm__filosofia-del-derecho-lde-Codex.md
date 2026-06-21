{
  "summary": [
    "Se consolida memoria de materia desde actividad con abstraccion ascendente y deduplicacion lossless.",
    "Se preservan reglas utiles previas sin regresion y se refuerza identidad editorial UnADM.",
    "Se mantiene normalizacion obligatoria de insumos no estructurados antes de cualquier propagacion.",
    "Se fijan ejes transferibles de toda actividad: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se conserva trazabilidad entre consigna, producto .tex y respaldo bibliografico .bib."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y criterios de integridad academica.",
    "Alinear la materia a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica de actividades y entregables.",
    "Marcar como [supuesto] todo dato no visible en consigna o documento fuente.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local. [supuesto]",
    "Conservar trazabilidad de fuente curricular en malla-curricular-derecho-unadm.pdf."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear cada entrega al tipo de producto pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener correspondencia entre actividad, archivo .tex y archivo .bib."
  ],
  "activity_rules": [
    "Evitar productos solo descriptivos; exigir postura argumentada del estudiante.",
    "Sustentar afirmaciones sustantivas con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir que fuentes de semanas posteriores aplican automaticamente a actividad inicial. [supuesto]",
    "Agregar fuentes especificas de actividad solo si son consultables y trazables.",
    "Comprobar que el producto final corresponde exactamente a la consigna de la actividad."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizacion.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de [supuesto].",
    "Validar consistencia entre citas en texto y entradas del .bib.",
    "Aplicar control de no regresion: no eliminar reglas utiles heredadas."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar sin migracion total.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Separar entregables por tipo en .tex dedicados: reporte y presentacion.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo con caracteres anomalos antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Distinguir bibliografia base de materia y bibliografia especifica de actividad.",
    "No inventar referencias; usar solo obras realmente consultables.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Registrar en .bib de materia las fuentes confirmadas de cada actividad.",
    "No completar entradas truncadas sin verificacion documental local. [supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Elevar patrones editoriales reutilizables, no redaccion literal de actividades.",
    "Reusar puertas de calidad institucionales en nodos laterales y superiores.",
    "Mantener compresion union-dedupe lossless en cada ciclo.",
    "Evitar propagar placeholders o nombres de archivo no resueltos. [supuesto]",
    "Registrar riesgos de ingesta no parseable sin perder reglas utiles."
  ],
  "open_questions": [
    "Confirmar consigna textual completa de Actividad 1 para fijar producto exacto.",
    "Confirmar nombre canonico final del .bib de la materia frente a placeholders.",
    "Confirmar si el .bib depurado de Semana 7 aplica parcial o nada a Actividad 1. [supuesto]",
    "Verificar integridad de la entrada scjnIncapacidadResistencia2019 truncada. [supuesto]",
    "Definir sustitucion verificada de fuentes provisionales heredadas.",
    "Precisar plantilla minima diferenciada para reporte vs presentacion."
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
      "Problema juridico o social delimitado.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable y trazable.",
      "Analisis propio con postura academica.",
      "Conclusion juridica aplicable."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos solidos y verificables.",
      "Garantizar coherencia entre consigna, argumentacion y evidencia.",
      "Transferir aprendizaje filosofico-juridico a practica profesional."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable y funcional.",
      "Marcado explicito de [supuesto].",
      "Cierre con criterio juridico propio.",
      "Trazabilidad documental constante."
    ],
    "argumentative_patterns": [
      "Delimitar problema antes de definir conceptos.",
      "Vincular doctrina y norma con el caso o pregunta.",
      "Justificar cada afirmacion relevante con cita verificable.",
      "Contrastar postura propia con fuentes academicas.",
      "Concluir con implicacion juridica concreta."
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
          "justification": "La interpretacion sustenta la construccion de razones juridicas."
        },
        {
          "source": "Argumentacion juridica",
          "target": "Analisis critico del fenomeno juridico",
          "kind": "develops",
          "justification": "Permite evaluar validez, coherencia y consecuencias."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "Integra debate axiologico y validez normativa."
        },
        {
          "source": "Marco normativo y doctrinal",
          "target": "Conclusion juridica aplicable",
          "kind": "depends_on",
          "justification": "La conclusion exige soporte normativo verificable."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "Regla persistente: bloquear salidas no JSON parseable.",
        "Actividad 1: patron argumentativo estable transferido al nivel materia."
      ]
    },
    "reinforcement_log": [
      "Ciclo 36: se eleva patron de actividad a materia sin copia literal.",
      "Ciclo 36: se refuerza no regresion y union-dedupe lossless.",
      "Ciclo 36: se mantiene control de calidad para JSON y estructura minima.",
      "Ciclo 36: se consolidan citas recurrentes y trazabilidad bibliografica.",
      "Ciclo 36: se preservan supuestos abiertos para verificacion posterior."
    ]
  }
}