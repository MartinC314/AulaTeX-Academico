{
  "summary": [
    "Sincronizacion transversal consolidada con estrategia conservadora y deduplicacion lossless.",
    "Se preserva identidad UnADM y estructura argumentativa reusable sin trasladar contenido tematico de Filosofia del Derecho.",
    "Se refuerza normalizacion obligatoria de salidas no estructuradas y bloqueo por JSON invalido.",
    "Se mantiene eje editorial comun: problema, conceptos/fuentes, analisis propio y conclusion juridica transferible.",
    "Se confirma contexto destino: materia electiva de Derecho, semestre 8, bloque 2, con vacios locales marcados como [supuesto]."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, metadatos y formato.",
    "Alinear entregables al contexto curricular local: Licenciatura en Derecho, semestre 8, bloque 2, tipo Electiva.",
    "Usar la carpeta de materia como entrada canonica editorial.",
    "Marcar como [supuesto] todo dato no confirmado en consigna o documentos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "Mantener autor y matricula confirmados en front matter cuando el artefacto lo requiera."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en bloques: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear siempre el producto al tipo solicitado en la planeacion semanal.",
    "Cerrar con conclusion juridica aplicable a la practica profesional.",
    "Mantener consistencia entre README, programa analitico, .tex y .bib."
  ],
  "activity_rules": [
    "Traducir cada consigna semanal a un producto concreto verificable.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar resumen descriptivo.",
    "Vincular conceptos, normas, doctrina o datos con el problema tratado.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No transferir contenido especifico de otra asignatura sin validacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar artefactos heredados no estructurados antes de reutilizar.",
    "Confirmar trazabilidad entre afirmaciones, citas en texto y .bib.",
    "Confirmar ausencia de placeholders visibles en README, programa, .tex y .bib.",
    "Verificar correspondencia entre producto entregado y consigna real de la actividad."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Conservar plantilla base local y actualizar titulo, subtitulo y numero real de actividad.",
    "Mantener nombres de archivo coherentes entre README, programa y carpeta real.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) a nombres literales.",
    "Corregir nombres truncados en listados de estructura antes de compilar.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas por actividad en el .bib local de la materia.",
    "Priorizar fuentes institucionales UnADM cuando correspondan.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente/editorial o URL.",
    "Distinguir bibliografia base institucional de bibliografia especifica de actividad.",
    "Mantener claves BibTeX estables y trazables con citas en texto."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo abstracciones estables y validadas.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar copiar redaccion literal o contenido tematico dependiente de materia origen.",
    "Mantener compresion por union-dedupe sin eliminar reglas utiles previas.",
    "Conservar etiqueta de herencia provisional hasta confirmacion manual.",
    "Usar ciclo 2 para reforzar normalizacion tecnica y no para ampliar supuestos no verificados."
  ],
  "open_questions": [
    "[supuesto] Confirmar creditos oficiales de la materia electiva para metadatos.",
    "[supuesto] Confirmar nombre oficial de figura docente en portada.",
    "[supuesto] Confirmar si existe denominacion institucional alterna de la electiva.",
    "[supuesto] Confirmar politica local para year y fecha de consulta en @misc institucional.",
    "[supuesto] Confirmar consigna de la primera actividad local para ajustar tipo de artefacto."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador en transferencia transversal."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada antes de propagar.",
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 8, bloque 2, tipo Electiva.",
        "[supuesto] Creditos pendientes de confirmacion."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo con evidencia.",
      "Analisis propio con postura.",
      "Conclusion juridica transferible.",
      "Trazabilidad tecnica y academica del entregable."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos publicables y verificables.",
      "Sostener consistencia editorial entre documentos de la materia.",
      "Asegurar calidad argumentativa y tecnica en cada entrega."
    ],
    "style_markers": [
      "Frases directas y modulares.",
      "Marcado explicito de [supuesto] ante vacios de informacion.",
      "Separacion clara entre hechos, evidencia y postura.",
      "Cierre juridico practico, no solo descriptivo."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Definir objetivo.",
      "Presentar conceptos y marco normativo.",
      "Contrastar evidencia verificable.",
      "Defender postura propia.",
      "Concluir con implicacion juridica aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Trazabilidad de fuentes",
        "Estructura problema-analisis-conclusion",
        "Normalizacion tecnica LaTeX",
        "Consistencia interdocumental README-programa-tex-bib"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Integridad academica",
          "target": "Trazabilidad de fuentes",
          "kind": "depends_on",
          "justification": "La integridad exige respaldo verificable de cada afirmacion."
        },
        {
          "source": "Estructura problema-analisis-conclusion",
          "target": "Calidad argumentativa",
          "kind": "supports",
          "justification": "Ordena el razonamiento y evita entregas meramente descriptivas."
        },
        {
          "source": "Normalizacion tecnica LaTeX",
          "target": "Publicabilidad del entregable",
          "kind": "supports",
          "justification": "Sin compilacion limpia y nombres correctos no hay reutilizacion confiable."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Consistencia interdocumental README-programa-tex-bib",
          "kind": "develops",
          "justification": "La identidad comun estabiliza la edicion transversal entre nodos."
        }
      ],
      "evidence": [
        "README local define identidad UnADM, integridad academica y conclusion juridica propia.",
        "Programa analitico local explicita ejes problema-conceptos-producto-analisis-conclusion.",
        "Se detectan placeholders/tokens en README y programa; requieren normalizacion verificable.",
        "Regla heredada valida: bloquear propagacion ante salida no JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: deduplicacion completa de reglas repetidas sin perdida semantica.",
      "Ciclo 2: transferencia solo de abstracciones estables, sin arrastre tematico de Filosofia del Derecho.",
      "Ciclo 2: refuerzo de quality gates JSON, trazabilidad y normalizacion de placeholders.",
      "Ciclo 2: consolidacion del patron argumentativo reusable para actividades de la materia destino."
    ]
  }
}