{
  "summary": [
    "Sincronizacion transversal aplicada desde actividad de Filosofia del Derecho hacia materia de Antropologia con estrategia conservadora.",
    "Se preservan reglas utiles previas y se consolida por union-dedupe sin recorte semantico.",
    "Se transfieren solo abstracciones estables: identidad UnADM, estructura reusable, gates de calidad y trazabilidad de fuentes.",
    "Se evita trasladar contenido tematico exclusivo de Filosofia del Derecho al destino.",
    "Se refuerza normalizacion obligatoria cuando existan salidas no JSON parseables.",
    "Se mantiene alerta institucional por fuentes heredadas no verificadas como provisionales."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener contexto curricular local del destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar como provisional toda fuente heredada no verificada.",
    "No trasladar metadatos curriculares de Filosofia del Derecho al nodo de Antropologia."
  ],
  "structure_rules": [
    "Iniciar cada producto con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o teorico, analisis propio y cierre.",
    "Alinear el artefacto al producto solicitado en la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias canonicas de estructura.",
    "Resolver placeholders en rutas y nombres antes de compilar o citar."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion.",
    "Evitar entregas solo descriptivas.",
    "Mantener conclusion transferible a la practica juridica cuando la consigna lo requiera.",
    "No asumir que fuentes de otras semanas o materias aplican a la actividad actual."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa del esquema antes de reutilizar.",
    "Normalizar manualmente respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregado y consigna local.",
    "No promover reglas provisionales a definitivas sin validacion disciplinar."
  ],
  "latex_rules": [
    "Mantener plantilla .tex local como base editorial.",
    "Usar codificacion en español y acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir rutas truncadas o caracteres anómalos antes de compilar.",
    "Resolver tokens dinamicos tipo $(@{...}.Slug) en README, programa y nombres de archivo."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras verificables y consultables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes especificas de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, año y fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No citar claves ausentes del .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y parseables.",
    "Compartir solo abstracciones editoriales estables en nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferencia de redaccion literal o contenido tematico de origen.",
    "Mantener compresion lossless por deduplicacion en cada ciclo.",
    "Registrar incidencias de parseo como alerta transversal reutilizable.",
    "Preservar reglas utiles previas sin regresion en consolidaciones futuras."
  ],
  "open_questions": [
    "Supuesto: falta consigna puntual de actividades de Antropologia para afinar profundidad de cierre juridico.",
    "Confirmar si la conclusion juridica es obligatoria en todas las actividades de la materia destino.",
    "Confirmar estandar formal de citacion institucional unico para la licenciatura.",
    "Confirmar si LDE-S4B2 es clave oficial o convencion local.",
    "Confirmar si el nombre definitivo del .bib se mantiene literal o deriva de plantilla dinamica."
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
        "Entrada canonica por carpeta de materia."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 4, bloque 2, obligatoria, 8 creditos.",
        "Asignatura destino: Antropologia de la cultura en Mexico."
      ]
    },
    "essence": [
      "Problema",
      "Conceptos",
      "Evidencia",
      "Analisis propio",
      "Conclusion transferible",
      "Normalizacion estructurada previa a propagacion"
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables academicos verificables.",
      "Sostener consistencia editorial institucional entre materias.",
      "Asegurar calidad formal y argumentativa con control de trazabilidad."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> respaldo verificable -> interpretacion propia.",
      "Pregunta guia -> desarrollo coherente -> cierre consistente."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad academica",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion transferible",
        "Validacion JSON parseable",
        "Normalizacion estructurada",
        "Propagacion conservadora"
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
          "justification": "La identidad institucional exige trazabilidad y rigor."
        },
        {
          "source": "Validacion JSON parseable",
          "target": "Normalizacion estructurada",
          "kind": "depends_on",
          "justification": "Sin parseo valido no hay reutilizacion segura."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura se legitima con respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "El cierre profesional deriva del razonamiento, no del resumen."
        },
        {
          "source": "Propagacion conservadora",
          "target": "Identidad UnADM",
          "kind": "supports",
          "justification": "Preserva reglas estables sin contaminar con especificidades de otra materia."
        }
      ],
      "evidence": [
        "README destino: identidad UnADM y pauta editorial.",
        "Programa analitico destino: ejes problema, conceptos, producto, analisis y cierre.",
        ".bib destino: entradas institucionales verificables.",
        "Memoria origen: regla de bloqueo por no JSON parseable y normalizacion previa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 50: consolidada transferencia transversal de abstracciones estables.",
      "Ciclo 50: deduplicadas reglas repetidas sin perdida funcional.",
      "Ciclo 50: reforzados gates de parseo JSON, supuestos y trazabilidad bibliografica.",
      "Ciclo 50: retenida separacion entre identidad institucional y contenido tematico local."
    ]
  }
}