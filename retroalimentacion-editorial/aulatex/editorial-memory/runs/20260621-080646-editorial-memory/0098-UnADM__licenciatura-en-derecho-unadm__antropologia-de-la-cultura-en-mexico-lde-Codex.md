{
  "summary": [
    "Sincronizacion transversal conservadora aplicada desde actividad de Filosofia del Derecho hacia materia de Antropologia.",
    "Se preservan reglas utiles previas y se elimina duplicidad por union-dedupe lossless.",
    "Se transfieren solo abstracciones estables: identidad UnADM, estructura reusable, calidad y trazabilidad.",
    "Se evita transferir contenido tematico exclusivo de Filosofia del Derecho al destino.",
    "Se mantiene alerta institucional por salidas no JSON parseable como riesgo operativo reutilizable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener contexto curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar toda fuente heredada no verificada como provisional hasta validacion local.",
    "No trasladar metadatos curriculares de otras materias al destino."
  ],
  "structure_rules": [
    "Iniciar cada entrega con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear el producto al entregable solicitado por la planeacion semanal.",
    "Distinguir artefactos: reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias de estructura editorial.",
    "Resolver placeholders de nombres de archivo antes de compilar o citar."
  ],
  "activity_rules": [
    "Sustentar afirmaciones relevantes con fuente verificable y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Cerrar con conclusion transferible a la practica juridica.",
    "Integrar conceptos antropologicos y juridicos con puente argumentativo explicito."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa del esquema antes de reutilizar.",
    "Normalizar manualmente respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Verificar consistencia entre citas en texto y archivo .bib.",
    "Comprobar correspondencia entre metadatos del documento y contexto curricular local.",
    "No promover reglas provisionales a definitivas sin validacion disciplinar."
  ],
  "latex_rules": [
    "Mantener plantilla .tex local como base de trabajo.",
    "Conservar configuracion de espanol y acentos correctos en .tex y .bib.",
    "Mantener clase y formato por defecto salvo justificacion academica.",
    "Actualizar documenttitle y documentsubtitle por actividad real.",
    "Compilar sin errores criticos, sin referencias rotas y sin rutas corruptas.",
    "Corregir tokens dinamicos sin expandir en README, programa y rutas de archivos."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias consultables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes especificas por actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Mantener trazabilidad de procedencia cuando se use archivo local o asset institucional."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y estables entre nodos no equivalentes.",
    "Propagar identidad, estructura reusable, quality gates y grafo conceptual; no redaccion literal.",
    "Conservar metodo union-dedupe sin regresion en ciclos siguientes.",
    "Registrar incidencias de parseo como alerta transversal reutilizable.",
    "Si falta contexto local en subnodos, crear cerebro minimo y abrir vacios como preguntas."
  ],
  "open_questions": [
    "Supuesto: confirmar si LDE-S4B2 es clave oficial o convencion local.",
    "Confirmar estandar unico de citacion para la licenciatura.",
    "Confirmar si toda actividad de la materia exige conclusion juridica explicita.",
    "Confirmar rubrica de evaluacion por actividad para calibrar profundidad argumentativa.",
    "Confirmar politica final sobre placeholders dinamicos en nombres de .bib."
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
        "Antropologia de la cultura en Mexico.",
        "Semestre 4, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema, conceptos, evidencia, analisis propio y conclusion transferible.",
      "Normalizacion estructurada antes de cualquier propagacion.",
      "Sincronizacion transversal con conservacion de identidad local."
    ],
    "reason_for_being": [
      "Guiar productos academicos verificables y argumentativos en formato UnADM.",
      "Convertir planeacion semanal en entregables consistentes y trazables."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados cuando falte evidencia local.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente verificable -> interpretacion propia.",
      "Pregunta guia -> desarrollo coherente -> cierre consistente."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Validacion JSON parseable",
        "Normalizacion estructurada",
        "Propagacion transversal conservadora"
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
          "justification": "Sin parseo valido no hay reutilizacion confiable."
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
          "justification": "El criterio personal se fortalece con fuentes."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion util surge del razonamiento argumentado."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Propagacion transversal conservadora",
          "kind": "supports",
          "justification": "La identidad fija limites de transferencia entre materias."
        }
      ],
      "evidence": [
        "README de materia destino con identidad UnADM y pauta editorial.",
        "Programa analitico con ejes problema-conceptos-producto-analisis-conclusion.",
        "Bib local con fuentes institucionales verificables.",
        "Memoria origen con regla estable de normalizacion y JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 98: deduplicacion completa sin eliminar reglas utiles previas.",
      "Ciclo 98: transferencia estable desde Filosofia del Derecho sin arrastre tematico especifico.",
      "Ciclo 98: reforzados quality gates de parseo JSON y trazabilidad bibliografica.",
      "Ciclo 98: mantenida alerta de fuentes heredadas provisionales."
    ]
  }
}