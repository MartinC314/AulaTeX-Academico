{
  "summary": [
    "Consolidar memoria de materia con abstraccion ascendente desde actividad-1, sin regresion.",
    "Aplicar compresion lossless por union-dedupe y conservar trazabilidad conceptual y editorial.",
    "Mantener normalizacion estructurada obligatoria antes de cualquier propagacion recursiva.",
    "Preservar identidad UnADM, integridad academica, citas verificables y conclusion juridica con criterio propio."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, redaccion y formato.",
    "Alinear la materia a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica de materia y actividades.",
    "Marcar como [supuesto] todo dato no visible en la consigna o no verificado localmente.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local. [supuesto]",
    "Conservar referencia de riesgo de ingesta por salidas no JSON parseable de Codex y GPT-Pro."
  ],
  "structure_rules": [
    "Estructurar entregables con: problema, conceptos/fuentes, analisis propio y cierre.",
    "Separar secciones estables: conceptos clave, marco normativo o doctrinal, analisis propio y conclusion.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear cada producto al tipo solicitado por planeacion semanal.",
    "Mantener trazabilidad entre actividad, .tex y .bib de materia.",
    "No canonizar nombres con tokens sin expandir; tratarlos como pendiente local. [supuesto]"
  ],
  "activity_rules": [
    "Iniciar cada actividad con problema juridico o social delimitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "No asumir que fuentes de semanas posteriores aplican automaticamente a actividad-1."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en .tex y entradas en .bib.",
    "Confirmar que no se eliminen reglas utiles previas en cada ciclo."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol para .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar sin migracion completa.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Verificar rutas y nombres de archivo antes de referenciarlos o propagar canon."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "Registrar fuentes de actividad en el .bib de la asignatura con metadatos minimos.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar y deduplicar entradas sin perdida de informacion.",
    "Tratar entradas truncadas como pendientes de integridad hasta verificacion local. [supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas por README, programa analitico y .bib local.",
    "Elevar patrones reutilizables: problema-conceptos-evidencia-analisis-conclusion.",
    "Propagar trazabilidad de citas recurrentes sin copiar redaccion literal de actividades.",
    "Mantener etiqueta de compresion union-dedupe lossless en saltos ascendentes y laterales.",
    "Registrar incidencias de parseo como riesgo tecnico, sin perder reglas editoriales validas.",
    "Aplicar normalizacion manual en ciclos con herencia no estructurada (ciclos 1 y 2)."
  ],
  "open_questions": [
    "Confirmar consigna textual completa y producto exacto de actividad-1. [supuesto]",
    "Confirmar nombre canonico final del archivo .bib de la asignatura.",
    "Determinar si filosofia-del-derecho-clean.bib es auxiliar o canon permanente. [supuesto]",
    "Completar y verificar la entrada truncada scjnIncapacidadResistencia2019. [supuesto]",
    "Corregir definitivamente nombres con caracteres anommalos detectados en README. [supuesto]",
    "Confirmar rubrica de evaluacion para ajustar profundidad argumentativa."
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
      "Problema juridico o social como disparador.",
      "Conceptos, normas, doctrina y datos pertinentes.",
      "Evidencia verificable con cita.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables y utiles para la practica juridica.",
      "Sostener coherencia editorial de toda la materia con estandares UnADM.",
      "Asegurar memoria persistente sin perdida por deduplicacion."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable y trazable.",
      "Marcado explicito de [supuesto].",
      "Cierre con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Definir objetivo.",
      "Construir marco conceptual y normativo.",
      "Sustentar con evidencia citada.",
      "Desarrollar analisis critico propio.",
      "Concluir con aplicabilidad profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofia del Derecho",
        "Hermeneutica e interpretacion juridica",
        "Argumentacion juridica",
        "Derecho y moral",
        "Justicia",
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
          "justification": "La interpretacion provee criterios para construir argumentos juridicos."
        },
        {
          "source": "Argumentacion juridica",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El analisis critico depende de razones explicitadas y evaluables."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "La conclusion valida requiere sustento normativo y doctrinal verificable."
        },
        {
          "source": "Identidad UnADM",
          "target": "Calidad editorial de materia",
          "kind": "supports",
          "justification": "La alineacion institucional estandariza tono, rigor y trazabilidad."
        }
      ],
      "evidence": [
        "README de materia: ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "Actividad-1: patron estable de construccion argumentativa.",
        "Reglas de calidad: bloqueo por no-JSON y normalizacion obligatoria."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas manteniendo contenido util sin recorte semantico.",
      "Se elevaron patrones transferibles del nivel actividad al nivel materia.",
      "Se preservo trazabilidad de citas recurrentes y controles de calidad.",
      "Se reforzo manejo de supuestos y fuentes provisionales no verificadas."
    ]
  }
}