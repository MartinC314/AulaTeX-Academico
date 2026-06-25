{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre actividad de origen y materia destino.",
    "Se preservan reglas utiles previas y se aplica deduplicacion lossless.",
    "Se refuerza marco estable reusable: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene bloqueo de propagacion para salidas no JSON parseables.",
    "Se conserva alerta local por tokens Slug sin expandir y artefactos en nombres de archivo.",
    "No se transfiere doctrina especifica de Filosofia del Derecho por no equivalencia disciplinar."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial de la materia destino en todos los artefactos.",
    "Usar Licenciatura en Derecho como programa academico.",
    "Respetar contexto curricular local: semestre 6, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no confirmado por consigna o archivo local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear el entregable al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Conservar correspondencia entre README, .tex, presentacion y .bib."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante y evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Agregar fuentes especificas de actividad al .bib local.",
    "No asumir fuentes de otras semanas sin confirmacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizar memoria.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y claves del .bib.",
    "No eliminar reglas utiles previas durante fusion por union-dedupe.",
    "No propagar datos locales no confirmados como reglas institucionales."
  ],
  "latex_rules": [
    "Compilar sin errores criticos ni referencias rotas.",
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir artefactos de nombres de archivo antes de compilar.",
    "Verificar integridad de entornos LaTeX y cierre de tablas en reporte."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo obras consultables.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Mantener bibliografia base local y separar bibliografia especifica por actividad.",
    "No citar fuentes ausentes del .bib local.",
    "Marcar como supuesto cualquier inferencia sobre archivo .bib canonicamente esperado."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo abstracciones editoriales estables.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferir redaccion literal o doctrina especifica entre materias no equivalentes.",
    "Aplicar propagacion recursiva solo tras validar JSON y estructura.",
    "Mantener estrategia progresiva y conservadora sin regresiones."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de actividades locales; confirmar productos exactos por semana.",
    "Confirmar si autor de plantilla debe parametrizarse por actividad.",
    "Confirmar expansion final del Slug en README y programa analitico.",
    "Confirmar si year=2026 en unadmSitioWeb se mantiene como anio bibliografico o solo fecha de consulta.",
    "Confirmar estado real del truncamiento en reporte .tex local."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con trazabilidad bibliografica.",
        "Entrada canonica por carpeta de materia."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 6, bloque 2, obligatoria, 8 creditos.",
        "Transferencia profesional como criterio de cierre."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo pertinente.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible.",
      "Control explicito de supuestos."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables academicos trazables y utiles.",
      "Garantizar calidad estructural, argumentativa y bibliografica.",
      "Sostener continuidad editorial entre nodos sin contaminar contexto disciplinar."
    ],
    "style_markers": [
      "Frases claras y directas.",
      "Supuestos etiquetados.",
      "Sin afirmaciones sin fuente.",
      "Cierre con aplicacion practica."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis propio -> conclusion.",
      "Marco normativo y doctrinal como soporte del criterio personal.",
      "Consistencia entre pregunta guia y respuesta final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Problema juridico",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Control de supuestos",
        "Integridad bibliografica"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin JSON valido no hay transferencia segura."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion requiere respaldo documental."
        },
        {
          "source": "Control de supuestos",
          "target": "Integridad argumentativa",
          "kind": "supports",
          "justification": "Distingue hechos confirmados de inferencias."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura de entregables",
          "kind": "supports",
          "justification": "Define tono, formato y criterios comunes."
        }
      ],
      "evidence": [
        "README local: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico local: proposito y ejes de trabajo.",
        "Archivo .bib local: base institucional verificable.",
        "Memoria origen: gates de calidad y estructura argumentativa reusable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 20: deduplicacion lossless aplicada sin eliminar reglas utiles.",
      "Ciclo 20: reforzada abstraccion transversal de estructura y calidad.",
      "Ciclo 20: retenida alerta tecnica de Slug sin expandir y artefactos de archivo.",
      "Ciclo 20: excluida transferencia de contenido doctrinal especifico por no equivalencia."
    ]
  }
}