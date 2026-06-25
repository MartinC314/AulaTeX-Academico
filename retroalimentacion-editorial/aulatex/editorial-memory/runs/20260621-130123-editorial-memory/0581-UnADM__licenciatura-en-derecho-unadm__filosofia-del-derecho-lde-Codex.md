{
  "summary": [
    "Se consolida la memoria de materia desde Actividad 1 con abstraccion ascendente y deduplicacion lossless.",
    "Se preservan reglas utiles previas sin regresion y se mantiene trazabilidad entre actividad, .tex y .bib.",
    "Se refuerzan ejes editoriales estables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene control de ingesta: bloquear propagacion ante salidas no JSON parseable y normalizar antes de reutilizar."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y rigor academico.",
    "Alinear la materia a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica editorial y operativa.",
    "Marcar como [supuesto] todo dato no visible en la consigna o no verificado localmente.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar referencia a malla-curricular-derecho-unadm.pdf como respaldo curricular verificado."
  ],
  "structure_rules": [
    "Abrir cada producto con encuadre breve del problema juridico o social.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear el formato final al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar entregas solo descriptivas.",
    "Sustentar afirmaciones sustantivas con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir que fuentes de semanas posteriores aplican a Actividad 1.",
    "Conservar vinculo metodologico entre actividades y memoria de materia."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en .tex y entradas en .bib.",
    "Confirmar que no se eliminen reglas utiles previas en cada ciclo."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar sin migracion completa.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) antes de fijar nombres canonicos.",
    "Tratar nombres anomalos en README como pendientes hasta correccion local. [supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "Registrar fuentes de actividad en el .bib de la asignatura con metadatos minimos.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar y deduplicar entradas sin perdida de informacion.",
    "Tratar filosofia-del-derecho-clean.bib como corpus tematico de Semana 7, no canon automatico de Actividad 1. [supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales verificadas y transferibles.",
    "Elevar patrones argumentativos y puertas de calidad desde actividad hacia materia.",
    "No copiar redaccion literal de un hijo; sintetizar patrones reutilizables.",
    "Mantener trazabilidad de citas recurrentes y riesgos de ingesta heredados.",
    "Aplicar normalizacion manual en ciclos con insumos historicos no estructurados."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 1 para fijar tipo de producto definitivo. [supuesto]",
    "Confirmar nombre canonico final del archivo .bib de la materia.",
    "Confirmar si Actividad 1 reutiliza bibliografia existente o requiere .bib propio.",
    "Completar y verificar entrada truncada scjnIncapacidadResistencia2019 en .bib local. [supuesto]",
    "Resolver definitivamente placeholders de Slug en README y programa analitico."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico",
        "Claro y juridicamente preciso",
        "Argumentativo con criterio propio"
      ],
      "institutional": [
        "Alineacion explicita con UnADM",
        "Integridad academica con citas verificables",
        "Materia como entrada canonica editorial"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Semestre 1, bloque 2, obligatoria, 8 creditos",
        "Asignatura Filosofia del Derecho"
      ]
    },
    "essence": [
      "Problema juridico delimitado",
      "Conceptos y marco normativo pertinentes",
      "Evidencia verificable",
      "Analisis propio",
      "Conclusion juridica aplicable"
    ],
    "reason_for_being": [
      "Convertir la planeacion semanal en productos academicos con fundamento juridico y utilidad profesional.",
      "Estandarizar calidad editorial y trazabilidad documental en toda la materia."
    ],
    "style_markers": [
      "Encuadre inicial breve",
      "Seccionado estable",
      "Postura propia explicita",
      "Cierre transferible a practica juridica",
      "Marcado de supuestos cuando falte verificacion"
    ],
    "argumentative_patterns": [
      "Delimitar problema",
      "Presentar conceptos y normas",
      "Analizar con postura propia",
      "Sustentar con evidencia citada",
      "Concluir con aplicacion juridica"
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofia del Derecho",
        "Hermeneutica e interpretacion juridica",
        "Argumentacion juridica",
        "Derecho y moral",
        "Justicia",
        "Analisis critico del fenomeno juridico",
        "Trazabilidad editorial actividad-materia"
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
          "justification": "La interpretacion provee base metodologica para construir argumentos."
        },
        {
          "source": "Argumentacion juridica",
          "target": "Analisis critico del fenomeno juridico",
          "kind": "develops",
          "justification": "La argumentacion permite evaluar validez, razones y consecuencias."
        },
        {
          "source": "Marco normativo y doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "La conclusion exige soporte normativo verificable."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "La asignatura integra debate axiologico y juridico."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "Bibliografia local: claves juridicas recurrentes y verificables.",
        "Actividad 1: patron estable problema-conceptos-evidencia-analisis-conclusion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 14: se eleva memoria de actividad a materia sin perdida semantica.",
      "Ciclo 14: se refuerza control de ingesta JSON y normalizacion previa.",
      "Ciclo 14: se consolidan citas recurrentes y reglas de trazabilidad .tex/.bib.",
      "Ciclo 14: se mantienen fuentes provisionales con marcado explicito de supuesto."
    ]
  }
}