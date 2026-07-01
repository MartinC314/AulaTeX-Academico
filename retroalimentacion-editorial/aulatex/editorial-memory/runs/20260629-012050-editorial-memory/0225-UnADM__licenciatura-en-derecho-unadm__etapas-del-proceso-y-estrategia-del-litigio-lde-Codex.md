{
  "summary": [
    "Sincronizacion transversal consolidada con estrategia conservadora y sin regresion.",
    "Se preservan reglas estables transferibles: identidad UnADM, cinco ejes editoriales, evidencia verificable y cierre juridico.",
    "Se refuerza normalizacion JSON parseable previa a toda propagacion recursiva.",
    "Se mantiene compresion lossless por union-dedupe sin recorte semantico.",
    "Se crea base minima robusta para materia destino con vacios locales abiertos y marcados."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables a Licenciatura en Derecho, semestre 5, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Conservar trazabilidad del origen editorial en cada consolidacion.",
    "Marcar como [supuesto] todo dato no visible en consigna o documento local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar desarrollo en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear siempre la salida al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Usar el programa analitico como guia de los cinco ejes."
  ],
  "activity_rules": [
    "Verificar instruccion especifica de cada actividad antes de redactar.",
    "Sustentar cada afirmacion con fuente verificable o marcar [supuesto].",
    "Incluir postura argumentada propia; evitar entregas solo descriptivas.",
    "Rubricar cada entrega contra los cinco ejes editoriales.",
    "Confirmar coherencia entre consigna, desarrollo y conclusion.",
    "Agregar fuentes especificas de actividad al .bib local antes de version final."
  ],
  "quality_gates": [
    "Bloquear propagacion si la memoria no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Comprobar union-dedupe sin eliminar reglas utiles previas.",
    "Verificar consistencia entre metadatos curriculares y contenido.",
    "Confirmar correspondencia entre citas en texto y archivo .bib.",
    "Revisar y normalizar toda salida no estructurada antes de reutilizar."
  ],
  "latex_rules": [
    "Usar plantilla .tex local de la materia como base.",
    "Conservar macros institucionales de portada y curso.",
    "Mantener compatibilidad con espanol y letterpaper definidos en plantilla.",
    "No eliminar campos de portada; completar segun actividad.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y documentos de apoyo.",
    "Corregir nombres de archivo corruptos antes de compilar y referenciar."
  ],
  "bibliography_rules": [
    "Usar etapas-del-proceso-y-estrategia-del-litigio.bib como repositorio local canonico.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; registrar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Incluir fecha de consulta en fuentes web o institucionales dinamicas.",
    "Distinguir bibliografia base de bibliografia especifica de actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo abstracciones estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "No propagar redaccion literal ni metadatos hiperlocales de actividad origen.",
    "Mantener advertencia institucional: normalizar salidas no parseables antes de fusionar.",
    "Aplicar estrategia progresiva: reforzar primero reglas nucleares, luego ajustes locales.",
    "Mantener estrategia conservadora: cero regresion en reglas utiles ya consolidadas."
  ],
  "open_questions": [
    "Confirmar estilo de citacion juridica oficial de la materia (APA, Chicago, ISO 690 u otro).",
    "Confirmar si documentauthor es fijo de plantilla o variable por estudiante. [supuesto]",
    "Confirmar vigencia operativa de coursecode LDE-S5B2. [supuesto]",
    "Confirmar checklist minimo por tipo de producto: reporte, presentacion y visual.",
    "Confirmar si toda referencia heredada provisional debe quedar solo como nota tecnica."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Sobrio y verificable."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta de asignatura como entrada canonica.",
        "Trazabilidad editorial en cada consolidacion."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 5, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Etapas del proceso y estrategia del litigio.",
        "Fuente curricular: malla-curricular-derecho-unadm.pdf."
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
      "Convertir planeacion semanal en entregables juridicos claros, sustentados y aplicables.",
      "Asegurar consistencia institucional y calidad editorial en toda actividad.",
      "Permitir propagacion transversal segura mediante reglas estables y verificables."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales reutilizables.",
      "Citas trazables.",
      "Marcado explicito de [supuesto].",
      "Cierre con implicacion practica juridica."
    ],
    "argumentative_patterns": [
      "Problema -> fundamento conceptual/normativo -> analisis -> conclusion.",
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
          "justification": "La identidad exige citas verificables y trazabilidad."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La secuencia de trabajo culmina en cierre aplicable."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Compresion union-dedupe sin perdida",
          "kind": "depends_on",
          "justification": "No hay deduplicacion segura sin estructura parseable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Toda afirmacion debe tener respaldo o [supuesto]."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "Bib local: claves institucionales activas y verificables.",
        "Plantilla .tex local: macros institucionales y estructura base."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin eliminar contenido util.",
      "Se preservaron gates institucionales de parseo JSON y no regresion.",
      "Se reforzo transferencia transversal en nivel de abstraccion estable.",
      "Se mantuvieron supuestos explicitamente marcados cuando falta validacion local."
    ]
  }
}