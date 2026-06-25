{
  "summary": [
    "Se consolida sincronizacion transversal desde actividad de otra materia con transferencia solo de abstracciones estables.",
    "Se preservan reglas utiles previas del destino sin eliminaciones y con deduplicacion semantica lossless.",
    "Se refuerzan ejes editoriales comunes UnADM: problema, conceptos/normas, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene incidente historico de salidas no JSON parseable como riesgo activo hasta verificacion de resolucion.",
    "Se confirma contexto local de la materia destino: semestre 6, bloque 2, obligatoria, 8 creditos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre exacto de asignatura: Derecho de la contratacion internacional.",
    "Vincular entregas a Licenciatura en Derecho y contexto curricular local.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar trazabilidad de reglas heredadas por nodo origen."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "No transferir redaccion literal entre nodos no equivalentes; solo patrones reutilizables."
  ],
  "activity_rules": [
    "Diferenciar resumen descriptivo y postura argumentada del estudiante.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Vincular argumentos con norma, doctrina o evidencia pertinente.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Declarar limites del analisis cuando falten datos de la actividad.",
    "No asumir fuentes de otras semanas o materias sin validacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar memoria.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregable y consigna local."
  ],
  "latex_rules": [
    "Mantener plantilla article en espanol con letterpaper y oneside cuando aplique.",
    "Conservar macros institucionales de curso, universidad y metadatos.",
    "Completar \\documenttitle y \\documentsubtitle segun actividad real.",
    "Usar acentos y codificacion correctos en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion.",
    "Evitar paquetes o comandos no estandar sin justificacion verificable.",
    "Corregir placeholders y rutas corruptas en README y programa antes de referenciar archivos."
  ],
  "bibliography_rules": [
    "Usar derecho-de-la-contratacion-internacional.bib como repositorio principal.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; incluir solo obras consultables.",
    "Registrar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Incluir fecha de consulta en fuentes web o mutables.",
    "No citar fuentes heredadas del origen si no fueron usadas en el destino.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validacion JSON y gates de calidad.",
    "Aplicar union-dedupe lossless por regla semantica, no por recorte textual.",
    "Preservar reglas locales mas especificas del destino ante reglas generales heredadas.",
    "Etiquetar como provisional toda herencia con verificacion pendiente.",
    "Mantener registro del incidente JSON historico hasta cierre confirmado.",
    "Si falta consigna local, propagar solo reglas institucionales generales."
  ],
  "open_questions": [
    "Supuesto: la incidencia de JSON no parseable sigue activa; confirmar cierre en ciclo actual.",
    "Confirmar checklist minimo por tipo de actividad: reporte, presentacion y producto visual.",
    "Confirmar formato uniforme de citas juridicas para norma, jurisprudencia y doctrina.",
    "Supuesto: README y programa aun requieren normalizacion de placeholders de slug.",
    "Confirmar si existe rubrica oficial especifica por actividad en esta materia."
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
      "Problema juridico activa el desarrollo.",
      "Marco conceptual y normativo sostiene argumentos.",
      "Evidencia verificable respalda afirmaciones.",
      "Analisis propio evita trabajo meramente descriptivo.",
      "Conclusion juridica transfiere a practica profesional."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros, fundados y evaluables.",
      "Garantizar consistencia institucional y calidad tecnica en contenidos LaTeX y bibliografia.",
      "Permitir propagacion segura entre nodos mediante memoria estructurada y trazable."
    ],
    "style_markers": [
      "Supuestos explicitos cuando falte evidencia local.",
      "Separacion clara entre descripcion y postura propia.",
      "Cierre con criterio juridico aplicable.",
      "Trazabilidad visible de herencia editorial."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/normas -> evidencia -> analisis -> conclusion.",
      "Afirmacion juridica -> fuente verificable -> interpretacion propia.",
      "Consigna local -> producto alineado -> verificacion final."
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
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin JSON valido no se permite reutilizacion segura."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El analisis se construye desde una pregunta juridica concreta."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusion juridica",
          "kind": "supports",
          "justification": "La conclusion debe sostenerse en fundamento verificable."
        },
        {
          "source": "Compresion lossless por deduplicacion",
          "target": "Trazabilidad de herencia",
          "kind": "supports",
          "justification": "Conserva memoria util sin perdida de reglas."
        }
      ],
      "evidence": [
        "README de materia con identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico con ejes de trabajo reutilizables.",
        "Archivo .bib local con fuentes institucionales base.",
        "Historial de incidentes de salida no JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 5: deduplicadas reglas repetidas y preservadas reglas utiles previas del destino.",
      "Ciclo 5: transferidas solo abstracciones estables desde actividad origen transversal.",
      "Ciclo 5: reforzados gates de JSON, estructura minima y trazabilidad.",
      "Ciclo 5: mantenidos vacios de contexto local como preguntas abiertas con marca de supuesto."
    ]
  }
}