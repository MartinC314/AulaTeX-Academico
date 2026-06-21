{
  "summary": [
    "Se consolida en materia la memoria valida de actividad-1 con abstraccion ascendente.",
    "Se preservan reglas utiles previas sin regresion y con deduplicacion lossless.",
    "Se refuerzan ejes editoriales transferibles: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene normalizacion obligatoria para insumos no JSON parseable antes de propagar.",
    "Se conserva trazabilidad entre README, programa analitico, .tex y .bib."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, redaccion y formato.",
    "Alinear la materia a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica de entregables y memoria.",
    "Marcar como [supuesto] todo dato no visible en consigna o archivo fuente.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local. [supuesto]",
    "Usar malla-curricular-derecho-unadm.pdf como respaldo curricular verificado."
  ],
  "structure_rules": [
    "Abrir cada producto con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear el tipo de entregable a la planeacion semanal.",
    "Mantener trazabilidad entre actividad, archivo .tex y archivo .bib."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir fuentes de semanas posteriores como obligatorias para actividad-1. [supuesto]",
    "Verificar que el producto corresponda a la consigna especifica de la actividad."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en texto y entradas en .bib.",
    "Confirmar no regresion: no eliminar reglas utiles heredadas."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar sin migracion completa.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo anómalos antes de fijarlos como canon. [supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "Registrar fuentes de actividad en el .bib canonico de la asignatura.",
    "No inventar referencias; usar solo obras realmente consultables.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente/editorial o URL.",
    "Tratar entradas truncadas como pendientes de verificacion local. [supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas por README, programa analitico y .bib local.",
    "Elevar patrones reutilizables; no copiar redaccion literal de actividades.",
    "Conservar trazabilidad de citas recurrentes al subir a niveles ancestro.",
    "Aplicar union-dedupe lossless en cada ciclo de consolidacion.",
    "Registrar incidencias de parseo como riesgo de ingesta sin perder contenido util."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-1 para cerrar supuestos de formato.",
    "Confirmar nombre canonico final del archivo .bib de la materia.",
    "Confirmar si filosofia-del-derecho-clean.bib se integra o se mantiene separado por semana. [supuesto]",
    "Completar y verificar la entrada truncada scjnIncapacidadResistencia2019 en .bib. [supuesto]"
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
      "Problema juridico o social delimitado.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable.",
      "Analisis propio con postura.",
      "Conclusion juridica aplicable."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables.",
      "Sostener una escritura juridica clara, fundada y transferible.",
      "Operar memoria editorial persistente sin perder reglas utiles."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable por funcion argumentativa.",
      "Cierre con criterio juridico propio.",
      "Marcado explicito de [supuesto] cuando falte verificacion."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer marco conceptual y normativo.",
      "Analizar con postura propia y evidencia.",
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
        "Ejes editoriales: problema, conceptos, evidencia, analisis propio, conclusion juridica"
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
          "justification": "La interpretacion funda la construccion de razones juridicas."
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
          "justification": "La conclusion exige soporte verificable."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "Integra el debate entre validez, justicia y etica."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y ejes de trabajo.",
        "Bibliografia local .bib: claves y fuentes juridicas verificables.",
        "Actividad-1: patron estable de estructura argumentativa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 24: elevacion de patrones desde actividad-1 a materia completada.",
      "Se eliminaron duplicados semanticos y se conservaron reglas transferibles.",
      "Se reforzo control de parseo JSON y normalizacion previa a propagacion.",
      "Se mantuvo trazabilidad de citas recurrentes y pendientes con [supuesto]."
    ]
  }
}