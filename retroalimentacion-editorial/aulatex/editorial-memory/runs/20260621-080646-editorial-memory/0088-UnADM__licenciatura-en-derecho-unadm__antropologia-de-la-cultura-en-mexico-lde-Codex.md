{
  "summary": [
    "Sincronizacion transversal conservadora aplicada desde actividad de Filosofia del Derecho hacia materia de Antropologia.",
    "Se preservan reglas institucionales UnADM y se deduplican sin perdida.",
    "Se transfieren solo abstracciones estables: objetivo, evidencia, analisis propio, coherencia y cierre.",
    "Se evita transferir contenido tematico exclusivo de Filosofia del Derecho.",
    "Se refuerza normalizacion estructurada y bloqueo por JSON no parseable.",
    "Se mantiene alerta de fuentes heredadas no verificadas como provisionales.",
    "Se confirma contexto local del destino: semestre 4, bloque 2, obligatoria, 8 creditos [verificado en README]."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener materia destino: Antropologia de la cultura en Mexico.",
    "Conservar ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No trasladar metadatos curriculares de otra asignatura al destino."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco teorico/normativo, analisis propio y cierre.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Distinguir artefactos: reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias canonicas de estructura.",
    "Resolver placeholders y tokens dinamicos en nombres de archivo antes de uso."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Evitar extrapolar fuentes o instrucciones de semanas no confirmadas.",
    "Cerrar con conclusion transferible a practica profesional juridica."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Exigir estructura minima completa del esquema antes de reutilizar.",
    "Revisar y normalizar manualmente respuestas no estructuradas.",
    "Confirmar que toda afirmacion tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que metadatos del documento coincidan con la materia destino.",
    "No promover reglas provisionales a definitivas sin validacion disciplinar."
  ],
  "latex_rules": [
    "Mantener plantilla base .tex de la materia destino.",
    "Conservar configuracion de espanol y acentos correctos en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Mantener claves BibTeX estables para evitar rupturas.",
    "Corregir rutas truncadas o caracteres anomalos antes de compilar.",
    "Resolver tokens tipo $(@{...}.Slug) en README, programa y referencias."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes especificas de cada actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "No citar claves ausentes en .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y estables.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferencia literal de redaccion entre nodos no equivalentes.",
    "Mantener compresion lossless por union-dedupe sin regresion.",
    "Registrar incidencias de parseo como alerta transversal reutilizable.",
    "Si falta contexto local en un nodo, crear memoria minima y abrir preguntas."
  ],
  "open_questions": [
    "Confirmar rubrica especifica de evaluacion para actividades de la materia destino.",
    "Confirmar estandar unico de citas para la licenciatura [supuesto: APA u otro].",
    "Confirmar si la conclusion juridica es obligatoria en todas las actividades antropologicas.",
    "Confirmar si la clave LDE-S4B2 es oficial institucional o etiqueta local.",
    "Confirmar lineamientos de extension y tipo de producto por semana."
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
        "Asignatura: Antropologia de la cultura en Mexico."
      ]
    },
    "essence": [
      "Problema claro.",
      "Conceptos pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos utiles y verificables.",
      "Sostener coherencia metodologica entre actividades y materia.",
      "Garantizar calidad editorial sin perder identidad institucional."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados cuando falte evidencia.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente -> interpretacion propia.",
      "Consigna -> desarrollo -> verificacion de coherencia final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "JSON parseable",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Propagacion transversal conservadora"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "JSON parseable",
          "target": "Normalizacion estructurada",
          "kind": "depends_on",
          "justification": "Sin parseo valido no hay integracion confiable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura academica requiere respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion util deriva del razonamiento argumentado."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "La pauta institucional exige integridad academica."
        }
      ],
      "evidence": [
        "README de materia destino con identidad y ubicacion curricular.",
        "Programa analitico con ejes problema-conceptos-evidencia-analisis-cierre.",
        ".bib local con fuentes institucionales base.",
        "Regla heredada y vigente: bloquear si no hay JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 88: deduplicacion completa sin eliminar reglas utiles previas.",
      "Ciclo 88: se reforzo gate de parseo JSON como requisito de propagacion.",
      "Ciclo 88: se transfirieron patrones argumentativos estables, no contenido tematico de origen.",
      "Ciclo 88: se mantuvo estado provisional de fuentes heredadas no verificadas."
    ]
  }
}