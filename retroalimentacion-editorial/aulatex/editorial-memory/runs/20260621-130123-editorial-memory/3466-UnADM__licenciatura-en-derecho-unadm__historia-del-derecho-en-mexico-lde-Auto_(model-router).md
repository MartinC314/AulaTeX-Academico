{
  "summary": [
    "Materia destino: Historia del Derecho en Mexico, Licenciatura en Derecho UnADM.",
    "Memoria local verificada desde README, programa analitico, plantilla LaTeX y .bib.",
    "Se preserva alerta historica de salidas no JSON parseables.",
    "Se consolida sincronizacion transversal conservadora desde Filosofia del Derecho.",
    "Se transfieren solo abstracciones editoriales estables: identidad, cinco ejes, trazabilidad y calidad.",
    "No se transfiere contenido tematico ni bibliografia de Filosofia del Derecho sin consulta local.",
    "La carpeta de materia funciona como punto de entrada canonico.",
    "La materia conserva semestre 1, bloque 1, obligatoria, 8 creditos.",
    "La plantilla declara autor Martin Jonathan de la Cruz, matricula ES2611202040 y figura docente por definir.",
    "Se mantiene compresion union-dedupe sin recortar reglas utiles previas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, metadatos y redaccion.",
    "Usar nombre oficial local: Historia del Derecho en Mexico.",
    "Conservar datos curriculares locales: semestre 1, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Mantener fuente curricular local: UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
    "Marcar como supuesto cualquier dato no visible en consigna o documentos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar antecedente provisional: Codex desde historia-del-derecho-en-mexico-lde.",
    "Conservar antecedente provisional institucional: Codex desde ingenieria-en-sistemas-computacionales.",
    "Conservar antecedente provisional transversal: GPT-Pro desde Actividad 1.",
    "No propagar datos curriculares de Filosofia del Derecho a esta materia."
  ],
  "structure_rules": [
    "Alinear cada entrega a cinco ejes: problema, conceptos y fuentes, producto, analisis propio, conclusion transferible.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones funcionales: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Mantener coherencia entre README, programa analitico, .tex y .bib.",
    "Transformar planeacion semanal en reporte, presentacion o producto visual segun consigna.",
    "Registrar fuentes especificas de actividad en historia-del-derecho-en-mexico.bib.",
    "Conservar subcarpeta referencias-historia-del-derecho-en-mexico para apoyo documental.",
    "Corregir placeholders de Slug en README y programa antes de automatizar.",
    "No mezclar contenido tematico de Filosofia del Derecho sin evidencia local verificable."
  ],
  "activity_rules": [
    "Iniciar cada actividad con problema juridico o social concreto.",
    "Usar conceptos, normas, doctrina o datos pertinentes al problema.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Adaptar formato al producto solicitado: reporte, presentacion o visual.",
    "Cerrar con conclusion juridica aplicable a la practica profesional.",
    "Verificar que el producto corresponda a la consigna local de actividad.",
    "No asumir que fuentes de otras materias o semanas corresponden a una actividad local."
  ],
  "quality_gates": [
    "Validar JSON parseable en cada ciclo de memoria.",
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar respuesta no estructurada antes de reutilizarla.",
    "Normalizar manualmente salidas no estructuradas antes de aplicar aguas abajo.",
    "Revisar estructura minima completa antes de propagar.",
    "Aplicar union-dedupe sin recortar reglas utiles previas.",
    "Confirmar que toda afirmacion sustantiva tenga soporte verificable o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar consistencia entre datos curriculares y portada del documento.",
    "Revisar render de nombres de archivo en README antes de automatizar.",
    "Revisar placeholders de Slug antes de compilar o citar.",
    "Validar correspondencia entre consigna, producto, desarrollo y conclusion."
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
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anomalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir entradas con salto de linea anomalo en README: eporte y eferencias [supuesto de render]."
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
    "No propagar bibliografia de Filosofia del Derecho sin consulta efectiva.",
    "Validar consistencia entre citas en texto y entradas BibTeX."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Propagar arriba y laterales solo reglas editoriales transversales verificables.",
    "Reutilizar estructura de cinco ejes con ajuste tematico por asignatura.",
    "Propagar validacion JSON y normalizacion temprana a materias hermanas.",
    "Mantener alerta de salidas no parseables en niveles superiores.",
    "No propagar datos curriculares especificos de esta materia a laterales.",
    "No propagar bibliografia local a nodos no consultados.",
    "Aplicar normalizacion manual si se detecta salida no estructurada en nodos vecinos.",
    "Evitar regresiones respecto de reglas utiles previas.",
    "Ciclo 1 necesita normalizacion manual si se reutiliza."
  ],
  "open_questions": [
    "Confirmar si Codex debe reemplazarse por fuente operativa definitiva.",
    "Confirmar si GPT-Pro desde Actividad 1 debe conservarse solo como antecedente provisional.",
    "Definir nombre oficial de figura docente en plantillas.",
    "Confirmar si LDE-S1B1 es codigo oficial o codigo local.",
    "Validar acentuacion oficial de Mexico/México segun lineamiento institucional.",
    "Verificar y corregir posibles errores de render en listado de archivos del README.",
    "Confirmar nombre canonico final del archivo .bib local.",
    "Confirmar rubricas y consignas especificas de cada actividad.",
    "Confirmar fuentes obligatorias por semana o unidad.",
    "Confirmar si la materia requiere productos visuales ademas de reporte y presentacion."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Institucional con voz estudiantil.",
        "Conservador en inferencias no verificadas."
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
      "Problema juridico o social que activa la asignatura.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion transferible a la practica juridica.",
      "Integridad academica.",
      "Trazabilidad bibliografica.",
      "Coherencia entre consigna y producto.",
      "Sincronizacion transversal sin copia tematica indebida."
    ],
    "reason_for_being": [
      "Orientar productos academicos con claridad, fundamento juridico, evidencia y transferencia profesional.",
      "Transformar la planeacion semanal en reportes, presentaciones y productos visuales.",
      "Integrar problema, conceptos, fuentes, analisis propio y cierre argumentativo.",
      "Preservar un cerebro editorial minimo y estable para la materia.",
      "Evitar regresiones mediante union-dedupe conservadora."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Objetivo puntual antes del desarrollo.",
      "Secciones funcionales y trazables.",
      "Citas explicitas y verificables.",
      "Marcado explicito de supuestos.",
      "Postura estudiantil argumentada.",
      "Cierre con criterio juridico propio.",
      "Metadatos institucionales consistentes.",
      "Lenguaje juridico preciso.",
      "Ajuste estricto al producto solicitado."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo al inicio.",
      "Delimitar conceptos clave antes del analisis.",
      "Relacionar marco normativo o doctrinal con el problema.",
      "Contrastar evidencia con postura propia.",
      "Evitar resumen descriptivo sin tesis.",
      "Cerrar con implicacion practica juridica.",
      "Alinear consigna, desarrollo, citas y conclusion.",
      "Separar bibliografia base de fuentes especificas de actividad.",
      "Marcar como supuesto lo no confirmado por la consigna local."
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
        "Producto solicitado por planeacion",
        "Analisis propio",
        "Postura academica",
        "Conclusion transferible",
        "Integridad academica",
        "Trazabilidad bibliografica",
        "Normalizacion JSON",
        "Coherencia entre README programa .tex y .bib",
        "Plantilla LaTeX local",
        "Bibliografia local",
        "Malla curricular Derecho UnADM",
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
          "justification": "La pauta local exige identidad UnADM, citas verificables y conclusion juridica."
        },
        {
          "source": "Malla curricular Derecho UnADM",
          "target": "Semestre 1 bloque 1",
          "kind": "supports",
          "justification": "El README local declara la fuente curricular y la ubicacion de la materia."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Coherencia entre README programa .tex y .bib",
          "kind": "supports",
          "justification": "Los ejes ordenan problema, fuentes, producto, analisis y cierre."
        },
        {
          "source": "Producto solicitado por planeacion",
          "target": "Plantilla LaTeX local",
          "kind": "depends_on",
          "justification": "El formato final debe elegirse segun consigna: reporte, presentacion o visual."
        },
        {
          "source": "Analisis propio",
          "target": "Postura academica",
          "kind": "develops",
          "justification": "La entrega debe argumentar con criterio estudiantil y no solo resumir."
        },
        {
          "source": "Conclusion transferible",
          "target": "Practica juridica",
          "kind": "develops",
          "justification": "El cierre debe expresar aplicacion profesional del razonamiento juridico."
        },
        {
          "source": "Trazabilidad bibliografica",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La verificabilidad depende de fuentes consultables y metadatos minimos."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Sincronizacion transversal conservadora",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay propagacion segura."
        },
        {
          "source": "Supuestos marcados",
          "target": "Conservador en inferencias no verificadas",
          "kind": "supports",
          "justification": "Los datos no confirmados deben etiquetarse para evitar invenciones."
        },
        {
          "source": "Bibliografia local",
          "target": "Historia del Derecho en Mexico",
          "kind": "supports",
          "justification": "El .bib local contiene las fuentes institucionales iniciales de la materia."
        },
        {
          "source": "Sincronizacion transversal conservadora",
          "target": "Contenido tematico de Filosofia del Derecho",
          "kind": "contrasts",
          "justification": "Solo se comparten abstracciones editoriales, no contenido tematico ajeno."
        }
      ],
      "evidence": [
        "README local: materia, ubicacion curricular, estructura y pauta editorial.",
        "Programa analitico local: encuadre institucional, proposito y cinco ejes de trabajo.",
        "historia-del-derecho-en-mexico.bib: entradas unadmSitioWeb y unadmMallaDerecho2024.",
        "reporte-historia-del-derecho-en-mexico.tex: metadatos, autor, matricula y tabla institucional.",
        "presentacion-historia-del-derecho-en-mexico.tex: soporte local para productos tipo presentacion.",
        "Memoria heredada institucional: alerta de salida no JSON parseable.",
        "Memoria origen transversal: estructura de problema, conceptos, evidencia, analisis propio y conclusion.",
        "Regla de transferencia: compartir solo abstracciones estables entre nodos no equivalentes."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin eliminar reglas utiles.",
      "Se reforzo identidad UnADM con datos curriculares locales.",
      "Se mantuvo alerta de normalizacion por salidas no JSON parseables.",
      "Se incorporo la estructura transversal de cinco ejes sin copiar contenido tematico.",
      "Se conservaron reglas locales de LaTeX, .bib, README y placeholders.",
      "Se excluyeron citas y temas de Filosofia del Derecho no consultados localmente.",
      "Se corrigio el grafo para usar solo relaciones permitidas.",
      "Se marcaron como supuestos los puntos pendientes de confirmacion local."
    ]
  }
}