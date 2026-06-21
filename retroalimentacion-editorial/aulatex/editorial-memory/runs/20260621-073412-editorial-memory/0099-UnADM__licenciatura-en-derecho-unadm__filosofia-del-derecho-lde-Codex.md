{
  "summary": [
    "Se consolida la memoria de materia desde Actividad 1 con abstraccion ascendente y deduplicacion lossless.",
    "Se preservan reglas institucionales UnADM, trazabilidad curricular y normalizacion obligatoria de insumos.",
    "Se refuerza el patron editorial comun: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene control de riesgo por salidas no JSON parseable sin perder contenido util recuperable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y criterio academico.",
    "Alinear la materia a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local. [supuesto]",
    "Usar la malla curricular UnADM como respaldo curricular verificado."
  ],
  "structure_rules": [
    "Abrir cada producto con encuadre breve del problema juridico o social.",
    "Separar en secciones: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear el tipo de entrega a la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Mantener trazabilidad entre actividad, .tex y .bib de materia."
  ],
  "activity_rules": [
    "Delimitar problema y pregunta guia desde el inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Verificar coherencia entre consigna, desarrollo y conclusion.",
    "No asumir que fuentes de semanas posteriores aplican a Actividad 1. [supuesto]",
    "Agregar fuentes especificas de actividad solo tras verificacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizacion.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Evitar regresion: no eliminar reglas utiles previas."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar sin migracion completa.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres/rutas anomalas antes de fijarlas como canon. [supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Registrar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Conservar y deduplicar entradas existentes sin perdida semantica.",
    "No completar entradas truncadas sin verificacion local. [supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas y estructuradas.",
    "Elevar al ancestro patrones reutilizables, no redaccion literal de actividad.",
    "Transferir citas recurrentes y puertas de calidad como nucleo comun.",
    "Aplicar union-dedupe lossless en cada ciclo para evitar regresiones.",
    "Registrar incidencias de ingesta no parseable como riesgo persistente."
  ],
  "open_questions": [
    "Confirmar consigna textual completa de Actividad 1 para cerrar supuestos de formato.",
    "Confirmar nombre canonico final del .bib de la materia.",
    "Confirmar si filosofia-del-derecho-clean.bib es temporal o base consolidada. [supuesto]",
    "Completar y verificar la entrada scjnIncapacidadResistencia2019 en .bib. [supuesto]",
    "Corregir placeholders/tokens y nombres anomalos en README y programa analitico."
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
      "Problema juridico o social como detonador.",
      "Conceptos y marco normativo con evidencia.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible.",
      "Trazabilidad tecnica y editorial en LaTeX."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables.",
      "Sostener coherencia entre identidad institucional, calidad argumentativa y evidencia.",
      "Permitir reutilizacion segura de reglas entre actividades y niveles."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable y funcional.",
      "Cierre con criterio juridico propio.",
      "Marcado explicito de [supuesto] cuando falte evidencia."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Construir marco conceptual y normativo.",
      "Contrastar fuentes y elaborar postura propia.",
      "Concluir con aplicacion juridica concreta."
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
          "source": "Filosofia del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "Integra el debate entre validez normativa y justificacion axiologica."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "La conclusion profesional exige soporte verificable."
        }
      ],
      "evidence": [
        "README de materia: identidad y pauta editorial.",
        "Programa analitico: proposito y cinco ejes.",
        "Bibliografia local: claves juridicas recurrentes verificables.",
        "Memoria de Actividad 1: patron argumentativo estable transferible."
      ]
    },
    "reinforcement_log": [
      "Ciclo 99: se elevo ADN editorial desde actividad a materia sin recorte semantico.",
      "Ciclo 99: se deduplicaron reglas repetidas y variantes ortograficas.",
      "Ciclo 99: se preservaron riesgos de ingesta no parseable como controles persistentes.",
      "Ciclo 99: se reforzo trazabilidad entre consigna, .tex y .bib."
    ]
  }
}