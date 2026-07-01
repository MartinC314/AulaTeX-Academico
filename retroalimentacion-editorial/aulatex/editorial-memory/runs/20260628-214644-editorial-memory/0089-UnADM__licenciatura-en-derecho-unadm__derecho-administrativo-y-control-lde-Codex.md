{
  "summary": [
    "Se consolida cerebro editorial minimo de materia con union-dedupe lossless y sin regresion.",
    "Se preserva identidad UnADM y alineacion curricular local: semestre 6, bloque 1, obligatoria, 8 creditos.",
    "Se refuerzan ejes transversales estables: problema, conceptos/fuentes, analisis propio y conclusion juridica transferible.",
    "Se mantiene gate critico: no propagar salidas no estructuradas ni JSON no parseable.",
    "Se corrigen como regla los artefactos de tokens sin expandir y nombres de archivo corruptos en README/programa. [supuesto]"
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre exacto de materia: Derecho administrativo y control.",
    "Conservar enfoque de Licenciatura en Derecho en todos los entregables.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como [supuesto] todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear el producto al solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica aplicable a la practica profesional.",
    "Mantener consistencia entre README, .tex y .bib.",
    "Normalizar placeholders y rutas antes de publicar estructura."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante en cada actividad.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Explicitar tipo de producto antes del desarrollo: reporte, presentacion o visual.",
    "Vincular analisis con control administrativo y practica juridica del campo."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Detener propagacion ante respuesta no estructurada o campos criticos vacios.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que reglas heredadas no contradigan el programa analitico local."
  ],
  "latex_rules": [
    "Mantener plantilla en espanol y letterpaper segun archivo base.",
    "Completar metadatos institucionales y de curso antes de compilar.",
    "Sustituir \"Actividad X\" por numero y nombre real.",
    "Sustituir \"Nombre por definir\" por figura docente oficial antes de entrega.",
    "Usar acentos y codificacion correctos en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) por slug literal en README y programa. [supuesto]"
  ],
  "bibliography_rules": [
    "Registrar fuentes de cada actividad en derecho-administrativo-y-control.bib.",
    "Priorizar fuentes institucionales UnADM y documentos juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener trazabilidad entre afirmacion y evidencia citada."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Compartir solo abstracciones editoriales estables en nodos transversales.",
    "No trasladar contenido doctrinal especifico de otra materia sin verificacion local.",
    "Aplicar normalizacion manual cuando se detecten salidas no estructuradas.",
    "Mantener estrategia progresiva y conservadora: agregar sin borrar reglas utiles previas."
  ],
  "open_questions": [
    "Confirmar rubrica de evaluacion especifica de la materia para ajustar profundidad argumentativa.",
    "Confirmar formato institucional de citacion exigido en Licenciatura en Derecho.",
    "Confirmar nombre oficial de la figura docente en plantilla.",
    "Confirmar si el anio de consulta del sitio UnADM debe mantenerse en 2026.",
    "Verificar y corregir en README los nombres truncados \"eporte\" y \"eferencias\". [supuesto]"
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
        "Semestre 6, bloque 1, obligatoria, 8 creditos.",
        "Materia: Derecho administrativo y control."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas, doctrina y fuentes pertinentes.",
      "Producto solicitado por planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros, fundados y verificables.",
      "Asegurar transferencia profesional del razonamiento juridico en cada entrega."
    ],
    "style_markers": [
      "Objetivo puntual al inicio.",
      "Secciones visibles y ordenadas.",
      "Cierre con criterio juridico aplicado.",
      "Marcado explicito de [supuesto] cuando falte evidencia."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis propio -> conclusion aplicada.",
      "Afirmacion -> evidencia verificable -> interpretacion juridica -> implicacion practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad academica",
        "Problema juridico",
        "Marco normativo/doctrinal",
        "Analisis propio",
        "Conclusion transferible",
        "Control administrativo",
        "Planeacion semanal"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Integridad academica",
          "target": "Citas verificables",
          "kind": "supports",
          "justification": "Evita afirmaciones sin respaldo y fuentes inventadas."
        },
        {
          "source": "Planeacion semanal",
          "target": "Tipo de producto",
          "kind": "depends_on",
          "justification": "La consigna define si se entrega reporte, presentacion o visual."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "El criterio juridico se construye sobre fuentes pertinentes."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion debe derivar del razonamiento del estudiante."
        }
      ],
      "evidence": [
        "README de materia: ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y ejes de trabajo.",
        "derecho-administrativo-y-control.bib: base institucional inicial."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas conservando semanticamente todo lo valido.",
      "Se reforzo gate JSON parseable como condicion de propagacion transversal.",
      "Se mantuvo separacion entre reglas editoriales estables y contenido doctrinal especifico.",
      "Se integraron correcciones estructurales locales detectadas en README/programa como supuestos verificables."
    ]
  }
}