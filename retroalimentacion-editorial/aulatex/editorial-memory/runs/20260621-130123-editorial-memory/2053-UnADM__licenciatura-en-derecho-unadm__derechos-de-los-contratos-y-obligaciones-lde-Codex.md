{
  "summary": [
    "Se conserva ADN editorial UnADM con enfoque juridico contractual en materia destino.",
    "Se refuerza sincronizacion transversal por abstracciones estables: identidad, cinco ejes, calidad y trazabilidad.",
    "Se mantiene normalizacion obligatoria de salidas no estructuradas antes de propagacion recursiva.",
    "Se confirma regla tecnica de resolver placeholders tipo $(@{...}.Slug) en README y programa analitico.",
    "Se preserva compresion lossless por union-dedupe sin regresion de reglas utiles previas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares confirmados de la materia: semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Conservar enfoque disciplinar en contratos y obligaciones.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como [supuesto] todo dato no visible en consigna local.",
    "Tratar herencias no verificadas de Codex o GPT-Pro como provisionales."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el entregable al producto de la planeacion semanal.",
    "Mantener trazabilidad entre objetivo, evidencia, argumento y conclusion.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Explicitar postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y cierre.",
    "Distinguir bibliografia base de fuentes especificas por actividad.",
    "No trasladar contenido literal de otras materias sin adecuacion contractual."
  ],
  "quality_gates": [
    "Bloquear persistencia o propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "No degradar reglas utiles previas durante union-dedupe."
  ],
  "latex_rules": [
    "Usar plantilla base local de reporte o presentacion segun consigna.",
    "Mantener metadatos completos: curso, autor, universidad, ubicacion y subtitulo de actividad.",
    "Actualizar documenttitle y documentsubtitle al producto real antes de compilar.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver placeholders tipo $(@{...}.Slug) en nombres de archivo antes de compilar.",
    "Corregir rutas con caracteres anomalos detectados en README."
  ],
  "bibliography_rules": [
    "Usar derechos-de-los-contratos-y-obligaciones.bib como archivo canonico local.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Agregar solo fuentes realmente consultables y verificables.",
    "No inventar referencias.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Registrar fuentes especificas por actividad separadas de la base institucional."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas transversales estables, no redaccion literal.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Excluir metadatos de actividad origen por no equivalencia de nodo.",
    "Aplicar compatibilidad disciplinar antes de propagacion lateral.",
    "Mantener estrategia progresiva y conservadora en cada ciclo."
  ],
  "open_questions": [
    "[supuesto] Falta consigna puntual de primeras actividades de esta materia; confirmar productos exactos.",
    "Confirmar rubrica de evaluacion por actividad para calibrar profundidad argumentativa.",
    "Confirmar guia de citacion obligatoria (APA, juridica mexicana u otra).",
    "Confirmar alcance normativo por actividad: federal, local o mixto.",
    "Confirmar si presentacion comparte todos los metadatos del reporte."
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
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos trazables y utiles.",
      "Mantener calidad institucional y validez juridica en cada entrega."
    ],
    "style_markers": [
      "Supuestos etiquetados como [supuesto].",
      "Secciones funcionales y trazables.",
      "Cierre juridico operativo.",
      "Consistencia entre reporte, presentacion y .bib."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Marco conceptual y normativo.",
      "Analisis propio sustentado.",
      "Conclusion juridica aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Contratos",
        "Obligaciones",
        "Normalizacion estructurada",
        "Evidencia verificable",
        "Analisis juridico propio",
        "Conclusion transferible",
        "Cinco ejes editoriales transversales"
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
          "justification": "La identidad institucional exige trazabilidad y citas verificables."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis juridico propio",
          "kind": "depends_on",
          "justification": "El analisis valido parte de un conflicto delimitado."
        },
        {
          "source": "Analisis juridico propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion profesional surge del razonamiento sustentado."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "supports",
          "justification": "Evita contaminar memoria con salidas no parseables."
        },
        {
          "source": "Cinco ejes editoriales transversales",
          "target": "Calidad del entregable",
          "kind": "supports",
          "justification": "Aseguran coherencia entre objetivo, evidencia, analisis y cierre."
        }
      ],
      "evidence": [
        "README de materia confirma ubicacion curricular y pauta editorial.",
        "Programa analitico confirma cinco ejes transversales.",
        "Archivo .bib local confirma base institucional verificable.",
        "Se detectan placeholders $(@{...}.Slug) en README y programa analitico."
      ]
    },
    "reinforcement_log": [
      "Ciclo 8: deduplicacion completa de reglas repetidas en origen y destino.",
      "Ciclo 8: transferencia conservadora de abstracciones estables entre nodos no equivalentes.",
      "Ciclo 8: se preservan controles de JSON parseable y normalizacion previa.",
      "Ciclo 8: se refuerza compatibilidad disciplinar para propagacion transversal."
    ]
  }
}