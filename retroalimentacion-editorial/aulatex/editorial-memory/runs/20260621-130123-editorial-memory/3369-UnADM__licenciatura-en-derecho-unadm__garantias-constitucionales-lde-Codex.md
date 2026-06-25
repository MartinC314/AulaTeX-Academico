{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia conservadora y union-dedupe sin regresion.",
    "Se preservan reglas estables de identidad, estructura reusable, calidad, LaTeX y bibliografia.",
    "Se evita transferencia de contenido disciplinar de Filosofia del Derecho hacia Garantias constitucionales.",
    "Se refuerza normalizacion obligatoria cuando existan salidas no parseables.",
    "Se mantiene cerebro editorial de materia con enfoque en trazabilidad y control institucional."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en tono, portada y metadatos.",
    "Usar contexto curricular local verificado: Licenciatura en Derecho, semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como [Supuesto] todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No trasladar contenido disciplinar entre materias sin validacion expresa."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto solicitado por la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion, programa analitico y bibliografia.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante y evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Vincular afirmaciones constitucionales con fundamento normativo o bibliografico.",
    "Confirmar que el producto entregado coincide con la consigna de la actividad."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de [Supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar compresion lossless por union-dedupe sin eliminar reglas utiles previas."
  ],
  "latex_rules": [
    "Compilar sin errores criticos y sin referencias rotas.",
    "Conservar clase y opciones base de la plantilla local salvo requerimiento verificado.",
    "Completar campos de portada: actividad, figura docente y fecha.",
    "Corregir truncamientos y placeholders en README, programa analitico y .tex antes de compilar.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "No introducir comandos o paquetes no estandar sin justificacion editorial o tecnica."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y normas juridicas verificables.",
    "Registrar fuentes especificas por actividad en garantias-constitucionales.bib.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Agregar identificador, emisor y fecha al citar normas juridicas."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Compartir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar propagar redaccion literal o contenido tematico de otra materia.",
    "Mantener alerta institucional de normalizacion manual para ciclos con herencia no estructurada.",
    "Preservar trazabilidad de cambios en cada ciclo de consolidacion."
  ],
  "open_questions": [
    "Confirmar consigna local de la primera actividad de Garantias constitucionales.",
    "Confirmar nombre de figura docente en plantilla .tex.",
    "Confirmar estilo de citacion requerido (APA, juridico mexicano u otro).",
    "Resolver y verificar truncamiento actual en reporte-garantias-constitucionales.tex.",
    "Resolver placeholders $(@{...}.Slug) en README y programa analitico.",
    "Confirmar si la fecha debe mantenerse automatica (\\today) o fija por entrega."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador ante datos no verificados."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada antes de propagar.",
        "Marcado explicito de [Supuesto].",
        "Separacion entre memoria local y herencia transversal."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura destino: Garantias constitucionales.",
        "Semestre 2, bloque 1, obligatoria, 8 creditos.",
        "Coursecode local: LDE-S2B1."
      ]
    },
    "essence": [
      "Problema juridico o social claro.",
      "Marco conceptual y normativo verificable.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible.",
      "Control de calidad estructural y bibliografico."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y verificables.",
      "Asegurar consistencia entre consigna, fuentes, argumento y entrega.",
      "Sostener un cerebro editorial persistente sin regresiones."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Separar norma, doctrina, hecho y opinion.",
      "Evitar afirmaciones absolutas sin evidencia.",
      "Cerrar con implicacion practica profesional.",
      "Etiquetar incertidumbre como [Supuesto]."
    ],
    "argumentative_patterns": [
      "Problema -> objetivo -> marco normativo/doctrinal -> analisis propio -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> implicacion juridica.",
      "Consigna local como ancla de alcance."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Problema juridico o social",
        "Marco normativo o doctrinal",
        "Analisis propio",
        "Conclusion transferible",
        "Consistencia cita-texto-bib",
        "Propagacion transversal conservadora"
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
          "justification": "La identidad institucional exige trazabilidad, citas verificables y consistencia formal."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere una pregunta juridica delimitada."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion profesional necesita sustento verificable."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion transversal conservadora",
          "kind": "depends_on",
          "justification": "Sin JSON parseable no hay transferencia confiable."
        },
        {
          "source": "Consistencia cita-texto-bib",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita afirmaciones sin respaldo y referencias huerfanas."
        }
      ],
      "evidence": [
        "README local con ubicacion curricular y pauta editorial.",
        "Programa analitico local con ejes de trabajo comunes.",
        "garantias-constitucionales.bib con base institucional activa.",
        "Regla persistente institucional: revisar y normalizar salidas no estructuradas."
      ]
    },
    "reinforcement_log": [
      "Ciclo 7: deduplicacion semantica aplicada sin eliminar reglas utiles previas.",
      "Ciclo 7: se reforzo bloqueo por JSON no parseable como gate institucional.",
      "Ciclo 7: se reforzo separacion entre herencia editorial y contenido disciplinar.",
      "Ciclo 7: se mantuvo enfoque transversal en identidad, estructura reusable y calidad."
    ]
  }
}