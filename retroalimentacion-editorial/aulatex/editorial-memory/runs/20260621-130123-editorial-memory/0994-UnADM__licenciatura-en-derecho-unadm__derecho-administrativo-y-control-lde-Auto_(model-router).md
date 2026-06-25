{
  "summary": [
    "Se consolida memoria editorial de materia para Derecho administrativo y control.",
    "Se aplica compresion union-dedupe sin regresion.",
    "Se preserva identidad UnADM y enfoque de Licenciatura en Derecho.",
    "Se mantiene alineacion curricular local: semestre 6, bloque 1, obligatoria, 8 creditos.",
    "Se reutilizan solo abstracciones editoriales estables desde Filosofia del Derecho.",
    "Se evita trasladar doctrina o citas sustantivas no verificadas en el destino.",
    "Se refuerzan ejes transversales: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se conserva alerta institucional sobre salidas no JSON parseables antes de propagar.",
    "Se mantiene necesidad de normalizacion estructurada previa a reutilizacion aguas abajo."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en portada, metadatos y redaccion academica.",
    "Usar nombre exacto de materia: Derecho administrativo y control.",
    "Conservar enfoque de Licenciatura en Derecho en todos los entregables.",
    "Conservar encuadre curricular local: semestre 6, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en la consigna local.",
    "Declarar cuando una regla provenga de fuente provisional.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Fuente provisional: Codex desde ingenieria-en-sistemas-computacionales.",
    "Fuente provisional: GPT-Pro desde Actividad 1."
  ],
  "structure_rules": [
    "Organizar cada producto con problema, conceptos, fuentes, analisis propio y conclusion juridica.",
    "Incluir marco normativo o doctrinal cuando la consigna lo requiera.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear entregables a la planeacion semanal y al programa analitico local.",
    "Explicitar tipo de producto antes de desarrollar: reporte, presentacion o visual.",
    "Transformar la planeacion en el producto solicitado por la consigna.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener consistencia entre README, plantilla .tex y archivo .bib.",
    "Nombrar archivos con slug derecho-administrativo-y-control cuando aplique.",
    "Corregir artefactos de estructura en README antes de publicar indices.",
    "Resolver tokens PowerShell sin expandir en README y programa analitico por el slug literal derecho-administrativo-y-control. [supuesto]",
    "Corregir nombres de archivo con caracteres espurios o saltos de linea en README. [supuesto]"
  ],
  "activity_rules": [
    "Cada actividad debe incluir postura academica propia.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Vincular el tema con control administrativo y practica profesional.",
    "Formular criterio juridico transferible a la practica profesional.",
    "No omitir conclusion final orientada a aplicacion juridica.",
    "Identificar si el producto es reporte, presentacion o visual.",
    "Separar reglas editoriales generales de contenidos sustantivos heredados de otras materias.",
    "No asumir que fuentes de otra materia correspondan a actividades locales."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar respuesta no estructurada antes de aplicar aguas abajo.",
    "Validar estructura minima completa antes de reutilizar memoria.",
    "Detener propagacion si hay campos criticos vacios.",
    "Verificar integridad academica con citas verificables y sin fuentes inventadas.",
    "Confirmar trazabilidad entre afirmaciones y bibliografia local.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Validar que README y programa no conserven placeholders ni rutas corruptas.",
    "Revisar que reglas heredadas no contradigan el programa analitico local.",
    "Verificar que el producto corresponda a la consigna de actividad."
  ],
  "latex_rules": [
    "Mantener plantilla LaTeX en espanol.",
    "Mantener formato letterpaper segun archivo base.",
    "Usar codificacion y acentos correctos en .tex y .bib.",
    "Completar metadatos institucionales y de curso antes de compilar.",
    "Conservar tabla de datos academicos del estudiante y docente en portada.",
    "Asegurar coherencia entre documenttitle, documentsubtitle y actividad real.",
    "Reemplazar Actividad X por numero y nombre real de la actividad.",
    "Mantener coursecode LDE-S6B1 salvo evidencia institucional distinta.",
    "Sustituir Nombre por definir por el nombre oficial de la figura docente antes de entregar.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anomalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico."
  ],
  "bibliography_rules": [
    "Registrar fuentes de cada actividad en derecho-administrativo-y-control.bib.",
    "Priorizar fuentes institucionales UnADM y documentos curriculares locales.",
    "Usar la malla curricular local como fuente de ubicacion curricular.",
    "Conservar entradas base: unadmSitioWeb y unadmMallaDerecho2024.",
    "Agregar fuentes especificas solo si fueron consultadas o proporcionadas.",
    "No inventar fuentes para llenar bibliografia.",
    "No agregar referencias sin evidencia documental.",
    "Usar solo obras realmente consultables.",
    "Conservar metadatos minimos: autor, titulo, anio, medio y nota de consulta.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Validar que toda cita en texto tenga entrada .bib local."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo tras validacion de estructura JSON.",
    "Propagar recursivamente solo reglas editoriales compartibles.",
    "No propagar contenido especifico de actividad a laterales.",
    "No trasladar doctrina de Filosofia del Derecho sin verificacion local.",
    "Aplicar normalizacion manual cuando la fuente sea provisional.",
    "Mantener estrategia union-dedupe lossless en fusiones futuras.",
    "Preservar alerta institucional sobre respuestas no estructuradas en niveles superiores.",
    "Marcar conflictos de nomenclatura entre rutas antes de consolidar. [supuesto]",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Evitar regresiones respecto de reglas utiles previas.",
    "Ciclo 1 necesita normalizacion manual si se reutiliza."
  ],
  "open_questions": [
    "Definir fuente definitiva para reemplazar referencias provisionales Codex y GPT-Pro.",
    "Confirmar nombre oficial de la figura docente en plantilla.",
    "Validar si existe formato institucional obligatorio de citas para la Licenciatura en Derecho.",
    "Confirmar convencion final del archivo de referencias en la materia.",
    "Verificar si el anio de consulta del sitio institucional UnADM debe mantenerse en 2026.",
    "Confirmar si los tokens PowerShell sin expandir en README y programa son artefactos de generacion. [supuesto]",
    "Corregir posibles artefactos de ruta o nombre en listado de estructura del README. [supuesto]",
    "Confirmar fuentes obligatorias por semana o actividad.",
    "Confirmar rubricas especificas de evaluacion por actividad.",
    "Confirmar producto exacto cuando la consigna local no sea visible."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Institucional sin rigidez innecesaria.",
        "Aplicado a la practica profesional.",
        "Conservador ante fuentes no verificadas."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta de materia como entrada canonica.",
        "Normalizacion estructurada antes de propagacion.",
        "Supuestos marcados de forma visible.",
        "No invencion de fuentes.",
        "Respeto del programa analitico local.",
        "Consistencia entre README, LaTeX y bibliografia."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho administrativo y control.",
        "Semestre 6, bloque 1.",
        "Tipo obligatoria.",
        "8 creditos.",
        "Fuente curricular local: malla-curricular-derecho-unadm.pdf.",
        "Coursecode local: LDE-S6B1."
      ]
    },
    "essence": [
      "Identidad UnADM.",
      "Integridad academica.",
      "Problema juridico delimitado.",
      "Conceptos, normas y doctrina pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Control administrativo.",
      "Conclusion juridica transferible.",
      "Practica profesional.",
      "Normalizacion estructurada."
    ],
    "reason_for_being": [
      "Orientar productos academicos con claridad, fundamento juridico y evidencia.",
      "Transformar la planeacion semanal en reportes, presentaciones o productos visuales.",
      "Integrar problema, conceptos, fuentes, analisis propio y cierre argumentativo.",
      "Vincular cada actividad con control administrativo y aplicacion profesional.",
      "Garantizar trazabilidad entre afirmaciones, citas y bibliografia local.",
      "Prevenir propagacion de memoria no estructurada o no verificable."
    ],
    "style_markers": [
      "Abrir con encuadre breve del problema juridico o social.",
      "Declarar objetivo puntual antes del desarrollo.",
      "Separar conceptos, marco normativo o doctrinal, analisis propio y cierre.",
      "Usar citas trazables y verificables.",
      "Marcar supuestos de forma explicita.",
      "Nombrar la materia exactamente como Derecho administrativo y control.",
      "Conservar conclusion practica obligatoria.",
      "Evitar redaccion puramente descriptiva.",
      "Evitar fuentes inventadas.",
      "Mantener coherencia entre metadatos, archivo .tex y .bib."
    ],
    "argumentative_patterns": [
      "Problema juridico -> objetivo -> conceptos -> marco normativo -> analisis -> conclusion.",
      "Consigna -> producto solicitado -> estructura editorial -> entrega verificable.",
      "Afirmacion -> fuente verificable -> cita -> criterio propio.",
      "Norma o doctrina -> aplicacion administrativa -> control -> consecuencia practica.",
      "Dato no visible -> marca [supuesto] -> confirmacion pendiente.",
      "Fuente heredada -> provisionalidad -> verificacion local.",
      "README local -> plantilla LaTeX -> bibliografia -> compilacion sin roturas.",
      "Planeacion semanal -> reporte, presentacion o visual segun corresponda."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Licenciatura en Derecho",
        "Derecho administrativo y control",
        "Semestre 6 bloque 1",
        "Obligatoria 8 creditos",
        "Problema juridico",
        "Conceptos juridicos",
        "Marco normativo",
        "Doctrina verificable",
        "Evidencia",
        "Analisis propio",
        "Postura academica",
        "Conclusion transferible",
        "Practica profesional",
        "Control administrativo",
        "Integridad academica",
        "Bibliografia local",
        "Malla curricular",
        "Normalizacion estructurada",
        "JSON parseable",
        "README local",
        "Programa analitico local",
        "Plantilla LaTeX",
        "Archivo BibTeX local",
        "Fuentes provisionales"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta local exige identidad institucional, citas verificables y criterio propio."
        },
        {
          "source": "Malla curricular",
          "target": "Semestre 6 bloque 1",
          "kind": "supports",
          "justification": "El README local declara la ubicacion curricular con fuente en la malla."
        },
        {
          "source": "Malla curricular",
          "target": "Obligatoria 8 creditos",
          "kind": "supports",
          "justification": "El README local registra tipo obligatoria y 8 creditos."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere un problema delimitado para evitar resumen descriptivo."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion practica debe derivar de fundamentos juridicos verificables."
        },
        {
          "source": "Control administrativo",
          "target": "Practica profesional",
          "kind": "develops",
          "justification": "La materia orienta los productos hacia aplicacion juridica en administracion y control."
        },
        {
          "source": "Bibliografia local",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La trazabilidad entre citas y .bib evita fuentes inventadas."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "JSON parseable",
          "kind": "depends_on",
          "justification": "La propagacion solo procede con estructura valida y reutilizable."
        },
        {
          "source": "Fuentes provisionales",
          "target": "Verificacion local",
          "kind": "depends_on",
          "justification": "Las reglas heredadas no verificadas deben confirmarse antes de consolidarse como definitivas."
        },
        {
          "source": "README local",
          "target": "Plantilla LaTeX",
          "kind": "supports",
          "justification": "Los nombres y metadatos del README deben coincidir con los artefactos compilables."
        },
        {
          "source": "Archivo BibTeX local",
          "target": "Plantilla LaTeX",
          "kind": "supports",
          "justification": "Las citas del documento deben resolverse contra derecho-administrativo-y-control.bib."
        },
        {
          "source": "Programa analitico local",
          "target": "Estructura editorial",
          "kind": "develops",
          "justification": "El programa fija los ejes: problema, conceptos, fuentes, analisis propio y cierre."
        }
      ],
      "evidence": [
        "README local: Materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 6, bloque 1, obligatoria, 8 creditos.",
        "README local: fuente curricular UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canonico.",
        "README local: identidad UnADM, integridad academica, citas verificables y conclusion juridica.",
        "Programa analitico local: productos academicos con claridad, fundamento juridico, evidencia y transferencia profesional.",
        "Programa analitico local: reportes, presentaciones y productos visuales.",
        "Programa analitico local: ejes de problema, conceptos, fuentes, analisis propio y cierre argumentativo.",
        "Bibliografia local: unadmSitioWeb.",
        "Bibliografia local: unadmMallaDerecho2024.",
        "Memoria institucional heredada: salida sin JSON parseable desde Codex para UnADM.",
        "Memoria transversal: bloquear propagacion si la salida no es JSON parseable.",
        "Memoria transversal: no inventar fuentes.",
        "Memoria transversal: validar consistencia entre citas en texto y archivo .bib."
      ]
    },
    "reinforcement_log": [
      "Ciclo 7 sincroniza transversalmente desde actividad de Filosofia del Derecho hacia materia no equivalente.",
      "Se conservaron solo abstracciones editoriales estables.",
      "Se excluyo doctrina especifica de Filosofia del Derecho por falta de verificacion local.",
      "Se reforzo estructura reusable: problema, conceptos, marco, analisis y conclusion.",
      "Se reforzo gate institucional de JSON parseable.",
      "Se reforzo control de fuentes verificables y bibliografia local.",
      "Se preservo alineacion curricular local de Derecho administrativo y control.",
      "Se mantuvieron alertas por fuentes provisionales Codex y GPT-Pro.",
      "Se agrego relacion conceptual entre control administrativo y practica profesional.",
      "Se mantuvo estrategia progresiva y conservadora sin regresion."
    ]
  }
}