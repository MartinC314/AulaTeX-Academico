{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia conservadora.",
    "Se preserva identidad UnADM y estructura editorial comun.",
    "Se transfieren solo abstracciones estables desde actividad origen.",
    "Se mantiene regla de normalizacion previa para salidas no JSON.",
    "Destino consolida cerebro editorial minimo con vacios locales abiertos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y metadatos.",
    "Usar nombre exacto de materia: Derecho de la propiedad y registro.",
    "Conservar programa: Licenciatura en Derecho.",
    "Registrar ubicacion curricular verificada: semestre 7, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el entregable al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar extrapolar fuentes de otras semanas sin validacion.",
    "Vincular cada actividad con propiedad y registro cuando corresponda."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar.",
    "Normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar que placeholders y tokens de ruta esten resueltos."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Mantener clase y opciones base locales salvo instruccion docente distinta.",
    "Completar metadatos academicos obligatorios antes de compilar.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, referencias rotas ni placeholders.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Mantener claves BibTeX estables para evitar rupturas."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Usar el .bib local de la materia para fuentes especificas.",
    "No inventar referencias; usar solo obras consultables o archivos locales.",
    "Conservar metadatos minimos: autor, titulo, año y fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y no ambiguas.",
    "Compartir solo abstracciones estables entre nodos no equivalentes.",
    "Evitar transferir redaccion literal o contenidos tematicos de otra materia.",
    "Preservar reglas utiles previas sin regresion por ciclos.",
    "Aplicar compresion lossless por union y deduplicacion."
  ],
  "open_questions": [
    "Supuesto: falta rubrica docente especifica de la materia destino.",
    "Confirmar formato exigido por actividad: reporte, presentacion u otro.",
    "Confirmar estilo de citacion juridica requerido por figura docente.",
    "Confirmar dato local pendiente: nombre de figura docente en plantilla.",
    "Confirmar si existe guia de evaluacion por semana para propiedad y registro."
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
        "Entrada canonica en carpeta de asignatura."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho de la propiedad y registro.",
        "Semestre 7, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos verificables.",
      "Garantizar fundamento juridico, evidencia y cierre argumentativo profesional."
    ],
    "style_markers": [
      "Supuestos explicitos cuando falte evidencia local.",
      "Razonamiento juridico con trazabilidad de fuentes.",
      "Estructura reusable centrada en problema-analisis-conclusion."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo al inicio.",
      "Construir marco conceptual y normativo minimo.",
      "Desarrollar analisis propio con contraste de fuentes.",
      "Cerrar con conclusion que responda al problema inicial."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Citas verificables",
        "Problema juridico",
        "Analisis propio",
        "Conclusion transferible",
        "Propiedad y registro"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige trazabilidad y rigor."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El analisis parte de una pregunta juridica delimitada."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion valida aplicabilidad profesional."
        },
        {
          "source": "Citas verificables",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "Las fuentes sustentan afirmaciones y evitan opinion vacia."
        },
        {
          "source": "Propiedad y registro",
          "target": "Problema juridico",
          "kind": "depends_on",
          "justification": "El problema debe anclarse al campo disciplinar destino."
        }
      ],
      "evidence": [
        "README de materia: pauta editorial y ubicacion curricular.",
        "Programa analitico: proposito y ejes de trabajo.",
        "Bib local: unadmSitioWeb y unadmMallaDerecho2024."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin perdida semantica.",
      "Se conservaron gates de JSON y normalizacion heredados.",
      "Se reforzo patron argumentativo reusable transversal.",
      "Se evito transferencia de contenidos tematicos no equivalentes de Filosofia del Derecho.",
      "Se marco como supuesto todo vacio de contexto local."
    ]
  }
}