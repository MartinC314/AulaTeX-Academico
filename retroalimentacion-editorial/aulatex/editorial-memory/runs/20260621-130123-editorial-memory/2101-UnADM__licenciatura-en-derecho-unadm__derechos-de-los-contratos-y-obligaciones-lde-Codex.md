{
  "summary": [
    "Se conserva base editorial UnADM y se refuerza para sincronizacion transversal en materia.",
    "Se mantiene normalizacion obligatoria de salidas no estructuradas antes de propagar.",
    "Se preserva modelo reusable de cinco ejes: problema, conceptos, producto, analisis propio y conclusion juridica.",
    "Se transfiere solo abstraccion estable desde Filosofia del Derecho, sin contenido tematico literal.",
    "Se confirma destino con cerebro editorial minimo operativo y vacios locales abiertos como [supuesto]."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares confirmados: semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Conservar enfoque juridico aplicado a contratos y obligaciones.",
    "Usar coursecode LDE-S4B1 cuando la plantilla lo requiera.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como [supuesto] todo dato no visible en consigna local.",
    "Tratar herencias Codex o GPT-Pro no verificadas como provisionales."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el entregable al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Mantener trazabilidad entre objetivo, evidencia, argumento y conclusion."
  ],
  "activity_rules": [
    "Adaptar cada actividad al formato solicitado: reporte, presentacion o producto visual.",
    "Explicitar postura argumentada del estudiante y evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y cierre.",
    "Distinguir bibliografia base de fuentes especificas por actividad.",
    "No trasladar contenido de otras materias sin adecuacion contractual."
  ],
  "quality_gates": [
    "Bloquear persistencia y propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar toda herencia no estructurada antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar correspondencia entre citas en texto y archivo .bib local.",
    "Corregir placeholders tipo $(@{...}.Slug) en README y programa analitico antes de compilar.",
    "No degradar reglas utiles previas durante union-dedupe."
  ],
  "latex_rules": [
    "Usar plantilla base local segun consigna y mantener metadatos completos.",
    "Mantener curso, autor, universidad, ubicacion y subtitulo de actividad consistentes.",
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Usar nombres de archivo canonicos y resolver rutas con caracteres anómalos."
  ],
  "bibliography_rules": [
    "Usar derechos-de-los-contratos-y-obligaciones.bib como archivo canonico local.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Registrar en .bib solo fuentes realmente consultables y verificables.",
    "No inventar referencias.",
    "Conservar metadatos minimos: autor, titulo, año, fuente editorial o URL.",
    "Priorizar fuentes institucionales UnADM, normativa y jurisprudencia verificable según actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas transversales estables.",
    "Excluir detalles tematicos propios de Filosofia del Derecho en nodos de contratos.",
    "Aplicar transferencia lateral solo tras validar compatibilidad disciplinar.",
    "Mantener estrategia progresiva y conservadora con union-dedupe lossless.",
    "Si un nodo destino carece de contexto, inyectar cerebro minimo y dejar vacios en open_questions."
  ],
  "open_questions": [
    "[supuesto] Falta guia formal de citacion juridica obligatoria para esta materia.",
    "[supuesto] Falta rubrica por actividad para calibrar profundidad argumentativa.",
    "[supuesto] Falta confirmar alcance de fuentes: federales, locales o mixtas por actividad.",
    "[supuesto] Falta confirmar si presentacion comparte todos los metadatos del reporte."
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
      "Resolver problemas juridicos con estructura argumentativa trazable.",
      "Integrar norma, doctrina, evidencia y criterio propio.",
      "Cerrar con utilidad profesional transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos validos y verificables.",
      "Preservar coherencia institucional y calidad tecnica LaTeX.",
      "Sostener memoria editorial persistente sin regresion."
    ],
    "style_markers": [
      "Supuestos siempre etiquetados como [supuesto].",
      "Secciones funcionales y no ornamentales.",
      "Conclusion juridica operativa, no solo recapitulativa."
    ],
    "argumentative_patterns": [
      "Problema delimitado al inicio.",
      "Marco conceptual y normativo pertinente.",
      "Analisis propio sustentado con evidencia.",
      "Conclusion juridica aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalizacion estructurada",
        "Cinco ejes editoriales",
        "Integridad academica",
        "Analisis juridico propio",
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
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "supports",
          "justification": "Evita contaminar nodos con salidas no parseables."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Analisis juridico propio",
          "kind": "develops",
          "justification": "La estructura obliga postura y razonamiento verificable."
        },
        {
          "source": "Analisis juridico propio",
          "target": "Conclusion transferible",
          "kind": "depends_on",
          "justification": "La conclusion valida nace del razonamiento sustentado."
        },
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y consistencia formal."
        },
        {
          "source": "Contratos",
          "target": "Obligaciones",
          "kind": "develops",
          "justification": "El enfoque disciplinar de la materia exige tratamiento conjunto."
        }
      ],
      "evidence": [
        "README de materia confirma ubicacion curricular y pauta editorial.",
        "Programa analitico confirma ejes transversales de trabajo.",
        ".bib local confirma base institucional minima verificable.",
        "Origen aporta regla estable de normalizacion previa a propagacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 20: deduplicacion aplicada sin recorte semantico.",
      "Ciclo 20: se refuerza gate JSON parseable como bloqueo duro.",
      "Ciclo 20: se preserva transferencia transversal por abstracciones estables.",
      "Ciclo 20: se evita migrar contenido tematico literal de Filosofia del Derecho."
    ]
  }
}