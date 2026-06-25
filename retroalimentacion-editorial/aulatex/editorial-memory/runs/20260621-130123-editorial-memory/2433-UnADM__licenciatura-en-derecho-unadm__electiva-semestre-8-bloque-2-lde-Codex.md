{
  "summary": [
    "Se sincroniza memoria transversal desde actividad de Filosofia del Derecho hacia materia Electiva S8B2 sin mover contenido tematico no verificable.",
    "Se preserva identidad UnADM, estructura argumentativa juridica y control de supuestos como reglas estables.",
    "Se refuerza normalizacion obligatoria: no propagar salidas no JSON parseable.",
    "Se mantiene compresion lossless por union-dedupe y sin regresion de reglas utiles.",
    "Se consolida gate operativo transversal: corregir placeholders y nombres truncados antes de compilar o propagar."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 8, bloque 2, tipo Electiva.",
    "Usar la carpeta de materia como entrada canonica.",
    "Mantener autor y matricula confirmados en front matter: Martin Jonathan de la Cruz, ES2611202040.",
    "Marcar como [supuesto] todo dato no confirmado en consigna o documentos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al tipo solicitado en planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener consistencia entre README, programa analitico, .tex y .bib."
  ],
  "activity_rules": [
    "Traducir cada consigna semanal a producto concreto solicitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar resumen descriptivo puro.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No transferir contenido especifico de otra asignatura sin validacion local.",
    "No asumir fuentes de semanas o actividades distintas."
  ],
  "quality_gates": [
    "Bloquear consolidacion o propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar trazabilidad entre afirmaciones, citas en texto y .bib.",
    "Confirmar que toda afirmacion sin respaldo este marcada como [supuesto].",
    "Verificar correspondencia del producto con la consigna vigente.",
    "Corregir placeholders visibles y tokens sin expandir en README, programa, .tex y .bib."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Actualizar titulo, subtitulo y numero real de actividad antes de compilar.",
    "Resolver tokens tipo $(@{...}.Slug) a nombres literales de archivo.",
    "Corregir nombres truncados en estructura (ej. eporte, eferencias)."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Registrar fuentes especificas por actividad en electiva-semestre-8-bloque-2.bib.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Mantener correspondencia 1:1 entre cita en texto y clave BibTeX."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas abstractas estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferencia de redaccion literal y de contenido tematico local del origen.",
    "Mantener etiqueta de herencia provisional cuando la fuente historica no fue JSON parseable.",
    "Aplicar estrategia conservadora: primero normalizar, luego expandir."
  ],
  "open_questions": [
    "[supuesto] Confirmar creditos oficiales de la materia para metadatos finales.",
    "[supuesto] Confirmar nombre oficial de figura docente.",
    "[supuesto] Confirmar politica institucional sobre year y fecha de consulta en @misc.",
    "[supuesto] Confirmar si existe nombre oficial alterno de la electiva.",
    "[supuesto] Confirmar consigna de la primera actividad local para ajustar artefacto principal."
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
        "Normalizacion estructurada antes de propagar.",
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
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos solidos y verificables.",
      "Asegurar trazabilidad entre argumento, evidencia y cierre profesional."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Secciones explicitas y ordenadas.",
      "Postura propia respaldada.",
      "Marcado de [supuesto] cuando falte confirmacion.",
      "Cierre aplicable a practica juridica."
    ],
    "argumentative_patterns": [
      "Problema -> objetivo -> marco conceptual/normativo -> analisis propio -> conclusion.",
      "Cada afirmacion relevante se ancla a fuente o a [supuesto] marcado.",
      "Se evita descripcion pura; se exige juicio juridico razonado."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Integridad academica",
        "Trazabilidad cita-texto-bib",
        "Control de supuestos",
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
          "justification": "Reduce herencia de errores y memoria no parseable."
        },
        {
          "source": "Integridad academica",
          "target": "Trazabilidad cita-texto-bib",
          "kind": "depends_on",
          "justification": "La verificabilidad exige correspondencia explicita entre texto y fuente."
        },
        {
          "source": "Analisis juridico propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion profesional deriva del razonamiento del estudiante."
        },
        {
          "source": "Control de supuestos",
          "target": "Rigor editorial",
          "kind": "supports",
          "justification": "Diferencia hechos confirmados de datos pendientes."
        }
      ],
      "evidence": [
        "README local: pauta editorial y ubicacion curricular.",
        "Programa analitico local: proposito y ejes de trabajo.",
        ".bib local: base institucional verificable.",
        "Historial heredado: requisito de normalizacion por salidas no JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 15: se refuerza gate JSON parseable como condicion de propagacion.",
      "Ciclo 15: se mantiene union-dedupe sin eliminar reglas previas utiles.",
      "Ciclo 15: se agregan reglas transversales de estructura argumentativa reusable.",
      "Ciclo 15: se preserva estrategia conservadora de no transferir contenido tematico no validado.",
      "Ciclo 15: se consolida control de placeholders y nombres truncados como riesgo operativo transversal."
    ]
  }
}