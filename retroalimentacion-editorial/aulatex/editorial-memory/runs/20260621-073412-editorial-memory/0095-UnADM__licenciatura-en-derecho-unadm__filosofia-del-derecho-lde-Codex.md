{
  "summary": [
    "Se consolida memoria de materia desde actividad-1 con abstraccion ascendente y deduplicacion lossless.",
    "Se preservan reglas utiles previas sin regresion y se normalizan variantes duplicadas.",
    "Se refuerza identidad UnADM, trazabilidad curricular y entrada canonica por carpeta de materia.",
    "Se elevan patrones transferibles: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene riesgo de ingesta por salidas no JSON parseable y su bloqueo preventivo."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en redaccion y formato.",
    "Alinear entregables con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en la consigna. [supuesto]",
    "Usar malla-curricular-derecho-unadm.pdf como fuente curricular verificada.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local. [supuesto]",
    "Conservar referencias provisionales Codex y GPT-Pro hasta sustitucion verificada. [supuesto]"
  ],
  "structure_rules": [
    "Iniciar cada producto con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear el entregable al producto solicitado por la planeacion semanal.",
    "Mantener trazabilidad entre actividad, archivo .tex y .bib de materia."
  ],
  "activity_rules": [
    "Delimitar problema juridico o social al inicio de cada actividad.",
    "Integrar conceptos, normas, doctrina o datos pertinentes al problema.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante y evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir que fuentes de semanas posteriores aplican a actividad-1. [supuesto]"
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar que no se eliminen reglas utiles previas en cada ciclo."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables y no renombrarlas sin migracion completa.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Separar entregables por tipo en archivos .tex dedicados.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico. [supuesto]",
    "No adoptar nombres anomalos como canon hasta correccion local. [supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "Registrar fuentes de actividad en el .bib de la asignatura con metadatos minimos.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar y deduplicar entradas existentes sin perdida de informacion.",
    "Mantener como provisional el uso de filosofia-del-derecho-clean.bib fuera de Semana 7. [supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas por README, programa analitico y .bib local.",
    "Elevar al ancestro patrones reutilizables, no redaccion literal de actividades.",
    "Reusar puertas de calidad institucionales antes de cualquier propagacion lateral.",
    "Registrar incidencias de parseo como riesgo de ingesta sin descartar contenido util.",
    "Aplicar union-dedupe lossless y evitar regresiones semanticas."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-1 para cerrar supuestos de formato.",
    "Confirmar nombre canonico final del .bib de materia frente al placeholder Slug.",
    "Determinar si filosofia-del-derecho-clean.bib se reutiliza fuera de Semana 7. [supuesto]",
    "Verificar integridad completa de la entrada scjnIncapacidadResistencia2019. [supuesto]",
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
        "Carpeta de materia como entrada canonica editorial."
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
      "Producto solicitado por la planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion transferible a la practica juridica."
    ],
    "reason_for_being": [
      "Transformar la planeacion semanal en productos academicos con fundamento juridico y evidencia.",
      "Estandarizar calidad editorial reproducible entre actividades de la materia.",
      "Asegurar transferencia profesional del cierre argumentativo."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable y trazable.",
      "Citas verificables en afirmaciones sustantivas.",
      "Marcado explicito de supuestos.",
      "Cierre juridico aplicable."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer marco conceptual y normativo.",
      "Analizar con postura propia.",
      "Sustentar con evidencia verificable.",
      "Concluir con transferencia a practica juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofia del Derecho",
        "Hermeneutica e interpretacion juridica",
        "Argumentacion juridica",
        "Derecho y moral",
        "Justicia",
        "Analisis critico del fenomeno juridico",
        "Trazabilidad actividad-tex-bib"
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
          "source": "Marco normativo y doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "La conclusion requiere soporte verificable."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "Integra debate axiologico y fundamento del derecho."
        }
      ],
      "evidence": [
        "README de materia y pauta editorial.",
        "Programa analitico y cinco ejes de trabajo.",
        "filosofia-del-derecho-clean.bib con claves juridicas recurrentes.",
        "Regla persistente de bloqueo por salida no JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 95: se elevo patron de actividad a materia sin copiar redaccion literal.",
      "Ciclo 95: se deduplicaron variantes ortograficas y semanticas sin perdida.",
      "Ciclo 95: se mantuvieron reglas de calidad heredadas de parseo y normalizacion.",
      "Ciclo 95: se conservaron citas recurrentes y trazabilidad bibliografica transferible."
    ]
  }
}