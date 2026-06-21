{
  "summary": [
    "Consolidar memoria de materia desde actividad con abstraccion ascendente y trazabilidad.",
    "Preservar reglas validas previas sin regresion y con deduplicacion lossless.",
    "Mantener normalizacion obligatoria para insumos no JSON parseable.",
    "Fijar ADN editorial UnADM: problema, conceptos, evidencia, analisis propio y conclusion juridica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en redaccion y formato.",
    "Alinear la materia con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como [supuesto] todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local. [supuesto]",
    "Usar malla-curricular-derecho-unadm.pdf como respaldo curricular verificado."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato solicitado por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener trazabilidad entre actividad, .tex y .bib."
  ],
  "activity_rules": [
    "Iniciar cada actividad con problema delimitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir fuentes de semanas posteriores para actividad 1. [supuesto]"
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar.",
    "Normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Validar correspondencia del producto con la consigna de la actividad.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables y no renombrarlas sin migracion completa.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Separar entregables por tipo en .tex dedicados.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "No adoptar nombres de archivo anomalos como canon hasta correccion local. [supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Registrar fuentes de actividad en el .bib de la materia.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Mantener y verificar claves recurrentes de UNAM, IIJ y SCJN."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas y estructuradas.",
    "Elevar patrones reutilizables del nivel actividad al nivel materia.",
    "Conservar trazabilidad conceptual y citas recurrentes al propagar.",
    "Aplicar union-dedupe lossless en cada ciclo sin recorte semantico.",
    "Registrar incidencias de ingesta no parseable como riesgo, sin perder reglas utiles."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad 1. [supuesto]",
    "Confirmar nombre canonico final del archivo .bib de la materia.",
    "Verificar si filosofia-del-derecho-clean.bib es solo de Semana 7 o reutilizable en actividad 1. [supuesto]",
    "Completar y verificar campos faltantes de scjnIncapacidadResistencia2019. [supuesto]",
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
      "Conceptos, normas, doctrina o datos.",
      "Evidencia verificable.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables academicos solidos.",
      "Asegurar fundamento juridico, claridad y trazabilidad editorial.",
      "Conectar teoria de filosofia del derecho con practica profesional."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable.",
      "Citas explicitas y verificables.",
      "Marcado de supuestos cuando falte evidencia.",
      "Cierre con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Definir marco conceptual y normativo.",
      "Analizar con postura propia.",
      "Contrastar con evidencia.",
      "Concluir con aplicacion practica."
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
          "justification": "La argumentacion permite evaluar validez, alcance y consecuencias."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "La asignatura articula debate axiologico y normativo."
        },
        {
          "source": "Marco normativo y doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "La conclusion valida requiere soporte verificable."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "Bib local depurada: claves recurrentes y trazables.",
        "Memoria de actividad 1: patron problema-conceptos-evidencia-analisis-conclusion."
      ]
    },
    "reinforcement_log": [
      "Se elevo patron editorial de actividad a materia sin copiar redaccion literal.",
      "Se deduplicaron reglas equivalentes manteniendo cobertura completa.",
      "Se reforzo puerta de calidad para JSON parseable y normalizacion previa.",
      "Se conservaron citas y conceptos recurrentes con trazabilidad.",
      "Se mantuvieron supuestos explicitos donde falta verificacion local."
    ]
  }
}