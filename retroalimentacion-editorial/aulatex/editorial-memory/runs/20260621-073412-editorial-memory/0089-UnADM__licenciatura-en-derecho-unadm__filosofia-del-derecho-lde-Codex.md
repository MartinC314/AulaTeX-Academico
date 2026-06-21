{
  "summary": [
    "Se consolida memoria de materia desde actividad-1 con abstraccion ascendente.",
    "Se preserva compresion lossless por union y deduplicacion sin regresion.",
    "Se mantiene normalizacion obligatoria para insumos no JSON parseable.",
    "Se refuerzan ejes transferibles: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se conserva trazabilidad entre README, programa analitico, .tex y .bib."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en redaccion y formato.",
    "Alinear a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica editorial.",
    "Marcar como [supuesto] todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local. [supuesto]",
    "Conservar regla de no eliminar controles de calidad heredados."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener trazabilidad entre actividad, archivo .tex y .bib de materia."
  ],
  "activity_rules": [
    "Evitar entregas solo descriptivas o de resumen.",
    "Incluir postura argumentada del estudiante.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir fuentes de semanas posteriores para actividad-1. [supuesto]",
    "Verificar correspondencia del producto con la consigna especifica."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar que no se eliminen reglas utiles previas en cada ciclo."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "No renombrar claves citadas sin migracion completa.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo anomalos antes de declararlos canonicos. [supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Registrar fuentes especificas de actividad en el .bib de la asignatura.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "No completar entradas truncadas sin verificacion local. [supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Elevar patrones reutilizables, no redaccion literal de actividades.",
    "Reutilizar puertas de calidad institucional en nodos laterales y superiores.",
    "Evitar propagar nombres de archivo no verificados. [supuesto]",
    "Mantener etiqueta de compresion union-dedupe lossless en toda propagacion."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-1 para fijar plantilla final. [supuesto]",
    "Confirmar nombre canonico definitivo del .bib de la materia. [supuesto]",
    "Confirmar si filosofia-del-derecho-clean.bib se limita a Semana 7 o se integra parcialmente a materia. [supuesto]",
    "Completar y verificar la entrada scjnIncapacidadResistencia2019 en el .bib local. [supuesto]",
    "Sustituir fuentes provisionales heredadas por fuentes verificadas locales."
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
        "Materia como punto de entrada canonico."
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
      "Evidencia verificable.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos con fundamento juridico y utilidad profesional.",
      "Estandarizar calidad editorial sin perder especificidad de cada actividad."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable y trazable.",
      "Marcado explicito de supuestos.",
      "Cierre con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Construir marco conceptual y normativo.",
      "Contrastar fuentes y justificar postura.",
      "Concluir con aplicabilidad practica juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofia del Derecho",
        "Hermeneutica e interpretacion juridica",
        "Argumentacion juridica",
        "Derecho y moral",
        "Justicia",
        "Analisis critico del fenomeno juridico",
        "Trazabilidad editorial materia-actividad"
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
          "justification": "Permite evaluar validez, coherencia y consecuencias normativas."
        },
        {
          "source": "Marco normativo y doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "La conclusion exige soporte verificable."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "Integra el debate entre validez formal y contenido axiologico."
        }
      ],
      "evidence": [
        "README de materia: identidad y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "Archivos .bib locales: claves juridicas recurrentes.",
        "Patron de actividad-1: problema-conceptos-evidencia-analisis-conclusion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 89: se elevo ADN editorial de actividad a materia sin recorte semantico.",
      "Ciclo 89: se deduplicaron reglas repetidas y se preservaron controles utiles.",
      "Ciclo 89: se reforzo trazabilidad conceptual y bibliografica para propagacion recursiva."
    ]
  }
}