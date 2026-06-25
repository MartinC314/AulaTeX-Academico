{
  "summary": [
    "Se preserva la identidad UnADM y el enfoque juridico contractual de la materia.",
    "Se refuerza la normalizacion obligatoria de salidas no estructuradas antes de propagar.",
    "Se consolida el modelo transversal de cinco ejes: problema, conceptos, producto, analisis propio y conclusion juridica.",
    "Se mantiene compresion lossless por union-dedupe sin regresion de reglas utiles.",
    "Se confirma la carpeta de materia como entrada canonica para .tex, .bib y programa analitico.",
    "Se conserva la regla tecnica de resolver placeholders tipo $(@{...}.Slug) en README y programa analitico."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares confirmados: semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Conservar enfoque disciplinar en derechos de los contratos y obligaciones.",
    "Usar codigo de curso LDE-S4B1 cuando la plantilla lo requiera.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna local.",
    "Tratar herencias no verificadas de Codex o GPT-Pro como provisionales."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el entregable al producto solicitado por la planeacion semanal.",
    "Mantener trazabilidad entre objetivo, evidencia, argumento y conclusion.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Distinguir bibliografia base y fuentes especificas por actividad."
  ],
  "activity_rules": [
    "Adaptar cada actividad al formato exigido en consigna.",
    "Explicitar postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y cierre.",
    "No trasladar contenido de otras materias sin adecuacion contractual.",
    "Marcar [supuesto] cuando falte instruccion especifica.",
    "Confirmar que el producto final corresponde a la actividad vigente."
  ],
  "quality_gates": [
    "Bloquear persistencia o propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Validar compatibilidad disciplinar antes de propagacion lateral.",
    "No degradar reglas utiles previas durante union-dedupe."
  ],
  "latex_rules": [
    "Usar plantilla local de reporte o presentacion segun consigna.",
    "Mantener metadatos completos: curso, autor, universidad, ubicacion y subtitulo de actividad.",
    "Actualizar documenttitle y documentsubtitle al producto real antes de compilar.",
    "Usar espanol academico con acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Compilar sin errores criticos ni referencias indefinidas.",
    "Resolver placeholders tipo $(@{...}.Slug) en README y programa analitico antes de referenciar archivos."
  ],
  "bibliography_rules": [
    "Usar derechos-de-los-contratos-y-obligaciones.bib como archivo canonico local.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Registrar fuentes especificas de cada actividad en el .bib local.",
    "Priorizar fuentes institucionales UnADM y documentos juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Declarar [supuesto] si una referencia obligatoria no esta disponible."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas editoriales estables y transversales.",
    "Evitar transferir redaccion literal o contenido tematico de Filosofia del Derecho.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Excluir metadatos especificos cuando el nodo destino lateral no coincida.",
    "Aplicar normalizacion manual a ciclos heredados con salida no estructurada."
  ],
  "open_questions": [
    "Confirmar rubrica de evaluacion por actividad en esta materia.",
    "Confirmar guia formal de citacion juridica obligatoria.",
    "Confirmar alcance normativo por actividad: federal, local o mixto.",
    "Confirmar si presentacion comparte todos los metadatos del reporte.",
    "Supuesto: autor por defecto y ubicacion institucional se mantienen hasta instruccion contraria."
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
      "Problema juridico delimitado.",
      "Base conceptual y normativa pertinente.",
      "Producto alineado a planeacion.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Guiar productos academicos consistentes, verificables y utiles para practica juridica.",
      "Convertir planeacion semanal en entregables con trazabilidad argumentativa."
    ],
    "style_markers": [
      "Supuestos etiquetados como [supuesto].",
      "Secciones funcionales y trazables.",
      "Cierre juridico operativo.",
      "Consistencia entre reporte, presentacion y bibliografia."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Marco conceptual-normativo.",
      "Analisis propio con evidencia.",
      "Conclusion juridica aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalizacion estructurada",
        "Problema juridico",
        "Analisis juridico propio",
        "Conclusion transferible",
        "Contratos",
        "Obligaciones",
        "Evidencia verificable"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "La pauta institucional exige integridad academica y citas verificables."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis juridico propio",
          "kind": "depends_on",
          "justification": "El analisis requiere una pregunta o conflicto delimitado."
        },
        {
          "source": "Analisis juridico propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion valida surge del razonamiento sustentado."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "Evita propagar contenido sin control de calidad."
        },
        {
          "source": "Contratos",
          "target": "Obligaciones",
          "kind": "develops",
          "justification": "Son ejes disciplinares complementarios de la materia."
        }
      ],
      "evidence": [
        "README de materia confirma ubicacion curricular y pauta editorial.",
        "Programa analitico confirma cinco ejes transversales.",
        "Archivo .bib local confirma entradas institucionales base.",
        "Se detectaron placeholders tipo $(@{...}.Slug) en README y programa analitico."
      ]
    },
    "reinforcement_log": [
      "Ciclo 17: deduplicacion completa de reglas repetidas sin perdida semantica.",
      "Ciclo 17: transferencia transversal conservadora desde actividad no equivalente aplicada solo a abstracciones estables.",
      "Ciclo 17: se preservan controles de JSON parseable y normalizacion previa.",
      "Ciclo 17: se evita importar contenido doctrinal especifico de Filosofia del Derecho al dominio contractual."
    ]
  }
}