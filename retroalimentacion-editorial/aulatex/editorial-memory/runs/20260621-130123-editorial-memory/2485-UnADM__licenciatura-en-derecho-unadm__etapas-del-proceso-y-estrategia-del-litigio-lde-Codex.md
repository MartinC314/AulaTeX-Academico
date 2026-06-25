{
  "summary": [
    "Se consolida sincronizacion transversal ciclo 6 con compresion lossless por union-dedupe.",
    "Se preservan reglas estables de identidad UnADM, estructura reusable y control de calidad.",
    "Se transfiere solo abstraccion editorial entre nodos no equivalentes.",
    "Se mantiene bloqueo de propagacion para salidas no JSON parseable.",
    "Se refuerza uso de cinco ejes: problema, conceptos, producto, analisis propio y conclusion juridica.",
    "Se conserva trazabilidad de fuentes provisionales como nota tecnica, no autoridad academica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Usar tono academico-juridico formal, claro y argumentativo.",
    "Exigir postura propia sustentada.",
    "Marcar como [supuesto] todo dato no visible en consigna o documentos locales.",
    "Conservar trazabilidad de origen editorial en cada fusion de memoria.",
    "Registrar fuentes heredadas no verificadas como provisionales."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear estructura al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Aplicar checklist por cinco ejes del programa analitico."
  ],
  "activity_rules": [
    "Verificar instruccion especifica de cada actividad antes de redactar.",
    "Rubricar cada entrega contra los cinco ejes editoriales.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Agregar fuentes especificas de actividad al .bib local antes de version final.",
    "No asumir pertinencia de fuentes de otras semanas o materias.",
    "Validar correspondencia entre pregunta guia, desarrollo y conclusion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de fusionar memoria.",
    "Aplicar union-dedupe sin eliminar reglas utiles previas.",
    "Confirmar que cada afirmacion factual tenga fuente o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar y normalizar salidas no estructuradas antes de reutilizar.",
    "Evitar contradicciones con reglas institucionales vigentes."
  ],
  "latex_rules": [
    "Usar plantilla .tex local de la materia como base.",
    "Conservar macros institucionales: documenttitle, coursename, coursecode, universityname.",
    "Mantener compatibilidad con espanol y letterpaper.",
    "No eliminar campos de portada; completar faltantes segun actividad.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir caracteres anomalos en rutas y nombres de archivo.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico."
  ],
  "bibliography_rules": [
    "Usar etapas-del-proceso-y-estrategia-del-litigio.bib como repositorio local.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias.",
    "Registrar solo obras realmente consultables.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Incluir fecha de consulta en fuentes web o institucionales dinamicas.",
    "Distinguir bibliografia base y bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales y estables.",
    "No propagar redaccion literal de actividades entre nodos no equivalentes.",
    "Priorizar propagacion de identidad, estructura reusable, quality gates y grafo conceptual.",
    "Mantener metadatos especificos solo en su nodo local.",
    "Marcar ciclos heredados no parseables como candidatos a normalizacion manual."
  ],
  "open_questions": [
    "Confirmar si documentauthor debe ser fijo o variable por estudiante. [supuesto]",
    "Confirmar estilo de citacion juridica requerido por la asignatura.",
    "Confirmar correccion definitiva de nombres con caracteres corruptos en README.",
    "Confirmar si coursecode LDE-S5B2 requiere ajuste institucional. [supuesto]",
    "Confirmar checklist minimo por tipo de producto: reporte, presentacion, visual."
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
      "Identidad institucional consistente.",
      "Cinco ejes editoriales como columna vertebral.",
      "Normalizacion estructurada antes de propagar.",
      "Compresion lossless por union-dedupe sin regresion."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos rigurosos y transferibles.",
      "Garantizar fundamento juridico, evidencia verificable y postura propia."
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
        "Trazabilidad de fuentes"
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
          "justification": "Conserva reglas utiles sin perdida."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Calidad del entregable",
          "kind": "supports",
          "justification": "Ordenan contenido, analisis y cierre juridico."
        },
        {
          "source": "Identidad UnADM",
          "target": "Coherencia institucional",
          "kind": "supports",
          "justification": "Asegura tono, formato y metadatos consistentes."
        }
      ],
      "evidence": [
        "README de materia: ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y ejes de trabajo.",
        "Bib local: claves institucionales verificables.",
        "Plantilla .tex local: macros y coursecode visible."
      ]
    },
    "reinforcement_log": [
      "Ciclo 6: deduplicacion completa de reglas repetidas.",
      "Ciclo 6: refuerzo de gates JSON y normalizacion previa.",
      "Ciclo 6: transferencia transversal limitada a abstracciones estables.",
      "Ciclo 6: preservacion de ADN editorial sin recorte semantico."
    ]
  }
}