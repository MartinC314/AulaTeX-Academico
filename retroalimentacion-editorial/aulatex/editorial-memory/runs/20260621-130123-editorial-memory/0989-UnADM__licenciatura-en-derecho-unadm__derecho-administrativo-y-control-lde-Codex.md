{
  "summary": [
    "Se consolida sincronizacion transversal conservadora desde actividad de Filosofia del Derecho hacia materia de Derecho administrativo y control.",
    "Se preservan reglas institucionales validas y se deduplican sin perdida.",
    "Se refuerzan ejes estables: problema, conceptos, evidencia, analisis propio y conclusion juridica transferible.",
    "Se mantiene bloqueo de propagacion ante salidas no JSON parseables.",
    "Se evita transferir doctrina o citas sustantivas de otra materia sin verificacion local."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en tono, metadatos y formato.",
    "Usar nombre exacto de materia: Derecho administrativo y control.",
    "Conservar enfoque de Licenciatura en Derecho en todos los entregables.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como [supuesto] todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener consistencia entre README, .tex y .bib.",
    "Corregir placeholders y rutas corruptas en README y programa analitico."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar resumen solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Explicitar el tipo de producto antes de desarrollar: reporte, presentacion o visual.",
    "Vincular el analisis con control administrativo y practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar y normalizar cualquier respuesta no estructurada antes de reutilizar.",
    "Verificar que reglas heredadas no contradigan el programa analitico local."
  ],
  "latex_rules": [
    "Mantener espanol y codificacion correcta en .tex y .bib.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Mantener claves BibTeX estables.",
    "Reemplazar Actividad X por numero y nombre reales antes de entrega.",
    "Completar figura docente antes de entrega.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) por slug literal en README y programa. [supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de cada actividad en derecho-administrativo-y-control.bib.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio, medio y nota/URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Compartir a nodos laterales solo abstracciones editoriales estables.",
    "No propagar contenido doctrinal especifico de Filosofia del Derecho.",
    "Mantener compresion lossless por union-dedupe sin regresion.",
    "Aplicar normalizacion manual cuando la fuente heredada sea provisional."
  ],
  "open_questions": [
    "Confirmar formato institucional de citas para la Licenciatura en Derecho.",
    "Confirmar nombre oficial de la figura docente en plantilla.",
    "Confirmar si el anio de consulta 2026 del sitio UnADM se mantiene. [supuesto]",
    "Confirmar convencion final de carpeta de referencias local (referencias-...). [supuesto]",
    "Confirmar que todos los tokens $(@{...}.Slug) son artefactos a corregir. [supuesto]"
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador ante fuentes no verificadas."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada antes de propagacion.",
        "No invencion de fuentes."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 6, bloque 1, obligatoria, 8 creditos.",
        "Asignatura: Derecho administrativo y control.",
        "Fuente curricular local: malla-curricular-derecho-unadm.pdf."
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
      "Convertir la planeacion semanal en productos academicos claros, fundados y aplicables.",
      "Sostener coherencia institucional entre contenido, formato y evidencia."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales y trazables.",
      "Postura propia obligatoria.",
      "Cierre practico profesional.",
      "Marcado explicito de [supuesto]."
    ],
    "argumentative_patterns": [
      "Problema -> objetivo -> marco conceptual/normativo -> analisis propio -> conclusion aplicada.",
      "Afirmacion -> evidencia verificable -> inferencia juridica -> criterio transferible."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad academica",
        "Normalizacion estructurada",
        "Problema juridico",
        "Marco normativo/doctrinal",
        "Analisis propio",
        "Conclusion transferible",
        "Control administrativo"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La identidad institucional exige trazabilidad y rigor."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere delimitacion previa del problema."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion aplicada exige fundamento verificable."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La estructura valida evita errores de propagacion y perdida de trazabilidad."
        },
        {
          "source": "Control administrativo",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La materia orienta aplicacion profesional en administracion y control."
        }
      ],
      "evidence": [
        "README local de la materia.",
        "Programa analitico local.",
        "Archivo derecho-administrativo-y-control.bib.",
        "Regla institucional historica: bloquear no-JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 6: deduplicacion completa de reglas repetidas sin recorte semantico.",
      "Ciclo 6: refuerzo de gates de calidad y normalizacion previa a propagacion.",
      "Ciclo 6: transferencia transversal limitada a abstracciones estables.",
      "Ciclo 6: se preserva ADN argumentativo comun y se evita arrastre doctrinal no verificado."
    ]
  }
}