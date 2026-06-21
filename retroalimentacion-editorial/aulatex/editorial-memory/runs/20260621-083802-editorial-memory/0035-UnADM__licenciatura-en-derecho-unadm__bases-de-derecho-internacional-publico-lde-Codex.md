{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre actividad origen y materia destino.",
    "Se preservan reglas utiles previas del destino sin eliminaciones.",
    "Se refuerzan abstracciones estables: identidad UnADM, estructura argumentativa y gates de calidad.",
    "Se evita transferir contenido tematico especifico de Filosofia del Derecho al destino.",
    "Se mantiene normalizacion estructurada obligatoria antes de propagacion recursiva.",
    "Se registra incidencia local verificable: tokens sin expandir y corte de tabular en plantilla de reporte."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local: Bases de derecho internacional publico.",
    "Usar contexto curricular verificado del destino: semestre 4, bloque 1, obligatoria, 8 creditos.",
    "No mezclar metadatos curriculares del origen con el destino.",
    "Usar carpeta de materia como entrada canonica.",
    "Tratar Codex/GPT-Pro como procedencia provisional, no como identidad del entregable.",
    "Marcar como supuesto todo dato no visible en consigna local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear la salida al producto solicitado en la planeacion semanal.",
    "Distinguir reporte, presentacion y producto visual segun consigna.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Conservar separacion entre README, programa analitico, .bib y plantillas .tex."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, normas, argumentos y criterio propio.",
    "No extrapolar fuentes de semanas no confirmadas por consigna.",
    "Marcar faltantes de consigna o evidencia como pendientes.",
    "Mantener trazabilidad entre consigna, desarrollo y entregable final."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna vigente.",
    "Validar sintaxis LaTeX y cierre de entornos antes de compilar."
  ],
  "latex_rules": [
    "Reutilizar plantilla .tex local de la materia como base.",
    "Mantener compatibilidad con article, spanish, letterpaper y oneside.",
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir corte de entorno tabular detectado en reporte-bases-de-derecho-internacional-publico.tex [supuesto: archivo sigue incompleto hasta verificacion local]."
  ],
  "bibliography_rules": [
    "Registrar fuentes de actividad en bases-de-derecho-internacional-publico.bib.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Validar que toda clave citada exista en el .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas y deduplicadas.",
    "Aplicar compresion lossless por union-dedupe sin recorte semantico.",
    "No propagar supuestos como reglas definitivas.",
    "Priorizar transferencia de identidad, estructura reusable, quality gates y grafo conceptual.",
    "Mantener incidencias historicas de parseo como alertas de control.",
    "Si falta contexto local en subnodos, crear cerebro editorial minimo y abrir preguntas."
  ],
  "open_questions": [
    "Confirmar criterio editorial final sobre uso de publico/publico con acento en nombres visibles.",
    "Confirmar reparacion completa de tokens $(@{...}.Slug) en README y programa analitico.",
    "Confirmar cierre correcto del entorno tabular del reporte base.",
    "Confirmar rubrica de evaluacion por actividad para ajustar profundidad argumentativa.",
    "Confirmar si existe formato minimo institucional para conclusion juridica en esta materia."
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
        "Normalizacion estructurada obligatoria antes de propagacion."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Destino verificado: semestre 4, bloque 1, obligatoria, 8 creditos.",
        "No mezclar contexto curricular de nodos origen."
      ]
    },
    "essence": [
      "Consigna valida la forma del entregable.",
      "Problema y conceptos orientan el desarrollo.",
      "Evidencia verificable sostiene el analisis propio.",
      "La conclusion debe ser juridicamente transferible.",
      "La propagacion segura depende de estructura parseable."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos juridicamente solidos.",
      "Sostener consistencia editorial transversal en toda la materia.",
      "Evitar regresiones de calidad en ciclos recursivos."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales sin redundancia.",
      "Supuestos siempre etiquetados.",
      "Cierre con criterio juridico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> norma/doctrina -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> posicion propia.",
      "Consigna -> desarrollo alineado -> verificacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Consigna de actividad",
        "Estructura argumentativa juridica",
        "Evidencia verificable",
        "Conclusion juridica transferible",
        "Normalizacion JSON",
        "Consistencia cita-bibliografia",
        "Control de supuestos"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Consigna de actividad",
          "target": "Estructura argumentativa juridica",
          "kind": "depends_on",
          "justification": "El producto define forma, secciones y alcance."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "Sin respaldo documental la conclusion pierde validez academica."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Solo memoria parseable puede transferirse sin riesgo."
        },
        {
          "source": "Consistencia cita-bibliografia",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita citas huerfanas y referencias inventadas."
        },
        {
          "source": "Control de supuestos",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Separa hechos verificados de inferencias."
        }
      ],
      "evidence": [
        "README destino: identidad, estructura y ubicacion curricular.",
        "Programa analitico destino: proposito y ejes de trabajo.",
        "Archivo .bib local: claves institucionales base existentes.",
        "Plantilla de reporte: incidencia de tabular incompleto [supuesto pendiente de verificacion final].",
        "Origen actividad: regla transversal de normalizacion y ejes argumentativos reutilizables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 35: deduplicacion completa de reglas repetidas.",
      "Ciclo 35: transferencia solo de abstracciones estables entre nodos no equivalentes.",
      "Ciclo 35: refuerzo de gates de parseo JSON y consistencia cita-bibliografia.",
      "Ciclo 35: preservacion de identidad local de la materia destino.",
      "Ciclo 35: apertura de vacios locales sin inventar fuentes ni consignas."
    ]
  }
}