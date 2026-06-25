{
  "summary": [
    "Se consolida sincronizacion transversal conservadora desde actividad no equivalente hacia materia.",
    "Se preservan reglas utiles previas y se elimina duplicidad semantica sin recorte.",
    "Se refuerza ADN UnADM con foco en estructura argumentativa juridica reusable.",
    "Se mantiene incidente historico de salidas no JSON parseables como control activo hasta verificacion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre exacto de asignatura: Derecho de la contratacion internacional.",
    "Vincular entregas a Licenciatura en Derecho y contexto curricular local (semestre 6, bloque 2, obligatoria, 8 creditos).",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna o planeacion oficial.",
    "Tratar herencias no verificadas como provisionales con trazabilidad de origen."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "No sustituir reglas locales especificas por reglas generales heredadas."
  ],
  "activity_rules": [
    "Diferenciar resumen descriptivo y postura propia.",
    "Sustentar afirmaciones con fuente verificable y cita explicita.",
    "Vincular cada argumento con norma, doctrina, jurisprudencia o evidencia pertinente.",
    "Verificar coherencia entre consigna, desarrollo y conclusion.",
    "Declarar limites del analisis cuando falten datos de actividad.",
    "Evitar asumir fuentes de otras semanas sin confirmacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar esquema minimo completo antes de reutilizacion aguas abajo.",
    "Confirmar que toda afirmacion normativa tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar y normalizar respuestas no estructuradas antes de propagar.",
    "Verificar correspondencia entre README, programa analitico y archivos reales."
  ],
  "latex_rules": [
    "Mantener clase article en espanol, letterpaper y oneside segun plantilla local.",
    "Conservar macros institucionales de curso y universidad.",
    "Completar \\documenttitle y \\documentsubtitle segun actividad real.",
    "Usar \\coursename y \\universitydepartment con nombre exacto de la asignatura.",
    "Evitar paquetes o comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, referencias rotas ni tokens sin expandir en rutas."
  ],
  "bibliography_rules": [
    "Usar derecho-de-la-contratacion-internacional.bib como repositorio principal.",
    "No inventar fuentes; incluir solo obras consultables.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Registrar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Incluir fecha de consulta en recursos web o mutables.",
    "No citar fuentes heredadas del origen si no fueron usadas en el destino."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validacion JSON y gates de calidad.",
    "Transferir solo abstracciones estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, calidad y grafo conceptual.",
    "Aplicar union-dedupe lossless por regla semantica, no por recorte textual.",
    "Conservar bandera de incidente historico JSON hasta confirmacion explicita de cierre.",
    "Normalizar placeholders y rutas corruptas antes de difusion lateral o superior."
  ],
  "open_questions": [
    "Confirmar si la incidencia de JSON no parseable ya quedo resuelta en este ciclo.",
    "Definir formato uniforme de cita juridica para norma, jurisprudencia y doctrina.",
    "Confirmar checklist minimo por tipo de producto: reporte, presentacion, visual.",
    "Supuesto: README y programa aun requieren correccion de placeholders Slug y lineas corruptas.",
    "Confirmar consignas oficiales por actividad para evitar sobre-generalizacion."
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
        "Entrada canonica por carpeta de materia."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 6, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Derecho de la contratacion internacional."
      ]
    },
    "essence": [
      "Problema juridico claro.",
      "Marco conceptual y normativo pertinente.",
      "Evidencia verificable.",
      "Analisis propio no descriptivo.",
      "Conclusion juridica aplicable."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con rigor juridico y utilidad profesional.",
      "Sostener consistencia institucional y tecnica en toda entrega LaTeX."
    ],
    "style_markers": [
      "Supuestos explicitados cuando falten datos.",
      "Separacion nitida entre descripcion y postura.",
      "Cierre con criterio juridico transferible.",
      "Trazabilidad de reglas heredadas."
    ],
    "argumentative_patterns": [
      "Problema -> marco normativo/doctrinal -> evidencia -> analisis -> conclusion.",
      "Afirmacion juridica -> fuente verificable -> interpretacion propia.",
      "Consigna local -> producto alineado -> validacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Compresion lossless por deduplicacion",
        "Problema juridico",
        "Marco normativo/doctrinal",
        "Analisis propio",
        "Conclusion juridica",
        "Bibliografia verificable",
        "Trazabilidad de herencia"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica con citas verificables",
          "kind": "supports",
          "justification": "La pauta institucional exige evidencia verificable y formato consistente."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin JSON valido no hay reutilizacion segura."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "La argumentacion se activa por una pregunta juridica concreta."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusion juridica",
          "kind": "supports",
          "justification": "La conclusion requiere fundamento normativo o doctrinal."
        },
        {
          "source": "Compresion lossless por deduplicacion",
          "target": "Trazabilidad de herencia",
          "kind": "supports",
          "justification": "Permite consolidar sin perder reglas utiles previas."
        }
      ],
      "evidence": [
        "README de materia con identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico con proposito y ejes de trabajo reutilizables.",
        "Bib local existente como repositorio canonico.",
        "Registro historico de incidentes JSON no parseable en memoria heredada."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas de tono, estructura y calidad sin perdida funcional.",
      "Se transfirieron solo abstracciones estables del origen de Filosofia del Derecho.",
      "Se evitaron contenidos tematicos especificos del nodo origen no aplicables al destino.",
      "Se reforzaron gates de JSON, supuestos y trazabilidad como controles persistentes."
    ]
  }
}