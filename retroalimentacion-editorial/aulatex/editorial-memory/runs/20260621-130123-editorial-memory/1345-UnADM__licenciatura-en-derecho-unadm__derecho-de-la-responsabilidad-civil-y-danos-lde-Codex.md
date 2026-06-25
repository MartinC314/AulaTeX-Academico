{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia conservadora y sin regresion.",
    "Se preservan reglas estables de identidad UnADM, estructura argumentativa y calidad tecnica.",
    "Se refuerza deduplicacion lossless y normalizacion obligatoria antes de propagacion.",
    "Se mantiene separacion entre reglas editoriales generales y contenido tematico local.",
    "Se conservan alertas locales verificables: JSON no parseable historico, placeholders y truncamientos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar contexto curricular local confirmado: Licenciatura en Derecho, semestre 6, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no confirmado por consigna o guia oficial.",
    "Tratar memorias heredadas no verificadas como provisionales hasta confirmacion local.",
    "No declarar oficial el codigo LDE-S6B1 sin respaldo documental explicito.",
    "No cambiar la convencion local danos/daños sin confirmacion documental."
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
    "Formular un problema juridico activador de responsabilidad civil y dano.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Separar fundamento juridico, evidencia y analisis propio.",
    "No arrastrar contenido tematico de otras materias si no aplica al nodo destino.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Adaptar solo abstracciones editoriales estables en transferencias transversales."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que toda afirmacion juridica tenga fuente o marca de analisis propio.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Detectar y corregir rutas truncadas, caracteres rotos y placeholders sin resolver.",
    "Aplicar control de no regresion sobre reglas utiles previas."
  ],
  "latex_rules": [
    "Usar español con acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Verificar nombres de archivo reales antes de referenciarlos.",
    "Resolver tokens tipo $(@{...}.Slug) en README y programa analitico.",
    "Completar plantilla .tex truncada antes de compilar [supuesto tecnico local]."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Registrar fuentes especificas por actividad en el .bib local de la materia.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No inventar referencias; registrar vacios como preguntas abiertas.",
    "Conservar metadatos minimos: autor, titulo, año y fuente/editorial o URL.",
    "Mantener como base local unadmSitioWeb y unadmMallaDerecho2024."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas estables y no redaccion literal.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferencia de contenido tematico especifico de Filosofia del Derecho.",
    "Aplicar compresion por union-dedupe sin recorte semantico.",
    "Mantener alerta historica de normalizacion manual por salidas no estructuradas previas.",
    "Propagar controles tecnicos de placeholders y truncamientos como higiene editorial general."
  ],
  "open_questions": [
    "Confirmar guia oficial de formato para actividades de esta materia.",
    "Confirmar si LDE-S6B1 es codigo oficial o interno [supuesto].",
    "Confirmar convencion final de nombres con danos versus daños.",
    "Validar y corregir entradas truncadas en README (reporte y referencias).",
    "Resolver placeholder del .bib en README y programa analitico.",
    "Completar bloque authortable truncado en plantilla .tex."
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
        "Entrada canonica por carpeta de materia.",
        "Normalizacion estructurada previa a propagacion."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 6, bloque 1, obligatoria, 8 creditos.",
        "Asignatura: Derecho de la responsabilidad civil y danos.",
        "Fuente curricular local: malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Problema juridico definido.",
      "Conceptos y fuentes verificables.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible.",
      "Disciplina tecnica en estructura y validacion."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables y utiles para la practica juridica.",
      "Sostener continuidad editorial institucional entre actividades, materias y ciclos."
    ],
    "style_markers": [
      "Supuestos explicitados.",
      "Secciones funcionales y trazables.",
      "Cierre con criterio juridico propio.",
      "Sincronizacion transversal sin traslado tematico literal."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Marco conceptual y normativo con evidencia.",
      "Analisis propio con contraste.",
      "Cierre aplicado a practica profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada JSON",
        "Problema juridico",
        "Marco normativo/doctrinal",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Responsabilidad civil",
        "Daño",
        "Integridad academica",
        "Trazabilidad bibliografica"
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
          "justification": "La identidad institucional exige citas verificables y consistencia formal."
        },
        {
          "source": "Normalizacion estructurada JSON",
          "target": "Trazabilidad bibliografica",
          "kind": "supports",
          "justification": "La estructura valida reduce ambiguedad y facilita control de referencias."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere pregunta juridica delimitada."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion exige base normativa y doctrinal verificable."
        },
        {
          "source": "Daño",
          "target": "Responsabilidad civil",
          "kind": "depends_on",
          "justification": "El nucleo de la materia articula responsabilidad desde la nocion de daño."
        },
        {
          "source": "Argumentacion reusable",
          "target": "Sincronizacion transversal",
          "kind": "develops",
          "justification": "Se transfieren patrones estables sin mover contenido tematico de origen."
        }
      ],
      "evidence": [
        "README local: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico local: proposito y ejes de trabajo.",
        "Archivo .bib local: unadmSitioWeb y unadmMallaDerecho2024.",
        "Plantilla .tex local truncada en authortable [supuesto tecnico].",
        "Historial: incidencias de salida no estructurada y necesidad de normalizacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 7: deduplicacion completa de reglas repetidas sin perdida semantica.",
      "Ciclo 7: se conserva regla institucional de bloqueo por JSON no parseable.",
      "Ciclo 7: se consolida patron argumentativo comun (problema-marco-analisis-cierre).",
      "Ciclo 7: se mantiene separacion entre abstracciones editoriales y contenido tematico local.",
      "Ciclo 7: se refuerzan controles tecnicos de placeholders, truncamientos y compilacion."
    ]
  }
}