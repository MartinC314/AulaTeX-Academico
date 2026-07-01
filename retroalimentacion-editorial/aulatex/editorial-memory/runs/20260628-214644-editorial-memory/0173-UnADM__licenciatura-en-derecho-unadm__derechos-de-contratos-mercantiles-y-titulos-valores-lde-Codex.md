{
  "summary": [
    "Se consolida sincronizacion transversal conservadora para materia destino con identidad UnADM.",
    "Se preservan ejes estables transferibles: problema, conceptos o normas, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene regla critica: no propagar salidas no estructuradas sin normalizacion previa.",
    "Se prioriza consistencia entre README, programa analitico, .tex y .bib locales.",
    "Supuesto: faltan consignas y rubricas por actividad; se mantiene cerebro editorial minimo reusable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear todo entregable a Licenciatura en Derecho y a la materia destino.",
    "Conservar tono juridico-formal con criterio academico propio.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Usar la carpeta de materia como punto de entrada canonico."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Mantener coherencia entre README, programa analitico, .tex y .bib."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir evidencia citada de interpretacion propia.",
    "Evitar entregas meramente descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir fuentes de otras semanas sin validacion de consigna.",
    "Comprobar que cada entrega corresponda al producto solicitado."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar trazabilidad entre afirmaciones, citas en texto y archivo .bib.",
    "Verificar que no se inventen fuentes ni metadatos.",
    "Evitar regresion de reglas utiles heredadas."
  ],
  "latex_rules": [
    "Mantener codificacion correcta de espanol en .tex y .bib.",
    "Conservar claves BibTeX estables para evitar referencias rotas.",
    "Corregir macros truncadas o incompletas antes de compilar.",
    "Resolver placeholders de slug en README y programa analitico.",
    "Validar nombres reales de archivo antes de referenciarlos.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Usar como base el .bib local confirmado de la materia destino.",
    "Priorizar fuentes institucionales UnADM y normas juridicas verificables.",
    "Registrar fuentes especificas por actividad en el .bib local.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente o URL.",
    "Agregar fecha de consulta en recursos web cuando aplique."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables en saltos transversales.",
    "No transferir redaccion literal ni detalles hiperlocales de una actividad.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Aplicar compresion lossless por union y deduplicacion en cada ciclo.",
    "Mantener alerta institucional por historico de salidas no parseables hasta nueva evidencia."
  ],
  "open_questions": [
    "Confirmar consignas y rubricas reales de actividades de la materia destino.",
    "Confirmar correccion final de nombres truncados en README.",
    "Confirmar resolucion de placeholders de slug en README y programa.",
    "Confirmar cierre de macro truncada en plantilla .tex.",
    "Supuesto: la alerta historica de salida no JSON parseable sigue vigente."
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
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 6, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Derechos de contratos mercantiles y titulos valores."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas o doctrina pertinente.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos solidos.",
      "Sostener trazabilidad entre argumento juridico y evidencia.",
      "Garantizar consistencia editorial de toda la carpeta de materia."
    ],
    "style_markers": [
      "Supuestos etiquetados de forma explicita.",
      "Secciones claras con progresion argumentativa estable.",
      "Cierre con postura juridica propia y aplicable."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer marco conceptual y normativo.",
      "Contrastar evidencia.",
      "Emitir analisis propio.",
      "Concluir con aplicabilidad profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "identidad institucional UnADM",
        "integridad academica",
        "trazabilidad de fuentes",
        "problema juridico",
        "analisis propio",
        "conclusion juridica transferible",
        "normalizacion estructurada",
        "consistencia README-programa-tex-bib"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "identidad institucional UnADM",
          "target": "integridad academica",
          "kind": "supports",
          "justification": "La identidad institucional exige evidencia verificable y forma academica."
        },
        {
          "source": "problema juridico",
          "target": "analisis propio",
          "kind": "develops",
          "justification": "El analisis surge de una delimitacion clara del problema."
        },
        {
          "source": "trazabilidad de fuentes",
          "target": "conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion gana validez cuando deriva de evidencia citada."
        },
        {
          "source": "normalizacion estructurada",
          "target": "consistencia README-programa-tex-bib",
          "kind": "depends_on",
          "justification": "La reutilizacion segura depende de estructura valida y coherente."
        }
      ],
      "evidence": [
        "README de materia con pauta editorial y ubicacion curricular.",
        "Programa analitico con ejes de trabajo transferibles.",
        ".bib local con entradas institucionales confirmadas.",
        "Historial institucional de salidas no parseables que exige control de calidad."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: deduplicacion completa de reglas repetidas.",
      "Ciclo 2: transferencia transversal solo de abstracciones estables.",
      "Ciclo 2: se preservan reglas utiles previas sin recorte funcional.",
      "Ciclo 2: se refuerza gate de JSON parseable y normalizacion obligatoria.",
      "Ciclo 2: se mantiene abierto contexto faltante por actividad con supuestos marcados."
    ]
  }
}