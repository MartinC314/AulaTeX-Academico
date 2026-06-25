{
  "summary": [
    "Sincronizacion transversal ciclo 6 aplicada con estrategia progresiva y conservadora.",
    "Se preservan reglas institucionales UnADM y estructura reusable sin traslado tematico literal.",
    "Se refuerzan ejes estables: problema, conceptos o fuentes, analisis propio y conclusion juridica transferible.",
    "Se mantiene compresion lossless por union y deduplicacion sin regresion.",
    "Persisten alertas tecnicas locales verificadas: JSON no estructurado previo, rutas truncadas y placeholders sin resolver."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar contexto curricular local confirmado de la materia destino.",
    "Marcar como supuesto todo dato no confirmado por consigna o guia oficial.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Usar la carpeta de materia como entrada canonica."
  ],
  "structure_rules": [
    "Iniciar cada entrega con encuadre breve del problema juridico o social.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear el producto al tipo solicitado en la planeacion semanal.",
    "Mantener separacion editorial entre reporte, presentacion, programa analitico y bibliografia."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica aplicable a la practica profesional.",
    "No arrastrar contenido tematico de otra asignatura si no aplica a responsabilidad civil y dano."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que cada afirmacion juridica tenga fuente o marca de analisis propio.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar control de no regresion sobre reglas utiles previas."
  ],
  "latex_rules": [
    "Usar espanol con acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Corregir rutas truncadas y placeholders sin resolver antes de compilar.",
    "Supuesto: la plantilla .tex local esta truncada en authortable y debe completarse."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Registrar fuentes especificas por actividad en el .bib local de la materia.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "No inventar referencias; registrar vacios como preguntas abiertas.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables en nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, calidad y grafo conceptual.",
    "Evitar transferir redaccion literal o contenido tematico puntual del origen.",
    "Mantener normalizacion manual en nodos con historial de salida no estructurada.",
    "Propagar alertas de placeholders y rutas truncadas como control tecnico general."
  ],
  "open_questions": [
    "Confirmar guia oficial de formato para actividades de la materia destino.",
    "Confirmar convencion final de nombres danos versus daños en todo el arbol.",
    "Confirmar si LDE-S6B1 es codigo oficial o mantenerlo como supuesto.",
    "Confirmar resolucion del placeholder Slug en README y programa analitico.",
    "Confirmar cierre tecnico de authortable en la plantilla .tex local."
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
        "Fuente curricular local: malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Problema juridico claro.",
      "Conceptos y fuentes pertinentes.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible.",
      "Rigor tecnico y trazabilidad editorial."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables.",
      "Unificar calidad editorial transversal sin perder contexto local.",
      "Asegurar utilidad profesional del cierre juridico."
    ],
    "style_markers": [
      "Supuestos declarados de forma explicita.",
      "Secciones funcionales y auditables.",
      "Citas verificables y consistentes con .bib.",
      "Cierre con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Marco conceptual y normativo con evidencia.",
      "Analisis propio con postura.",
      "Conclusion juridica aplicada."
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
          "justification": "La identidad institucional exige trazabilidad y citas verificables."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere una pregunta juridica definida."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida depende del sustento normativo."
        },
        {
          "source": "Responsabilidad civil",
          "target": "Dano",
          "kind": "depends_on",
          "justification": "El campo material de la asignatura se articula sobre dano juridicamente relevante."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La estructura valida evita ambiguedad y perdida de reglas."
        }
      ],
      "evidence": [
        "README local de la materia destino.",
        "Programa analitico local.",
        "Archivo .bib local con fuentes institucionales.",
        "Historial de incidencias de salida no estructurada y truncamientos."
      ]
    },
    "reinforcement_log": [
      "Se conservaron reglas utiles previas sin eliminacion.",
      "Se deduplicaron formulaciones equivalentes.",
      "Se reforzaron gates de JSON y normalizacion.",
      "Se mantuvo separacion entre abstraccion estable y contenido tematico local.",
      "Se dejaron explicitos los supuestos tecnicos pendientes."
    ]
  }
}