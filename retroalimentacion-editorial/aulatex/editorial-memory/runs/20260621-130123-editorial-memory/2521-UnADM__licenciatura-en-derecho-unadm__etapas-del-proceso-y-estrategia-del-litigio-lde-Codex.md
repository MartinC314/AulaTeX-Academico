{
  "summary": [
    "Se consolida sincronizacion transversal desde actividad de Filosofia del Derecho hacia materia de Etapas del proceso y estrategia del litigio.",
    "Se preservan reglas estables: identidad UnADM, cinco ejes editoriales, validacion JSON parseable y compresion union-dedupe sin regresion.",
    "Se evita transferencia literal entre nodos no equivalentes; solo se propagan abstracciones reutilizables.",
    "Se mantiene trazabilidad de fuentes heredadas no verificadas como provisionales y fuera de autoridad academica.",
    "Se refuerza normalizacion estructurada previa a propagacion recursiva."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Mantener tono academico-juridico formal, claro y argumentativo.",
    "Exigir postura propia sustentada en cada entrega.",
    "Marcar como [supuesto] todo dato no visible en consigna o documentos locales.",
    "Registrar fuentes heredadas no verificadas como provisionales."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear estructura al producto solicitado por la planeacion semanal.",
    "Aplicar cinco ejes editoriales: problema, conceptos, producto, analisis propio, conclusion transferible.",
    "Cerrar con conclusion juridica aplicable a la practica profesional."
  ],
  "activity_rules": [
    "Verificar instruccion especifica de cada actividad antes de redactar.",
    "Rubricar cada entrega contra los cinco ejes del programa analitico.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar cada afirmacion con evidencia verificable y cita explicita.",
    "Agregar fuentes especificas de actividad al .bib local antes de la version final.",
    "No asumir que bibliografia de otras semanas aplica automaticamente."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de fusionar memoria.",
    "Aplicar union-dedupe sin eliminar reglas utiles previas.",
    "Confirmar que toda afirmacion factual tenga fuente o marca [supuesto].",
    "Revisar consistencia entre citas en texto y archivo .bib.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Validar correspondencia entre producto entregado y consigna de actividad."
  ],
  "latex_rules": [
    "Usar plantilla .tex local de la materia como base.",
    "Conservar macros institucionales de portada y metadatos.",
    "Mantener compatibilidad con español y letterpaper segun plantilla.",
    "No eliminar campos de portada; completar faltantes segun actividad.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir rutas o nombres con caracteres corruptos antes de compilar.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Usar etapas-del-proceso-y-estrategia-del-litigio.bib como repositorio local.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año, fuente o URL.",
    "Incluir fecha de consulta en fuentes web o institucionales dinamicas.",
    "Distinguir bibliografia base de bibliografia especifica de actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales y estables en nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "No propagar redaccion literal de actividades origen.",
    "Mantener advertencia de normalizacion manual para memorias heredadas no parseables de ciclos iniciales.",
    "Conservar no regresion como criterio obligatorio en cada ciclo."
  ],
  "open_questions": [
    "Confirmar si documentauthor debe ser fijo de plantilla o variable por estudiante. [supuesto]",
    "Confirmar estilo de citacion juridica requerido por la asignatura.",
    "Confirmar si coursecode LDE-S5B2 es definitivo. [supuesto]",
    "Confirmar checklist minimo por tipo de producto: reporte, presentacion y visual.",
    "Confirmar si toda fuente provisional heredada debe quedar solo como nota tecnica."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Verificable y orientado a practica profesional."
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
      "Problema juridico o social.",
      "Conceptos, normas y doctrina pertinentes.",
      "Producto solicitado por planeacion.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos juridicos claros, sustentados y aplicables.",
      "Estandarizar calidad editorial sin perder adaptacion a cada actividad."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Bloques argumentativos visibles.",
      "Citas trazables.",
      "Cierre juridico aplicable.",
      "Supuestos etiquetados."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis propio -> conclusion juridica.",
      "Afirmacion -> evidencia -> interpretacion -> implicacion practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Cinco ejes editoriales",
        "JSON parseable",
        "Normalizacion estructurada",
        "Union-dedupe sin regresion",
        "Conclusion juridica transferible",
        "Fuentes provisionales no autoritativas"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica con citas verificables",
          "kind": "supports",
          "justification": "La identidad institucional exige verificabilidad."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Estructura de entrega",
          "kind": "develops",
          "justification": "Los ejes definen el orden argumentativo reutilizable."
        },
        {
          "source": "JSON parseable",
          "target": "Propagacion recursiva segura",
          "kind": "depends_on",
          "justification": "Sin parseo valido no hay fusion confiable."
        },
        {
          "source": "Union-dedupe sin regresion",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Permite compresion lossless sin perder reglas utiles."
        }
      ],
      "evidence": [
        "README de materia con ubicacion curricular y pauta editorial.",
        "Programa analitico con cinco ejes de trabajo.",
        "Archivo .bib local con fuentes institucionales base.",
        "Plantilla .tex con macros y metadatos institucionales."
      ]
    },
    "reinforcement_log": [
      "Ciclo 15: se preservan reglas validas previas y se deduplican sin recorte.",
      "Ciclo 15: se refuerza transferencia transversal por abstracciones estables.",
      "Ciclo 15: se mantiene bloqueo por JSON no parseable.",
      "Ciclo 15: se refuerza etiquetado de [supuesto] para datos no verificados."
    ]
  }
}