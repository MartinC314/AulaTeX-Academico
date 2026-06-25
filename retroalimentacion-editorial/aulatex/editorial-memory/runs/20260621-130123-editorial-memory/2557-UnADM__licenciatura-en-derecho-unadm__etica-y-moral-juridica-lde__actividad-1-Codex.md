{
  "summary": [
    "Se consolida transferencia lateral desde Filosofia del Derecho hacia Etica y Moral juridica con deduplicacion lossless.",
    "Se preservan reglas institucionales, estructurales y de calidad reutilizables ya verificadas.",
    "Se refuerza la normalizacion obligatoria: solo JSON parseable y con esquema completo.",
    "Se mantiene el nucleo editorial comun: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se evita transferir conclusiones o bibliografia exclusiva del nodo hermano."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Marcar como [Supuesto] todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Citar malla-curricular-derecho-unadm.pdf para ubicacion curricular."
  ],
  "structure_rules": [
    "Responder y almacenar memoria solo en JSON valido y parseable.",
    "Usar frases cortas, accionables y sin duplicados.",
    "No eliminar reglas utiles previas; solo unir y deduplicar.",
    "Aplicar compresion lossless por deduplicacion, no por recorte.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el entregable al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo resumen descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar asumir fuentes de semanas posteriores para Actividad 1.",
    "Confirmar que el producto final coincide con la consigna de Actividad 1.",
    "Integrar fundamento juridico, evidencia y transferencia profesional en cada producto."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin etiqueta [Supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar deduplicacion semantica sin perdida de reglas vigentes."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo anomalos en README antes de referenciarlos."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de la actividad en etica-y-moral-juridica.bib.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano, editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Deduplicar claves duplicadas en .bib sin perder informacion bibliografica."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo patrones reutilizables, no redaccion literal ni conclusiones especificas.",
    "Mantener trazabilidad de origen, destino y ciclo en cada consolidacion.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Si faltan datos locales, propagar estructura base y abrir preguntas en vez de inventar contenido."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 1 en Etica y Moral juridica.",
    "Confirmar si el producto requerido es reporte, presentacion u otro formato.",
    "Confirmar rubrica de evaluacion especifica para calibrar profundidad argumentativa.",
    "Confirmar criterio canonico para deduplicar entradas duplicadas en etica-y-moral-juridica.bib.",
    "Confirmar fuentes obligatorias de la semana para Actividad 1."
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
        "Carpeta de asignatura como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Etica y Moral juridica."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo o doctrinal.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica aplicable."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables academicos solidos.",
      "Sostener identidad UnADM con rigor argumentativo y trazabilidad.",
      "Garantizar transferencia lateral consistente entre asignaturas afines."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Secciones explicitas y ordenadas.",
      "Supuestos etiquetados como [Supuesto].",
      "Citas verificables y cierre juridico propio."
    ],
    "argumentative_patterns": [
      "Del problema al concepto.",
      "Del concepto a norma o doctrina.",
      "De la evidencia al analisis propio.",
      "Del analisis a la conclusion juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad academica",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica",
        "Etica",
        "Moral"
      ],
      "citations": [
        "malla-curricular-derecho-unadm.pdf",
        "huerta2000etica",
        "ronquillo2018etica",
        "prieto2009favor"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La identidad institucional exige citas verificables y trazabilidad."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura argumentada debe apoyarse en fuentes comprobables."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica",
          "kind": "develops",
          "justification": "La conclusion juridica deriva del razonamiento y no de descripcion."
        },
        {
          "source": "Etica",
          "target": "Moral",
          "kind": "contrasts",
          "justification": "Relacion transversal central en la asignatura destino. [Supuesto]"
        }
      ],
      "evidence": [
        "README de Etica y Moral juridica.",
        "programa-analitico-etica-y-moral-juridica.md.",
        "etica-y-moral-juridica.bib."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: se incorporan patrones laterales reutilizables del origen sin copiar contenido especifico.",
      "Ciclo 2: se preserva normalizacion estricta de salida estructurada.",
      "Ciclo 2: se refuerzan gates de calidad y trazabilidad bibliografica.",
      "Ciclo 2: se mantiene politica de supuestos explicitos ante vacios de consigna."
    ]
  }
}