{
  "summary": [
    "Se consolida sincronizacion transversal desde actividad de Filosofia del Derecho hacia materia de Antropologia sin mover contenido tematico especifico.",
    "Se preservan reglas utiles previas y se aplica deduplicacion lossless sin recorte.",
    "Se refuerzan identidad UnADM, estructura reusable, control de supuestos y validacion JSON como gate duro.",
    "Se mantiene alerta institucional por salidas no parseables heredadas como antecedente de riesgo.",
    "Se confirma contexto local de destino: semestre 4, bloque 2, obligatoria, 8 creditos [verificado en README]."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Usar nombre canonico de materia: Antropologia de la cultura en Mexico.",
    "Conservar ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en la consigna activa.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No trasladar metadatos curriculares de Filosofia del Derecho al destino."
  ],
  "structure_rules": [
    "Iniciar cada entrega con objetivo puntual y encuadre del problema juridico o social.",
    "Organizar en secciones: conceptos clave, marco normativo o teorico, analisis propio y cierre.",
    "Alinear el artefacto al producto solicitado por la planeacion semanal.",
    "Separar artefactos: reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias canonicas de estructura.",
    "Resolver placeholders y tokens dinamicos a nombres literales antes de compilar."
  ],
  "activity_rules": [
    "Sustentar afirmaciones relevantes con fuente verificable y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar solo descripcion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion transferible a practica juridica.",
    "En Antropologia, tender puente explicito entre analisis cultural y encuadre juridico."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Exigir esquema minimo completo antes de reutilizar memoria.",
    "Normalizar manualmente cualquier salida no estructurada antes de propagar.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre metadatos del documento y contexto curricular local.",
    "No promover reglas provisionales a definitivas sin validacion disciplinar."
  ],
  "latex_rules": [
    "Mantener plantilla .tex local como base editorial.",
    "Usar configuracion de espanol coherente y acentos correctos en .tex y .bib.",
    "Mantener clase article, letterpaper y oneside salvo instruccion formal distinta.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion.",
    "Compilar sin errores criticos, sin referencias rotas y sin tokens sin expandir en rutas."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias consultables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes especificas por actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Mantener trazabilidad de archivos locales cuando se cite assets-unadm."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas estables y abstractas entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferencia literal de redaccion o temas exclusivos de Filosofia del Derecho.",
    "Conservar union-dedupe lossless y politica sin regresion en cada ciclo.",
    "Registrar incidencias de parseo como alertas transversales reutilizables."
  ],
  "open_questions": [
    "[supuesto] Confirmar si coursecode LDE-S4B2 es oficial institucional o clave local.",
    "Confirmar rubrica y formato obligatorio por actividad en Antropologia.",
    "Confirmar estandar unico de citas para la licenciatura (APA u otro).",
    "Confirmar si toda actividad de Antropologia exige conclusion juridica explicita o solo cuando aplique.",
    "Confirmar resolucion definitiva de placeholders detectados en README y programa analitico."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con trazabilidad de fuentes.",
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 4, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Antropologia de la cultura en Mexico."
      ]
    },
    "essence": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Coherencia argumentativa con postura propia.",
      "Transferencia profesional del cierre.",
      "Control estricto de supuestos y verificabilidad."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables claros, verificables y utiles para formacion juridica.",
      "Asegurar continuidad editorial entre actividades y materias sin contaminar contexto local."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Citas verificables y consistentes con .bib.",
      "Supuestos etiquetados de forma visible."
    ],
    "argumentative_patterns": [
      "Afirmacion relevante -> evidencia verificable -> interpretacion propia.",
      "Concepto cultural -> puente juridico -> implicacion profesional.",
      "Pregunta guia -> desarrollo coherente -> conclusion util."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Validacion JSON parseable",
        "Normalizacion estructurada",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Puente antropologico-juridico"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Validacion JSON parseable",
          "target": "Normalizacion estructurada",
          "kind": "depends_on",
          "justification": "Sin parseo valido no hay memoria reusable."
        },
        {
          "source": "Integridad academica",
          "target": "Evidencia verificable",
          "kind": "depends_on",
          "justification": "La integridad requiere respaldo trazable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura gana solidez con fuentes comprobables."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "El cierre profesional deriva del razonamiento argumentado."
        },
        {
          "source": "Puente antropologico-juridico",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "Conecta hallazgos culturales con utilidad juridica."
        }
      ],
      "evidence": [
        "README local confirma identidad UnADM y ubicacion curricular.",
        "Programa analitico local fija ejes problema, conceptos, producto, analisis y cierre.",
        "Bib local contiene bases institucionales verificables.",
        "Memoria origen aporta regla estable de JSON parseable y normalizacion previa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 40: se transfirieron solo abstracciones editoriales estables desde actividad origen.",
      "Ciclo 40: se preservaron gates de parseo JSON y normalizacion como reglas duras.",
      "Ciclo 40: se evito transferir citas y contenidos tematicos exclusivos de Filosofia del Derecho.",
      "Ciclo 40: se reforzo resolucion de placeholders en README/programa/.tex/.bib.",
      "Ciclo 40: consolidacion aplicada con union-dedupe lossless y sin regresion."
    ]
  }
}