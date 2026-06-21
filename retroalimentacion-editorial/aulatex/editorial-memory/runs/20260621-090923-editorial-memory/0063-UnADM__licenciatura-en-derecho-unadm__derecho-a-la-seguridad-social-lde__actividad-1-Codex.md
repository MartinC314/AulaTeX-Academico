{
  "summary": [
    "Se consolida refuerzo lateral desde Filosofia del Derecho con transferencia solo de patrones reutilizables.",
    "Se preserva identidad UnADM y contexto curricular local verificado para Derecho a la Seguridad Social.",
    "Se mantiene normalizacion estricta: no propagar salidas no estructuradas ni JSON invalido.",
    "Se fija secuencia editorial persistente: problema, fundamento, analisis, evidencia, postura y cierre profesional.",
    "Se aplica compresion lossless por deduplicacion sin recortar reglas utiles."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho y a Derecho a la Seguridad Social.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Basar ubicacion curricular en semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar README y programa analitico locales como fuentes primarias de identidad.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato y alcance al producto pedido en la consigna semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Adaptar salida a reporte, presentacion u otro formato permitido por consigna."
  ],
  "activity_rules": [
    "Sustentar cada afirmacion con fuente verificable y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar solo resumen.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Verificar correspondencia exacta del producto con la consigna de Actividad 1.",
    "No asumir fuentes de otras semanas sin validacion local de pertinencia."
  ],
  "quality_gates": [
    "Bloquear propagacion si no hay JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Rechazar afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Normalizar respuestas no estructuradas antes de reutilizar.",
    "Verificar ajuste del producto a consigna local de Actividad 1."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Verificar nombres canonicos de archivo segun README local.",
    "Usar derecho-a-la-seguridad-social.bib como base canonica local.",
    "Corregir rutas o caracteres anomalos antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y normatividad vigente verificable.",
    "Registrar fuentes especificas de actividad en el .bib local.",
    "No inventar referencias; usar solo obras realmente consultables.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Usar cpeum2026, lss2026 y lissste2026 solo cuando la consigna lo requiera."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir lateralmente solo identidad, estructura, calidad, conceptos y patrones argumentativos reutilizables.",
    "No copiar redaccion literal, conclusiones ni bibliografia exclusiva entre nodos hermanos.",
    "Aplicar analogia controlada: primero reglas institucionales y calidad; luego estructura y conceptos.",
    "Preservar reglas utiles previas y sumar solo mejoras verificables sin regresion."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual completa de Actividad 1; confirmar entregable exacto.",
    "Confirmar si formato requerido es reporte, presentacion o mixto.",
    "Confirmar rubrica especifica de evaluacion para calibrar profundidad argumentativa.",
    "Confirmar fuentes obligatorias de la semana en planeacion local.",
    "Confirmar si se exige jurisprudencia especifica en esta actividad."
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
        "Asignatura: Derecho a la Seguridad Social.",
        "Semestre 2, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social bien delimitado.",
      "Fundamento constitucional y legal verificable.",
      "Analisis propio con evidencia trazable.",
      "Postura argumentada del estudiante.",
      "Cierre profesional transferible a la practica juridica."
    ],
    "reason_for_being": [
      "Transformar cada consigna en un producto juridico verificable.",
      "Evitar entregas descriptivas sin criterio propio.",
      "Garantizar trazabilidad entre consigna, fuentes, desarrollo y conclusion."
    ],
    "style_markers": [
      "Objetivo puntual al inicio.",
      "Secciones claras y trazables.",
      "Marcado explicito de supuestos.",
      "Citas verificables en cada afirmacion sustantiva.",
      "Conclusion juridica aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> fundamento normativo -> analisis -> evidencia -> conclusion.",
      "Regla general -> contraste con contexto -> postura -> implicacion practica.",
      "Pregunta guia -> criterios juridicos -> inferencia razonada."
    ],
    "knowledge_graph": {
      "concepts": [
        "Derecho a la seguridad social",
        "Marco constitucional en Mexico",
        "Ley del Seguro Social",
        "Ley del ISSSTE",
        "Universalidad",
        "Progresividad",
        "Igualdad y no discriminacion",
        "Acceso, cobertura y justiciabilidad",
        "Consigna de Actividad 1"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024",
        "cpeum2026",
        "lss2026",
        "lissste2026"
      ],
      "relations": [
        {
          "source": "Marco constitucional en Mexico",
          "target": "Derecho a la seguridad social",
          "kind": "supports",
          "justification": "El fundamento constitucional delimita alcance y exigibilidad del derecho."
        },
        {
          "source": "Ley del Seguro Social",
          "target": "Derecho a la seguridad social",
          "kind": "develops",
          "justification": "La LSS operacionaliza prestaciones y mecanismos del regimen correspondiente."
        },
        {
          "source": "Ley del ISSSTE",
          "target": "Derecho a la seguridad social",
          "kind": "develops",
          "justification": "La LISSSTE desarrolla cobertura para personas servidoras publicas."
        },
        {
          "source": "Universalidad",
          "target": "Acceso, cobertura y justiciabilidad",
          "kind": "supports",
          "justification": "Permite evaluar brechas de acceso y extension real del derecho."
        },
        {
          "source": "Progresividad",
          "target": "Acceso, cobertura y justiciabilidad",
          "kind": "supports",
          "justification": "Sirve para analizar avances, retrocesos y obligaciones estatales."
        },
        {
          "source": "Consigna de Actividad 1",
          "target": "Estructura del producto",
          "kind": "depends_on",
          "justification": "El tipo de entregable y profundidad argumentativa dependen de la consigna local."
        }
      ],
      "evidence": [
        "README local de la asignatura.",
        "Programa analitico local.",
        "derecho-a-la-seguridad-social.bib."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas manteniendo cobertura funcional completa.",
      "Se preservaron controles de calidad heredados y se alinearon al contexto local.",
      "Se reforzo transferencia lateral sin copiar contenido tematico exclusivo del nodo origen.",
      "Se mantuvo politica de supuestos explicitos ante falta de consigna completa."
    ]
  }
}