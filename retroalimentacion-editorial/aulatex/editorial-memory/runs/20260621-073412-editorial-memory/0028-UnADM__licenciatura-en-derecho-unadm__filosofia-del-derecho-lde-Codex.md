{
  "summary": [
    "Se consolida la memoria de materia desde actividad-1 con abstraccion ascendente y deduplicacion lossless.",
    "Se preservan reglas utiles previas sin regresion y con trazabilidad a UnADM.",
    "Se mantiene normalizacion obligatoria para insumos no JSON parseable antes de toda propagacion.",
    "Se fija el patron editorial transferible: problema, conceptos, evidencia, analisis propio y conclusion juridica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y criterios academicos.",
    "Alinear contenidos a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica de entregables y memoria editorial.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local verificable.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local. [supuesto]",
    "Conservar trazabilidad a malla-curricular-derecho-unadm.pdf como respaldo curricular."
  ],
  "structure_rules": [
    "Abrir cada producto con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener correspondencia entre actividad, .tex y .bib de la materia."
  ],
  "activity_rules": [
    "Evitar entregas solo descriptivas; exigir postura argumentada del estudiante.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir fuentes de semanas posteriores para actividad-1 sin evidencia. [supuesto]",
    "Agregar solo fuentes especificas de actividad que sean comprobables."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizacion.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de [supuesto].",
    "Validar correspondencia entre consigna y tipo de producto entregado.",
    "Verificar consistencia entre citas en .tex y entradas en .bib."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar sin migracion completa.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir rutas o nombres anomalos antes de considerarlos canonicos."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras realmente consultables.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Registrar fuentes de actividad en el .bib de la materia con trazabilidad.",
    "Mantener como [supuesto] que filosofia-del-derecho-clean.bib corresponde a Semana 7 hasta confirmar alcance."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON, estructura y calidad.",
    "Elevar al ancestro patrones reutilizables, no redaccion literal de actividades.",
    "Conservar citas recurrentes y reglas de calidad como nucleo comun.",
    "Aplicar union-dedupe lossless en cada ciclo, sin recorte semantico.",
    "Evitar propagar nombres de archivo no verificados hasta correccion local."
  ],
  "open_questions": [
    "Confirmar consigna textual completa de actividad-1 para validar producto exacto.",
    "Confirmar nombre canonico final del .bib de la materia.",
    "Confirmar si actividad-1 reutiliza bibliografia existente o requiere .bib propio.",
    "Completar y verificar entrada truncada scjnIncapacidadResistencia2019 en .bib. [supuesto]"
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
      "Conceptos y marco normativo-doctrinal.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables con fundamento juridico, evidencia y postura propia.",
      "Asegurar continuidad editorial entre actividades, materia y niveles superiores."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable.",
      "Cierre juridico aplicable.",
      "Marcado explicito de [supuesto].",
      "Trazabilidad entre consigna, argumento y evidencia."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer conceptos y normas pertinentes.",
      "Contrastar doctrina o criterios.",
      "Sostener postura propia con fuentes.",
      "Concluir con criterio juridico practicable."
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
          "justification": "La interpretacion sustenta la construccion de razones juridicas."
        },
        {
          "source": "Argumentacion juridica",
          "target": "Analisis critico del fenomeno juridico",
          "kind": "develops",
          "justification": "Permite evaluar validez normativa y consecuencias."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "Integra debate axiologico y fundamento del deber juridico."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "La conclusion requiere soporte normativo verificable."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "Bib local: claves juridicas recurrentes y verificables.",
        "Actividad-1: patron problema-conceptos-evidencia-analisis-conclusion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 28: se elevo patron editorial de actividad a materia sin copia literal.",
      "Ciclo 28: se conservaron reglas de normalizacion y bloqueo por JSON no parseable.",
      "Ciclo 28: se reforzo trazabilidad entre consigna, .tex, .bib y control de supuestos.",
      "Ciclo 28: se deduplicaron reglas repetidas manteniendo cobertura semantica completa."
    ]
  }
}