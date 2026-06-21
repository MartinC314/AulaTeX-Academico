{
  "summary": [
    "Sincronizacion transversal aplicada con union-dedupe lossless y sin regresion.",
    "Se preservan reglas institucionales UnADM y estructura canonica del destino.",
    "Se agregan abstracciones estables del origen: objetivo puntual, evidencia verificable, postura propia y coherencia argumentativa.",
    "Se evita transferir contenido tematico especifico de Filosofia del Derecho al nodo de Antropologia.",
    "Se refuerza normalizacion obligatoria cuando exista salida no JSON parseable.",
    "Se mantiene estado provisional para fuentes heredadas no verificadas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Usar nombre de materia: Antropologia de la cultura en Mexico.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No trasladar metadatos curriculares de otras materias al destino."
  ],
  "structure_rules": [
    "Iniciar cada entrega con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Ordenar secciones en: conceptos clave, marco normativo o teorico, analisis propio y cierre.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias de estructura editable.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar solo descripcion.",
    "Sustentar afirmaciones relevantes con fuente verificable y cita explicita.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Integrar conceptos antropologicos, culturales, juridicos o sociales pertinentes.",
    "Evitar puentes argumentativos debiles entre analisis cultural y conclusion juridica."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar memoria.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Comprobar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto final y consigna vigente.",
    "No promover reglas provisionales a definitivas sin validacion disciplinar."
  ],
  "latex_rules": [
    "Mantener plantilla .tex local como base editorial.",
    "Conservar configuracion en espanol y acentos correctos en .tex y .bib.",
    "Mantener clase article, letterpaper y oneside salvo instruccion distinta.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens dinamicos tipo $(@{...}.Slug) en README, programa y rutas de archivos.",
    "Corregir rutas con caracteres truncados antes de compilar."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables y consultables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales pertinentes.",
    "Registrar fuentes especificas de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No citar claves ausentes en el .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y abstraidas.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar propagar redaccion literal o contenido tematico de otra asignatura.",
    "Conservar compresion lossless por union-dedupe en ciclos siguientes.",
    "Registrar incidencias de parseo como alertas transversales reutilizables.",
    "Mantener estrategia progresiva y conservadora: agregar sin eliminar reglas utiles previas."
  ],
  "open_questions": [
    "Supuesto: falta consigna local de actividades especificas; confirmar formatos por semana.",
    "Confirmar estandar institucional de citacion para toda la licenciatura.",
    "Confirmar si la clave LDE-S4B2 es oficial institucional o solo local.",
    "Confirmar si la conclusion juridica aplica a todas las actividades de antropologia o solo a algunas.",
    "Confirmar si existen fuentes base obligatorias adicionales a malla curricular y sitio UnADM."
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
      "Problema relevante.",
      "Conceptos pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros, sustentados y utiles para formacion juridica.",
      "Garantizar consistencia editorial y tecnica entre actividades, plantillas y referencias."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Cierre con valor profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente verificable -> interpretacion propia.",
      "Coherencia entre pregunta guia y respuesta final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Normalizacion estructurada",
        "Validacion JSON parseable",
        "Supuestos marcados",
        "Sincronizacion transversal conservadora"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "El marco institucional exige trazabilidad y rigor."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura personal gana solidez con respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La utilidad profesional depende del razonamiento desarrollado."
        },
        {
          "source": "Validacion JSON parseable",
          "target": "Normalizacion estructurada",
          "kind": "depends_on",
          "justification": "Sin parseo valido no hay propagacion confiable."
        },
        {
          "source": "Supuestos marcados",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Diferencia hechos confirmados de datos no verificados."
        }
      ],
      "evidence": [
        "README local de la materia: identidad UnADM y pauta editorial.",
        "Programa analitico local: ejes de problema, conceptos, evidencia, analisis y cierre.",
        "Bibliografia local: unadmSitioWeb y unadmMallaDerecho2024.",
        "Regla transversal consolidada: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 54: se integran abstracciones estables desde actividad de Filosofia del Derecho.",
      "Ciclo 54: se conserva identidad y curricularidad local de Antropologia sin mezclar metadatos externos.",
      "Ciclo 54: se refuerzan quality gates de parseo, normalizacion y trazabilidad.",
      "Ciclo 54: se mantiene compresion lossless por deduplicacion semantica."
    ]
  }
}