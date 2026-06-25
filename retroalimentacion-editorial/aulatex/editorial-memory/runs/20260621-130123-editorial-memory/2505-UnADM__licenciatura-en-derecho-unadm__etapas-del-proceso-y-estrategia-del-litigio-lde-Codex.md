{
  "summary": [
    "Sincronizacion transversal ciclo 11 aplicada con estrategia progresiva y conservadora.",
    "Se preservan reglas utiles previas del destino sin eliminaciones.",
    "Se incorporan solo abstracciones estables del origen no equivalente.",
    "Se refuerzan ejes reutilizables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene compresion lossless por union y deduplicacion.",
    "Se mantiene bloqueo de propagacion para salidas no JSON parseable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Conservar trazabilidad de origen editorial en cada fusion.",
    "Marcar como [supuesto] todo dato no visible en consigna o documentos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales y no como autoridad academica."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear estructura al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Aplicar cinco ejes editoriales del programa analitico en toda entrega."
  ],
  "activity_rules": [
    "Verificar instruccion especifica de actividad antes de redactar.",
    "Rubricar la entrega contra los cinco ejes editoriales.",
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar resumen descriptivo puro.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir pertinencia automatica de fuentes de otras semanas o materias."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Exigir estructura minima completa antes de fusionar memoria.",
    "Confirmar que cada afirmacion factual tenga fuente o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar union-dedupe sin borrar reglas utiles previas.",
    "Normalizar respuestas no estructuradas antes de reutilizacion recursiva."
  ],
  "latex_rules": [
    "Usar plantilla .tex local de la materia como base.",
    "Conservar macros institucionales de portada y metadatos.",
    "Mantener compatibilidad con espanol y letterpaper.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y documentos de apoyo.",
    "Corregir nombres de archivo corruptos antes de referenciar o compilar. [supuesto]"
  ],
  "bibliography_rules": [
    "Usar etapas-del-proceso-y-estrategia-del-litigio.bib como repositorio local.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Agregar fuentes especificas de cada actividad antes de version final.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Incluir fecha de consulta en fuentes web o institucionales dinamicas."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales y estables entre nodos no equivalentes.",
    "Priorizar identidad, gates de calidad, estructura reusable y grafo conceptual.",
    "No propagar redaccion literal de actividades de origen.",
    "Mantener metadatos especificos anclados al nodo destino.",
    "Reforzar en nodos vecinos la regla de JSON parseable previo a fusion.",
    "Si un nodo destino esta incompleto, crear cerebro minimo y abrir vacios locales."
  ],
  "open_questions": [
    "Confirmar estilo de citacion juridica requerido por la asignatura.",
    "Confirmar si documentauthor es fijo de plantilla o variable por estudiante. [supuesto]",
    "Confirmar coursecode institucional definitivo para la materia. [supuesto]",
    "Confirmar checklist minimo por tipo de producto: reporte, presentacion, visual.",
    "Confirmar correccion definitiva de nombres corruptos en README. [supuesto]"
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Juridicamente preciso.",
        "Claro y verificable.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta de asignatura como entrada canonica.",
        "Fuentes provisionales separadas de autoridad academica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 5, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Etapas del proceso y estrategia del litigio."
      ]
    },
    "essence": [
      "Problema juridico claro.",
      "Conceptos y fundamento normativo pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con rigor juridico.",
      "Mantener coherencia entre consigna, desarrollo argumentativo y cierre profesional.",
      "Sostener memoria editorial persistente sin regresion."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Bloques argumentativos visibles.",
      "Citas trazables en el cuerpo del texto.",
      "Cierre aplicable a practica juridica."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis propio -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> implicacion practica.",
      "Objetivo puntual -> desarrollo alineado -> verificacion de coherencia final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Cinco ejes editoriales",
        "JSON parseable",
        "Normalizacion estructurada",
        "Union-dedupe sin regresion",
        "Conclusion juridica transferible",
        "Integridad academica",
        "Trazabilidad editorial"
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
          "justification": "La propagacion segura requiere estructura valida previa."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Union-dedupe sin regresion",
          "kind": "supports",
          "justification": "Evita perdida de reglas utiles durante consolidacion."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La secuencia editorial conduce a un cierre aplicable."
        },
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige verificabilidad y rigor."
        }
      ],
      "evidence": [
        "README de materia: ubicacion curricular y pauta editorial.",
        "Programa analitico: cinco ejes de trabajo.",
        "Bib local con fuentes institucionales verificables.",
        "Regla heredada estable: bloquear salidas no JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 11: se refuerza transferencia transversal por abstracciones estables.",
      "Ciclo 11: se mantiene no regresion y deduplicacion lossless.",
      "Ciclo 11: se consolidan gates de calidad como nucleo persistente.",
      "Ciclo 11: se preserva separacion entre fuentes provisionales y autoridad academica."
    ]
  }
}