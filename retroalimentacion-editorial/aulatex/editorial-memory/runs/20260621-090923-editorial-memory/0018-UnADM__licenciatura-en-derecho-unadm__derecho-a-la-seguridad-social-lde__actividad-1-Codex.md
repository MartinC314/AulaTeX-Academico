{
  "summary": [
    "Se consolida refuerzo lateral desde Filosofia del Derecho con transferencia de patrones reutilizables.",
    "Se preserva identidad UnADM y contexto local de Derecho a la Seguridad Social.",
    "Se mantiene compresion lossless por deduplicacion y union sin recorte util.",
    "Se fija secuencia editorial estable: problema, fundamento, analisis, evidencia, postura y cierre.",
    "Se mantiene bloqueo de propagacion para salidas no estructuradas o JSON invalido.",
    "Se evita copiar contenido tematico exclusivo, conclusiones o bibliografia de nodo hermano."
  ],
  "identity_rules": [
    "Mantener tono institucional UnADM, formal y juridico.",
    "Vincular la actividad a Licenciatura en Derecho y Derecho a la Seguridad Social.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Basar ubicacion curricular en semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar README y programa analitico locales como fuentes primarias.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato al producto pedido en la consigna semanal.",
    "Permitir reporte o presentacion segun instruccion local.",
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
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Usar cpeum2026, lss2026 y lissste2026 cuando la consigna lo requiera."
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
    "Confirmar rubrica especifica para calibrar profundidad argumentativa.",
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
      "Transformar consignas en productos juridicos verificables.",
      "Asegurar calidad editorial estable entre actividades.",
      "Preservar identidad institucional y trazabilidad de fuentes."
    ],
    "style_markers": [
      "Objetivo puntual al inicio.",
      "Secciones claras y trazables.",
      "Postura personal sustentada.",
      "Marcado explicito de supuestos.",
      "Cierre no meramente descriptivo."
    ],
    "argumentative_patterns": [
      "Problema -> fundamento -> analisis -> evidencia -> conclusion.",
      "Regla general -> contraste contextual -> postura -> implicacion practica.",
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
          "justification": "Define base juridica del derecho en la asignatura."
        },
        {
          "source": "Ley del Seguro Social",
          "target": "Derecho a la seguridad social",
          "kind": "develops",
          "justification": "Concreta prestaciones y reglas del regimen aplicable."
        },
        {
          "source": "Ley del ISSSTE",
          "target": "Derecho a la seguridad social",
          "kind": "develops",
          "justification": "Regula cobertura para personas trabajadoras del Estado."
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
          "justification": "Permite valorar avances y retrocesos en proteccion social."
        }
      ],
      "evidence": [
        "README local de la asignatura.",
        "Programa analitico local.",
        "derecho-a-la-seguridad-social.bib."
      ]
    },
    "reinforcement_log": [
      "Ciclo 18: deduplicacion completa de reglas repetidas.",
      "Ciclo 18: preservadas reglas utiles previas sin eliminacion regresiva.",
      "Ciclo 18: reforzada transferencia lateral por patrones y no por contenido tematico.",
      "Ciclo 18: normalizado grafo a relaciones permitidas y justificaciones breves."
    ]
  }
}