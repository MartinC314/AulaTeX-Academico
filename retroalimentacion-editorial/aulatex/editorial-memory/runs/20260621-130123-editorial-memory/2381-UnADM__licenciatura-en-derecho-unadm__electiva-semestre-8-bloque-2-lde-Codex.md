{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre actividad origen y materia destino.",
    "Se preservan reglas utiles previas sin regresion y con deduplicacion lossless.",
    "Se refuerzan ejes estables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene obligatoriedad de normalizacion estructurada antes de propagacion recursiva.",
    "Se evita transferir contenido tematico especifico de Filosofia del Derecho sin validacion local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 8, bloque 2, tipo Electiva.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no confirmado en consigna o documentos locales.",
    "Mantener autor y matricula confirmados en front matter: Martin Jonathan de la Cruz, ES2611202040.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion manual."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener consistencia entre README, programa analitico, .tex y .bib."
  ],
  "activity_rules": [
    "Traducir cada consigna semanal a producto concreto solicitado.",
    "Incluir postura argumentada del estudiante y evitar resumen puramente descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Vincular conceptos, normas, doctrina o datos con el problema juridico tratado.",
    "No asumir que fuentes de otras semanas o materias aplican sin confirmacion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar memoria aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas heredadas antes de uso.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar ausencia de placeholders o tokens sin expandir en README, programa, .tex y .bib."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Conservar plantilla base de la materia y metadatos institucionales.",
    "Actualizar titulo, subtitulo y numero real de actividad antes de compilar.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion.",
    "Corregir rutas, nombres truncados y placeholders antes de entrega.",
    "Compilar sin errores criticos y sin referencias rotas."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas por actividad en electiva-semestre-8-bloque-2.bib.",
    "Priorizar fuentes institucionales UnADM cuando corresponda.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Mantener trazabilidad entre afirmaciones, citas y entradas BibTeX."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas abstractas y estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferencia literal de redaccion o contenido tematico local del origen.",
    "Mantener compresion por union-dedupe sin eliminar reglas utiles previas.",
    "Etiquetar herencias no verificadas como provisionales hasta confirmacion local.",
    "Mantener ciclo de normalizacion manual para herencias de salidas no estructuradas."
  ],
  "open_questions": [
    "[supuesto] Confirmar creditos oficiales de la materia para completar metadatos.",
    "[supuesto] Confirmar nombre oficial de figura docente en front matter.",
    "[supuesto] Confirmar si LDE-S8B2 es codigo institucional definitivo.",
    "[supuesto] Confirmar politica institucional para year y fecha de consulta en @misc.",
    "[supuesto] Confirmar si la electiva tiene nombre oficial alterno.",
    "[supuesto] Confirmar consigna local de primera actividad para ajustar tipos de artefacto."
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
        "Semestre 8, bloque 2, tipo Electiva.",
        "[supuesto] Creditos pendientes de confirmacion."
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
      "Convertir planeacion semanal en entregables juridicos claros y verificables.",
      "Garantizar trazabilidad editorial y academica en todo artefacto.",
      "Sostener una memoria persistente reusable sin perder contexto institucional."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Secciones explicitas y ordenadas.",
      "Postura propia respaldada por fuentes.",
      "Cierre con aplicacion profesional.",
      "Marcado explicito de [supuesto] cuando falte verificacion."
    ],
    "argumentative_patterns": [
      "Problema -> objetivo -> marco conceptual/normativo -> analisis propio -> conclusion aplicable.",
      "Afirmacion -> evidencia -> interpretacion -> implicacion juridica.",
      "Control de coherencia entre consigna, desarrollo y cierre."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Integridad academica",
        "Trazabilidad cita-texto-bib",
        "Control de supuestos",
        "Analisis juridico propio",
        "Conclusion juridica transferible"
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
          "justification": "La verificabilidad exige correspondencia entre afirmaciones y fuentes."
        },
        {
          "source": "Analisis juridico propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La transferencia profesional surge del razonamiento propio."
        },
        {
          "source": "Control de supuestos",
          "target": "Rigor editorial",
          "kind": "supports",
          "justification": "Diferencia datos confirmados de datos pendientes."
        }
      ],
      "evidence": [
        "README local de la materia.",
        "Programa analitico local.",
        "Archivo bib local con base institucional.",
        "Memoria origen con gates de calidad y estructura estable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: se deduplican reglas repetidas y se preserva cobertura funcional.",
      "Ciclo 2: se refuerza gate de JSON parseable como bloqueo duro de propagacion.",
      "Ciclo 2: se mantiene estrategia conservadora de no transferir contenido tematico especifico.",
      "Ciclo 2: se consolidan patrones argumentativos reutilizables a nivel materia.",
      "Ciclo 2: se conserva herencia provisional de fuentes no verificadas con marcado explicito."
    ]
  }
}