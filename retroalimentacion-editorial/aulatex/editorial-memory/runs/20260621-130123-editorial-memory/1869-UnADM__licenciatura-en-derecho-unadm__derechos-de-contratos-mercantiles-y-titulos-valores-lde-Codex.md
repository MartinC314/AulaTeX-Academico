{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre actividad de origen y materia destino.",
    "Se preservan solo abstracciones editoriales estables y reutilizables.",
    "Se mantiene identidad UnADM, estructura argumentativa base y trazabilidad de fuentes.",
    "Se refuerza gate critico: bloquear propagacion si no hay JSON parseable.",
    "Se conserva contexto local verificado del destino: semestre 6, bloque 2, obligatoria, 8 creditos, .bib local existente.",
    "Supuesto: persiste alerta institucional por salidas no estructuradas hasta cierre formal de incidencia."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables a Licenciatura en Derecho y a la materia destino.",
    "Conservar tono juridico-formal, claro y argumentativo.",
    "Cerrar con postura academica propia y criterio juridico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Etiquetar como provisionales las fuentes heredadas no verificadas."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Definir objetivo puntual antes del desarrollo.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar en secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por la planeacion semanal.",
    "Mantener consistencia entre README, programa analitico, .tex y .bib."
  ],
  "activity_rules": [
    "Contextualizar cada actividad con problema concreto y delimitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir evidencia citada de interpretacion propia.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Comprobar trazabilidad entre citas en texto y archivo .bib.",
    "Evitar regresion de reglas utiles previamente consolidadas."
  ],
  "latex_rules": [
    "Usar espanol correcto con acentos consistentes en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir nombres truncados o anomalias de archivo antes de compilar.",
    "Resolver placeholders de slug en README y programa analitico.",
    "Evitar comandos no estandar sin justificacion editorial."
  ],
  "bibliography_rules": [
    "Usar como base el .bib local confirmado de la materia destino.",
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "No inventar referencias.",
    "Agregar solo obras realmente consultables.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente o URL.",
    "Agregar fecha de consulta en recursos web.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas normalizadas y deduplicadas.",
    "Transferir solo patrones estables; no transferir contenido tematico de Filosofia del Derecho.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Mantener compresion lossless por union-dedupe en cada ciclo.",
    "Conservar alerta institucional de normalizacion manual mientras siga abierta.",
    "Si falta contexto local, mantener cerebro minimo y abrir preguntas."
  ],
  "open_questions": [
    "Confirmar cierre formal de incidencias historicas de salida no JSON parseable.",
    "Confirmar correccion definitiva de placeholders de slug en README y programa.",
    "Confirmar si la plantilla de presentacion oficial difiere del reporte.",
    "Confirmar si year del sitio UnADM se mantiene fijo o solo con fecha de consulta.",
    "Confirmar rubricas de evaluacion por actividad para ajustar profundidad argumentativa."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Juridicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta canonica como punto de entrada."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 6, bloque 2, obligatoria, 8 creditos.",
        "Materia: Derechos de contratos mercantiles y titulos valores."
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Marco conceptual y normativo verificable.",
      "Analisis propio no descriptivo.",
      "Conclusion juridica transferible.",
      "Normalizacion estructurada previa a propagacion."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con trazabilidad y criterio juridico.",
      "Asegurar continuidad editorial institucional entre nodos no equivalentes sin contaminar contenido tematico."
    ],
    "style_markers": [
      "Apertura breve con problema.",
      "Secciones explicitas y ordenadas.",
      "Supuestos marcados cuando falte evidencia.",
      "Citas verificables en cada afirmacion relevante.",
      "Cierre con implicacion profesional."
    ],
    "argumentative_patterns": [
      "Problema -> marco normativo/doctrinal -> evidencia -> analisis propio -> conclusion.",
      "Afirmacion juridica siempre respaldada por fuente verificable.",
      "Consistencia estricta entre consigna, desarrollo y cierre."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "JSON parseable",
        "Normalizacion estructurada",
        "Problema juridico delimitado",
        "Marco normativo o doctrinal",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion transferible"
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
          "justification": "La identidad exige trazabilidad y citas verificables."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "JSON parseable",
          "kind": "depends_on",
          "justification": "La propagacion segura requiere estructura valida."
        },
        {
          "source": "Problema juridico delimitado",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin delimitacion no hay argumentacion pertinente."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "El cierre profesional requiere base juridica explicita."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura propia gana solidez con respaldo comprobable."
        }
      ],
      "evidence": [
        "README de materia con ubicacion curricular y pauta editorial.",
        "Programa analitico con ejes: problema, conceptos, producto, analisis y conclusion.",
        ".bib local existente con entradas institucionales verificables.",
        "Regla transversal vigente: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 6: deduplicacion completa de reglas repetidas.",
      "Ciclo 6: refuerzo de gates de calidad sobre parseo y normalizacion.",
      "Ciclo 6: transferencia conservadora sin contenido tematico del nodo origen.",
      "Ciclo 6: mantenimiento de supuestos abiertos y trazables."
    ]
  }
}