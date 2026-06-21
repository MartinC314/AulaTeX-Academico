{
  "summary": [
    "Sincronizacion transversal consolidada con union-dedupe lossless y sin regresion.",
    "Se preservan reglas institucionales UnADM, estructura canonica y gates de parseo JSON.",
    "Se incorporan abstracciones estables del origen: objetivo puntual, evidencia verificable, postura propia y coherencia argumentativa.",
    "Se evita transferir contenido tematico exclusivo de Filosofia del Derecho al nodo de Antropologia.",
    "Se refuerza resolucion de placeholders y tokens dinamicos en README, programa y rutas .bib/.tex."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar toda fuente heredada no verificada como provisional.",
    "No trasladar metadatos curriculares de otra materia al destino."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco teorico/normativo, analisis propio y cierre.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias canonicass de estructura.",
    "Resolver nombres dinamicos a rutas literales antes de compilar."
  ],
  "activity_rules": [
    "Sustentar afirmaciones relevantes con fuente verificable y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Evitar afirmaciones juridicas sin puente argumentativo cultural cuando aplique.",
    "Cerrar con conclusion transferible a practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa del esquema antes de reutilizar.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar consistencia entre metadatos del documento y metadata curricular local.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No promover reglas provisionales a definitivas sin verificacion local."
  ],
  "latex_rules": [
    "Mantener plantilla base .tex de la materia como referencia inicial.",
    "Conservar configuracion en espanol y acentos correctos en .tex y .bib.",
    "Mantener clase article, letterpaper y oneside salvo instruccion valida en contrario.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir rutas truncadas o caracteres anomalo antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README, programa y archivos."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes especificas por actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Mantener trazabilidad de procedencia en notas cuando sea archivo local.",
    "No asumir reutilizacion automatica de .bib de otra asignatura."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar propagar redaccion literal o contenidos tematicos locales de otra materia.",
    "Conservar alertas historicas de parseo como control institucional transversal.",
    "Aplicar estrategia conservadora: agregar mejoras verificables sin eliminar reglas utiles previas."
  ],
  "open_questions": [
    "Supuesto: falta consigna puntual de actividades de la materia destino para ajustar profundidad por evidencia.",
    "Confirmar si existe norma institucional unica de estilo de cita para toda la licenciatura.",
    "Confirmar si LDE-S4B2 es clave oficial definitiva o clave operativa local.",
    "Confirmar si toda actividad de Antropologia exige cierre juridico explicito o depende de rubrica."
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
      "Problema, conceptos, evidencia, analisis propio y conclusion transferible.",
      "Normalizacion estructurada previa a toda propagacion.",
      "Compresion lossless por union-dedupe sin recorte."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros, verificables y utiles para la practica profesional.",
      "Sostener un marco editorial estable transversal entre materias de Derecho UnADM."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados cuando falte dato verificable.",
      "Cierre con valor profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente verificable -> interpretacion propia.",
      "Coherencia vertical entre pregunta guia, desarrollo y cierre."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON parseable",
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
          "source": "Validacion JSON parseable",
          "target": "Normalizacion estructurada",
          "kind": "depends_on",
          "justification": "Sin parseo valido no hay reutilizacion confiable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura personal requiere respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion util deriva del razonamiento sustentado."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Propagacion transversal conservadora",
          "kind": "supports",
          "justification": "Define limites y continuidad editorial entre nodos."
        }
      ],
      "evidence": [
        "README local: identidad UnADM y pauta editorial canonica.",
        "Programa analitico local: ejes de trabajo y proposito de realizacion.",
        "Bib local: unadmSitioWeb y unadmMallaDerecho2024 verificables.",
        "Historial institucional: alertas por salidas no JSON parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 78: se consolidan abstracciones estables de actividad origen sin contaminar contenido tematico.",
      "Ciclo 78: se refuerzan gates JSON y normalizacion como precondicion de propagacion recursiva.",
      "Ciclo 78: se mantiene regla de supuestos marcados y fuentes provisionales no verificadas."
    ]
  }
}