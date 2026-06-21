{
  "summary": [
    "Sincronizacion transversal conservadora aplicada con union-dedupe lossless.",
    "Se preserva identidad UnADM y estructura canonica del nodo materia.",
    "Se incorporan abstracciones estables del origen: objetivo, evidencia, analisis propio y coherencia.",
    "Se evita transferir contenido tematico exclusivo de Filosofia del Derecho.",
    "Se refuerza gate de normalizacion: no propagar salidas no JSON parseable.",
    "Se mantiene alerta de fuentes heredadas no verificadas como provisionales.",
    "Se consolida resolucion obligatoria de placeholders tipo $(@{...}.Slug)."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No trasladar metadatos curriculares de Filosofia del Derecho al destino."
  ],
  "structure_rules": [
    "Iniciar cada entrega con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco teorico/normativo, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por planeacion semanal.",
    "Separar artefactos: reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias de estructura reutilizable.",
    "Resolver nombres/rutas corruptas o truncadas antes de compilar."
  ],
  "activity_rules": [
    "Sustentar afirmaciones relevantes con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar resumen descriptivo puro.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion transferible a practica juridica cuando la consigna lo permita [supuesto].",
    "No asumir que fuentes de otras semanas o materias aplican automaticamente."
  ],
  "quality_gates": [
    "Bloquear propagacion si salida no es JSON parseable.",
    "Exigir esquema minimo completo antes de reutilizar memoria.",
    "Normalizar manualmente respuestas no estructuradas de ciclos heredados.",
    "Verificar trazabilidad de cada afirmacion o marcarla como supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No promover reglas provisionales a definitivas sin validacion disciplinar.",
    "Confirmar correspondencia entre entregable y consigna local."
  ],
  "latex_rules": [
    "Mantener plantilla .tex local como base editorial.",
    "Conservar configuracion en espanol y acentos correctos en .tex/.bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, referencias rotas ni placeholders sin resolver.",
    "Resolver tokens dinamicos $(@{...}.Slug) a nombres literales antes de usar.",
    "Verificar rutas de README/programa/.tex antes de referenciarlas."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo obras verificables y consultables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales pertinentes.",
    "Registrar fuentes especificas por actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/editorial/URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "No citar entradas inexistentes en .bib local.",
    "Mantener unadmSitioWeb y unadmMallaDerecho2024 como base institucional."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y abstractas entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar propagar redaccion literal o contenido tematico de otra materia.",
    "Registrar incidencias de parseo como alerta transversal reutilizable.",
    "Preservar reglas utiles previas sin regresion en ciclos siguientes.",
    "Si falta contexto local, crear minimo viable y abrir preguntas."
  ],
  "open_questions": [
    "Confirmar rubrica oficial de evaluacion para actividades de la materia.",
    "Confirmar si la conclusion juridica aplica a todas las actividades antropologicas o solo algunas [supuesto].",
    "Confirmar estandar de citacion institucional unico (APA u otro).",
    "Confirmar si LDE-S4B2 es clave oficial institucional o clave local.",
    "Confirmar que no quedan placeholders en archivos no inspeccionados."
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
        "Semestre 4, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Antropologia de la cultura en Mexico."
      ]
    },
    "essence": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Normalizacion estructurada previa a toda propagacion.",
      "Compresion lossless por union-dedupe sin recorte semantico.",
      "Transferencia transversal por abstracciones estables."
    ],
    "reason_for_being": [
      "Orientar productos academicos consistentes, verificables y transferibles.",
      "Convertir planeacion semanal en entregables con fundamento y postura propia."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Supuestos etiquetados cuando falte evidencia local.",
      "Secciones funcionales y cierre profesional.",
      "Citas verificables con coherencia biblica."
    ],
    "argumentative_patterns": [
      "Afirmacion -> evidencia -> interpretacion -> implicacion.",
      "Problema contextual -> marco conceptual -> analisis propio -> conclusion.",
      "Coherencia vertical entre consigna, desarrollo y cierre."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON parseable",
        "Evidencia verificable",
        "Analisis propio",
        "Coherencia argumentativa",
        "Conclusion transferible"
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
          "justification": "La postura se sostiene con respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion util deriva del razonamiento."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Coherencia argumentativa",
          "kind": "supports",
          "justification": "La pauta institucional exige claridad y consistencia."
        }
      ],
      "evidence": [
        "README destino confirma identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico confirma ejes de trabajo reutilizables.",
        ".bib local contiene base institucional verificable.",
        "Memoria origen aporta gates de parseo y normalizacion transferibles."
      ]
    },
    "reinforcement_log": [
      "Ciclo 3: deduplicacion semantica completada sin eliminar reglas utiles previas.",
      "Ciclo 3: reforzada regla de no propagar no-JSON y de normalizacion manual heredada.",
      "Ciclo 3: integrada abstraccion objetivo-evidencia-analisis-conclusion como patron transversal.",
      "Ciclo 3: excluido contenido tematico especifico de Filosofia por no equivalencia de nodo."
    ]
  }
}