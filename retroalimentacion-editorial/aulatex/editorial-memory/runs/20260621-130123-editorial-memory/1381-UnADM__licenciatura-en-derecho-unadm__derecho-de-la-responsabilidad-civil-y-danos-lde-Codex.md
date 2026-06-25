{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia conservadora y sin regresion.",
    "Se preservan reglas estables de identidad UnADM, estructura argumentativa y control de calidad.",
    "Se mantiene separacion entre abstracciones reutilizables y contenido tematico no transferible.",
    "Se refuerza normalizacion obligatoria de salidas JSON antes de propagacion recursiva.",
    "Se conservan incidencias locales verificadas: rutas truncadas, placeholders sin resolver y plantilla .tex incompleta [supuesto tecnico]."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Mantener contexto curricular local confirmado: Licenciatura en Derecho, semestre 6, bloque 1, obligatoria, 8 creditos.",
    "Marcar como supuesto todo dato no confirmado por consigna o fuente oficial.",
    "Tratar memorias heredadas no verificadas como provisionales hasta confirmacion local.",
    "No declarar oficial el codigo LDE-S6B1 sin respaldo documental explicito [supuesto].",
    "No cambiar la convencion local danos/daños sin confirmacion documental."
  ],
  "structure_rules": [
    "Iniciar cada entrega con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto con la planeacion semanal y la consigna vigente.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener separacion editorial entre reporte, presentacion, programa analitico y bibliografia .bib."
  ],
  "activity_rules": [
    "Formular problema juridico pertinente a responsabilidad civil y daños.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Separar fundamento juridico, evidencia y analisis propio.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No arrastrar contenido tematico de otras materias si no aplica al nodo destino."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que afirmaciones juridicas tengan fuente o marca de analisis propio.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar control de no regresion sobre reglas utiles previas.",
    "Detectar y corregir rutas truncadas y placeholders sin resolver antes de compilar."
  ],
  "latex_rules": [
    "Usar español con acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Completar plantilla .tex truncada antes de uso productivo [supuesto tecnico].",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Verificar nombres canonicos de archivos antes de referenciarlos."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Registrar fuentes especificas por actividad en el .bib local de la materia.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Mantener trazabilidad entre citas usadas y entradas reales del .bib."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas estables y transversales.",
    "Evitar transferir redaccion literal o temas propios de una actividad origen.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Conservar compresion lossless por union y deduplicacion.",
    "Mantener alerta historica de normalizacion manual por salidas no estructuradas en ciclos iniciales."
  ],
  "open_questions": [
    "Confirmar guia oficial de formato para actividades de la materia.",
    "Confirmar convencion final danos/daños en todo el arbol.",
    "Confirmar si LDE-S6B1 es codigo oficial o interno [supuesto].",
    "Corregir placeholders de .bib en README y programa analitico.",
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
      "Problema juridico claro.",
      "Conceptos y fuentes pertinentes.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible.",
      "Disciplina editorial con trazabilidad."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables.",
      "Asegurar coherencia entre consigna, evidencia y argumento.",
      "Sostener calidad institucional reproducible en toda la materia."
    ],
    "style_markers": [
      "Supuestos etiquetados explicitamente.",
      "Secciones funcionales y comparables entre actividades.",
      "Cierre con utilidad para practica juridica.",
      "Sin invencion de fuentes."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Marco conceptual y normativo con citas.",
      "Analisis propio con postura.",
      "Cierre juridico aplicado."
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
          "source": "Normalizacion estructurada JSON",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita ambiguedad y permite auditoria editorial."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin problema definido no hay analisis pertinente."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion requiere fundamento normativo verificable."
        },
        {
          "source": "Responsabilidad civil",
          "target": "Daño",
          "kind": "depends_on",
          "justification": "La materia organiza el juicio juridico desde la nocion de daño."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "El criterio del estudiante convierte fuentes en decision argumentada."
        }
      ],
      "evidence": [
        "README local: pauta editorial e identidad institucional.",
        "Programa analitico local: proposito y ejes de trabajo.",
        "Archivo .bib local: fuentes institucionales base.",
        "Plantilla .tex local: truncamiento en bloque de autoria [supuesto tecnico]."
      ]
    },
    "reinforcement_log": [
      "Ciclo 16: deduplicacion completa sin recorte semantico.",
      "Ciclo 16: se preservan reglas utiles heredadas y locales sin regresion.",
      "Ciclo 16: se transfiere solo abstraccion estable desde nodo no equivalente.",
      "Ciclo 16: se refuerzan gates de JSON parseable y normalizacion previa.",
      "Ciclo 16: se mantienen vacios locales abiertos para validacion documental."
    ]
  }
}