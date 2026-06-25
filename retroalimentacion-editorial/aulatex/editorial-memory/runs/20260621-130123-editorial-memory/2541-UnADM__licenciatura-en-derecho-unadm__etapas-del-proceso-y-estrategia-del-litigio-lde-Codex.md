{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia progresiva y conservadora.",
    "Se preservan reglas validas del destino y se integran abstracciones estables del origen.",
    "Se mantiene compresion lossless por union-dedupe sin regresion.",
    "Se refuerza el nucleo: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene bloqueo de propagacion ante salida no JSON parseable.",
    "Se conserva trazabilidad de fuentes provisionales como notas tecnicas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Usar tono academico-juridico formal, claro y verificable.",
    "Exigir postura propia sustentada en cada entrega.",
    "Marcar como [supuesto] todo dato no visible en consigna o documentos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Registrar origen editorial de cada consolidacion para trazabilidad."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar bloques: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear estructura al producto solicitado en la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Aplicar cinco ejes: problema, conceptos, producto, analisis propio, conclusion."
  ],
  "activity_rules": [
    "Verificar instruccion especifica de actividad antes de redactar.",
    "Rubricar cada entrega contra los cinco ejes del programa analitico.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Integrar evidencia trazable en el cuerpo del trabajo.",
    "Agregar fuentes especificas de actividad al .bib local antes de version final.",
    "No asumir fuentes de otras semanas sin validacion de pertinencia."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de fusionar memoria.",
    "Confirmar que no haya afirmaciones factuales sin fuente o sin marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Comprobar union-dedupe sin eliminar reglas utiles previas.",
    "Revisar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Validar correspondencia del producto con la consigna local vigente."
  ],
  "latex_rules": [
    "Usar plantilla .tex local como base del producto.",
    "Conservar macros institucionales: documenttitle, coursename, coursecode, universityname.",
    "Mantener compatibilidad en espanol y letterpaper segun plantilla.",
    "No eliminar campos de portada; completar faltantes segun actividad.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir caracteres anomales en rutas y nombres antes de compilar. [supuesto]",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico. [supuesto]"
  ],
  "bibliography_rules": [
    "Usar etapas-del-proceso-y-estrategia-del-litigio.bib como repositorio local.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Incluir fecha de consulta en fuentes web o institucionales dinamicas.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No citar bibliografia no utilizada en el argumento."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales y estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "No propagar redaccion literal de actividades.",
    "Mantener metadatos especificos anclados al nodo destino.",
    "Si un nodo vecino esta vacio, inyectar cerebro minimo con gates de JSON y cinco ejes.",
    "Propagar advertencia de normalizacion manual para memorias historicas no parseables."
  ],
  "open_questions": [
    "Confirmar estilo de citacion juridica requerido por la asignatura.",
    "Confirmar si documentauthor es fijo de plantilla o variable por estudiante. [supuesto]",
    "Confirmar correccion de nombres corruptos en README (prefijos truncados). [supuesto]",
    "Confirmar existencia operativa de plantilla de presentacion en todos los flujos.",
    "Confirmar si coursecode LDE-S5B2 requiere ajuste institucional. [supuesto]"
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Juridicamente preciso.",
        "Claro, verificable y argumentativo."
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
      "Resolver problemas juridicos con fundamento verificable.",
      "Estructurar entregas con cinco ejes editoriales.",
      "Exigir analisis propio y cierre juridico transferible.",
      "Mantener normalizacion estructurada antes de propagar."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos solidos.",
      "Asegurar calidad editorial persistente y reusable.",
      "Evitar regresiones en memoria institucional."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Bloques argumentativos visibles.",
      "Citas trazables.",
      "Cierre juridico aplicable.",
      "Marcado explicito de [supuesto] cuando falte evidencia local."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis propio -> conclusion juridica.",
      "Afirmacion -> evidencia -> interpretacion -> implicacion practica.",
      "Consigna -> desarrollo alineado -> verificacion de rubrica -> cierre transferible."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Cinco ejes editoriales",
        "JSON parseable",
        "Normalizacion estructurada",
        "Union-dedupe sin regresion",
        "Conclusion juridica transferible",
        "Evidencia verificable",
        "Fuentes provisionales"
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
          "justification": "La fusion segura requiere estructura valida."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "supports",
          "justification": "Evita contaminar nodos con salidas no confiables."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La secuencia editorial conduce a cierre aplicable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Sustenta afirmaciones y evita especulacion."
        },
        {
          "source": "Fuentes provisionales",
          "target": "Autoridad academica",
          "kind": "contrasts",
          "justification": "No sustituyen fuentes confirmadas."
        }
      ],
      "evidence": [
        "README de materia: ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y cinco ejes.",
        "Bib local con unadmSitioWeb y unadmMallaDerecho2024.",
        "Regla historica: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 20: se refuerzan abstracciones estables transversales desde actividad origen.",
      "Ciclo 20: se preservan reglas locales de materia sin eliminar activos previos.",
      "Ciclo 20: se depuran duplicados semanticos por union-dedupe lossless.",
      "Ciclo 20: se mantiene separacion entre fuentes provisionales y autoridad academica."
    ]
  }
}