{
  "summary": [
    "Sincronizacion transversal aplicada con compresion union-dedupe lossless.",
    "Se preservan reglas utiles previas sin regresion.",
    "Se transfieren solo abstracciones editoriales estables desde actividad de otra materia.",
    "Se refuerzan identidad UnADM, estructura reusable y gates de calidad.",
    "Se evita mover contenido tematico exclusivo de Filosofia del Derecho al destino.",
    "Se mantiene alerta por salidas no JSON parseables heredadas y su normalizacion obligatoria."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar toda fuente heredada no verificada como provisional.",
    "No trasladar metadatos curriculares de otra asignatura al destino."
  ],
  "structure_rules": [
    "Iniciar cada entrega con objetivo puntual y encuadre del problema.",
    "Mantener secuencia reusable: problema, conceptos, evidencia, analisis propio y cierre.",
    "Separar artefactos: reporte, presentacion y bibliografia.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Usar README y programa analitico como guias rectoras.",
    "Resolver placeholders y tokens dinamicos antes de compilar o citar rutas."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Sustentar afirmaciones relevantes con fuente verificable y cita explicita.",
    "Distinguir evidencia, interpretacion y opinion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion transferible a practica juridica o profesional.",
    "Evitar asumir fuentes de otras semanas o materias sin validacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Exigir estructura minima completa del esquema antes de reutilizar.",
    "Normalizar manualmente respuestas no estructuradas heredadas.",
    "Confirmar que afirmaciones sin respaldo esten marcadas como supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto final y consigna real."
  ],
  "latex_rules": [
    "Conservar plantilla .tex local como base editorial.",
    "Mantener configuracion en espanol, letterpaper y oneside salvo instruccion distinta.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Mantener acentos y codificacion correctos en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir rutas truncadas y tokens sin expandir en README, programa y .tex."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes consultables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes especificas de cada actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Mantener trazabilidad entre cita textual y entrada BibTeX.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y estables.",
    "Propagar transversalmente identidad, estructura y gates; no redaccion literal.",
    "Mantener compresion union-dedupe sin eliminar reglas utiles previas.",
    "Etiquetar incidentes de parseo como alertas reutilizables inter-materias.",
    "Si falta contexto local, conservar cerebro minimo y abrir vacios como preguntas."
  ],
  "open_questions": [
    "Supuesto: falta consigna puntual de la proxima actividad en destino; confirmar formato exacto.",
    "Confirmar estandar de citacion institucional unico para la licenciatura.",
    "Confirmar si conclusion juridica aplica a todas las actividades de la materia o segun consigna.",
    "Confirmar si LDE-S4B2 es clave oficial definitiva o local.",
    "Confirmar que no existan placeholders restantes en archivos de la materia."
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
      "Problema claro al inicio.",
      "Conceptos pertinentes y delimitados.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Cierre transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos solidos y verificables.",
      "Asegurar coherencia entre consigna, desarrollo y resultado.",
      "Preservar calidad institucional en entregables LaTeX."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados cuando falte evidencia.",
      "Citas trazables en cada afirmacion clave.",
      "Conclusion con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente -> interpretacion propia.",
      "Consigna -> desarrollo alineado -> verificacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON parseable",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion transferible",
        "Coherencia argumentativa",
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
          "justification": "Sin JSON valido no hay propagacion confiable."
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
          "justification": "La conclusion util surge del razonamiento y no del resumen."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Coherencia argumentativa",
          "kind": "supports",
          "justification": "El marco institucional exige claridad, rigor y consistencia."
        }
      ],
      "evidence": [
        "README de destino confirma identidad UnADM y pauta editorial.",
        "Programa analitico confirma ejes de trabajo reutilizables.",
        "Bib local confirma base institucional verificable.",
        "Historial heredado confirma gate de JSON parseable y normalizacion manual."
      ]
    },
    "reinforcement_log": [
      "Ciclo 68: deduplicacion completa de reglas repetidas.",
      "Ciclo 68: transferencia conservadora de abstracciones estables desde nodo transversal.",
      "Ciclo 68: exclusion explicita de contenidos tematicos no equivalentes.",
      "Ciclo 68: refuerzo de gates de parseo, trazabilidad y consistencia bibliografica."
    ]
  }
}