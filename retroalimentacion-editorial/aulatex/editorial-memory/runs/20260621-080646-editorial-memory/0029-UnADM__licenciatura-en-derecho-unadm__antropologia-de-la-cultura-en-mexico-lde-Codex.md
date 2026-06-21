{
  "summary": [
    "Sincronizacion transversal aplicada con union-dedupe lossless y sin regresion.",
    "Se preserva identidad UnADM y contexto curricular local del destino.",
    "Se transfieren solo abstracciones estables desde actividad de otra materia.",
    "Se refuerza normalizacion estructurada y bloqueo por JSON no parseable.",
    "Se mantiene alerta de fuentes heredadas no verificadas como provisionales.",
    "Se evita trasladar contenido tematico especifico de Filosofia del Derecho."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener materia destino: Antropologia de la cultura en Mexico.",
    "Conservar ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar toda fuente heredada no verificada como provisional.",
    "No mover metadatos curriculares de otras materias al destino."
  ],
  "structure_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar secciones en conceptos, marco de referencia, analisis propio y cierre.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias canonicas.",
    "Resolver placeholders y tokens dinamicos a nombres literales antes de usar rutas."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Evitar afirmaciones culturales o juridicas sin puente argumentativo.",
    "Cerrar con conclusion transferible a la practica juridica cuando la consigna lo exija."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa del esquema antes de reutilizar.",
    "Revisar y normalizar respuestas no estructuradas antes de propagar.",
    "Confirmar consistencia entre metadatos del documento y malla curricular local.",
    "Verificar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No promover reglas provisionales a definitivas sin verificacion local."
  ],
  "latex_rules": [
    "Mantener plantilla .tex local como base.",
    "Usar configuracion en espanol coherente con la plantilla.",
    "Mantener clase article, letterpaper y oneside salvo instruccion distinta.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Conservar coursename y coursecode locales salvo cambio institucional.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Corregir rutas con caracteres truncados antes de compilar."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo fuentes realmente consultables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales verificables.",
    "Registrar fuentes especificas por actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Mantener claves BibTeX estables.",
    "No citar claves inexistentes en el .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y parseables.",
    "Compartir entre nodos no equivalentes solo abstracciones editoriales estables.",
    "Priorizar identidad, estructura reusable, gates y grafo conceptual.",
    "Evitar transferencia de redaccion literal o contenidos disciplinares especificos.",
    "Registrar incidencias de parseo como alertas reutilizables.",
    "Aplicar estrategia progresiva y conservadora sin eliminar reglas utiles previas."
  ],
  "open_questions": [
    "Supuesto: falta consigna puntual de actividad en destino para fijar formato final.",
    "Confirmar si conclusion juridica es obligatoria en todas las actividades de antropologia.",
    "Confirmar estandar institucional unico de citacion para la licenciatura.",
    "Confirmar si LDE-S4B2 permanece como clave oficial vigente.",
    "Confirmar si existen fuentes obligatorias adicionales de la materia."
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
      "Problema, conceptos, evidencia, analisis propio y cierre.",
      "Normalizacion estructurada antes de toda propagacion.",
      "Compresion lossless por union-dedupe y sin regresion.",
      "Transferencia transversal de metarreglas, no de contenido tematico."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y utiles.",
      "Asegurar consistencia editorial institucional entre actividades y materias.",
      "Sostener calidad tecnica de LaTeX y bibliografia verificable."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Cierre con aplicabilidad academica o profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente verificable -> interpretacion propia.",
      "Pregunta guia -> desarrollo coherente -> cierre consistente."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion transferible",
        "Validacion JSON parseable",
        "Normalizacion estructurada",
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
          "justification": "Sin parseo valido no hay memoria reutilizable confiable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura propia se legitima con respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion surge del razonamiento y no del resumen."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y trazabilidad."
        }
      ],
      "evidence": [
        "README local: identidad UnADM y pauta editorial.",
        "Programa analitico local: ejes problema, conceptos, producto, analisis y cierre.",
        "Bib local: unadmSitioWeb y unadmMallaDerecho2024.",
        "Regla vigente: bloquear propagacion si no hay JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 29: se consolidan reglas comunes de actividad a materia sin arrastre tematico.",
      "Ciclo 29: se deduplican reglas repetidas y se conserva cobertura total util.",
      "Ciclo 29: se refuerzan gates de parseo, supuestos y trazabilidad bibliografica.",
      "Ciclo 29: se mantiene compatibilidad con estrategia progresiva y conservadora."
    ]
  }
}