{
  "summary": [
    "Se consolida refuerzo lateral desde Filosofia del Derecho hacia Etica y Moral juridica con deduplicacion lossless.",
    "Se preservan reglas utiles previas y se normalizan variantes duplicadas sin recorte semantico.",
    "Se refuerzan ejes comunes reutilizables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene validacion JSON estricta antes de propagacion recursiva.",
    "Se conserva trazabilidad de fuentes provisionales y marcado explicito de supuestos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como [Supuesto] todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Citar malla-curricular-derecho-unadm.pdf para sustento de ubicacion curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Integrar evidencia verificable en el desarrollo.",
    "Alinear el producto final a la planeacion semanal de la actividad.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar afirmaciones sin respaldo documental.",
    "Confirmar que el tipo de entrega corresponde a la consigna de Actividad 7.",
    "No asumir fuentes de semanas o materias distintas sin validacion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar esquema requerido completo antes de guardar memoria.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no se eliminen reglas utiles previas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de [Supuesto].",
    "Validar correspondencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir caracteres anomalos en rutas o nombres antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de Actividad 7 en etica-y-moral-juridica.bib.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, anio, editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener clave canonica y alias controlados en duplicados bibliograficos. [Supuesto]",
    "No normalizar masivo si el .bib esta truncado; abrir incidencia primero. [Supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo patrones reutilizables, no redaccion literal ni conclusiones especificas.",
    "Aplicar analogia controlada: conservar marco editorial comun y adaptar contenido a consigna local.",
    "Evitar regresiones de calidad respecto a ciclos previos.",
    "Si faltan datos locales, propagar estructura base y abrir preguntas en lugar de inventar contenido."
  ],
  "open_questions": [
    "Confirmar consigna exacta y producto solicitado en Actividad 7.",
    "Confirmar rubrica de evaluacion especifica para calibrar profundidad argumentativa.",
    "Confirmar politica local de alias BibTeX para duplicados existentes.",
    "Confirmar si se corrige primero el .bib truncado antes de nuevas normalizaciones. [Supuesto]",
    "Confirmar fuentes obligatorias de la semana correspondiente a Actividad 7."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Sobrio y verificable."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta de asignatura como entrada canonica.",
        "Validacion estructural previa a propagacion."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura destino: Etica y Moral juridica."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo o doctrinal.",
      "Evidencia verificable.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos con fundamento juridico y criterio propio.",
      "Asegurar coherencia entre identidad institucional, estructura argumentativa y calidad verificable."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Secciones claras y trazables.",
      "Citas explicitas y verificables.",
      "Supuestos etiquetados.",
      "Cierre aplicable a practica profesional."
    ],
    "argumentative_patterns": [
      "Delimitacion del problema.",
      "Marco conceptual y normativo.",
      "Contraste de posturas con evidencia.",
      "Toma de posicion del estudiante.",
      "Conclusion aplicable al ejercicio juridico."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Etica",
        "Moral",
        "Practica juridica"
      ],
      "citations": [
        "malla-curricular-derecho-unadm.pdf",
        "programa-analitico-etica-y-moral-juridica.md",
        "etica-y-moral-juridica.bib"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La identidad institucional exige citas verificables y trazabilidad."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El razonamiento parte del problema para construir postura."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida deriva de fuentes y analisis."
        },
        {
          "source": "Etica",
          "target": "Moral",
          "kind": "contrasts",
          "justification": "La distincion conceptual orienta el analisis de la materia."
        },
        {
          "source": "Moral",
          "target": "Practica juridica",
          "kind": "depends_on",
          "justification": "La valoracion moral incide en criterios de actuacion profesional."
        }
      ],
      "evidence": [
        "README de asignatura: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito de realizacion y ejes de trabajo.",
        "Reglas base del origen: estructura argumentativa y compuertas de calidad reutilizables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 6: se incorporan patrones transversales validados del origen sin copiar contenido especifico de Filosofia del Derecho.",
      "Ciclo 6: se deduplican reglas equivalentes y se conserva cobertura completa por union lossless.",
      "Ciclo 6: se mantiene control de supuestos y bloqueo por no-JSON como invariantes de calidad."
    ]
  }
}