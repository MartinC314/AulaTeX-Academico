{
  "summary": [
    "Memoria transversal consolidada para materia destino con estrategia conservadora y sin regresion.",
    "Se preservan reglas estables: identidad UnADM, cinco ejes editoriales, validacion JSON y union-dedupe lossless.",
    "Se agrega mejora verificable: corregir tokens sin resolver y caracteres corruptos en README/programa antes de propagar."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Conservar trazabilidad de origen editorial en cada consolidacion.",
    "Marcar como [supuesto] todo dato no visible en consigna o documentos locales.",
    "Mantener fuentes heredadas no verificadas como provisionales y fuera de autoridad academica."
  ],
  "structure_rules": [
    "Partir de problema juridico o social claro.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en bloques: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear estructura al producto solicitado por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Aplicar cinco ejes: problema, conceptos, producto, analisis propio y conclusion."
  ],
  "activity_rules": [
    "Verificar instruccion especifica de cada actividad antes de redactar.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Comprobar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Agregar fuentes especificas de actividad al .bib local antes de version final.",
    "No transferir redaccion literal desde nodos no equivalentes; solo abstracciones."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de fusionar memoria.",
    "Aplicar compresion lossless por union-dedupe sin eliminar reglas utiles previas.",
    "Confirmar que cada afirmacion factual tenga fuente o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Normalizar manualmente cualquier herencia no estructurada de ciclos previos."
  ],
  "latex_rules": [
    "Usar plantilla .tex local de la materia como base.",
    "Conservar macros institucionales: documenttitle, coursename, coursecode, universityname.",
    "Mantener compatibilidad con espanol y letterpaper de plantilla.",
    "No eliminar campos de portada; completar faltantes segun actividad.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir caracteres corruptos en nombres de archivo antes de referenciar."
  ],
  "bibliography_rules": [
    "Usar etapas-del-proceso-y-estrategia-del-litigio.bib como repositorio local canonico.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Incluir fecha de consulta en fuentes web o institucionales dinamicas.",
    "No citar bibliografia base si no fue usada en el argumento."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales y estables en nodos transversales.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "No propagar metadatos o artefactos especificos de actividad origen.",
    "Mantener advertencia activa: ciclos con salida no parseable requieren normalizacion manual.",
    "Propagar regla de validacion JSON y no regresion como minima institucional."
  ],
  "open_questions": [
    "Confirmar si documentauthor es fijo de plantilla o variable por estudiante. [supuesto]",
    "Confirmar estilo de citacion juridica requerido por la asignatura.",
    "Confirmar si coursecode LDE-S5B2 es definitivo institucionalmente. [supuesto]",
    "Verificar correccion final de nombres corruptos en README (reporte/referencias).",
    "Confirmar checklist minimo por tipo de producto: reporte, presentacion y visual."
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
      "Problema juridico o social.",
      "Fundamento conceptual y normativo.",
      "Analisis propio con criterio.",
      "Conclusion juridica aplicable.",
      "Persistencia editorial sin regresion."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos juridicos con evidencia y utilidad profesional.",
      "Mantener un cerebro editorial estable, verificable y reusable entre nodos."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Bloques argumentativos visibles.",
      "Citas trazables.",
      "Cierre juridico transferible.",
      "Supuestos marcados explicitamente."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis propio -> conclusion juridica.",
      "Afirmacion -> evidencia -> interpretacion -> implicacion practica.",
      "Consigna -> ejes editoriales -> producto alineado -> verificacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Cinco ejes editoriales",
        "JSON parseable",
        "Union-dedupe sin regresion",
        "Normalizacion estructurada",
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
          "source": "Union-dedupe sin regresion",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Preserva reglas utiles sin recorte."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Calidad argumentativa de entregables",
          "kind": "supports",
          "justification": "Estandariza estructura y profundidad juridica."
        },
        {
          "source": "Identidad UnADM",
          "target": "Coherencia institucional",
          "kind": "supports",
          "justification": "Mantiene tono, formato y trazabilidad."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Transferencia transversal",
          "kind": "develops",
          "justification": "Permite compartir abstracciones estables entre nodos no equivalentes."
        }
      ],
      "evidence": [
        "README de materia: ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "Bib local: claves institucionales existentes.",
        "Plantilla tex local: macros y coursecode visibles.",
        "Historial: salidas no parseables previas exigen gate de normalizacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 22: se preservan reglas vigentes y se deduplican sin perdida.",
      "Ciclo 22: se refuerza transferencia transversal por abstracciones, no por literalidad.",
      "Ciclo 22: se agrega mejora verificable de saneamiento de tokens/paths corruptos."
    ]
  }
}