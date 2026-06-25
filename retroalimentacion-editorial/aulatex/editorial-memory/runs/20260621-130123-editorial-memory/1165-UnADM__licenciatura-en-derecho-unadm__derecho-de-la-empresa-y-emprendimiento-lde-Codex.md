{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre actividad de origen y materia destino.",
    "Se preserva el marco editorial estable: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene la regla de normalizacion estructurada obligatoria antes de propagacion recursiva.",
    "Se refuerza deduplicacion lossless por union sin recorte ni regresion.",
    "Se evita transferir doctrina especifica de Filosofia del Derecho por no equivalencia disciplinar.",
    "Se conserva alerta local por tokens Slug sin expandir y nombres de archivo con artefactos en README/programa."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial de la materia destino en todos los artefactos.",
    "Usar Licenciatura en Derecho como programa academico.",
    "Respetar contexto curricular local: semestre 6, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto cualquier dato no confirmado por consigna o archivo local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar desarrollo en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el entregable al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Conservar correspondencia entre README, .tex, presentacion y .bib."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Agregar fuentes especificas de actividad al .bib local.",
    "No asumir fuentes de semanas posteriores sin confirmacion de consigna.",
    "Verificar que el producto final coincida con la consigna de la actividad."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar o propagar.",
    "No eliminar reglas utiles previas durante fusion por union-dedupe.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Corregir placeholders y tokens sin expandir antes de generar entregables."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Actualizar documenttitle y documentsubtitle por actividad real.",
    "Verificar integridad de entornos y cierres antes de compilar."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos pertinentes al nodo destino.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No citar fuentes no registradas en el .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas abstractas estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar propagar redaccion literal o contenido doctrinal especifico de otra materia.",
    "Aplicar normalizacion manual cuando exista antecedente de salida no estructurada.",
    "Mantener estrategia progresiva y conservadora sin regresion."
  ],
  "open_questions": [
    "Supuesto: falta consigna puntual de actividades locales para granularidad por semana.",
    "Confirmar si el autor de plantilla debe parametrizarse por actividad.",
    "Confirmar valor final del Slug expandido en README y programa analitico.",
    "Confirmar correccion de nombres con artefactos de salto en README.",
    "Confirmar criterio local para year de unadmSitioWeb: bibliografico vs fecha de consulta."
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
      "Problema juridico activador.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible.",
      "Control explicito de supuestos."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables academicos verificables.",
      "Asegurar coherencia entre identidad institucional, argumentacion y evidencia.",
      "Permitir propagacion segura por estructura normalizada."
    ],
    "style_markers": [
      "Frases directas y accionables.",
      "Supuestos etiquetados de forma visible.",
      "Sin afirmaciones sin fuente.",
      "Cierre con aplicacion practica juridica."
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
        "Problema juridico",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Integridad bibliografica",
        "Control de supuestos"
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
          "justification": "La conclusion requiere respaldo normativo y documental."
        },
        {
          "source": "Control de supuestos",
          "target": "Integridad bibliografica",
          "kind": "supports",
          "justification": "Evita mezclar hechos confirmados con inferencias."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura de entregables",
          "kind": "develops",
          "justification": "Define tono, formato y estandar academico comun."
        }
      ],
      "evidence": [
        "README local con pauta editorial y ubicacion curricular.",
        "Programa analitico local con ejes de trabajo reutilizables.",
        "Archivo .bib local con claves institucionales base.",
        "Reglas heredadas de actividad origen normalizadas por deduplicacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 6: se preservan reglas utiles previas sin eliminacion.",
      "Ciclo 6: se deduplican variantes semanticas y ortograficas sin perdida funcional.",
      "Ciclo 6: se refuerzan gates de JSON parseable y estructura minima.",
      "Ciclo 6: se mantiene frontera transversal para no transferir doctrina no equivalente."
    ]
  }
}