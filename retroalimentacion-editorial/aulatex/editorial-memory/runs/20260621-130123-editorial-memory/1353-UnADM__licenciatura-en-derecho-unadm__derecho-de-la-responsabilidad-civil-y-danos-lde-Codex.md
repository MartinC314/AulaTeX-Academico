{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia conservadora y sin regresion.",
    "Se preservan reglas institucionales UnADM y normalizacion JSON obligatoria.",
    "Se transfieren solo abstracciones estables: identidad, estructura reusable, calidad y grafo conceptual.",
    "Se evita traslado tematico literal desde Filosofia del Derecho hacia Responsabilidad Civil y Danos.",
    "Se mantiene compresion lossless por union y deduplicacion.",
    "Se refuerzan incidencias locales verificadas: salida no estructurada previa, placeholders y truncamientos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar contexto curricular local confirmado: Licenciatura en Derecho, semestre 6, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no confirmado por consigna o fuente oficial.",
    "Tratar memorias heredadas no verificadas como provisionales hasta confirmacion local.",
    "No declarar oficial el codigo LDE-S6B1 sin evidencia documental."
  ],
  "structure_rules": [
    "Iniciar cada entrega con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto a la planeacion semanal y a la consigna vigente.",
    "Mantener separacion editorial entre reporte, presentacion, programa analitico y .bib.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Formular problema juridico pertinente a responsabilidad civil y dano.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Separar fundamento juridico, evidencia y analisis propio.",
    "No arrastrar contenido tematico de origen si no aplica al nodo destino.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de propagar.",
    "Confirmar que toda afirmacion juridica tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar control de no regresion sobre reglas utiles previas."
  ],
  "latex_rules": [
    "Usar espanol con acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir rutas truncadas y caracteres anomalos antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: la plantilla .tex local esta truncada en authortable y debe completarse."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Registrar fuentes especificas por actividad en el .bib local de la materia.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Registrar vacios de referencia como preguntas abiertas."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas estables y no literales.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar propagar detalles exclusivos de una actividad no equivalente.",
    "Mantener alerta de normalizacion manual por antecedentes de salida no estructurada.",
    "Propagar control de placeholders y rutas truncadas como regla tecnica general.",
    "Conservar compresion por union-dedupe sin recorte semantico."
  ],
  "open_questions": [
    "Confirmar guia oficial de formato para actividades de la materia.",
    "Confirmar convencion final de nombres danos versus daños en todo el arbol.",
    "Confirmar si LDE-S6B1 es codigo oficial o solo interno. [supuesto]",
    "Completar y validar la seccion authortable truncada en la plantilla .tex.",
    "Resolver placeholders de .bib en README y programa analitico.",
    "Confirmar rubrica de evaluacion para calibrar profundidad argumentativa."
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
        "Normalizacion estructurada previa a propagacion.",
        "Entrada canonica por carpeta de materia."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 6, bloque 1, obligatoria, 8 creditos.",
        "Asignatura: Derecho de la responsabilidad civil y danos.",
        "Fuente curricular: malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Problema juridico.",
      "Conceptos y fuentes pertinentes.",
      "Analisis propio.",
      "Conclusion juridica transferible.",
      "Identidad institucional verificable."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico y utilidad profesional.",
      "Estandarizar calidad editorial sin perder adaptacion local por actividad."
    ],
    "style_markers": [
      "Supuestos explicitos cuando falte evidencia.",
      "Estructura por secciones funcionales.",
      "Cierre con criterio juridico propio.",
      "Sin literalidad tematica en transferencias transversales."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Marco conceptual y normativo con fuentes.",
      "Analisis propio con contraste.",
      "Conclusion aplicada a practica juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion JSON",
        "Problema juridico",
        "Marco normativo/doctrinal",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Responsabilidad civil",
        "Dano",
        "Integridad academica"
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
          "justification": "La identidad exige trazabilidad de fuentes y forma consistente."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita propagar contenido ambiguo o no verificable."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere pregunta juridica definida."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida depende de fundamento verificable."
        },
        {
          "source": "Responsabilidad civil",
          "target": "Dano",
          "kind": "depends_on",
          "justification": "El eje material del curso se articula sobre la nocion de dano."
        }
      ],
      "evidence": [
        "README local de la materia.",
        "Programa analitico local.",
        "Archivo .bib local con entradas institucionales.",
        "Plantilla .tex local con truncamiento detectado. [supuesto tecnico verificado por contexto]"
      ]
    },
    "reinforcement_log": [
      "Ciclo 9: se consolidan reglas estables sin eliminar reglas utiles previas.",
      "Ciclo 9: deduplicacion aplicada sobre identidad, estructura, calidad y LaTeX.",
      "Ciclo 9: transferencia transversal sin arrastre tematico literal.",
      "Ciclo 9: se mantienen alertas tecnicas locales y preguntas abiertas criticas."
    ]
  }
}