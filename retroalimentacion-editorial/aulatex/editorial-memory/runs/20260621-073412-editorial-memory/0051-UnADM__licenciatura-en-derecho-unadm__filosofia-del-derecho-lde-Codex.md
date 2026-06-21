{
  "summary": [
    "Se consolida memoria de materia desde actividad con abstraccion ascendente y deduplicacion lossless.",
    "Se preserva identidad UnADM, trazabilidad curricular y regla de no regresion editorial.",
    "Se mantienen ejes nucleares: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se refuerza normalizacion obligatoria para insumos no JSON parseable antes de propagacion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y criterios academicos.",
    "Alinear entregables a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuentes locales.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local. [supuesto]",
    "Conservar referencia curricular verificable en malla-curricular-derecho-unadm.pdf."
  ],
  "structure_rules": [
    "Abrir cada producto con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar secciones en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear forma de entrega al producto solicitado por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Mantener trazabilidad entre actividad, archivo .tex y .bib de materia."
  ],
  "activity_rules": [
    "Verificar correspondencia exacta entre consigna y tipo de entregable.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "No asumir fuentes de semanas posteriores para actividad inicial sin verificacion. [supuesto]",
    "Integrar conceptos, normas, doctrina o datos pertinentes al problema delimitado."
  ],
  "quality_gates": [
    "Bloquear propagacion si salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizar.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en texto y entradas BibTeX.",
    "Evitar eliminar reglas utiles previas en cada ciclo."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar sin migracion completa.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Corregir nombres/rutas con caracteres anomalos antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Conservar separacion de entregables .tex por tipo: reporte y presentacion."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "Registrar fuentes de actividad en .bib de asignatura con metadatos minimos.",
    "No inventar referencias; usar solo obras realmente consultables.",
    "Conservar deduplicacion sin perdida y mantener claves ya citadas.",
    "No completar entradas truncadas sin verificacion local. [supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas y normalizadas.",
    "Elevar al ancestro patrones reutilizables, no redaccion literal de actividad.",
    "Conservar trazabilidad de citas recurrentes y puertas de calidad transferibles.",
    "Aplicar union-dedupe lossless en cada salto para evitar regresiones.",
    "Etiquetar ciclos con riesgo de ingesta cuando hubo salida no parseable."
  ],
  "open_questions": [
    "Confirmar nombre canonico final del .bib de materia tras resolver token Slug. [supuesto]",
    "Confirmar consigna textual exacta de actividad 1 y su rubrica oficial. [supuesto]",
    "Verificar si filosofia-del-derecho-clean.bib se limita a Semana 7 o se reutiliza parcialmente. [supuesto]",
    "Completar y validar entrada scjnIncapacidadResistencia2019 en .bib local. [supuesto]"
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
      "Conceptos y marco normativo.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables, argumentados y utiles para practica juridica.",
      "Preservar continuidad editorial entre actividades y materia sin perder calidad ni verificabilidad."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable y funcional.",
      "Citas explicitas y verificables.",
      "Marcado visible de supuestos.",
      "Cierre con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer marco conceptual y normativo.",
      "Contrastar fuentes y justificar postura.",
      "Concluir con implicacion profesional concreta."
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
          "justification": "La interpretacion fundamenta la construccion de razones juridicas."
        },
        {
          "source": "Argumentacion juridica",
          "target": "Analisis critico del fenomeno juridico",
          "kind": "develops",
          "justification": "Permite evaluar validez normativa y consecuencias."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "La conclusion valida exige sustento normativo verificable."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "Integra discusion axiologica y juridica en el analisis."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "Bibliografia local .bib: claves recurrentes de doctrina, SCJN y normatividad.",
        "Regla persistente: normalizar salidas no parseables antes de propagar."
      ]
    },
    "reinforcement_log": [
      "Ciclo 51: se elevan patrones de actividad a materia sin copiar redaccion literal.",
      "Ciclo 51: se deduplican reglas repetidas y se conserva contenido util previo.",
      "Ciclo 51: se refuerza compresion lossless por union-dedupe y no regresion.",
      "Ciclo 51: se mantiene trazabilidad de citas y control de supuestos."
    ]
  }
}