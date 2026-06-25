{
  "summary": [
    "Consolidar memoria de materia de Filosofia del Derecho con identidad UnADM.",
    "Aplicar compresion lossless por union-dedupe sin eliminar reglas utiles previas.",
    "Mantener normalizacion obligatoria de insumos no JSON parseable antes de propagar.",
    "Elevar desde actividad-1 el patron: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Conservar trazabilidad entre README, programa analitico, .tex y .bib de la materia."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, redaccion y formato.",
    "Alinear entregables a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Usar malla-curricular-derecho-unadm.pdf como respaldo curricular verificado."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear cada entrega al tipo de producto solicitado en planeacion semanal.",
    "Mantener trazabilidad entre actividad, archivo .tex y archivo .bib."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir que fuentes de semanas posteriores aplican a actividad-1.",
    "Agregar fuentes especificas de actividad solo tras verificacion local.",
    "Conservar vinculo editorial con los cinco ejes del programa analitico."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en texto y entradas en .bib.",
    "Verificar correspondencia del producto con la consigna de la actividad."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar sin migracion completa.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres/rutas anomalas antes de tratarlos como canon."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Registrar fuentes de actividad en .bib de materia con deduplicacion sin perdida.",
    "No completar entradas truncadas sin verificacion local. [supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas por README, programa analitico y .bib local.",
    "Elevar al ancestro patrones reutilizables, no redaccion literal de actividad.",
    "Conservar trazabilidad de citas recurrentes al subir de actividad a materia.",
    "Mantener bitacora de riesgos de ingesta por salidas no parseables.",
    "Evitar regresion: nunca eliminar puertas de calidad ya activas.",
    "Aplicar normalizacion manual en ciclos con insumos no estructurados."
  ],
  "open_questions": [
    "Confirmar nombre canonico final del .bib de materia frente a token Slug. [supuesto]",
    "Confirmar producto exacto exigido por la consigna de actividad-1. [supuesto]",
    "Confirmar si bibliografia de Semana 7 se reutiliza en actividad-1. [supuesto]",
    "Completar y verificar entrada scjnIncapacidadResistencia2019 truncada. [supuesto]",
    "Sustituir referencias provisionales heredadas (Codex/GPT-Pro) por fuentes verificadas."
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
      "Convertir planeacion semanal en productos academicos solidos.",
      "Asegurar trazabilidad editorial y juridica en toda actividad.",
      "Sostener continuidad metodologica entre actividades y materia."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable.",
      "Cierre con criterio juridico propio.",
      "Marcado explicito de [supuesto].",
      "Citas verificables y consistentes con .bib."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer marco conceptual-normativo.",
      "Analizar con postura propia.",
      "Concluir con aplicacion practica juridica.",
      "Verificar coherencia interna del hilo argumental."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofia del Derecho",
        "Hermeneutica e interpretacion juridica",
        "Argumentacion juridica",
        "Derecho y moral",
        "Justicia",
        "Analisis critico del fenomeno juridico",
        "Ejes editoriales de actividad transferidos a materia"
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
          "justification": "Permite evaluar validez, justificacion y consecuencias."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "Integra debate axiologico y normativo."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "La conclusion exige soporte normativo verificable."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "Actividad-1: patron problema-conceptos-evidencia-analisis-conclusion.",
        "Regla persistente: bloquear propagacion sin JSON parseable.",
        "Regla persistente: no inventar fuentes y marcar [supuesto]."
      ]
    },
    "reinforcement_log": [
      "Ciclo 6: se elevaron patrones de actividad al nivel materia sin copiar texto literal.",
      "Ciclo 6: se deduplicaron reglas equivalentes preservando cobertura funcional.",
      "Ciclo 6: se reforzaron puertas de calidad de parseo JSON y trazabilidad bibtex.",
      "Ciclo 6: se conservaron referencias provisionales como provisionales con marca [supuesto].",
      "Ciclo 6: se mantuvo estrategia progresiva y sintetica con abstraccion ascendente."
    ]
  }
}