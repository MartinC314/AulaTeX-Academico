{
  "summary": [
    "Se consolida memoria de materia desde Actividad 1 con abstraccion ascendente y deduplicacion lossless.",
    "Se preserva identidad UnADM, ubicacion curricular y pauta editorial sin regresion.",
    "Se refuerza normalizacion obligatoria para insumos no JSON parseable antes de propagacion.",
    "Se institucionaliza el patron editorial: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene trazabilidad entre actividad, archivos .tex y .bib de la materia."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en redaccion y formato.",
    "Alinear entregables con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica editorial.",
    "Marcar como [supuesto] todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local. [supuesto]",
    "Usar malla-curricular-derecho-unadm.pdf como respaldo curricular verificado.",
    "No eliminar reglas heredadas utiles de calidad y normalizacion."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener trazabilidad entre consigna, desarrollo y conclusion."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir fuentes de semanas posteriores para Actividad 1 sin verificacion. [supuesto]",
    "Validar que el producto corresponda a la consigna especifica de la actividad."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar no regresion de reglas utiles en cada ciclo."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "No renombrar claves citadas sin migracion completa.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo con caracteres anommalos antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "Registrar fuentes de actividad en el .bib de la asignatura con trazabilidad.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "No completar entradas truncadas sin verificacion local. [supuesto]",
    "Mantener y deduplicar claves recurrentes verificables de UNAM, IIJ y SCJN."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Elevar al ancestro solo patrones reutilizables, no redaccion literal de actividades.",
    "Conservar trazabilidad de citas recurrentes y reglas de calidad transferibles.",
    "Aplicar union-dedupe lossless en cada salto para evitar regresiones.",
    "Marcar ciclos con insumos no estructurados como requeridos de normalizacion manual."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 1 para fijar producto definitivo. [supuesto]",
    "Confirmar nombre canonico final del .bib de la materia frente a placeholders del README. [supuesto]",
    "Confirmar si filosofia-del-derecho-clean.bib se limita a Semana 7 o se integra parcialmente a la base general. [supuesto]",
    "Completar y verificar la entrada scjnIncapacidadResistencia2019 en el .bib local. [supuesto]",
    "Sustituir fuentes provisionales heredadas (Codex/GPT-Pro) por fuentes locales verificadas."
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
        "Carpeta de materia como punto de entrada canonico."
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
      "Evidencia verificable y trazable.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible a la practica."
    ],
    "reason_for_being": [
      "Orientar productos academicos con claridad, fundamento juridico y transferencia profesional.",
      "Convertir planeacion semanal en entregables consistentes, verificables y argumentados."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable y funcional.",
      "Citas explicitas en afirmaciones sustantivas.",
      "Marcado explicito de [supuesto].",
      "Cierre con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer marco conceptual y normativo.",
      "Contrastar evidencia y doctrina.",
      "Desarrollar postura propia sustentada.",
      "Concluir con aplicacion juridica concreta."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofia del Derecho",
        "Hermeneutica e interpretacion juridica",
        "Argumentacion juridica",
        "Derecho y moral",
        "Justicia",
        "Analisis critico del fenomeno juridico",
        "Trazabilidad editorial entre actividad, .tex y .bib"
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
          "justification": "La interpretacion fundamenta la calidad del argumento juridico."
        },
        {
          "source": "Argumentacion juridica",
          "target": "Analisis critico del fenomeno juridico",
          "kind": "develops",
          "justification": "La argumentacion permite evaluar normas, razones y efectos."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "La materia integra el debate axiologico y la validez normativa."
        },
        {
          "source": "Marco normativo y doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "La conclusion requiere sustento normativo verificable."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "Bib local: claves recurrentes de UNAM, IIJ y SCJN.",
        "Memoria de Actividad 1: patron estable problema-conceptos-evidencia-analisis-conclusion."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas conservando cobertura semantica completa.",
      "Se elevaron patrones de Actividad 1 al nivel materia sin copiar redaccion literal extensa.",
      "Se preservaron puertas de calidad heredadas y control de no regresion.",
      "Se reforzo la regla de normalizacion previa para salidas no parseables.",
      "Se mantuvo trazabilidad de citas recurrentes y pendientes bibliograficos marcados como [supuesto]."
    ]
  }
}