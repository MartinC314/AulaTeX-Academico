{
  "summary": [
    "Se consolida refuerzo lateral desde Filosofia del Derecho con transferencia solo de patrones reutilizables.",
    "Se preserva identidad UnADM y contexto curricular local verificado en README y programa analitico.",
    "Se mantiene secuencia editorial estable: problema, fundamento, analisis, evidencia, postura y cierre profesional.",
    "Se conserva bloqueo de propagacion para salidas no estructuradas o JSON invalido.",
    "Se aplica compresion lossless por deduplicacion sin recorte de reglas utiles previas."
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
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Sustentar cada afirmacion con fuente verificable y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Verificar correspondencia exacta con consigna de Actividad 1.",
    "No asumir fuentes de otras semanas sin validacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Rechazar afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Normalizar respuestas no estructuradas antes de reutilizar.",
    "Verificar ajuste del producto a consigna local de Actividad 1."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Verificar nombres canonicos de archivo segun README local.",
    "Usar derecho-a-la-seguridad-social.bib como base canonica local.",
    "Corregir rutas o caracteres anomalos antes de compilar.",
    "Resolver tokens sin expandir en nombres de archivo si aparecen."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y normatividad vigente verificable.",
    "Registrar fuentes especificas de actividad en el .bib local.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Usar cpeum2026, lss2026 y lissste2026 cuando la consigna lo requiera."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir lateralmente solo patrones reutilizables de identidad, estructura, calidad y argumentacion.",
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
        "Carpeta de asignatura como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Derecho a la Seguridad Social.",
        "Semestre 2, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Fundamento normativo verificable.",
      "Analisis propio con postura.",
      "Evidencia trazable.",
      "Cierre profesional transferible."
    ],
    "reason_for_being": [
      "Transformar cada consigna en un producto juridico verificable y util para practica profesional."
    ],
    "style_markers": [
      "Objetivo puntual al inicio.",
      "Secciones claras y trazables.",
      "Supuestos marcados de forma explicita.",
      "Cierre no descriptivo con implicacion juridica."
    ],
    "argumentative_patterns": [
      "Problema -> fundamento normativo -> analisis -> evidencia -> conclusion.",
      "Regla general -> contraste con contexto -> postura -> implicacion practica.",
      "Pregunta guia -> criterio juridico -> inferencia razonada."
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
        "Acceso, cobertura y justiciabilidad"
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
          "justification": "Define base juridica primaria del derecho en el curso local."
        },
        {
          "source": "Ley del Seguro Social",
          "target": "Derecho a la seguridad social",
          "kind": "develops",
          "justification": "Concreta prestaciones y operacion institucional del regimen."
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
          "justification": "Sirve para evaluar alcance real y barreras de acceso."
        },
        {
          "source": "Progresividad",
          "target": "Acceso, cobertura y justiciabilidad",
          "kind": "supports",
          "justification": "Permite valorar avances y retrocesos en garantia del derecho."
        }
      ],
      "evidence": [
        "README local de la asignatura.",
        "Programa analitico local.",
        "derecho-a-la-seguridad-social.bib."
      ]
    },
    "reinforcement_log": [
      "Ciclo 19: deduplicacion completa de reglas repetidas.",
      "Ciclo 19: se preservan reglas utiles previas sin eliminacion regresiva.",
      "Ciclo 19: se agrega regla transversal de resolver tokens sin expandir si aparecen.",
      "Ciclo 19: se mantiene transferencia lateral sin copiar contenido tematico exclusivo del nodo hermano."
    ]
  }
}