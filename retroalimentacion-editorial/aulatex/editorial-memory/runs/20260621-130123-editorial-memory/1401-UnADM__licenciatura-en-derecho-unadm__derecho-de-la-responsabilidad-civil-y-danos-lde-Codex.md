{
  "summary": [
    "Se mantiene sincronizacion transversal entre nodos no equivalentes con transferencia de reglas estables.",
    "Se conserva identidad UnADM, normalizacion estructurada y ejes argumentativos reutilizables.",
    "Se refuerza compresion lossless por union-dedupe sin recorte semantico ni regresion.",
    "Se preservan alertas tecnicas locales verificadas: JSON no parseable historico, rutas truncadas y placeholders sin resolver.",
    "Se evita traslado tematico literal de Filosofia del Derecho hacia Responsabilidad Civil y Danos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar contexto curricular local confirmado: Licenciatura en Derecho, semestre 6, bloque 1, obligatoria, 8 creditos.",
    "Marcar como supuesto todo dato no confirmado por consigna, guia o fuente institucional.",
    "Tratar memorias heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar carpeta de materia como entrada canonica editorial.",
    "No oficializar el codigo LDE-S6B1 sin respaldo documental explicito.",
    "No cambiar convencion local danos/daños sin confirmacion documental."
  ],
  "structure_rules": [
    "Iniciar cada entrega con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto final con la planeacion semanal y la consigna vigente.",
    "Mantener separacion editorial entre reporte, presentacion, programa analitico y .bib.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Formular problema juridico pertinente a responsabilidad civil y dano.",
    "Sustentar afirmaciones con fuentes verificables o marcar analisis propio.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Adaptar reglas heredadas solo si son compatibles con la materia destino.",
    "No arrastrar contenido tematico de origen cuando no sea aplicable.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Aplicar control de no regresion sobre reglas utiles heredadas.",
    "Confirmar que cada afirmacion juridica tenga fuente o etiqueta de supuesto/analisis propio.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Detectar y corregir rutas truncadas y placeholders sin resolver antes de propagar."
  ],
  "latex_rules": [
    "Usar espanol con acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres truncados en rutas y archivos antes de compilar.",
    "Completar plantilla .tex truncada en authortable antes de uso productivo [supuesto local]."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Registrar fuentes especificas por actividad en el .bib local de la materia.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener trazabilidad entre citas del texto y entradas BibTeX."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo abstracciones editoriales estables.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar propagar redaccion literal o contenido tematico puntual del nodo origen.",
    "Aplicar estrategia progresiva y conservadora: agregar mejoras verificables sin borrar reglas utiles.",
    "Mantener alerta de normalizacion manual por antecedentes de salida no estructurada (ciclos 1, 2 y 3).",
    "Propagar controles tecnicos de placeholders y truncamientos como regla general de higiene editorial."
  ],
  "open_questions": [
    "Confirmar guia oficial de formato para actividades de la materia destino.",
    "Confirmar convencion final de nombres con danos versus daños en todo el arbol.",
    "Confirmar estatus oficial del codigo de curso LDE-S6B1.",
    "Confirmar correccion definitiva de placeholders Slug en README y programa analitico.",
    "Confirmar correccion total de truncamientos en README y plantilla .tex."
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
        "Normalizacion estructurada obligatoria antes de propagacion.",
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
      "Conceptos, normas y doctrina pertinentes.",
      "Evidencia verificable con citas.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible a practica profesional."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos solidos y verificables.",
      "Asegurar consistencia institucional, argumentativa y tecnica en LaTeX.",
      "Permitir propagacion segura entre nodos mediante reglas estables y auditables."
    ],
    "style_markers": [
      "Declarar supuestos de forma explicita.",
      "Usar secciones funcionales y reutilizables.",
      "Evitar afirmaciones sin respaldo.",
      "Mantener cierre con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Plantear problema inicial breve.",
      "Desarrollar marco conceptual y normativo con fuentes.",
      "Contrastar ideas en analisis propio.",
      "Concluir con aplicacion juridica concreta."
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
          "justification": "El marco institucional exige formato consistente y citas verificables."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva segura",
          "kind": "supports",
          "justification": "Evita reutilizar salidas ambiguas o no parseables."
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
          "justification": "La conclusion se legitima con sustento normativo y doctrinal."
        },
        {
          "source": "Responsabilidad civil",
          "target": "Dano",
          "kind": "depends_on",
          "justification": "La materia estructura la responsabilidad a partir del dano juridico."
        },
        {
          "source": "Trazabilidad bibliografica",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La correspondencia texto-.bib evita citas huerfanas o inventadas."
        }
      ],
      "evidence": [
        "README local de la materia (ubicacion curricular y pauta editorial).",
        "Programa analitico local (proposito y ejes de trabajo).",
        "Archivo .bib local con entradas institucionales verificables.",
        "Incidencias locales observables: placeholders Slug y truncamientos [supuesto tecnico validable en archivos]."
      ]
    },
    "reinforcement_log": [
      "Ciclo 21: deduplicacion completa de reglas repetidas en identidad, estructura y calidad.",
      "Ciclo 21: preservadas reglas heredadas utiles sin eliminacion regresiva.",
      "Ciclo 21: reforzada separacion entre transferencia estable y contenido tematico no equivalente.",
      "Ciclo 21: mantenidas alertas de normalizacion manual por historial de salidas no estructuradas."
    ]
  }
}