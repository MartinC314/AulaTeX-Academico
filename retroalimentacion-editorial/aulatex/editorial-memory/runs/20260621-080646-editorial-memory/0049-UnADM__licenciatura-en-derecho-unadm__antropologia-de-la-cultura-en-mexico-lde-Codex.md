{
  "summary": [
    "Sincronizacion transversal consolidada con union-dedupe lossless y sin regresion.",
    "Se preservan reglas estables de identidad UnADM, estructura canonica y calidad.",
    "Se transfieren solo abstracciones reutilizables desde actividad de Filosofia del Derecho.",
    "Se evita transferir contenido tematico especifico de Filosofia al nodo de Antropologia.",
    "Se mantiene alerta institucional por salidas no JSON parseables y necesidad de normalizacion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener ubicacion curricular local del destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar toda fuente heredada no verificada como provisional hasta confirmacion local.",
    "No trasladar metadatos curriculares de Filosofia del Derecho a Antropologia de la cultura en Mexico."
  ],
  "structure_rules": [
    "Iniciar cada entrega con objetivo puntual y encuadre breve del problema juridico o social.",
    "Organizar secciones en: conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear el producto al entregable solicitado en la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Usar README y programa analitico locales como guias primarias.",
    "Resolver placeholders o tokens dinamicos en nombres de archivos antes de usar rutas."
  ],
  "activity_rules": [
    "Sustentar afirmaciones relevantes con fuente verificable y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion transferible a la practica juridica cuando la consigna lo permita.",
    "Marcar como supuesto cualquier inferencia no confirmada por la actividad."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar memoria.",
    "Normalizar manualmente respuestas no estructuradas antes de aplicarlas aguas abajo.",
    "Confirmar consistencia entre metadatos del documento y contexto curricular local.",
    "No aceptar afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Conservar plantilla .tex local de la materia como base.",
    "Mantener configuracion de espanol y acentos correctos en .tex y .bib.",
    "Mantener clase y formato base salvo justificacion academica.",
    "Actualizar documenttitle y documentsubtitle por actividad real.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir rutas corruptas y tokens sin expandir en README, programa y .tex."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes especificas de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener trazabilidad de archivos locales usados como evidencia documental."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y parseables.",
    "Transferir entre nodos no equivalentes solo abstracciones editoriales estables.",
    "Evitar redaccion literal y contenido disciplinar especifico del nodo origen.",
    "Preservar reglas utiles previas; consolidar por union-dedupe sin recorte.",
    "Etiquetar incidencias de parseo como alertas institucionales reutilizables.",
    "Si falta contexto local, mantener cerebro minimo y abrir vacios en preguntas."
  ],
  "open_questions": [
    "Confirmar rubrica oficial de evaluacion para actividades de Antropologia.",
    "Confirmar si la conclusion juridica es obligatoria en todas las actividades de la materia.",
    "Confirmar estandar de citacion institucional unico para la licenciatura.",
    "Confirmar si la clave LDE-S4B2 es oficial o convencion local.",
    "Supuesto: el .bib canonico local es antropologia-de-la-cultura-en-mexico.bib; confirmar en lineamientos institucionales."
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
      "Problema, conceptos, evidencia, analisis propio y cierre transferible.",
      "Normalizacion estructurada obligatoria antes de propagar.",
      "Compresion lossless por deduplicacion, no por recorte.",
      "Sincronizacion transversal conservadora entre nodos no equivalentes."
    ],
    "reason_for_being": [
      "Asegurar coherencia editorial institucional en entregables LaTeX de la suite academica.",
      "Convertir planeacion semanal en productos verificables y argumentativos.",
      "Preservar memoria util sin regresiones en ciclos sucesivos."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Cierre con valor academico y profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente verificable -> interpretacion propia.",
      "Consigna -> desarrollo alineado -> validacion final de coherencia."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion estructurada",
        "Validacion JSON parseable",
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
          "justification": "Sin parseo valido no hay propagacion confiable."
        },
        {
          "source": "Integridad academica",
          "target": "Evidencia verificable",
          "kind": "depends_on",
          "justification": "La integridad exige respaldo trazable de afirmaciones."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura argumentativa se fortalece con fuentes comprobables."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion util deriva del razonamiento y no del resumen."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Propagacion transversal conservadora",
          "kind": "supports",
          "justification": "La identidad fija limites de transferencia entre materias."
        }
      ],
      "evidence": [
        "README de Antropologia: identidad UnADM y estructura de carpeta canonica.",
        "Programa analitico: ejes problema, conceptos, producto, analisis y cierre.",
        "Bib local: presencia de unadmSitioWeb y unadmMallaDerecho2024.",
        "Memoria origen: gate de bloqueo por salida no JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 49: se refuerza gate JSON parseable como condicion de propagacion recursiva.",
      "Ciclo 49: se incorpora objetivo puntual y coherencia argumentativa como abstracciones estables transferidas.",
      "Ciclo 49: se mantiene separacion entre reglas estables y contenido tematico no transferible.",
      "Ciclo 49: se conserva politica de fuentes provisionales hasta validacion local."
    ]
  }
}