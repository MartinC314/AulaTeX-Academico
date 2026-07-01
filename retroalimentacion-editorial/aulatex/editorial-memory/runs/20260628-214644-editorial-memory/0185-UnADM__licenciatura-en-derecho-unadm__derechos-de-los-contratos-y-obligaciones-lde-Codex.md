{
  "summary": [
    "Se consolida memoria transversal minima para la materia con identidad UnADM y enfoque juridico.",
    "Se preservan reglas estables de normalizacion estructurada y compresion por union-dedupe sin regresion.",
    "Se refuerzan ejes editoriales reutilizables: problema, conceptos, evidencia, analisis propio y conclusion juridica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares verificados: Licenciatura en Derecho, semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Conservar enfoque disciplinar en contratos y obligaciones.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como [supuesto] todo dato no visible en consigna local.",
    "Tratar herencias no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al tipo solicitado en la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener trazabilidad entre objetivo, evidencia, argumento y conclusion."
  ],
  "activity_rules": [
    "Adaptar cada entrega al producto requerido por la actividad.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y cierre.",
    "Evitar traslado literal desde otras materias sin adecuacion contractual."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No eliminar reglas utiles previas durante fusion por deduplicacion."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y metadatos institucionales completos.",
    "Usar espanol academico con acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Compilar sin errores criticos, referencias rotas ni placeholders.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Usar como .bib canonico derechos-de-los-contratos-y-obligaciones.bib [verificado]."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y normas o doctrina verificables.",
    "Registrar fuentes especificas por actividad en el .bib local de la materia.",
    "No inventar referencias.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas editoriales estables y transversales.",
    "Excluir redaccion literal y metadatos no compatibles en saltos laterales.",
    "Aplicar estrategia progresiva y conservadora: primero identidad y quality gates.",
    "Reforzar primero grafo conceptual reusable antes de detalles locales.",
    "Mantener control de ciclo con normalizacion manual cuando haya herencia ambigua."
  ],
  "open_questions": [
    "Confirmar guia formal de citacion juridica obligatoria para la materia.",
    "Confirmar rubrica por actividad para calibrar profundidad argumentativa.",
    "Confirmar si presentacion y reporte comparten metadatos obligatorios exactos.",
    "Confirmar uso esperado de legislacion federal, local o mixta segun actividad."
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
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 4, bloque 1, obligatoria, 8 creditos.",
        "Asignatura: Derechos de los contratos y obligaciones."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos juridicamente solidos.",
      "Garantizar fundamento, evidencia y criterio propio en cada entrega."
    ],
    "style_markers": [
      "Frases claras y verificables.",
      "Supuestos explicitados cuando falte contexto.",
      "Cierre con utilidad profesional juridica."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Marco conceptual y normativo.",
      "Analisis propio sustentado.",
      "Conclusion juridica aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema juridico",
        "Marco normativo y doctrinal",
        "Analisis argumentativo propio",
        "Conclusion transferible",
        "Contratos",
        "Obligaciones"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica con citas verificables",
          "kind": "supports",
          "justification": "La pauta local exige verificabilidad y formato institucional."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis argumentativo propio",
          "kind": "develops",
          "justification": "El analisis parte de una pregunta o conflicto definido."
        },
        {
          "source": "Marco normativo y doctrinal",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica debe derivar de fundamento verificable."
        },
        {
          "source": "Contratos",
          "target": "Obligaciones",
          "kind": "depends_on",
          "justification": "La materia articula ambas categorias como nucleo disciplinar."
        }
      ],
      "evidence": [
        "README de la materia: identidad UnADM, carpeta canonica, conclusion juridica con criterio propio.",
        "Programa analitico: cinco ejes de trabajo y proposito editorial.",
        "derechos-de-los-contratos-y-obligaciones.bib: base institucional verificable."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin perdida semantica.",
      "Se transfirieron solo abstracciones estables entre nodos no equivalentes.",
      "Se mantuvieron gates de JSON y normalizacion como control transversal.",
      "Se reforzo el grafo conceptual minimo del destino con evidencia local verificada."
    ]
  }
}