{
  "summary": [
    "Sincronizacion transversal consolidada para materia destino con identidad UnADM.",
    "Se preservan reglas estables del origen: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene estrategia conservadora: union-dedupe sin perdida y sin regresion.",
    "Se refuerza validacion previa de JSON parseable antes de propagar.",
    "Se crea cerebro editorial minimo reconstruible para el destino con vacios locales abiertos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables a Licenciatura en Derecho, semestre 5, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como [supuesto] todo dato no visible en consigna o documento local.",
    "Conservar trazabilidad de origen editorial en cada consolidacion.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto pedido por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Usar programa analitico como guia de los cinco ejes editoriales."
  ],
  "activity_rules": [
    "Verificar instruccion especifica de la actividad antes de redactar.",
    "Rubricar cada entrega contra los cinco ejes editoriales.",
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Incluir postura argumentada propia; evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir fuentes de otras semanas sin validacion de pertinencia."
  ],
  "quality_gates": [
    "Bloquear propagacion si la memoria no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que toda afirmacion factual tenga fuente o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar y normalizar salidas no estructuradas antes de reutilizarlas.",
    "Evitar regresiones: no eliminar reglas utiles previas en fusion."
  ],
  "latex_rules": [
    "Usar plantilla .tex local de la materia como base.",
    "Conservar macros institucionales de curso y universidad.",
    "Mantener compatibilidad con espanol y letterpaper.",
    "No eliminar campos de portada; completar segun actividad.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo corruptos en README antes de referenciar en LaTeX. [supuesto]",
    "Compilar sin errores criticos y sin referencias rotas."
  ],
  "bibliography_rules": [
    "Usar etapas-del-proceso-y-estrategia-del-litigio.bib como repositorio local.",
    "Agregar fuentes especificas de actividad antes de version final.",
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Incluir fecha de consulta en fuentes web o institucionales dinamicas.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo abstracciones estables, no redaccion literal.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "No propagar metadatos hiperlocales a nodos no equivalentes.",
    "Aplicar normalizacion manual cuando un nodo vecino entregue salida no parseable.",
    "Reutilizar regla institucional: validar JSON antes de cualquier fusion recursiva.",
    "Mantener ciclo progresivo y conservador con union-dedupe sin perdida."
  ],
  "open_questions": [
    "Confirmar checklist minimo por tipo de producto: reporte, presentacion y visual.",
    "Confirmar estilo de citacion juridica requerido por la asignatura.",
    "Confirmar si documentauthor en plantilla es fijo o variable por estudiante. [supuesto]",
    "Confirmar correccion definitiva de nombres de archivo corruptos en README. [supuesto]",
    "Confirmar si existen exigencias de rubrica docente adicionales a los cinco ejes. [supuesto]"
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
        "Carpeta de asignatura como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 5, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Etapas del proceso y estrategia del litigio."
      ]
    },
    "essence": [
      "Problema juridico o social que activa la actividad.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion transferible a practica juridica."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos claros, fundados y aplicables.",
      "Asegurar trazabilidad, verificabilidad de fuentes y coherencia argumentativa.",
      "Sostener estandar institucional transversal entre materias juridicas."
    ],
    "style_markers": [
      "Encuadre inicial breve del problema.",
      "Secciones claras y reutilizables.",
      "Citas trazables y verificables.",
      "Cierre juridico con criterio propio.",
      "Marcado explicito de [supuesto] cuando falte evidencia local."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis -> conclusion juridica.",
      "Afirmacion -> evidencia -> interpretacion -> implicacion practica.",
      "Consigna -> desarrollo alineado -> verificacion por rubrica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Cinco ejes editoriales",
        "Integridad academica",
        "Evidencia verificable",
        "Conclusion juridica transferible",
        "Normalizacion JSON",
        "Compresion union-dedupe sin perdida"
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
          "justification": "La pauta editorial exige citas verificables y consistencia institucional."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La secuencia de ejes culmina en cierre aplicable a practica profesional."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Compresion union-dedupe sin perdida",
          "kind": "depends_on",
          "justification": "La fusion segura requiere estructura parseable para deduplicar sin recorte."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Toda afirmacion debe tener fuente o marca de supuesto."
        }
      ],
      "evidence": [
        "README de materia: identidad UnADM, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "Archivo .bib local: unadmSitioWeb y unadmMallaDerecho2024.",
        "Plantilla .tex: macros institucionales y coursecode LDE-S5B2 [supuesto operativo hasta validacion docente]."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas manteniendo significado completo.",
      "Se transfirieron solo abstracciones estables desde actividad origen a materia destino.",
      "Se evitaron contenidos tematicos hiperlocales de Filosofia del Derecho no equivalentes al destino.",
      "Se reforzaron gates de calidad y grafo conceptual para propagacion recursiva.",
      "Se marcaron vacios locales y supuestos sin inventar fuentes."
    ]
  }
}