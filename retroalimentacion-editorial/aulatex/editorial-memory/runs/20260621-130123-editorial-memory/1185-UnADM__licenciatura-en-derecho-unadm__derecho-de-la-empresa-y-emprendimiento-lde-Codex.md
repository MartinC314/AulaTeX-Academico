{
  "summary": [
    "Se consolida sincronizacion transversal entre actividad origen y materia destino con deduplicacion lossless.",
    "Se preservan reglas institucionales UnADM, normalizacion estructurada y control de supuestos.",
    "Se transfiere solo marco editorial estable y reusable; no se transfiere doctrina especifica de Filosofia del Derecho.",
    "Se refuerza estructura comun: problema, conceptos, evidencia, analisis propio y conclusion juridica transferible.",
    "Se mantienen alertas locales verificables: JSON invalido previo, tokens Slug sin expandir y posible truncamiento LaTeX."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial de la materia destino en todos los artefactos.",
    "Usar Licenciatura en Derecho como programa academico.",
    "Respetar contexto curricular local confirmado: semestre 6, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como supuesto todo dato no confirmado por consigna o archivo local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar desarrollo en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Conservar correspondencia entre README, programa analitico, .tex, presentacion y .bib."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Agregar fuentes especificas de actividad al .bib de la materia.",
    "No asumir fuentes de otras semanas o materias sin confirmacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar memoria.",
    "No eliminar reglas utiles previas durante fusion por union-dedupe.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y claves del archivo .bib.",
    "Normalizar manualmente cualquier salida no estructurada antes de propagacion recursiva."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir artefactos de nombres de archivo en README (ej. cortes de linea en 'reporte' y 'referencias').",
    "Verificar cierre completo de entornos LaTeX en reporte base [Supuesto: archivo local truncado en authortable]."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo obras consultables.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Mantener metadatos minimos: autor, titulo, año y fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Registrar fuentes de actividad en derecho-de-la-empresa-y-emprendimiento.bib.",
    "No citar fuentes no registradas en el .bib local."
  ],
  "propagation_hints": [
    "Propagar lateral y ascendentemente solo reglas estables y no disciplina-especificas.",
    "No propagar contenido doctrinal propio de Filosofia del Derecho a materias no equivalentes.",
    "Propagar alertas tecnicas reutilizables: JSON invalido, tokens sin expandir, control de supuestos.",
    "Mantener estrategia progresiva y conservadora: reforzar sin reemplazar reglas locales validas.",
    "Aplicar validacion estructural antes de cada salto recursivo."
  ],
  "open_questions": [
    "Confirmar consigna y rubrica de la primera actividad local para ajustar profundidad argumentativa.",
    "Confirmar si documentauthor debe parametrizarse por actividad.",
    "Confirmar expansion final del Slug en README y programa analitico.",
    "Confirmar si el reporte .tex esta truncado en repositorio o solo en captura.",
    "Confirmar criterio institucional para year=2026 en unadmSitioWeb (año bibliografico vs fecha de consulta)."
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
        "Enfoque en transferencia profesional."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo pertinente.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y utiles para la practica juridica.",
      "Asegurar calidad editorial uniforme en reportes y presentaciones.",
      "Preservar memoria institucional sin regresiones."
    ],
    "style_markers": [
      "Frases directas y verificables.",
      "Supuestos marcados de forma explicita.",
      "Sin afirmaciones sin fuente.",
      "Cierre aplicado a contexto profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis propio -> conclusion.",
      "Marco normativo como soporte del criterio personal.",
      "Consistencia entre pregunta guia y respuesta final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Control de supuestos",
        "Evidencia verificable",
        "Conclusion juridica transferible",
        "Integridad bibliografica",
        "Correspondencia documental README-programa-.tex-.bib"
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
          "justification": "La conclusion exige respaldo normativo y documental."
        },
        {
          "source": "Control de supuestos",
          "target": "Integridad bibliografica",
          "kind": "supports",
          "justification": "Evita mezclar hechos confirmados con inferencias."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Correspondencia documental README-programa-.tex-.bib",
          "kind": "develops",
          "justification": "La identidad se materializa en metadatos y estructura consistente."
        }
      ],
      "evidence": [
        "README local con ubicacion curricular y pauta editorial.",
        "Programa analitico local con ejes de trabajo reutilizables.",
        ".bib local con claves base institucionales verificables.",
        "Memoria origen con gates de JSON, supuestos y trazabilidad."
      ]
    },
    "reinforcement_log": [
      "Ciclo 11: se deduplican reglas repetidas y se conserva cobertura completa sin recorte.",
      "Ciclo 11: se incorpora marco argumentativo estable desde origen por relacion transversal.",
      "Ciclo 11: se mantiene exclusion de contenido doctrinal no equivalente entre materias.",
      "Ciclo 11: se sostienen alertas tecnicas locales verificables (Slug, artefactos README, truncamiento LaTeX)."
    ]
  }
}