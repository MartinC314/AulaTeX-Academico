{
  "summary": [
    "Sincronizacion transversal consolidada con union-dedupe lossless y sin regresion.",
    "Se preserva identidad UnADM y contexto curricular local de Antropologia de la cultura en Mexico.",
    "Se transfieren solo abstracciones estables desde Filosofia del Derecho: objetivo, evidencia, postura propia y coherencia argumentativa.",
    "Se mantiene bloqueo de propagacion para salidas no JSON parseable y exigencia de normalizacion estructurada.",
    "Se refuerza resolucion de placeholders en README y programa analitico antes de compilar o propagar."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Conservar ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "No trasladar metadatos curriculares de Filosofia del Derecho al nodo de Antropologia."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias canonicas de estructura."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuente verificable y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Evitar afirmaciones juridicas o culturales sin puente argumentativo.",
    "Cerrar con conclusion transferible a la practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa del esquema antes de reutilizar.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que cada afirmacion relevante tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto final y consigna real de la actividad.",
    "No promover reglas provisionales a definitivas sin confirmacion disciplinar."
  ],
  "latex_rules": [
    "Mantener plantilla base de la materia como referencia inicial.",
    "Usar codificacion en espanol y acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens dinamicos tipo $(@{...}.Slug) a nombres literales antes de compilar.",
    "Corregir rutas con caracteres truncados en README antes de referenciarlas."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes especificas por actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Mantener trazabilidad de procedencia cuando se use archivo local en assets-unadm."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y estructuradas.",
    "Compartir entre nodos no equivalentes solo abstracciones editoriales estables.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferencia de contenido tematico especifico de Filosofia del Derecho.",
    "Conservar historial de incidencias de parseo como alerta institucional reutilizable.",
    "Aplicar estrategia progresiva y conservadora: agregar mejoras verificables sin eliminar reglas utiles."
  ],
  "open_questions": [
    "Supuesto: falta consigna local de actividad concreta en Antropologia; confirmar formato exacto solicitado.",
    "Confirmar estandar unico de citacion para la licenciatura.",
    "Confirmar si LDE-S4B2 es clave oficial definitiva o clave operativa local.",
    "Confirmar si la conclusion juridica es obligatoria en todas las actividades de la materia.",
    "Confirmar que no queden placeholders activos en README y programa analitico."
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
      "Problema, conceptos, evidencia, analisis propio y conclusion transferible.",
      "Normalizacion estructurada antes de propagacion.",
      "Compresion lossless por union-dedupe sin recorte."
    ],
    "reason_for_being": [
      "Guiar productos academicos verificables y utiles para la practica profesional.",
      "Convertir la planeacion semanal en entregables claros, trazables y argumentados."
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
      "Pregunta guia -> desarrollo coherente -> respuesta final."
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
        "Resolucion de placeholders"
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
          "justification": "El analisis se legitima con respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion profesional surge del razonamiento argumentado."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y trazabilidad."
        },
        {
          "source": "Resolucion de placeholders",
          "target": "Normalizacion estructurada",
          "kind": "supports",
          "justification": "Evita rutas invalidas y errores de compilacion o referencia."
        }
      ],
      "evidence": [
        "README local define identidad UnADM y carpeta canonica.",
        "Programa analitico local fija ejes problema-conceptos-producto-analisis-cierre.",
        "Bibliografia local contiene unadmSitioWeb y unadmMallaDerecho2024.",
        "Memoria origen exige JSON parseable y normalizacion previa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 20: se refuerzan gates de parseo JSON y normalizacion estructurada.",
      "Ciclo 20: se consolidan patrones argumentativos transversales sin mover contenido tematico de origen.",
      "Ciclo 20: se mantiene alerta de fuentes heredadas no verificadas como provisionales.",
      "Ciclo 20: se preservan reglas utiles previas y se deduplican variantes redundantes."
    ]
  }
}