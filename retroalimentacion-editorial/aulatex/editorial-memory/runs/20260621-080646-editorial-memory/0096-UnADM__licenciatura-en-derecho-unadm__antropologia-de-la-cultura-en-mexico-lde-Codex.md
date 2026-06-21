{
  "summary": [
    "Se consolida sincronizacion transversal desde actividad de Filosofia del Derecho hacia materia de Antropologia con estrategia conservadora.",
    "Se preservan reglas validas previas y se deduplican sin perdida.",
    "Se transfieren solo abstracciones estables: identidad UnADM, estructura reusable, gates de calidad y patron argumentativo.",
    "Se evita transferir contenido tematico exclusivo de Filosofia del Derecho al destino.",
    "Se refuerza normalizacion obligatoria de salidas no estructuradas antes de propagacion recursiva.",
    "Se mantiene alerta historica por salidas no JSON parseables (Codex y GPT-Pro) como riesgo de calidad."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener contexto curricular local del destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar toda fuente heredada no verificada como provisional hasta confirmacion local.",
    "No trasladar metadatos curriculares de otras materias al destino."
  ],
  "structure_rules": [
    "Iniciar cada producto con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco teorico/normativo, analisis propio y cierre.",
    "Alinear el formato final al entregable de la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias canonicas de estructura."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Evitar afirmaciones sin puente argumentativo entre cultura y derecho.",
    "Cerrar con conclusion transferible a la practica juridica cuando la consigna lo permita."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa del esquema antes de reutilizar.",
    "Normalizar manualmente respuestas no estructuradas antes de uso aguas abajo.",
    "Confirmar respaldo o marca de supuesto en toda afirmacion relevante.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregado y consigna local.",
    "No promover reglas provisionales a definitivas sin validacion disciplinar."
  ],
  "latex_rules": [
    "Usar configuracion en espanol coherente con plantilla local.",
    "Mantener clase y formato base salvo justificacion academica.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Mantener campos institucionales completos y consistentes.",
    "Corregir rutas truncadas o caracteres anomales antes de compilar.",
    "Resolver tokens dinamicos tipo $(@{...}.Slug) a nombres literales antes de citar archivos.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales pertinentes.",
    "Registrar fuentes especificas de cada actividad en el .bib local de la materia.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y estables.",
    "Transferir entre nodos no equivalentes solo abstracciones editoriales, no redaccion literal.",
    "Preservar union-dedupe lossless sin eliminar reglas utiles previas.",
    "Etiquetar incidencias de parseo como alertas reutilizables inter-materias.",
    "Mantener traza de supuestos para futura verificacion local."
  ],
  "open_questions": [
    "Supuesto: confirmar si la conclusion juridica es obligatoria en todas las actividades de antropologia.",
    "Supuesto: confirmar estandar de citacion institucional unico para la licenciatura.",
    "Confirmar si LDE-S4B2 es clave oficial o convencion local.",
    "Confirmar rubrica local para ajustar profundidad argumentativa por actividad.",
    "Confirmar si existen fuentes base obligatorias adicionales a malla y sitio UnADM."
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
        "Destino local: semestre 4, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Antropologia de la cultura en Mexico."
      ]
    },
    "essence": [
      "Problema, conceptos, evidencia, analisis propio y cierre.",
      "Normalizacion estructurada antes de propagacion.",
      "Compresion lossless por deduplicacion sin regresion.",
      "Transferencia transversal de patrones, no de contenido tematico."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y utiles.",
      "Sostener coherencia institucional entre materias con variacion disciplinar controlada.",
      "Garantizar calidad tecnica y argumentativa en LaTeX y bibliografia."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos siempre marcados.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente verificable -> interpretacion propia.",
      "Coherencia entre pregunta guia y respuesta final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Validacion JSON parseable",
        "Normalizacion estructurada",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion transferible",
        "Sincronizacion transversal conservadora"
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
          "justification": "Sin parseo valido no hay propagacion confiable."
        },
        {
          "source": "Integridad academica",
          "target": "Evidencia verificable",
          "kind": "depends_on",
          "justification": "La integridad exige respaldo trazable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura personal gana solidez con fuentes."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion util deriva del razonamiento argumentado."
        },
        {
          "source": "Sincronizacion transversal conservadora",
          "target": "Identidad institucional UnADM",
          "kind": "supports",
          "justification": "Permite coherencia editorial sin mezclar contenidos disciplinares."
        }
      ],
      "evidence": [
        "README local de materia con pauta editorial UnADM y ubicacion curricular.",
        "Programa analitico local con ejes de trabajo reutilizables.",
        "Archivo .bib local con entradas institucionales verificables.",
        "Historial de incidencias por salidas no JSON parseables en ciclos previos."
      ]
    },
    "reinforcement_log": [
      "Ciclo 96: se refuerza gate de JSON parseable como condicion dura.",
      "Ciclo 96: se consolidan ejes argumentativos transferibles desde origen.",
      "Ciclo 96: se bloquea transferencia de contenido tematico exclusivo de Filosofia del Derecho.",
      "Ciclo 96: se refuerza resolucion de placeholders en README/programa/.tex/.bib.",
      "Ciclo 96: se preservan reglas previas utiles sin eliminaciones."
    ]
  }
}