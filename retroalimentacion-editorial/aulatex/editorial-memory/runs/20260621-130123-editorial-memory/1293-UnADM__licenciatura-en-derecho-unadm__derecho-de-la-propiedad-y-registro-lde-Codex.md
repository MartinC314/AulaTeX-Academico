{
  "summary": [
    "Se consolida sincronizacion transversal entre nodos no equivalentes con abstracciones estables.",
    "Se preserva identidad UnADM y ubicacion curricular local de la materia destino.",
    "Se refuerza regla critica: no propagar ni reutilizar salidas no JSON sin normalizacion.",
    "Se mantienen ejes editoriales transferibles: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se agrega control de tokens corruptos en README y programa analitico como gate operativo verificable."
  ],
  "identity_rules": [
    "Mantener identidad explicita UnADM en tono, portada y metadatos.",
    "Usar nombre exacto de materia: Derecho de la propiedad y registro.",
    "Conservar programa: Licenciatura en Derecho.",
    "Registrar ubicacion curricular verificada: semestre 7, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear cada entrega al producto pedido en la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Transformar planeacion en reporte o presentacion segun consigna."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Relacionar el desarrollo con propiedad y registro cuando aplique.",
    "No asumir fuentes de semanas posteriores sin validacion de consigna.",
    "Verificar que el producto final corresponda a la actividad solicitada."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar que no existan placeholders ni tokens sin resolver en archivos y metadatos."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener clase article con spanish, letterpaper y oneside salvo instruccion distinta.",
    "Completar metadatos academicos obligatorios antes de compilar.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico antes de automatizar rutas.",
    "Corregir placeholders visibles como Figura docente antes de entrega."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Usar archivo BibTeX local de la materia para fuentes especificas.",
    "No inventar referencias; usar solo obras consultables o locales existentes.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales validadas y no ambiguas.",
    "Compartir entre nodos no equivalentes solo abstracciones editoriales estables.",
    "Evitar transferir redaccion literal o datos hiperlocales no verificables.",
    "Preservar reglas utiles previas sin regresion mediante union y deduplicacion.",
    "Marcar supuestos durante transferencia transversal hasta confirmacion local."
  ],
  "open_questions": [
    "Confirmar rubrica formal de evaluacion por actividad en la materia destino.",
    "Confirmar estilo de citacion juridica requerido por figura docente.",
    "Confirmar nombre de figura docente para reemplazar placeholder.",
    "Supuesto: persisten tokens corruptos en README/programa; confirmar si ya fueron saneados en repositorio.",
    "Confirmar si cada actividad requiere reporte, presentacion u otro producto."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador en inferencias."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta de asignatura como entrada canonica.",
        "Normalizacion estructurada obligatoria antes de propagacion."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 7, bloque 1, obligatoria, 8 creditos.",
        "Materia: Derecho de la propiedad y registro.",
        "Codigo local: LDE-S7B1."
      ]
    },
    "essence": [
      "Problema juridico",
      "Marco conceptual y normativo",
      "Evidencia verificable",
      "Analisis propio",
      "Conclusion juridica transferible",
      "Trazabilidad tecnica y bibliografica"
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos solidos y verificables.",
      "Asegurar consistencia institucional y rigor juridico en cada entrega.",
      "Habilitar propagacion segura por estructura parseable y reglas estables."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Supuestos explicitamente marcados.",
      "Sin afirmaciones sin fuente.",
      "Sin placeholders al cierre."
    ],
    "argumentative_patterns": [
      "Del problema al marco conceptual.",
      "Del marco normativo a la evidencia.",
      "De la evidencia al analisis propio.",
      "Del analisis a una conclusion aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad academica",
        "Problema juridico",
        "Marco normativo o doctrinal",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion JSON",
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
          "justification": "La identidad institucional exige formato consistente y citas verificables."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis debe responder al problema planteado."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica requiere fundamento normativo."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Trazabilidad bibliografica",
          "kind": "supports",
          "justification": "La estructura valida permite verificar citas y reglas en propagacion."
        }
      ],
      "evidence": [
        "README de la materia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y ejes de trabajo.",
        "derecho-de-la-propiedad-y-registro.bib: claves institucionales existentes.",
        "Regla heredada estable: bloquear salidas no JSON parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 16: deduplicacion completa de reglas repetidas sin perdida semantica.",
      "Ciclo 16: transferencia transversal limitada a abstracciones estables.",
      "Ciclo 16: refuerzo de gates de parseo JSON y normalizacion previa.",
      "Ciclo 16: conservacion de ADN argumentativo comun entre materias de Derecho."
    ]
  }
}