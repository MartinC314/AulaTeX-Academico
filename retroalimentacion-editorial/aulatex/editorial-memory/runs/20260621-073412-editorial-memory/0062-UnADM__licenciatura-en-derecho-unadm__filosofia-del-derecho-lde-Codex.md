{
  "summary": [
    "Consolidar memoria de materia de Filosofia del Derecho con identidad UnADM.",
    "Elevar desde actividad-1 patrones reutilizables sin copiar redaccion literal.",
    "Mantener compresion lossless por union y deduplicacion sin regresion.",
    "Preservar normalizacion obligatoria para insumos no JSON parseable.",
    "Reforzar ejes editoriales transferibles: problema, conceptos, evidencia, analisis propio y conclusion juridica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y trazabilidad.",
    "Alinear la materia a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica de entregables.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local. [supuesto]",
    "Conservar referencia de riesgo de ingesta por salidas no parseables de Codex y GPT-Pro."
  ],
  "structure_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener trazabilidad entre actividad, .tex y .bib de la materia."
  ],
  "activity_rules": [
    "Iniciar cada actividad con problema delimitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir que fuentes de semanas posteriores aplican a actividad-1. [supuesto]",
    "Confirmar correspondencia exacta entre consigna y tipo de producto."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Validar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar no regresion de reglas utiles heredadas en cada ciclo."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas.",
    "No renombrar claves citadas sin migracion completa.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo anom
alos antes de tratarlos como canon. [supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "Registrar fuentes de actividad en el .bib canonico de la asignatura.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente editorial o URL.",
    "No completar entradas truncadas sin verificacion local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas y normalizadas.",
    "Elevar al ancestro patrones editoriales, no redaccion literal de actividades.",
    "Reutilizar puertas de calidad institucional en nodos laterales.",
    "Mantener etiqueta union-dedupe lossless en toda propagacion.",
    "Evitar propagar nombres anom
alos hasta correccion local.",
    "Conservar trazabilidad de citas recurrentes al subir de actividad a materia."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-1 para fijar formato final. [supuesto]",
    "Confirmar nombre canonico definitivo del .bib de la materia. [supuesto]",
    "Confirmar si filosofia-del-derecho-clean.bib es solo semanal o base reutilizable. [supuesto]",
    "Completar y verificar entrada truncada scjnIncapacidadResistencia2019. [supuesto]",
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
      "Resolver problemas juridicos con fundamento conceptual y normativo.",
      "Transformar planeacion semanal en productos academicos trazables.",
      "Integrar evidencia verificable, analisis propio y conclusion aplicable."
    ],
    "reason_for_being": [
      "Estandarizar calidad editorial de la materia.",
      "Asegurar coherencia entre consigna, argumento y evidencia.",
      "Facilitar propagacion segura de reglas utiles a nivel superior."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable por funcion argumentativa.",
      "Marcado explicito de supuestos.",
      "Cierre con criterio juridico propio.",
      "Trazabilidad cita-.bib obligatoria."
    ],
    "argumentative_patterns": [
      "Problema delimitado -> marco conceptual/normativo -> analisis propio -> conclusion transferible.",
      "Afirmacion sustantiva -> evidencia verificable -> inferencia juridica.",
      "Consigna semanal -> tipo de producto -> validacion de cumplimiento."
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
          "justification": "La interpretacion fundamenta la construccion de razones juridicas."
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
          "justification": "La conclusion exige sustento verificable."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "Integra debate sobre validez, justicia y etica."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "Actividad-1: patron estable de estructura argumentativa.",
        "Regla persistente: bloquear propagacion no parseable.",
        "Bibliografia local: claves juridicas recurrentes y verificables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 62: se elevo patron de actividad a materia con abstraccion ascendente.",
      "Se deduplicaron reglas repetidas manteniendo cobertura total.",
      "Se conservaron controles de calidad heredados sin eliminaciones.",
      "Se reforzo trazabilidad conceptual y de citas recurrentes.",
      "Se marcaron supuestos pendientes de verificacion local."
    ]
  }
}