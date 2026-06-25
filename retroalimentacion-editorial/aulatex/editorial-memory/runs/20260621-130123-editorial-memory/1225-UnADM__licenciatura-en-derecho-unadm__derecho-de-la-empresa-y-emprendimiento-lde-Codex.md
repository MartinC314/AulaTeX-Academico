{
  "summary": [
    "Se consolida sincronizacion transversal con transferencia de abstracciones estables.",
    "Se preservan reglas utiles previas sin regresion y con deduplicacion lossless.",
    "Se refuerza marco reusable: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene normalizacion estructurada obligatoria antes de propagacion recursiva.",
    "Se conserva alerta local por tokens Slug sin expandir y nombres de archivo con artefactos.",
    "Se evita transferir contenido doctrinal especifico de Filosofia del Derecho al nodo no equivalente."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial de la materia destino en todos los artefactos.",
    "Usar Licenciatura en Derecho como programa academico.",
    "Respetar contexto curricular local confirmado: semestre 6, bloque 2, obligatoria, 8 creditos.",
    "Usar codigo LDE-S6B2 cuando la plantilla lo requiera.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no confirmado por consigna o archivo local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar desarrollo en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el entregable al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Conservar correspondencia entre README, programa analitico, .tex y .bib.",
    "Resolver placeholders y tokens sin expandir en archivos de estructura antes de publicar."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Incluir conclusion juridica con criterio propio y aplicacion practica.",
    "Agregar fuentes especificas de cada actividad al .bib local.",
    "No asumir fuentes de otras semanas o materias sin confirmacion."
  ],
  "quality_gates": [
    "Bloquear consolidacion o propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar memoria.",
    "No eliminar reglas utiles previas durante fusion por union-dedupe.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y claves en .bib.",
    "Verificar que README liste archivos reales y rutas existentes.",
    "Corregir placeholders visibles antes de generar entregables.",
    "Aplicar normalizacion manual cuando existan antecedentes de salida no estructurada."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener consistencia de metadatos de curso y licenciatura en macros.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo con saltos o caracteres anómalos antes de compilar.",
    "Verificar integridad sintactica del .tex primario y cierre de entornos."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo obras verificables.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos pertinentes a la materia.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Registrar fuentes especificas en derecho-de-la-empresa-y-emprendimiento.bib.",
    "No citar fuentes no agregadas al .bib local.",
    "Mantener unadmSitioWeb y unadmMallaDerecho2024 como base local hasta nueva evidencia."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales validadas y no dependientes de disciplina especifica.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual estable.",
    "No propagar datos curriculares locales a otros nodos sin confirmacion local.",
    "Propagar alerta de salida no estructurada y necesidad de normalizacion manual.",
    "Propagar alerta de tokens Slug sin expandir a nodos con plantillas similares.",
    "Mantener estrategia progresiva y conservadora: agregar mejoras verificables sin recortar memoria util."
  ],
  "open_questions": [
    "Supuesto: falta consigna de actividad concreta en materia destino para ajustar artefacto final.",
    "Confirmar si documentauthor de plantilla debe parametrizarse por actividad.",
    "Confirmar valor expandido final del Slug en README y programa analitico.",
    "Confirmar correccion de nombres truncados en README (reporte y referencias).",
    "Confirmar si year=2026 en unadmSitioWeb se mantiene como anio bibliografico o solo consulta.",
    "Confirmar estado completo del .tex primario por posible truncamiento."
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
        "Integridad academica con trazabilidad bibliografica.",
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 6, bloque 2, obligatoria, 8 creditos.",
        "Enfoque en transferencia profesional."
      ]
    },
    "essence": [
      "Problema juridico claro.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible.",
      "Control explicito de supuestos."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables juridicos solidos y verificables.",
      "Asegurar coherencia entre identidad institucional, metodo argumentativo y evidencia.",
      "Permitir propagacion segura de reglas editoriales entre nodos."
    ],
    "style_markers": [
      "Frases directas y accionables.",
      "Sin afirmaciones sin fuente.",
      "Supuestos siempre etiquetados.",
      "Cierre con aplicacion practica."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis propio -> conclusion.",
      "Marco normativo como soporte de la postura.",
      "Coherencia total entre pregunta guia y cierre."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Problema juridico",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Integridad bibliografica",
        "Control de supuestos",
        "Tokens Slug sin expandir"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin salida estructurada no hay transferencia segura."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "El cierre juridico exige sustento documental."
        },
        {
          "source": "Control de supuestos",
          "target": "Integridad argumentativa",
          "kind": "supports",
          "justification": "Distingue hechos confirmados de inferencias."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura de entregables",
          "kind": "supports",
          "justification": "Fija tono, formato y criterios comunes."
        },
        {
          "source": "Tokens Slug sin expandir",
          "target": "Calidad de artefactos",
          "kind": "contrasts",
          "justification": "Generan errores de ruta y trazabilidad si no se corrigen."
        }
      ],
      "evidence": [
        "README local de materia con pauta editorial y ubicacion curricular.",
        "Programa analitico local con proposito y ejes de trabajo.",
        "Archivo .bib local con claves institucionales verificables.",
        "Memoria origen valida para reglas transversales de estructura y calidad."
      ]
    },
    "reinforcement_log": [
      "Ciclo 21: se conserva ADN institucional y se deduplican reglas repetidas.",
      "Ciclo 21: se agregan gates de consistencia cita-texto y control de supuestos.",
      "Ciclo 21: se refuerza no transferencia de doctrina especifica entre materias no equivalentes.",
      "Ciclo 21: se mantiene alerta operativa por JSON no parseable y placeholders Slug."
    ]
  }
}