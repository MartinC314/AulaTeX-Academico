{
  "summary": [
    "Se consolida sincronizacion transversal en materia destino con compresion lossless por union-dedupe.",
    "Se preservan reglas institucionales UnADM, gates de calidad y trazabilidad de herencia sin recorte.",
    "Se refuerza normalizacion obligatoria de JSON y estructura antes de propagacion recursiva.",
    "Se mantiene el nucleo editorial reusable: problema, conceptos o normas, evidencia, analisis propio y conclusion juridica.",
    "Supuesto: persiste incidencia historica de salidas no JSON parseables hasta verificacion de cierre."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre exacto de asignatura: Derecho de la contratacion internacional.",
    "Vincular entregas a Licenciatura en Derecho y contexto curricular local (semestre 6, bloque 2, obligatoria, 8 creditos).",
    "Usar la carpeta de materia como entrada canonica.",
    "Conservar trazabilidad del origen heredado y etiquetar fuentes no verificadas como provisionales.",
    "Marcar como supuesto todo dato no visible en consigna o planeacion oficial."
  ],
  "structure_rules": [
    "Estructurar cada entrega en: problema, conceptos o marco normativo, evidencia, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear formato final al producto solicitado por planeacion semanal.",
    "Separar con claridad contenido descriptivo y postura del estudiante.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "No eliminar reglas utiles previas; solo agregar mejoras verificables."
  ],
  "activity_rules": [
    "Identificar el problema juridico o social que activa la actividad.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar resumen puro.",
    "Vincular cada argumento con norma, doctrina, jurisprudencia o dato verificable.",
    "Declarar limites del analisis cuando falten datos de consigna.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar memoria.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Verificar correspondencia entre producto entregado y consigna local."
  ],
  "latex_rules": [
    "Mantener plantilla article en espanol, letterpaper y oneside cuando aplique.",
    "Conservar macros institucionales de curso, universidad y autor.",
    "Completar documenttitle y documentsubtitle segun actividad real.",
    "Usar codificacion correcta de acentos en .tex y .bib.",
    "Evitar paquetes o comandos no estandar sin justificacion editorial.",
    "Corregir tokens sin expandir y nombres corruptos en README o programa antes de referenciarlos."
  ],
  "bibliography_rules": [
    "Usar derecho-de-la-contratacion-internacional.bib como repositorio principal de materia.",
    "Agregar fuentes especificas por actividad en el .bib local.",
    "No inventar referencias; usar solo obras consultables.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Mantener claves BibTeX estables y metadatos minimos completos.",
    "No citar fuentes heredadas de otros nodos si no fueron consultadas en destino."
  ],
  "propagation_hints": [
    "Propagar de forma recursiva solo tras validar JSON y estructura.",
    "Transferir solo abstracciones editoriales estables en nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates y grafo conceptual sobre redaccion literal.",
    "No sobrescribir reglas locales mas especificas con reglas institucionales generales.",
    "Mantener aviso de incidente JSON historico hasta confirmacion explicita de resolucion.",
    "Aplicar deduplicacion semantica por union, sin perdida de reglas utiles."
  ],
  "open_questions": [
    "Confirmar si la incidencia de JSON no parseable ya quedo cerrada en este ciclo.",
    "Definir formato uniforme de cita juridica para norma, jurisprudencia y doctrina.",
    "Confirmar checklist minimo por tipo de producto: reporte, presentacion y visual.",
    "Supuesto: README y programa aun requieren correccion final de placeholders de slug.",
    "Confirmar si existe planeacion oficial de actividades con consignas por semana."
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
        "Semestre 6, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Derecho de la contratacion internacional."
      ]
    },
    "essence": [
      "Problema juridico bien delimitado.",
      "Marco conceptual o normativo pertinente.",
      "Evidencia verificable.",
      "Analisis propio con postura.",
      "Conclusion juridica aplicable."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros, fundados y transferibles.",
      "Asegurar coherencia entre consigna, desarrollo argumentativo y cierre profesional."
    ],
    "style_markers": [
      "Supuestos explicitos cuando falten datos.",
      "Trazabilidad de herencia y fuentes provisionales.",
      "Separacion nitida entre descripcion y argumento propio.",
      "Cierre con criterio juridico operativo."
    ],
    "argumentative_patterns": [
      "Problema -> marco normativo/doctrinal -> evidencia -> analisis -> conclusion.",
      "Afirmacion juridica -> cita verificable -> interpretacion propia.",
      "Consigna local -> producto alineado -> control final de coherencia."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Compresion lossless por deduplicacion",
        "Trazabilidad de herencia",
        "Problema juridico",
        "Marco normativo o doctrinal",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin JSON valido no se reutiliza memoria de forma segura."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y formato consistente."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El analisis se activa desde una pregunta juridica concreta."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion juridica",
          "kind": "supports",
          "justification": "La conclusion debe apoyarse en fundamento verificable."
        },
        {
          "source": "Compresion lossless por deduplicacion",
          "target": "Trazabilidad de herencia",
          "kind": "supports",
          "justification": "Permite consolidar reglas sin perder memoria util."
        }
      ],
      "evidence": [
        "README de materia con ubicacion curricular y pauta editorial.",
        "Programa analitico con ejes de trabajo reutilizables.",
        "Archivo BibTeX local con fuentes institucionales base.",
        "Registro historico de incidente JSON no parseable en herencia institucional."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: se deduplican reglas repetidas y se preserva contenido util previo.",
      "Ciclo 2: se transfiere solo abstraccion estable desde actividad origen a materia destino.",
      "Ciclo 2: se refuerzan quality gates de JSON, estructura y respaldo de afirmaciones.",
      "Ciclo 2: se mantiene estado provisional de fuentes heredadas no verificadas.",
      "Ciclo 2: se fortalecen conexiones entre identidad, patron argumentativo y grafo conceptual."
    ]
  }
}