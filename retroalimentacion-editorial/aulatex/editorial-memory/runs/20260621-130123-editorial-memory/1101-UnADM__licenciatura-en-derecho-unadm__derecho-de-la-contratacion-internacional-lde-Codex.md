{
  "summary": [
    "Se consolida sincronizacion transversal desde actividad no equivalente con transferencia por abstracciones estables.",
    "Se preservan reglas utiles previas sin regresion y con deduplicacion lossless.",
    "Se refuerza nucleo editorial UnADM: problema, conceptos o normas, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene gate estricto: no propagar si la salida no es JSON parseable.",
    "Se confirma contexto local de materia: semestre 6, bloque 2, obligatoria, 8 creditos.",
    "Se mantiene normalizacion de rutas y placeholders corruptos en README y programa como deuda tecnica activa."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre exacto de asignatura: Derecho de la contratacion internacional.",
    "Vincular entregas a Licenciatura en Derecho.",
    "Usar carpeta de materia como entrada canonica.",
    "Conservar coursecode local LDE-S6B2 cuando aplique plantilla vigente.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales.",
    "Conservar trazabilidad del origen heredado en cada ciclo."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto final con la consigna semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Transformar planeacion semanal en reporte, presentacion o producto visual segun consigna.",
    "No eliminar reglas utiles previas; solo anexar mejoras verificables."
  ],
  "activity_rules": [
    "Identificar problema juridico que activa la actividad.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Diferenciar resumen descriptivo de postura propia.",
    "Vincular argumentos con norma, doctrina o evidencia.",
    "Declarar limites del analisis cuando falten datos.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar uso de fuentes de otras semanas sin confirmacion de pertinencia local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar memoria.",
    "Revisar y normalizar respuestas no estructuradas antes de propagar.",
    "Confirmar que afirmaciones normativas tengan respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre README, programa analitico y archivos reales.",
    "Aplicar deduplicacion semantica por regla, no por recorte."
  ],
  "latex_rules": [
    "Mantener clase article en espanol con letterpaper y oneside si usa plantilla actual.",
    "Conservar macros institucionales de curso, universidad y autor.",
    "Completar documenttitle y documentsubtitle segun actividad real.",
    "Usar coursename exacto de la asignatura.",
    "No sustituir macros institucionales por texto libre sin justificacion.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir tokens sin expandir tipo $(@{...}.Slug) en README y programa antes de automatizar rutas."
  ],
  "bibliography_rules": [
    "Usar derecho-de-la-contratacion-internacional.bib como repositorio principal.",
    "No inventar referencias; usar solo fuentes consultables.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas pertinentes.",
    "Agregar fuentes especificas por actividad al .bib local.",
    "Usar claves BibTeX estables y descriptivas.",
    "Incluir fecha de consulta en fuentes web o mutables.",
    "No citar fuentes heredadas del origen si no fueron usadas en destino."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validacion JSON y estructura.",
    "Compartir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "No transferir redaccion literal de actividades origen.",
    "Conservar incidente historico de JSON no parseable hasta cierre verificado.",
    "No sobrescribir reglas locales mas especificas con reglas institucionales."
  ],
  "open_questions": [
    "Supuesto: persiste deuda de placeholders corruptos en README y programa; confirmar correccion.",
    "Definir formato uniforme de cita juridica para norma, jurisprudencia y doctrina.",
    "Confirmar checklist minimo por tipo de producto: reporte, presentacion, visual.",
    "Confirmar si el incidente de salida no JSON parseable ya quedo resuelto en este ciclo.",
    "Confirmar consignas reales por actividad para ajustar profundidad argumentativa."
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
        "Entrada canonica por carpeta de materia.",
        "Trazabilidad de herencia entre ciclos."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 6, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Derecho de la contratacion internacional."
      ]
    },
    "essence": [
      "Problema juridico como detonante.",
      "Marco conceptual y normativo verificable.",
      "Analisis propio con postura academica.",
      "Conclusion juridica aplicable.",
      "Normalizacion estructurada antes de propagar."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos solidos y verificables.",
      "Asegurar consistencia institucional UnADM en toda entrega.",
      "Preservar memoria editorial util sin perdida por recorte."
    ],
    "style_markers": [
      "Supuestos explicitos cuando falten datos.",
      "Separacion clara entre descripcion y argumentacion propia.",
      "Cierre con criterio juridico transferible.",
      "Reglas accionables y auditables."
    ],
    "argumentative_patterns": [
      "Problema -> marco normativo/doctrinal -> evidencia -> analisis -> conclusion.",
      "Afirmacion juridica -> cita verificable -> interpretacion propia.",
      "Consigna local -> producto alineado -> validacion final de coherencia."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico",
        "Marco normativo/doctrinal",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica",
        "Normalizacion estructurada",
        "JSON parseable",
        "Compresion lossless por deduplicacion",
        "Trazabilidad de herencia",
        "Bibliografia local canonica"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La identidad exige citas verificables y formato consistente."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El analisis nace de una pregunta juridica concreta."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusion juridica",
          "kind": "supports",
          "justification": "La conclusion valida depende de fundamento normativo o doctrinal."
        },
        {
          "source": "JSON parseable",
          "target": "Normalizacion estructurada",
          "kind": "depends_on",
          "justification": "Sin parseo valido no hay propagacion confiable."
        },
        {
          "source": "Compresion lossless por deduplicacion",
          "target": "Trazabilidad de herencia",
          "kind": "supports",
          "justification": "Permite conservar reglas utiles sin recorte destructivo."
        }
      ],
      "evidence": [
        "README de materia con identidad UnADM y ubicacion curricular.",
        "Programa analitico con proposito y ejes transferibles.",
        "Bib local existente como repositorio canonico.",
        "Registro historico de incidentes por salida no JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 12: se refuerza transferencia transversal por abstracciones estables.",
      "Ciclo 12: se preservan gates de JSON y normalizacion como bloqueo duro.",
      "Ciclo 12: se evita importar contenido tematico especifico de Filosofia del Derecho no aplicable al destino.",
      "Ciclo 12: se mantiene deuda tecnica de placeholders como asunto abierto, no como regla cerrada."
    ]
  }
}