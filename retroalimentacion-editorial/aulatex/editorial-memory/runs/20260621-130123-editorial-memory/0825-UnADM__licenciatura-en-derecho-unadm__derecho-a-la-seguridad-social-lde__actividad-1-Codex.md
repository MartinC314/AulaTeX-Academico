{
  "summary": [
    "Se consolida refuerzo lateral con transferencia solo de patrones reutilizables.",
    "Se preserva identidad UnADM y contexto local de Derecho a la Seguridad Social.",
    "Se mantiene normalizacion obligatoria: no propagar salidas no estructuradas ni JSON invalido.",
    "Se fija secuencia editorial estable: problema, fundamento, analisis, evidencia, postura y cierre profesional.",
    "Se aplica compresion lossless por union y deduplicacion sin recorte de reglas utiles."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho y a Derecho a la Seguridad Social.",
    "Basar ubicacion curricular en semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Usar README y programa analitico locales como fuentes primarias de identidad.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto pedido en la consigna semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Permitir reporte o presentacion segun instruccion local."
  ],
  "activity_rules": [
    "Sustentar cada afirmacion con fuente verificable y cita explicita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Verificar correspondencia exacta con consigna de Actividad 1.",
    "No asumir fuentes de otras semanas sin validacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si no hay JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Rechazar afirmaciones sin respaldo o sin marca de supuesto.",
    "Normalizar respuestas no estructuradas antes de reutilizar.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar ajuste del producto a consigna local de Actividad 1."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Verificar nombres canonicos de archivo segun README local.",
    "Usar derecho-a-la-seguridad-social.bib como base canonica local.",
    "Corregir rutas o caracteres anomalos antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y normatividad vigente verificable.",
    "Registrar fuentes especificas de actividad en el .bib local.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Usar cpeum2026, lss2026 y lissste2026 solo cuando la consigna lo requiera."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir lateralmente solo identidad, estructura, calidad y patrones argumentativos.",
    "No copiar redaccion literal, conclusiones ni bibliografia exclusiva entre nodos hermanos.",
    "Aplicar analogia controlada: primero reglas institucionales y calidad, luego estructura y conceptos.",
    "Preservar reglas utiles previas y sumar solo mejoras verificables."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual completa de Actividad 1; confirmar entregable exacto.",
    "Confirmar si el formato requerido es reporte, presentacion o mixto.",
    "Confirmar rubrica especifica de evaluacion para calibrar profundidad.",
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
        "Control editorial desde la carpeta de asignatura."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Derecho a la Seguridad Social.",
        "Semestre 2, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social bien delimitado.",
      "Fundamento normativo verificable.",
      "Analisis propio con postura academica.",
      "Evidencia y citas trazables.",
      "Cierre profesional transferible."
    ],
    "reason_for_being": [
      "Transformar cada consigna en un producto juridico verificable.",
      "Asegurar consistencia metodologica entre identidad, estructura, evidencia y conclusion."
    ],
    "style_markers": [
      "Objetivo puntual al inicio.",
      "Secciones claras y trazables.",
      "Marcado explicito de supuestos.",
      "Cierre no meramente descriptivo."
    ],
    "argumentative_patterns": [
      "Problema -> fundamento normativo -> analisis -> evidencia -> conclusion.",
      "Regla general -> contraste contextual -> postura -> implicacion practica.",
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
          "justification": "Define base juridica del derecho y su exigibilidad."
        },
        {
          "source": "Ley del Seguro Social",
          "target": "Derecho a la seguridad social",
          "kind": "develops",
          "justification": "Operacionaliza prestaciones y mecanismos del regimen general."
        },
        {
          "source": "Ley del ISSSTE",
          "target": "Derecho a la seguridad social",
          "kind": "develops",
          "justification": "Regula cobertura para personas servidoras publicas."
        },
        {
          "source": "Universalidad",
          "target": "Acceso, cobertura y justiciabilidad",
          "kind": "supports",
          "justification": "Sirve para evaluar inclusion real y barreras de acceso."
        },
        {
          "source": "Progresividad",
          "target": "Acceso, cobertura y justiciabilidad",
          "kind": "supports",
          "justification": "Permite medir avances y retrocesos en proteccion social."
        },
        {
          "source": "Consigna de Actividad 1",
          "target": "Formato de entrega",
          "kind": "depends_on",
          "justification": "El producto final debe ajustarse a instruccion local verificada."
        }
      ],
      "evidence": [
        "README local define estructura canonica y control editorial.",
        "Programa analitico local define proposito y ejes de trabajo.",
        "derecho-a-la-seguridad-social.bib concentra bibliografia base verificable."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin perdida semantica.",
      "Se mantuvieron reglas de calidad y bloqueo JSON como puerta obligatoria.",
      "Se reforzaron patrones argumentativos transferibles desde nodo lateral.",
      "Se excluyo contenido tematico exclusivo de Filosofia del Derecho.",
      "Se conservaron supuestos abiertos donde falta consigna local."
    ]
  }
}