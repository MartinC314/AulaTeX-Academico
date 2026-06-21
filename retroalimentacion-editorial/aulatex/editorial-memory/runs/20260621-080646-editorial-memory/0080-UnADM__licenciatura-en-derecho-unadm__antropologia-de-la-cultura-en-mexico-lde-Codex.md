{
  "summary": [
    "Sincronizacion transversal aplicada desde actividad de Filosofia del Derecho hacia materia de Antropologia con estrategia conservadora.",
    "Se preservan reglas institucionales UnADM, estructura canonica y control de calidad por JSON parseable.",
    "Se transfieren solo abstracciones estables: objetivo, estructura argumentativa, evidencia verificable y cierre transferible.",
    "Se evita mover contenido tematico especifico de Filosofia del Derecho al destino.",
    "Se mantiene compresion lossless por union-dedupe sin regresion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener ubicacion curricular local del destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales.",
    "No transferir metadatos curriculares de Filosofia del Derecho a Antropologia."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar secciones en: conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias de estructura reutilizable.",
    "Corregir placeholders y tokens dinamicos en rutas y nombres de archivo antes de usar."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Evitar afirmaciones juridicas o culturales sin puente argumentativo.",
    "Cerrar con conclusion transferible a la practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar memoria.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregado y consigna local."
  ],
  "latex_rules": [
    "Mantener plantilla .tex base de la materia destino como referencia.",
    "Usar configuracion en espanol y acentos consistentes en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Mantener claves BibTeX estables.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README, programa y rutas de bibliografia.",
    "Corregir nombres truncados en README (supuesto: errores de salto en 'reporte' y 'referencias')."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes especificas por actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "No citar claves inexistentes en el .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y abstractas entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Etiquetar incidencias de parseo como alerta reutilizable inter-materias.",
    "Mantener politica sin regresion en ciclos futuros.",
    "Si falta contexto local, conservar cerebro editorial minimo y abrir preguntas."
  ],
  "open_questions": [
    "Supuesto: confirmar si el estandar de citacion institucional es APA u otro para esta materia.",
    "Confirmar si LDE-S4B2 es clave oficial o local.",
    "Confirmar rubrica de evaluacion por actividad para calibrar profundidad argumentativa.",
    "Confirmar si toda actividad de Antropologia exige cierre explicitamente juridico.",
    "Confirmar que el nombre canonico del .bib queda fijo en antropologia-de-la-cultura-en-mexico.bib."
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
      "Problema inicial claro.",
      "Conceptos y marco pertinente.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos consistentes y verificables.",
      "Sostener continuidad editorial transversal sin contaminar contexto disciplinar local."
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
      "Pregunta guia -> desarrollo coherente -> respuesta final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON parseable",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion transferible",
        "Sincronizacion transversal conservadora"
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
          "justification": "Sin parseo valido no hay propagacion confiable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura academica requiere respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "El cierre profesional surge del razonamiento y no del resumen."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Sincronizacion transversal conservadora",
          "kind": "supports",
          "justification": "La coherencia institucional guia la transferencia entre nodos."
        }
      ],
      "evidence": [
        "README destino confirma identidad UnADM y ubicacion curricular.",
        "Programa analitico destino fija ejes problema-conceptos-producto-analisis-cierre.",
        "Memoria origen aporta gates de parseo y estructura argumentativa reutilizable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 80: deduplicacion aplicada sin eliminar reglas utiles previas.",
      "Ciclo 80: transferidas abstracciones estables; excluido contenido tematico no transversal.",
      "Ciclo 80: reforzado gate de JSON parseable y control de supuestos.",
      "Ciclo 80: reforzada resolucion de tokens dinamicos en rutas editoriales."
    ]
  }
}