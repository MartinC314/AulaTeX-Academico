{
  "summary": [
    "Sincronizacion transversal aplicada con union-dedupe lossless y sin regresion.",
    "Se preserva identidad UnADM y contexto curricular local de Antropologia en Derecho.",
    "Se incorporan solo abstracciones estables del origen: objetivo, evidencia, analisis propio y coherencia.",
    "Se mantiene bloqueo de propagacion para salidas no JSON parseable y normalizacion previa."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener contexto local del destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No transferir metadatos curriculares especificos de Filosofia del Derecho al destino."
  ],
  "structure_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Organizar en secciones: conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear el producto con la planeacion semanal y la consigna real.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Resolver placeholders y tokens dinamicos en README, programa y rutas antes de usar."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Evitar extrapolar contenidos tematicos de otra asignatura sin puente disciplinar.",
    "Cerrar con conclusion transferible a la practica juridica cuando la consigna lo permita."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa del esquema antes de reutilizar.",
    "Normalizar manualmente respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar trazabilidad de afirmaciones o marcarlas como supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No promover reglas provisionales a definitivas sin validacion disciplinar local."
  ],
  "latex_rules": [
    "Mantener plantilla .tex local de la materia como base.",
    "Usar configuracion en espanol y metadatos institucionales consistentes.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, sin referencias rotas y sin tokens sin expandir.",
    "Corregir rutas o nombres con caracteres truncados antes de compilar.",
    "Actualizar documenttitle y documentsubtitle segun actividad real."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo obras verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes especificas por actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "No asumir reutilizacion automatica de .bib de otra materia."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y abstractas entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferir redaccion literal o contenido tematico exclusivo del origen.",
    "Conservar historial de incidencias de parseo como alerta transversal.",
    "Aplicar estrategia progresiva y conservadora: agregar mejoras verificables sin borrar reglas utiles."
  ],
  "open_questions": [
    "Supuesto: falta consigna puntual de actividades de Antropologia para calibrar profundidad de conclusion juridica.",
    "Confirmar si LDE-S4B2 es clave institucional definitiva o clave local.",
    "Confirmar estandar unico de citacion para toda la licenciatura.",
    "Confirmar si toda actividad exige cierre juridico explicito o depende de rubrica local.",
    "Confirmar si el nombre canonico del .bib queda fijo en literal sin plantilla dinamica."
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
        "Materia destino: Antropologia de la cultura en Mexico.",
        "Semestre 4, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema, conceptos, evidencia, analisis propio y cierre.",
      "Normalizacion estructurada antes de propagar.",
      "Compresion lossless por union-dedupe sin recorte."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables y utiles.",
      "Sostener coherencia institucional y calidad transversal entre materias.",
      "Evitar regresiones editoriales en consolidaciones sucesivas."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos etiquetados cuando falte evidencia.",
      "Cierre con utilidad academica o profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente verificable -> interpretacion propia.",
      "Consigna -> desarrollo alineado -> verificacion final."
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
          "justification": "Sin parseo valido no hay reutilizacion segura."
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
          "justification": "La conclusion util deriva del razonamiento argumentado."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige rigor y citas verificables."
        }
      ],
      "evidence": [
        "README y programa analitico del destino confirman ejes editoriales y contexto curricular.",
        "Memoria origen valida patron estable: objetivo, evidencia, analisis propio y conclusion.",
        "Incidencias previas de salida no estructurada justifican gates de parseo y normalizacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 18: se refuerzan abstracciones estables sin migrar contenido tematico de Filosofia.",
      "Ciclo 18: se conserva alerta transversal por no JSON parseable.",
      "Ciclo 18: se mantiene regla de no regresion y deduplicacion lossless."
    ]
  }
}