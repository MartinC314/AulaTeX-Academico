{
  "summary": [
    "Materia destino consolidada: Historia del Derecho en Mexico, Licenciatura en Derecho UnADM.",
    "Se preserva identidad UnADM, marco curricular local y plantilla LaTeX verificable.",
    "Se sincroniza transversalmente solo abstraccion editorial estable desde Filosofia del Derecho.",
    "Se mantienen cinco ejes editoriales: problema, conceptos/fuentes, producto, analisis propio y conclusion transferible.",
    "Se conserva alerta historica de salidas no JSON parseables desde Codex y GPT-Pro.",
    "Se refuerza normalizacion estructurada antes de propagacion recursiva.",
    "Se evita copiar contenido tematico o bibliografia de Filosofia del Derecho sin evidencia local.",
    "Se conserva base bibliografica local con fuentes institucionales UnADM.",
    "Se detectan placeholders de Slug y errores de render en README y programa analitico.",
    "Se aplica compresion union-dedupe sin eliminar reglas utiles previas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar nombre local de materia: Historia del Derecho en Mexico.",
    "Conservar datos curriculares locales: semestre 1, bloque 1, obligatoria, 8 creditos.",
    "Mantener fuente curricular local: UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
    "Tratar la carpeta de materia como punto de entrada canonico.",
    "Vincular toda actividad a la Licenciatura en Derecho.",
    "Marcar como supuesto cualquier dato no visible en consigna o documentos locales.",
    "Tratar fuentes operativas heredadas no verificadas como provisionales.",
    "Conservar antecedente provisional: Codex desde historia-del-derecho-en-mexico-lde.",
    "Conservar antecedente institucional provisional: Codex desde ingenieria-en-sistemas-computacionales.",
    "Conservar antecedente provisional: GPT-Pro desde Actividad 1.",
    "Usar coursecode LDE-S1B1 solo como codigo local hasta confirmacion oficial.",
    "Validar acentuacion oficial de Mexico/México antes de entrega final."
  ],
  "structure_rules": [
    "Alinear cada entrega a cinco ejes: problema, conceptos/fuentes, producto, analisis propio y conclusion transferible.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones funcionales: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Transformar la planeacion semanal en reporte, presentacion o producto visual segun consigna.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener coherencia entre README, programa analitico, .tex y .bib.",
    "Registrar fuentes especificas de actividad en historia-del-derecho-en-mexico.bib.",
    "Conservar subcarpeta referencias-historia-del-derecho-en-mexico para apoyo documental.",
    "No mezclar contenido tematico de Filosofia del Derecho sin evidencia local verificable.",
    "Corregir placeholders de Slug en README y programa antes de automatizar.",
    "Corregir errores de render en nombres de archivo antes de referenciarlos."
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
    "Confirmar que el producto corresponda a la consigna local de actividad.",
    "No asumir que fuentes de otras semanas o materias correspondan a la actividad local.",
    "Conservar integridad academica y trazabilidad bibliografica en cada actividad."
  ],
  "quality_gates": [
    "Validar JSON parseable en cada ciclo de memoria.",
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Aplicar union-dedupe sin recortar reglas utiles previas.",
    "Confirmar que toda afirmacion sustantiva tenga soporte verificable o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar consistencia entre datos curriculares y portada del documento.",
    "Revisar render de nombres de archivo en README antes de automatizar.",
    "Revisar placeholders de Slug antes de compilar o citar.",
    "Normalizar manualmente salidas de ciclo 1 antes de reutilizacion automatica.",
    "Validar correspondencia del producto con la consigna local."
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
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anomalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico."
  ],
  "bibliography_rules": [
    "Usar historia-del-derecho-en-mexico.bib como repositorio bibliografico local.",
    "Conservar entradas institucionales existentes de UnADM y malla curricular.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Agregar solo fuentes realmente consultadas.",
    "No inventar referencias.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Incluir trazabilidad minima: origen y fecha de consulta cuando aplique.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Corregir placeholders de Slug antes de compilar o citar.",
    "No propagar bibliografia de Filosofia del Derecho sin consulta efectiva.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Compartir solo abstracciones editoriales estables entre materias no equivalentes.",
    "Propagar validacion JSON y normalizacion temprana a materias hermanas.",
    "Reutilizar estructura de cinco ejes con ajuste tematico por asignatura.",
    "Propagar arriba y laterales solo reglas editoriales transversales verificables.",
    "No propagar datos curriculares especificos de esta materia a laterales.",
    "No propagar bibliografia local a otros nodos sin consulta efectiva.",
    "Mantener alerta de salidas no parseables en niveles superiores.",
    "Aplicar normalizacion manual si se detecta salida no estructurada en nodos vecinos.",
    "Evitar regresiones respecto de reglas utiles previas.",
    "Ciclo 1 necesita normalizacion manual si se reutiliza.",
    "Ciclo 2 requiere normalizacion manual si se reutiliza desde memorias previas."
  ],
  "open_questions": [
    "Confirmar fuente operativa definitiva para consolidacion de memoria.",
    "Definir nombre oficial de figura docente en plantillas.",
    "Confirmar si LDE-S1B1 es codigo oficial o codigo local.",
    "Validar acentuacion oficial de Mexico/México segun lineamiento institucional.",
    "Verificar y corregir errores de render en README: eporte y eferencias.",
    "Confirmar si existen consignas locales de actividades para ajustar estructura.",
    "Confirmar rubricas de evaluacion especificas por actividad.",
    "Confirmar fuentes obligatorias por semana.",
    "Confirmar si la subcarpeta referencias-historia-del-derecho-en-mexico contiene materiales consultables.",
    "Confirmar si los placeholders de Slug provienen de generador pendiente o de error de plantilla."
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
        "Fuente curricular: malla-curricular-derecho-unadm.pdf.",
        "Coursecode local: LDE-S1B1 [supuesto hasta confirmacion oficial]."
      ]
    },
    "essence": [
      "Identidad institucional UnADM.",
      "Cinco ejes editoriales.",
      "Problema juridico o social situado.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible.",
      "Integridad academica.",
      "Trazabilidad bibliografica.",
      "Coherencia entre consigna y producto.",
      "Sincronizacion transversal sin traslado tematico indebido."
    ],
    "reason_for_being": [
      "Orientar productos academicos con claridad, fundamento juridico, evidencia y transferencia profesional.",
      "Transformar la planeacion semanal en reportes, presentaciones y productos visuales.",
      "Integrar problema, conceptos, fuentes, analisis propio y cierre argumentativo.",
      "Servir como cerebro editorial persistente de la materia.",
      "Preservar memoria util sin regresiones.",
      "Asegurar que cada actividad sea verificable, estructurada y juridicamente pertinente."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Objetivo puntual antes del desarrollo.",
      "Secciones funcionales y trazables.",
      "Citas explicitas y verificables.",
      "Postura estudiantil argumentada.",
      "Cierre con criterio juridico propio.",
      "Marcado explicito de supuestos.",
      "Lenguaje academico claro.",
      "Metadatos institucionales consistentes.",
      "Evitar transferencia tematica no verificada."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo al inicio.",
      "Delimitar conceptos clave antes del analisis.",
      "Relacionar marco normativo o doctrinal con el problema.",
      "Contrastar evidencia con postura propia.",
      "Evitar resumen sin evaluacion critica.",
      "Cerrar con implicacion practica juridica.",
      "Alinear argumento, fuentes y producto solicitado.",
      "Distinguir hechos, normas, doctrina y criterio personal.",
      "Marcar supuestos cuando falte consigna o fuente local.",
      "Usar estructura de cinco ejes como esqueleto reusable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Historia del Derecho en Mexico",
        "Licenciatura en Derecho UnADM",
        "Identidad institucional UnADM",
        "Cinco ejes editoriales",
        "Problema juridico o social",
        "Conceptos y fuentes",
        "Producto solicitado por planeacion",
        "Analisis propio",
        "Conclusion transferible",
        "Integridad academica",
        "Trazabilidad bibliografica",
        "Normalizacion JSON",
        "Coherencia entre consigna y producto",
        "Plantilla LaTeX local",
        "Bibliografia local",
        "Malla curricular de Derecho",
        "Sincronizacion transversal",
        "Supuestos verificables",
        "No transferencia tematica indebida"
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
          "justification": "La identidad institucional exige fuentes verificables y formato academico."
        },
        {
          "source": "Malla curricular de Derecho",
          "target": "Datos curriculares locales",
          "kind": "supports",
          "justification": "El README declara la malla curricular como fuente de semestre, bloque, tipo y creditos."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Coherencia entre consigna y producto",
          "kind": "supports",
          "justification": "Los ejes ordenan problema, fuentes, producto, analisis y cierre."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay reutilizacion segura aguas abajo."
        },
        {
          "source": "Trazabilidad bibliografica",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La verificabilidad depende de metadatos y fuentes consultables."
        },
        {
          "source": "Plantilla LaTeX local",
          "target": "Metadatos institucionales",
          "kind": "develops",
          "justification": "La plantilla define portada, curso, autor, ubicacion y tabla institucional."
        },
        {
          "source": "Bibliografia local",
          "target": "Trazabilidad bibliografica",
          "kind": "supports",
          "justification": "El archivo .bib conserva entradas institucionales y notas de consulta."
        },
        {
          "source": "Sincronizacion transversal",
          "target": "No transferencia tematica indebida",
          "kind": "depends_on",
          "justification": "Entre materias no equivalentes solo deben viajar abstracciones editoriales."
        },
        {
          "source": "Supuestos verificables",
          "target": "Conservador en inferencias no verificadas",
          "kind": "supports",
          "justification": "Marcar supuestos evita convertir inferencias en hechos."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La postura argumentada debe culminar en criterio juridico aplicable."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 1, bloque 1, obligatoria, 8 creditos.",
        "README local: fuente curricular malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canonico.",
        "README local: identidad UnADM, integridad academica, citas verificables y conclusion juridica.",
        "Programa analitico local: proposito de transformar planeacion en reportes, presentaciones y productos visuales.",
        "Programa analitico local: cinco ejes de trabajo.",
        "Programa analitico local: bibliografia especifica debe agregarse al .bib local.",
        "historia-del-derecho-en-mexico.bib: entrada unadmSitioWeb.",
        "historia-del-derecho-en-mexico.bib: entrada unadmMallaDerecho2024.",
        "Plantilla LaTeX local: documenttitle, documentsubtitle, documentsubject, coursename y coursecode.",
        "Plantilla LaTeX local: alumno Martin Jonathan de la Cruz y matricula ES2611202040.",
        "Plantilla LaTeX local: figura docente por definir.",
        "Memoria previa: hubo salidas no JSON parseables.",
        "Regla transversal: no copiar contenido tematico de Filosofia del Derecho sin evidencia local."
      ]
    },
    "reinforcement_log": [
      "Ciclo 7: se deduplican reglas repetidas sin recortar contenido util.",
      "Ciclo 7: se preserva memoria local verificable de Historia del Derecho en Mexico.",
      "Ciclo 7: se transfiere desde Filosofia del Derecho solo estructura editorial reusable.",
      "Ciclo 7: se bloquea traslado de bibliografia y temas filosoficos no consultados localmente.",
      "Ciclo 7: se refuerza validacion JSON como puerta de propagacion.",
      "Ciclo 7: se mantienen alertas de Codex y GPT-Pro como fuentes provisionales.",
      "Ciclo 7: se consolidan cinco ejes como nucleo transversal.",
      "Ciclo 7: se agregan relaciones conceptuales con tipos permitidos.",
      "Ciclo 7: se marca LDE-S1B1 como supuesto hasta confirmacion oficial.",
      "Ciclo 7: se conserva pregunta abierta sobre acentuacion oficial de Mexico/México."
    ]
  }
}