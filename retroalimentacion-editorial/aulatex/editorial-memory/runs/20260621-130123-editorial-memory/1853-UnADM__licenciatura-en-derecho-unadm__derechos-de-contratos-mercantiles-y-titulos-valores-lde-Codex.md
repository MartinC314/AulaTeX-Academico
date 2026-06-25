{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre actividad de origen y materia destino.",
    "Se preservan reglas estables de identidad UnADM, estructura argumentativa y control de calidad.",
    "Se mantiene propagacion por union-dedupe lossless sin traslado de contenido tematico especifico de Filosofia del Derecho.",
    "Se refuerza prioridad de normalizacion: solo memoria JSON parseable y estructurada.",
    "Se confirma contexto local del destino: semestre 6, bloque 2, obligatoria, 8 creditos, con .bib local existente.",
    "Se detectan placeholders y nombres truncados en README/programa como deuda tecnica local a corregir."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables a Licenciatura en Derecho y a la materia destino.",
    "Conservar tono juridico-formal, claridad tecnica y cierre con postura propia.",
    "Usar carpeta de materia como entrada canonica documental.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto pedido por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Mantener consistencia entre README, programa, .tex y .bib."
  ],
  "activity_rules": [
    "Contextualizar cada actividad con problema concreto y delimitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir evidencia citada de interpretacion propia.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir fuentes de otras semanas o materias sin validacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Comprobar trazabilidad entre afirmaciones y fuentes.",
    "Verificar no inventar fuentes ni citas.",
    "Revisar regresion: no eliminar reglas utiles previamente vigentes."
  ],
  "latex_rules": [
    "Usar español con acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Corregir macros truncadas antes de compilar.",
    "Resolver placeholders de slug en nombres de archivo de README y programa."
  ],
  "bibliography_rules": [
    "Usar como base el .bib local de la materia destino.",
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Registrar fuentes especificas por actividad en el .bib local.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente/URL.",
    "Agregar fecha de consulta en recursos web."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo abstracciones editoriales estables.",
    "No propagar redaccion literal ni contenido tematico de otra asignatura.",
    "Mantener estrategia progresiva y conservadora por ciclos.",
    "Aplicar union-dedupe lossless en cada fusion.",
    "Etiquetar incidencias historicas de parseo como alerta activa hasta cierre verificado.",
    "Si falta contexto local, crear cerebro minimo y abrir preguntas."
  ],
  "open_questions": [
    "Confirmar correccion de macro truncada en plantilla .tex del destino.",
    "Confirmar sustitucion final de placeholders de slug en README y programa.",
    "Confirmar si incidencia de salida no JSON parseable sigue activa en flujo actual.",
    "Confirmar plantilla oficial de presentacion si difiere del reporte.",
    "Supuesto: el .bib canonico del destino es derechos-de-contratos-mercantiles-y-titulos-valores.bib; validar en pipeline."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Juridicamente preciso.",
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
        "Materia: Derechos de contratos mercantiles y titulos valores."
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Marco conceptual y normativo pertinente.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos consistentes y verificables.",
      "Sostener calidad editorial institucional en reportes y presentaciones.",
      "Garantizar trazabilidad entre argumento, evidencia y cierre profesional."
    ],
    "style_markers": [
      "Apertura breve con problema.",
      "Secciones explicitas y ordenadas.",
      "Supuestos marcados cuando falte evidencia.",
      "Cierre con implicacion profesional."
    ],
    "argumentative_patterns": [
      "Problema -> marco normativo/doctrinal -> evidencia -> analisis propio -> conclusion.",
      "Afirmacion juridica siempre respaldada por fuente verificable.",
      "Contrastar evidencia antes de fijar postura."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico",
        "Marco normativo o doctrinal",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion estructurada",
        "JSON parseable"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La identidad institucional exige trazabilidad y citas verificables."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin delimitacion del problema no hay argumentacion pertinente."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La transferencia profesional requiere base juridica explicita."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "JSON parseable",
          "kind": "depends_on",
          "justification": "La propagacion recursiva segura requiere estructura valida."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El analisis gana validez cuando contrasta fuentes comprobables."
        }
      ],
      "evidence": [
        "README de materia: ubicacion curricular y pauta editorial canonica.",
        "Programa analitico: proposito y ejes de trabajo.",
        ".bib local existente con entradas institucionales verificables.",
        "Regla vigente: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: deduplicadas reglas repetidas sin perdida semantica.",
      "Ciclo 2: reforzada separacion entre abstracciones transferibles y contenido tematico local.",
      "Ciclo 2: mantenida alerta historica de normalizacion por salidas no estructuradas.",
      "Ciclo 2: añadida deuda tecnica local verificable sobre placeholders y macro truncada."
    ]
  }
}