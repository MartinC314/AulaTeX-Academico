{
  "summary": [
    "Se consolida memoria lateral de Actividad 4 con deduplicacion lossless y sin recorte util.",
    "Se preserva identidad UnADM, contexto curricular y pauta editorial comun de la asignatura.",
    "Se refuerza gate obligatorio de JSON parseable por antecedentes de salidas no estructuradas.",
    "Se transfieren patrones reutilizables de estructura, calidad, LaTeX y bibliografia sin copiar conclusiones de Actividad 1.",
    "Supuesto: la consigna especifica de Actividad 4 no esta visible y requiere confirmacion local."
  ],
  "identity_rules": [
    "Mantener tono formal academico y precision juridica.",
    "Alinear toda entrega a UnADM, Licenciatura en Derecho y Filosofia del Derecho.",
    "Usar la carpeta de asignatura como entrada canonica documental.",
    "Conservar integridad academica con citas verificables.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "Sostener ubicacion curricular: semestre 1, bloque 2, obligatoria, 8 creditos."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato solicitado en la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Separar hechos, conceptos, argumentos y postura personal."
  ],
  "activity_rules": [
    "Incluir problema, conceptos, evidencia y analisis propio en secuencia clara.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Confirmar producto exacto de Actividad 4 antes de fijar plantilla final.",
    "No trasladar bibliografia exclusiva de un hermano sin verificar pertinencia local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar aguas abajo.",
    "Normalizar respuestas no estructuradas heredadas antes de propagar.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre entrega y consigna local de Actividad 4."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en espanol en .tex y .bib.",
    "Citar solo claves existentes en el .bib activo.",
    "No renombrar claves BibTeX usadas en documentos activos sin migracion controlada.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Verificar nombres reales de archivos cuando README tenga tokens sin resolver.",
    "Resolver o sustituir rutas con plantilla tipo $(@{...}.Slug) antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y juridicas verificables.",
    "Registrar fuentes especificas de cada actividad en el .bib de la asignatura.",
    "No inventar referencias ni metadatos faltantes.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "No asumir que filosofia-del-derecho-clean.bib aplica a Actividad 4 sin confirmacion.",
    "Marcar entradas incompletas como pendientes de verificacion."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales y verificadas.",
    "Preservar reglas utiles previas y evitar regresiones.",
    "Aplicar union-dedupe semantica para no duplicar variantes equivalentes.",
    "Cuando falte consigna local, transferir estructura base y dejar preguntas abiertas.",
    "Mantener bandera de normalizacion manual en ciclos con antecedentes no parseables."
  ],
  "open_questions": [
    "Confirmar consigna textual de Actividad 4.",
    "Confirmar tipo de producto requerido: reporte, presentacion u otro.",
    "Confirmar rubrica de evaluacion y extension esperada.",
    "Confirmar nombre canonico final del .bib cuando el slug del README esta sin resolver.",
    "Confirmar si la bibliografia de interpretacion juridica (Semana 7) es pertinente para Actividad 4."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro.",
        "Juridicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con trazabilidad de fuentes.",
        "Entrada canonica en carpeta de asignatura.",
        "Normalizacion estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura Filosofia del Derecho.",
        "Semestre 1, bloque 2.",
        "Obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico.",
      "Mantener coherencia entre identidad institucional, evidencia y argumentacion."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Cita explicita en afirmaciones sustantivas.",
      "Supuestos marcados cuando faltan datos locales."
    ],
    "argumentative_patterns": [
      "Plantear problema.",
      "Delimitar conceptos y norma.",
      "Contrastar evidencia.",
      "Fijar postura propia.",
      "Cerrar con conclusion aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON estricta",
        "Integridad academica verificable",
        "Ejes problema-conceptos-evidencia-analisis-conclusion"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "README.md de la asignatura",
        "programa-analitico-filosofia-del-derecho.md"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica verificable",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y formato academico."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Validacion JSON estricta",
          "kind": "depends_on",
          "justification": "La propagacion segura requiere salida parseable y estructura minima."
        },
        {
          "source": "Ejes problema-conceptos-evidencia-analisis-conclusion",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "El cierre deriva del desarrollo argumentativo completo."
        }
      ],
      "evidence": [
        "README: pauta editorial y entrada canonica.",
        "Programa analitico: ejes de trabajo y proposito de realizacion.",
        "Historial: incidentes de salida no parseable en ciclos previos."
      ]
    },
    "reinforcement_log": [
      "Ciclo 10: deduplicacion semantica aplicada a reglas repetidas.",
      "Ciclo 10: se conserva gate JSON y normalizacion como regla dura.",
      "Ciclo 10: se refuerza transferencia lateral solo de patrones reutilizables.",
      "Ciclo 10: se mantiene separacion entre bibliografia base y especifica por actividad."
    ]
  }
}