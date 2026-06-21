{
  "summary": [
    "Sincronizacion transversal consolidada con compresion lossless por union-dedupe.",
    "Se preservan reglas institucionales UnADM, estructura canonica y gates de calidad.",
    "Se transfieren solo abstracciones estables desde Filosofia del Derecho a Antropologia.",
    "Se evita migrar contenido tematico especifico de Filosofia del Derecho.",
    "Se mantiene alerta por salidas no JSON parseables heredadas y normalizacion obligatoria."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener ubicacion curricular local del destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar toda fuente heredada no verificada como provisional.",
    "No trasladar metadatos curriculares de otras materias al destino."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco normativo o teorico, analisis propio y cierre.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Mantener separados reporte, presentacion y bibliografia.",
    "Usar README y programa analitico locales como guias primarias."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Sustentar afirmaciones relevantes con fuente verificable y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Cerrar con conclusion transferible a la practica juridica.",
    "Evitar afirmaciones juridicas o culturales sin puente argumentativo."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar esquema minimo completo antes de reutilizar memoria.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que cada supuesto este marcado como supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregado y consigna local."
  ],
  "latex_rules": [
    "Conservar plantilla .tex local como base de trabajo.",
    "Usar configuracion en espanol consistente y acentos correctos.",
    "Mantener clase y formato base salvo justificacion academica.",
    "Actualizar documenttitle y documentsubtitle por actividad real.",
    "Resolver placeholders y tokens dinamicos en README, programa y rutas.",
    "Corregir rutas con caracteres truncados antes de compilar.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes especificas de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No citar claves inexistentes en el .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y abstractas.",
    "Mantener estrategia progresiva y conservadora sin regresion.",
    "Aplicar union-dedupe en cada ciclo para preservar memoria util.",
    "Transferir identidad, estructura reusable, gates y grafo conceptual.",
    "Etiquetar incidencias de parseo como alertas reutilizables inter-nodos.",
    "Mantener como provisionales las reglas heredadas no verificadas localmente."
  ],
  "open_questions": [
    "Supuesto: falta consigna puntual de actividades del destino; confirmar formatos exigidos por semana.",
    "Confirmar estandar institucional unico de citacion para la licenciatura.",
    "Confirmar si LDE-S4B2 es clave oficial o convencion local.",
    "Confirmar si toda actividad del destino exige cierre juridico explicito.",
    "Confirmar si persisten tokens dinamicos en otros archivos no inspeccionados."
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
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura destino: Antropologia de la cultura en Mexico.",
        "Semestre 4, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema, conceptos, evidencia, analisis propio y conclusion transferible.",
      "Normalizacion estructurada antes de propagar.",
      "Compresion lossless por deduplicacion sin recorte.",
      "Sincronizacion transversal con fronteras disciplinares claras."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables y utiles.",
      "Preservar identidad institucional y calidad metodologica entre nodos.",
      "Asegurar continuidad editorial sin contaminar contexto local."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos etiquetados.",
      "Citas verificables en cada afirmacion clave.",
      "Cierre con valor profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente verificable -> interpretacion propia.",
      "Coherencia completa entre consigna, desarrollo y cierre."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Validacion JSON parseable",
        "Normalizacion estructurada",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Transferencia transversal de abstracciones estables"
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
          "source": "Integridad academica",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "La integridad exige trazabilidad y respaldo documental."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura personal gana validez con fuentes comprobables."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion profesional deriva del razonamiento argumentado."
        },
        {
          "source": "Transferencia transversal de abstracciones estables",
          "target": "Identidad institucional UnADM",
          "kind": "supports",
          "justification": "Permite sincronizar reglas sin mover contenido tematico ajeno."
        }
      ],
      "evidence": [
        "README local define identidad UnADM y ubicacion curricular.",
        "Programa analitico local fija ejes problema-conceptos-producto-analisis-cierre.",
        "Bib local incluye fuentes institucionales verificables.",
        "Memoria origen refuerza normalizacion y bloqueo por JSON invalido."
      ]
    },
    "reinforcement_log": [
      "Ciclo 36: se consolidan reglas transversales estables sin copiar redaccion literal del origen.",
      "Ciclo 36: se refuerza gate de JSON parseable y normalizacion previa.",
      "Ciclo 36: se preserva nucleo argumentativo comun y se excluye contenido tematico de Filosofia del Derecho.",
      "Ciclo 36: se mantiene estado provisional para fuentes heredadas no verificadas."
    ]
  }
}