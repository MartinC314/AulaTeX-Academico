{
  "summary": [
    "Se consolida memoria de materia desde actividad-1 con abstraccion ascendente y deduplicacion lossless.",
    "Se preserva identidad UnADM, ubicacion curricular y pauta editorial como nucleo estable.",
    "Se mantienen ejes editoriales transferibles: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se refuerza normalizacion obligatoria para insumos no JSON parseable antes de propagar.",
    "Se conserva trazabilidad entre actividad, archivos .tex y bibliografia de materia."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en redaccion y formato.",
    "Alinear entregables con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Usar malla-curricular-derecho-unadm.pdf como fuente curricular verificada.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local. [supuesto]",
    "No eliminar reglas heredadas utiles de calidad y normalizacion."
  ],
  "structure_rules": [
    "Abrir cada entrega con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato exigido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener trazabilidad entre actividad, .tex y .bib."
  ],
  "activity_rules": [
    "Delimitar problema juridico o social al inicio de cada actividad.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Integrar postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir fuentes de semanas posteriores como aplicables a actividad-1 sin verificacion. [supuesto]",
    "Confirmar que el producto entregado coincide con la consigna especifica."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar respaldo o marca de supuesto en toda afirmacion sustantiva.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Evitar regresion: no remover reglas utiles previas en cada ciclo."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "No renombrar claves citadas sin migracion completa.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo con caracteres anomalos antes de tratarlos como canon. [supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "Registrar fuentes de actividad en el .bib de la asignatura.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente/editorial o URL.",
    "No completar entradas truncadas sin verificacion local. [supuesto]",
    "Mantener trazables claves recurrentes de SCJN, UNAM e IIJ ya verificadas."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Elevar al ancestro solo patrones reutilizables, no redaccion literal de actividades.",
    "Reusar puertas de calidad institucional en nodos laterales sin perder especificidad local.",
    "Aplicar union-dedupe lossless en cada salto para evitar duplicados y regresion.",
    "Mantener registro de incidencias de ingesta no parseable como riesgo editorial."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-1 y tipo de producto final. [supuesto]",
    "Confirmar nombre canonico definitivo del .bib de la materia tras resolver placeholders. [supuesto]",
    "Verificar si filosofia-del-derecho-clean.bib se usa solo para semana 7 o tambien para actividad-1. [supuesto]",
    "Completar y validar la entrada scjnIncapacidadResistencia2019 en bibliografia local. [supuesto]"
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
      "Conceptos y marco normativo o doctrinal.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir la planeacion semanal en productos academicos con fundamento juridico y utilidad profesional.",
      "Sostener una memoria editorial persistente, trazable y sin regresion."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable.",
      "Postura propia explicita.",
      "Marcado de supuestos.",
      "Cierre juridico aplicado."
    ],
    "argumentative_patterns": [
      "Problema delimitado -> marco conceptual/normativo -> evidencia -> analisis critico -> conclusion.",
      "Afirmacion sustantiva -> cita verificable -> inferencia juridica.",
      "Consigna -> producto solicitado -> validacion final de coherencia."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofia del Derecho",
        "Hermeneutica e interpretacion juridica",
        "Argumentacion juridica",
        "Derecho y moral",
        "Justicia",
        "Analisis critico del fenomeno juridico",
        "Trazabilidad editorial"
      ],
      "citations": [
        "hernandezManriquezHermeneutica2019",
        "scjnMemoriaArgumentacion2008",
        "scjnViolenciaFisica2022",
        "scjnIncapacidadResistencia2019",
        "ruiz_rodriguez_filosofia_derecho_2009",
        "rojas_gonzalez_filosofia_derecho_2018"
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
          "justification": "La argumentacion permite evaluar validez, justificacion y consecuencias."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "La conclusion profesional exige soporte normativo verificable."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "La materia integra debate axiologico y normativo."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "Bibliografia local: claves juridicas recurrentes y verificables.",
        "Memoria de actividad-1: patron argumentativo estable y transferible."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin perdida semantica.",
      "Se preservaron reglas utiles heredadas de calidad, estructura y trazabilidad.",
      "Se elevo al nivel materia el patron canonico de actividad sin copiar redaccion literal.",
      "Se mantuvo registro de riesgos por salidas no JSON parseable.",
      "Se reforzo la politica de supuestos para datos no visibles."
    ]
  }
}