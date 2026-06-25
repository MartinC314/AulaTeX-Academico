{
  "summary": [
    "Materia destino consolidada: Historia del Derecho en Mexico, Licenciatura en Derecho UnADM.",
    "Memoria local verificada desde README, programa analitico, plantilla LaTeX y .bib local.",
    "Se preserva identidad institucional UnADM y marco curricular local: semestre 1, bloque 1, obligatoria, 8 creditos.",
    "Se mantiene alerta historica: hubo salidas no JSON parseables desde Codex y GPT-Pro.",
    "Se transfiere desde Filosofia del Derecho solo abstraccion editorial transversal.",
    "Se evita transferir contenido tematico o bibliografia de Filosofia del Derecho sin evidencia local.",
    "Se refuerzan cinco ejes editoriales: problema, conceptos y fuentes, producto, analisis propio, conclusion transferible.",
    "Se aplica compresion union-dedupe sin recortar reglas utiles previas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, metadatos y redaccion.",
    "Usar nombre local de materia: Historia del Derecho en Mexico.",
    "Conservar datos curriculares locales: semestre 1, bloque 1, obligatoria, 8 creditos.",
    "Mantener fuente curricular local: UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
    "Tratar la carpeta de materia como punto de entrada canonico.",
    "Marcar como supuesto cualquier dato no confirmado por consigna o documentos locales.",
    "Tratar fuentes operativas heredadas como provisionales hasta confirmacion local.",
    "Conservar antecedente provisional: Codex desde historia-del-derecho-en-mexico-lde.",
    "Conservar antecedente provisional institucional: Codex desde ingenieria-en-sistemas-computacionales.",
    "Conservar antecedente provisional transversal: GPT-Pro desde Actividad 1."
  ],
  "structure_rules": [
    "Alinear cada entrega a cinco ejes: problema, conceptos y fuentes, producto, analisis propio, conclusion transferible.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones funcionales: conceptos clave, marco historico-juridico, analisis propio y cierre.",
    "Transformar la planeacion semanal en reporte, presentacion o producto visual segun consigna.",
    "Mantener coherencia entre README, programa analitico, .tex y .bib.",
    "Registrar fuentes especificas de actividad en historia-del-derecho-en-mexico.bib.",
    "Conservar subcarpeta referencias-historia-del-derecho-en-mexico para apoyo documental.",
    "Corregir placeholders de Slug en README y programa antes de automatizar.",
    "No mezclar contenido tematico de Filosofia del Derecho sin evidencia local verificable."
  ],
  "activity_rules": [
    "Iniciar cada actividad con problema juridico o social concreto.",
    "Usar conceptos, normas, doctrina o datos pertinentes al problema.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Adaptar formato al producto solicitado: reporte, presentacion o visual.",
    "Cerrar con conclusion juridica aplicable a la practica profesional.",
    "No asumir fuentes de otra asignatura como fuentes de esta materia.",
    "No asumir bibliografia de Filosofia del Derecho sin consulta efectiva."
  ],
  "quality_gates": [
    "Validar JSON parseable en cada ciclo de memoria.",
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Comprobar que toda afirmacion sustantiva tenga soporte verificable o marca de supuesto.",
    "Validar correspondencia entre consigna, producto, desarrollo y conclusion.",
    "Verificar consistencia entre datos curriculares y portada del documento.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar union-dedupe sin recortar reglas utiles previas.",
    "Revisar render de nombres de archivo en README antes de automatizar.",
    "Revisar placeholders de Slug antes de compilar o citar."
  ],
  "latex_rules": [
    "Usar reporte-historia-del-derecho-en-mexico.tex como base editable para reportes.",
    "Usar presentacion-historia-del-derecho-en-mexico.tex para productos tipo presentacion.",
    "Conservar metadatos clave: documenttitle, documentsubtitle, documentsubject, coursename y coursecode.",
    "Actualizar documentsubtitle con numero y nombre real de actividad.",
    "Conservar universidad, facultad, departamento, imagen institucional y ubicacion.",
    "Mantener tabla de autor con alumno, matricula, figura docente, semestre/bloque y tipo/creditos.",
    "No eliminar campos institucionales; solo actualizar valores concretos por actividad.",
    "Mantener coursecode local LDE-S1B1 salvo confirmacion contraria.",
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Corregir caracteres anomalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico."
  ],
  "bibliography_rules": [
    "Usar historia-del-derecho-en-mexico.bib como repositorio bibliografico local.",
    "Conservar entradas institucionales existentes de UnADM y malla curricular.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Agregar solo fuentes realmente consultadas.",
    "No inventar referencias.",
    "Registrar fuentes especificas de cada actividad en el .bib de la asignatura.",
    "Conservar metadatos minimos: autor, titulo, año, fuente editorial o URL.",
    "Incluir trazabilidad minima: origen y fecha de consulta cuando aplique.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Corregir placeholders de Slug en README y programa antes de compilar o citar.",
    "No propagar bibliografia de Filosofia del Derecho sin consulta efectiva."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Propagar a niveles superiores reglas de validacion JSON y normalizacion temprana.",
    "Propagar laterales solo abstracciones editoriales transversales verificables.",
    "Reutilizar estructura de cinco ejes con ajuste tematico por asignatura.",
    "No propagar datos curriculares especificos de esta materia a laterales.",
    "Mantener alerta de salidas no parseables en niveles superiores.",
    "Priorizar deduplicacion por union sin regresiones.",
    "Aplicar normalizacion manual si se detectan salidas no estructuradas en nodos vecinos.",
    "Evitar transferir redaccion literal entre materias no equivalentes.",
    "Conservar especificidad local al incorporar reglas heredadas."
  ],
  "open_questions": [
    "Confirmar si la fuente operativa provisional debe reemplazarse por fuente definitiva.",
    "Definir nombre oficial de figura docente en plantillas.",
    "Confirmar si LDE-S1B1 es codigo oficial o codigo local.",
    "Validar acentuacion oficial de Mexico/México segun lineamiento institucional.",
    "Corregir posibles saltos anomalos en README: eporte y eferencias.",
    "Confirmar producto exacto de cada actividad antes de generar entrega.",
    "Confirmar rubrica de evaluacion especifica por actividad.",
    "Confirmar fuentes obligatorias de cada semana.",
    "Confirmar si la subcarpeta de referencias contiene materiales consultables adicionales.",
    "Confirmar si el nombre oficial de la materia debe incluir acento en México."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Institucional sin perder voz estudiantil."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada obligatoria antes de propagar.",
        "Portada y metadatos coherentes con plantilla local.",
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Historia del Derecho en Mexico.",
        "Semestre 1, bloque 1, obligatoria, 8 creditos.",
        "Fuente curricular local: malla-curricular-derecho-unadm.pdf.",
        "Coursecode local: LDE-S1B1 [supuesto hasta confirmacion oficial]."
      ]
    },
    "essence": [
      "Historia juridica tratada como base para comprender instituciones actuales.",
      "Problema juridico o social como punto de partida.",
      "Conceptos, normas, doctrina y datos historicos pertinentes.",
      "Producto solicitado por la planeacion semanal.",
      "Analisis propio y postura academica.",
      "Conclusion transferible a la practica juridica.",
      "Identidad institucional UnADM.",
      "Integridad academica.",
      "Trazabilidad bibliografica.",
      "Coherencia entre consigna y producto.",
      "Sincronizacion transversal sin copiar contenido tematico ajeno."
    ],
    "reason_for_being": [
      "Orientar productos academicos con claridad, fundamento juridico, evidencia y transferencia profesional.",
      "Transformar planeacion semanal en reportes, presentaciones y productos visuales.",
      "Conectar el estudio historico del derecho con problemas juridicos actuales.",
      "Ordenar cada entrega mediante problema, fuentes, analisis propio y cierre argumentativo.",
      "Preservar un cerebro editorial minimo, estable y verificable para la materia.",
      "Prevenir regresiones por salidas no estructuradas o fuentes no verificadas."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Objetivo puntual antes del desarrollo.",
      "Secciones funcionales y trazables.",
      "Marco historico-juridico diferenciado de opinion personal.",
      "Citas explicitas y verificables.",
      "Postura estudiantil argumentada.",
      "Cierre con criterio juridico propio.",
      "Marcado explicito de supuestos.",
      "Evitar redaccion literal heredada de materias no equivalentes.",
      "Usar nombre local de materia de forma consistente."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo al inicio.",
      "Contextualizar historicamente la institucion o fenomeno juridico.",
      "Definir conceptos clave antes de valorar.",
      "Vincular fuentes con afirmaciones especificas.",
      "Contrastar evidencia historica con relevancia juridica actual.",
      "Distinguir descripcion historica de analisis propio.",
      "Integrar postura academica del estudiante.",
      "Cerrar con implicacion practica para la formacion juridica.",
      "Alinear formato y profundidad a la consigna.",
      "Verificar que conclusion responda al problema inicial."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Historia del Derecho en Mexico",
        "Licenciatura en Derecho",
        "Semestre 1 bloque 1",
        "Cinco ejes editoriales",
        "Problema juridico o social",
        "Conceptos y fuentes pertinentes",
        "Marco historico-juridico",
        "Analisis propio",
        "Conclusion transferible",
        "Integridad academica",
        "Trazabilidad bibliografica",
        "Normalizacion JSON",
        "Coherencia entre consigna y producto",
        "Plantilla LaTeX local",
        "Repositorio bibliografico local",
        "Malla curricular de Derecho",
        "Fuentes institucionales UnADM",
        "Supuestos marcados",
        "Sincronizacion transversal conservadora"
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
          "justification": "La pauta local exige identidad UnADM, citas verificables y conclusion con criterio propio."
        },
        {
          "source": "Malla curricular de Derecho",
          "target": "Semestre 1 bloque 1",
          "kind": "supports",
          "justification": "El README declara la malla curricular como fuente de ubicacion curricular."
        },
        {
          "source": "Historia del Derecho en Mexico",
          "target": "Licenciatura en Derecho",
          "kind": "depends_on",
          "justification": "El README identifica la materia como parte de la Licenciatura en Derecho de la UnADM."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Coherencia entre consigna y producto",
          "kind": "supports",
          "justification": "Los ejes ordenan problema, fuentes, producto, analisis y conclusion."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El problema inicial activa la argumentacion y evita el resumen descriptivo."
        },
        {
          "source": "Conceptos y fuentes pertinentes",
          "target": "Marco historico-juridico",
          "kind": "supports",
          "justification": "Las fuentes verificables sustentan la contextualizacion historica y juridica."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La postura argumentada conduce a una conclusion aplicable a la practica juridica."
        },
        {
          "source": "Trazabilidad bibliografica",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La verificabilidad depende de metadatos, origen y consulta de fuentes."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Sincronizacion transversal conservadora",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay propagacion recursiva segura."
        },
        {
          "source": "Plantilla LaTeX local",
          "target": "Coherencia entre consigna y producto",
          "kind": "supports",
          "justification": "Los metadatos y subtitulos actualizados alinean la entrega con la actividad."
        },
        {
          "source": "Repositorio bibliografico local",
          "target": "Trazabilidad bibliografica",
          "kind": "supports",
          "justification": "El .bib local concentra fuentes base y especificas de la materia."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Historia del Derecho en Mexico",
          "kind": "contrasts",
          "justification": "La transferencia es transversal; no autoriza copiar contenido tematico ni bibliografia ajena."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicacion curricular, estructura y pauta editorial.",
        "Programa analitico local: encuadre institucional, proposito y cinco ejes de trabajo.",
        "historia-del-derecho-en-mexico.bib: entradas unadmSitioWeb y unadmMallaDerecho2024.",
        "Plantilla reporte local: metadatos de materia, autor, matricula, figura docente pendiente y datos curriculares.",
        "Plantilla presentacion local disponible para productos tipo presentacion.",
        "Memoria previa del destino: alerta por salidas no JSON parseables.",
        "Memoria de origen: reglas transversales de estructura, calidad, citas y postura argumentada.",
        "Regla de transferencia: compartir solo abstracciones estables entre nodos no equivalentes."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin eliminar contenido util.",
      "Se conservaron reglas locales verificadas por README, programa, .tex y .bib.",
      "Se incorporaron del origen solo patrones transversales de calidad y argumentacion.",
      "Se excluyo bibliografia tematica de Filosofia del Derecho por falta de consulta local.",
      "Se reforzo el bloqueo de propagacion ante JSON no parseable.",
      "Se corrigio el grafo para usar solo relaciones permitidas.",
      "Se marco como supuesto el codigo LDE-S1B1 hasta confirmacion oficial.",
      "Se mantuvo abierta la validacion de acentuacion Mexico/México.",
      "Se preservo la necesidad de corregir placeholders Slug antes de compilar.",
      "Se consolido cerebro editorial minimo para sincronizacion transversal progresiva."
    ]
  }
}