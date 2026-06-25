{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia conservadora y sin regresion.",
    "Se preservan reglas estables de identidad UnADM, estructura argumentativa y control de calidad JSON.",
    "Se transfiere solo abstraccion reusable desde actividad origen, sin arrastre tematico de Filosofia del Derecho.",
    "Se refuerza el nucleo editorial de materia: problema, conceptos/fuentes, analisis propio y conclusion juridica transferible.",
    "Se mantienen alertas locales verificadas: rutas truncadas, placeholders sin resolver y plantilla .tex incompleta [supuesto tecnico local]."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar contexto curricular local confirmado de la materia destino.",
    "Marcar como supuesto todo dato no visible en consigna o guia oficial.",
    "Tratar memorias heredadas no verificadas como provisionales hasta confirmacion local.",
    "No cambiar convenciones locales de nombres sin evidencia documental."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como entrada canonica.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear el producto final con la planeacion semanal y la consigna vigente.",
    "Mantener separacion editorial entre reporte, presentacion, programa analitico y .bib."
  ],
  "activity_rules": [
    "Formular una pregunta juridica clara para cada actividad.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Separar fundamento juridico, evidencia y analisis propio.",
    "Cerrar con conclusion juridica aplicable a la practica profesional.",
    "No transferir contenido tematico de otra asignatura si no es compatible con responsabilidad civil y danos."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que toda afirmacion juridica tenga fuente o marca de analisis propio.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar control de no regresion sobre reglas utiles previas."
  ],
  "latex_rules": [
    "Usar espanol con acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Corregir rutas truncadas y placeholders sin resolver antes de compilar.",
    "Completar plantilla .tex truncada antes de uso productivo [supuesto tecnico local]."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Registrar fuentes especificas por actividad en el .bib local de la materia.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Si falta referencia, registrar vacio como pregunta abierta."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas estables y transversales.",
    "Evitar transferencia de redaccion literal o contenido puntual de actividad origen.",
    "Mantener compresion lossless por union y deduplicacion.",
    "Preservar alertas tecnicas como controles generales, no como contenido tematico.",
    "Revalidar JSON y estructura antes de cada salto lateral o ascendente."
  ],
  "open_questions": [
    "Confirmar guia oficial de formato para actividades de la materia destino.",
    "Confirmar convencion final de nombres con danos o daños en todo el arbol.",
    "Confirmar si el codigo LDE-S6B1 es oficial [supuesto vigente].",
    "Resolver placeholder del .bib en README y programa analitico.",
    "Completar y validar bloque authortable truncado en plantilla .tex."
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
        "Asignatura: Derecho de la responsabilidad civil y danos [convencion local pendiente].",
        "Fuente curricular: UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Problema juridico bien delimitado.",
      "Conceptos y fuentes pertinentes.",
      "Analisis propio con sustento normativo y doctrinal.",
      "Conclusion juridica transferible a la practica profesional.",
      "Rigor tecnico editorial para produccion LaTeX reutilizable."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables y utiles.",
      "Garantizar coherencia institucional, argumentativa y tecnica en toda entrega.",
      "Sostener un cerebro editorial persistente sin perdida semantica."
    ],
    "style_markers": [
      "Supuestos marcados de forma explicita.",
      "Secciones funcionales y verificables.",
      "Cierre con criterio juridico propio.",
      "Sin afirmaciones sin respaldo."
    ],
    "argumentative_patterns": [
      "Problema inicial breve y contextualizado.",
      "Marco conceptual y normativo con citas.",
      "Analisis propio que conecta hechos, normas y doctrina.",
      "Conclusion aplicada con transferencia profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion JSON",
        "Problema juridico",
        "Marco normativo o doctrinal",
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
          "justification": "El marco institucional exige citas verificables y formato consistente."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita reutilizar salidas ambiguas y mantiene trazabilidad editorial."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin pregunta juridica definida no hay argumentacion consistente."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion requiere fundamento verificable."
        },
        {
          "source": "Responsabilidad civil",
          "target": "Dano",
          "kind": "depends_on",
          "justification": "La materia articula imputacion y reparacion desde la nocion de dano."
        }
      ],
      "evidence": [
        "README local de materia.",
        "Programa analitico local.",
        "Archivo .bib local con claves institucionales.",
        "Incidencias tecnicas locales observables en rutas y plantilla .tex."
      ]
    },
    "reinforcement_log": [
      "Ciclo 13: deduplicacion completa sin recorte semantico.",
      "Ciclo 13: se reforzaron gates de JSON parseable y no regresion.",
      "Ciclo 13: se consolidaron patrones argumentativos transversales no tematicos.",
      "Ciclo 13: se mantuvieron supuestos tecnicos locales y preguntas abiertas operativas."
    ]
  }
}