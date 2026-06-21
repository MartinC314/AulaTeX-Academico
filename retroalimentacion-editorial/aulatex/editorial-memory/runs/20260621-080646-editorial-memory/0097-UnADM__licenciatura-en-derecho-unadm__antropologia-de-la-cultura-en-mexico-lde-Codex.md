{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia conservadora y union-dedupe lossless.",
    "Se preservan reglas institucionales UnADM, parseo JSON y normalizacion estructurada.",
    "Se transfieren solo abstracciones estables desde actividad de Filosofia del Derecho.",
    "No se transfieren contenidos tematicos exclusivos de Filosofia al nodo de Antropologia.",
    "Se refuerzan ejes reutilizables: objetivo, evidencia, analisis propio, coherencia y cierre transferible."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener contexto curricular local del destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No trasladar metadatos curriculares de Filosofia del Derecho al destino."
  ],
  "structure_rules": [
    "Iniciar cada entrega con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear el producto con la planeacion semanal y la consigna real.",
    "Distinguir artefactos: reporte, presentacion y bibliografia.",
    "Resolver placeholders y tokens dinamicos en README, programa y rutas antes de uso."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Evitar extrapolar fuentes de semanas o materias no confirmadas.",
    "Cerrar con conclusion juridica transferible a practica profesional cuando la consigna lo pida."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Exigir estructura minima completa del esquema antes de reutilizar.",
    "Normalizar manualmente cualquier salida no estructurada heredada.",
    "Confirmar que toda afirmacion tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregado y consigna vigente."
  ],
  "latex_rules": [
    "Usar configuracion en espanol y acentos correctos en .tex y .bib.",
    "Mantener clase y formato base salvo justificacion academica.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Compilar sin errores criticos, referencias rotas ni rutas invalidas.",
    "Mantener claves BibTeX estables y coherentes con citas en texto.",
    "Corregir caracteres truncados y resolver tokens tipo $(@{...}.Slug) en nombres de archivo."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias consultables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales pertinentes.",
    "Registrar fuentes especificas por actividad en el .bib local de la materia.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Marcar como supuesto cualquier asignacion de fuente no confirmada por consigna."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y abstractas.",
    "Mantener union-dedupe sin eliminar reglas utiles previas.",
    "Registrar incidencias de parseo como alertas reutilizables inter-materias.",
    "Propagar identidad, gates de calidad y patrones argumentativos antes que contenido tematico.",
    "Si falta contexto local en nodos vecinos, crear base minima y dejar vacios explicitos."
  ],
  "open_questions": [
    "Supuesto: falta consigna puntual de actividades especificas en Antropologia; confirmar formato y rubricas.",
    "Confirmar estandar de citacion institucional unico para la licenciatura.",
    "Confirmar si la conclusion juridica es obligatoria en todas las actividades de la materia.",
    "Confirmar nombre canonico definitivo del .bib cuando haya plantillas dinamicas en documentos."
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
        "Destino local: semestre 4, bloque 2, obligatoria, 8 creditos.",
        "Asignatura destino: Antropologia de la cultura en Mexico."
      ]
    },
    "essence": [
      "Problema relevante.",
      "Conceptos y marco pertinente.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Cierre transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y utiles.",
      "Sostener calidad institucional transversal entre materias.",
      "Evitar regresiones de estructura, evidencia y verificabilidad."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados cuando falte evidencia.",
      "Cierre con aplicacion profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> cita verificable -> interpretacion propia.",
      "Pregunta guia -> desarrollo coherente -> respuesta final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON parseable",
        "Evidencia verificable",
        "Analisis propio",
        "Coherencia argumentativa",
        "Conclusion transferible",
        "Separacion de artefactos"
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
          "justification": "Sin parseo valido no hay memoria reusable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura personal se legitima con respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "El cierre util surge del razonamiento y no del resumen."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Coherencia argumentativa",
          "kind": "supports",
          "justification": "La pauta institucional exige rigor, claridad y trazabilidad."
        }
      ],
      "evidence": [
        "README de destino confirma identidad UnADM y pauta editorial.",
        "Programa analitico confirma ejes problema-conceptos-producto-analisis-cierre.",
        "Bib local confirma base institucional con unadmSitioWeb y unadmMallaDerecho2024.",
        "Memoria origen confirma gates de parseo JSON y normalizacion obligatoria."
      ]
    },
    "reinforcement_log": [
      "Ciclo 97: deduplicacion completa de reglas repetidas.",
      "Ciclo 97: transferencia transversal limitada a abstracciones estables.",
      "Ciclo 97: refuerzo de gates JSON, supuestos y trazabilidad bibliografica.",
      "Ciclo 97: exclusion explicita de contenido tematico no equivalente entre materias."
    ]
  }
}