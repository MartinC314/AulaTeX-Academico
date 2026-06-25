{
  "summary": [
    "Materia destino consolidada: Historia del Derecho en Mexico, Licenciatura en Derecho UnADM.",
    "Se preserva memoria local verificada desde README, programa analitico, plantilla LaTeX y .bib.",
    "Se integra del origen solo abstraccion transversal reusable: cinco ejes, postura propia, citas verificables y cierre juridico.",
    "Se evita transferir contenido tematico, bibliografia o casos de Filosofia del Derecho sin evidencia local.",
    "Se mantiene alerta historica por salidas no JSON parseables en ciclos previos.",
    "Se aplica compresion union-dedupe sin eliminar reglas utiles previas.",
    "Se refuerza el cerebro editorial de materia con identidad UnADM, trazabilidad y control de calidad."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar nombre local de materia: Historia del Derecho en Mexico.",
    "Conservar ubicacion curricular local: semestre 1, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Mantener fuente curricular local: UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
    "Marcar como supuesto cualquier dato no visible en consigna o documentos locales.",
    "Tratar fuentes operativas heredadas de Codex o GPT-Pro como provisionales hasta confirmacion local.",
    "Conservar antecedente institucional provisional: Codex desde ingenieria-en-sistemas-computacionales.",
    "Conservar antecedente local provisional: Codex desde historia-del-derecho-en-mexico-lde.",
    "Conservar antecedente transversal provisional: GPT-Pro desde Actividad 1.",
    "No importar datos curriculares de Filosofia del Derecho al destino."
  ],
  "structure_rules": [
    "Alinear cada entrega a cinco ejes: problema, conceptos y fuentes, producto, analisis propio y conclusion transferible.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar bloques funcionales: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Transformar la planeacion semanal en reporte, presentacion o producto visual segun consigna.",
    "Mantener coherencia entre README, programa analitico, .tex y .bib.",
    "Registrar fuentes especificas de actividad en historia-del-derecho-en-mexico.bib.",
    "Conservar subcarpeta referencias-historia-del-derecho-en-mexico para apoyo documental.",
    "Corregir placeholders de Slug en README y programa antes de automatizar.",
    "No mezclar contenido tematico de Filosofia del Derecho sin evidencia local verificable."
  ],
  "activity_rules": [
    "Verificar que el producto corresponda a la consigna de la actividad.",
    "Adaptar formato de salida al producto solicitado: reporte, presentacion o visual.",
    "Usar conceptos, normas, doctrina o datos pertinentes al problema.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica aplicable a la practica profesional.",
    "No asumir fuentes de otras semanas o materias como fuentes de la actividad local."
  ],
  "quality_gates": [
    "Validar JSON parseable en cada ciclo de memoria.",
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Aplicar union-dedupe sin recortar reglas utiles previas.",
    "Confirmar que toda afirmacion sustantiva tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar consistencia entre datos curriculares y portada del documento.",
    "Revisar render de nombres de archivo en README antes de automatizar.",
    "Revisar placeholders de Slug antes de compilar o citar.",
    "Normalizar manualmente salidas de ciclos previos marcadas como no estructuradas."
  ],
  "latex_rules": [
    "Usar reporte-historia-del-derecho-en-mexico.tex como base editable para reportes.",
    "Usar presentacion-historia-del-derecho-en-mexico.tex para productos tipo presentacion.",
    "Conservar metadatos clave: documenttitle, documentsubtitle, documentsubject, coursename y coursecode.",
    "Actualizar documentsubtitle con numero y nombre real de actividad.",
    "Mantener coursecode local LDE-S1B1 salvo confirmacion contraria.",
    "Conservar universidad, facultad, departamento, imagen institucional y ubicacion.",
    "Mantener tabla de autor con alumno, matricula, figura docente, semestre/bloque y tipo/creditos.",
    "No eliminar campos institucionales; solo actualizar valores concretos por actividad.",
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Corregir caracteres anomalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas."
  ],
  "bibliography_rules": [
    "Usar historia-del-derecho-en-mexico.bib como repositorio bibliografico local.",
    "Conservar entradas institucionales existentes de UnADM y malla curricular.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Agregar solo fuentes realmente consultadas.",
    "No inventar referencias.",
    "Conservar metadatos minimos: autor, titulo, año, fuente editorial o URL.",
    "Incluir trazabilidad minima: origen y fecha de consulta cuando aplique.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Corregir placeholders de Slug antes de compilar o citar.",
    "No propagar bibliografia de Filosofia del Derecho sin consulta efectiva."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Propagar a niveles superiores reglas de validacion JSON y normalizacion temprana.",
    "Reutilizar en materias hermanas la estructura de cinco ejes con ajuste tematico.",
    "Propagar solo reglas editoriales transversales verificables.",
    "No propagar datos curriculares especificos de esta materia a nodos laterales.",
    "Mantener alerta de salidas no parseables en niveles superiores.",
    "Aplicar normalizacion manual si se detecta salida no estructurada en nodos vecinos.",
    "Evitar regresiones respecto de reglas utiles previas.",
    "Sincronizar transversalmente sin copiar redaccion literal ni contenido tematico local."
  ],
  "open_questions": [
    "Confirmar si la fuente operativa provisional Codex debe reemplazarse por una fuente definitiva.",
    "Confirmar si el antecedente GPT-Pro desde Actividad 1 es solo transversal o tambien operativo.",
    "Definir nombre oficial de figura docente en plantillas.",
    "Confirmar si LDE-S1B1 es codigo oficial o codigo local.",
    "Validar acentuacion oficial de Mexico/México segun lineamiento institucional.",
    "Corregir entradas con salto de linea anomalo en README: eporte y eferencias [supuesto de render].",
    "Confirmar producto exacto y rubrica de cada actividad antes de desarrollar.",
    "Confirmar fuentes obligatorias por semana o unidad.",
    "Confirmar si la materia requiere bibliografia historico-juridica base adicional."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Institucional con voz estudiantil.",
        "Conservador ante inferencias no verificadas."
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
      "Identidad institucional UnADM.",
      "Cinco ejes editoriales.",
      "Problema juridico o social como punto de partida.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto alineado a planeacion semanal.",
      "Analisis propio y postura academica.",
      "Conclusion transferible a la practica juridica.",
      "Integridad academica.",
      "Trazabilidad bibliografica.",
      "Coherencia entre consigna y producto.",
      "Sincronizacion transversal sin traslado tematico indebido."
    ],
    "reason_for_being": [
      "Orientar productos academicos de Historia del Derecho en Mexico con claridad, fundamento juridico, evidencia y transferencia profesional.",
      "Transformar la planeacion semanal en reportes, presentaciones y productos visuales.",
      "Integrar problema, conceptos, fuentes, analisis propio y cierre argumentativo.",
      "Preservar un cerebro editorial reusable para actividades de la materia.",
      "Evitar que la propagacion transversal contamine el contexto local con fuentes o temas no verificados."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Objetivo puntual antes del desarrollo.",
      "Secciones funcionales y trazables.",
      "Citas explicitas y verificables.",
      "Marcado explicito de supuestos.",
      "Cierre con criterio juridico propio.",
      "Metadatos UnADM consistentes.",
      "Redaccion academica sin relleno.",
      "Inferencias conservadoras."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo al inicio.",
      "Definir conceptos clave antes de argumentar.",
      "Relacionar fuentes con el problema planteado.",
      "Distinguir hechos, normas, doctrina y postura propia.",
      "Contrastar evidencia cuando exista tension interpretativa.",
      "Evitar resumen descriptivo como producto final.",
      "Conectar desarrollo y conclusion con la pregunta guia.",
      "Cerrar con implicacion practica juridica.",
      "Ajustar profundidad al producto y rubrica solicitados."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Historia del Derecho en Mexico",
        "Licenciatura en Derecho",
        "Semestre 1 bloque 1",
        "Cinco ejes editoriales",
        "Problema juridico o social",
        "Conceptos juridicos e historicos",
        "Normas, doctrina y datos pertinentes",
        "Analisis propio",
        "Postura academica",
        "Conclusion transferible",
        "Integridad academica",
        "Citas verificables",
        "Trazabilidad bibliografica",
        "Normalizacion JSON",
        "Plantilla LaTeX local",
        "Repositorio bibliografico local",
        "Coherencia entre README, programa, .tex y .bib",
        "Placeholders de Slug",
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
          "justification": "La pauta local exige identidad UnADM, citas verificables y conclusion juridica."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Coherencia entre consigna y producto",
          "kind": "supports",
          "justification": "Los ejes ordenan problema, conceptos, producto, analisis y cierre."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El problema inicial activa la argumentacion del estudiante."
        },
        {
          "source": "Citas verificables",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La verificabilidad impide afirmaciones sin respaldo."
        },
        {
          "source": "Trazabilidad bibliografica",
          "target": "Citas verificables",
          "kind": "supports",
          "justification": "Los metadatos y la fecha de consulta permiten comprobar fuentes."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion transversal conservadora",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay reutilizacion segura."
        },
        {
          "source": "Plantilla LaTeX local",
          "target": "Identidad institucional UnADM",
          "kind": "supports",
          "justification": "La plantilla contiene portada, metadatos y tabla institucional."
        },
        {
          "source": "Repositorio bibliografico local",
          "target": "Trazabilidad bibliografica",
          "kind": "supports",
          "justification": "El .bib local centraliza fuentes base y fuentes de actividad."
        },
        {
          "source": "Placeholders de Slug",
          "target": "Compilacion LaTeX confiable",
          "kind": "contrasts",
          "justification": "Los tokens sin expandir generan rutas o referencias inestables."
        },
        {
          "source": "Propagacion transversal conservadora",
          "target": "Contenido tematico de Filosofia del Derecho",
          "kind": "contrasts",
          "justification": "Solo se transfieren abstracciones editoriales, no temas ni bibliografia no consultada."
        },
        {
          "source": "Conclusion transferible",
          "target": "Practica profesional juridica",
          "kind": "develops",
          "justification": "El cierre debe proyectar utilidad juridica profesional."
        },
        {
          "source": "README de materia",
          "target": "Carpeta de materia como entrada canonica",
          "kind": "supports",
          "justification": "El README declara la carpeta como punto de entrada de la asignatura."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 1, bloque 1, obligatoria, 8 creditos.",
        "README local: fuente curricular malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canonico.",
        "README local: identidad UnADM, integridad academica, citas verificables y conclusion juridica.",
        "Programa analitico local: productos academicos con claridad, fundamento juridico, evidencia y transferencia profesional.",
        "Programa analitico local: transformar planeacion semanal en reportes, presentaciones y productos visuales.",
        "Programa analitico local: cinco ejes de trabajo.",
        "Bibliografia local: unadmSitioWeb.",
        "Bibliografia local: unadmMallaDerecho2024.",
        "Plantilla local: documenttitle, documentsubtitle, documentsubject, coursename y coursecode.",
        "Plantilla local: alumno Martin Jonathan de la Cruz y matricula ES2611202040.",
        "Plantilla local: figura docente por definir.",
        "Plantilla local: semestre/bloque 1/1 y tipo/creditos obligatoria/8.",
        "Memoria heredada: hubo salida no JSON parseable desde Codex.",
        "Transferencia ciclo 15: se incorporan solo abstracciones editoriales estables del origen."
      ]
    },
    "reinforcement_log": [
      "Ciclo 15: se consolida union-dedupe entre memoria destino, herencia institucional y abstracciones del origen.",
      "Ciclo 15: se preserva identidad curricular local de Historia del Derecho en Mexico.",
      "Ciclo 15: se refuerza la regla de no transferir contenido tematico de Filosofia del Derecho.",
      "Ciclo 15: se normalizan reglas repetidas sobre cinco ejes, citas verificables y conclusion juridica.",
      "Ciclo 15: se mantiene bloqueo por JSON no parseable.",
      "Ciclo 15: se fortalecen gates de consistencia entre README, programa, .tex y .bib.",
      "Ciclo 15: se fijan placeholders de Slug como riesgo operativo antes de compilar.",
      "Ciclo 15: se conserva la pregunta abierta sobre acentuacion oficial Mexico/México.",
      "Ciclo 15: se actualiza grafo conceptual con relaciones validas y evidencia local."
    ]
  }
}