{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia progresiva y conservadora.",
    "Se preservan reglas validas del destino y del origen sin regresion.",
    "Se transfieren solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Se refuerzan identidad UnADM, estructura reusable, gates de calidad y grafo conceptual.",
    "Se mantiene alerta de salidas no JSON parseable como riesgo operativo recurrente."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener contexto curricular local del destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar toda fuente heredada no verificada como provisional.",
    "No transferir metadatos curriculares especificos de Filosofia del Derecho al destino."
  ],
  "structure_rules": [
    "Iniciar con objetivo puntual y encuadre del problema juridico o social.",
    "Usar secuencia reusable: problema, conceptos, evidencia, analisis propio, conclusion.",
    "Separar artefactos: reporte, presentacion y bibliografia.",
    "Alinear cada entrega al producto solicitado por la planeacion semanal.",
    "Usar README y programa analitico como guias canonicas de estructura.",
    "Resolver placeholders de archivos antes de compilar o citar."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar extrapolar fuentes o contenidos de semanas no confirmadas.",
    "Cerrar con conclusion transferible a la practica juridica."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar memoria.",
    "Revisar y normalizar manualmente respuestas no estructuradas heredadas.",
    "Confirmar consistencia entre citas en texto y archivo .bib.",
    "Comprobar correspondencia entre producto entregado y consigna vigente.",
    "No promover reglas provisionales a definitivas sin validacion local."
  ],
  "latex_rules": [
    "Mantener plantilla .tex base de la materia destino.",
    "Usar configuracion de espanol y acentos coherente en .tex y .bib.",
    "Mantener claves BibTeX estables y trazables.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir rutas truncadas y tokens dinamicos sin expandir en README, programa y .tex."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes especificas por actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Marcar como supuesto cualquier correspondencia bibliografica no confirmada."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas ya validadas por gates.",
    "Transferir solo abstracciones estables; no redaccion literal ni temario ajeno.",
    "Mantener compresion lossless por union-dedupe sin eliminar reglas utiles previas.",
    "Registrar incidencias de parseo como alertas reutilizables inter-materias.",
    "Preservar identidad local del destino al recibir reglas transversales."
  ],
  "open_questions": [
    "Supuesto: falta consigna local detallada de actividades especificas; confirmar formatos exactos.",
    "Confirmar estandar de citacion oficial transversal de la licenciatura.",
    "Confirmar si la conclusion juridica es obligatoria en todas las actividades de antropologia.",
    "Confirmar si la clave LDE-S4B2 permanece oficial en todos los artefactos.",
    "Confirmar resolucion definitiva de placeholders tipo $(@{...}.Slug) en todos los documentos."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro, preciso y argumentativo.",
        "Orientado a trazabilidad y criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Entrada canonica por carpeta de materia."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Destino: Antropologia de la cultura en Mexico.",
        "Contexto local vigente: semestre 4, bloque 2, obligatoria, 8 creditos."
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
      "Convertir planeacion semanal en productos academicos consistentes y verificables.",
      "Garantizar continuidad editorial transversal sin perder identidad local.",
      "Asegurar calidad formal, argumentativa y bibliografica en LaTeX."
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
      "Consigna -> desarrollo alineado -> cierre coherente."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON parseable",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Sincronizacion transversal conservadora"
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
          "justification": "El argumento propio se legitima con respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion util surge del razonamiento, no del resumen."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Sincronizacion transversal conservadora",
          "kind": "supports",
          "justification": "La identidad comun permite reglas compartidas sin romper contexto local."
        }
      ],
      "evidence": [
        "README destino confirma identidad UnADM y pauta editorial.",
        "Programa analitico destino confirma ejes de trabajo reutilizables.",
        ".bib local confirma base institucional minima verificable.",
        "Memoria origen aporta gates de parseo y normalizacion estructurada."
      ]
    },
    "reinforcement_log": [
      "Ciclo 93: deduplicacion completada sin recorte semantico.",
      "Ciclo 93: se conservaron reglas utiles previas del destino.",
      "Ciclo 93: se agregaron abstracciones estables del origen no tematicas.",
      "Ciclo 93: se mantuvo separacion entre contenido disciplinar y reglas editoriales transversales."
    ]
  }
}