{
  "summary": [
    "Se sincroniza memoria transversal hacia Derechos de autor con estrategia conservadora.",
    "Se preservan reglas utiles vigentes y se deduplican sin perdida.",
    "Se refuerza normalizacion estructurada obligatoria antes de toda propagacion.",
    "Se mantiene estado provisional para herencias no verificadas (Codex, GPT-Pro).",
    "Se consolidan ejes editoriales estables: problema, conceptos, evidencia, analisis propio y conclusion juridica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Citar malla-curricular-derecho-unadm.pdf para soporte de ubicacion curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener separacion entre reporte, presentacion y bibliografia de materia."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar solo resumen descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Agregar fuentes especificas por actividad al .bib local.",
    "No asumir fuentes de otras semanas sin confirmacion de consigna.",
    "Validar que cada entrega corresponda a la consigna concreta de la actividad."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Auditar README y programa analitico para corregir tokens de plantilla sin expandir.",
    "Corregir campos pendientes de plantilla antes de publicar."
  ],
  "latex_rules": [
    "Usar espanol con acentos correctos en .tex y .bib.",
    "Declarar metadatos antes de cargar template cuando la plantilla lo requiera.",
    "No dejar comandos incompletos en preambulo (ejemplo: usepackage sin argumento).",
    "Mantener paquetes en preambulo efectivo y compilar sin errores criticos.",
    "Conservar claves BibTeX estables para evitar referencias rotas.",
    "Normalizar nombres de archivo segun slug de asignatura y resolver tokens no expandidos."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo obras consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas pertinentes.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/editorial o URL.",
    "Incluir fecha de consulta para fuentes web.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "Mantener correspondencia 1:1 entre citas en texto y entradas .bib."
  ],
  "propagation_hints": [
    "Propagar lateral y recursivo solo tras validacion de JSON y estructura.",
    "Compartir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Evitar transferir redaccion literal o contenido tematico especifico de otra materia.",
    "Preservar reglas previas utiles sin regresion.",
    "Mantener bandera de revision manual para herencia historica no estructurada.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual."
  ],
  "open_questions": [
    "Confirmar si la clave LDE-S5B1 es nomenclatura oficial en toda la suite. [supuesto]",
    "Definir figura docente para reemplazar marcador pendiente en portada local.",
    "Validar si la ubicacion institucional en portada debe permanecer fija.",
    "Confirmar orden correcto de paquetes respecto a template en esta plantilla local.",
    "Confirmar limpieza definitiva de nombres corruptos en README (eporte/eferencias).",
    "Confirmar retiro o conservacion de herencia provisional tras validacion local."
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
        "Normalizacion estructurada antes de propagar.",
        "Herencia no verificada tratada como provisional."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 5, bloque 1, obligatoria, 8 creditos.",
        "Asignatura destino: Derechos de autor."
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y utiles.",
      "Asegurar coherencia entre identidad institucional, argumento juridico y evidencia.",
      "Permitir propagacion segura por reglas estables y verificables."
    ],
    "style_markers": [
      "Supuestos declarados explicitamente.",
      "Secciones funcionales y trazables.",
      "Consistencia entre portada, cuerpo y referencias.",
      "Cierre con implicacion practica juridica."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Marco conceptual y normativo.",
      "Analisis con postura propia.",
      "Conclusion aplicable a practica juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Integridad bibliografica",
        "Propagacion segura"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion segura",
          "kind": "supports",
          "justification": "Evita heredar salidas no parseables."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad bibliografica",
          "kind": "supports",
          "justification": "Toda afirmacion requiere respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La postura argumentada sostiene un cierre profesional util."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Propagacion segura",
          "kind": "depends_on",
          "justification": "La consistencia institucional reduce ruido entre nodos transversales."
        }
      ],
      "evidence": [
        "README local define ubicacion curricular y entrada canonica.",
        "Programa analitico fija ejes problema-conceptos-producto-analisis-cierre.",
        "Regla historica: bloquear salida no JSON parseable.",
        "Regla historica: tratar fuentes heredadas no verificadas como provisionales."
      ]
    },
    "reinforcement_log": [
      "Ciclo 16: deduplicacion lossless aplicada sin eliminar reglas utiles previas.",
      "Ciclo 16: reforzada prioridad de calidad_gates y normalizacion estructurada.",
      "Ciclo 16: transferidas solo abstracciones estables; sin copia literal de contenido de Filosofia del Derecho.",
      "Ciclo 16: mantenida trazabilidad de supuestos y fuentes provisionales."
    ]
  }
}