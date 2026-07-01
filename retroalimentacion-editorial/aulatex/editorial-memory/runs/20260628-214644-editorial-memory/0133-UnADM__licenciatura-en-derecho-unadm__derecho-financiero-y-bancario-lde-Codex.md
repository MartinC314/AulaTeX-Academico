{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre actividad de origen y materia destino.",
    "Se preserva identidad UnADM, integridad academica, trazabilidad y compresion lossless por union-dedupe.",
    "Se refuerza flujo editorial reusable: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene regla critica: no propagar salidas no estructuradas sin normalizacion.",
    "Se conserva contexto local del destino: semestre 3, bloque 2, obligatoria, 8 creditos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar contexto curricular local verificado del destino.",
    "Mantener Licenciatura en Derecho como programa academico.",
    "Marcar como supuesto todo dato no confirmado en consigna o documentos locales.",
    "Tratar fuentes heredadas de motor como provisionales hasta verificacion local.",
    "Usar carpeta de materia como entrada canonica."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear producto al tipo solicitado por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Mantener coherencia entre README, programa analitico, .tex y .bib."
  ],
  "activity_rules": [
    "Exigir postura argumentada del estudiante, no solo descripcion.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar afirmaciones sin respaldo o sin marca de supuesto.",
    "Separar descripcion conceptual de analisis propio.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar memoria.",
    "Revisar y normalizar respuesta no estructurada antes de aplicar aguas abajo.",
    "Confirmar trazabilidad de cada regla a contexto local o memoria heredada.",
    "Validar deduplicacion semantica antes de guardar.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Mantener codificacion y acentos correctos en español en .tex y .bib.",
    "Mantener documentclass y macros institucionales salvo instruccion contraria.",
    "Reemplazar titulos de plantilla por datos reales de actividad antes de entrega.",
    "Completar campos incompletos como Figura docente con dato real o etiqueta de supuesto.",
    "Resolver tokens sin expandir en README y programa analitico.",
    "Usar derecho-financiero-y-bancario.bib como nombre canonico del .bib local.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias ni metadatos.",
    "Registrar fuentes especificas de actividad en el .bib de la materia.",
    "Conservar metadatos minimos: autor, titulo, año, fuente o URL.",
    "Incluir fecha de consulta en referencias web.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas estables e independientes de actividad puntual.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferencia de redaccion literal entre nodos no equivalentes.",
    "Aplicar estrategia progresiva y conservadora: agregar solo mejoras verificables.",
    "Mantener no regresion de reglas utiles previas."
  ],
  "open_questions": [
    "Confirmar formato de citacion obligatorio de la materia (supuesto: no definido).",
    "Confirmar figura docente y grupo para portada (supuesto).",
    "Confirmar si localizacion institucional en portada debe mantenerse.",
    "Confirmar planeacion semanal vigente antes de instanciar actividades.",
    "Confirmar si correccion de tokens en README/programa sera manual o automatica."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Sobrio y verificable."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Normalizacion estructurada antes de propagar.",
        "Integridad academica con citas verificables.",
        "Fuentes heredadas tratadas como provisionales."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Derecho financiero y bancario.",
        "Semestre 3, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Conceptos y normas pertinentes.",
      "Evidencia verificable.",
      "Analisis juridico propio.",
      "Conclusion transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con rigor juridico y utilidad profesional.",
      "Preservar un cerebro editorial estable, auditable y reusable entre actividades."
    ],
    "style_markers": [
      "Frases precisas y accionables.",
      "Separacion explicita entre descripcion y analisis.",
      "Uso visible de etiquetas de supuesto cuando falta dato.",
      "Cierre con postura juridica propia."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer marco conceptual y normativo.",
      "Evaluar evidencia.",
      "Sostener postura propia.",
      "Concluir con aplicacion practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Evidencia verificable",
        "Analisis juridico propio",
        "Conclusion transferible"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Normalizacion estructurada",
          "kind": "supports",
          "justification": "La identidad institucional exige salidas auditables y consistentes."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis juridico propio",
          "kind": "depends_on",
          "justification": "La argumentacion valida requiere respaldo comprobable."
        },
        {
          "source": "Analisis juridico propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion practica deriva del razonamiento y no del resumen."
        }
      ],
      "evidence": [
        "README de materia: pauta editorial y ubicacion curricular.",
        "Programa analitico: proposito y ejes de trabajo.",
        "Bib local: fuentes institucionales base.",
        "Memoria heredada: bloqueo a salida no JSON y normalizacion obligatoria."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: deduplicacion semantica aplicada sin recorte de reglas utiles.",
      "Ciclo 2: se transfiere solo abstraccion editorial estable desde nodo transversal.",
      "Ciclo 2: se preserva gate critico de JSON parseable y trazabilidad.",
      "Ciclo 2: se mantiene pendiente local todo dato no verificable bajo etiqueta de supuesto."
    ]
  }
}