{
  "summary": [
    "Se consolida transferencia lateral reutilizable desde Filosofia del Derecho hacia Etica y Moral juridica sin copiar redaccion especifica.",
    "Se preservan reglas utiles previas y se aplica deduplicacion lossless.",
    "Se refuerzan ejes editoriales comunes: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene validacion JSON estricta antes de propagacion recursiva.",
    "Se incorpora control de supuestos cuando falte consigna local verificable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como [Supuesto] todo dato no visible en la consigna de Actividad 7.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar trazabilidad de origen por ciclo y nodo fuente."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual de la actividad antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto final a la planeacion semanal de Actividad 7.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Incluir evidencia explicita en el desarrollo y no solo en la conclusion."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante y evitar solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar asumir fuentes de semanas o materias distintas sin validacion local.",
    "Confirmar que el tipo de entrega coincide con la consigna real de Actividad 7.",
    "Distinguir claramente entre descripcion de autores y posicion propia."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar esquema requerido completo antes de guardar memoria.",
    "Confirmar que no se eliminen reglas utiles previas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [Supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Permitir propagacion recursiva solo tras pasar todas las compuertas."
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
    "Mantener una clave canonica por obra y conservar aliases solo por retrocompatibilidad [Supuesto]."
  ],
  "propagation_hints": [
    "Propagar lateral y recursivo solo despues de validar JSON y estructura.",
    "Transferir solo patrones reutilizables, no conclusiones especificas de otra materia.",
    "Aplicar normalizacion manual si un nodo vecino entrega salida no estructurada.",
    "Evitar regresiones de reglas institucionales ya consolidadas.",
    "Cuando falte consigna local, propagar plantilla base y abrir preguntas."
  ],
  "open_questions": [
    "Confirmar consigna exacta y producto solicitado en Actividad 7.",
    "Confirmar rubrica de evaluacion para calibrar profundidad argumentativa.",
    "Confirmar fuentes obligatorias de la semana para Actividad 7.",
    "Confirmar politica final de aliases BibTeX para duplicados ya usados.",
    "Confirmar si procede limpieza del .bib truncado antes de nuevas propagaciones [Supuesto]."
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
        "Integridad academica con citas verificables.",
        "Carpeta de asignatura como entrada canonica.",
        "Validacion estructural previa a propagacion."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura destino: Etica y Moral juridica.",
        "Actividad destino: Actividad 7."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo o doctrinal.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir la planeacion semanal en productos argumentativos verificables.",
      "Asegurar coherencia entre consigna, desarrollo, evidencia y cierre.",
      "Mantener continuidad editorial entre nodos de la suite academica."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones claras y trazables.",
      "Citas explicitas y verificables.",
      "Supuestos etiquetados.",
      "Cierre con utilidad profesional juridica."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Definir conceptos operativos.",
      "Sustentar con norma, doctrina o fuente institucional.",
      "Contrastar posturas.",
      "Tomar posicion propia.",
      "Concluir con aplicacion juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco normativo o doctrinal",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Etica",
        "Moral",
        "Practica profesional juridica"
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
          "justification": "La pauta institucional exige citas verificables y trazabilidad."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El razonamiento parte del problema para construir postura."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida depende del analisis y la evidencia."
        },
        {
          "source": "Etica",
          "target": "Moral",
          "kind": "contrasts",
          "justification": "La distincion conceptual orienta la argumentacion en la asignatura."
        },
        {
          "source": "Moral",
          "target": "Practica profesional juridica",
          "kind": "depends_on",
          "justification": "La valoracion moral influye en criterios de actuacion juridica."
        }
      ],
      "evidence": [
        "README de la asignatura: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y ejes de trabajo.",
        "Archivo .bib local: base de fuentes y necesidad de control de duplicados.",
        "Memoria origen valida: patron transversal problema-conceptos-evidencia-analisis-conclusion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 19: se refuerza patron transversal sin copiar contenido especifico del nodo hermano.",
      "Ciclo 19: se mantiene bloqueo por no JSON parseable como compuerta obligatoria.",
      "Ciclo 19: se preservan reglas previas y se unifican duplicados por deduplicacion lossless."
    ]
  }
}