{
  "summary": [
    "Se consolida sincronizacion transversal conservadora desde actividad de origen hacia materia destino.",
    "Se preservan reglas estables: identidad UnADM, estructura argumentativa juridica y control de supuestos.",
    "Se mantiene compresion lossless por union y deduplicacion sin eliminar reglas utiles previas.",
    "Se refuerza normalizacion obligatoria ante herencias no parseables de ciclos tempranos.",
    "Se evita transferir contenido tematico especifico de Filosofia del Derecho no reutilizable en electiva."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 8, bloque 2, tipo Electiva.",
    "Usar carpeta de materia como punto de entrada canonico.",
    "Conservar tono academico-juridico claro, preciso y argumentativo.",
    "Marcar como [supuesto] todo dato no confirmado en consigna o documentos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "Mantener autor y matricula confirmados en front matter: Martin Jonathan de la Cruz, ES2611202040."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener consistencia entre README, programa analitico, .tex y .bib."
  ],
  "activity_rules": [
    "Traducir cada consigna semanal al producto concreto solicitado.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Vincular conceptos, normas, doctrina o datos con el problema juridico tratado.",
    "Evitar traslado literal de contenidos de otra materia sin validacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar ausencia de placeholders o tokens sin expandir en README, programa, .tex y .bib.",
    "Verificar correspondencia del producto con la consigna local vigente."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Conservar plantilla base de la materia y metadatos institucionales.",
    "Actualizar titulo, subtitulo y numero real de actividad antes de compilar.",
    "Completar campos pendientes solo con datos confirmados; si no, marcar [supuesto].",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens tipo $(@{...}.Slug) a nombres literales de archivo.",
    "Corregir nombres truncados en estructura documental (ej. eporte, eferencias)."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas por actividad en electiva-semestre-8-bloque-2.bib.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Mantener trazabilidad entre afirmacion, cita en texto y clave BibTeX.",
    "[supuesto] Verificar politica local sobre year y fecha de consulta para @misc institucional."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas abstractas y estables entre nodos no equivalentes.",
    "Priorizar transferencia de identidad, gates de calidad, estructura reusable y grafo conceptual.",
    "No propagar redaccion literal ni contenido tematico dependiente de una actividad especifica.",
    "Mantener etiqueta de herencia provisional para fuentes no verificadas.",
    "Aplicar estrategia progresiva y conservadora: reforzar sin reemplazar reglas validas previas.",
    "Usar union-dedupe como mecanismo de consolidacion sin regresion."
  ],
  "open_questions": [
    "[supuesto] Confirmar creditos oficiales de la materia destino.",
    "[supuesto] Confirmar nombre oficial de figura docente para front matter.",
    "[supuesto] Confirmar si existe nombre oficial alterno de la electiva.",
    "[supuesto] Confirmar politica institucional de citacion para sitio UnADM (year y fecha de consulta).",
    "[supuesto] Confirmar si la materia requiere artefactos adicionales a reporte y presentacion."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador ante datos no confirmados."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Entrada canonica por carpeta de materia.",
        "Control explicito de supuestos."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 8, bloque 2, tipo Electiva.",
        "Codigo de curso LDE-S8B2.",
        "[supuesto] Creditos por confirmar."
      ]
    },
    "essence": [
      "Problema juridico.",
      "Conceptos y marco normativo.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible.",
      "Normalizacion estructurada antes de propagar."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables juridicos claros, verificables y utiles para practica profesional.",
      "Sostener coherencia editorial entre documentos de materia.",
      "Asegurar trazabilidad y rigor en cada actividad."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Secciones explicitas y ordenadas.",
      "Postura propia respaldada por fuentes.",
      "Cierre con transferencia profesional.",
      "Marcado explicito de [supuesto]."
    ],
    "argumentative_patterns": [
      "Problema -> objetivo -> marco conceptual/normativo -> analisis propio -> conclusion aplicada.",
      "Afirmacion relevante -> evidencia verificable -> interpretacion juridica.",
      "Evitar descripcion pura; priorizar razonamiento juridico."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Integridad academica",
        "Control de supuestos",
        "Trazabilidad cita-texto-bib",
        "Analisis juridico propio",
        "Conclusion juridica transferible",
        "Compresion union-dedupe"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva segura",
          "kind": "supports",
          "justification": "Evita heredar errores de formato y memoria no parseable."
        },
        {
          "source": "Integridad academica",
          "target": "Trazabilidad cita-texto-bib",
          "kind": "depends_on",
          "justification": "La verificabilidad exige correspondencia entre afirmaciones, citas y .bib."
        },
        {
          "source": "Analisis juridico propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion profesional surge del razonamiento del estudiante."
        },
        {
          "source": "Control de supuestos",
          "target": "Rigor editorial",
          "kind": "supports",
          "justification": "Diferencia datos confirmados de datos pendientes."
        }
      ],
      "evidence": [
        "README local: pauta editorial, ubicacion curricular y riesgos de placeholders.",
        "Programa analitico local: proposito y ejes de trabajo reutilizables.",
        "Archivo .bib local: claves institucionales base verificables.",
        "Memoria origen: regla estable de normalizacion y JSON parseable antes de propagacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 10: deduplicacion completa de reglas repetidas entre origen y destino.",
      "Ciclo 10: refuerzo de gates transversales de parseo JSON y normalizacion previa.",
      "Ciclo 10: transferencia conservadora de patrones argumentativos reutilizables.",
      "Ciclo 10: exclusion deliberada de contenido tematico especifico no transversal.",
      "Ciclo 10: consolidacion de ADN editorial minimo robusto para materia destino."
    ]
  }
}