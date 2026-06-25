{
  "summary": [
    "Se consolida cerebro editorial minimo de materia con identidad UnADM y enfoque juridico contractual.",
    "Se preserva normalizacion obligatoria de salidas no estructuradas antes de toda propagacion.",
    "Se mantiene modelo transversal de cinco ejes: problema, conceptos, producto, analisis propio y conclusion juridica.",
    "Se refuerza deduplicacion lossless sin regresion de reglas utiles previas.",
    "Se corrige como regla tecnica la resolucion de placeholders tipo $(@{...}.Slug) en README y programa analitico."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares confirmados de la materia: semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Conservar enfoque disciplinar en derechos de los contratos y obligaciones.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como [supuesto] todo dato no visible en consigna local.",
    "Tratar herencias Codex o GPT-Pro no verificadas como provisionales."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear el entregable al producto de planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Mantener trazabilidad entre objetivo, evidencia, argumento y conclusion."
  ],
  "activity_rules": [
    "Explicitar postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y cierre.",
    "Distinguir bibliografia base de fuentes especificas por actividad.",
    "No trasladar contenido de otras materias sin adecuacion contractual."
  ],
  "quality_gates": [
    "Bloquear persistencia o propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregado y consigna de actividad.",
    "No degradar reglas utiles previas durante union-dedupe."
  ],
  "latex_rules": [
    "Usar plantilla base local de reporte o presentacion segun consigna.",
    "Mantener metadatos completos: curso, autor, universidad, ubicacion y subtitulo de actividad.",
    "Actualizar documenttitle y documentsubtitle al producto final.",
    "Usar espanol academico con acentos correctos en .tex y .bib.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver placeholders tipo $(@{...}.Slug) en nombres de archivo antes de compilar.",
    "Evitar comandos no estandar sin justificacion editorial."
  ],
  "bibliography_rules": [
    "Usar derechos-de-los-contratos-y-obligaciones.bib como archivo canonico local.",
    "Conservar y reutilizar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Agregar solo fuentes realmente consultables y verificables.",
    "No inventar referencias.",
    "Registrar metadatos minimos: autor, titulo, anio y fuente/editorial o URL.",
    "Priorizar fuentes institucionales UnADM, norma vigente y doctrina pertinente."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo abstracciones estables de identidad, estructura y calidad.",
    "Aplicar propagacion lateral solo tras validar compatibilidad disciplinar.",
    "Excluir metadatos especificos de materia al propagar a nodos no equivalentes.",
    "Mantener estrategia progresiva y conservadora en ciclo 1.",
    "Reforzar controles transversales de JSON, supuestos y trazabilidad de citas."
  ],
  "open_questions": [
    "Confirmar guia formal de citacion obligatoria para esta materia.",
    "Confirmar rubrica de evaluacion por actividad para ajustar profundidad argumentativa.",
    "Confirmar si presentacion comparte todos los metadatos del reporte.",
    "Confirmar alcance de fuentes: solo federales o tambien codigos locales segun actividad.",
    "Confirmar si existe formato institucional fijo para conclusion juridica."
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
      "Conceptos, normas y doctrina pertinentes.",
      "Producto solicitado por planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables.",
      "Asegurar consistencia entre forma editorial, evidencia y criterio juridico."
    ],
    "style_markers": [
      "Supuestos siempre etiquetados como [supuesto].",
      "Secciones funcionales y trazables.",
      "Cierre juridico aplicable a practica profesional."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Marco conceptual y normativo.",
      "Analisis propio sustentado.",
      "Conclusion juridica operativa."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Contratos",
        "Obligaciones",
        "Evidencia verificable",
        "Analisis juridico propio",
        "Conclusion transferible",
        "Normalizacion estructurada"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y formato consistente."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis juridico propio",
          "kind": "depends_on",
          "justification": "El analisis parte de una pregunta o conflicto delimitado."
        },
        {
          "source": "Analisis juridico propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion valida surge del razonamiento sustentado."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "supports",
          "justification": "Evita contaminar nodos con salidas no parseables."
        }
      ],
      "evidence": [
        "README de materia confirma ubicacion curricular y pauta editorial.",
        "Programa analitico confirma cinco ejes transversales.",
        "Archivo .bib local confirma entradas base institucionales."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin perdida semantica.",
      "Se conservaron controles de calidad heredados y se mantuvieron como transversales.",
      "Se evitaron traslados literales de contenido de Filosofia del Derecho.",
      "Se creo base minima robusta del destino por sincronizacion transversal conservadora."
    ]
  }
}