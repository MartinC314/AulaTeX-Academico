{
  "summary": [
    "Sincronizacion transversal consolidada con union-dedupe lossless y sin regresion.",
    "Se preserva identidad UnADM y contexto local de Antropologia de la cultura en Mexico.",
    "Se integran solo abstracciones estables del origen: objetivo, evidencia, analisis propio y cierre transferible.",
    "Se mantiene bloqueo de propagacion ante salida no JSON parseable y exigencia de normalizacion previa.",
    "Se refuerza resolucion de placeholders y rutas corruptas detectadas en README y programa analitico."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales.",
    "No trasladar metadatos curriculares de Filosofia del Derecho a Antropologia."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco teorico-normativo, analisis propio y cierre.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Mantener artefactos separados: reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias canonicas de estructura."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Evitar extrapolar contenidos tematicos exclusivos de otra materia.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar esquema minimo completo antes de reutilizar memoria.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que toda afirmacion tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregado y consigna real de la actividad."
  ],
  "latex_rules": [
    "Usar configuracion en espanol y codificacion consistente con la plantilla local.",
    "Mantener clase article, letterpaper y oneside salvo instruccion explicita.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Mantener coursename y coursecode locales salvo cambio institucional verificado.",
    "Resolver tokens dinamicos tipo $(@{...}.Slug) a nombres literales antes de compilar.",
    "Corregir rutas con caracteres truncados en README y referencias.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener claves BibTeX estables y trazables."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y abstraidas.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar propagar redaccion literal o contenidos tematicos de nodo no equivalente.",
    "Registrar alertas de parseo como memoria institucional reutilizable.",
    "Preservar reglas utiles previas; solo agregar mejoras verificables."
  ],
  "open_questions": [
    "Supuesto: falta consigna puntual de actividades especificas de Antropologia; confirmar formatos requeridos.",
    "Confirmar estandar de citacion oficial unico para la licenciatura.",
    "Confirmar si coursecode LDE-S4B2 es clave oficial o convencion local.",
    "Confirmar si la conclusion juridica aplica a todas las actividades de la materia o por tipo de tarea."
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
      "Problema claro.",
      "Conceptos pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables.",
      "Garantizar coherencia entre identidad institucional, metodo argumentativo y calidad tecnica."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados cuando falte evidencia directa.",
      "Cierre con utilidad juridica profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> respaldo verificable -> interpretacion propia.",
      "Pregunta guia -> desarrollo coherente -> respuesta final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON parseable",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Resolucion de placeholders en rutas y Slug"
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
          "justification": "La postura academica requiere sustento trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion util deriva del razonamiento argumentado."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "La pauta institucional exige integridad academica."
        },
        {
          "source": "Resolucion de placeholders en rutas y Slug",
          "target": "Normalizacion estructurada",
          "kind": "supports",
          "justification": "Evita errores de compilacion y ambiguedad documental."
        }
      ],
      "evidence": [
        "README local con ubicacion curricular y pauta editorial.",
        "Programa analitico con ejes problema-conceptos-producto-analisis-cierre.",
        "Bib local con entradas institucionales verificables.",
        "Regla heredada valida: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 53: se consolidan abstracciones estables de Filosofia del Derecho sin transferir contenido tematico especifico.",
      "Ciclo 53: se mantiene alerta institucional por salidas no estructuradas heredadas.",
      "Ciclo 53: se refuerza gate tecnico de placeholders y rutas corruptas en ecosistema LaTeX."
    ]
  }
}