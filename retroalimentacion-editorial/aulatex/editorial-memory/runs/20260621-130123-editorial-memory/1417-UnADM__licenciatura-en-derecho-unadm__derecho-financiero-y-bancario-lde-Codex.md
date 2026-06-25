{
  "summary": [
    "Sincronizacion transversal ciclo 3 aplicada con union-dedupe y sin regresion.",
    "Se preservan reglas estables de identidad UnADM, estructura argumentativa y control de calidad JSON.",
    "Se mantiene enfoque reusable: problema, conceptos/normas, evidencia, analisis propio y conclusion juridica transferible.",
    "Se refuerza normalizacion de artefactos de plantilla en README y programa analitico del destino.",
    "Se conservan vacios locales como preguntas abiertas con marca de supuesto."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares verificados del destino: semestre 3, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no confirmado en consigna local.",
    "Tratar fuentes heredadas de motor como provisionales hasta verificacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener coherencia entre README, programa analitico, .tex y .bib."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante y no solo descripcion.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar afirmaciones sin respaldo o sin marca de supuesto.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir fuentes de semanas distintas sin confirmacion de consigna."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar toda respuesta no estructurada antes de reutilizar.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar trazabilidad de cada regla a contexto local o memoria heredada.",
    "Validar deduplicacion semantica antes de guardar memoria.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Mantener codificacion y acentos correctos en español en .tex y .bib.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir de plantilla en nombres de archivo.",
    "Corregir artefactos de plantilla en README y programa analitico.",
    "Sincronizar titulo, subtitulo y materia con la actividad real antes de entrega."
  ],
  "bibliography_rules": [
    "Usar derecho-financiero-y-bancario.bib como archivo canonico de la materia.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Incluir fecha de consulta en referencias web.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferir redaccion literal o contenido tematico propio de otra asignatura.",
    "Aplicar normalizacion manual si reaparece salida no estructurada en ciclos previos."
  ],
  "open_questions": [
    "Supuesto: falta consigna semanal concreta de la siguiente actividad del destino.",
    "Confirmar figura docente y grupo para portada.",
    "Confirmar formato obligatorio de citacion de la materia.",
    "Confirmar si la localizacion institucional de portada debe actualizarse.",
    "Confirmar si los artefactos de plantilla del README se corrigen manualmente o por regeneracion."
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
        "Entrada canonica por carpeta de materia."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Derecho financiero y bancario.",
        "Semestre 3, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Conceptos y normas pertinentes.",
      "Evidencia verificable.",
      "Analisis juridico propio.",
      "Conclusion transferible a practica profesional."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos rigurosos y utiles.",
      "Asegurar consistencia editorial entre documentos fuente y entregables.",
      "Preservar calidad institucional con propagacion segura y trazable."
    ],
    "style_markers": [
      "Frases directas y verificables.",
      "Supuestos marcados en forma explicita.",
      "Sin fuentes inventadas.",
      "Coherencia entre estructura, argumento y evidencia."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Marco conceptual y normativo delimitado.",
      "Analisis propio sustentado.",
      "Cierre con implicacion practica juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "JSON parseable",
        "Evidencia verificable",
        "Analisis juridico propio",
        "Conclusion transferible",
        "Consistencia .tex-.bib"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "JSON parseable",
          "kind": "depends_on",
          "justification": "La propagacion segura requiere estructura valida."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis juridico propio",
          "kind": "supports",
          "justification": "El analisis gana validez cuando se sustenta con fuentes comprobables."
        },
        {
          "source": "Analisis juridico propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion profesional deriva del razonamiento argumentado."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Consistencia .tex-.bib",
          "kind": "supports",
          "justification": "La calidad institucional exige coherencia formal y bibliografica."
        }
      ],
      "evidence": [
        "README de materia: pauta editorial y ubicacion curricular.",
        "Programa analitico: proposito y ejes de trabajo.",
        "derecho-financiero-y-bancario.bib: fuentes base institucionales.",
        "Regla heredada: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 3: deduplicadas reglas repetidas en summary, estructura y quality gates.",
      "Ciclo 3: transferidas solo abstracciones estables desde actividad de Filosofia del Derecho.",
      "Ciclo 3: preservadas reglas utiles previas del destino sin eliminacion.",
      "Ciclo 3: reforzada trazabilidad y marca de supuestos para vacios locales."
    ]
  }
}