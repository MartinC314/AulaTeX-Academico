{
  "summary": [
    "Se consolida memoria transversal minima para Historia del Derecho en Mexico desde reglas estables de Actividad 1 de Filosofia del Derecho.",
    "Se preserva identidad UnADM y ubicacion curricular local verificable: semestre 1, bloque 1, obligatoria, 8 creditos.",
    "Se refuerza estructura reusable de cinco ejes: problema, conceptos/fuentes, producto, analisis propio y conclusion juridica.",
    "Se mantiene gate critico: bloquear propagacion de salidas no JSON parseables y normalizar antes de reutilizar.",
    "Se conserva estrategia conservadora: no transferir contenido tematico especifico de Filosofia sin evidencia local."
  ],
  "identity_rules": [
    "Mantener tono institucional UnADM en portada, metadatos y redaccion.",
    "Usar nombre oficial local de la materia: Historia del Derecho en Mexico.",
    "Conservar contexto curricular local verificado desde README y programa analitico.",
    "Tratar fuentes heredadas no verificadas como provisionales.",
    "Marcar como [supuesto] todo dato no visible en la consigna local."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como entrada canonica.",
    "Iniciar cada entrega con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado en planeacion semanal."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar resumen solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "No asumir fuentes o consignas de semanas distintas sin confirmacion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que cada afirmacion sustantiva tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar compresion lossless por union-dedupe sin eliminar reglas utiles previas."
  ],
  "latex_rules": [
    "Usar plantillas locales de reporte o presentacion segun consigna.",
    "Conservar metadatos institucionales y curriculares; actualizar solo campos variables de actividad.",
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Resolver placeholders de Slug sin expandir antes de compilar o citar.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Usar historia-del-derecho-en-mexico.bib como repositorio local canonico.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Registrar en .bib solo fuentes realmente consultadas.",
    "No inventar referencias.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas transversales estables, no redaccion literal.",
    "Priorizar identidad, gates de calidad y patron argumentativo de cinco ejes.",
    "No propagar datos curriculares especificos a nodos laterales no equivalentes.",
    "Si un nodo destino esta incompleto, crear memoria minima y abrir vacios locales.",
    "Mantener alerta historica de salidas no parseables en ciclos tempranos."
  ],
  "open_questions": [
    "Confirmar acentuacion oficial institucional de Mexico/México en nombres visibles.",
    "Confirmar si LDE-S1B1 es codigo oficial o solo de plantilla [supuesto].",
    "Definir nombre oficial de figura docente en plantillas.",
    "Corregir artefactos de render en README (eporte/eferencias) [supuesto].",
    "Confirmar consignas y rubricas por actividad para granularidad local."
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
        "Historia del Derecho en Mexico.",
        "Semestre 1, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico claro.",
      "Conceptos y fuentes pertinentes.",
      "Producto alineado a consigna.",
      "Analisis propio sustentado.",
      "Conclusion juridica aplicable."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico y utilidad profesional.",
      "Sostener continuidad editorial entre actividades, materia y nivel institucional.",
      "Evitar regresiones de calidad en flujos de memoria automatizada."
    ],
    "style_markers": [
      "Frases directas y verificables.",
      "Separacion explicita entre hechos y supuestos.",
      "Citas trazables y consistentes con .bib."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Marco conceptual y normativo pertinente.",
      "Analisis propio con postura explicita.",
      "Contraste entre fuentes cuando aplique.",
      "Cierre con implicacion juridica concreta."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Cinco ejes editoriales",
        "Integridad academica",
        "Normalizacion JSON",
        "Trazabilidad bibliografica",
        "Conclusion juridica transferible"
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
          "justification": "La identidad institucional exige trazabilidad y verificabilidad."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La secuencia problema-analisis-cierre conduce a aplicacion profesional."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia confiable."
        },
        {
          "source": "Trazabilidad bibliografica",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Las citas verificables sostienen afirmaciones sustantivas."
        }
      ],
      "evidence": [
        "README de materia: pauta editorial y ubicacion curricular.",
        "Programa analitico: proposito y cinco ejes.",
        "historia-del-derecho-en-mexico.bib: base institucional verificable.",
        "Plantilla LaTeX local: metadatos institucionales y curriculares."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas equivalentes sin recorte semantico.",
      "Se transfirieron solo abstracciones estables entre nodos transversales.",
      "Se evitaron conceptos tematicos especificos de Filosofia no verificados en Historia.",
      "Se fortalecio el gate de JSON parseable por historial de fallos previos.",
      "Se creo cerebro editorial minimo util para propagacion recursiva conservadora."
    ]
  }
}