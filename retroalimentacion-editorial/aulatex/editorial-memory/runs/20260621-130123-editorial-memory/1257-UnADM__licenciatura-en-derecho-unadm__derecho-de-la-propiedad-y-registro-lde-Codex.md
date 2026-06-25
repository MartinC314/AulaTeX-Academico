{
  "summary": [
    "Sincronizacion transversal aplicada con union-dedupe y sin regresion.",
    "Se transfieren solo abstracciones estables desde actividad de Filosofia del Derecho.",
    "Se refuerzan ejes comunes: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene normalizacion obligatoria para salidas no JSON parseables.",
    "Se conserva identidad institucional UnADM y contexto curricular local de la materia destino."
  ],
  "identity_rules": [
    "Mantener identidad explicita UnADM en tono, portada y metadatos.",
    "Usar nombre exacto de materia: Derecho de la propiedad y registro.",
    "Conservar programa: Licenciatura en Derecho.",
    "Conservar ubicacion curricular verificada: semestre 7, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante y evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir fuentes de semanas posteriores sin validar consigna.",
    "Relacionar el desarrollo con propiedad y registro cuando aplique."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de propagarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto final y consigna de actividad."
  ],
  "latex_rules": [
    "Mantener codificacion y acentos correctos en español en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Mantener claves BibTeX estables.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir placeholders en portada y tabla de autor antes de entrega."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Registrar fuentes especificas por actividad en derecho-de-la-propiedad-y-registro.bib.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Compartir entre nodos no equivalentes solo reglas editoriales abstractas y estables.",
    "Evitar transferir redaccion literal o contenido tematico especifico de otra materia.",
    "Reforzar gates de calidad e identidad institucional en nodos laterales UnADM.",
    "Mantener estrategia progresiva y conservadora sin eliminar reglas utiles previas."
  ],
  "open_questions": [
    "Supuesto: falta rubrica local detallada por actividad; confirmar criterio de evaluacion.",
    "Confirmar estilo de citacion juridica solicitado por figura docente.",
    "Confirmar si cada actividad exige reporte, presentacion u otro producto.",
    "Confirmar correccion definitiva de rutas con tokens corruptos en README.",
    "Confirmar sustitucion del placeholder 'Figura docente' en plantilla .tex."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Accionable y verificable."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada antes de propagacion.",
        "Entrada canonica por carpeta de asignatura."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho de la propiedad y registro.",
        "Semestre 7, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico.",
      "Conceptos y marco normativo.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos con fundamento juridico y criterio propio.",
      "Asegurar trazabilidad editorial y bibliografica reutilizable en ciclos recursivos."
    ],
    "style_markers": [
      "Frases breves y accionables.",
      "Supuestos marcados explicitamente.",
      "Sin afirmaciones sin fuente.",
      "Sin placeholders al cierre."
    ],
    "argumentative_patterns": [
      "Del problema al marco conceptual.",
      "Del marco normativo a la evidencia.",
      "De la evidencia al analisis propio.",
      "Del analisis a la conclusion aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalizacion JSON",
        "Problema juridico",
        "Marco normativo/doctrinal",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion transferible",
        "Trazabilidad bibliografica"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "El marco institucional exige formato consistente y citas verificables."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay reutilizacion segura."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis debe responder a la pregunta juridica planteada."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion requiere fundamento normativo verificable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Trazabilidad bibliografica",
          "kind": "develops",
          "justification": "La evidencia exige consistencia entre texto y .bib."
        }
      ],
      "evidence": [
        "README de la materia: identidad UnADM y pauta editorial.",
        "Programa analitico: ejes de trabajo y proposito de realizacion.",
        "Archivo .bib local con claves institucionales verificables.",
        "Regla consolidada: bloquear propagacion de salidas no JSON parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 7: deduplicadas reglas repetidas y conservadas reglas utiles previas.",
      "Ciclo 7: transferidas abstracciones estables transversales sin contenido literal de Filosofia del Derecho.",
      "Ciclo 7: reforzados gates de calidad, normalizacion JSON y trazabilidad bibliografica.",
      "Ciclo 7: mantenidos supuestos abiertos de contexto local sin inventar fuentes."
    ]
  }
}