{
  "summary": [
    "Se sincroniza memoria transversal desde actividad de otra materia con transferencia solo de abstracciones estables.",
    "Se conserva identidad UnADM y alineacion curricular local de Derecho administrativo y control.",
    "Se refuerzan ejes editoriales reutilizables: problema, conceptos/fuentes, analisis propio y conclusion juridica.",
    "Se mantiene compresion lossless por union-dedupe sin regresion.",
    "Se preserva gate critico: bloquear propagacion ante salida no JSON parseable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre exacto de materia: Derecho administrativo y control.",
    "Conservar enfoque de Licenciatura en Derecho en todos los productos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como [supuesto] todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear siempre el producto a la planeacion semanal y consigna vigente.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Mantener consistencia entre README, programa analitico, .tex y .bib.",
    "Corregir placeholders y tokens sin expandir en rutas y nombres de archivo. [supuesto]"
  ],
  "activity_rules": [
    "Explicitar tipo de producto antes del desarrollo: reporte, presentacion o visual.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante en cada actividad.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Separar reglas editoriales generales de contenido doctrinal de otras materias."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Detener propagacion ante respuesta no estructurada o campos criticos vacios.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar que reglas heredadas no contradigan el programa analitico local."
  ],
  "latex_rules": [
    "Mantener plantilla LaTeX en español y formato base institucional.",
    "Completar metadatos de actividad real antes de compilar.",
    "Reemplazar 'Actividad X' por numero y nombre real.",
    "Completar figura docente con nombre oficial antes de entrega. [supuesto]",
    "Usar codificacion y acentos correctos en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas."
  ],
  "bibliography_rules": [
    "Registrar fuentes de cada actividad en derecho-administrativo-y-control.bib.",
    "Priorizar fuentes institucionales UnADM y documentos juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Tratar cualquier referencia heredada de otra materia como provisional hasta validacion local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validacion JSON y estructura.",
    "Transferir entre nodos no equivalentes solo reglas editoriales estables.",
    "No propagar redaccion literal ni contenido doctrinal especifico de Filosofia del Derecho.",
    "Aplicar normalizacion manual cuando reaparezcan salidas no estructuradas.",
    "Mantener estrategia progresiva y conservadora: agregar solo mejoras verificables."
  ],
  "open_questions": [
    "Confirmar formato institucional de citacion exigido por la materia. [supuesto]",
    "Confirmar nombre oficial de figura docente para plantilla .tex. [supuesto]",
    "Confirmar si el año de consulta del sitio UnADM debe actualizarse por ciclo. [supuesto]",
    "Confirmar que todos los tokens $(@{...}.Slug) ya fueron resueltos en README/programa. [supuesto]"
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Aplicado a practica profesional."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada antes de propagar.",
        "Marcado explicito de supuestos."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 6, bloque 1, obligatoria, 8 creditos.",
        "Materia: Derecho administrativo y control."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y fuentes pertinentes.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible.",
      "Calidad estructural verificable."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros, fundamentados y aplicables.",
      "Asegurar trazabilidad entre afirmaciones, evidencia y conclusion.",
      "Preservar continuidad editorial institucional entre actividades y materias."
    ],
    "style_markers": [
      "Objetivo puntual al inicio.",
      "Secciones visibles y ordenadas.",
      "Cierre con criterio juridico aplicado.",
      "Etiqueta [supuesto] cuando falte evidencia."
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
        "Planeacion semanal",
        "Control administrativo"
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
          "justification": "Sostiene afirmaciones con evidencia y evita fuentes inventadas."
        },
        {
          "source": "Planeacion semanal",
          "target": "Tipo de producto",
          "kind": "depends_on",
          "justification": "La consigna define formato y alcance de entrega."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "El criterio juridico requiere fundamento verificable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion deriva del razonamiento del estudiante."
        },
        {
          "source": "Reglas transversales estables",
          "target": "Sincronizacion entre materias",
          "kind": "supports",
          "justification": "Permite continuidad editorial sin mezclar contenidos sustantivos no equivalentes."
        }
      ],
      "evidence": [
        "README de materia con ubicacion curricular y pauta editorial.",
        "Programa analitico con proposito y ejes de trabajo.",
        "derecho-administrativo-y-control.bib con base institucional.",
        "Historial de alerta por salidas no JSON parseables."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin perdida semantica.",
      "Se transfirieron solo abstracciones editoriales estables desde origen transversal.",
      "Se mantuvieron gates de calidad y no regresion.",
      "Se dejaron abiertos vacios de contexto local no verificados."
    ]
  }
}