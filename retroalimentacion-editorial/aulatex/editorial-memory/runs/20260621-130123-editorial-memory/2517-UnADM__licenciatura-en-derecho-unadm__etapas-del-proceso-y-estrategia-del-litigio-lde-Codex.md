{
  "summary": [
    "Sincronizacion transversal consolidada con compresion lossless por union-dedupe y sin regresion.",
    "Se preservan reglas estables: identidad UnADM, cinco ejes editoriales, validacion JSON parseable y trazabilidad.",
    "Se transfiere solo abstraccion reusable desde actividad de Filosofia del Derecho a materia de litigio.",
    "Se mantiene separacion entre fuentes provisionales tecnicas y autoridad academica verificable.",
    "Se refuerza normalizacion estructurada obligatoria antes de propagacion recursiva."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Conservar trazabilidad de origen editorial en cada fusion de memoria.",
    "Marcar como [supuesto] todo dato no visible en consigna o documentos locales.",
    "Registrar fuentes heredadas no verificadas como provisionales y no como autoridad academica."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Aplicar cinco ejes: problema, conceptos, producto solicitado, analisis propio, conclusion transferible.",
    "Alinear estructura al producto pedido en planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Verificar instruccion especifica de cada actividad antes de redactar.",
    "Evitar entregas solo descriptivas; exigir postura argumentada del estudiante.",
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Agregar fuentes especificas de actividad al .bib local antes de version final.",
    "No asumir reutilizacion automatica de fuentes de otras semanas o materias."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de fusionar aguas abajo.",
    "Confirmar que toda afirmacion factual tenga fuente o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar union-dedupe sin eliminar reglas utiles previas.",
    "Normalizar manualmente memorias heredadas no estructuradas de ciclos tempranos."
  ],
  "latex_rules": [
    "Usar plantilla .tex local de la materia como base.",
    "Conservar macros institucionales de portada y curso.",
    "Mantener compatibilidad con espanol y letterpaper segun plantilla.",
    "No eliminar campos de portada; completar faltantes por actividad.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y documentos de apoyo.",
    "Corregir nombres de archivo corruptos antes de compilar y referenciar.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Usar etapas-del-proceso-y-estrategia-del-litigio.bib como repositorio local canonico.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/editorial o URL.",
    "Incluir fecha de consulta en fuentes web o institucionales dinamicas.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "No propagar redaccion literal ni metadatos hiperlocales de actividad origen.",
    "Reforzar en nodos vecinos la regla de JSON parseable previo a fusion.",
    "Mantener advertencia historica: ciclos con salida no estructurada requieren normalizacion manual.",
    "Preservar no regresion en cada ciclo de sincronizacion transversal."
  ],
  "open_questions": [
    "Confirmar estilo de citacion juridica requerido por la materia (APA, Chicago, ISO 690 u otro).",
    "Confirmar si documentauthor debe ser fijo de plantilla o variable por estudiante. [supuesto]",
    "Validar coursecode institucional definitivo si cambia respecto a LDE-S5B2. [supuesto]",
    "Confirmar checklist minimo por tipo de producto: reporte, presentacion y visual.",
    "Verificar y corregir entradas README con caracteres corruptos y rutas incompletas."
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
        "Trazabilidad editorial en consolidaciones."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 5, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Etapas del proceso y estrategia del litigio."
      ]
    },
    "essence": [
      "Problema juridico activo.",
      "Fundamento conceptual y normativo pertinente.",
      "Analisis propio sustentado.",
      "Cierre juridico transferible.",
      "Normalizacion estructurada antes de propagar."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos solidos y verificables.",
      "Asegurar consistencia editorial transversal sin perder contexto local.",
      "Sostener memoria persistente con compresion lossless y no regresion."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Bloques argumentativos visibles.",
      "Citas trazables.",
      "Marcado explicito de [supuesto] cuando aplique.",
      "Conclusion juridica aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis propio -> conclusion juridica.",
      "Afirmacion -> evidencia -> interpretacion -> implicacion practica.",
      "Objetivo puntual -> desarrollo alineado -> verificacion de consigna."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Cinco ejes editoriales",
        "JSON parseable",
        "Normalizacion estructurada",
        "Union-dedupe sin regresion",
        "Integridad academica",
        "Conclusion juridica transferible"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "JSON parseable",
          "target": "Propagacion recursiva segura",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay fusion confiable."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Calidad de entregables",
          "kind": "supports",
          "justification": "Ordenan contenido, evidencia y cierre juridico."
        },
        {
          "source": "Union-dedupe sin regresion",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Conserva reglas utiles previas sin perdida."
        },
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica",
          "kind": "develops",
          "justification": "La pauta institucional exige verificabilidad y trazabilidad."
        }
      ],
      "evidence": [
        "README local de materia con ubicacion curricular y pauta editorial.",
        "Programa analitico con proposito y cinco ejes de trabajo.",
        "Bib local con fuentes institucionales base.",
        "Plantilla .tex local con macros institucionales y coursecode visible."
      ]
    },
    "reinforcement_log": [
      "Ciclo 14: se refuerza transferencia por abstracciones estables entre nodos transversales.",
      "Ciclo 14: se mantiene regla critica de bloqueo por JSON no parseable.",
      "Ciclo 14: se preserva separacion entre fuente provisional tecnica y fuente academica verificable.",
      "Ciclo 14: se agrega control de tokens sin expandir en README como gate LaTeX operativo."
    ]
  }
}