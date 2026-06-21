{
  "summary": [
    "Se consolida en materia el patron editorial transferido desde actividad-1.",
    "Se preserva compresion lossless por union-dedupe sin eliminar reglas utiles.",
    "Se refuerza normalizacion obligatoria antes de cualquier propagacion recursiva.",
    "Se fija trazabilidad entre consigna, producto .tex y respaldo .bib.",
    "Se mantiene identidad UnADM con enfoque juridico argumentativo y verificable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y criterios academicos.",
    "Alinear la materia a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica de la asignatura.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local. [supuesto]",
    "Conservar referencia de riesgo de ingesta por salidas no JSON parseable de Codex y GPT-Pro."
  ],
  "structure_rules": [
    "Abrir cada producto con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en bloques: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto solicitado por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Mantener trazabilidad entre actividad, archivo .tex y archivo .bib."
  ],
  "activity_rules": [
    "Exigir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir fuentes de semanas posteriores como validas para actividad-1. [supuesto]",
    "Validar correspondencia exacta entre entregable y consigna de cada actividad.",
    "Propagar al nivel materia solo patrones reutilizables, no redaccion literal del hijo."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de [supuesto].",
    "Validar consistencia entre citas en texto y entradas en .bib.",
    "Confirmar no regresion: no eliminar reglas utiles heredadas."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar sin migracion completa.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Tratar nombres de archivo anomalos como pendientes de correccion, no como canon. [supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "Registrar fuentes de actividad en el .bib de asignatura con metadatos minimos completos.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar y deduplicar entradas existentes sin perdida de informacion.",
    "Tratar scjnIncapacidadResistencia2019 como entrada potencialmente incompleta hasta verificacion local. [supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Elevar al ancestro reglas generales de identidad, calidad y trazabilidad.",
    "No propagar placeholders de nombres de archivo como definitivos.",
    "Reusar puertas de calidad institucional en nodos laterales de Derecho.",
    "Cuando falte consigna textual, propagar solo reglas generales verificadas.",
    "Mantener bitacora de incidencias de ingesta sin perder contenido util."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-1 para fijar plantilla final.",
    "Confirmar nombre canonico final del .bib de la asignatura.",
    "Definir si filosofia-del-derecho-clean.bib es auxiliar o canon permanente. [supuesto]",
    "Completar y verificar campos faltantes de scjnIncapacidadResistencia2019.",
    "Confirmar rubrica de evaluacion para ajustar profundidad argumentativa.",
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
      "Conceptos, normas y doctrina pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos juridicos trazables y utiles.",
      "Sostener un marco editorial estable para reportes y presentaciones en LaTeX."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable y funcional.",
      "Postura propia explicita.",
      "Cierre juridico aplicado.",
      "Marcado explicito de supuestos."
    ],
    "argumentative_patterns": [
      "Problema delimitado -> marco conceptual/normativo -> analisis critico -> conclusion aplicada.",
      "Afirmacion sustantiva -> cita verificable -> inferencia propia.",
      "Consigna -> producto solicitado -> verificacion de coherencia final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofia del Derecho",
        "Hermeneutica e interpretacion juridica",
        "Argumentacion juridica",
        "Derecho y moral",
        "Justicia",
        "Trazabilidad editorial",
        "Normalizacion de ingesta"
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
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La calidad argumentativa determina la solidez del cierre aplicado."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis exige fundamento verificable para evitar opinion vacia."
        },
        {
          "source": "Normalizacion de ingesta",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Solo datos estructurados permiten transferencia confiable."
        }
      ],
      "evidence": [
        "README de materia: identidad, estructura y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "Actividad-1: patron problema-conceptos-evidencia-analisis-conclusion.",
        "Regla persistente: bloquear salidas no JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 27: se elevo patron de actividad-1 a nivel materia sin perdida.",
      "Ciclo 27: se deduplicaron reglas repetidas conservando trazabilidad conceptual.",
      "Ciclo 27: se reforzo no regresion y control de calidad estructural.",
      "Ciclo 27: se mantuvieron citas recurrentes y riesgos de ingesta como memoria activa."
    ]
  }
}