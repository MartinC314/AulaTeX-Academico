{
  "summary": [
    "Se consolida refuerzo lateral con transferencia solo de patrones reutilizables.",
    "Se mantiene identidad UnADM y contexto local verificado de Derecho a la Seguridad Social.",
    "Se preserva secuencia editorial estable: problema, fundamento, analisis, evidencia, postura y cierre.",
    "Se conserva bloqueo de propagacion para JSON invalido o salida no estructurada.",
    "Se aplica compresion lossless por union y deduplicacion sin recorte de reglas utiles."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y trazabilidad.",
    "Vincular Actividad 1 a Licenciatura en Derecho y a Derecho a la Seguridad Social.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Basar ubicacion curricular en semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar README y programa analitico locales como fuentes primarias.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto pedido en la consigna semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Permitir reporte o presentacion segun instruccion local."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuente verificable y cita explicita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Confirmar correspondencia exacta con la consigna de Actividad 1.",
    "No asumir fuentes de otras semanas sin validacion local."
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
    "Usar cpeum2026, lss2026 y lissste2026 cuando la consigna lo requiera."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir lateralmente solo identidad, estructura, calidad y patrones argumentativos.",
    "No copiar redaccion literal, conclusiones ni bibliografia exclusiva entre hermanos.",
    "Aplicar analogia controlada: primero reglas institucionales y calidad, luego estructura y conceptos.",
    "Preservar reglas utiles previas y sumar solo mejoras verificables."
  ],
  "open_questions": [
    "[Supuesto] Falta consigna textual completa de Actividad 1; confirmar entregable exacto.",
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
      "Problema juridico o social como detonador.",
      "Fundamento constitucional y legal verificable.",
      "Analisis propio con postura academica.",
      "Evidencia trazable y cierre profesional transferible."
    ],
    "reason_for_being": [
      "Convertir cada consigna en producto juridico verificable.",
      "Asegurar coherencia entre objetivo, desarrollo y conclusion.",
      "Sostener estandar institucional reproducible en nodos laterales."
    ],
    "style_markers": [
      "Objetivo puntual al inicio.",
      "Secciones claras y trazables.",
      "Supuestos marcados de forma explicita.",
      "Cierre no descriptivo, con implicacion juridica."
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
        "Jurisprudencia y criterios relevantes"
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
          "justification": "Define fundamento juridico primario del derecho."
        },
        {
          "source": "Ley del Seguro Social",
          "target": "Derecho a la seguridad social",
          "kind": "develops",
          "justification": "Desarrolla mecanismos de cobertura y prestaciones."
        },
        {
          "source": "Ley del ISSSTE",
          "target": "Derecho a la seguridad social",
          "kind": "develops",
          "justification": "Regula proteccion para trabajadores del Estado."
        },
        {
          "source": "Universalidad",
          "target": "Acceso, cobertura y justiciabilidad",
          "kind": "supports",
          "justification": "Permite evaluar alcance real del derecho."
        },
        {
          "source": "Progresividad",
          "target": "Acceso, cobertura y justiciabilidad",
          "kind": "supports",
          "justification": "Permite medir avances y evitar retrocesos."
        }
      ],
      "evidence": [
        "README local: estructura canonica y control editorial.",
        "Programa analitico local: proposito y ejes oficiales.",
        "derecho-a-la-seguridad-social.bib: base bibliografica verificable.",
        "Regla vigente: bloquear salidas no estructuradas o JSON invalido."
      ]
    },
    "reinforcement_log": [
      "Ciclo 89: deduplicacion completa de reglas repetidas.",
      "Ciclo 89: se mantiene transferencia lateral sin arrastre tematico exclusivo del origen.",
      "Ciclo 89: se refuerzan compuertas de calidad y trazabilidad bibliografica.",
      "Ciclo 89: se conservan supuestos abiertos donde falta consigna local."
    ]
  }
}