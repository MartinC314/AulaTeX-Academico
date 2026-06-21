{
  "summary": [
    "Consolidar memoria de materia con abstraccion ascendente desde actividad-1.",
    "Preservar reglas validas previas sin regresion y con deduplicacion lossless.",
    "Mantener normalizacion obligatoria de insumos no JSON antes de propagar.",
    "Sostener identidad UnADM, trazabilidad curricular y cierre juridico con criterio propio.",
    "Elevar patrones reutilizables: problema, conceptos, evidencia, analisis propio y conclusion juridica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y redaccion.",
    "Alinear entregables a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna. [supuesto]",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local. [supuesto]",
    "Usar malla-curricular-derecho-unadm.pdf como fuente curricular verificada.",
    "Conservar referencias provisionales Codex y GPT-Pro hasta sustitucion verificada. [supuesto]"
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener trazabilidad entre actividad, .tex y .bib de la materia."
  ],
  "activity_rules": [
    "Delimitar problema central en cada actividad.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir fuentes de semanas posteriores para actividad-1. [supuesto]",
    "Validar que el producto corresponda exactamente a la consigna activa."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar no eliminacion de reglas utiles previas en cada ciclo."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar sin migracion completa.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo anomalos antes de compilar.",
    "Usar archivos .tex dedicados por tipo de entregable."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Registrar fuentes de actividad en el .bib de la materia con deduplicacion sin perdida.",
    "No completar entradas BibTeX truncadas sin verificacion local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas y estructuradas.",
    "Elevar al ancestro patrones argumentativos reutilizables, no redaccion literal.",
    "Conservar trazabilidad conceptual y citas recurrentes al subir de nivel.",
    "Aplicar union-dedupe lossless en cada ciclo de consolidacion.",
    "Registrar incidencias de parseo como riesgo de ingesta sin perder contenido util."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-1. [supuesto]",
    "Confirmar formato requerido: reporte, presentacion u otro.",
    "Confirmar rubrica especifica para calibrar profundidad argumentativa.",
    "Confirmar nombre canonico final del .bib de la asignatura.",
    "Confirmar si filosofia-del-derecho-clean.bib aplica a actividad-1 o solo semana 7. [supuesto]",
    "Completar y verificar la entrada truncada scjnIncapacidadResistencia2019."
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
      "Problema juridico o social como punto de partida.",
      "Conceptos, normas y doctrina pertinentes.",
      "Evidencia verificable y analisis propio.",
      "Conclusion juridica aplicable a la practica.",
      "Trazabilidad editorial entre actividad y materia."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos utiles y verificables.",
      "Unificar calidad editorial en reportes y presentaciones.",
      "Asegurar transferencia profesional del razonamiento juridico."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable y explicito.",
      "Marcado explicito de supuestos.",
      "Cierre con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer marco conceptual y normativo.",
      "Contrastar evidencia y doctrina.",
      "Sostener postura propia con citas.",
      "Concluir con implicacion juridica transferible."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofia del Derecho",
        "Hermeneutica e interpretacion juridica",
        "Argumentacion juridica",
        "Derecho y moral",
        "Justicia",
        "Analisis critico del fenomeno juridico",
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
          "justification": "La interpretacion sustenta la construccion de razones juridicas."
        },
        {
          "source": "Argumentacion juridica",
          "target": "Analisis critico del fenomeno juridico",
          "kind": "develops",
          "justification": "Permite evaluar normas, hechos y consecuencias."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "Integra debate axiologico y validez normativa."
        },
        {
          "source": "Marco normativo y doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "La conclusion exige soporte verificable."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "Actividad-1: patron estable problema-conceptos-evidencia-analisis-conclusion.",
        "Regla persistente: bloquear propagacion sin JSON parseable.",
        "Bib local: presencia de claves recurrentes en hermeneutica y argumentacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 17: se elevo patron nuclear desde actividad al nivel materia.",
      "Ciclo 17: se mantuvo compresion lossless por union y deduplicacion.",
      "Ciclo 17: se conservaron reglas historicas de normalizacion y control de calidad.",
      "Ciclo 17: se reforzo trazabilidad de citas y conceptos sin copiar redaccion literal."
    ]
  }
}