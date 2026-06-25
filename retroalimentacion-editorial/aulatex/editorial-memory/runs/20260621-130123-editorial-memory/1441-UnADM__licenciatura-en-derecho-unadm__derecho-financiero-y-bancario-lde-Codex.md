{
  "summary": [
    "Se consolida sincronizacion transversal desde actividad de Filosofia del Derecho hacia materia de Derecho financiero y bancario sin regresion.",
    "Se preservan reglas institucionales UnADM, normalizacion estructurada y compresion lossless por deduplicacion semantica.",
    "Se refuerza nucleo reusable: problema, conceptos o normas, evidencia, analisis propio y conclusion juridica transferible.",
    "Se mantiene estado provisional de datos no confirmados con marca explicita de supuesto.",
    "Se confirma contexto local de destino: semestre 3, bloque 2, obligatoria, 8 creditos y entrada canonica por carpeta de materia."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar Licenciatura en Derecho como programa academico del destino.",
    "Usar datos curriculares verificados del destino: semestre 3, bloque 2, obligatoria, 8 creditos.",
    "Marcar como supuesto cualquier dato no visible o no confirmado en consigna local.",
    "Tratar fuentes heredadas de motor como provisionales hasta verificacion local.",
    "Conservar autoria y matricula locales del .tex mientras no exista instruccion oficial en contrario."
  ],
  "structure_rules": [
    "Usar carpeta de materia como punto de entrada canonico.",
    "Abrir cada entrega con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar desarrollo en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Mantener coherencia entre README, programa analitico, .tex y .bib."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir fuentes o consignas de semanas distintas sin confirmacion.",
    "Separar descripcion conceptual de analisis propio.",
    "Ajustar profundidad segun rubrica local cuando exista; si no existe, marcar supuesto."
  ],
  "quality_gates": [
    "Bloquear propagacion si salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar trazabilidad de cada regla a contexto local o memoria heredada.",
    "Bloquear guardado si hay campos obligatorios vacios sin marca de supuesto.",
    "Validar deduplicacion semantica y no regresion de reglas utiles.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Mantener configuracion base de documento en espanol salvo lineamiento contrario.",
    "Mantener macros de identidad academica sincronizadas con metadatos reales.",
    "Reemplazar titulos de plantilla por datos reales de actividad antes de entrega.",
    "Completar campos pendientes como figura docente con dato real o etiqueta [Supuesto].",
    "Resolver tokens de plantilla sin expandir en README, programa y referencias de archivo.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Usar derecho-financiero-y-bancario.bib como archivo canonico de la materia.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Agregar entradas BibTeX solo con fuente consultable.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Incluir fecha de consulta en fuentes web.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas abstractas estables entre nodos no equivalentes.",
    "Priorizar transferencia de identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferir redaccion literal o contenidos tematicos exclusivos de Filosofia del Derecho.",
    "Aplicar estrategia progresiva y conservadora: agregar mejoras verificables sin borrar reglas validas.",
    "Si aparece salida no estructurada de ciclos previos, activar normalizacion manual contingente."
  ],
  "open_questions": [
    "Confirmar nombre real de figura docente en portada. [Supuesto]",
    "Confirmar formato obligatorio de citacion para la materia. [Supuesto]",
    "Confirmar si localizacion institucional de portada debe mantenerse. [Supuesto]",
    "Confirmar planeacion semanal vigente antes de generar actividades especificas. [Supuesto]"
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Sobrio, verificable y orientado a practica profesional."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Trazabilidad documental entre README, programa, .tex y .bib.",
        "No regresion de reglas utiles previas."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho financiero y bancario.",
        "Semestre 3, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable.",
      "Analisis juridico propio.",
      "Conclusion transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico y utilidad profesional.",
      "Sostener coherencia editorial persistente en toda la suite LaTeX."
    ],
    "style_markers": [
      "Frases directas y accionables.",
      "Supuestos explicitamente marcados.",
      "Consistencia entre estructura, citas y cierre argumentativo."
    ],
    "argumentative_patterns": [
      "Problema inicial breve -> objetivo puntual -> marco conceptual/normativo -> analisis propio -> conclusion aplicable.",
      "Toda conclusion deriva de evidencia citada."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Evidencia verificable",
        "Analisis juridico propio",
        "Conclusion transferible",
        "No regresion editorial"
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
          "justification": "Sin JSON parseable no hay transferencia segura."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion profesional requiere respaldo comprobable."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La identidad institucional exige trazabilidad y cita valida."
        },
        {
          "source": "Problema juridico delimitado",
          "target": "Analisis juridico propio",
          "kind": "develops",
          "justification": "El problema define el eje del razonamiento."
        }
      ],
      "evidence": [
        "README de materia: ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y ejes de trabajo.",
        "derecho-financiero-y-bancario.bib: base institucional verificable.",
        "Regla persistente: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 9: deduplicacion semantica completada sin eliminar reglas utiles.",
      "Ciclo 9: transferidas solo abstracciones estables desde nodo transversal no equivalente.",
      "Ciclo 9: reforzados quality gates de parseo, trazabilidad y supuestos.",
      "Ciclo 9: mantenida compatibilidad con estrategia progresiva y conservadora."
    ]
  }
}