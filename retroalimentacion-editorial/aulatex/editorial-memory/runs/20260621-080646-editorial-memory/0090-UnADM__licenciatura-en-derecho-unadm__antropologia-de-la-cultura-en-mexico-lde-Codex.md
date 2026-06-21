{
  "summary": [
    "Sincronizacion transversal aplicada con union-dedupe lossless y sin regresion.",
    "Se preservan reglas validas del destino y del origen como abstracciones estables.",
    "Se refuerza identidad UnADM, estructura reusable, calidad de parseo y trazabilidad de fuentes.",
    "Se evita transferir contenido tematico exclusivo de Filosofia del Derecho al nodo de Antropologia.",
    "Se mantiene estado provisional de fuentes heredadas no verificadas.",
    "Se detecta destino operativo con base minima suficiente; se consolidan vacios locales abiertos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener contexto curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar toda fuente heredada no verificada como provisional hasta confirmacion disciplinar.",
    "No trasladar metadatos curriculares de materias distintas al destino."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear el artefacto al producto solicitado en planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias canonicas de estructura.",
    "Resolver placeholders de nombre de archivos a literales antes de compilar."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Cerrar con conclusion transferible a practica juridica cuando la consigna lo permita.",
    "Integrar conceptos culturales y juridicos con puente argumentativo explicito."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar memoria.",
    "Normalizar manualmente salidas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que rutas y nombres no contengan tokens sin resolver.",
    "No promover reglas provisionales a definitivas sin validacion local."
  ],
  "latex_rules": [
    "Usar codificacion en espanol coherente en .tex y .bib.",
    "Mantener clase y configuracion base salvo justificacion academica.",
    "Actualizar documenttitle y documentsubtitle por actividad real.",
    "Conservar campos institucionales completos y consistentes con la materia.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Mantener claves BibTeX estables.",
    "Corregir caracteres truncados en rutas antes de compilar."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias consultables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales verificables.",
    "Registrar fuentes especificas de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "No citar claves ausentes en el .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y abstraidas.",
    "Compartir entre nodos no equivalentes solo patrones editoriales estables.",
    "Evitar redaccion literal y contenido disciplinar no transferible.",
    "Registrar alertas de parseo como control transversal reutilizable.",
    "Mantener estrategia progresiva y conservadora: agregar sin borrar reglas utiles.",
    "Marcar como supuesto cualquier extrapolacion inter-materia."
  ],
  "open_questions": [
    "Supuesto: la conclusion juridica aplica a todas actividades de antropologia; confirmar por consigna.",
    "Confirmar estandar unico de citacion de la licenciatura.",
    "Confirmar si LDE-S4B2 es clave oficial institucional o clave operativa local.",
    "Confirmar si el .bib canonical debe fijarse explicitamente en README sin placeholder.",
    "Confirmar rubricas de evaluacion por actividad para modular profundidad argumentativa."
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
      "Problema juridico o social.",
      "Conceptos y marco pertinente.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Cierre transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables y argumentados.",
      "Asegurar coherencia entre identidad institucional, estructura y calidad editorial."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Cierre con valor profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente -> interpretacion propia.",
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
        "Supuestos marcados",
        "Separacion de artefactos",
        "Trazabilidad bibliografica"
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
          "justification": "El analisis gana validez con respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion surge del razonamiento y no del resumen."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Trazabilidad bibliografica",
          "kind": "supports",
          "justification": "La pauta institucional exige integridad academica."
        }
      ],
      "evidence": [
        "README local fija identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico local fija ejes de trabajo y proposito.",
        "Bib local contiene base institucional verificable.",
        "Memoria origen confirma gates de parseo y normalizacion como reglas estables."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin perdida semantica.",
      "Se conservaron controles criticos de JSON parseable y normalizacion manual.",
      "Se transfirieron solo abstracciones estables del origen transversal.",
      "Se excluyeron referencias tematicas exclusivas de Filosofia del Derecho.",
      "Se reforzo manejo de supuestos y fuentes provisionales."
    ]
  }
}