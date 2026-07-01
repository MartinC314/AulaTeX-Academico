{
  "summary": [
    "Se consolida sincronizacion transversal entre actividad de origen y materia destino sin recorte.",
    "Se preservan reglas estables: identidad UnADM, cinco ejes editoriales y validacion estructural previa.",
    "Se mantiene estrategia conservadora: union-dedupe lossless y sin regresion.",
    "Se refuerza que la materia destino use cerebro editorial minimo reconstruible mientras se completan vacios locales.",
    "Se confirma que las salidas no parseables quedan como insumo provisional y requieren normalizacion manual."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables a Licenciatura en Derecho, semestre 5, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Conservar trazabilidad de origen editorial en cada consolidacion.",
    "Marcar como [supuesto] cualquier dato no visible en consigna o documento local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Registrar fuentes provisionales como nota tecnica y no como autoridad academica."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto pedido por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Usar el programa analitico como guia operativa de los cinco ejes editoriales."
  ],
  "activity_rules": [
    "Verificar instruccion especifica de cada actividad antes de redactar.",
    "Rubricar cada entrega contra los cinco ejes: problema, conceptos, producto, analisis, conclusion.",
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Incluir postura argumentada del estudiante y evitar entregas solo descriptivas.",
    "Agregar fuentes especificas de actividad al .bib local antes de version final.",
    "No extrapolar fuentes de otras semanas sin justificar pertinencia."
  ],
  "quality_gates": [
    "Bloquear propagacion si la memoria no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Comprobar que toda afirmacion factual tenga fuente o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar correspondencia entre producto entregado y consigna de actividad.",
    "Aplicar union-dedupe sin eliminar reglas utiles previas."
  ],
  "latex_rules": [
    "Usar plantilla .tex local de la materia como base.",
    "Conservar macros institucionales: documenttitle, coursename, coursecode, universityname.",
    "Mantener compatibilidad con espanol y formato letterpaper.",
    "No eliminar campos de portada; completar faltantes segun actividad.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y documentos de apoyo.",
    "Corregir nombres de archivo corruptos antes de compilar.",
    "Compilar sin errores criticos, sin referencias rotas y con acentos correctos."
  ],
  "bibliography_rules": [
    "Usar etapas-del-proceso-y-estrategia-del-litigio.bib como repositorio local canonico.",
    "Conservar fuentes institucionales existentes: unadmSitioWeb y unadmMallaDerecho2024.",
    "No inventar referencias; usar solo obras consultables y verificables.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Incluir metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Incluir fecha de consulta en fuentes web o institucionales dinamicas."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables en saltos transversales.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "No propagar redaccion literal ni metadatos hiperlocales de actividad.",
    "Mantener advertencia: ciclos con insumo no parseable requieren normalizacion manual.",
    "Aplicar propagacion recursiva solo tras validar JSON y no regresion."
  ],
  "open_questions": [
    "Confirmar si coursecode LDE-S5B2 es definitivo. [supuesto]",
    "Confirmar si documentauthor es fijo de plantilla o variable por estudiante. [supuesto]",
    "Confirmar estilo de citacion juridica requerido por docente (APA, Chicago, ISO 690 u otro).",
    "Confirmar checklist minimo por tipo de producto: reporte, presentacion, visual.",
    "Confirmar que no existan mas rutas con tokens Slug sin resolver en README/programa."
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
      "Problema juridico o social que activa la asignatura.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion transferible a la practica juridica."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos con fundamento juridico y evidencia.",
      "Garantizar entregables con criterio propio y utilidad profesional.",
      "Sostener continuidad editorial entre nodos sin perder especificidad local."
    ],
    "style_markers": [
      "Encuadre inicial breve del problema.",
      "Secciones claras y reutilizables.",
      "Afirmaciones con fuente o [supuesto].",
      "Cierre juridico transferible.",
      "Consistencia de portada y metadatos institucionales."
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
          "justification": "La identidad exige consistencia formal y citas verificables."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La secuencia metodologica culmina en cierre aplicable a practica."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Compresion union-dedupe sin perdida",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay deduplicacion segura ni trazable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Toda afirmacion debe ser comprobable o marcada como supuesto."
        }
      ],
      "evidence": [
        "README de materia: identidad UnADM, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "Archivo .bib local: claves institucionales existentes.",
        "Plantilla .tex local: macros institucionales y estructura base."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: se deduplican reglas repetidas y se conserva contenido util sin recorte.",
      "Ciclo 2: se refuerza gate de JSON parseable como requisito de propagacion.",
      "Ciclo 2: se mantiene separacion entre fuentes provisionales y autoridad academica.",
      "Ciclo 2: se consolidan conexiones transversales estables sin trasladar redaccion literal."
    ]
  }
}