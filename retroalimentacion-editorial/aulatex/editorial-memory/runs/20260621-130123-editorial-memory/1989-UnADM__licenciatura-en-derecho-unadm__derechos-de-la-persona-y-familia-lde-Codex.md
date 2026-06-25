{
  "summary": [
    "Sincronizacion transversal consolidada sin arrastre tematico entre nodos no equivalentes.",
    "Se preserva nucleo editorial estable UnADM: problema, conceptos y normas, evidencia, analisis propio, conclusion juridica.",
    "Se mantiene regla critica: no propagar salidas no JSON parseable sin normalizacion previa.",
    "Se refuerza contexto local destino: semestre 3, bloque 1, obligatoria seriada, 8 creditos.",
    "Se confirma necesidad operativa de corregir placeholders de slug y rutas corruptas en README y programa analitico."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar nombre canonico de asignatura: Derechos de la persona y familia.",
    "Alinear productos a Licenciatura en Derecho, semestre 3, bloque 1, obligatoria seriada, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como [supuesto] todo dato no confirmado por consigna o documento local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No modificar datos de alumno o matricula sin verificacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el desarrollo al producto solicitado en la planeacion o consigna.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Mantener trazabilidad explicita entre consigna, desarrollo y conclusion."
  ],
  "activity_rules": [
    "Identificar consigna, rubrica y producto solicitado antes de redactar.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar resumen descriptivo puro.",
    "Evitar texto generico y vincular argumentos al problema juridico concreto.",
    "No asumir fuentes de semanas o materias distintas sin validacion de pertinencia.",
    "Registrar como pendiente toda ausencia de contexto de actividad."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de guardar o propagar.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Exigir respaldo verificable o marca [supuesto] en afirmaciones no confirmadas.",
    "Verificar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre consigna, rubrica y producto entregado.",
    "Corregir placeholders y rutas corruptas antes de compilacion o reutilizacion."
  ],
  "latex_rules": [
    "Usar plantilla local de la materia como base.",
    "Mantener espanol academico y terminologia juridica consistente.",
    "Conservar documentclass article, spanish, letterpaper y oneside salvo consigna distinta.",
    "Actualizar documentsubtitle al numero real de actividad.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Verificar nombres reales de archivos de reporte, presentacion y referencias antes de compilar."
  ],
  "bibliography_rules": [
    "Usar derechos-de-la-persona-y-familia.bib como archivo canonico local.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Registrar fuentes especificas de cada actividad en el .bib local.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas estables y abstractas entre nodos transversales.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferir redaccion literal o contenido tematico propio de otra asignatura.",
    "Aplicar compresion lossless por union y deduplicacion sin regresion.",
    "Si reaparece salida no estructurada, forzar normalizacion manual antes de propagar."
  ],
  "open_questions": [
    "Confirmar consignas y rubricas reales de actividades del destino.",
    "Confirmar vigencia de datos de alumno y figura docente en plantilla. [supuesto]",
    "Confirmar si coursecode LDE-S3B1 es obligatorio en todos los productos.",
    "Validar correccion definitiva de rutas corruptas en README (reporte/referencias).",
    "Validar sustitucion definitiva del placeholder dinamico del .bib en README y programa analitico."
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
        "Semestre 3, bloque 1, obligatoria seriada, 8 creditos.",
        "Asignatura: Derechos de la persona y familia."
      ]
    },
    "essence": [
      "Problematizar, fundamentar, analizar y concluir con utilidad juridica.",
      "Sostener cada afirmacion relevante con evidencia verificable.",
      "Conservar compatibilidad tecnica entre memoria, LaTeX y BibTeX."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos juridicos claros, sustentados y transferibles.",
      "Asegurar continuidad editorial institucional con control de calidad verificable."
    ],
    "style_markers": [
      "Frases directas y verificables.",
      "Separacion nitida entre marco conceptual y postura propia.",
      "Etiquetado explicito de [supuesto] cuando falte confirmacion documental."
    ],
    "argumentative_patterns": [
      "Iniciar con problema juridico concreto.",
      "Fundamentar con norma, doctrina o fuente institucional.",
      "Desarrollar analisis propio con criterio juridico.",
      "Cerrar con conclusion aplicable a practica profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Estructura argumentativa juridica",
        "Integridad de evidencia y citas",
        "Normalizacion JSON de memoria",
        "Consistencia tecnica LaTeX/BibTeX",
        "Problema-conceptos-evidencia-analisis-conclusion"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura argumentativa juridica",
          "kind": "supports",
          "justification": "Define tono, formato y criterio academico."
        },
        {
          "source": "Normalizacion JSON de memoria",
          "target": "Integridad de evidencia y citas",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay trazabilidad confiable."
        },
        {
          "source": "Consistencia tecnica LaTeX/BibTeX",
          "target": "Integridad de evidencia y citas",
          "kind": "supports",
          "justification": "Evita citas rotas y perdida de respaldo."
        },
        {
          "source": "Problema-conceptos-evidencia-analisis-conclusion",
          "target": "Estructura argumentativa juridica",
          "kind": "develops",
          "justification": "Es el patron reusable transversal entre actividades."
        }
      ],
      "evidence": [
        "README local del destino con ubicacion curricular y pauta editorial.",
        "Programa analitico local con ejes de trabajo.",
        "Archivo derechos-de-la-persona-y-familia.bib con fuentes institucionales base.",
        "Regla persistente: bloquear propagacion ante salida no JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 14: se transfieren solo abstracciones estables desde actividad origen a materia destino.",
      "Ciclo 14: se deduplican reglas repetidas y se preserva contenido util sin recorte.",
      "Ciclo 14: se refuerzan gates de parseo JSON, trazabilidad y control de supuestos.",
      "Ciclo 14: se mantiene separacion entre identidad editorial y contenido tematico de asignaturas distintas."
    ]
  }
}