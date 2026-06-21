{
  "summary": [
    "Sincronizacion transversal ciclo 99 aplicada con union-dedupe lossless y sin regresion.",
    "Se preservan reglas institucionales UnADM, estructura canonica y gates de calidad JSON.",
    "Se transfieren solo abstracciones estables desde actividad de Filosofia del Derecho a materia de Antropologia.",
    "Se evita transferir contenido tematico exclusivo de Filosofia del Derecho al destino.",
    "Se refuerza marcacion de supuestos y manejo de fuentes heredadas como provisionales.",
    "Se consolida resolucion obligatoria de placeholders dinamicos en README, programa y rutas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Mantener adscripcion a Licenciatura en Derecho.",
    "Mantener contexto local del destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar toda fuente heredada no verificada como provisional.",
    "No trasladar metadatos curriculares de otra asignatura al destino."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o teorico, analisis propio y cierre.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias de estructura.",
    "Cerrar con conclusion transferible a la practica juridica."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion.",
    "Evitar afirmaciones juridicas sin puente argumentativo cultural.",
    "Confirmar que el producto final coincide con la consigna real de la actividad.",
    "No asumir fuentes de otras semanas sin validacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar memoria.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No promover reglas provisionales a definitivas sin validacion disciplinar."
  ],
  "latex_rules": [
    "Usar codificacion y acentos en espanol de forma consistente en .tex y .bib.",
    "Mantener clase y formato base salvo justificacion academica.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Mantener coursename y coursecode locales del destino salvo instruccion oficial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README, programa y nombres de archivo.",
    "Corregir rutas truncadas o caracteres anomalos antes de compilar."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Usar solo referencias verificables y consultables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes especificas de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No citar claves inexistentes en el .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y parseables.",
    "Compartir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferencia literal de redaccion o contenido tematico de otra materia.",
    "Mantener compresion lossless por union-dedupe en ciclos futuros.",
    "Registrar incidencias de parseo como alertas transversales reutilizables."
  ],
  "open_questions": [
    "Supuesto: falta consigna especifica de actividades de Antropologia; confirmar productos exactos por semana.",
    "Confirmar estandar unico de citacion para la licenciatura.",
    "Confirmar si LDE-S4B2 es clave oficial o local.",
    "Confirmar si la conclusion juridica es obligatoria en todas las actividades de la materia.",
    "Confirmar politica institucional para placeholders dinamicos en artefactos fuente."
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
        "Asignatura: Antropologia de la cultura en Mexico."
      ]
    },
    "essence": [
      "Problema.",
      "Conceptos.",
      "Evidencia.",
      "Analisis propio.",
      "Conclusion transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables academicos verificables.",
      "Asegurar coherencia entre identidad institucional, evidencia y argumentacion.",
      "Sostener calidad reproducible en reportes y presentaciones."
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
      "Pregunta guia -> desarrollo alineado -> respuesta final coherente."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON parseable",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Supuestos marcados",
        "Propagacion transversal conservadora"
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
          "justification": "Sin parseo valido no hay reutilizacion confiable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "El argumento gana legitimidad con respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion util deriva del razonamiento."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "La pauta institucional exige integridad academica."
        },
        {
          "source": "Supuestos marcados",
          "target": "Propagacion transversal conservadora",
          "kind": "supports",
          "justification": "Reduce errores al transferir reglas entre nodos distintos."
        }
      ],
      "evidence": [
        "README local de la materia destino.",
        "Programa analitico local con ejes de trabajo.",
        "Archivo .bib local con fuentes institucionales base.",
        "Regla heredada y vigente: bloquear salida no JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin perdida de contenido util.",
      "Se conservaron alertas historicas de parseo no estructurado.",
      "Se incorporaron abstracciones estables del origen: objetivo puntual, evidencia, postura y coherencia.",
      "Se excluyeron contenidos doctrinales especificos de Filosofia del Derecho por no equivalencia disciplinar.",
      "Se reforzo gate de placeholders sin expandir como riesgo tecnico transversal."
    ]
  }
}