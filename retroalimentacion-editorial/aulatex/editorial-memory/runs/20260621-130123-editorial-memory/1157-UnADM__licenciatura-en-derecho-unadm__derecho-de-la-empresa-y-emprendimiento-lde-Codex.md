{
  "summary": [
    "Se consolida sincronizacion transversal con transferencia de abstracciones estables desde actividad de otra materia.",
    "Se preservan reglas utiles vigentes del destino sin regresion y con deduplicacion lossless.",
    "Se refuerza el marco editorial reusable: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene obligatoria la normalizacion estructurada antes de propagacion recursiva.",
    "Se conserva alerta local por tokens Slug sin expandir y nombres de archivo con artefactos en README y programa."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial de la materia destino en todos los artefactos.",
    "Usar Licenciatura en Derecho como programa academico.",
    "Respetar contexto curricular local: semestre 6, bloque 2, obligatoria, 8 creditos.",
    "Marcar como supuesto cualquier dato no visible en la consigna o no confirmado por archivo local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Usar la carpeta de materia como punto de entrada canonico."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Conservar correspondencia entre reporte, presentacion y bibliografia local.",
    "Usar README y programa analitico como guias operativas de estructura."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante y evitar entregas solo descriptivas.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Identificar problema, conceptos pertinentes, evidencia y aplicacion practica.",
    "Agregar fuentes especificas de actividad al .bib de la materia.",
    "No asumir fuentes o requisitos de semanas no confirmadas para la actividad."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar memoria.",
    "No eliminar reglas utiles previas durante fusion por union-dedupe.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo, lateral o ascendente.",
    "Verificar correspondencia del producto con la consigna local de actividad.",
    "No propagar datos locales no confirmados como reglas institucionales."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo con artefactos antes de compilar.",
    "Verificar integridad sintactica del .tex y cierre de entornos truncados.",
    "Actualizar documenttitle y documentsubtitle segun actividad real."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo obras verificables.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos pertinentes al tema local.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No citar fuentes no incluidas en el .bib local.",
    "Mantener y reutilizar claves base locales unadmSitioWeb y unadmMallaDerecho2024."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo reglas generales de identidad, estructura y calidad.",
    "Evitar transferir contenido doctrinal especifico de Filosofia del Derecho al destino por no equivalencia disciplinar.",
    "Aplicar estrategia progresiva y conservadora: primero normalizar, luego expandir.",
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Mantener alertas tecnicas de plantillas solo en nodos con sintomas equivalentes."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de actividades locales; confirmar producto exacto por semana.",
    "Confirmar si autor visible en plantilla se parametriza por actividad o se conserva fijo.",
    "Confirmar valor final del Slug expandido en README y programa analitico.",
    "Confirmar si year=2026 en unadmSitioWeb se mantiene como anio bibliografico o solo fecha de consulta.",
    "Confirmar reparacion completa del archivo de reporte truncado y cierres de entornos."
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
        "Integridad academica y trazabilidad bibliografica.",
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 6, bloque 2, obligatoria, 8 creditos.",
        "Enfoque en transferencia profesional."
      ]
    },
    "essence": [
      "Problema juridico.",
      "Conceptos y marco normativo.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible.",
      "Control de supuestos."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables claros, verificables y utiles para practica juridica.",
      "Asegurar coherencia entre identidad institucional, metodo argumentativo y trazabilidad de fuentes."
    ],
    "style_markers": [
      "Frases directas y verificables.",
      "Supuestos marcados de forma explicita.",
      "Sin afirmaciones sin fuente.",
      "Cierre con aplicacion practica."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Marco normativo y doctrinal soporta postura propia.",
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
        "Integridad bibliografica",
        "Control de supuestos",
        "Consigna de actividad"
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
          "target": "Integridad bibliografica",
          "kind": "supports",
          "justification": "Evita mezclar inferencias con datos confirmados."
        },
        {
          "source": "Consigna de actividad",
          "target": "Estructura de entregable",
          "kind": "depends_on",
          "justification": "El formato final debe responder a la instruccion local."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura de entregable",
          "kind": "supports",
          "justification": "Define tono, metadatos y estandar academico."
        }
      ],
      "evidence": [
        "README local de materia.",
        "Programa analitico local.",
        "Archivo .bib local con claves base institucionales.",
        "Memoria previa de destino con alertas de normalizacion y placeholders."
      ]
    },
    "reinforcement_log": [
      "Ciclo 4: se refuerzan reglas transversales estables sin mover contenido doctrinal especifico del origen.",
      "Ciclo 4: se preservan quality gates de JSON parseable y normalizacion previa.",
      "Ciclo 4: se mantiene alerta tecnica por Slug sin expandir y truncamiento LaTeX local.",
      "Ciclo 4: deduplicacion aplicada sin recorte semantico de reglas utiles."
    ]
  }
}