{
  "summary": [
    "Sincronizacion transversal consolidada por union-dedupe lossless y sin regresion.",
    "Se preservan reglas institucionales UnADM, estructura canonica y gates de parseo JSON.",
    "Se transfieren solo abstracciones estables desde actividad de Filosofia del Derecho.",
    "Se evita transferir contenido tematico exclusivo de Filosofia del Derecho al nodo de Antropologia.",
    "Se refuerza resolucion de placeholders y rutas corruptas detectadas en README y programa.",
    "Se mantiene estado provisional para fuentes heredadas no verificadas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener datos curriculares locales del destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar toda fuente heredada no verificada como provisional.",
    "No trasladar metadatos curriculares de otra asignatura al destino."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco normativo o teorico, analisis propio y cierre.",
    "Alinear el producto al entregable pedido por la planeacion semanal.",
    "Distinguir artefactos: reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias canonicas de estructura.",
    "Resolver nombres de archivo con placeholders a literales antes de editar."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar resumen descriptivo puro.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Integrar puentes argumentativos entre enfoque cultural y juridico.",
    "Cerrar con conclusion transferible a la practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Exigir estructura minima completa del esquema antes de reutilizar.",
    "Normalizar manualmente respuestas no estructuradas antes de aplicar aguas abajo.",
    "Validar que todo supuesto este marcado como supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto final y consigna de actividad.",
    "Verificar ausencia de placeholders sin resolver en README, programa, .tex y rutas."
  ],
  "latex_rules": [
    "Mantener configuracion en espanol coherente con la plantilla.",
    "Mantener clase y formato base salvo justificacion academica.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Usar acentos y codificacion correctos en .tex y .bib.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir rutas y nombres con caracteres truncados antes de compilar.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes consultables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales verificables.",
    "Registrar fuentes especificas de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No citar claves inexistentes en el .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y estables.",
    "Propagar transversalmente identidad, estructura reusable y quality gates.",
    "No propagar redaccion literal ni contenido tematico de nodo no equivalente.",
    "Mantener compresion lossless por union-dedupe sin eliminar reglas utiles previas.",
    "Registrar alertas de parseo como incidencias reutilizables inter-materias.",
    "Si falta contexto local, conservar cerebro editorial minimo y abrir vacios como preguntas."
  ],
  "open_questions": [
    "Supuesto: falta consigna puntual de actividades actuales de la materia destino; confirmar formato exacto por semana.",
    "Confirmar rubrica oficial de evaluacion para calibrar profundidad argumentativa.",
    "Confirmar estandar de citacion institucional unico para la licenciatura.",
    "Confirmar si la clave LDE-S4B2 es oficial o convencion local.",
    "Confirmar si toda actividad exige cierre juridico explicito en esta asignatura."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con trazabilidad de fuentes.",
        "Entrada canonica por carpeta de materia."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 4, bloque 2, obligatoria, 8 creditos.",
        "Asignatura destino: Antropologia de la cultura en Mexico."
      ]
    },
    "essence": [
      "Problema relevante, conceptos pertinentes, evidencia verificable, analisis propio y conclusion transferible.",
      "Normalizacion estructurada previa a toda propagacion.",
      "Sincronizacion transversal conservadora sin contaminar contexto disciplinar."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y utiles para formacion juridica.",
      "Preservar consistencia editorial institucional entre nodos de la suite."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente verificable -> interpretacion propia.",
      "Coherencia continua entre consigna, desarrollo y cierre."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion estructurada",
        "Validacion JSON parseable",
        "Marcado de supuestos",
        "Separacion de artefactos academicos",
        "Resolucion de placeholders en rutas y nombres"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Validacion JSON parseable",
          "target": "Normalizacion estructurada",
          "kind": "depends_on",
          "justification": "Sin parseo valido no existe base confiable para propagar memoria."
        },
        {
          "source": "Integridad academica",
          "target": "Evidencia verificable",
          "kind": "depends_on",
          "justification": "La integridad requiere respaldo trazable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura personal gana validez cuando se fundamenta."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La utilidad profesional surge del razonamiento argumentado."
        },
        {
          "source": "Marcado de supuestos",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Distingue hechos verificados de elementos pendientes."
        },
        {
          "source": "Resolucion de placeholders en rutas y nombres",
          "target": "Normalizacion estructurada",
          "kind": "supports",
          "justification": "Evita errores de compilacion y referencias ambiguas."
        }
      ],
      "evidence": [
        "README local confirma identidad UnADM y ubicacion curricular.",
        "Programa analitico local fija ejes problema-conceptos-producto-analisis-cierre.",
        "Bib local contiene unadmSitioWeb y unadmMallaDerecho2024.",
        "Historico de incidencias reporta salidas no parseables y necesidad de normalizacion manual."
      ]
    },
    "reinforcement_log": [
      "Ciclo 34: deduplicacion completada sin eliminar reglas utiles previas.",
      "Ciclo 34: se reforzaron gates de JSON parseable y estructura minima obligatoria.",
      "Ciclo 34: se incorporaron patrones argumentativos estables del origen no equivalente.",
      "Ciclo 34: se preservo la identidad curricular local del destino sin mezclar metadatos del origen."
    ]
  }
}